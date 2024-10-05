from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

# Configuración de la conexión a Azure SQL Database
server = 'serverapp.database.windows.net'
database = 'appdb'
username = 'admins'
password = 'Julietta20.,'
driver = '{ODBC Driver 17 for SQL Server}'

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
