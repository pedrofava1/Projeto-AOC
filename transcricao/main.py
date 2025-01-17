from app.groq_model import GroqModel
from app.teaching_assistant import TeachingAssistant

# Configuração do modelo Groq
api_key = "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"  # Substituir pela chave da API Groq
groq_model = GroqModel(api_key=api_key)
assistant = TeachingAssistant(groq_model)

def ask(ask):
    """Processa a mensagem do usuário e retorna a resposta."""
    print('ask',ask)
    user_question = ask
    response = assistant.explain_concept(user_question)
    return response

if __name__ == "__main__":
    ask()
