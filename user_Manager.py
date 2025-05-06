import os
import subprocess
import socket
import shutil

# Caminhos do ambiente
BASE_DIR = os.path.expanduser("~/openvpn-ca")
PKI_DIR = os.path.join(BASE_DIR, "pki")
PERFIS_DIR = os.path.abspath(".")  # onde salvará o .ovpn
SCRIPT_INIT = os.path.abspath("init_easyrsa_env.sh")


def get_local_ip():
    """Obtém o IP local da máquina para colocar no .ovpn"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def create_user(username):
    print(f"[INFO] Criando usuário: {username}...")

    # Verifica e executa o script de preparação do ambiente
    if not os.path.exists(SCRIPT_INIT):
        print(f"[ERRO] Script '{SCRIPT_INIT}' não encontrado.")
        return

    try:
        subprocess.run(["chmod", "+x", SCRIPT_INIT], check=True)
        subprocess.run(["bash", SCRIPT_INIT], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Falha ao preparar o ambiente Easy-RSA. Detalhes: {e}")
        return

    try:
        # 1. Gera chave e requisição de certificado
        subprocess.run(
            f"cd {BASE_DIR} && ./easyrsa gen-req {username} nopass",
            shell=True, check=True, executable="/bin/bash"
        )

        # 2. Assina o certificado
        subprocess.run(
            f"cd {BASE_DIR} && echo yes | ./easyrsa sign-req client {username}",
            shell=True, check=True, executable="/bin/bash"
        )

        # 3. Gera ta.key se ainda não existir
        ta_key_path = os.path.join(PERFIS_DIR, "ta.key")
        if not os.path.exists(ta_key_path):
            subprocess.run(
                f"cd {PERFIS_DIR} && openvpn --genkey --secret ta.key",
                shell=True, check=True, executable="/bin/bash"
            )

        # 4. Copia arquivos necessários para a pasta do projeto
        shutil.copy(os.path.join(PKI_DIR, "ca.crt"), PERFIS_DIR)
        shutil.copy(os.path.join(PKI_DIR, "issued", f"{username}.crt"), os.path.join(PERFIS_DIR, f"{username}.crt"))
        shutil.copy(os.path.join(PKI_DIR, "private", f"{username}.key"), os.path.join(PERFIS_DIR, f"{username}.key"))

        # 5. Cria o arquivo .ovpn
        server_ip = get_local_ip()
        ovpn_path = os.path.join(PERFIS_DIR, f"{username}.ovpn")

        with open(ovpn_path, "w") as f:
            f.write(f"""client
dev tun
proto udp
remote {server_ip} 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
cert {username}.crt
key {username}.key
tls-auth ta.key 1
cipher AES-256-CBC
auth SHA256
verb 3
""")

        print(f"[OK] Arquivo {username}.ovpn criado com sucesso!")

    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Falha ao criar o usuário '{username}'. Detalhes: {e}")
