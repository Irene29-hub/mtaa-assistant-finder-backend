# MTAA Assistant Backend

A Flask-based backend for the MTAA Assistant application with job marketplace functionality.

## Features

- RESTful API endpoints for jobs, users, and quotes
- SQLAlchemy ORM with SQLite/PostgreSQL
- Database migrations with Flask-Migrate
- CORS support for frontend integration
- OpenAI integration for AI responses
- Production-ready with Gunicorn

## Complete Setup Guide

### 1. Python Environment Setup
```bash
# Install pyenv (if not already installed)
curl https://pyenv.run | bash

# Install Python 3.8+
pyenv install 3.8.13
pyenv local 3.8.13

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create `.env` file in project root:
```
DATABASE_URL=sqlite:///mtaa_fundi.db
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### 4. Database Setup
```bash
# Initialize migrations (first time only)
flask db init

# Create migration
flask db migrate -m "Add job marketplace models"

# Apply migrations
flask db upgrade
```

### 5. Run Application
```bash
# Development server
flask run

# Or directly
python app.py
```

Server runs on http://localhost:5000

## API Endpoints

### Job Management
- `GET /api/v1/jobs` - Get all jobs (with optional status filter)
- `POST /api/v1/jobs` - Create a new job
- `DELETE /api/v1/jobs/<id>` - Delete a job

### User Management
- `GET /api/v1/users` - Get users (with optional role/phone filter)
- `POST /api/v1/users` - Create a new user

### Quote Management
- `POST /api/v1/quotes` - Submit a quote for a job

### AI Assistant
- `POST /api/conversations` - Create a new conversation
- `GET /api/conversations/<id>/messages` - Get messages
- `POST /api/conversations/<id>/message` - Send a message

### Health Check
- `GET /api/health` - Health check endpoint

## Frontend Integration

The backend is configured with CORS to work with the React frontend running on port 3000.

## Deployment

Configured for deployment on Render.com with the included `render.yaml` configuration.