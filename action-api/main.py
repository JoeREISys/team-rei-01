from fastapi import FastAPI, HTTPException, Request
from openai import OpenAI, ChatCompletion
from pydantic import BaseModel
import os

app = FastAPI()

class Query(BaseModel):
    query: str

# Initialize OpenAI client
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_api_key)

@app.post("/retrieve")
async def retrieve(query: Query):
    try:
        # This is where you'd add any specific business logic
        # For now, it simply forwards the query to OpenAI's ChatGPT
        response = openai_client.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query.query}]
        )
        # Extract and return the relevant part of the response
        chat_response = response.choices[0].message['content']
        return {"response": chat_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
