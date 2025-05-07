# 🔐 VPN SYSTEM - OpenVPN Based com Interface Gráfica

Este projeto implementa um sistema completo de gerenciamento e conexão VPN baseado em **OpenVPN**, com uma **interface gráfica em Python/Tkinter** para facilitar a criação de usuários, geração de certificados e controle da conexão VPN de forma amigável.

---

## 📌 Contexto

Durante a execução de sistemas VPN via terminal, usuários sem experiência técnica podem ter dificuldades na criação de certificados, configuração de arquivos `.ovpn` e gerenciamento da conexão. Este projeto foi desenvolvido como uma solução prática e visual para facilitar esse processo.

---

## 🧩 Aplicação

A aplicação é composta por:

* Interface gráfica (Tkinter)
* Automação de Easy-RSA (para geração de certificados)
* Criação automatizada de arquivos `.ovpn`
* Conexão e desconexão da VPN via interface
* Monitoramento de status da VPN
* Separação por guias (Usuário | VPN)

---

## 🏗️ Arquitetura

```
projeto_vpn/
├── app.py                  # Interface principal e controle da lógica
├── user_Manager.py         # Criação de usuários e certificados .ovpn
├── session_Cache.py        # Gerenciamento de sessões dos usuários
├── init_easyrsa_env.sh     # Inicialização do ambiente Easy-RSA
├── user.ovpn (gerado)   # Exemplo de perfil VPN criado
├── openvpn-ca/             # Ambiente Easy-RSA clonado e usado
└── README.md               # Instruções e documentação do projeto
```

---

## ⚙️ Pré-requisitos

* Python 3.11+ com Tkinter instalado
* `openvpn` instalado no sistema
* `git`, `bash`, `chmod`, `systemctl`
* Acesso root para operações `sudo`

---

## 🚀 Instalação

```bash
# Clone o projeto
git clone https://github.com/seu-usuario/projeto_vpn.git
cd projeto_vpn

# Torne o script executável
chmod +x init_easyrsa_env.sh
```

> ✅ Ao rodar o sistema pela interface, o ambiente Easy-RSA será inicializado automaticamente na primeira criação de usuário.

---

## ▶️ Executando o sistema

```bash
python3 app.py
```

Você verá uma interface com duas abas:

1. **Gerenciar Usuário**: onde você cria um usuário e gera seu certificado
2. **Gerenciar VPN**: conecta/desconecta e verifica o status da VPN

---

## 🛡️ Criação de Usuário e Perfil `.ovpn`

Na aba "Gerenciar Usuário":

* Digite o nome do novo usuário
* Clique em **Criar Usuário**
* O sistema irá gerar:

  * Certificado (`user.crt`)
  * Chave privada (`user.key`)
  * Arquivo `.ovpn` já preenchido com o IP da máquina local

---

## 🌐 Conexão VPN

Na aba "Gerenciar VPN":

* Clique em **Conectar VPN** para iniciar a conexão com o servidor
* Use **Verificar VPN** para ver o status da conexão
* Use **Desconectar VPN** para encerrar

---

## 📄 Observações

* O projeto utiliza `openvpn --config user.ovpn` via subprocess
* O script `init_easyrsa_env.sh` inicializa o ambiente de CA com Easy-RSA 3
* O IP local da máquina é detectado automaticamente e inserido no arquivo `.ovpn`

---

## 🧪 Testando a VPN

1. Execute `Wireshark` e filtre pacotes sem VPN conectada (`http`, `dns`, etc.)
2. Conecte a VPN via a interface
3. Observe que os pacotes agora estão encapsulados (e.g., `UDP`, `OpenVPN`, criptografados)
4. Use `ip route` para confirmar o roteamento via tun0/tun1

---

# 🔐 VPN SYSTEM - OpenVPN Based with Graphical Interface

This project implements a full VPN management and connection system based on **OpenVPN**, with a **Python/Tkinter GUI** to simplify user creation, certificate generation, and VPN connection control.

---

## 📌 Context

Running a VPN via terminal can be challenging for non-technical users, especially regarding certificate creation, `.ovpn` configuration, and connection management. This project provides a practical and visual solution to streamline the process.

---

## 🧩 Application

The application features:

* Graphical interface (Tkinter)
* Easy-RSA automation (for certificate generation)
* Automatic creation of `.ovpn` files
* VPN connect/disconnect controls via GUI
* VPN status monitoring
* Tabbed interface (User | VPN)

---

## 🏗️ Architecture

```
projeto_vpn/
├── app.py                  # Main interface and logic controller
├── user_Manager.py         # User creation and certificate generation
├── session_Cache.py        # User session handling
├── init_easyrsa_env.sh     # Easy-RSA environment initialization
├── user.ovpn (generated) # Example VPN profile
├── openvpn-ca/             # Easy-RSA working directory
└── README.md               # Project documentation
```

---

## ⚙️ Requirements

* Python 3.11+ with Tkinter
* `openvpn` installed on the system
* `git`, `bash`, `chmod`, `systemctl`
* Root access (`sudo`) required

---

## 🚀 Installation

```bash
# Clone the project
git clone https://github.com/your-user/projeto_vpn.git
cd projeto_vpn

# Make init script executable
chmod +x init_easyrsa_env.sh
```

> ✅ The Easy-RSA environment is automatically initialized on first user creation.

---

## ▶️ Running the system

```bash
python3 app.py
```

The GUI includes two tabs:

1. **User Management**: create new users and generate certificates
2. **VPN Management**: connect, disconnect, and check VPN status

---

## 🛡️ User & Profile `.ovpn` Generation

In the "User Management" tab:

* Enter a username
* Click **Create User**
* System will generate:

  * Certificate (`user.crt`)
  * Private key (`user.key`)
  * `.ovpn` file with local machine IP

---

## 🌐 VPN Connection

In the "VPN Management" tab:

* Click **Connect VPN** to start the tunnel
* Click **Check VPN** to view connection status
* Click **Disconnect VPN** to close the session

---

## 📄 Notes

* Uses `openvpn --config user.ovpn` via subprocess
* `init_easyrsa_env.sh` initializes Easy-RSA 3 environment
* IP is auto-inserted into the `.ovpn` file

---

## 🧪 Testing the VPN

1. Start `Wireshark` and capture non-VPN traffic (`http`, `dns`, etc.)
2. Connect to the VPN via the GUI
3. Notice encapsulated/encrypted packets (`UDP`, `OpenVPN`)
4. Run `ip route` to check routing via tun0/tun1
