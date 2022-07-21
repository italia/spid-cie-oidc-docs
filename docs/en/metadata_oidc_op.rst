.. include:: ../common/common_definitions.rst

.. _MetadataOP:

OpenID Connect Provider Metadata (OP)
+++++++++++++++++++++++++++++++++++++

An OP MUST publish in its EC a Metadata of type *federation_entity* and a Metadata of type *openid_provider*, as 
reported in the following example:

.. code-block:: 

 {
    "metadata":{
      "federation_entity":{
        ...
      }
      "openid_provider":{
        ...
      }
    }
 }

The EC of an OP MUST configure a Metadata of type **"federation_entity"** and contain at least the following 
mandatory parameters:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Supported by**
  * - **federation_resolve_endpoint**
    - See Section :ref:`Federation Endpoint <federation_endpoint>` and `OIDC-FED#Section.4.6`_
    - |spid-icon| |cieid-icon|


The EC of an OP MUST configure a metadata of type **"openid_provider"**, that MUST contain at least the following mandatory parameters:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Supported by**
  * - **issuer**
    - See `OpenID.Discovery#OP_Metadata`_. It MUST contain an HTTPS URL that uniquely identifies the OP.
    - |spid-icon| |cieid-icon|
  * - **authorization_endpoint**
    - See `OpenID.Discovery#OP_Metadata`_.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint**
    - See `OpenID.Discovery#OP_Metadata`_.
    - |spid-icon| |cieid-icon|
  * - **userinfo_endpoint**
    - See `OpenID.Discovery#OP_Metadata`_.
    - |spid-icon| |cieid-icon|
  * - **introspection_endpoint**
    - See :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **revocation_endpoint** 
    - See :rfc:`8414#page-4`.
    - |spid-icon| |cieid-icon|
  * - **revocation_endpoint_auth_methods_supported**
    - See :rfc:`8414#page-4`. The supported value is **private_key_jwt**
    - |cieid-icon|
  * - **code_challenge_methods_supported**
    - See :rfc:`8414#page-4`. The OP MUST support S256 (see :rfc:`7636#section-4.3`).
    - |spid-icon| |cieid-icon|
  * - **scopes_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The supported values are **openid**, **offline_access**, **profile**, **email**. For more details, see the section :ref:`User's Claims <user_claims_scopes>`.
    - |spid-icon| |cieid-icon|
  * - **response_types_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The supported value is **code**. 
    - |spid-icon| |cieid-icon|
  * - **response_modes_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The supported values are **form_post** and **query**.
    - |spid-icon| |cieid-icon|
  * - **grant_types_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The supported values are **refresh_token** and **authorization_code**.
    - |spid-icon| |cieid-icon|
  * - **acr_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The supported values are:
      
      ``https://www.spid.gov.it/SpidL1``
      ``https://www.spid.gov.it/SpidL2``
      ``https://www.spid.gov.it/SpidL3``

    - |spid-icon| |cieid-icon|
  * - **subject_types_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The supported value is **pairwise**. 
    - |spid-icon| |cieid-icon|
  * - **id_token_signing_alg_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The OP MUST support RS256 and CAN also support other 
      algorithms of types RS, ES and PS, defined at :rfc:`7518#section-3.1`
    - |spid-icon| |cieid-icon|
  * - **userinfo_signing_alg_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The OP MUST support RS256 and CAN also support other  
      algorithms of types RS, ES and PS, defined at :rfc:`7518#section-3.1`.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encryption_alg_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. For the definition of the encryption algorithms (*alg*) RSA-OAEP-256 e RSA-OAEP.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encryption_enc_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. For the definition of the encryption algorithms (*enc*) see :rfc:`7518#section-5.1`
    - |spid-icon| |cieid-icon|
  * - **request_object_signing_alg_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The OP MUST support RS256 and CAN also support other 
      algorithms of types RS, ES and PS, defined at :rfc:`7518#section-3.1`.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_methods_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The supported value is **private_key_jwt**
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_signing_alg_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The OP MUST support RS256 and CAN also support other
      algorithms of types RS, ES and PS, defined at :rfc:`7518#section-3.1`.
    - |spid-icon| |cieid-icon|
  * - **claims_supported**
    - See `OpenID.Discovery#OP_Metadata`_. See :ref:`User Claims <user_claims>` for more details.
    - |spid-icon| |cieid-icon|
  * - **claims_parameter_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The supported value is **true**.
    - |spid-icon| |cieid-icon|
  * - **request_parameter_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The supported value is **true**.
    - |spid-icon| |cieid-icon|
  * - **authorization_response_iss_parameter_supported**
    - See :rfc:`9207#section-3`. It must contain *true*.
    - |cieid-icon|
  * - **jwks**
    - See `OIDC-FED#Section.4.2`_ and `JWK`_.
    - |spid-icon| |cieid-icon|
  * - **client_registration_types_supported**
    - See `OIDC-FED#Section.4.2`_. The supported value is **automatic**. 
    - |spid-icon| |cieid-icon|
  * - **request_authentication_methods_supported**
    - See `OIDC-FED#Section.4.2`_. The supported value is **request_object**.
    - |spid-icon| |cieid-icon|
  * - **request_authentication_signing_alg_values_supported**
    - See `OIDC-FED#Section.4.2`_. The OP MUST support RS256 and CAN also support other
      algorithms of types RS, ES and PS, defined at :rfc:`7518#section-3.1`.
    - |spid-icon| |cieid-icon|


.. warning::
  The OP Metadata of type **"openid_provider"** exposes the claim **jwks** as regulated by OID-FED instead of
  the claim **jwks_uri** as required at `OpenID.Discovery#OP_Metadata`_.

.. seealso:: 

   - :ref:`Example of an EC of an OP <Esempio_EN1.2>`

