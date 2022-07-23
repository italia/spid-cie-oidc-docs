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

  I parametri **client_id** e **response_type** DOVREBBERO essere trasmessi sia come parametri sulla chiamata HTTP sia all'interno dell'oggetto request. In questo caso, i parametri all'interno dell'oggetto request prevalgono su quelli indicati nella chiamata HTTP.

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
     - Vedi `OpenID.Core#AuthRequest`_. Vedi Sezione :ref:`Utilizzo dei parametri scope e claims <parametri_scope_claims>`
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


..
  FIXME: Fatta sezione ad hoc per le modalità di utilizzo dei parametri claims e scope	 
  Claim
  +++++

  Il parametro claims definisce gli attributi richiesti dal **RP**. Gli attributi SPID sono richiesti all'interno dell'elemento "userinfo", elencando gli attributi da richiedere come chiavi di oggetti JSON, i cui valori devono essere indicati come {"essential": true}. Per SPID non è possibile richiedere attributi nell'id_token, mentre è possibile farlo per CIE. Gli attributi elencati sotto "userinfo" sono disponibili al momento della chiamata allo UserInfo Endpoint.

  .. code-block:: 

  {
      "userinfo":{
          "https://attributes.spid.gov.it/familyName":{
              "essential":true
          }
      }
  }


  .. seealso::

  - https://openid.net/specs/openid-connect-core-1_0.html#IndividualClaimsRequests


Response
++++++++

Un'Authentication response è un messaggio di risposta di autorizzazione OAuth 2.0
restituito dall'authorization endpoint dell'OpenID Provider (OP) al termine del flusso di
autenticazione. L'OP reindirizzerà l'utente all'url contenuto nel parametro redirect_uri specificato nella richiesta di autorizzazione, aggiungendo i parametri della risposta.

.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-4.1.2
 - https://openid.net/specs/openid-connect-core-1_0.html#AuthRequestValidation

Se l'autenticazione è avvenuta con successo, l'OpenID Provider (OP),
reindirizza l'utente con i seguenti parametri:


.. code-block:: 

 GET /resp?
 code=usDwMnEzJPpG5oaV8x3j&
 state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd

 Host: https://rp.spid.agid.gov.it
 HTTP/1.1


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
       questo parametro e NON DEVE permettere a più OP di usare lo stesso identificatore. OBBLIGATORIO solo per
       CIE.
     - |cieid-icon|

Errori
++++++

In caso di errore, l'OP visualizza i messaggi di anomalia relativi agli scambi OpenID
Connect descritti nelle relative tabelle definite dalle `Linee Guida UX SPID`_. Nei casi in cui tali linee
guida prescrivono un redirect dell'utente verso il RP, l'OP effettua il redirect verso l'URL indicata
nel parametro redirect_uri della richiesta (solo se valido, ovvero presente nel client metadata), con
i seguenti parametri.

**Esempio:**

.. code-block:: 

 GET /resp?
 error=invalid_request&
 error_description=request%20malformata&
 state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd

 Host: https://rp.spid.agid.gov.it
 HTTP/1.1


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **error**
     - Codice dell'errore
     - |spid-icon| |cieid-icon|
   * - **error_description**
     - Descrizione più dettagliata dell'errore, finalizzata ad aiutare lo sviluppatore per eventuale debugging. Questo messaggio non è 
       destinato ad essere visualizzato all'utente (a tal fine si faccia riferimento alle `Linee Guida UX SPID`_
     - |spid-icon| |cieid-icon|
   * - **state**
     - Valore *state* incluso nella Authentication Request.  Il client è tenuto a verificare che corrisponda a quello inviato nella Authentication Request.
     - |spid-icon| |cieid-icon|


.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-4.1.2.1





