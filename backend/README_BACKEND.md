MTAA Assistant Backend README
-----------------------------
1. Set env vars:
   - DATABASE_URL (postgres URL)
   - OPENAI_API_KEY
   - SECRET_KEY

2. Local dev:
   pip install -r requirements.txt
   export FLASK_APP=app.py
   flask db init
   flask db migrate -m "init"
   flask db upgrade
   flask run

3. Deploy to Render:
   - Create managed Postgres.
   - Create Web Service pointing to repo backend/Dockerfile.
   - Add env vars on Render (DATABASE_URL, OPENAI_API_KEY, SECRET_KEY).
