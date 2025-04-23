import tkinter as tk
from tkinter import messagebox
import os
from user_Manager import create_user
from session_Cache import init_session, session_cache
import sys
print("Usando Python:", sys.executable)


def user():
    username = input_name.get()
    if username:
        create_user(username)
        messagebox.showinfo(f"Usuário '{username}' criado com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, insira um nome de usuário válido.")

def user_conect():
    username = input_name.get()
    if username:
        init_session(username)
        messagebox.showinfo(f"Usuário '{username}' conectado com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, insira um nome de usuário válido.")

def verify_session():
    username = input_name.get()
    if username:
        msg = session_cache(username)
        messagebox.showinfo("Verificação de Sessão", msg)
    else:
        messagebox.showerror("Campo vazio", "Insira um nome de usuário.")    


window = tk.Tk()
window.title("VPN SYSTEM - OpenVPN Based")
window.geometry("400x250")

tk.Label(window, text="Nome de Usuário:").pack(pady=10)
input_name = tk.Entry(window, width=10)
input_name.pack()