
#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

nombre = form.getvalue("nombre")
apellido = form.getvalue("apellido")

print(f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado del Formulario</title>
</head>
<body>
    <h1>Datos Recibidos</h1>
    <p>Nombre: {nombre}</p>
    <p>Apellido: {apellido}</p>
</body>
</html>
""")