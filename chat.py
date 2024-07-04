from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
import json
import requests

app = FastAPI(debug=True)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to allow only specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

class Itemexample(BaseModel):
    name: str
    prompt: str
    instruction: str
    is_offer: Union[bool, None] = None

class Item(BaseModel):
    model: str
    prompt: str

urls = ["http://localhost:11434/api/generate"]

headers = {
    "Content-Type": "application/json"
}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat/{llms_name}")
def update_item(llms_name: str, item: Item):
    if llms_name == "llama3":
        url = urls[0]
        payload = {
            "model": "llama3",
            "prompt": item.prompt,
            "stream": False
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise exception for non-2xx status codes
            return {"data": response.json(), "llms_name": llms_name}
        except requests.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Error calling external API: {e}")
    else:
        raise HTTPException(status_code=404, detail=f"LLMS {llms_name} not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
