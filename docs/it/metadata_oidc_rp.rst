.. include:: ./common_definitions.rst

.. _MetadataRP:

OpenID Connect Relying Party Metadata (RP)
++++++++++++++++++++++++++++++++++++++++++

Un RP DEVE pubblicare all'interno del suo EC un Metadata da *federation_entity* e uno da *openid_relying_party* come riportato nel seguente esempio:

.. code-block:: 

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

Il Metadata dell'OP da **"federation_entity"** DEVE contenere almeno i seguenti parametri obbligatori:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Supportato da**
  * - **federation_resolve_endpoint**
    - Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED#Section.4.6`_
    - |spid-icon| |cieid-icon|




Il Metadata del RP da **"openid_relying_party"** DEVE contenere almeno i seguenti parametri obbligatori:

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
  * - **logo_uri**
    - Vedi `OpenID.Registration#ClientMetadata`_. L'immagine disponibile all'URL indicata DEVE essere in formato *SVG*.
    - |spid-icon| |cieid-icon|
  * - **jwks**
    - Vedi `OpenID.Registration#ClientMetadata`_ e `JWK`_.
    - |spid-icon| |cieid-icon| 
  * - **id_token_signed_response_alg**
    - Vedi `OpenID.Registration#ClientMetadata`_.
    - |spid-icon| |cieid-icon| 
  * - **userinfo_signed_response_alg**
    - Vedi `OpenID.Registration#ClientMetadata`_.
    - |spid-icon| |cieid-icon| 
  * - **userinfo_encrypted_response_alg**
    - Vedi `OpenID.Registration#ClientMetadata`_.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_enc**
    - Vedi `OpenID.Registration#ClientMetadata`_.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_method**
    - Vedi `OpenID.Registration#ClientMetadata`_. Il valore richiesto è **private_key_jwt**.
    - |spid-icon| |cieid-icon|  
  * - **client_id**
    - Vedi `OpenID.Registration`_. DEVE essere valorizzato con un HTTPS URL che identifica univocamente il RP.
    - |spid-icon| |cieid-icon|
  * - **client_registration_types**
    - Vedi `OIDC-FED#Section.4.1`_. Il valore richiesto è **automatic**. 
    - |spid-icon| |cieid-icon|

.. note:: 
  Gli URI presenti nel parametro **redirect_uris** POSSONO anche seguire eventuali schemi custom (ad es. myapp://) al fine di supportare applicazioni mobili.

