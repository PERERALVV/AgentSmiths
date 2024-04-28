# import src
from uvicorn import run
from src.routes.api import asgi_app

if __name__ == "__main__":
    run("src.routes.api:asgi_app", port=8000, reload=True)