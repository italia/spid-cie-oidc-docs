.. include:: ../common/common_definitions.rst


Attribute Authority Metadata
++++++++++++++++++++++++++++

An AA MUST publish in its EC a *federation_entity* Metadata and an *oauth_resource* Metadata, if the resources are protected it MUST also publish an *oauth_authorization_server* Metadata.


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

The AA Metadata of type **"federation_entity"** MUST contain at least the following mandatory parameters:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Supported by**
  * - **organization_name**
    - Name of the organization.
    - |spid-icon| |cieid-icon|
  * - **federation_resolve_endpoint**
    - See Section :ref:`Federation Endpoint <federation_endpoint>` and `OIDC-FED#Section.4.6`_
    - |spid-icon| |cieid-icon|
  * - **federation_status_endpoint**
    - See Section :ref:`Federation Endpoint <federation_endpoint>` and `OIDC-FED#Section.4.6`_
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
    - See :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **op_policy_uri**
    - See :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **dpop_signing_alg_values_supported**
    - See `OAuth-DPoP`_.
    - |spid-icon| |cieid-icon|



The AA Metadata of type **"oauth_resource"** MUST contain at least the following mandatory parameters:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Supported by**
  * - **logo_uri**
    - See :rfc:`7591`. he image available at the indicated URL MUST be of *SVG* format.
    - |spid-icon| |cieid-icon|
  * - **resource**
    - See `OAuth-RS`_. One or more HTTPS URLs that identify the endpoints of the protected resources.
    - |spid-icon| |cieid-icon|
