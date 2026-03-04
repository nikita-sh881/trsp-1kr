from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List
import models 

app = FastAPI()

current_user = models.User(name="Nikita", id=1)

feedback_storage: List[models.Feedback] = []

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content

@app.get("/users")
async def get_user():
    return current_user

@app.post("/feedback")
async def create_feedback(feedback: models.Feedback):
    feedback_storage.append(feedback)
    return {
        "message": f"Feedback received. Thank you, {feedback.name}."
    }

@app.get("/feedback")
async def get_all_feedback():
    return feedback_storage