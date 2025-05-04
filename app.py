import tkinter as tk
from tkinter import messagebox
import os
from user_Manager import create_user
from session_Cache import init_session, session_cache
import sys
import time
# print("Usando Python:", sys.executable)

def user():
    username = input_name.get()
    if username:
        create_user(username)
        messagebox.showinfo("Sucesso", f"Usuário '{username}' criado com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, insira um nome de usuário válido.")

def user_conect():
    username = input_name.get()
    if username:
        init_session(username)
        messagebox.showinfo("Sucesso", f"Usuário '{username}' conectado com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, insira um nome de usuário válido.")

def verify_session():
    username = input_name.get()
    if username:
        if username in session_cache:
            time_online = int(time.time() - session_cache[username])
            messagebox.showinfo("Sessão Ativa", f"{username} está conectado há {time_online} segundos.")
        else:
            messagebox.showinfo("Sessão Inativa", f"{username} não está conectado.")
    else:
        messagebox.showerror("Campo vazio", "Insira um nome de usuário.")    

# Interface
window = tk.Tk()
window.title("VPN SYSTEM - OpenVPN Based")
window.geometry("400x250")


tk.Button(window, text="Criar Usuário", command=user).pack(pady=5)
tk.Button(window, text="Conectar Usuário", command=user_conect).pack(pady=5)
tk.Button(window, text="Verificar Sessão", command=verify_session).pack(pady=5)
tk.Button(window, text="Sair", command=window.quit).pack(pady=5)
tk.Label(window, text="Nome de Usuário:").pack(pady=10)
input_name = tk.Entry(window, width=10)
input_name.pack()

# Faltava isso!
window.mainloop()
