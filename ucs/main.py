from fastapi import FastAPI
from ucs.api.create_project.routes import router as project_router

app = FastAPI(title="Backend monolith")

app.include_router(project_router)


"""
curl -X POST http://localhost:8000/create-project/ \
  -H "Content-Type: application/json" \
  -d '{
        "title": "Мой первый стартап",
        "subtitle": "Мы меняем мир",
        "description": "Короткое описание проекта…",
        "category_id": 3,
        "stage_id": 1,
        "invest_amount": 0,
        "members": [
          { "email": "founder@example.com", "function": "Founder & CEO" },
          { "email": "dev@example.com",     "function": "Backend Developer" }
        ],
        "links": [
          { "title": "Landing", "url": "https://project.example.com" },
          { "title": "GitHub",  "url": "https://github.com/org/repo" }
        ],
        "documents": [
          { "filename": "pitch_deck.pdf" },
          { "filename": "logo.png" }
        ]
      }'
"""