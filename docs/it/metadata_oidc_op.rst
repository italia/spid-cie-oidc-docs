.. include:: ./common_definitions.rst

OpenID Connect Provider Metadata (OP)
+++++++++++++++++++++++++++++++++++++

È il Metadata che gli OP pubblicano con l'identificativo **openid_provider**, come segue.

.. code-block:: 

 {
     "Metadata":{
         "openid_provider":{
             ...
         }
     }
 }


Se un OP nei propri Metadata non ha i claim **client_registration_types_supported** e/o **request_authentication_methods_supported** i valori da intendersi come impliciti sono i seguenti. 

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **client_registration_types_supported**
     - Array di stringhe che specifica i tipi supportati dalla federazione (solo *automatic*)
     - |check-icon|
   * - **organization_name**
     - Un nome leggibile che rappresenta l'organizzazione proprietaria dell'OP. È inteso per l'utilizzo nell'interfaccia
       utente, per essere riconosciuto dagli utenti finali che usano l'OP per autenticarsi. 

       L'unico metodo di richiesta autenticazione supportato **request_object** per le Richieste di Autorizzazione.

       ..code-block::

        {
            "authorization_endpointer":[
                 "request_object"
            ]
        }
     - |uncheck-icon|
   * - **request_authentication_methods_supported**
     - Un oggetto JSON con membri che rappresentano metodi di richiesta autenticazione e come valori liste di metodi di
       richieste di autenticazione che sono supportati dall'Authorization Endpoint.
     - |uncheck-icon|
   * - **organization_name**
     - Un nome leggibile che rappresenta l'organizzazione proprietaria dell'OP. 
     - |check-icon|
   * - **issuer**
     - URL HTTPS che identifica univocamente l'OP all'interno della Federazione.
     - |check-icon|
   * - **authorization_endpoint**
     - URL HTTPS dell'Authorization Endpoint dell'OP, al quale gli RP sono rediretti per iniziare il flusso 
       di autenticazione.
     - |check-icon|
   * - **token_endpoint**
     - URL HTTPS del Token Endpoint dell'OP, che gli RP devono chiamare per scambiare il codice di autorizzazione 
       per un ID Token, un Access Token ed eventualmente un Refresh Token.
     - |check-icon|
   * - **userinfo_endpoint**
     - URL HTTPS dello UserInfo Endpoint dell'OP, che gli RP possono usare per ottenere informazioni consentite 
       sull'utente autenticato.
     - |check-icon|
   * - **introspection_endpoint**
     - URL HTTPS dell'Introspection Endpoint dell'OP, che può essere usato dagli RP per verificare la validità di 
       un Access Token.
     - |check-icon|
   * - **revocation_endpoint**
     - URL HTTPS del Revocation Endpoint dell'OP, che gli RP possono usare per revocare gli Access Token e/o i Refresh Token già rilasciati.
     - |check-icon|
   * - **jwks**
     - JSON Web Key Set :rfc:`7517#appendix-A.1`
     - |check-icon| in assenza del claim **signed_jwks_uri**. 
   * - **jwks_uri**
     - URL del JSON Web Key Set (JWKS) dell'OP, che contiene la/le chiavi pubbliche di cifratura/decifratura che il RP deve usare.
     - |check-icon|
   * - **signed_jwks_uri**
     - Un URL HTTP che punta a un JWT firmato che ha come payload il JWK Set dell'entità.
       Il JWT è firmato con una chiave inclusa nel JWK che l'entità ha pubblicato nel suo Entity Statement autofirmato.
     - |uncheck-icon|
   * - **response_types_supported**
     - JSON Array che contiene una lista di *response_type* supportati dall'OP.
     - |check-icon|
   * - **response_modes_supported**
     - JSON Array che contiene una lista dei valori dei *response_modes* supportati dall'OP.
     - |check-icon|
   * - **acr_values_supported**
     - Array contenente i livelli SPID supportati dall'OP, rappresentati come URI. 
       Deve contenere per SPID uno o più valori tra i seguenti:
       
       ``https://www.spid.gov.it/SpidL1``
       ``https://www.spid.gov.it/SpidL2``
       ``https://www.spid.gov.it/SpidL3``

       Deve contenere per CIE uno o più valori tra i seguenti:
       
       ``CIE_L1`` |br|
       ``CIE_L2`` |br|
       ``CIE_L3`` 

     - |check-icon| 
   * - **request_object_signing_alg_values_supported**
     - JSON Array contenente gli algoritmi di firma supportati per il JWS dei Request Object. 
       L'OP deve supportare RS256 e può supportare anche altri algoritmi definiti in :rfc:`7518#section3.1`
     - |check-icon|
   * - **request_object_encryption_alg_values_supported**
     - Array contenente gli algoritmi di cifratura (alg) supportati per il JWS dei Request Object, 
       come definito in :rfc:`7518#section4.1`
     - |check-icon|
   * - **request_object_encryption_enc_values_supported**
     - Array contenente gli algoritmi di cifratura (enc) supportati per il JWS dei Request Object, 
       come definito in :rfc:`7518#section-5.1`
     - |check-icon|
   * - **id_token_signing_alg_values_supported**
     - Array contenente gli algoritmi di firma supportati per il JWS dell'ID Token.
       L'OP deve supportare RS256 e può supportare anche altri algoritmi definiti in :rfc:`7518#section-3.1`
     - |check-icon|
   * - **id_token_encryption_alg_values_supported**
     - Array contenente gli algoritmi di cifratura (alg) supportati per il JWS dell'ID Token, come definito
       in :rfc:`7518#section-4.1`
     - |check-icon|
   * - **id_token_encryption_enc_values_supported**
     - Array contenente gli algoritmi di cifratura (enc) supportati per il JWS dell'ID Token, come definito
       in :rfc:`7518#section-5.1`
     - |check-icon|
   * - **userinfo_signing_alg_values_supported**
     - Array contenente gli algoritmi di firma supportati per il JWS dell'UserInfo Endpoint. 
       L'OP deve supportare RS256 e può supportare anche altri algoritmi definiti in :rfc:`7518#section-3.1`
     - |check-icon|
   * - **userinfo_encryption_alg_values_supported**
     - Array contenente gli algoritmi di cifratura (alg) supportati per il JWE dell'UserInfo Endpoint, 
       come definito in :rfc:`7518#section-4.1`
     - |check-icon|
   * - **userinfo_encryption_enc_values_supported**
     - Array contenente gli algoritmi di cifratura (enc) supportati per il JWE dell'UserInfo Endpoint, 
       come definito in :rfc:`7518#section-5.1`
     - |check-icon|
   * - **token_endpoint_auth_methods_supported**
     - Array contenente i metodi di autenticazione supportati dal Token Endpoint. 
       Deve essere presente solo il valore **private_key_jwt**
     - |check-icon|
   * - **request_parameter_supported**
     - Valore booleano che indica se il parametro *request* è supportato dall'OP. Deve essere obbligatoriamente *true*.
     - |check-icon|
   * - **subject_types_supported**
     - Array contenente i tipi di Subject Identifier supportati dall'OP. Deve contenere *pairwise*.
     - |check-icon|
   * - **claims_parameter_supported**
     - Valore booleano chje indica se l'OP supporta l'utilizzo del parametro *claims*. Deve valere *true*
     - |check-icon|
   * - **federation_resolve_endpoint**
     - String. Url presso il quale è possibile ottenere i Trust Mark validati, il Metadata finale e la Trust Chain, 
       relativamente ad un soggetto.
     - |check-icon| 



.. seealso:: 
   - `OpenID.Discovery#OP_Metadata`_



.. toctree:: 
   :maxdepth: 1

   metadata_oidc_op_spid.rst
   metadata_oidc_op_cie.rst
