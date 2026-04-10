from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Action(BaseModel):
    action: str

@app.get("/")
def main():
    return {"message": "OpenEnv server running"}

@app.post("/reset")
def reset():
    return {"task": "Classify: Win money now!!!"}

@app.post("/step")
def step(action: Action):
    reward = 1.0 if action.action.lower() == "spam" else 0.0

    return {
        "observation": "done",
        "reward": reward,
        "done": True,
        "info": {}
    }
