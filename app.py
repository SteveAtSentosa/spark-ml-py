from typing import Dict
from fastapi import FastAPI, HTTPException
from services.summary_topics_generator import daily_digest_llm

app = FastAPI()


@app.post("/daily-digest", response_model=Dict)
def daily_digest(user_id: str):
    try:
        result = daily_digest_llm(user_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9001)
