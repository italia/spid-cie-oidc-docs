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
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere i JWKS del RP relativi alle operazioni di Core
    - |spid-icon| |cieid-icon|
  * - **grant_types**
    - Operazioni: *subset_of* |br|
      Valori: DEVE essere *authorization_code* e *refresh_token*
    - |spid-icon| |cieid-icon|
  * - **id_token_signed_response_alg**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **id_token_encrypted_response_alg**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |cieid-icon|
  * - **id_token_encrypted_response_enc**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |cieid-icon|
  * - **userinfo_signed_response_alg**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_alg**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_enc**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_method**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *private_key_jwt*
    - |spid-icon| |cieid-icon|
  * - **client_registration_types**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *automatic*
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
    - Operazioni: *subset_of* |br|
      Valori: DEVE essere *authorization_code* e *refresh_token*
    - |spid-icon| |cieid-icon|
  * - **id_token_signed_response_alg**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **id_token_encrypted_response_alg**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |cieid-icon|
  * - **id_token_encrypted_response_enc**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |cieid-icon|
  * - **userinfo_signed_response_alg**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_alg**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_enc**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_method**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *private_key_jwt*
    - |spid-icon| |cieid-icon|
  * - **client_registration_types**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *automatic*
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
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere i JWKS del RP relativi alle operazioni di Core
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
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere i JWKS del OP relativi alle operazioni di Core
    - |spid-icon| |cieid-icon|
  * - **revocation_endpoint_auth_methods_supported**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *private_key_jwt*
    - |spid-icon| |cieid-icon|
  * - **code_challenge_methods_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE essere *S256*
    - |spid-icon| |cieid-icon|
  * - **scopes_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere *openid*, *offline_access*. Per CIE id PUÒ contenere anche *profile*, *email*.
    - |spid-icon| |cieid-icon|
  * - **response_types_supported**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *code*.
    - |spid-icon| |cieid-icon|
  * - **response_modes_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE essere *form_post*, *query*.
    - |spid-icon| |cieid-icon|
  * - **grant_types_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE essere *refresh_token*, *authorization_code*.
    - |spid-icon| |cieid-icon|
  * - **acr_values_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE essere |br| *https://www.spid.gov.it/SpidL1*, |br| *https://www.spid.gov.it/SpidL2*, |br| *https://www.spid.gov.it/SpidL3*.
    - |spid-icon| |cieid-icon|
  * - **subject_types_supported**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *pairwise*.
    - |spid-icon| |cieid-icon|
  * - **id_token_signing_alg_values_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **id_token_encryption_alg_values_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **id_token_encryption_enc_values_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_signing_alg_values_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encryption_alg_values_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encryption_enc_values_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_methods_supported**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *private_key_jwt*
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_signing_alg_values_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **claims_parameter_supported**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *true*
    - |spid-icon| |cieid-icon|
  * - **request_parameter_supported**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *true*
    - |spid-icon| |cieid-icon|
  * - **authorization_response_iss_parameter_supported**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *true*
    - |spid-icon| |cieid-icon|
  * - **client_registration_types_supported**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *automatic*
    - |spid-icon| |cieid-icon|
  * - **request_authentication_methods_supported**
    - Operazioni: *one_of* |br|
      Valori: DEVE essere *request_object*
    - |spid-icon| |cieid-icon|
  * - **request_authentication_signing_alg_values_supported**
    - Operazioni: *subset_of* |br|
      Valori: DEVE contenere gli algoritmi definiti nella Sezione :ref:`Algoritmi Crittografici <supported_algs>`
    - |spid-icon| |cieid-icon|

.. seealso:: 

   - :ref:`Esempi non normativi di Metadata Policy<Esempio_EN7>`


