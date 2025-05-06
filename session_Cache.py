import time

# Armazena sessões ativas: {username: timestamp}
session_cache = {}

def init_session(username):
    """Registra o horário de início da sessão de um usuário."""
    session_cache[username] = time.time()
