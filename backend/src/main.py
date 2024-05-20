import uvicorn
from uvicorn import run

from fastapi import FastAPI
from routes.api import sio_app
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount('/',app=sio_app)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__=='__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=80,reload=True)