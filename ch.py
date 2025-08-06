import re
import time
import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")
SERPAPI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def split_into_sentences(text):
    text = re.sub(r'\s+', ' ', text.strip())
    return re.split(r'(?<=[.!?]) +', text)

def get_web_sources(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "engine": "google",
        "num": 3,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = []

        for result in data.get("organic_results", []):
            snippet = result.get("snippet", "")
            link = result.get("link", "")
            if snippet and link:
                results.append((snippet, link))

        time.sleep(1)
        return results
    except Exception as e:
        print(f"Error fetching sources: {e}")
        return []

def check_sentence_plagiarism(sentence):
    .
    .
    .
    .
    .

    return max_score * 100, list(set(matching_links))

def run_plagiarism_check(text, threshold=60):
    .
    .
    .
    .
    .
    final_percentage = (total_score / count) if count > 0 else 0.0

    return {
        "results": results,
        "final_percentage": final_percentage
    }            
