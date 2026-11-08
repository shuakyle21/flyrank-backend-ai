# Job application email classifier

`POST /classify` takes an email you received about a job application and returns a small JSON object: which stage the application is at, the company, the job title, and how far along the process it is (1–5).

Stage 1 status: the endpoint, input validation and stub mode work. The model is not wired yet.

## Try it

Start the server in stub mode (no model calls):

```
LLM_STUB=1 uvicorn main:app --port 8000
```

Valid request, returns 200:

```
curl -s -w ' HTTP %{http_code}\n' -X POST http://127.0.0.1:8000/classify \
  -H 'Content-Type: application/json' \
  -d '{"subject":"Application received","raw_text":"Thanks for applying","from_address":"jobs@example.com","known_from_rules":{"company":"Acme","job_title":"Backend Engineer"}}'
```

Response:

```
{"status":null,"company":null,"job_title":null,"max_stage":1} HTTP 200
```

Broken request (missing `subject`), returns 400 naming the field:

```
curl -s -w ' HTTP %{http_code}\n' -X POST http://127.0.0.1:8000/classify \
  -H 'Content-Type: application/json' \
  -d '{"raw_text":"x","from_address":"a@b.c"}'
```

Response:

```
{"detail":"invalid request body","errors":[{"field":"subject","message":"Field required"}]} HTTP 400
```

## Configuration

Copy the names from `.env.example` into `.env` and fill in the values. The app reads:

- `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL`: required at startup, even in stub mode
- `LLM_STUB`: `1` (default) returns a fixed answer without calling a model; `0` returns 503 until the model is wired

`.env` is git-ignored.
