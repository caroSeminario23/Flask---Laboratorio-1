# INICIALIZACIÓN DE LA INSTANCIA DE LA APLICACION
from flask import Flask # Importación de la clase Flask
#from flask_script import Manager # Importación de la clase Manager para la gestión de la aplicación

app = Flask(__name__) # Creación de la instancia de la aplicación
#manager = Manager(app) # Creación de la instancia del administrador de la aplicación

# RUTEO DE UNA FUNCIÓN PYTHON MEDIANTE URL
@app.route('/') # Decorador que indica la URL que se va a utilizar
def index(): # Función que se va a ejecutar (Función de vista)
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>') # Ruta con un parámetro
def user(name): # Definición de la función
    return '<h1>Hello, %s!</h1>' % name

# EJECUCIÓN DE LA APLICACIÓN
if __name__ == '__main__': # Verificación de que el script se está ejecutando
    app.run() # Inicialización de la aplicación mediante el administrador