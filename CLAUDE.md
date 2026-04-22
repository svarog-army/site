# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Python (managed with `uv`)

```bash
uv sync                          # install dependencies
uv run flask run                 # Flask dev server (reads .flaskenv)
uv run uvicorn api:app --reload  # FastAPI dev server
flask db upgrade                 # apply migrations
flask db migrate -m "message"   # generate migration
uv run pytest                    # all tests
uv run pytest test_flask/        # Flask tests only
uv run pytest test_api/          # API tests only
uv run pytest test_flask/test_auth.py::test_name  # single test
uv run ruff check .              # lint
uv run mypy                      # type check
```

### Frontend (TypeScript + Tailwind)
```bash
npm run css-watch    # Tailwind watch
npm run js-watch     # Webpack watch
npm run build        # prod build (css + js)
```

### i18n
```bash
./translate-update.sh   # extract strings → messages.pot, update .po files
./translate-compile.sh  # compile .po → .mo (must run after editing .po)
```
After editing `translations/*/LC_MESSAGES/messages.po`, remove `#, fuzzy` lines or translations won't apply.

### Docker
```bash
docker compose up -d db     # start PostgreSQL only (for local dev)
docker compose up           # full stack (db + app + signal bot)
```

## Architecture

**Dual-app structure** — Flask and FastAPI share the same database and config but run as separate processes.

- `svarog/` — Flask app (web UI)
- `api/` — FastAPI app (REST API, JWT auth)
- `src/` — TypeScript source → compiled to `svarog/static/js/` via Webpack
- `config.py` — Pydantic settings loaded from `project.env`, `.env.dev`, `.env`; `APP_ENV` selects development/testing/production

### Flask blueprints (`svarog/views/`)
All public-facing routes live under the `multilingual` blueprint with URL prefix `/<lang_code>/` (supported: `uk`, `en`). The root `/` redirects to `/<detected_lang>/`. Other blueprints:
- `auth` — login/logout
- `admin` — admin panel (login-protected)
- `application` — volunteer application form submission
- `recruit` — recruiter-facing views
- `specialty` — specialty management
- `stats` — public statistics page

### Models (`svarog/models/`)
`User`, `Application`, `Recruit`, `Specialty`, `DayStats`, `CustomLink`, `RecruitStatusChangeEvent`. All accessed via `svarog.db` (alchemical/SQLAlchemy session).

### Frontend bundles (`src/` → `svarog/static/js/`)
Each `.ts` file compiles to a separate JS bundle: `base`, `cookies`, `landing`, `recruit`, `admin`, `stats`, `phone-formatting`, `redirect`.

### Signal bot
Runs as a Docker sidecar (`bbernhard/signal-cli-rest-api`). Config lives in `signal-cli-config/`. Used to send notifications via Signal messenger. See README.md for setup instructions.

### Config & env
`config.py` reads env vars via pydantic-settings. For local dev, copy `project.env` values or create `.env`. `PARKING=true` enables under-construction mode site-wide. `ROBOTS_DISALLOW` controls robots.txt. Custom social/external links (`LINK_*`) are stored in `CustomLink` model and injected via `get_custom_links()` controller into every request via `g.custom_links`.
