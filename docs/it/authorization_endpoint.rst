.. include:: ./common_definitions.rst

Authorization Request (Authentication Endpoint)
-----------------------------------------------

Per avviare il processo di autenticazione, l'RP reindirizza l'utente all'*Authorization Endpoint* dell'OP selezionato, inviando una richiesta *HTTP* contenente il parametro **request** un oggetto in formato **JWT** che contiene l'*Authorization Request* firmata dall'RP.

Per veicolare la richiesta, l'RP PUÒ utilizzare i metodi **POST** e **GET**. Mediante il metodo **POST** i parametri DEVONO essere trasmessi utilizzando la *Form Serialization*. 
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
  Il parametro **typ** PUÒ essere omesso nel caso di **JWT**.


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
     - Stringa di almeno 32 caratteri alfanumerici, generata casualmente dal Client e finalizzata a mitigare attacchi replay.
       Questo valore sarà restituito nell'ID Token fornito dal Token Endpoint, in modo da consentire al client di verificare
       che sia uguale a quello inviato nella richiesta di autenticazione.
     - |spid-icon| |cieid-icon|
   * - **prompt**
     - Definisce come l'OP deve richiedere l'autenticazione all'utente.
       
       **consent** (valore consigliato): Se non è già attiva una sessione di Single Sign-On, 
       l'OP fa una richiesta di autenticazione all'utente.
       Quindi chiede il consenso al trasferimento degli attributi. 

       **consent login**: l'OP forza una richiesta di autenticazione all'utente.
       Quindi chiede il consenso al trasferimento degli attributi. 

     - |spid-icon| |cieid-icon|
   * - **redirect_uri**
     - URL dove l'OP reindirizzerà l'utente al termine del processo di autenticazione. 
       Deve essere uno degli URL indicati nel client metadata. 
     - |spid-icon| |cieid-icon|
   * - **response_type**
     - Il tipo di credenziali che deve restituire l'OP.
       **code**
     - |spid-icon| |cieid-icon|
   * - **scope**
     - Come definito nella  :ref:`Tabella dei parametri HTTP <tabella_parametri_http_req>`.
     - |spid-icon| |cieid-icon|
   * - **acr_values**
     - Valori di riferimento della classe di contesto dell'Authentication Request. 
       Stringa separata da uno spazio, che specifica i valori "acr" richiesti al server di autorizzazione per l'elaborazione della richiesta di autenticazione con i valori indicati in ordine di preferenza. L'OP può utilizzare un'autenticazione ad un livello più alto di quanto richiesto.
       Deve contenere per SPID e CIE uno o più valori tra i seguenti:
       
       ``https://www.spid.gov.it/SpidL1``
       ``https://www.spid.gov.it/SpidL2``
       ``https://www.spid.gov.it/SpidL3``
     - |spid-icon| |cieid-icon|
   * - **claims**
     - Lista dei claims (attributi) che un RP intende richiedere. Vedi paragrafo *Claims*
     - |spid-icon| |cieid-icon|
   * - **state**
     - Stringa di almeno 32 caratteri alfanumerici. Identificativo univoco della sessione lato RP. Questo valore verrà restituito al client nella risposta al termine dell'autenticazione. Il valore deve essere significativo esclusivamente per il RP e non deve essere intellegibile ad altri.
     - |spid-icon| |cieid-icon|
   * - **ui_locales**
     - Lista di codici :rfc:`5646` separati da spazi. Lingue preferibili per visualizzare le pagine dell'OP. L'OP può ignorare questo parametro se non dispone di nessuna delle lingue indicate.
     - |spid-icon| |cieid-icon|	
   * - **exp**
     - UNIX Timestamp con l'istante di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **iat**
     - UNIX Timestamp con l'istante di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **iss**
     - String. Uguale a client_id. 
     - |spid-icon| |cieid-icon|
   * - **aud**
     - String. Deve corrispondere all'identificatore del OP.
     - |spid-icon| |cieid-icon|
   * - **typ**
     - Ove fosse assente, viene considerato *JWT* come definito da :rfc:`7519#section-5.1`
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


