
import tkinter as tk
from controller import processar_mensagem

def iniciar_interface():
    janela = tk.Tk()
    janela.title("Chat com OpenAI")
    janela.geometry("500x500")

    chat_log = tk.Text(janela, state='disabled', wrap='word')
    chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entrada = tk.Entry(janela)
    entrada.pack(padx=10, pady=5, fill=tk.X)

    def enviar_mensagem():
        mensagem = entrada.get()
        if mensagem.strip():
            chat_log.config(state='normal')
            chat_log.insert(tk.END, "Você: " + mensagem + "\n")
            chat_log.config(state='disabled')
            entrada.delete(0, tk.END)
            janela.update()

            resposta = processar_mensagem(mensagem)
            chat_log.config(state='normal')
            chat_log.insert(tk.END, "IA: " + resposta + "\n\n")
            chat_log.config(state='disabled')
            chat_log.see(tk.END)

    botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem)
    botao_enviar.pack(pady=5)

    janela.mainloop()
