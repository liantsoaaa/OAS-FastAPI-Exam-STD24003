from fastapi import FastAPI, Response #type: ignore
from fastapi.responses import PlainTextResponse # type: ignore

app = FastAPI()

@app.get("/ping", response_class=PlainTextResponse)
async def ping():
    return Response(content="pong", media_type="text/plain", status_code=200)