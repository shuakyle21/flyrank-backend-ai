# FlyRank AI — Backend AI Engineering Internship

Hands-on tasks from my Backend AI Engineering internship at FlyRank — FastAPI, SQLite, Postgres, Docker, Supabase Auth, and ethical scraping, one task per folder.

> This repository contains only my personal learning work. It does not contain FlyRank proprietary systems, credentials, or client code. Consolidated from standalone repos via clean copy (no history).

## Portfolio at a Glance

| Project | Focus | Core Technologies | Evidence |
| --- | --- | --- | --- |
| [BE-01 — First CRUD API](backend-engineering/be-01) | HTTP and API fundamentals | Python, FastAPI, Uvicorn | In-memory CRUD, 7 endpoints, Swagger UI |
| [BE-02 — Database-Backed CRUD](backend-engineering/be-02) | Persistence and SQL | FastAPI, SQLite, DB Browser | Full CRUD, restart persistence, database view |
| [BE-03 — Auth: Login and Protect](backend-engineering/be-03) | Authentication and route security | Supabase Auth, JWT, HTTPBearer | Signup/login/logout, protected routes, token-invalidation notes |
| [BE-04 — Containerized Stack](backend-engineering/be-04) | Architecture and infrastructure | PostgreSQL, Docker Compose, psycopg2 | App + DB containers, healthcheck, named volume, `.env` setup |
| [BE-05 — The Polite Scraper](backend-engineering/be-05) | Ethical data collection | Python, Pydantic, requests, pytest | Cache-aware pipeline, Pydantic validation, mocked tests |

Sources: [Week2_Assignment_CRUDApi](https://github.com/shuakyle21/Week2_Assignment_CRUDApi) → BE-01 · [Week3_Assignment_TasksDB](https://github.com/shuakyle21/Week3_Assignment_TasksDB) @ SQLite stage → BE-02 · [Week4_Auth_and_Login](https://github.com/shuakyle21/Week4_Auth_and_Login) → BE-03 · [Week3_Assignment_TasksDB](https://github.com/shuakyle21/Week3_Assignment_TasksDB) @ HEAD → BE-04 · [the-polite-scraper](https://github.com/shuakyle21/the-polite-scraper) → BE-05.

## Engineering Progression

```
BE-01 (in-memory CRUD) --> BE-02 (SQLite) --> BE-03 (Supabase JWT auth) --> BE-04 (Postgres + Docker) --> BE-05 (scraping pipeline)
```

Each project adds one production-oriented backend concern while keeping API contracts explicit and testable.

## Skills Demonstrated

| Area | Practices |
| --- | --- |
| API development | REST-style routes, JSON contracts, validation, HTTP status codes, Swagger UI |
| Data | Parameterized SQL, schema init + seed, SQLite, PostgreSQL, persistence |
| Security | Env-based secrets, Supabase Auth, Bearer-token protection, JWT expiry awareness |
| Architecture | Route/service separation, cache-aware pipeline, stage-based evolution |
| Quality | Mocked pytest suite (BE-05), clean-clone setup, per-project READMEs |
| Operations | Dockerfile, Compose orchestration, healthchecks, `.env.example` templates, volumes |

## Repository Map

```
flyrank-backend-ai/
├── backend-engineering/
│   ├── be-01/    First FastAPI task CRUD (in-memory)
│   ├── be-02/    SQLite-backed task CRUD API
│   ├── be-03/    Supabase authentication and protected routes
│   ├── be-04/    PostgreSQL service orchestrated with Docker Compose
│   └── be-05/    Polite book-catalogue scraper (src/ + tests/)
├── assets/       Screenshots consolidated from source repos
├── devlog.md     Weekly progress log
```

Every project is self-contained and has its own README with setup instructions and API reference.

## Running a Project

Open the README inside the project you want to run:

- BE-01 / BE-02: `pip install -r requirements.txt` then `uvicorn main:app --reload`
- BE-03: copy `.env.example` → `.env` (Supabase keys), then `uvicorn app:app --reload`
- BE-04: copy `.env.example` → `.env`, then `docker compose up`
- BE-05: `uv sync` then `uv run polite-scraper --pages 3`; tests with `uv run pytest`

## Related Repositories

- [the-polite-scraper](https://github.com/shuakyle21/the-polite-scraper) — standalone upstream of BE-05
- [Week3_Assignment_TasksDB](https://github.com/shuakyle21/Week3_Assignment_TasksDB) — full evolution history (SQLite → Postgres)

## Author

**Joshua Klyne Pudadera**
Backend AI Intern @ FlyRank AI · [Portfolio](https://shua-kyle.me) · [LinkedIn](https://www.linkedin.com/in/joshua-klyne-pudadera-b76b73368/)
