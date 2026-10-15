# Devlog — FlyRank Backend AI Internship

Consolidated from standalone repos. Dates reflect source repo activity.

| Week | Assignment | Status | Source |
| --- | --- | --- | --- |
| 2 | BE-01 — Build task CRUD API (in-memory list, FastAPI, Swagger, AI-vs-me reflection) | Complete | Week2_Assignment_CRUDApi |
| 3a | BE-02 — Connect CRUD to SQLite (parameterized SQL, seed data, DB Browser inspection) | Complete | Week3_Assignment_TasksDB @ `dded237` |
| 4 | BE-03 — Auth: login and protect (Supabase signup/login/logout, Bearer guard, JWT-expiry notes) | Complete | Week4_Auth_and_Login |
| 3b | BE-04 — Containerize stack (Postgres 16, Dockerfile, Compose healthcheck, named volume, `.env` setup) | Complete | Week3_Assignment_TasksDB @ HEAD |
| 5 | BE-05 — The polite scraper (cache-aware fetch, paginated discovery, Pydantic validation, mocked pytest) | Complete | the-polite-scraper |

## Notes

- BE-02 and BE-04 share one upstream repo; BE-02 is pinned to the last SQLite-only commit (`dded237 Stage 5: database documentation`), BE-04 tracks HEAD (Postgres + Docker).
- No `ai-fluency/` or capstone agent yet — to be added when those tracks are complete.
- Secrets were never committed: each backend requiring credentials ships only a `.env.example`; real `.env` files are gitignored.
