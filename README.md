# Glo-2005-team10

# Lancer le projet localement

Naviguer jusqu'au directory où vous avez cloné le projet et faire "docker-compose up"

## Note pour utilisateur Windows

Besoin de Docker Toolbox. Celui-ci se prend une adresse IP lorsque vous le lancez (affiché en haut de la console).
C'est l'adresse IP que vous devez utiliser dans votre browser pour accèder à l'app (et non pas localhost).

Assurez-vous aussi que votre éditeur de texte mets des séparateurs de ligne linux (\n) et non pas windows (\r\n) sinon
docker donnera une erreur disant qu'il ne trouve pas "python\r".

## Quelques erreurs qui pourraient arriver en buildant

### secur-priv-file is enabled
Assurez vous que le fichier /databaseconfig/configfile/custom.cnf est en read-only mode. On change cette configuration dans ce fichier mais docker ne le lira pas en buildant la db si il n'est pas en read-only mode. (Dans Pycharm, c'est le petit cadenas en bas à droite de l'éditeur)
On peut egalement resoudre ce probleme a l'aide de la commande:
```bash
# chmod 0444 /databaseconfig/configfile/custom.cnf
```

