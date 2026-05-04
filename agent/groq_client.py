import os
from groq import Groq
from dotenv import load_dotenv

class GroqClient:
    def __init__(self):
        load_dotenv(override=True)
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            # Fallback for better error messaging in the UI
            self.api_key = None
        else:
            self.client = Groq(api_key=self.api_key)

    def get_completion(self, messages, model="llama-3.3-70b-versatile", temperature=0.7, max_tokens=2048):
        if not self.api_key:
            return "Error: Groq API Key missing. Please check your .env file."
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=1,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    def stream_completion(self, messages, model="llama-3.3-70b-versatile", temperature=0.7, max_tokens=2048):
        if not self.api_key:
            yield "Error: Groq API Key missing. Please check your .env file."
            return
        try:
            stream = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=1,
                stream=True
            )
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Error: {str(e)}"
