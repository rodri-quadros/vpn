import time
session_cache = {}

def init_session(username):
    session_cache[username] = time.time()

def verify_session(username):
    if username in session_cache:
        time_online = time.time() - session_cache[username]
        print(f"{username} está conectado há {int(time_online)} segundos.")
    else:
        print(f"{username} não está conectado.")