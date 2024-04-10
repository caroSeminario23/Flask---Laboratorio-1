# INICIALIZACIÓN DE LA INSTANCIA DE LA APLICACION
from flask import Flask # Importación de la clase Flask
from flask import make_response # Importación de la función make_response para crear respuestas personalizadas

app = Flask(__name__) # Creación de la instancia de la aplicación

# RUTEO DE UNA FUNCIÓN PYTHON MEDIANTE URL
@app.route('/') # Decorador que indica la URL que se va a utilizar
def index(): # Función que se va a ejecutar (Función de vista)
    response = make_response('<h1>This document carries a cookie!</h1>') # Creación de una respuesta personalizada con una cookie
    """ Una cookie es un pequeño archivo que un servidor coloca en el navegador del usuario. Por lo general, se utiliza
    para saber si dos solicitudes provienen del mismo navegador, como mantener la sesión de un usuario """
    response.set_cookie('answer', '42') # Creación de una cookie con el nombre 'answer' y el valor '42'
    return response # Retorno de la respuesta personalizada

# EJECUCIÓN DE LA APLICACIÓN
if __name__ == '__main__': # Verificación de que el script se está ejecutando
    app.run(debug=True) # Inicialización de la aplicación