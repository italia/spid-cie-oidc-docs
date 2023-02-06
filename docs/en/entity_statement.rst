.. include:: ../common/common_definitions.rst

.. _Entity_Statement:

Entity Statements
-----------------

The basic component for building a Trust Chain is the **Entity Statement (ES)**, a signed JWT that
contains the Federation public keys of a subordinate Entity (subject) and further data used to control the
process of Trust Chain resolution.

An Entity publishes an **ES** related to a subordinate, at its :ref:`Fetch Endpoint<Esempio_EN2>`. 
The superior Entity MAY define the Metadata policy for a subject and publishes the TMs that it has issued for it.


Entity Statement Signature
++++++++++++++++++++++++++

The same considerations made for the **ECs** and reported in the section :ref:`Firma della Entity Configuration<firma_EC>`, apply.


Entity Statement
++++++++++++++++

The ES issued by the TA or by an Intermediate for its own direct subordinates, MUST contain the following attributes:


.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **iss**
     - See `OIDC-FED`_ Section 3.1 for further details.
     - |spid-icon| |cieid-icon|
   * - **sub**
     - See `OIDC-FED`_ Section 3.1 for further details.
     - |spid-icon| |cieid-icon|
   * - **iat**
     - See `OIDC-FED`_ Section 3.1 for further details.
     - |spid-icon| |cieid-icon|
   * - **exp**
     - See `OIDC-FED`_ Section 3.1 for further details.
     - |spid-icon| |cieid-icon|
   * - **jwks**
     - Federation JWKS of the *sub* entity. See `OIDC-FED`_ Section 3.1 for further details.
     - |spid-icon| |cieid-icon|
   * - **metadata_policy**
     - JSON Object that describes the Metadata policy. Each key of the JSON Object represents an 
       identifier of the type of Metadata and each value MUST be a JSON Object that represents the Metadata 
       policy according to that Metadata type. Please refer to the `OIDC-FED`_ specifications, Section-5.1,
       for the implementation details.
     - |spid-icon| |cieid-icon|
   * - **trust_marks**
     - JSON Array containing the Trust Marks issued by itself for the subordinate subject.
     - |spid-icon| |cieid-icon|
   * - **constraints**
     - It MAY contain the **allowed_leaf_entity_types**, that restricts what types of metadata a subject is allowed to publish.
     - |spid-icon| |cieid-icon|


.. seealso:: 

   - `OIDC-FED#Section_3.1`_
   - :ref:`Non-normative example of Entity Statement<Esempio_EN2.1>`


.. _Metadata_Policy:

Metadata Policy
+++++++++++++++

Trust Anchors and Intermediates (SAs) MUST publish a policy regarding their respective descendants in the Entity Statement referring to them. The Metadata Policy MUST cascade to all descendants. 

TA Metadata Policy for RP
^^^^^^^^^^^^^^^^^^^^^^^^^

The following claims MUST be considered in the *metadata* parameter of type *openid_realying_party* within the policy that the TA establishes for an RP. 


.. list-table::
  :widths: 20 20 20
  :header-rows: 1

  * - **Claim**
    - **Operations** / **Values**
    - **Supported by**
  * - **jwks**
    - Operations: *subset_of* |br|
      Values: MUST contain the RP JWKS related to the OIDC Core operations.
    - |spid-icon| |cieid-icon|
  * - **grant_types**
    - Operations: *subset_of* |br|
      Values: MUST be *authorization_code*, *refresh_token*
    - |spid-icon| |cieid-icon|
  * - **id_token_signed_response_alg**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **id_token_encrypted_response_alg**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |cieid-icon|
  * - **id_token_encrypted_response_enc**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |cieid-icon|
  * - **userinfo_signed_response_alg**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_alg**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_enc**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_method**
    - Operations: *one_of* |br|
      Values: MUST be *private_key_jwt*
    - |spid-icon| |cieid-icon|
  * - **client_registration_types**
    - Operations: *one_of* |br|
      Values: MUST be *automatic*
    - |spid-icon| |cieid-icon|
  

TA Metadata Policy for SA
^^^^^^^^^^^^^^^^^^^^^^^^^

The following claims MUST be considered in the *metadata* parameter of type *openid_relying_party* within the policy that the TA establishes for a SA. This policy MUST be cascaded to the metadata of the direct descendant (RP aggregate) of the SA.  

.. list-table::
  :widths: 20 20 20
  :header-rows: 1

  * - **Claim**
    - **Operations** / **Values**
    - **Supported by**
  * - **grant_types**
    - Operations: *subset_of* |br|
      Values: MUST be *authorization_code*, *refresh_token*
    - |spid-icon| |cieid-icon|
  * - **id_token_signed_response_alg**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **id_token_encrypted_response_alg**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |cieid-icon|
  * - **id_token_encrypted_response_enc**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |cieid-icon|
  * - **userinfo_signed_response_alg**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_alg**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_enc**
    - Operations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_method**
    - Operations: *one_of* |br|
      Values: MUST be *private_key_jwt*
    - |spid-icon| |cieid-icon|
  * - **client_registration_types**
    - Operations: *one_of* |br|
      Values: MUST be *automatic*
    - |spid-icon| |cieid-icon|

SA Metadata Policy for RP
^^^^^^^^^^^^^^^^^^^^^^^^^

The following claims MUST be considered in the *metadata* parameter of type *openid_relying_party* within the policy that the SA establishes for an RP its direct descendant (Aggregate). 

.. list-table::
  :widths: 20 20 20
  :header-rows: 1

  * - **Claim**
    - **Operations** / **Values**
    - **Supported by**
  * - **jwks**
    - Operations: *subset_of* |br|
      Values: MUST contain the RP JWKS related to the OIDC Core Operations
    - |spid-icon| |cieid-icon|


TA Metadata Policy for OP
^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito vengono riportati i claim che DEVONO essere considerati nel parametro *metadata* di tipo *openid_provider* all'interno della policy che il TA stabilisce per un RP suo discendente diretto. 

.. list-table::
  :widths: 20 20 20
  :header-rows: 1

  * - **Claim**
    - **Operarations** / **Values**
    - **Supportato da**
  * - **jwks**
    - Operarations: *subset_of* |br|
      Values: DEVE contenere i JWKS del OP relativi alle Operarations di Core
    - |spid-icon| |cieid-icon|
  * - **revocation_endpoint_auth_methods_supported**
    - Operarations: *one_of* |br|
      Values: MUST be *private_key_jwt*
    - |spid-icon| |cieid-icon|
  * - **code_challenge_methods_supported**
    - Operarations: *subset_of* |br|
      Values: MUST be *S256*
    - |spid-icon| |cieid-icon|
  * - **scopes_supported**
    - Operarations: *subset_of* |br|
      Values: MUST contain *openid*, *offline_access*. CIE id MAY also contain *profile*, *email*.
    - |spid-icon| |cieid-icon|
  * - **response_types_supported**
    - Operarations: *one_of* |br|
      Values: MUST be *code*.
    - |spid-icon| |cieid-icon|
  * - **response_modes_supported**
    - Operarations: *subset_of* |br|
      Values: MUST be *form_post*, *query*.
    - |spid-icon| |cieid-icon|
  * - **grant_types_supported**
    - Operarations: *subset_of* |br|
      Values: MUST be *refresh_token*, *authorization_code*.
    - |spid-icon| |cieid-icon|
  * - **acr_values_supported**
    - Operarations: *subset_of* |br|
      Values: MUST be |br| *https://www.spid.gov.it/SpidL1*, |br| *https://www.spid.gov.it/SpidL2*, |br| *https://www.spid.gov.it/SpidL3*.
    - |spid-icon| |cieid-icon|
  * - **subject_types_supported**
    - Operarations: *one_of* |br|
      Values: MUST be *pairwise*.
    - |spid-icon| |cieid-icon|
  * - **id_token_signing_alg_values_supported**
    - Operarations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **id_token_encryption_alg_values_supported**
    - Operarations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **id_token_encryption_enc_values_supported**
    - Operarations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_signing_alg_values_supported**
    - Operarations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encryption_alg_values_supported**
    - Operarations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **userinfo_encryption_enc_values_supported**
    - Operarations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_methods_supported**
    - Operarations: *one_of* |br|
      Values: MUST be *private_key_jwt*
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_signing_alg_values_supported**
    - Operarations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|
  * - **claims_parameter_supported**
    - Operarations: *one_of* |br|
      Values: MUST be *true*
    - |spid-icon| |cieid-icon|
  * - **request_parameter_supported**
    - Operarations: *one_of* |br|
      Values: MUST be *true*
    - |spid-icon| |cieid-icon|
  * - **authorization_response_iss_parameter_supported**
    - Operarations: *one_of* |br|
      Values: MUST be *true*
    - |spid-icon| |cieid-icon|
  * - **client_registration_types_supported**
    - Operarations: *one_of* |br|
      Values: MUST be *automatic*
    - |spid-icon| |cieid-icon|
  * - **request_authentication_methods_supported**
    - Operarations: *one_of* |br|
      Values: MUST be *request_object*
    - |spid-icon| |cieid-icon|
  * - **request_authentication_signing_alg_values_supported**
    - Operarations: *subset_of* |br|
      Values: MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`
    - |spid-icon| |cieid-icon|

.. seealso:: 

   - :ref:`Non-normative examples of Metadata Policy<Esempio_EN7>`

