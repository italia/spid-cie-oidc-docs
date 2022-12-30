.. include:: ../common/common_definitions.rst

.. _MetadataOP:

OpenID Connect Provider Metadata (OP)
+++++++++++++++++++++++++++++++++++++

An OP MUST publish in its EC a Metadata of type *federation_entity* and a Metadata of type *openid_provider*, as 
reported in the following example:

.. code-block:: json

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
    - See `OpenID.Discovery#OP_Metadata`_. The supported values are **openid** and **offline_access**. CIE id supports also **profile**, **email**. For more details, see the section :ref:`User's Claims <user_claims_scopes>`.
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
    - See `OpenID.Discovery#OP_Metadata`_. See signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
  * - **id_token_encryption_alg_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. See key encryption :ref:`supported_algs`.
    - |cieid-icon|
  * - **id_token_encryption_enc_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. See content encryption :ref:`supported_algs`.
    - |cieid-icon|
  * - **userinfo_signing_alg_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. See signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encryption_alg_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. See key encryption :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encryption_enc_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. See content encryption :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
  * - **request_object_signing_alg_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. See signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
..    * - **request_object_encryption_alg_values_supported**
..      - Until otherwise indicated by AgID, this MUST NOT be included.
..      - |spid-icon|
..    * - **request_object_encryption_enc_values_supported**
..      - Until otherwise indicated by AgID, this MUST NOT be included.
..      - |spid-icon|
  * - **token_endpoint_auth_methods_supported**
    - See `OpenID.Discovery#OP_Metadata`_. The supported value is **private_key_jwt**
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_signing_alg_values_supported**
    - See `OpenID.Discovery#OP_Metadata`_. See signature :ref:`supported_algs`.
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
    - See `OIDC-FED`_ Section 4.2 and `JWK`_.
    - |spid-icon| |cieid-icon|
  * - **client_registration_types_supported**
    - See `OIDC-FED`_ Section 4.2. The supported value is **automatic**. 
    - |spid-icon| |cieid-icon|
  * - **request_authentication_methods_supported**
    - See `OIDC-FED`_ Section 4.2`_. The supported value is **request_object**.
    - |spid-icon| |cieid-icon|
  * - **request_authentication_signing_alg_values_supported**
    - See `OIDC-FED`_ Section 4.2. See signature :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|


.. warning::
  The OP Metadata of type **"openid_provider"** exposes the claim **jwks** as regulated by OID-FED instead of
  the claim **jwks_uri** as required at `OpenID.Discovery#OP_Metadata`_. 

.. seealso:: 

   - :ref:`Example of an EC of an OP <Esempio_EN1.2>`

