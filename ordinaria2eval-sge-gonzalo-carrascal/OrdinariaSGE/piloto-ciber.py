import json
import pandas as pd
import openpyxl

def loadJSON():
    try:
        with open("reservas.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}

reservas = loadJSON()

reservas_con_salas = []

for reserva in reservas:
    for sala in reservas:
        reservas_con_salas.append(sala['salaId'])
        reservas_con_salas.append(sala['suite'])
        reservas_con_salas.append(sala['plazas'])

salaIds = []
usuarioIds = []
plazas = []
suites = []
fechasReservas = []
horasReservas = []
nombresCompletos = []

for reserva in reservas:
    for sala in reserva['sala']:
       salaIds.append(sala['salaId'])
       usuarioIds.append(reserva['userId'])
       plazas.append(sala['plazas'])
       suites.append(sala['suite'])
       fechasReservas.append(reserva['date'])
       horasReservas.append(reserva['hours'])

df = pd.DataFrame({
    "ID Sala": salaIds,
    "ID Usuario": usuarioIds,
    "Plaza": plazas,
    "Suite": suites,
    "Fecha de reserva": fechasReservas,
    "Horas reservadas": horasReservas
})

df = df.sort_values("ID Sala")
df.to_excel("reservas.xlsx")
