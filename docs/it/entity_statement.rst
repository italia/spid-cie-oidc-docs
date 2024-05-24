.. include:: ../common/common_definitions.rst

.. _Entity_Statement:

Entity Statement
----------------

Il componente basilare per costruire una Catena di Fiducia (Trust Chain) è l'**Entity Statement (ES)**, un JWT firmato che contiene la chiavi pubbliche dell' Entità discendente (subject) e ulteriori dati usati per controllare il processo di risoluzione della Trust Chain. 

Una entità pubblica un **ES** relativo ad un suo discendente presso il proprio :ref:`Fetch Endpoint<federation_endpoint>`. L'entità superiore PUÒ definire le policy sui metadata per un soggetto discendente e pubblicare i TM da lei emessi per questo.



Firma di Entity Statement
+++++++++++++++++++++++++

Si applicano le medesime considerazioni fatte per gli **EC** e riportate nella sezione :ref:`Firma della Entity Configuration<firma_EC>`.


Entity Statement
++++++++++++++++

Gli ES emessi dal TA o da un suo Intermediario per i propri diretti discendenti, DEVONO contenere i seguenti attributi:

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **iss**
     - Si rimanda alla specifica `OIDC-FED`_ Sezione 3.1 per i dettagli.
     - |spid-icon| |cieid-icon|
   * - **sub**
     - Si rimanda alla specifica `OIDC-FED`_ Sezione 3.1 per i dettagli.
     - |spid-icon| |cieid-icon|
   * - **iat**
     - Si rimanda alla specifica `OIDC-FED`_ Sezione 3.1 per i dettagli.
     - |spid-icon| |cieid-icon|
   * - **exp**
     - Si rimanda alla specifica `OIDC-FED`_ Sezione 3.1 per i dettagli.
     - |spid-icon| |cieid-icon|
   * - **jwks**
     - JWKS di Federazione dell'entità *sub*. Si rimanda alla specifica `OIDC-FED`_ Sezione 3.1 per i dettagli.
     - |spid-icon| |cieid-icon|
   * - **metadata_policy**
     - JSON Object che descrive un criterio di Metadata. Ogni chiave dell'oggetto JSON rappresenta un identificatore del tipo di Metadata e ogni valore DEVE essere un oggetto JSON che rappresenta la politica dei Metadata in base allo schema di quel tipo di Metadata. Si rimanda alla specifica `OIDC-FED`_ Section 5.1 per i dettagli implementativi.
     - |spid-icon| |cieid-icon|
   * - **trust_marks**
     - JSON Array contenente i Trust Mark emessi da se stesso per il soggetto discendente.
     - |spid-icon| |cieid-icon|
   * - **constraints**
     - PUÒ contenere il claim **allowed_leaf_entity_types** per restringere i tipi di Entità riconoscobili per il suo discendente (esempio: solo RP).
     - |spid-icon| |cieid-icon|


.. seealso:: 

   - `OIDC-FED#Section_3.1`_
   - :ref:`Esempio non normativo di Entity Statement<Esempio_EN2.1>`

.. _Metadata_Policy:

Metadata Policy
+++++++++++++++

Trust Anchors e Intermediari (SA) DEVONO pubblicare una policy relativa ai rispettivi discendenti nell'Entity Statement ad essi riferito. La Metadata Policy si DEVE applicare a cascata su tutti i discendenti. 

Metadata Policy di un TA per un RP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito vengono riportati i claim che DEVONO essere considerati nel parametro *metadata* di tipo *openid_realying_party* all'interno della policy che il TA stabilisce per un RP suo discendente diretto. 

.. list-table::
  :widths: 20 20 20
  :header-rows: 1

  * - **Claim**
    - **Operazioni** / **Valori**
    - **Supportato da**
  * - **jwks**
    - Operazioni: *value*, *essential* |br|
      Valori: value è un JSON Object che DEVE contenere keys, un JSON Array di JSON Web Key del RP relativi alle operazioni di Core, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **grant_types**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of è un array che DEVE contenere authorization_code, subset_of è un array che DEVE contenere authorization_code e refresh_token, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **id_token_signed_response_alg**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere uno degli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **id_token_encrypted_response_alg**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere uno degli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *false*.
    - |cieid-icon|
  * - **id_token_encrypted_response_enc**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere uno degli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *false*.
    - |cieid-icon|
  * - **userinfo_signed_response_alg**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere uno degli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_alg**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere uno degli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_enc**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere uno degli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_method**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE essere *private_key_jwt*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **client_registration_types**
    - Operazioni: *subset_of*, *essential* |br|
      Valori: subset_of è un array che DEVE avere valore *automatic*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **redirect_uris**
    - Operazioni: *essential* |br|
      Valori: essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **client_id**
    - Operazioni: *essential* |br|
      Valori: essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **response_types**
    - Operazioni: *value*, *essential* |br|
      Valori: value è un array che DEVE essere *code*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  



Metadata Policy di un TA per un SA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito vengono riportati i claim che DEVONO essere considerati nel parametro *metadata* di tipo *openid_relying_party* all'interno della policy che il TA stabilisce per un SA. Questa policy DEVE essere applicata a cascata ai metadata dei RP discendenti diretti (aggregati) del SA.  

.. list-table::
  :widths: 20 20 20
  :header-rows: 1

  * - **Claim**
    - **Operazioni** / **Valori**
    - **Supportato da**
  * - **grant_types**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of è un array che DEVE contenere *authorization_code*, subset_of è un array che DEVE contenere *authorization_code* e *refresh_token*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **id_token_signed_response_alg**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere uno degli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **id_token_encrypted_response_alg**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *false*.
    - |cieid-icon|
  * - **id_token_encrypted_response_enc**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere uno degli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *false*.
    - |cieid-icon|
  * - **userinfo_signed_response_alg**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere uno degli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_alg**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere uno degli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_enc**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE contenere uno degli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_method**
    - Operazioni: *one_of*, *essential* |br|
      Valori: one_of è un array che DEVE essere *private_key_jwt*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **client_registration_types**
    - Operazioni: *subset_of*, *essential* |br|
      Valori: subset_of è un array che DEVE essere *automatic*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **redirect_uris**
    - Operazioni: *essential* |br|
      Valori: essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **client_id**
    - Operazioni: *essential* |br|
      Valori: essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **response_types**
    - Operazioni: *value*, *essential* |br|
      Valori: value è un array che DEVE essere *code*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|


Metadata Policy di un SA per una RP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito vengono riportati i claim che DEVONO essere considerati nel parametro *metadata* di tipo *openid_relying_party* all'interno della policy che il SA stabilisce per un RP suo discendente diretto (Aggregato). 

.. list-table::
  :widths: 20 20 20
  :header-rows: 1

  * - **Claim**
    - **Operazioni** / **Valori**
    - **Supportato da**
  * - **jwks**
    - Operazioni: *value*, *essential* |br|
      Valori: value è un JSON Object che DEVE contenere keys, un JSON Array di JSON Web Key del RP relativi alle operazioni di Core, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|


Metadata Policy di un TA per un OP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito vengono riportati i claim che DEVONO essere considerati nel parametro *metadata* di tipo *openid_provider* all'interno della policy che il TA stabilisce per un RP suo discendente diretto. 

.. list-table::
  :widths: 20 20 20
  :header-rows: 1

  * - **Claim**
    - **Operazioni** / **Valori**
    - **Supportato da**
  * - **jwks**
    - Operazioni: *value*, *essential* |br|
      Valori: value è un JSON Object che DEVE contenere keys, un JSON Array di JSON Web Key del OP relativi alle operazioni di Core, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **revocation_endpoint_auth_methods_supported**
    - Operazioni: *subset_of*, *essential* |br|
      Valori: subset_of è un array che DEVE essere *private_key_jwt*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **code_challenge_methods_supported**
    - Operazioni: *subset_of*, *essential* |br|
      Valori: subset_of è un array che DEVE essere *S256*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **scopes_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of e subset_of sono array che DEVONO contenere *openid* e *offline_access*, essential è un boolean impostato a *true*. Per CIE id subset_of PUÒ contenere anche *profile*, *email*.
    - |spid-icon| |cieid-icon|
  * - **response_types_supported**
    - Operazioni: *subset_of*, *essential* |br|
      Valori: subset_of è un array che DEVE essere *code*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **response_modes_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of e subset_of sono array che DEVONO contenere *form_post* e *query*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **grant_types_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of e subset_of sono array che DEVONO contenere *refresh_token* e *authorization_code*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **acr_values_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: DEVE contenere |br| *https://www.spid.gov.it/SpidL1*, |br| *https://www.spid.gov.it/SpidL2*, |br| *https://www.spid.gov.it/SpidL3*.  |br|
      *essential = true*
    - |spid-icon| |cieid-icon|
  * - **subject_types_supported**
    - Operazioni: *subset_of*, *essential* |br|
      Valori: subset_of è un array che DEVE essere *pairwise*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **id_token_signing_alg_values_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of è un array che DEVE contenere gli algoritmi OBBLIGATORI sulle operazioni di Signature, subset_of è un array che DEVE contenere sia gli algoritmi OBBLIGATORI che RACCOMANDATI, e essential è un boolean impostato a *true*. Gli algoritmi di Signature sono definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **id_token_encryption_alg_values_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of è un array che DEVE contenere gli algoritmi OBBLIGATORI sulle operazioni di Key Encryption, subset_of è un array che DEVE contenere sia gli algoritmi OBBLIGATORI che RACCOMANDATI e essential è un boolean impostato a *true*. Gli algoritmi di Key Encryption sono definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`.
    - |cieid-icon|
  * - **id_token_encryption_enc_values_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of è un array che DEVE contenere gli algoritmi OBBLIGATORI sulle operazioni di Content Encryption, subset_of è un array che DEVE contenere sia gli algoritmi OBBLIGATORI che RACCOMANDATI e essential è un boolean impostato a *true*. Gli algoritmi di Content Encryption sono definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`.
    - |cieid-icon|
  * - **userinfo_signing_alg_values_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of è un array che DEVE contenere gli algoritmi OBBLIGATORI sulle operazioni di Signature, subset_of è un array che DEVE contenere sia gli algoritmi OBBLIGATORI che RACCOMANDATI e essential è un boolean impostato a *true*. Gli algoritmi di Signature sono definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encryption_alg_values_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of è un array che DEVE contenere gli algoritmi OBBLIGATORI sulle operazioni di Key Encryption, subset_of è un array che DEVE contenere sia gli algoritmi OBBLIGATORI che RACCOMANDATI e essential è un boolean impostato a *true*. Gli algoritmi di Key Encryption sono definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encryption_enc_values_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of è un array che DEVE contenere gli algoritmi OBBLIGATORI sulle operazioni di Content Encryption, subset_of è un array che DEVE contenere sia gli algoritmi OBBLIGATORI che RACCOMANDATI e essential è un boolean impostato a *true*. Gli algoritmi di Content Encryption sono definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_methods_supported**
    - Operazioni: *subset_of*, *essential* |br|
      Valori: subset_of è un array che DEVE essere *private_key_jwt*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_signing_alg_values_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of è un array che DEVE contenere gli algoritmi OBBLIGATORI sulle operazioni di Signature, subset_of è un array che DEVE contenere sia gli algoritmi OBBLIGATORI che RACCOMANDATI e essential è un boolean impostato a *true*. Gli algoritmi di Signature sono definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **claims_parameter_supported**
    - Operazioni: *value*, *essential* |br|
      Valori: value è un boolean che DEVE essere *true*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **request_parameter_supported**
    - Operazioni: *value*, *essential* |br|
      Valori: value è un boolean che DEVE essere *true*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **authorization_response_iss_parameter_supported**
    - Operazioni: *value*, *essential* |br|
      Valori: value è un boolean che DEVE essere *true*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **client_registration_types_supported**
    - Operazioni: *subset_of*, *essential* |br|
      Valori: subset_of è un array che DEVE essere *automatic*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **request_authentication_methods_supported**
    - Operazioni: *value*, *essential* |br|
      Valori: value è un oggetto JSON contenente un array *authorization_endpoint* che DEVE essere *request_object*, e essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **request_authentication_signing_alg_values_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of è un array che DEVE contenere gli algoritmi OBBLIGATORI sulle operazioni di Signature, subset_of è un array che DEVE contenere sia gli algoritmi OBBLIGATORI che RACCOMANDATI e essential è un boolean impostato a *true*. Gli algoritmi di Signature sono definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **request_object_signing_alg_values_supported**
    - Operazioni: *subset_of*, *superset_of*, *essential* |br|
      Valori: superset_of è un array che DEVE contenere gli algoritmi OBBLIGATORI sulle operazioni di Signature, subset_of è un array che DEVE contenere sia gli algoritmi OBBLIGATORI che RACCOMANDATI e essential è un boolean impostato a *true*. Gli algoritmi di Signature sono definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **issuer**
    - Operazioni: *essential* |br|
      Valori: essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **authorization_endpoint**
    - Operazioni: *essential* |br|
      Valori: essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint**
    - Operazioni: *essential* |br|
      Valori: essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **userinfo_endpoint**
    - Operazioni: *essential* |br|
      Valori: essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **introspection_endpoint**
    - Operazioni: *essential* |br|
      Valori: essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|
  * - **revocation_endpoint**
    - Operazioni: *essential* |br|
      Valori: essential è un boolean impostato a *true*.
    - |spid-icon| |cieid-icon|

.. seealso:: 

   - :ref:`Esempi non normativi di Metadata Policy<Esempio_EN7>`


