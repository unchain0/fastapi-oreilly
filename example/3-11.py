from fastapi.responses import PlainTextResponse
from fastapi import FastAPI

app = FastAPI()


@app.get("/hi/{who}", response_class=PlainTextResponse)
def greet(who: str) -> str:
    return f"Hello? {who}?"


if __name__ == "__main__":
    import uvicorn
    from pathlib import Path

    uvicorn.run(f"{Path(__file__).stem}:app", reload=True, port=3030)
