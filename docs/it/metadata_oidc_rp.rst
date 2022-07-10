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


Dove un RP non disponesse all'interno dei propri Metadata dei claim **client_registration_types** i valori da intendersi come impliciti sono i seguenti.

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio** 
   * - **client_registration_types**
     - Array di stringhe che specifica i tipi supportati dalla federazione (solo *automatic*)
     - |check-icon| 
   * - **organization_name**
     - Un nome leggibile che rappresenta l'organizzazione proprietaria dell'RP. 
     - |check-icon| 
   * - **jwks**
     - JSON Web Key Set |br|
       :rfc:`7517#appendix-A.1` |br|
       È composto dai seguenti claim:
        
        **kty**: famiglia dell'algoritmo crittografico utilizzato

        **alg**: algoritmo utilizzato

        **use**: utilizzo della chiave pubblica per firma (sig) o encryption (enc)

        **kid**: identificatore univoco della chiave, valorizzato come |br|
        :rfc:`7638`

        **n**: modulo (solo per chiavi RSA)

        **e**: esponente (solo per chiavi RSA)

        **x**: parametro coordinata x (solo per chiavi EC)

        **y**: parametro coordinata y (solo per chiavi EC)

        **crv**: parametro curva (solo per chiavi EC)
     - |check-icon| in assenza del claim **signed_jwks_uri**. 
   * - **client_id**
     - URI che identifica univocamente il RP.
     - |check-icon|
   * - **redirect_uris**
     - Array di URI di redirezione utilizzati dal client (RP). Deve esserci un match esatto tra uno degli URI
       nell'array e quello utilizzato nell'Authentication request. Non è ammesso l'uso dello schema http (è
       obbligatorio HTTPS); tuttavia gli URI possono seguire eventuali schemi custom (ad es. myapp://) al 
       fine di supportare applicazioni mobili.
       *Alla luce della normativa vigente in tema di protezione dei dati personali, è opportuno che
       l'URL non contenga informazioni utili ad individuare lo specifico servizio a cui l'utente
       intende accedere. Si raccomanda dunque di reindirizzare verso un sistema di access
       management che a sua volta rimanderà l'utente allo specifico servizio*.
     - |check-icon|
   * - **client_name**
     - Nome del RP da visualizzare nelle schermate di autenticazione e richiesta di consenso. 
       Può essere specificato in più lingue apponendo al nome dell'elemento il suffisso "#" seguito 
       dal codice :rfc:`5646`. Un nome di default senza indicazione della lingua è sempre presente.
     - |check-icon|
   * - **response_types**
     - Array dei valori di response_type previsti da OAuth 2.0 che il client userà nelle richieste di autenticazione.
       Deve contenere il solo valore **code**.
     - |check-icon|
   * - **grant_types**
     - Array dei valori di **grant_type** previsti da OAuth 2.0 che il client userà nelle richieste al
       **Token Endpoint**. Deve contenere i soli valori **authorization_code** e **refresh_token**.
     - |check-icon|
   * - **userinfo_signed_response_alg**
     - `JWS`_ alg algorithm `JWA`_ OBBLIGATORIO per firmare le :ref:`UserInfo Response<userinfo_response>`. 
       Se specificato, la UserInfo Response sarà `JWT`_ serialized, e firmata usando `JWS`_. 
       Se viene omesso, UserInfo Response ritorna come default i claim come JSON object codificato UTF-8 usando il content-type application/json.
     - |uncheck-icon|
   * - **userinfo_encrypted_response_alg**
     - `JWE`_ alg algorithm `JWA`_ OBBLIGATORIO per cifrare le :ref:`UserInfo Response<userinfo_response>`. 
       Se vengono richieste sia la firma che la cifratura, la UserInfo Response sarà firmata e poi cifrata,
       con il risultato come Nested JWT, come definito in `JWT`_. 
       Il default, se omesso, è che non viene eseguita la cifratura.
     - |uncheck-icon|
   * - **userinfo_encrypted_response_enc**
     - `JWE`_ enc algorithm `JWA`_ OBBLIGATORIO per cifrare le :ref:`UserInfo Response<userinfo_response>`.
       Se **userinfo_encrypted_response_alg** viene specificato, il default per questo valore è ``A128CBC-HS256``. 
       Quando **userinfo_encrypted_response_enc** viene incluso, anche **userinfo_encrypted_response_alg** DEVE essere presente.
     - |uncheck-icon|

Vedere `OIDC-FED#RP_metadata`_
