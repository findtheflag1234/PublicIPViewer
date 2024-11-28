# PublicIPViewer
Description
Public IP Viewer and Details est une application Python qui permet à l'utilisateur de récupérer son adresse IP publique, ainsi que des informations détaillées sur cette adresse IP, telles que sa géolocalisation, son organisation, et d'autres détails pertinents. L'application utilise les APIs ipify pour obtenir l'IP publique et ipinfo.io pour fournir des informations détaillées sur l'adresse IP.

Cette application peut être utilisée pour des démonstrations en cybersécurité, des exercices de certification CEH (Certified Ethical Hacker), ou pour simplement explorer et comprendre les informations relatives aux adresses IP publiques.

Fonctionnalités
Obtenir l'adresse IP publique de l'utilisateur : L'application utilise l'API ipify pour récupérer l'adresse IP publique de l'utilisateur.
Détails sur l'adresse IP : Pour toute adresse IP, l'application récupère des informations comme la localisation (ville, pays, région), l'organisation, le nom d'hôte et le code postal à l'aide de l'API ipinfo.io.
Interface utilisateur interactive : Un menu interactif permet à l'utilisateur de choisir facilement entre obtenir son IP publique, récupérer des détails sur une IP spécifique, ou quitter l'application.
Gestion d'erreurs robuste : L'application gère les erreurs liées aux requêtes API et offre des messages d'erreur explicites en cas de problème.
Prérequis
Avant de commencer, vous devez avoir Python 3 installé sur votre machine ainsi que les bibliothèques nécessaires. Vous pouvez installer les dépendances en utilisant pip.

Python 3.x
Bibliothèque requests (utilisée pour faire des requêtes HTTP)
Installation des dépendances
Clonez ce repository :

bash
Copier le code
git clone https://github.com/votre-utilisateur/public-ip-viewer.git
Accédez au dossier du projet :

bash
Copier le code
cd public-ip-viewer
Installez les dépendances requises :

bash
Copier le code
pip install requests
Utilisation
Lancer l'application
Exécutez le script Python depuis la ligne de commande :

bash
Copier le code
python public_ip_viewer.py
Un menu interactif apparaîtra, vous permettant de choisir une option :

Option 1 : Obtenir votre adresse IP publique.
Option 2 : Obtenir des détails supplémentaires sur une adresse IP (géolocalisation, organisation, etc.).
Option 3 : Quitter l'application.
Exemple d'exécution
Voici à quoi cela pourrait ressembler après avoir exécuté l'application :

bash
Copier le code
Bienvenue dans l'application de récupération d'IP publique et de ses détails.

=== Menu ===
1. Obtenir mon adresse IP publique
2. Obtenir des détails sur une adresse IP (géolocalisation, organisation, etc.)
3. Quitter
Choisissez une option (1-3) : 1

Votre adresse IP publique est : 203.0.113.45
Si vous choisissez l'option 2 pour obtenir des détails sur une adresse IP spécifique, vous pourriez voir quelque chose comme ceci :

bash
Copier le code
Entrez l'adresse IP dont vous voulez obtenir les détails : 8.8.8.8

Détails de l'adresse IP 8.8.8.8:
Localisation : Mountain View, California, US
Organisation : AS15169 Google LLC
Hostname : dns.google
Code postal : 94043
IP géolocalisée sur : 37.4056,-122.0775
Contribuer
Si vous souhaitez contribuer à ce projet, vous pouvez suivre ces étapes :

Forkez le repository.
Créez une branche pour votre fonctionnalité (git checkout -b feature/ma-fonctionnalité).
Faites vos modifications et committez-les (git commit -m 'Ajout de la fonctionnalité X').
Poussez vos changements sur votre fork (git push origin feature/ma-fonctionnalité).
Ouvrez une Pull Request dans ce repository.
Nous accueillons toutes les contributions, qu'elles soient des corrections de bugs, des améliorations de fonctionnalités, ou des suggestions d'optimisation.

License
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

Auteurs
Findtheflag - Développeur Principal
