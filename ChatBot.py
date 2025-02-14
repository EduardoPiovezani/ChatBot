import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model ='llama-3.3-70b-versatile')

def resposta_bot(mensagens):
    mensagens_modelo = [('system' , 'Você é um assistente virtual amigável chamado IAgo')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({}).content

print('Bem vindo sou IAgo o ChatBot da NexView!\n')
nome = input('Digite o seu nome para começarmos: ')



mensagens = []

while True:
    pergunta = input(f'Olá {nome}. No que posso auxilixar? ')
    if pergunta.lower() == 'encerrar':
        break
    mensagens.append(( 'user', pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')
print('Encerrando o atendimento, muito mobrigado por entrar em contato!')
print(mensagens)

