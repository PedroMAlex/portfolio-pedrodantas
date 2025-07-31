 import PyPDF2
 import os

 merger = PyPDF2.pdfMerger()

 Lista_arquivos = os.listdir("arquivos")
 Lista_arquivos.sort()
 print(Lista_arquivos)

 for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivo/{arquivo}")
 
 merger.write("PDF Final.pdf")

