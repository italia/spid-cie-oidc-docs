.. include:: ../common/common_definitions.rst

Authorization endpoint (Authentication)
---------------------------------------

Request
+++++++

Per avviare il processo di autenticazione, il RP reindirizza l'utente all'*Authorization Endpoint* dell'OP selezionato, inviando una richiesta *HTTP* contenente il parametro **request** un oggetto in formato **JWT** che contiene l'*Authorization Request* firmata dal RP.

Per veicolare la richiesta, il RP PUÒ utilizzare i metodi **POST** e **GET**. Mediante il metodo **POST** i parametri DEVONO essere trasmessi utilizzando la *Form Serialization*. 
Mediante il metodo **GET** i parametri DEVONO essere trasmessi utilizzando la *Query String Serialization*. Per maggiori dettagli vedi `OpenID.Core#Serializations`_.

.. warning::
  Il parametro **scope** DEVE essere trasmesso sia come parametro nella chiamata HTTP sia all'interno dell'oggetto request e i loro valori DEVONO corrispondere.

  I parametri **client_id** e **response_type** DOVREBBERO essere trasmessi sia come parametri sulla chiamata HTTP sia all'interno dell'oggetto request.

.. seealso:: 

   - :ref:`Esempio di Authorization Request <Esempio_EN6>`

Di seguito i parametri obbligatori nella richiesta di autenticazione *HTTP*.

.. _tabella_parametri_http_req:

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

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Jose Header**
    - **Descrizione**
    - **Supportato da**
  * - **alg**
    - Vedi :rfc:`7516#section-4.1.1`. DEVE essere valorizzato con uno dei valori presenti nel parametro **request_object_encryption_alg_values_supported** nel :ref:`Metadata OP <MetadataOP>`.
    - |spid-icon| |cieid-icon|
  * - **kid**
    - Vedi :rfc:`7638#section_3`. 
    - |spid-icon| |cieid-icon|

.. note::
  Il parametro **typ** se omesso assume il valore implicito di **JWT**.


Il payload del **JWT** contiene i seguenti parametri obbligatori.


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

.. note::
  **PKCE** è un'estensione del protocollo *OAuth 2.0* prevista anche nel profilo *iGov* (`International Government Assurance Profile for OAuth 2.0 <https://openid.net/specs/openid-igov-oauth2-1_0-03.html#Section-3.1.7>`_) e finalizzata ad evitare un potenziale attacco attuato con l'intercettazione dell'*authorization code*. Consiste nella generazione di un codice (**code verifier**) e del suo hash (**code challenge**). Il **code challenge** viene inviato all'OP nella richiesta di autenticazione. 
  
  Quando il RP contatta il *Token Endpoint* al termine del flusso di autenticazione, invia il **code verifier** originariamente creato, in modo che l'OP possa confrontare che il suo hash corrisponda con quello acquisito nella richiesta di autenticazione.

  Di seguito un script Python di esempio per generare i parametri richiesti.

  .. literalinclude :: ../../static/pkce.py
   :language: python

..
  FIXME: Fatta sezione ad hoc per le modalità di utilizzo dei parametri claims e scope	 
  Claim
  +++++

  Il parametro claims definisce gli attributi richiesti dal **RP**. Gli attributi SPID sono richiesti all'interno dell'elemento "userinfo", elencando gli attributi da richiedere come chiavi di oggetti JSON, i cui valori devono essere indicati come {"essential": true}. Per SPID non è possibile richiedere attributi nell'id_token, mentre è possibile farlo per CIE. Gli attributi elencati sotto "userinfo" sono disponibili al momento della chiamata allo UserInfo Endpoint.

  .. code-block:: json

  {
      "userinfo":{
          "https://attributes.spid.gov.it/familyName":{
              "essential":true
          }
      }
  }


  .. seealso::

  - https://openid.net/specs/openid-connect-core-1_0.html#IndividualClaimsRequests


.. parametri_scope_claims:

Parametri **scope** e **claims**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Gli attributi richiesti tramite il parametro **scope** sono disponibili sia nell'ID Token e sia nella risposta allo userinfo endpoint.

.. note::
    Il parametro **scope** PUÒ contenere uno o più valori separati da uno spazio. Ad esempio l'utilizzo congiunto di *profile* e *email* permette di ottenere l'unione degli insiemi degli attributi (Minimum Dataset eIDAS e l'email).

Nel caso di richiesta di singoli attributi dell'utente o specifiche combinazioni di essi, Il RP PUÒ usare il parametro **claims**. 
Per la definizione del parametro **claims** e la modalità di utilizzo per la richiesta degli attributi dell'utente si può fare riferimento a `OpenID.Core#ClaimsParameter`_. 

.. warning::
    - Solo per CIE id: Nell'oggetto *id_token* del parametro **claims** è possibile richiedere solo il Minimum Dataset eIDAS. Gli altri attributi dell'utente DEVONO essere richiesti nell'oggetto *userinfo* del parametro **claims**. Inoltre, gli attributi utente richiesti nell'oggetto *id_token* sono disponibili anche allo *userinfo endpoint*. 

.. warning::
    - Se il parametro **claims** non è presente o non è valorizzato, viene restituito solo il claim *sub* nella risposta allo userinfo endpoint. 

La tabella seguente mostra alcuni esempi di utilizzo.

.. list-table:: 
    :widths: 10 10 20 20
    :header-rows: 1

    * - **claims**
      - **scope**
      - **Attributi nella Userinfo Response**
      - **Attributi nell'ID Token**
    * - *userinfo*: \- |br| *id_token*: \-
      - *openid*
      - *sub*
      - *sub*
    * - *userinfo*: \- |br| *id_token*: \-
      - *openid* |br| *profile*
      - *sub*, |br| *given_name*, |br| *family_name*, |br| *birthdate*, |br| *\https://attributes.eid.gov.it/fiscal_number*
      - *sub*, |br| *given_name*, |br| *family_name*, |br| *birthdate*, |br| *\https://attributes.eid.gov.it/fiscal_number*
    * - *userinfo*: \- |br| *id_token*:"birthdate":{essential:true}
      - *openid* 
      - *sub*, |br|  *birthdate*
      - *sub*, |br|  *birthdate*
    * - *userinfo*: \- |br| *id_token*: \-
      - *openid* |br| *email*
      - *sub*, |br| *email*, |br| *email_verified*
      - *sub*, |br| *email*, |br| *email_verified*
    * - *userinfo*:"family_name":null |br| *id_token*:"given_name":{essential:true}
      - *openid* 
      - *sub*, |br|  *given_name*, |br|  *family_name*
      - *sub*, |br|  *given_name*
    * - *userinfo*:\- |br| *id_token*:"birthdate":{essential:true} "gender":{essential:true}
      - *openid* 
      - *sub*, |br|  *birthdate*, |br|  *gender*
      - *sub*, |br|  *birthdate*


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


