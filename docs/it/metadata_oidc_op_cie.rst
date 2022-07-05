.. include:: ./common_definitions.rst


.. _claim_OP_CIE:


OpenID Connect Provider Metadata (OP) per CIE
+++++++++++++++++++++++++++++++++++++++++++++

Segue la tabella dei claim specifici  per la Federazione CIE.

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **scopes_supported**
     - JSON Array che contiene una lista di valori degli scope supportati dall'OP.
     - |check-icon| 
   * - **grant_types_supported**
     - JSON Array che contiene una lista dei valori di *grant_types* supportati dall'OP. I valori ammessi sono
       *refresh_token* e *authorization_code*
     - |check-icon|
   * - **tls_client_certificate_bound_access_tokens**
     - Valore booleano che specifica se l'OP supporta l'uso dei Token **mTLS bound**. Deve valere *true*
     - |check-icon| 
   * - **authorization_response_iss_parameter_supported**
     - Valore booleano che specifica se l'OP fornisce il parametro **iss** nell'Authorization Response. Deve valere *true*
     - |check-icon|
   * - **claims_supported**
     - JSON Array che contiene una lista di claim che l'OP supporta. Vedere allo scopo i :ref:`Claim Utente CIE <claim_utente_CIE>` al prossimo paragrafo `
     - |check-icon|



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
     - **Obbligatorio**
   * - **given_name**
     - Nome proprio dell'utente. Nel caso di nomi multipli, separarli da spazi.
     - |check-icon|
   * - **family_name**
     - Cognome dell'utente. Nel caso di cognomi multipli, separarli da spazi.
     - |check-icon|
   * - **email**
     - Indirizzo email preferito dell'utente. DEVE essere conforme alla sintassi specificata in :rfc:`5322`. 
       Il RP NON DEVE basarsi sull'univocità di questo valore, come discusso in [OIDC.Core#section-5.7]
     - |check-icon|
   * - **email_verified**
     - Valore booleano che indica se l'indirizzo email  dell'utente è stato verificato. 
       Quando vale *true*, significa che l'OP ha compiuto passi significativi per assicurarsi che l'utente
       abbia già svolto la verifica, al momento in cui questo controllo è stato effettuato. 
       La misura in cui un indirizzo email è considerato verificato, dipende dal contesto e dalla struttura 
       della fiducia o dell'accordo contrattuale con il quale le parti operano.
     - |check-icon|
   * - **gender**
     - String per il genere dell'utente. Si possono usare i valori *maschio*, *femmina* o anche altri.
     - |uncheck-icon|
   * - **birthdate**
     - Campo data che indica la data di nascita dell'utente necondo il formato AAAA-MM-GG. 
       L'anno può anche essere 0000, indicando così che il valore è omesso. È permesso rappresentare anche solo
       l'anno nel formato AAAA. Notare che, a seconda della piattaforma sottostante, l'indicazione del solo anno potrebbe comportare valori variabili per il giorno ed il mese, rendendo necessario fare attenzione quando si
       elaborano le date.
     - |uncheck-icon|
   * - **phone_number**
     - String che indica il numero di telefono preferito dell'utente. Si RACCOMANDA di usare il formato dato
       in `E164`_ ad esempio +1 (425) 555-1212 o +56 (2) 687 2400. Se il numero di telefono contiene un'estensione,
       si RACCOMANDA di usare il formato come al :rfc:`3966`, ad esempio +1 (604) 555-1234;ext=5678.
     - |uncheck-icon|
   * - **phone_number_verified**
     - Valore booleano che indica se il numero di telefono mobile è stato verificato. 
       Quando vale *true*, significa che l'OP ha compiuto passi significativi per assicurarsi che l'utente
       abbia già svolto la verifica, al momento in cui questo controllo è stato effettuato. 
       Significa inoltre che il formato DEVE essere come in `E164`_ e le estensioni come in :rfc:`3966`.
     - |check-icon|
   * - **address**
     - Indirizzo postale preferito dell'utente. È un Oggetto JSON :rfc:`4627` contenente gli attributi seguenti:
       
       **street_address**: indirizzo completo contenente numero civico, via, casella postale.

       **locality**: città o località

       **region**: stato, provincia, prefettura o regione.

       **postal_code**: codice postale o zip code

       **country**: String che denota il codice del paese come in ISO 3166-1 alpha-2, es., "IT".
     - |uncheck-icon|



Claim Utente da OpenID Connect Identity Assurance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Claim Utente da OpenID Connect Identity Assurance
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **place_of_birth**
     - Luogo di nascita dell'utente. È un Oggetto JSON :rfc:`4627` contenente alcuni o tutti 
       gli attributi seguenti:
       
       **country**: String che denota il codice del paese come in ISO 3166-1 alpha-2, es., "DE".

       **region**: stato, provincia, prefettura o regione. Questo campo può essere obbligatorio in alcune giurisdizioni.

       **locality**: città o località
     - |uncheck-icon|
   * - **document_details**
     - Oggetto JSON che rappresenta il documento. L'unico documento supportato alla data è la CIE.
       Contiene i seguenti claim:
       
       **type**: String che denota il tipo di documento. L'unico valore supportato è "cie"

       **document_number**: String che rappresenta un identificativo che definisce univocamente la CIE dell'utente.

       **date_of_issuance**: data del documento in formato AAAA-MM-GG (ISO `ISO8601-2004`_ )

       **date_of_expiry**: data di scadenza in formato AAAA-MM-GG (ISO `ISO8601-2004`_ )

       **issuer**: Oggetto JSON contenente le informazioni dell'emittente della CIE. Questo oggetto ha le seguenti proprietà:
       
         **name**: nome dell'emittente della CIE. Questo campo è sempre valorizzato con la String 
         "mint" (Ministero dell'Interno)

         **country_code**: st String che denota il Paese o l'organizzazione sovranazionale che ha emesso il documento,
         come da codici di 3 lettere ISO 3166/ICAO `ICAO-Doc9303`_, es. "ITA".
     - |uncheck-icon|


Claim Utente specifici per CIEid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Claim Utente specifici per CIEid
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **e_delivery_service**
     - String che indica il servizio di consegna elettronica preferito dall'utente,
       come presentato in EIDAS e CAD.
     - |uncheck-icon|
   * - **fiscal_number**
     - Codice fiscale dell'utente. String di 16 caratteri. 
     - |uncheck-icon|
   * - **idANPR**
     - Non ancora supportato.
     - |uncheck-icon|
   * - **physical_phone_number**
     - Telefono fisico preferito dell'utente. Si RACCOMANDA di usare il formato dato
       in `E164`_ ad esempio +1 (425) 555-1212 o +56 (2) 687 2400. Se il numero di telefono contiene un'estensione,
       si RACCOMANDA di usare il formato come al :rfc:`3966`, ad esempio +1 (604) 555-1234;ext=5678.
     - |uncheck-icon|


Per favorire la minimizzazione dei dati, al posto di condividere un insieme fisso di **Claim Utente** con gli **RP**, 
i Claim Utente necessari possono essere richiesti dall'**RP** stesso nell'**Authorization Request** usando lo scope del
claim **claims**.

Sulla base dello scope scelt, l'OP restituisce un insieme predefinito di Claim Utente CIE OIDC definisce i 
seguenti valori dello **scope** da usare per richiedere i Claim:

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **profile**
     - Questo valore richiede l'accesso ai Claim di default del profilo dell'utente finale, 
       che nello scenario CIE OIDC corrisponde al minimo dataset di eIDAS (es. cognome, nome, codice fiscale, data di nascita)
     - |uncheck-icon|
   * - **email**
     - Questo valore richiede laccesso all'**email** e **email_verified**
     - |uncheck-icon|

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
     - **Obbligatorio**
   * - **userinfo**
     - Richiede che i claim della lista siano ritornati dall'**UserInfo Endpoint**. 
       Se presenti, i claim della lista vengono aggiunti agli altri claim richiesti usando valori scope. 
       Se non sono presenti, i claim restituiti dall'UserInfo Endpoint saranno solo quelli richiesti usando i valori scope.
     - |uncheck-icon|
   * - **id_token**
     - Richiede che i claim della lista siano ritornati nell'**ID Token**. 
       Se presenti, i claim della lista vengono aggiunti ai claim di default dell'ID Token. 
       Se non sono presenti, vengono richiesti i claim di default dell'ID Token.
     - |uncheck-icon|

Nello scenario CIE OIDC l'RP può solo chiedere **given_name**, **family_name**, **birthdate** e
**fiscal_number** nell'**id_token object** del parametro **claim**.
Gli altri claim riportati DEVONO essere richiesti nell'oggetto **userinfo** del parametro **claim**.



.. _claims_parameter:

Parametro claims
^^^^^^^^^^^^^^^^

Il parametro OIDC **claims** definisce un meccanismo per richiedere esplicitamente i claim utente 
dall'**UserInfo Endpoint** e/o nell'**ID Token**.
Il valore è un Oggetto JSON che fa una lista dei claim richiesti da queste due posizioni.

Se viene omessa la richiesta **claims** e lo scope è uguale a **openid**, l'OP DOVREBBE fornire un insieme
di default di claim che ha disponibile per il soggetto (in CIE OIDC corrisponde al minimo dataset di eIDAS) nella 
risposta **userinfo**, mentre l'**id_token** conterrà solo il claim **sub** valorizzato a **pairwise**.

CIE OIDC permette l'uso di questo parametro sia per gli elementi "userinfo" che per quelli "id_token" del parametro **claims**. Perciò gli attributi CIE possono essere richiesti sia dentro gli elementi "userinfo" che in quelli "id_token", facendo una lista degli attributi richiesti come chiave dell'oggetto JSON e indicando i loro valori come ``{"essential":true}``, ``{"value":"string"}``, ``{"values":[string1,string2]}``, ``null`` per indicare rispettivamente che il claim è essenziale, da ritornare con un valore specifico, da ritornare con un insieme di valori e da ritornare in modalità default (un claim volontario), rispettivamente.

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

