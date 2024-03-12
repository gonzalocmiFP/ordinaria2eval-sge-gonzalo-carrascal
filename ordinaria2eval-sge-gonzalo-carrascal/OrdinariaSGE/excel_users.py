import json
import pandas as pd
import openpyxl

def loadJSON():
    try:
        with open("secure-users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

usuarios = loadJSON()

ids = []
passwords = []

for usuario in usuarios:
    ids.append(usuario['id'])
    passwords.append(usuario['password'])

df = pd.DataFrame({
    'id': ids,
    'password': passwords
})

df.to_excel("usuarios.xlsx")
print(df)