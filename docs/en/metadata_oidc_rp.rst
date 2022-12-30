.. include:: ../common/common_definitions.rst

.. _MetadataRP:

OpenID Connect Relying Party Metadata (RP)
++++++++++++++++++++++++++++++++++++++++++

An RP MUST publish in its EC a Metadata of type *federation_entity* and a Metadata of type *openid_relying_party*, as reported in the following example:

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

The OP Metadata of type **"federation_entity"** MUST contain at least the following mandatory parameters:

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
  * - **federation_resolve_endpoint**
    - See Section :ref:`Federation Endpoint <federation_endpoint>` and `OIDC-FED`_ Section 4.6.
    - |spid-icon| |cieid-icon|



The RP Metadata of type **"openid_relying_party"** MUST contain at least the following mandatory parameters:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Supported by***
  * - **redirect_uris**
    - See `OpenID.Registration#ClientMetadata`_. It is mandatory using an HTTPS schema in case of a web-based client.
    - |spid-icon| |cieid-icon|
  * - **grant_types**
    - See `OpenID.Registration#ClientMetadata`_. The supported values are **authorization_code** and **refresh_token**.
    - |spid-icon| |cieid-icon|
  * - **jwks**
    - See `OpenID.Registration#ClientMetadata`_ and `JWK`_.
    - |spid-icon| |cieid-icon| 
  * - **id_token_signed_response_alg**
    - See `OpenID.Registration#ClientMetadata`_. See signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon| 
  * - **id_token_encrypted_response_alg**
    - See `OpenID.Registration#ClientMetadata`_. See key encryption :ref:`supported_algs`.
    - |cieid-icon| 
  * - **id_token_encrypted_response_enc**
    - See `OpenID.Registration#ClientMetadata`_. This content encryption is required only if the *id_token_encrypted_response_alg* is given. See key encryption :ref:`supported_algs`.
    - |cieid-icon| 
  * - **userinfo_signed_response_alg**
    - See `OpenID.Registration#ClientMetadata`_. See signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon| 
  * - **userinfo_encrypted_response_alg**
    - See `OpenID.Registration#ClientMetadata`_. See key encryption :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_enc**
    - See `OpenID.Registration#ClientMetadata`_. See content encryption :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_method**
    - See `OpenID.Registration#ClientMetadata`_. The required value is **private_key_jwt**.
    - |spid-icon| |cieid-icon|  
  * - **client_id**
    - See `OpenID.Registration`_. It MUST contain an HTTPS URL that uniquely identifies the RP.
    - |spid-icon| |cieid-icon|
  * - **client_registration_types**
    - See `OIDC-FED`_ Section 4.1. The required value is **automatic**. 
    - |spid-icon| |cieid-icon|
  * - **response_types**
    - JSON array containing a list of the OAuth 2.0 response_type values that the RP is declaring that it will restrict itself to using. It MUST contain the value **code**.
    - |spid-icon| |cieid-icon|

.. note:: 
  The URIs contained in the claim **redirect_uris** MAY also use custom schemas (e.g. myapp://) 
  in order to support mobile applications.

