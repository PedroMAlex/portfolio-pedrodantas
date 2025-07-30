import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def enviar_email():
    remetente = "seu email"
    senha = "senha de app"
    #Para encontrar a "senha de app" basta entrar em seu gmail, clicar em "Gerenciar a sua conta do Google" e pesquisar "senha de app" na barra de pesquisa. Dê um nome a sua senha de app e cole o código criado pelo google em senha=" "
    destinatario = "pythonimpressionador+diretoria@gmail.com"
    assunto = "Relatório de vendas do dia de hoje"
    corpo = "Este é um email automático do relatório de vendas do dia de hoje. Batemos a meta."

    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(corpo, "plain"))

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatario, mensagem.as_string())
    servidor.quit()
    print("Email enviado com sucesso")

enviar_email()