## Scripts ansible

Différents scripts qui permettent de configurer et mettre en place l'environnement de production

### Requis
- ansible
- sshpass

### Configuration
Les serveurs sont définis dans l'inventaire, `inv.ini`

Pour vérifier la connexion:
```bash
# sshpass fonctionne
sshpass -p [MOTDEPASSE] ssh [USER]@[HOST] echo 'OK'

# ansible sait se connecter
ansible -i inv.ini -u admin --ask-pass server -m ping
```

### Détails des _playbooks_

- **secure_ssh**: configuration accès SSH
- **default_apps**: applications par défaut
- **docker_suppport**: Support docker
- **travis_support**: Ajout utilisateur déploiement Travis
- **toolset**: Installation de services et d'outils spécifiques
- **postgresql_config**: Configuration de base PostgreSQL

### Exécution
Le playbook `secure_ssh` s'exécute avec les droits d'aministrateur (root). Les autres utilisent l'utilisateur de déploiement définit dans les _playbooks_

#### Examples:
```bash
# configuration SSH
ansible-playbook secure_ssh.yml -i inv_root.ini -u [ROOT_USER] --ask-pass

# Alternativement, en fournissant l'adresse IP de l'hôte
# la dernière partie est à inclure si l'utilisateur n'est pas root
ansible-playbook secure_ssh.yml -i "[IP]," -u [ROOT_USER] --ask-pass [-b --become-user=root]

# applications par défaut et autres playbooks
ansible-playbook default_apps.yml -i inv.ini -b --become-user=root
```
