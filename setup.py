import os
import subprocess
import sys

print("🔧 Preparando ambiente para o projeto VPN...")

# Cria pasta de perfis se não existir
os.makedirs("ovpn-profiles", exist_ok=True)

# Instala dependências
print("📦 Instalando dependências...")
subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requisitos.txt"])

# Executa a aplicação
print("🚀 Iniciando aplicação...")
os.system("python app.py")
