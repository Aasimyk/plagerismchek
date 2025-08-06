from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ch import run_plagiarism_check

app = FastAPI()

#settings for frontend-backend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContentRequest(BaseModel):
    content: str

@app.post("/check")
async def check_plagiarism(request: ContentRequest):
    result = run_plagiarism_check(request.content)
    highlighted = ""

    for item in result["results"]:
        if item["highlight"]:
            highlighted += f'<span class="highlight">{item["sentence"]}</span> '
        else:
            highlighted += f'{item["sentence"]} '

    all_sources = set()
    for item in result["results"]:
        all_sources.update(item["sources"])

    return {
        "highlighted": highlighted.strip(),
        "plagiarism_score": result["final_percentage"],
        "sentence_scores": [r["score"] for r in result["results"]],
        "sources": list(all_sources)
    }
