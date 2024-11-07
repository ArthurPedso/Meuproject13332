import os 
from groq import groq

# Defina a chave da API diretamente no código ou que ela esteja configurada corretamente no ambiente
os.envirom["GROQ_API_KEY"] = "Digite aqui a sua chave de API"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# Inicializa a lista de mensagens para manter o contexto da conversa
mensages = []

while True:
    usuario = input ("Digite uma mensagem ou 'sair' para encerrar: ")

    if usuario.lower() == 'sair':
        print("Conversa encerrada.")
        break

    # Adiciona a mensagem do usuário á lista de mensagens
    mensages.append({"role": "user", "content": usuario})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-70b-versale",
    )

    resposta = chat_completion.choices[0].message.content
    print("Resposta:",resposta)

    # Adiciona a resposta do assistente á lista de mensagens para manter o contexto
    messages.append({"role": "assistant", "content": resposta})