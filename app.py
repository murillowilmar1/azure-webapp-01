from flask import Flask, render_template

# Inicializa la aplicación Flask
app = Flask(__name__)

# Ruta principal que devuelve el archivo HTML
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para el Health Check
@app.route('/health')
def health_check():
    return 'Healthy', 200

# Inicia el servidor si este archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)
