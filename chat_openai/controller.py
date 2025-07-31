
from model import gerar_resposta

def processar_mensagem(entrada_usuario):
    resposta = gerar_resposta(entrada_usuario)
    return resposta
