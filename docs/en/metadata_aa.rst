.. include:: ../common/common_definitions.rst


Attribute Authority Metadata
++++++++++++++++++++++++++++

An AA MUST publish in its EC a *federation_entity* Metadata and an *oauth_resource* Metadata, if the resources are protected it MUST also publish an *oauth_authorization_server* Metadata.


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

The AA Metadata of type **"federation_entity"** MUST contain at least the following mandatory parameters:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Supported by**
  * - **organization_name**
    - See `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **homepage_uri**
    - See `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **policy_uri**
    - See `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **logo_uri**
    - URL of the entity's logo; it MUST be in SVG format. See `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **contacts**
    - Institutional certified email address (PEC) of the entity. See `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **federation_trust_mark_status_endpoint**
    - See Section :ref:`Federation Endpoint <federation_endpoint>` and `OIDC-FED`_ Section 4.8.
    - |spid-icon| |cieid-icon|
  * - **federation_resolve_endpoint**
    - See Section :ref:`Federation Endpoint <federation_endpoint>` and `OIDC-FED`_ Section 4.8.
    - |spid-icon| |cieid-icon|

The AA Metadata with **"oauth_authorization_server"** MUST contain at least the following mandatory parameters:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Supported by**
  * - **issuer**
    - See :rfc:`8414#page-4`. It MUST contain an HTTPS URL that uniquely identifies the AA.
    - |spid-icon| |cieid-icon|
  * - **authorization_endpoint**
    - Only for Attribute Authority private flow. See `LG-AA` and :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint**
    - See :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **jwks**
    - See `JWK`_.
    - |spid-icon| |cieid-icon|
  * - **scopes_supported**
    - See :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **response_types_supported**
    - See :rfc:`8414#page-4`,
    - |spid-icon| |cieid-icon|
  * - **grant_types_supported**
    - See :rfc:`8414#page-4` and :rfc:`8623`.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_methods_supported**
    - See :rfc:`8414#page-4`. The supported value is **private_key_jwt**.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_signing_alg_values_supported**
    - See :rfc:`8414#page-4`. See signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
  * - **op_policy_uri**
    - See :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **op_tos_uri**
    - See :rfc:`8414#page-6`.
    - |spid-icon| |cieid-icon|
  * - **dpop_signing_alg_values_supported**
    - See `OAuth-DPoP`_. See signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|



The AA Metadata of type **"oauth_resource"** MUST contain at least the following mandatory parameters:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Supported by**
  * - **resource**
    - See `OAuth-RS`_. One or more HTTPS URLs that identify the endpoints of the protected resources.
    - |spid-icon| |cieid-icon|
