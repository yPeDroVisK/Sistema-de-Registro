import tkinter as tk
from tkinter import messagebox
import re
import sqlite3

# Regex - Email-Usuário (Definidos antes para as funções usarem)
__EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
__USER_RE = re.compile(r"^[a-zA-ZÀ-ÿ\s]{3,50}$")

def registrar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()

    # Validação primeiro
    if __EMAIL_RE.match(email) and __USER_RE.match(nome):
        try:
            messagebox.showinfo("Sucesso", "Email e Usuário cadastrados!")
            
            # Limpa os campos após sucesso
            entry_nome.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            
        except Exception as e:
            messagebox.showerror("Erro ao resgistrar", f"Erro: {e}")
    else:
        # Se os dados não passarem no Regex
        messagebox.showerror("Erro", "Nome (3-50 letras) ou E-mail inválido!")
        entry_email.delete(0, tk.END)
        entry_nome.delete(0, tk.END)

def banco_dados():
    conn = sqlite3.connect("sistema_usuarios.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL )''')
    conn.commit()
    conn.close()

# Inicializa o DB
banco_dados()

Janela = tk.Tk()
Janela.title("Sistema de Registro")
Janela.geometry("400x350")
Janela.resizable(False, False)

tk.Label(Janela, text="Bem-vindo ao Sistema", font=("Arial", 12, "bold")).pack(pady=15)
tk.Label(Janela, text="Nome Completo:").pack()
entry_nome = tk.Entry(Janela, width=35, relief="solid")
entry_nome.pack(pady=5)
tk.Label(Janela, text="E-mail:").pack()
entry_email = tk.Entry(Janela, width=35, relief="solid")
entry_email.pack(pady=5)

btn_registrar = tk.Button(Janela, text="Registrar", width=15)
btn_registrar.pack(pady=20)

Janela.mainloop()