.. include:: ../common/common_definitions.rst


Metadata Attribute Authority
++++++++++++++++++++++++++++

Una AA DEVE pubblicare, all'interno del suo EC, un Metadata *federation_entity* e un Metadata *oauth_resource* e, se le risorse sono protette, DEVE anche pubblicare un Metadata *oauth_authorization_server*.


.. code-block:: json

 {
    "metadata":{
      "federation_entity":{
        ...
      },
      "oauth_authorization_server":{
        ...
      },
      "oauth_resource":{
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
    - URL del logo dell'entità; DEVE essere in formato SVG. Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **contacts**
    - PEC istituzionale dell'ente. Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **federation_trust_mark_status_endpoint**
    - Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **federation_resolve_endpoint**
    - Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|


Il Metadata di tipo **"oauth_authorization_server"** DEVE contenere almeno i seguenti parametri obbligatori:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Supportato da**
  * - **issuer**
    - Vedi :rfc:`8414#page-4`.  DEVE essere valorizzato con un HTTPS URL che identifica univocamente l'AA.
    - |spid-icon| |cieid-icon|
  * - **authorization_endpoint**
    - Solo per Attribute Authority **private** flow. Vedi `LG-AA` and :rfc:`8414#page-4`.
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
    - Vedi :rfc:`8414#page-4`. Vedi signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
  * - **op_policy_uri**
    - Vedi :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **op_tos_uri**
    - Vedi :rfc:`8414#page-6`.
    - |spid-icon| |cieid-icon|
  * - **dpop_signing_alg_values_supported**
    - Vedi `OAuth-DPoP`_. Vedi signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|


Il Metadata di tipo **"oauth_resource"** DEVE contenere almeno i seguenti parametri obbligatori:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Supportato da**
  * - **resource**
    - Vedi `OAuth-RS`_. Una o più HTTPS URL che identificano gli endpoint delle risorse protette.
    - |spid-icon| |cieid-icon|
