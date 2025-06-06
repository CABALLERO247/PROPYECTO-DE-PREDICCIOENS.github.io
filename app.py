"""
NOMBRE DE LOS ALUMNOS:
DULCE CECILIA HERNANDES DE LA CRUZ.
ERICK GABRIEL LOPEZ MELO.
LEONARDO LEDESMA MERCADO.
NOMBRE DEL DOCENTE:
ELI HUSIM RUIZ CRUZ.
GRUPO:
605
MATERIA:
ANALISIS DEL LENGUAJE NATURAL.
CARRERA:
CIENCIA DE DATOS E INTELIGENCIA ARTIFICIAL.
SEMESTRE:
6.TO
FECHA:
19/05/2025
ACTIVIDAD:
EL CODIGO PARA LA CONEXION ESTABLE TANTO EL ARCHIVO GENERADO DE LA PREDICCION A LA PAGINA WEB.
"""

from flask import Flask, send_from_directory # "FLASK" ES PARA CREAR LA APLICACION WEB Y "SEND_FROM_DIRECTORY" PARA SERVIR ARCHIVOS ESTATICOS
import os # ESTA LIBRERIA SIRVE PARA ACCEDER A UNA SERIE DE FUCIONES QUE PERMITEN INTERACTUAR CON EL SISTEMA OPERATIVO SUBYACENTE

app = Flask(__name__, static_folder="public") # CREA UNA OBJETO DE APLICACION FLASK, ESTABLECIENDO LA CARPETA ESTATICA COMO "PUBLICA"

@app.route("/") # DEFINIMOS LA RUTA RAIZ, QUE SIRVE EL "INDEX.HTML" ARCHIVO DESDE "STATIC" DIRECTORIO
def home(): # LA FUNCION HOME DEVUELVE EL ARCHIVO "INDEX.HTML" UTILIZANDO "APP.SEND_STATIC_FILES"
    return app.send_static_file("D:/CONALEP/6TO.SEMESTRE/ANALISIS DEL LENGUAJE NATURAL/TRABAJOS/PROYECTO DE LA JORNADA TECNOLOGICA/index1.html") # LO QUE HACE QUE EL ARCHIVO HTML SE SIRVA AL USUARIO QUE VISITA LA PAGINA PRINCIPAL

@app.route("/download") # DEFINE LA RUTA PARA DESCARGAR UN ARCHIVO
def download_file(): # UTILIZA "SEND_FROM_DIRECTORY" PARA SERVIR UN ARCHIVO EXCEL DESDE UN DIRECTORIO
    # Envía el Excel desde public/files
    return send_from_directory(
        directory=os.path.join(app.root_path, "public", "files"),
        path="D:/CONALEP/6TO.SEMESTRE/ANALISIS DEL LENGUAJE NATURAL/TRABAJOS/PROYECTO DE LA JORNADA TECNOLOGICA/Predicciones_Abandono_2034.xlsx", # RECIBE EL DIRECTORIO DEL ARCHIVO EXCEL
        as_attachment=True, # PARA FORZAR LA DESCARGA
        download_name="Predicciones_abandono_2034.xlsx" # NOMBRE DEL ARCHIVO
    )

if __name__ == "__main__": # ASEGURA QUE EL CODIGO DENTRO DE ESTE BLOQUE SE EJECUTE SOLO CUANDO EL SCRIPT SE EJECUTA DIRECTAMENTE (NO CUANDO SE IMPORTA COMO UN MODULO)
    app.run(debug=True) # INICIA EL SERVIRDOR WEB CON LA CONFIGURACION DE DEPURACION ACTIVADA. ESTO PERMITE A LA APLICACION MOSTRAR MENSAJES DE ERROR Y FACILITA LA DEPURACION