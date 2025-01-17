from groq import Groq

class GroqModel:
    def __init__(self, api_key, model="llama3-70b-8192"):
        self.client = Groq(api_key=api_key)
        self.model = model

    def get_response(self, prompt):
        """Envia o prompt para a API Groq e retorna a resposta."""
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300,
        )
        return completion.choices[0].message.content.strip()
