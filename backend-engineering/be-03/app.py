import os
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
bearer_scheme = HTTPBearer(auto_error=False)

app = FastAPI(title="Auth API")

supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_PUBLISHABLE_KEY")
)

def get_access_token(creds: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if creds is None or not creds.credentials:
        raise HTTPException(status_code=401, detail={"error":"Access token required"})

    token = creds.credentials

    try:
      response = supabase.auth.get_user(token)
    except Exception:
      raise HTTPException(status_code=401, detail={"error": "Invalid or expired access token"})
    
    if response.user is None:
      raise HTTPException(status_code=401, detail={"error": "Invalid or expired access token"})
    
    return {"email": response.user.email, "token": token}



@app.get('/')
def home():
    return {"message": "Auth API is running. Use /auth/signup or /auth/login."}


@app.get('/login')
def login_info(supabase: Client = Depends(lambda: supabase)):
    response = supabase.auth.refresh_session()
    return {"message": "Use POST /auth/login with email and password.", "session": response.session}


@app.get('/signup')
def signup_info():
    return {"message": "Use POST /auth/signup with email and password."}


@app.post('/auth/signup', status_code=201)
def signup(payload: dict):
    email = payload.get("email")
    password = payload.get("password")

    if email is None or password is None:
        raise HTTPException(status_code=400, detail="Email and password are required.")

    response = supabase.auth.sign_up(
        {
            "email": email,
            "password": password,
        }
    )
    return {"user": response.user, "session": response.session}


@app.post('/auth/login', status_code=200)
def login(payload: dict):
    email = payload.get("email")
    password = payload.get("password")

    if email is None or password is None:
        raise HTTPException(status_code=400, detail="Email and password are required.")

    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password,
        })
    except Exception as e:
        raise HTTPException(status_code=401, detail={"error": str(e)})



    return {"user": response.user, "session": response.session}

@app.get('/public/info')
def public_info():
    return {"message": "This is public information."}

@app.get('/protected/info')
def protected_info(creds=Depends(get_access_token)):
    return {"message": "This is protected information.", "user": creds["email"], "token": creds["token"]}

    
@app.post('/auth/logout', status_code=204)
def logout(creds=Depends(get_access_token)):
    return
    
@app.get('/protected/profile')
def protected_profile(creds=Depends(get_access_token)):
    return {"message": "This is protected information.", "user": creds["email"]}

# Second protected route example
@app.get('/protected/dashboard')
def protected_dashboard(creds=Depends(get_access_token)):
    return {"message": "Welcome to the protected dashboard.", "user": creds["email"]}

#Challenge: Refresh token route
@app.post('/auth/refresh', status_code=200)
def refresh(payload: dict):
    refresh_new_token = payload.get("refresh_token")
    if refresh_new_token is None:
        raise HTTPException(status_code=400, detail="Refresh token is required.")
    
    try:
        response = supabase.auth.refresh_session(refresh_new_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail={"error": str(e)})

    return {"session": response.session}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
