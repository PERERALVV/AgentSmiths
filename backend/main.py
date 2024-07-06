from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
# from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_PATH = './workspace/static/'

# app.mount("/static", StaticFiles(directory=BASE_PATH), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get-html-files", response_class=JSONResponse)
async def get_html_files():
    html_files = sorted(
        [f for f in os.listdir(BASE_PATH) if f.endswith('.html')])
    return {"files": html_files}


@app.get("/get-html-css/{filename}", response_class=JSONResponse)
async def get_html_css(filename: str):
    html_file_path = os.path.join(BASE_PATH, filename)
    css_file_path = os.path.join(BASE_PATH, filename.replace('.html', '.css'))

    if not os.path.exists(html_file_path):
        return JSONResponse(content={'error': 'HTML file not found'}, status_code=404)

    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    css_content = ""
    if os.path.exists(css_file_path):
        with open(css_file_path, 'r', encoding='utf-8') as file:
            css_content = file.read()

    return JSONResponse(content={'html': html_content, 'css': css_content})


@app.post("/save-html")
async def save_html(request: Request):
    data = await request.json()
    filename = data.get('filename')
    html_content = data.get('html')

    if not filename or not html_content:
        raise HTTPException(
            status_code=400, detail="Filename and HTML content are required")

    css_filename = filename.replace('.html', '.css')
    html_with_css_link = f'<link rel="stylesheet" href="{css_filename}">\n{html_content}'

    html_file_path = os.path.join(BASE_PATH, filename)
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_with_css_link)

    return {"message": "HTML content saved successfully"}


@app.post("/save-css")
async def save_css(request: Request):
    data = await request.json()
    filename = data.get('filename')
    css_content = data.get('css')

    if not filename or not css_content:
        raise HTTPException(
            status_code=400, detail="Filename and CSS content are required")

    css_file_path = os.path.join(BASE_PATH, filename)
    with open(css_file_path, 'w', encoding='utf-8') as file:
        file.write(css_content)

    return {"message": "CSS content saved successfully"}
