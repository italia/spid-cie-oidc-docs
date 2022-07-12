.. include:: ./common_definitions.rst


.. _claim_utente_CIE:


Claim Utente per CIE
^^^^^^^^^^^^^^^^^^^^

Per identificare con successo l'utente, CIE OIDC ha identificato un unsieme di **claim utente**. La maggior
parte sono presi dai claim utente definiti in `iGov.OIDC`_ (vedi Tabella 1) e in `OpenID.IDA`_ (vedi Tabella 2). 
Un sottoinsieme di essi è personalizzato ed è stato introdotto per lo scenario CIE (vedi Tabella 3).

.. list-table:: Claim Utente da OpenID Connect Core
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **email_verified**
     - Valore booleano che indica se l'indirizzo email  dell'utente è stato verificato. 
       Quando vale *true*, significa che l'OP ha compiuto passi significativi per assicurarsi che l'utente
       abbia già svolto la verifica, al momento in cui questo controllo è stato effettuato. 
       La misura in cui un indirizzo email è considerato verificato, dipende dal contesto e dalla struttura 
       della fiducia o dell'accordo contrattuale con il quale le parti operano.
     - |cieid-icon|
   * - **phone_number_verified**
     - Valore booleano che indica se il numero di telefono mobile è stato verificato. 
       Quando vale *true*, significa che l'OP ha compiuto passi significativi per assicurarsi che l'utente
       abbia già svolto la verifica, al momento in cui questo controllo è stato effettuato. 
       Significa inoltre che il formato DEVE essere come in `E164`_ e le estensioni come in :rfc:`3966`.
     - |cieid-icon|



Claim Utente specifici per CIEid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Claim Utente specifici per CIEid
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **https://attributes.eid.gov.it/idANPR**
     - Non ancora supportato.
     - |cieid-icon|
   * - **https://attributes.eid.gov.it/physical_phone_number**
     - Telefono fisico preferito dell'utente. Si RACCOMANDA di usare il formato dato
       in `E164`_ ad esempio +1 (425) 555-1212 o +56 (2) 687 2400. Se il numero di telefono contiene un'estensione, si RACCOMANDA di usare il formato come al :rfc:`3966`, ad esempio +1 (604) 555-1234;ext=5678.
     - |cieid-icon|


.. note::
   
   Usando lo scope **openid** non si ottengono Claim Utente, se non specificati nel parametro claims. 
   Solo il valore **sub** viene incluso.
   Si POSSONO usare valori multipli dello scope, creando una lista "case sensitive" di valori ASCII delimitati da spazi. 
   Claim Utente individuali possono essere richiesti usando il parametro di richiesta **claims** (vedere :ref:`Parametro Claims <claims_parameter>`). 
   Usare il parametro **claims** è l'unico modo per richiedere specifiche combinazioni di Claim Utente che non possono
   essere specificati usando valori di scope. 
   Il parametro OIDC *claims* definisce un meccanismo per richiedere esplicitamente i Claim Utente da restituire
   dall'**UserInfo Endpoint** e/o nell'**ID Token**. 
   I membri top-level dell'Oggetto JSON della richiesta **claims** sono:


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **userinfo**
     - Richiede che i claim della lista siano ritornati dall'**UserInfo Endpoint**. 
       Se presenti, i claim della lista vengono aggiunti agli altri claim richiesti usando valori scope. 
       Se non sono presenti, i claim restituiti dall'UserInfo Endpoint saranno solo quelli richiesti usando i valori scope.
     - |cieid-icon|
   * - **id_token**
     - Richiede che i claim della lista siano ritornati nell'**ID Token**. 
       Se presenti, i claim della lista vengono aggiunti ai claim di default dell'ID Token. 
       Se non sono presenti, vengono richiesti i claim di default dell'ID Token.
     - |cieid-icon|

Il RP può solo chiedere **given_name**, **family_name**, **birthdate** e **fiscal_number** 
nell'**id_token object** del parametro **claim**. Gli altri claim riportati DEVONO essere richiesti nell'oggetto **userinfo** del parametro **claim**.

Se viene omessa la richiesta **claims** e lo scope è uguale a **openid**, l'OP DOVREBBE fornire solo
il claim **sub** valorizzato a **pairwise**.
Pe motivi di privacy, i claim necessari DOVREBBERO essere richiesti esplicitamente dal RP nell'Authorization Request.

I claim richiesti nei parametri di scope vengono ritornati sia nella risposta userinfo, che nell'ID Token. 



.. _claims_parameter:

Parametro claims
^^^^^^^^^^^^^^^^

Il parametro OIDC **claims** definisce un meccanismo per richiedere esplicitamente i claim utente 
dall'**UserInfo Endpoint** e/o nell'**ID Token**.
Il valore è un Oggetto JSON che fa una lista dei claim richiesti da queste due posizioni.

CIE OIDC permette l'uso di questo parametro sia per gli elementi "userinfo" che per quelli "id_token" del parametro **claims**. Perciò gli attributi CIE possono essere richiesti sia dentro gli elementi "userinfo" che in quelli "id_token", facendo una lista degli attributi richiesti come chiave dell'oggetto JSON e indicando i loro valori come ``{"essential":true}``, ``{"value":"string"}``, ``{"values":[string1,string2]}``, ``null`` per indicare rispettivamente che il claim è essenziale, da ritornare con un valore specifico, da ritornare con un insieme di valori e da ritornare in modalità default, rispettivamente.

.. code-block::

   {
       "userinfo":{
           "family_name":null
       },
       "id_token":{
           "email":{
               "essential":true
           }
       }
   }

