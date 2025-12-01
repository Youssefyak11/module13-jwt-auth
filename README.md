# Module 13 - JWT Login/Registration with Playwright E2E

This project implements JWT-based authentication using FastAPI, with simple frontend pages
for registration and login, Playwright end-to-end tests, and a GitHub Actions CI pipeline
that runs tests and builds/pushes a Docker image.

## Running locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open:

- http://localhost:8000/static/register.html
- http://localhost:8000/static/login.html

## Running Playwright E2E tests

```bash
pip install pytest-playwright
playwright install
pytest tests/e2e
```

## Docker

Build and run:

```bash
docker build -t youssefyak11/module13-jwt-auth .
docker run -p 8000:8000 youssefyak11/module13-jwt-auth
```

Then visit the same `/static` URLs as above.

## CI/CD

The GitHub Actions workflow (`.github/workflows/ci.yml`) will:

- Start PostgreSQL
- Start the FastAPI app
- Run Playwright tests
- Build & push a Docker image to Docker Hub if tests pass

Make sure to set the following repository secrets:

- `SECRET_KEY`
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
