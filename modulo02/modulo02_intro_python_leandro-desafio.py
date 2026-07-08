
from datetime import datetime


agora = datetime.now()

hora_formatada = agora.strftime("%H:%M")

nome_usuario = input("Digite seu nome: ")

print(f"Olá, {nome_usuario}! Agora são {hora_formatada}. Tenha um ótimo dia!")