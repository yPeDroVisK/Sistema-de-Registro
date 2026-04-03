import tkinter as tk

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