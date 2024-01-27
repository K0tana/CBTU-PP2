import mimetypes
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/")
def root():
    data = "Hello METANIT.COM"
    return Response(content=data, media_type="text/plain")


@app.get("/about")
def about():
    return HTMLResponse(content="<h2>Sup my homie</h2>")
@app.get("/about/legs")
def leg():
    return FileResponse("publick/index.html", filename="vilka.html", media_type="application/octet-stream")