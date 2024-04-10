# INICIALIZACIÓN DE LA INSTANCIA DE LA APLICACION
from flask import Flask # Importación de la clase Flask

app = Flask(__name__) # Creación de la instancia de la aplicación

# RUTEO DE UNA FUNCIÓN PYTHON MEDIANTE URL
@app.route('/') # Decorador que indica la URL que se va a utilizar
def index(): # Función que se va a ejecutar (Función de vista)
    return '<h1>Bad Request</h1>', 400 # Retorno de un Bad Request (Código 400 para indicar errores)

# EJECUCIÓN DE LA APLICACIÓN
if __name__ == '__main__': # Verificación de que el script se está ejecutando
    app.run(debug=True) # Inicialización de la aplicación