import re
import tkinter as tk
from tkinter import filedialog, messagebox

def converter_datas(texto):
    padrao_data = r'(\d{4})-(\d{2})-(\d{2})'
    texto_convertido = re.sub(padrao_data, r'\3/\2/\1', texto)
    return texto_convertido

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo de texto",
        filetypes=[("Arquivos de texto", "*.txt")]
    )
    if caminho_arquivo:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        
        conteudo_convertido = converter_datas(conteudo)
        
        salvar_como = filedialog.asksaveasfilename(
            title="Salvar arquivo convertido como...",
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt")]
        )
        if salvar_como:
            with open(salvar_como, 'w', encoding='utf-8') as arquivo_saida:
                arquivo_saida.write(conteudo_convertido)
            messagebox.showinfo("Sucesso", f"Arquivo convertido salvo em:\n{salvar_como}")

# Criando a janela principal
janela = tk.Tk()
janela.title("Conversor de datas AAAA-MM-DD para DD/MM/AAAA")
janela.geometry("400x200")

# Texto informativo
label = tk.Label(janela, text="Clique no botão abaixo para selecionar o arquivo e converter as datas:", wraplength=350)
label.pack(pady=20)

# Botão para selecionar o arquivo
botao_selecionar = tk.Button(janela, text="Selecionar arquivo", command=selecionar_arquivo, width=20, height=2)
botao_selecionar.pack(pady=10)

# Rodar a interface
janela.mainloop()
