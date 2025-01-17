class TeachingAssistant:
    def __init__(self, groq_model):
        self.groq_model = groq_model

    def explain_concept(self, concept):
        """Cria um prompt para explicar conceitos de computadores."""
        prompt = (
            f"Explique o conceito de '{concept}' para uma criança. Use linguagem simples, "
            "analogias divertidas e mantenha a explicação curta. Responda sempre em português."	
        )
        return self.groq_model.get_response(prompt)
