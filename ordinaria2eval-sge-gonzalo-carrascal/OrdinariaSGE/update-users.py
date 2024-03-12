import json
import hashlib

def saveJSON(data):
    with open("secure-users.json", "w") as file:
        json.dump(data, file, indent=4)

def loadJSON():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def hashPassword(plain_password):
    return hashlib.sha256(plain_password.encode()).hexdigest()

secure_users = []
usuarios = loadJSON()

for usuario in usuarios:
    secure_user = {
        "id": usuario['id'],
        "password": hashPassword(usuario['password'])
    }
    secure_users.append(secure_user)

saveJSON(secure_users)