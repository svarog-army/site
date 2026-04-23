# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Stack

- **Flask** (web app) + **FastAPI** (REST API), both backed by PostgreSQL
- **SQLAlchemy** via `alchemical`, migrations via **Flask-Migrate** (Alembic)
- **Pydantic v2** + `pydantic-settings` for config and API schemas
- **Flask-Babel** for i18n (default locale `uk`, also `en`)
- **Signal bot** integration via `signalbot`
- Frontend: **TypeScript** + **Tailwind CSS v3** + **Flowbite**, bundled with **Webpack**
- Python package manager: **uv**; JS: **npm**

## Setup

```bash
uv sync                        # install Python deps
npm install                    # install JS deps
cp project.env .env            # then fill in secrets in .env
docker compose up -d db        # start Postgres
uv run flask db upgrade        # apply migrations
uv run flask create-admin      # create super-admin account
uv run flask create-specialties
uv run flask fill-custom-links
```

## Running Locally

```bash
# Flask web app
uv run flask run

# FastAPI (separate port)
uv run uvicorn api:app --reload --port 8002

# Frontend (in separate terminals)
npm run css-watch
npm run js-watch

# Or build once
npm run build
```

## Tests

```bash
uv run pytest                  # all tests (test_flask/ + test_api/)
uv run pytest test_flask/      # Flask tests only
uv run pytest test_api/        # API tests only
uv run pytest test_flask/test_auth.py  # single file
```

Tests use an in-memory SQLite DB via `test_flask/test.env`. The `client` fixture calls `db.drop_all()` / `db.create_all()` around each test.

## Linting & Type Checking

```bash
uv run ruff check .
uv run ruff format .
uv run mypy
```

## Architecture

### Flask app (`svarog/`)

- `__init__.py` — app factory `create_app()`, registers all blueprints
- `models/` — SQLAlchemy models: `User`, `Application`, `Recruit`, `Specialty`, `RecruitStatusChangeEvent`, `DayStats`, `CustomLink`
- `views/` — blueprints: `auth`, `main`, `application`, `admin`, `recruit`, `specialty`, `stats`, `multilingual` (language-prefixed routes)
- `controllers/` — business logic used by views: `stats`, `recruit`, `pagination`, `custom_links`, `signal_bot`
- `forms/` — WTForms form classes
- `schema/` — Pydantic schemas shared between Flask and API
- `templates/` — Jinja2 HTML templates
- `commands/` — Flask CLI commands (`create-admin`, `create-specialties`, `fill-custom-links`, `fill-recruits`, `fill-stats`, `db-populate`)

The `multilingual` blueprint prefixes all main routes with `/<lang_code>` (e.g. `/uk/`, `/en/`). The root `/` redirects to the locale-prefixed index.

### FastAPI app (`api/`)

- `__init__.py` — FastAPI app factory, mounts router
- `routes/` — endpoints: `auth` (JWT login), `user`
- `dependency/` — FastAPI `Depends` helpers (DB session, current user)
- `oauth2.py` — JWT token creation/validation with `python-jose`

### Frontend (`src/`)

TypeScript files compiled by Webpack to `svarog/static/`. Tailwind input at `src/styles.css`, output at `svarog/static/css/styles.css`.

### Config

`config.py` uses `pydantic-settings`. Env files loaded in priority order: `project.env` → `.env.dev` → `.env`. `APP_ENV` selects `DevelopmentConfig | TestingConfig | ProductionConfig`. `PARKING=True` enables under-construction mode.

## Translations (i18n)

Templates use `{{ _("text") }}`. Workflow:

```bash
./translate-update.sh    # extract new strings → messages.pot, merge into .po files
./translate-compile.sh   # compile .po → .mo
```

Edit `translations/<lang>/LC_MESSAGES/messages.po`, remove `#, fuzzy` lines after verifying translations, then recompile.

## Flask CLI Commands

| Command | Purpose |
|---|---|
| `flask db upgrade` | Apply migrations |
| `flask create-admin` | Create super-admin from env config |
| `flask create-specialties` | Seed specialty table |
| `flask fill-custom-links` | Seed custom links from env config |
| `flask fill-recruits --count N` | Seed dummy recruits |
| `flask fill-stats --count N` | Seed dummy day stats |
| `flask db-populate --count N` | Seed dummy users (dev only) |
