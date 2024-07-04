Ollama ChatBot API
==================

This API provides endpoints to interact with the Ollama chatbot using the Llama3 model. It allows you to send prompts and receive responses from the chatbot.

Installation
------------

### Installing Dependencies
    
    pip install fastapi  
    pip install requests  
    pip install uvicorn 

### Running the FastAPI Application

To run the FastAPI application locally:

    uvicorn main:app --reload

This command starts the FastAPI application on http://localhost:8000 by default.

API Endpoints
-------------

### /

*   **GET**: Returns a simple "Hello World" message to verify the API is running.
    

### /chat/{llms\_name}

*   **POST**: Sends a prompt to the specified LLMs (Language Model) endpoint (llama3 in this case) and retrieves the response.
    

#### Request Body (Item model):
    
    {
    "model": "llama3",
    "prompt": "Your prompt text here"
    }

#### Response:
    
    {
    "data": { 
        "response": "Response from the Llama3 model"
        },
    "llms_name": "llama3"  
    }

### CORS Configuration

*   The API is configured with CORS middleware to allow requests from any origin (\*). Modify allow\_origins in main.py to restrict access to specific origins if needed.
    

Usage Example
-------------

### Sending a Request

You can send a POST request to /chat/llama3 with a JSON body containing the model and prompt:
       
       curl -X 'POST' \    'http://localhost:8000/chat/llama3' \    -H 'Content-Type: application/json' \    -d '{    "model": "llama3",    "prompt": "Tell me about Nepal"  }'

### Response Example
    
    {    
        "data": {
            "response": "Nepal is a beautiful country located in South Asia, with a rich culture and history..."    
            },   
        "llms_name": "llama3"  } 

Installing Ollama and Llama3 Model
----------------------------------

### Installing Ollama

1.  **Clone the Repository**: Clone the [!Ollama](https://github.com/ollama/ollama) repository from the source.
    
2.  **Setup Environment**: Follow the setup instructions provided in the repository's README to set up Ollama.
    

### Installing Llama3 Model

1.  **Clone Llama3 Repository**: Clone the Llama3 model repository from the source.
    
2.  **Install Dependencies**: Install necessary dependencies as per the model's README instructions.
    
3.  **Model Initialization**: Initialize and configure Llama3 as required by your application.
