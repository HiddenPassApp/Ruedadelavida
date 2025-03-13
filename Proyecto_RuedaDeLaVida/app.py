from flask import Flask, render_template, request, redirect, url_for
import csv


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/enviar', methods=['POST'])
def enviar_datos():
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
  
  return redirect(url_for('home'))

@app.route("/leer")
def leer():
    data = []
    with open("./datos.csv") as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    data.append(row)
    return render_template('table.html', data=data)
  