## Réutilisation et variantes des images de VM

| Tags |
|------|
| `VM` `image` `réutilisation` `variantes` |

Pour créer une nouvelle machine virtuelle (VM) à partir d'une image existante, suivez ces étapes :

1.  Connectez-vous à l'instance [NOM] via SSH en utilisant l'adresse IP [IP] et les informations d'identification appropriées.

2.  Exécutez la commande suivante pour cloner l'image VM existante. Remplacez `[nom_image_source]` par le nom de l'image source et `[nom_nouvelle_image]` par le nom de la nouvelle image :

    ```bash
    sudo virsh snapshot-create-as --domain [nom_image_source] [nom_nouvelle_image] --no-metadata --disk-only --atomic
    ```

3.  Démarrez la nouvelle VM à l'aide de la commande suivante, en remplaçant `[nom_nouvelle_image]` par le nom de la nouvelle image :

    ```bash
    sudo virsh start [nom_nouvelle_image]
    ```

4.  Si vous devez configurer le réseau pour la nouvelle VM, utilisez la commande suivante pour arrêter la VM :

    ```bash
    sudo virsh shutdown [nom_nouvelle_image]
    ```

5.  Modifiez le fichier de configuration de la VM en utilisant la commande suivante, en remplaçant `[nom_nouvelle_image]` par le nom de la nouvelle image :

    ```bash
    sudo virsh edit [nom_nouvelle_image]
    ```

6.  Dans le fichier de configuration de la VM, vous devrez peut-être modifier les paramètres réseau tels que l'adresse MAC et l'adresse IP pour éviter les conflits avec d'autres VM.

7.  Après avoir configuré le réseau, démarrez la VM à l'aide de la commande suivante, en remplaçant `[nom_nouvelle_image]` par le nom de la nouvelle image :

    ```bash
    sudo virsh start [nom_nouvelle_image]
    ```

Une fois que la nouvelle VM est démarrée, vous pouvez vous y connecter via SSH en utilisant l'adresse IP configurée et les informations d'identification appropriées.


## Réutilisation d'une image VM générique dans VirtualBox

| Tags |
|------|
| `VirtualBox` `VM` `Clonage` `Image` `Configuration` |

Réutiliser une image de machine virtuelle (VM) générique dans VirtualBox pour créer des variantes est un processus simple. Voici les étapes :

1.  **Création d'une image de base :**

    *   Configurez une VM avec le système d'exploitation et les logiciels souhaités.
    *   Appliquez les mises à jour et configurations nécessaires.
    *   Arrêtez la VM une fois terminée.

2.  **Clonage de la machine virtuelle :**

    *   Dans VirtualBox, sélectionnez la VM à cloner.
    *   Cliquez avec le bouton droit et choisissez "Cloner".
    *   Suivez l'assistant, en choisissant entre un clone complet ou lié (le clone lié économise de l'espace disque).
    *   Nommez la nouvelle VM et choisissez son emplacement.

3.  **Configuration des variantes :**

    *   Démarrez la VM clonée.
    *   Effectuez les modifications spécifiques à cette variante (installation de logiciels, modification des paramètres, etc.).
    *   Arrêtez la VM une fois terminée.

4.  **Répétition du processus pour d'autres variantes :**

    *   Répétez les étapes 2 et 3 pour créer autant de variantes que nécessaire à partir de l'image de base.

5.  **Utilisation de snapshots (facultatif) :**

    *   Utilisez les snapshots de VirtualBox pour sauvegarder différents états d'une VM. Utile pour revenir rapidement à un état précédent.

6.  **Exportation et importation (facultatif) :**

    *   Pour partager vos VM, exportez-les via "Exporter l'Appliance" dans le menu "Fichier". Cela crée un fichier OVA importable dans d'autres VirtualBox.

7.  **Gestion des adresses MAC (facultatif) :**

    *   Lorsque vous clonez une VM, régénérez les adresses MAC pour éviter les conflits réseau.

En suivant ces étapes, vous pouvez créer et gérer plusieurs variantes d'une VM générique dans VirtualBox. Cela est utile pour tester différentes configurations, développer des logiciels, etc.


## Création d'une image VirtualBox depuis un ISO

| Tags |
|------|
| `VirtualBox` `ISO` `VM` `Installation` |

<p>Créer une image VirtualBox à partir d'un fichier ISO est un processus standard pour installer un système d'exploitation dans une machine virtuelle. Voici comment vous pouvez le faire :</p>
<ol>
<li>
<p><strong>Ouvrez VirtualBox</strong> :</p>
<ul>
<li>Lancez VirtualBox sur votre ordinateur.</li>
</ul>
</li>
<li>
<p><strong>Créez une Nouvelle Machine Virtuelle</strong> :</p>
<ul>
<li>Cliquez sur &quot;Nouveau&quot; pour créer une nouvelle machine virtuelle.</li>
<li>Nommez votre machine virtuelle et choisissez le type de système d'exploitation que vous allez installer.</li>
<li>Configurez la mémoire et les autres paramètres selon vos besoins.</li>
</ul>
</li>
<li>
<p><strong>Configurez le Stockage</strong> :</p>
<ul>
<li>Dans l'assistant de création, vous serez invité à configurer le stockage. Choisissez de créer un nouveau disque dur virtuel.</li>
<li>Sélectionnez le type de fichier pour le disque dur virtuel (VDI est généralement recommandé) et configurez la taille.</li>
</ul>
</li>
<li>
<p><strong>Montez l'ISO</strong> :</p>
<ul>
<li>Une fois la machine virtuelle créée, sélectionnez-la et cliquez sur &quot;Configuration&quot;.</li>
<li>Allez dans la section &quot;Stockage&quot; et cliquez sur l'icône du CD vide sous &quot;Contrôleur: IDE&quot; ou &quot;Contrôleur: SATA&quot;.</li>
<li>Cliquez sur l'icône du CD à droite et sélectionnez &quot;Choisir/Creéer un disque optique&quot;.</li>
<li>Trouvez et sélectionnez votre fichier ISO, puis cliquez sur &quot;OK&quot;.</li>
</ul>
</li>
<li>
<p><strong>Configurez d'Autres Paramètres (Facultatif)</strong> :</p>
<ul>
<li>Vous pouvez également configurer d'autres paramètres tels que le réseau, les périphériques USB, etc., selon vos besoins.</li>
</ul>
</li>
<li>
<p><strong>Démarrez la Machine Virtuelle</strong> :</p>
<ul>
<li>Sélectionnez la machine virtuelle et cliquez sur &quot;Démarrer&quot;.</li>
<li>La machine virtuelle devrait démarrer à partir de l'ISO, et vous pouvez suivre les instructions à l'écran pour installer le système d'exploitation.</li>
</ul>
</li>
<li>
<p><strong>Installez les Additions Invité (Facultatif)</strong> :</p>
<ul>
<li>Une fois le système d'exploitation installé, vous pouvez installer les Additions Invité de VirtualBox pour améliorer l'intégration avec votre système hôte.</li>
</ul>
</li>
<li>
<p><strong>Éteignez la Machine Virtuelle</strong> :</p>
<ul>
<li>Une fois que vous avez terminé l'installation et la configuration, éteignez la machine virtuelle.</li>
</ul>
</li>
<li>
<p><strong>(Facultatif) Détachez l'ISO</strong> :</p>
<ul>
<li>Si vous ne voulez plus que l'ISO soit connecté, retournez dans &quot;Configuration&quot; &gt; &quot;Stockage&quot; et retirez l'ISO.</li>
</ul>
</li>
</ol>
<p>Vous avez maintenant une machine virtuelle VirtualBox créée à partir d'un fichier ISO. Vous pouvez la cloner, prendre des snapshots, ou l'exporter.</p>
