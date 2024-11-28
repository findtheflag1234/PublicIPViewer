import requests

def get_public_ip():
    # Utilisation de l'API gratuite "https://api.ipify.org" pour récupérer l'IP publique
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            ip = response.json()['ip']
            print(f"Votre adresse IP publique est : {ip}")
        else:
            print("Erreur lors de la récupération de l'adresse IP.")
    except requests.exceptions.RequestException as e:
        print(f"Une erreur est survenue : {e}")

if _name_ == "_main_":
    get_public_ip()
