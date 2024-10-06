from flask import Flask, render_template
import pyodbc
import os 
from dotenv import load_dotenv
app = Flask(__name__)

# Configuración de la conexión a Azure SQL Database
load_dotenv()  # Cargar las variables del archivo .env

server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
driver = os.getenv('DB_DRIVER')

def get_db_connection():
    connection = pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
    return connection

@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 5 * FROM Empleados")
    empleados = cursor.fetchall()
    conn.close()
    return render_template('index.html', empleados=empleados)

if __name__ == '__main__':
    app.run(debug=True)
