import os 

def create_user(username):
    print(f"Criando usuário: {username}...")
    os.system(f"cd ~/openvpn-ca && source vars && ./build-key --batch {username}")

    with open(f"{username}.ovpn", "w") as f:
        f.write(f"""client
dev tun
proto udp
remote # COLOCAR IP AQUI
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.cre
cert {username}.crt
key {username}.key
tls-auth ta.key 1
cipher AES-256-CBC
auth SHA256
verb 3
""")
    print(f"Usuário {username} criado com sucesso!")