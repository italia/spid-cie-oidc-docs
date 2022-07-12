.. include:: ./common_definitions.rst

OpenID Connect Relying Party Metadata (RP)
++++++++++++++++++++++++++++++++++++++++++

È il Metadata che i RP pubblicano con l'identificativo **openid_relying_party**, come segue.

.. code-block:: 

 {
     "metadata":{
         "openid_relying_party":{
             ...
         }
     }
 }


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da** 
   * - **client_registration_types**
     - Array di stringhe che specifica i tipi supportati dalla Federazione (solo *automatic*)
     - |spid-icon| |cieid-icon|
   * - **organization_name**
     - Un nome leggibile che rappresenta l'organizzazione proprietaria del RP. 
     - |spid-icon| |cieid-icon| 
   * - **signed_jwks_uri**
     - Un URL HTTP che punta a un JWT firmato che ha come payload il JWK Set dell'entità (vedere esempio sotto).
       Il JWT è firmato con una chiave inclusa nel JWK che l'entità ha pubblicato nel suo Entity Statement autofirmato.
       Se un RP può usare **signed_jwks_uri**, NON DEVE usare **jwks** o **jwks_uri**. Un JWT firmato può
       contenere i seguenti claim, escluse le chiavi definite in `:rfc:7519`:

       **keys**: Lista dei JWK. OBBLIGATORIO.

       **iss**: "iss" (emettitore) identifica l'emettitore del JWT. OBBLIGATORIO.
 
       **sub**: Identifica il proprietario delle chiavi. DOVREBBE coincidere con l'emettitore. OBBLIGATORIO.

       **iat**: UNIX Timestamp con l'istante di emissione del JWT. FACOLTATIVO.

       **exp**: UNIX Timestamp con l'istante di scadenza del JWT. FACOLTATIVO.

     - |spid-icon| |cieid-icon| 
   * - **jwks**
     - JSON Web Key Set |br|
       :rfc:`7517#appendix-A.1` |br|
       Obbligatorio in assenza del claim **signed_jwks_uri**. 
     - |spid-icon| |cieid-icon| 
   * - **client_id**
     - URI che identifica univocamente il RP.
     - |spid-icon| |cieid-icon|
   * - **redirect_uris**
     - Array di URI di redirezione utilizzati dal client (RP). Deve esserci un match esatto tra uno degli URI
       nell'array e quello utilizzato nell'Authentication request. Non è ammesso l'uso dello schema http (è
       obbligatorio HTTPS); tuttavia gli URI possono seguire eventuali schemi custom (ad es. myapp://) al 
       fine di supportare applicazioni mobili.
       *Alla luce della normativa vigente in tema di protezione dei dati personali, è opportuno che
       l'URL non contenga informazioni utili ad individuare lo specifico servizio a cui l'utente
       intende accedere. Si raccomanda dunque di reindirizzare verso un sistema di access
       management che a sua volta rimanderà l'utente allo specifico servizio*.
     - |spid-icon| |cieid-icon|
   * - **client_name**
     - Nome del RP da visualizzare nelle schermate di autenticazione e richiesta di consenso. 
       Può essere specificato in più lingue apponendo al nome dell'elemento il suffisso "#" seguito 
       dal codice :rfc:`5646`. Un nome di default senza indicazione della lingua è sempre presente.
     - |spid-icon| |cieid-icon|
   * - **response_types**
     - Array dei valori di response_type previsti da OAuth 2.0 che il client userà nelle richieste di autenticazione.
       Deve contenere il solo valore **code**.
     - |spid-icon| |cieid-icon|
   * - **grant_types**
     - Array dei valori di **grant_type** previsti da OAuth 2.0 che il client userà nelle richieste al
       **Token Endpoint**. Deve contenere i soli valori **authorization_code** e **refresh_token**.
     - |spid-icon| |cieid-icon|
   * - **userinfo_signed_response_alg**
     - `JWS`_ alg algorithm `JWA`_ OBBLIGATORIO per firmare le :ref:`UserInfo Response<userinfo_response>`. 
       Se specificato, la UserInfo Response sarà `JWT`_ serialized, e firmata usando `JWS`_. 
       Se viene omesso, UserInfo Response ritorna come default i claim come JSON Object codificato UTF-8 usando il content-type application/json.
     - |spid-icon| |cieid-icon|
   * - **userinfo_encrypted_response_alg**
     - `JWE`_ alg algorithm `JWA`_ OBBLIGATORIO per cifrare le :ref:`UserInfo Response<userinfo_response>`. 
       Se vengono richieste sia la firma che la cifratura, la UserInfo Response sarà firmata e poi cifrata,
       con il risultato come Nested JWT, come definito in `JWT`_. 
       Il default, se omesso, è che non viene eseguita la cifratura.
     - |spid-icon| |cieid-icon|
   * - **userinfo_encrypted_response_enc**
     - `JWE`_ enc algorithm `JWA`_ OBBLIGATORIO per cifrare le :ref:`UserInfo Response<userinfo_response>`.
       Se **userinfo_encrypted_response_alg** viene specificato, il default per questo valore è ``A128CBC-HS256``. 
       Quando **userinfo_encrypted_response_enc** viene incluso, anche **userinfo_encrypted_response_alg** DEVE essere presente.
     - |spid-icon| |cieid-icon|

Vedere `OIDC-FED#RP_metadata`_


.. _example_of_signed_jwks:

Esempio non normativo di JWKS firmato
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il seguente è un esempio non normativo di JWKS firmato, prima della serializzazione e della firma.

.. code-block::

  {
      "keys":[
          {
              "kty":"RSA",
              "kid":"SUdtUndEWVY2cUFDeDV5NVlBWDhvOXJodVl2am1mNGNtR0pmd",
              "n":"y_Zc8rByfeRIC9fFZrDZ2MGH2ZnxLrc0ZNNwkNet5rwCPYeRF3Sv5nihZA9NHkDTEX97dN8hG6ACfeSo6JB2P7heJtmzM8oOBZbmQ90nEA_JCHszkejHaOtDDfxPH6bQLrMlItF4JSUKua301uLB7C8nzTxmtF3eAhGCKn8LotEseccxsmzApKRNWhfKDLpKPe9i9PZQhhJaurwDkMwbWTAeZbqCScU1o09piuK1JDf2PaDFevioHncZcQO74Obe4nN3oNPNAxrMClkZ9s9GMEd5vMqOD4huXlRpHwm9V3oJ3LRutOTxqQLVyPucu7eHA7her4FOFAiUk-5SieXL9Q",
              "e":"AQAB"
          },
          {
              "kty":"EC",
              "kid":"MFYycG1raTI4SkZvVDBIMF9CNGw3VEZYUmxQLVN2T21nSWlkd3",
              "crv":"P-256",
              "x":"qAOdPQROkHfZY1daGofOmSNQWpYK8c9G2m2Rbkpbd4c",
              "y":"G_7fF-T8n2vONKM15Mzj4KR_shvHBxKGjMosF6FdoPY"
          } 
      ],
      "iss":"https://example.org/op",
      "iat":1618410883
  }


