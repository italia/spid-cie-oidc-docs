.. include:: ../common/common_definitions.rst

Authorization endpoint (Authentication)
---------------------------------------

Request
+++++++

Per avviare il processo di autenticazione, il RP reindirizza l'utente all'*Authorization Endpoint* dell'OP selezionato, inviando una richiesta *HTTP* contenente il parametro **request** in formato **JWT** firmato e contenente l'*Authorization Request* firmata dal RP.

Per veicolare la richiesta, il RP PUÒ utilizzare i metodi **POST** e **GET**. Mediante il metodo **POST** i parametri DEVONO essere trasmessi utilizzando la *Form Serialization*. 
Mediante il metodo **GET** i parametri DEVONO essere trasmessi utilizzando la *Query String Serialization*. Per maggiori dettagli vedi `OpenID.Core#Serializations`_.

.. warning::
  Il parametro **scope** DEVE essere trasmesso sia come parametro nella chiamata HTTP sia all'interno dell'oggetto request e i loro valori DEVONO corrispondere.

  |cieid-icon|
  I parametri **client_id** e **response_type** DOVREBBERO essere trasmessi sia come parametri sulla chiamata HTTP sia all'interno dell'oggetto request.

  |spid-icon|
  I parametri **client_id** e **response_type** DEVONO essere trasmessi sia come parametri sulla chiamata HTTP sia all'interno dell'oggetto request e i loro valori DEVONO corrispondere, in caso contrario solo i parametri all’interno dell’oggetto request DEVONO essere considerati.

.. seealso:: 

   - :ref:`Esempio di Authorization Request <Esempio_EN6>`

Di seguito i parametri obbligatori nella richiesta di autenticazione *HTTP*.

.. _tabella_parametri_authz_req: Authorization request

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Supportato da**
  * - **scope**
    - Riporta di valori di *scope* supportati dall'OP e definiti dal parametro **scopes_supported** nel :ref:`Metadata OP <MetadataOP>`. DEVE essere presente almeno il valore *openid*.
    - |spid-icon| |cieid-icon|
  * - **code_challenge**
    - Vedi :rfc:`7636#section-4.2`.
    - |spid-icon| |cieid-icon|
  * - **code_challenge_method**
    - Come definito dal parametro **code_challenge_methods_supported** nel :ref:`Metadata OP <MetadataOP>`.
    - |spid-icon| |cieid-icon|
  * - **request**
    - Vedi `OpenID.Core#JWTRequests`_. DEVE essere un **JWT** firmato.
    - |spid-icon| |cieid-icon|

Di seguito una tabella che riporta la composizione dell'header del **JWT**.

.. _tabella_jwt_header_authz_req: Authorization request JWT header

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Jose Header**
    - **Descrizione**
    - **Supportato da**
  * - **alg**
    - Vedi :rfc:`7516#section-4.1.1`. Vedi :ref:`supported_algs`..
    - |spid-icon| |cieid-icon|
  * - **kid**
    - Vedi :rfc:`7638#section_3`. 
    - |spid-icon| |cieid-icon|

.. note::
  Il parametro **typ** se omesso assume il valore implicito di **JWT**.


Il payload del **JWT** contiene i seguenti parametri obbligatori.

.. _tabella_jwt_payload_authz_req: Authorization request

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **client_id**
     - Vedi `OpenID.Registration`_. DEVE essere valorizzato con un HTTPS URL che identifica univocamente il RP.
     - |spid-icon| |cieid-icon|
   * - **code_challenge**
     - Come definito nella  :ref:`Tabella dei parametri HTTP <tabella_parametri_http_req>`.
     - |spid-icon| |cieid-icon|
   * - **code_challenge_method**
     - Come definito nella  :ref:`Tabella dei parametri HTTP <tabella_parametri_http_req>`.
     - |spid-icon| |cieid-icon|
   * - **nonce**
     - Vedi `OpenID.Core#AuthRequest`_. DEVE essere una stringa casuale di almeno 32 caratteri alfanumerici. Questo valore sarà restituito nell'ID Token fornito dal Token Endpoint, in modo da consentire al client di verificare che sia uguale a quello inviato nella richiesta di autenticazione.
     - |spid-icon| |cieid-icon|
   * - **prompt**
     - Vedi `OpenID.Core#AuthRequest`_. I valori consentiti sono:
       
       **consent**: Se non è già attiva una sessione di Single Sign-On, 
       l'OP fa una richiesta di autenticazione all'utente.
       Quindi chiede il consenso al trasferimento degli attributi. 

       **consent login**: l'OP forza una richiesta di autenticazione all'utente.
       Quindi chiede il consenso al trasferimento degli attributi. 

     - |spid-icon| |cieid-icon|
   * - **redirect_uri**
     - Vedi `OpenID.Core#AuthRequest`_. DEVE essere una URL indicata nel :ref:`Metadata RP <MetadataRP>`. 
     - |spid-icon| |cieid-icon|
   * - **response_type**
     - Vedi `OpenID.Core#AuthRequest`_. Come definito dal parametro **response_types_supported** nel :ref:`Metadata OP <MetadataOP>`.
     - |spid-icon| |cieid-icon|
   * - **scope**
     - Come definito nella  :ref:`Tabella dei parametri HTTP <tabella_parametri_http_req>`.
     - |spid-icon| |cieid-icon|
   * - **acr_values**
     - Vedi `OpenID.Core#AuthRequest`_. Come definito dal parametro **acr_values_supported** nel :ref:`Metadata OP <MetadataOP>`.
       Valori di riferimento della classe di contesto dell'Authentication Request. 
       DEVE essere una stringa separata da uno spazio, che specifica i valori "acr" richiesti in ordine di preferenza. L'OP PUÒ utilizzare un'autenticazione ad un livello più alto di quanto richiesto. Tale scelta non DEVE comportare un esito negativo della richiesta.
     - |spid-icon| |cieid-icon|
   * - **claims**
     - Vedi `OpenID.Core#ClaimsRequestParameter`_. Vedi Sezione "Parametri scope e claims".
     - |spid-icon| |cieid-icon|
   * - **state**
     - Vedi `OpenID.Core#AuthRequest`_. DEVE essere una stringa casuale di almeno 32 caratteri alfanumerici. Identificativo univoco della sessione lato RP. Questo valore verrà restituito al client nella risposta al termine dell'autenticazione.
     - |spid-icon| |cieid-icon|
   * - **exp**
     - UNIX Timestamp con l'istante di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **iat**
     - UNIX Timestamp con l'istante di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **iss**
     - DEVE corrispondere al *client_id*. 
     - |spid-icon| |cieid-icon|
   * - **aud**
     - DEVE corrispondere all'identificativo del OP (parametro *issuer* presente nel :ref:`Metadata OP <MetadataOP>`.)
     - |spid-icon| |cieid-icon|
   * - **ui_locales**
     - Lingue preferibili per visualizzare le pagine dell’OP. L’OP può ignorare questo parametro se non dispone di nessuna delle lingue indicate. Lista di codici RFC5646 separati da spazi.
     - |spid-icon| |cieid-icon|

.. note::
  **PKCE** è un'estensione del protocollo *OAuth 2.0* prevista anche nel profilo *iGov* (`International Government Assurance Profile for OAuth 2.0 <https://openid.net/specs/openid-igov-oauth2-1_0-03.html#Section-3.1.7>`_) e finalizzata ad evitare un potenziale attacco attuato con l'intercettazione dell'*authorization code*. Consiste nella generazione di un codice (**code verifier**) e del suo hash (**code challenge**). Il **code challenge** viene inviato all'OP nella richiesta di autenticazione. 
  
  Quando il RP contatta il *Token Endpoint* al termine del flusso di autenticazione, invia il **code verifier** originariamente creato, in modo che l'OP possa confrontare che il suo hash corrisponda con quello acquisito nella richiesta di autenticazione.

  Di seguito un script Python di esempio per generare i parametri richiesti.

  .. literalinclude :: ../../static/pkce.py
   :language: python


.. _parametri_scope_claims:

Parametri **scope** e **claims**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: |spid-icon|

  Gli attributi dell'utente POSSONO essere richiesti dal RP nell'Authorization Request usando il parametro **claims**.

  Non è possibile richiedere attributi SPID nell' ID Token. Gli attributi dell'utente sono disponibili all'interno della response dello UserInfo endpoint.



.. admonition:: |cieid-icon|

  Gli attributi dell'utente POSSONO essere richiesti dal RP nell'Authorization Request usando i parametri **scope** o **claims**.


  Nel caso di utilizzo del parametro **scope** i seguenti valori sono supportati:

  - **profile**: usando questo valore è possibile ottenere il profilo utente di default che corrisponde al Minimum Dataset eIDAS: 

      - *family_name*, 
      - *given_name*,
      - *birthdate*, 
      - *\https://attributes.eid.gov.it/fiscal_number* (National Unique Identifier).

  - **email**: questo valore permette di ottenere, se resi disponibili dall'utente, i seguenti attributi:

      - *email*,
      - *email_verified*.

  Il parametro **scope** PUÒ contenere uno o più valori separati da uno spazio. Ad esempio l'utilizzo congiunto di *profile* e *email* permette di ottenere l'unione degli insiemi degli attributi (Minimum Dataset eIDAS e l'email).
  Nel caso di richiesta di singoli attributi dell'utente o specifiche combinazioni di essi, Il RP DOVREBBE usare il parametro **claims**.

  Gli attributi richiesti tramite il parametro **scope** sono disponibili sia nell'ID Token e sia nella risposta allo *userinfo endpoint*.

  .. warning::

    Quando il parametro **scope** contiene solo il valore **openid** e il parametro **claims** non è presente oppure non è valorizzato, la response dello userinfo endpoint NON DEVE contenere nessun attributo utente ma soltanto il claim *sub*.

Per la definizione del parametro **claims** e la modalità di utilizzo per la richiesta degli attributi dell'utente si può fare riferimento a `OpenID.Core#ClaimsParameter`_.


Response
++++++++

Un'Authentication response è un messaggio di risposta di autorizzazione OAuth 2.0
restituito dall'authorization endpoint dell'OpenID Provider (OP) al termine del flusso di
autenticazione. L'OP reindirizzerà l'utente all'url contenuto nel parametro redirect_uri specificato nella richiesta di autorizzazione, aggiungendo i parametri della risposta.

.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-4.1.2
 - https://openid.net/specs/openid-connect-core-1_0.html#AuthRequestValidation

Se l'autenticazione è avvenuta con successo, l'OpenID Provider (OP),
reindirizza l'utente aggiungendo i seguenti parametri obbligatori come query parameters al *redirect_uri* (come definito in `OpenID.Core#AuthResponse`_):

.. _tabella_authz_res: Authorization response

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **code**
     - Codice univoco di autorizzazione (*Authorization Code*) che il client può passare al Token Endpoint per ottenere un ID Token e un Access Token. Questo ha il vantaggio di non esporre alcun token allo User Agent o a malware che controllano questo. 
     - |spid-icon| |cieid-icon|
   * - **state**
     - Valore state incluso nell'*Authentication Request*. Il client è tenuto a verificarne la corrispondenza. Deve essere lo stesso valore indicato dal client nella Authorization Request.
     - |spid-icon| |cieid-icon|
   * - **iss**
     - Identificatore univoco dell'OP che ha creato l'Authentication Response. Il RP DEVE validare 
       questo parametro e NON DEVE permettere a più OP di usare lo stesso identificatore.
     - |cieid-icon|


Esempio di Authorization Response dell'OP:

  .. code-block:: http

    http://rp-test.it/oidc/rp/callback/?code=a032faf23d986353019ff8eda96cadce2ea1c368f04bf4c5e1759d559dda1c08056c7c4d4e8058cb002a0c8fa9a920272350aa102548523a8aff4ccdb44cb3fa&state=2Ujz3tbBHWQEL4XPFSJ5ANSjkhd7IlfC&iss=http%3A%2F%2Fop-test%2Foidc%2Fop%2F


Gestione degli errori
+++++++++++++++++++++

In caso di errore, l'OP o il RP rappresentano i messaggi di anomalia relativi agli scambi OpenID
Connect, come descritti nelle relative tabelle definite dalle `Linee Guida UX SPID`_.

.. _tabella_authz_errs_res: Authorization response errors

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **Errore**
     - Vedi :ref:`Codici di errori <codici_errore>`
     - |spid-icon| |cieid-icon|
   * - **Descrizione dell'errore**
     - Descrizione più dettagliata dell'errore, finalizzata ad aiutare lo sviluppatore per eventuale debugging. Questo messaggio non è 
       destinato ad essere visualizzato all'utente (a tal fine si faccia riferimento alle `Linee Guida UX SPID`_)
     - |spid-icon| |cieid-icon|
   * - **state**
     - Parametro obbligatorio solo nel caso di risposta di errore alla *Authentication Request* e DEVE essere uguale al valore *state* incluso nella *Authentication Request*.  Il RP DEVE verificare che corrisponda a quello inviato nella *Authentication Request*.
     - |spid-icon| |cieid-icon|


.. _codici_errore:

Codici di errore
^^^^^^^^^^^^^^^^

.. _tabella_authz_errs: Authorization errors


.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Errore**
    - **Descrizione**
    - **Codice HTTP**
    - **Supportato da**

  * - *access_denied*
    - L’OP ha negato l’accesso a causa di credenziali non valide o non adeguate al livello SPID richiesto (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *unauthorized_client*
    - Il client non è autorizzato a richiedere un authorization code (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *invalid_request*
    - La richiesta non è valida a causa della mancanza o della non correttezza di uno o più parametri (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *invalid_scope*
    - Sono stati richiesti degli scope non validi (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *server_error*
    - L’OP ha riscontrato un problema interno (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *temporarily_unavailable*
    - L’OP ha riscontrato un problema interno temporaneo (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *unsupported_response_type*
    - Il response_type richiesto non è supportato (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *login_required*
    - L'OP richiede l'autenticazione da parte dell'utente (`OpenID.Core#AuthError`_).
    - *302 Found*
    - |spid-icon| |cieid-icon|
  
  * - *consent_required*
    - L'OP richiede il consenso esplicito da parte dell'utente (`OpenID.Core#AuthError`_).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *request_uri_not_supported*
    - L'OP non supporta l'uso del parametro *request_uri* (`OpenID.Core#AuthError`_).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *registration_not_supported*
    - L'OP non supporta l'uso del parametro *registration* (`OpenID.Core#AuthError`_).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *invalid_request_object*
    - Il parametro *request* contiene un *Request Object* non valido (`OpenID.Core#AuthError`_).
    - *302 Found*
    - |spid-icon| |cieid-icon|


.. warning::

  In caso di URI di reindirizzamento non valido, non corrispondente o mancante, l'OP restituisce *400 Bad Request* come codice HTTP.  


