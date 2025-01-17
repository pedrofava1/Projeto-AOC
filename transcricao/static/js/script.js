// Função para enviar a mensagem
async function sendMessage() {
    const userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return; // Não faça nada se o campo estiver vazio
  
    // Exibir a mensagem do usuário (alinhada à direita)
    const messagesDiv = document.getElementById("messages");
    const userMessage = `<div class="message user">${userInput}</div>`;
    messagesDiv.innerHTML += userMessage;
  
    // Limpar o campo de entrada
    document.getElementById("user-input").value = "";
  
    // Enviar a mensagem para o servidor
    const response = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: userInput }),
    });
  
    // Obter a resposta do servidor
    const data = await response.json();
  
    // Exibir a resposta do bot (alinhada à esquerda)
    const botMessage = `<div class="message bot">${data.response}</div>`;
    messagesDiv.innerHTML += botMessage;
  
    // Scroll automático para o final
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
  }
  
  // Adicionar evento de clique no botão "Enviar"
  document.getElementById("send-button").addEventListener("click", sendMessage);
  
  // Adicionar evento para enviar mensagem ao pressionar "Enter"
  document.getElementById("user-input").addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
      event.preventDefault(); // Evita a quebra de linha no campo de entrada
      sendMessage();
    }
  });
  