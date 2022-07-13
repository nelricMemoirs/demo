from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from main_app import dash_app
import uvicorn



app = FastAPI()
app.mount("/dashboard", WSGIMiddleware(dash_app.server))

@app.get('/')
def index():
    return "Hello"