#!/bin/bash

# Caminho do diretório onde o Easy-RSA está localizado
EASYRSA_DIR=~/openvpn-ca

# Verifica se o diretório existe
if [ ! -d "$EASYRSA_DIR" ]; then
    echo "[INFO] Clonando Easy-RSA no diretório $EASYRSA_DIR..."
    git clone https://github.com/OpenVPN/easy-rsa.git "$EASYRSA_DIR"
fi

cd "$EASYRSA_DIR" || exit 1

# Inicializa o PKI se ainda não existir
if [ ! -d "pki" ]; then
    echo "[INFO] Inicializando PKI..."
    ./easyrsa init-pki
else
    echo "[INFO] PKI já inicializado."
fi

# Cria a CA se ainda não existir
if [ ! -f "pki/ca.crt" ]; then
    echo "[INFO] Criando Autoridade Certificadora (CA)..."
    echo | ./easyrsa build-ca nopass
else
    echo "[INFO] CA já existente."
fi

echo "[OK] Ambiente Easy-RSA está pronto para uso."
