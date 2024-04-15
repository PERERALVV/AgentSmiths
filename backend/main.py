import uvicorn
from fastapi import FastAPI
from sockets import sio_app
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount('/',app=sio_app)

# Specify the origins - or else won't have permission
# origins = ["http://localhost:3000"]

# Add middleware
app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def home():
    return {'message':'Hello Developers!'}

if __name__=='__main__':
    uvicorn.run('main:app',reload=True)