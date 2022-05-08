from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/about")
def about():
    return {"about": "About Data"}