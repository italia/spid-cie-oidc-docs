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
    - Operations: *value*, *essential* |br|
      Values: value is a JSON Object that MUST contain keys, a JSON Array of RP's JSON Web Keys related to Core operations, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **grant_types**
    - Operations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of is an array that MUST contain *authorization_code*, subset_of is an array that MUST contain *authorization_code* and *refresh_token*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **id_token_signed_response_alg**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST contain one of the algorithms defined in Section :ref:`Cryptographic Algorithms <supported_algs>`, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **id_token_encrypted_response_alg**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST contain one of the algorithms defined in Section :ref:`Cryptographic Algorithms <supported_algs>`, and essential is a boolean set to *false*.
    - |cieid-icon|
  * - **id_token_encrypted_response_enc**
    - Operations: *one_of*, *essential* |br|
      Values: MUST contain one of the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>` |br|
      *essential = false*
    - |cieid-icon|
  * - **userinfo_signed_response_alg**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST contain one of the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_alg**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST contain one of the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_enc**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST contain one of the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_method**
    - Operations: *one_of*, *essential*  |br|
      Values: one_of is an array that MUST be *private_key_jwt*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **client_registration_types**
    - Operations: *subset_of*, *essential* |br|
      Values: subset_of is an array that MUST have the value *automatic*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **redirect_uris**
    - Operations: *essential* |br|
      Values: essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **client_id**
    - Operations: *essential* |br|
      Values: essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **response_types**
    - Operations: *value*, *essential* |br|
      Values: value is an array that MUST be *code*, and essential is a boolean set to *true*.
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
    - Operations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of is an array that MUST contain *authorization_code*, subset_of is an array that MUST contain *authorization_code* and *refresh_token*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **id_token_signed_response_alg**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST contain one of the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **id_token_encrypted_response_alg**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST contain the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`, and essential is a boolean set to *false*.
    - |cieid-icon|
  * - **id_token_encrypted_response_enc**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST contain one of the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`, and essential is a boolean set to *false*.
    - |cieid-icon|
  * - **userinfo_signed_response_alg**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST contain one of the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_alg**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST contain one of the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encrypted_response_enc**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST contain one of the algorithms defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_method**
    - Operations: *one_of*, *essential* |br|
      Values: one_of is an array that MUST be *private_key_jwt*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **client_registration_types**
    - Operations: *subset_of*, *essential* |br|
      Values: subset_of is an array that MUST be *automatic*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **redirect_uris**
    - Operations: *essential* |br|
      Values: essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **client_id**
    - Operations: *essential* |br|
      Values: essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **response_types**
    - Operations: *value*, *essential* |br|
      Values: value is an array that MUST be *code*, and essential is a boolean set to *true*.
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
    - Operations: *value*, *essential*  |br|
      Values: value is a JSON Object that MUST contain keys, a JSON Array of JSON Web Keys of the RP related to Core operations, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|


TA Metadata Policy for OP
^^^^^^^^^^^^^^^^^^^^^^^^^

The following claims MUST be considered in the *metadata* parameter of type *openid_provider* within the policy that the TA establishes for a direct descendant RP.

.. list-table::
  :widths: 20 20 20
  :header-rows: 1

  * - **Claim**
    - **Operarations** / **Values**
    - **Supportato da**
  * - **jwks**
    - Operarations: *value*, *essential* |br|
      Values: value is a JSON Object that MUST contain keys, a JSON Array of JSON Web Keys of the OP related to Core operations, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **revocation_endpoint_auth_methods_supported**
    - Operarations: *subset_of*, *essential* |br|
      Values: subset_of is an array that MUST be *private_key_jwt*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **code_challenge_methods_supported**
    - Operarations: *subset_of*, *essential* |br|
      Values: subset_of is an array that MUST be *S256*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **scopes_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of and subset_of are arrays that MUST contain *openid* and *offline_access*, and essential is a boolean set to *true*. For CIE id subset_of MAY also contain *profile*, *email*.
    - |spid-icon| |cieid-icon|
  * - **response_types_supported**
    - Operarations: *subset_of*, *essential* |br|
      Values: subset_of is an array that MUST be *code*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **response_modes_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of and subset_of are arrays that MUST contain *form_post* and *query*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **grant_types_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of and subset_of are arrays that MUST contain *refresh_token* and *authorization_code*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **acr_values_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: MUST contain |br| *https://www.spid.gov.it/SpidL1*, |br| *https://www.spid.gov.it/SpidL2*, |br| *https://www.spid.gov.it/SpidL3*. |br|
      *essential = true*
    - |spid-icon| |cieid-icon|
  * - **subject_types_supported**
    - Operarations: *subset_of*, *essential* |br|
      Values: subset_of is an array that MUST be *pairwise*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **id_token_signing_alg_values_supported**
    - Operarations: *subset_of*, *superset_of*, *essential*  |br|
      Values: superset_of is an array that MUST contain the MANDATORY algorithms for Signature operations, subset_of is an array that MUST contain both the MANDATORY and RECOMMENDED algorithms, and essential is a boolean set to *true*. The Signature algorithms are defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **id_token_encryption_alg_values_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of is an array that MUST contain the MANDATORY algorithms for Key Encryption operations, subset_of is an array that MUST contain both the MANDATORY and RECOMMENDED algorithms, and essential is a boolean set to *true*. The Key Encryption algorithms are defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **id_token_encryption_enc_values_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of is an array that MUST contain the MANDATORY algorithms for Content Encryption operations, subset_of is an array that MUST contain both the MANDATORY and RECOMMENDED algorithms, and essential is a boolean set to *true*. The Content Encryption algorithms are defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **userinfo_signing_alg_values_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of is an array that MUST contain the MANDATORY algorithms for Signature operations, subset_of is an array that MUST contain both the MANDATORY and RECOMMENDED algorithms, and essential is a boolean set to *true*. The Signature algorithms are defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`.
    - |spid-icon| |cieid-icon| |br|
  * - **userinfo_encryption_alg_values_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of is an array that MUST contain the MANDATORY algorithms for Key Encryption operations, subset_of is an array that MUST contain both the MANDATORY and RECOMMENDED algorithms, and essential is a boolean set to *true*. The Key Encryption algorithms are defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **userinfo_encryption_enc_values_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of is an array that MUST contain the MANDATORY algorithms for Content Encryption operations, subset_of is an array that MUST contain both the MANDATORY and RECOMMENDED algorithms, and essential is a boolean set to *true*. The Content Encryption algorithms are defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_methods_supported**
    - Operarations: *subset_of*, *essential* |br|
      Values: subset_of is an array that MUST be *private_key_jwt*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint_auth_signing_alg_values_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of is an array that MUST contain the MANDATORY algorithms for Signature operations, subset_of is an array that MUST contain both the MANDATORY and RECOMMENDED algorithms, and essential is a boolean set to *true*. The Signature algorithms are defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **claims_parameter_supported**
    - Operarations: *value*, *essential* |br|
      Values: value is a boolean that MUST be *true*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **request_parameter_supported**
    - Operarations: *value*, *essential* |br|
      Values: value is a boolean that MUST be *true*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **authorization_response_iss_parameter_supported**
    - Operarations: *value*, *essential* |br|
      Values: value is a boolean that MUST be *true*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **client_registration_types_supported**
    - Operarations: *subset_of*, *essential* |br|
      Values: subset_of is an array that MUST be *automatic*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **request_authentication_methods_supported**
    - Operarations: *value*, *essential* |br|
      Values: value is a JSON object containing an array *authorization_endpoint* that MUST be *request_object*, and essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **request_authentication_signing_alg_values_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of is an array that MUST contain the MANDATORY algorithms for Signature operations, subset_of is an array that MUST contain both the MANDATORY and RECOMMENDED algorithms, and essential is a boolean set to *true*. The Signature algorithms are defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **request_object_signing_alg_values_supported**
    - Operarations: *subset_of*, *superset_of*, *essential* |br|
      Values: superset_of is an array that MUST contain the MANDATORY algorithms for Signature operations, subset_of is an array that MUST contain both the MANDATORY and RECOMMENDED algorithms, and essential is a boolean set to *true*. The Signature algorithms are defined in the Section :ref:`Cryptographic Algorithms <supported_algs>`.
    - |spid-icon| |cieid-icon|
  * - **issuer**
    - Operarations: *essential* |br|
      Values: essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **authorization_endpoint**
    - Operarations: *essential* |br|
      Values: essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **token_endpoint**
    - Operarations: *essential* |br|
      Values: essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **userinfo_endpoint**
    - Operarations: *essential* |br|
      Values: essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **introspection_endpoint**
    - Operarations: *essential* |br|
      Values: essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|
  * - **revocation_endpoint**
    - Operarations: *essential* |br|
      Values: essential is a boolean set to *true*.
    - |spid-icon| |cieid-icon|

.. seealso:: 

   - :ref:`Non-normative examples of Metadata Policy<Esempio_EN7>`
