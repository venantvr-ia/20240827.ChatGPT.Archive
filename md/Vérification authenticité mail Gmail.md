## Vérification de l'authenticité d'un e-mail Gmail

| Tags |
|------|
| `Gmail` `e-mail` `Authentification` `SPF` `DKIM` `DMARC` |

Pour vérifier l'authenticité d'un e-mail Gmail, examinez les en-têtes du message. Voici les étapes :

1.  **Ouvrez l'e-mail.**
2.  **Cliquez sur les trois points verticaux** à côté du bouton "Répondre".
3.  **Sélectionnez "Afficher l'original".** Une nouvelle fenêtre s'ouvrira avec les en-têtes de l'e-mail.

Dans les en-têtes, vous trouverez des informations cruciales :

*   **De:** L'adresse e-mail de l'expéditeur. Assurez-vous qu'elle correspond à la personne attendue.
*   **Envoyé par:** Le domaine d'envoi. Vérifiez la cohérence avec l'adresse "De:".
*   **Signé par:** Indique le domaine qui a signé numériquement l'e-mail.

Examinez les champs liés à l'authentification :

*   **SPF (Sender Policy Framework):** Vérifie si le serveur d'envoi est autorisé par le propriétaire du domaine à envoyer des e-mails en son nom. Recherchez `spf=pass`.

    Exemple :

    ```text
    Received-SPF: pass (google.com: domain of [EMAIL] designates [IP] as permitted sender)
    ```

*   **DKIM (DomainKeys Identified Mail):** Utilise une signature numérique pour vérifier l'intégrité du message. Recherchez `dkim=pass`.

    Exemple :

    ```text
    DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=example.com; s=selector;
        h=mime-version:subject:from:date:message-id:reply-to:to;
        [...]
        b=signature
    ```

*   **DMARC (Domain-based Message Authentication, Reporting & Conformance):**  Fournit des instructions aux fournisseurs de messagerie sur la façon de traiter les e-mails qui échouent aux vérifications SPF et DKIM. Recherchez `dmarc=pass`.

    Exemple :

    ```text
    Authentication-Results: mx.google.com;
       spf=pass (google.com: domain of [EMAIL] designates [IP] as permitted sender) smtp.mailfrom=[EMAIL];
       dkim=pass header.i=[NOM]
       dmarc=pass ([NOM]) header.from=[EMAIL]
    ```

Si SPF, DKIM et DMARC passent, l'e-mail est probablement authentique.  Si un ou plusieurs de ces contrôles échouent, l'e-mail pourrait être suspect.  Méfiez-vous particulièrement des e-mails provenant de domaines inconnus ou non sollicités, même s'ils semblent passer ces vérifications. Si vous avez des doutes, contactez l'expéditeur par un autre moyen pour confirmer l'authenticité du message.

## Tracer l'authenticité d'un e-mail Gmail

| Tags |
|------|
| `Gmail` `e-mail` `sécurité` `phishing` |

Pour tracer l'authenticité d'un e-mail reçu avec Gmail, suivez ces étapes afin de vérifier les détails techniques et les indices de phishing ou d'usurpation d'identité.


## Examiner l'adresse de l'expéditeur

| Tags |
|------|
| `Sécurité` `Email` `Phishing` |

Regardez attentivement l'adresse email de l'expéditeur. Les cybercriminels peuvent utiliser des adresses qui ressemblent à des adresses légitimes mais contiennent des petites différences (par exemple, <code>support@[NOM].com</code> au lieu de <code>support@gmail.com</code>).


## Analyse des en-têtes d'email

| Tags |
|------|
| `email` `en-têtes` `Gmail` `sécurité` |

Les en-têtes d'email fournissent des informations techniques cruciales sur l'origine et le parcours d'un message. Pour afficher les en-têtes dans Gmail :

1.  Ouvrez l'email concerné.
2.  Cliquez sur les trois points verticaux dans le coin supérieur droit.
3.  Sélectionnez "Afficher l'original".

Cela ouvrira une fenêtre affichant les en-têtes et le contenu brut de l'email. Les éléments suivants sont particulièrement importants :

*   **Received** : Les lignes "Received" révèlent le chemin de l'email à travers les serveurs. Examinez les adresses IP et les noms de domaine pour toute anomalie. Par exemple :

    ```
    Received: from mail.example.com ([IP] via mail.example.com
    ```

*   **From** : Vérifiez que l'adresse email et le nom de domaine correspondent aux attentes. Exemple:

    ```
    From: [NOM] <[EMAIL]>
    ```

*   **Return-Path** : Cette ligne doit correspondre à l'adresse de l'expéditeur légitime.


## Vérification des signatures DKIM et SPF

| Tags |
|------|
| `DKIM` `SPF` `Sécurité Email` |

Pour vérifier l'intégrité d'un email, examinez les en-têtes pour les éléments suivants :

*   **DKIM (DomainKeys Identified Mail)** : Recherchez la ligne "DKIM-Signature". Une signature DKIM valide confirme l'authenticité et l'intégrité de l'email, prouvant qu'il provient du domaine annoncé et n'a pas été modifié.
*   **SPF (Sender Policy Framework)** : Examinez les résultats SPF dans les en-têtes. Une entrée SPF valide indique que l'email a été envoyé par un serveur autorisé par le domaine.


## Analyse du contenu des emails
| Tags |
|------|
| `Sécurité` `Email` `Analyse` |

*   **Liens** : Survolez les liens pour examiner leurs URLs. Vérifiez qu'elles dirigent vers des sites fiables.
*   **Pièces jointes** : Soyez prudent avec les pièces jointes, notamment les exécutables (.exe), les archives ZIP et les documents macros (.docm, .xlsm).
*   **Langue et ton** : Détectez les erreurs grammaticales, les tournures de phrases inhabituelles, ainsi que les messages urgents ou menaçants. Les organisations légitimes évitent de solliciter des informations personnelles par email de manière pressante.


## Utilisation d'outils tiers pour l'analyse d'en-têtes

| Tags |
|------|
| `MxToolbox` `Email Header Analyzer` `sécurité` |

Il est possible d'utiliser des outils et logiciels tiers pour analyser les en-têtes d'e-mails et vérifier leur authenticité. Parmi les outils disponibles :

*   **MxToolbox** : Cet outil peut analyser les en-têtes d'e-mails et fournir des informations sur les serveurs de messagerie.
*   **Email Header Analyzer** : Plusieurs sites web proposent des services d'analyse d'en-têtes d'e-mails pour la détection de tentatives de phishing.


## Ressources et outils

| Tags |
|------|
| `sécurité` `email` `Gmail` |

*   **<a href="https://safety.google/">Google Safety Center</a>** : Informations sur la sécurité et des outils fournis par Google.
*   **<a href="https://mxtoolbox.com/EmailHeaders.aspx">MxToolbox Email Header Analyzer</a>** : Un outil pour analyser les en-têtes d'email.

En suivant ces étapes, vous devriez pouvoir vérifier l'authenticité d'un email reçu sur Gmail et vous protéger contre les tentatives de phishing et autres types de fraude par email.
