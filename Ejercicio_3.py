# INICIALIZACIÓN DE LA INSTANCIA DE LA APLICACION
from flask import Flask # Importación de la clase Flask
from flask import request # Importación de la clase request

app = Flask(__name__) # Creación de la instancia de la aplicación

# RUTEO DE UNA FUNCIÓN PYTHON MEDIANTE URL
@app.route('/') # Decorador que indica la URL que se va a utilizar
def index(): # Función que se va a ejecutar (Función de vista)
    user_agent = request.headers.get('User-Agent') # Obtención del User-Agent del navegador
    return '<p>Your browser is %s</p>' % user_agent # Retorno del User-Agent del navegador

# EJECUCIÓN DE LA APLICACIÓN
if __name__ == '__main__': # Verificación de que el script se está ejecutando
    app.run(debug=True) # Inicialización de la aplicación