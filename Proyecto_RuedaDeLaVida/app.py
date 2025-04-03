from flask import Flask, render_template, request, redirect, url_for
import csv

import mysql.connector

import pandas as pd
import matplotlib.pyplot as plt

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='RuedaDeLaVida')


cursor = cnx.cursor()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/persona")
def persona():
    return render_template("persona.html")

@app.route("/enviar/db", methods=['POST'])
def enviar_datos_db():

  nombre = request.form['nombre']
  apellido = request.form['apellido']
  ocio = request.form['ocio']
  personal = request.form['personal']
  dinero = request.form['dinero']
  trabajo = request.form['trabajo']
  fisica = request.form['fisica']
  familiar = request.form['familiar']
  social = request.form['social']
  espiritual = request.form['espiritual']

  # Procesar los datos (por ejemplo, guardarlos en una base de datos)
  # Aquí simplemente los imprimimos por el momento
  print(f'Nombre: {nombre}')

  totalMavIa = [nombre, apellido, ocio, personal, dinero, trabajo, fisica, familiar, social, espiritual]

  with open("datos.csv", "a+", newline ='') as csvfile:
    wr = csv.writer(csvfile, dialect='excel', delimiter=',')
    wr.writerow(totalMavIa)

  guardar_datos = ("INSERT INTO Encuesta(nombre, apellido, ocio, personal, dinero, trabajo, fisica, familiar, social, espiritual) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
  
  datos_encuenta = (nombre, apellido, int(ocio), int(personal), int(dinero), int(trabajo), int(fisica), int(familiar), int(social), int(espiritual))


  cursor.execute(guardar_datos, datos_encuenta)
  cnx.commit()

  cursor.close()
  cnx.close()

  df = pd.read_csv("C:/Users/y2kds/OneDrive - SENA/TRIM 6/CIENCIA DE DATOS/Ruedadelavida/Proyecto_RuedaDeLaVida/datos.csv")

  df.columns = df.columns.str.strip()

  columnas_y = ["Ocio", "Personal", "Dinero", "Trabajo", "Fisica", "Familiar", "Social", "Espiritual"]

  # Por ejemplo, graficar una columna vs otra
  df.plot(x="Nombre", y=columnas_y, kind="bar")  # puede ser "line", "bar", "scatter", etc.
  plt.title("Ventas por Fecha")
  plt.xlabel("Fecha")
  plt.ylabel("Ventas")
  plt.grid(True)

  plt.savefig('static/uploads/balance.png') 

  plt.close()


  return redirect(url_for('persona'))

@app.route("/leer")
def leer():
    data = []
    with open("./datos.csv") as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    data.append(row)
    return render_template('table.html', data=data)
  