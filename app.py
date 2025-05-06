import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import time
import os

# Importa funções de arquivos externos
from user_Manager import create_user
from session_Cache import init_session, session_cache

# Caminho absoluto do arquivo de configuração OpenVPN
vpn_config_path = os.path.abspath("rodrigo.ovpn")

# === Funções de gerenciamento de usuários e sessão ===
def user():
    username = input_name.get().strip()
    if username:
        create_user(username)
        messagebox.showinfo("Sucesso", f"Usuário '{username}' criado com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, insira um nome de usuário válido.")

def user_conect():
    username = input_name.get().strip()
    if username:
        init_session(username)
        messagebox.showinfo("Sucesso", f"Usuário '{username}' conectado com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, insira um nome de usuário válido.")

def verify_session():
    username = input_name.get().strip()
    if username:
        if username in session_cache:
            time_online = int(time.time() - session_cache[username])
            messagebox.showinfo("Sessão Ativa", f"{username} está conectado há {time_online} segundos.")
        else:
            messagebox.showinfo("Sessão Inativa", f"{username} não está conectado.")
    else:
        messagebox.showerror("Erro", "Insira um nome de usuário.")

# === Funções de controle da VPN ===
def conectar_vpn():
    try:
        subprocess.Popen(["sudo", "openvpn", "--config", vpn_config_path])
        messagebox.showinfo("VPN", "Conectando à VPN...")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar à VPN:\n{e}")

def desconectar_vpn():
    try:
        subprocess.run(["sudo", "pkill", "openvpn"])
        messagebox.showinfo("VPN", "VPN desconectada.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao desconectar:\n{e}")

def verificar_status_vpn():
    try:
        output = subprocess.check_output("ip a | grep tun", shell=True).decode()
        status = "✅ VPN está CONECTADA." if "tun" in output else "❌ VPN está DESCONECTADA."
        messagebox.showinfo("Status VPN", status)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao verificar status:\n{e}")

def reiniciar_servidor():
    try:
        subprocess.run(["sudo", "systemctl", "restart", "openvpn"])
        messagebox.showinfo("Servidor", "Servidor OpenVPN reiniciado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao reiniciar servidor:\n{e}")

# Janela principal
window = tk.Tk()
window.title("VPN SYSTEM - OpenVPN Based")
window.geometry("400x400")

# Notebook com abas
notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

# Frame para a aba de usuário
aba_usuario = ttk.Frame(notebook)
notebook.add(aba_usuario, text="Gerenciar Usuário")

# Frame para a aba de VPN
aba_vpn = ttk.Frame(notebook)
notebook.add(aba_vpn, text="Gerenciar VPN")

# --- Aba 1: Usuário ---
tk.Label(aba_usuario, text="Nome de Usuário:").pack(pady=5)
input_name = tk.Entry(aba_usuario, width=30)
input_name.pack(pady=5)

tk.Button(aba_usuario, text="Criar Usuário", command=user).pack(pady=5)
tk.Button(aba_usuario, text="Conectar Usuário", command=user_conect).pack(pady=5)
tk.Button(aba_usuario, text="Verificar Sessão", command=verify_session).pack(pady=5)

# --- Aba 2: VPN ---
tk.Button(aba_vpn, text="Conectar VPN", command=conectar_vpn).pack(pady=10)
tk.Button(aba_vpn, text="Desconectar VPN", command=desconectar_vpn).pack(pady=5)
tk.Button(aba_vpn, text="Verificar VPN", command=verificar_status_vpn).pack(pady=5)
tk.Button(aba_vpn, text="Reiniciar Servidor", command=reiniciar_servidor).pack(pady=5)
tk.Button(aba_vpn, text="Sair", command=window.quit).pack(pady=20)

# Loop principal
window.mainloop()
