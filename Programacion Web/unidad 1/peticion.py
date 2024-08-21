import requests
url = "https://api.github.com/users/dg203302"
headers = {
    "User-Agent": "ProgramacionWeb/1.0",
    "Accept": "application/vnd.github.v3+json"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print("Nombre de usuario:", data["login"])
    print("ID del usuario:", data["id"])
    print("Número de repositorios públicos:", data["public_repos"])
else:
    print("Error en la solicitud:", response.status_code)
    print("Detalle del error:", response.text)