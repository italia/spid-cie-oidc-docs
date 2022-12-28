.. include:: ../common/common_definitions.rst

.. _MetadataRP:

OpenID Connect Relying Party Metadata (RP)
++++++++++++++++++++++++++++++++++++++++++

Un RP DEVE pubblicare all'interno del suo EC un Metadata di tipo *federation_entity* e uno di tipo *openid_relying_party* come riportato nel seguente esempio:

.. code-block:: json

 {
    "metadata":{
      "federation_entity":{
        ...
      }
      "openid_relying_party":{
        ...
      }
    }
 }

Il Metadata di tipo **"federation_entity"** DEVE contenere almeno i seguenti parametri obbligatori:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Supportato da**
  * - **organization_name**
    - Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **homepage_uri**
    - Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **policy_uri**
    - Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **logo_uri**
    - (RACCOMANDATO) URL del logo dell'entità; DEVE essere in formato SVG. Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **contacts**
    - PEC istituzionale dell'ente. Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **federation_resolve_endpoint**
    - Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED`_ Section 4.6
    - |spid-icon| |cieid-icon|




Il Metadata di tipo **"openid_relying_party"** DEVE contenere almeno i seguenti parametri obbligatori:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Supportato da** 
  * - **redirect_uris**
    - Vedi `OpenID.Registration#ClientMetadata`_. È obbligatorio l'uso dello schema HTTPS nel caso di client web-based.
    - |spid-icon| |cieid-icon|
  * - **grant_types**
    - Vedi `OpenID.Registration#ClientMetadata`_. I valori ammissibili **authorization_code** e **refresh_token**.
    - |spid-icon| |cieid-icon|
  * - **jwks**
    - Vedi `OpenID.Registration#ClientMetadata`_ e `JWK`_.
    - |spid-icon| |cieid-icon| 
  * - **id_token_signed_response_alg**
    - Vedi `OpenID.Registration#ClientMetadata`_. Vedi signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon| 
  * - **id_token_encrypted_response_alg**
    - Vedi `OpenID.Registration#ClientMetadata`_. Vedi key encryption :ref:`supported_algs`.
    - |cieid-icon| 
  * - **id_token_encrypted_response_enc**
    - Vedi `OpenID.Registration#ClientMetadata`_. Obbligatorio solo nel caso sia presente anche il parametro *id_token_encrypted_response_alg*. Vedi content encryption :ref:`supported_algs`.
    - |cieid-icon| 
  * - **userinfo_signed_response_alg**
    - Vedi `OpenID.Registration#ClientMetadata`_. Vedi signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon| 
  * - **userinfo_encrypted_response_alg**
    - Vedi `OpenID.Registration#ClientMetadata`_. Vedi key encryption :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_enc**
    - Vedi `OpenID.Registration#ClientMetadata`_. Vedi content encryption :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_method**
    - Vedi `OpenID.Registration#ClientMetadata`_. Il valore richiesto è **private_key_jwt**.
    - |spid-icon| |cieid-icon|  
  * - **client_id**
    - Vedi `OpenID.Registration`_. DEVE essere valorizzato con un HTTPS URL che identifica univocamente il RP.
    - |spid-icon| |cieid-icon|
  * - **client_registration_types**
    - Vedi `OIDC-FED`_ Section 4.1. Il valore richiesto è **automatic**. 
    - |spid-icon| |cieid-icon|
  * - **response_types**
    - Array dei valori di response_type previsti da OAuth 2.0 che il RP userà nelle richieste di autenticazione. Deve contenere il valore **code**. 
    - |spid-icon| |cieid-icon|

.. note:: 
  Gli URI presenti nel parametro **redirect_uris** POSSONO anche usare eventuali schemi custom (ad es. myapp://) al fine di supportare applicazioni mobili.

