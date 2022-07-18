.. include:: ./common_definitions.rst


Metadata Attribute Authority
++++++++++++++++++++++++++++

Una AA DEVE pubblicare all'interno del suo EC un Metadata da *federation_entity*, uno da *oauth_authorization_server* e uno da *oauth_resource* come riportato nel seguente esempio:

.. code-block:: 

 {
    "metadata":{
      "federation_entity":{
        ...
      }
      "oauth_authorization_server":{
        ...
      }
      "oauth_resource":{
        ...
      }
    }
 }

Il Metadata dell'AA da **"federation_entity"** DEVE contenere almeno i seguenti parametri obbligatori:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Supportato da**
  * - **organization_name**
    - Denominazione dell'organizzazione.
    - |spid-icon| |cieid-icon|
  * - **federation_resolve_endpoint**
    - Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED#Section.4.6`_
    - |spid-icon| |cieid-icon|
  * - **federation_status_endpoint**
    - Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED#Section.4.6`_
    - |spid-icon| |cieid-icon|

Il Metadata dell'AA da **"oauth_authorization_server"** DEVE contenere almeno i seguenti parametri obbligatori:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Supportato da**
  * - **issuer**
    - Vedi :rfc:`8414#page-4`.  DEVE essere valorizzato con un HTTPS URL che identifica univocamente l'AA.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint**
    - Vedi :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **jwks**
    - Vedi `JWK`_.
    - |spid-icon| |cieid-icon|
  * - **scopes_supported**
    - Vedi :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **response_types_supported**
    - Vedi :rfc:`8414#page-4`,
    - |spid-icon| |cieid-icon|
  * - **grant_types_supported**
    - Vedi :rfc:`8414#page-4` e :rfc:`8623`.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_methods_supported**
    - Vedi :rfc:`8414#page-4`. Il valore supportato è **private_key_jwt**.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_signing_alg_values_supported**
    - Vedi :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **op_policy_uri**
    - Vedi :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **dpop_signing_alg_values_supported**
    - Vedi `OAuth-DPoP`_.
    - |spid-icon| |cieid-icon|






Il Metadata dell'AA da **"oauth_resource"** DEVE contenere almeno i seguenti parametri obbligatori:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Supportato da**
  * - **logo_uri**
    - Vedi :rfc:`7591`. L'immagine disponibile all'URL indicata DEVE essere in formato *SVG*.
    - |spid-icon| |cieid-icon|
  * - **resource**
    - Vedi `OAuth-RS`_. Una o più HTTPS URL che identificano gli endpoint delle risorse protette.
    - |spid-icon| |cieid-icon|
