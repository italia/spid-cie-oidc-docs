.. include:: ../common/common_definitions.rst

.. _Entity_Configuration:

Entity Configuration
--------------------

An **Entity Configuration (EC)** is a Federation Metadata in Jose format, signed by its issuing subject 
and regarding itself, published at the web endpoint **.well-known/openid-federation**.

.. _firma_EC:

Entity Configuration Signature
++++++++++++++++++++++++++++++

The JWT :rfc:`7515` signature occurs through the RSA SHA-256 (RS256) algorithm. All the Federation
members MUST support this signing algorithm. All the signature-check operations regarding the ESs, ECs and TMs,
are carried out with the Federation public keys.

.. warning::
  The Federation keys must be distinguished by the OIDC Core ones. The latter ones are contained in the OIDC Metadata. An EC contains both the Federation public keys and the OIDC Metadata.


Entity Configuration - common claims
++++++++++++++++++++++++++++++++++++

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **iss**
     - String. Identifier of the issuing Entity.
     - |spid-icon| |cieid-icon|
   * - **sub**
     - String. Identifier of the Entity to which it is referred.
     - |spid-icon| |cieid-icon|
   * - **iat**
     - UNIX Timestamp with the time of generation of the JWT, coded as NumericDate as indicated at :rfc:`7519`
     - |spid-icon| |cieid-icon| 
   * - **exp**
     - UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated at :rfc:`7519`.
     - |spid-icon| |cieid-icon|
   * - **jwks**
     - A JSON Web Key Set (JWKS) :rfc:`7517` that represents the public part of the signing keys of the 
       Entity at issue. Each JWK in the JWK set MUST have a key ID (claim kid).
     - |spid-icon| |cieid-icon|
   * - **metadata**
     - JSON Object. Each key of the JSON Object represents an identifier of the type of
       :ref:`Metadata<metadata_oidc>` and each value MUST be a JSON Object that represents
       the Metadata, according to the Metadata schema of that type.

       An Entity configuration MAY contain more Metadata statements, but only one for each type of
       Metadata (<**entity_type**>). 

       The allowed types are the following:

       - openid_relying_party
       - openid_provider
       - federation_entity
       - oauth_authorization_server
       - oauth_resource
       - trust_mark_issuer
     - |spid-icon| |cieid-icon|

.. warning::
  Inside the EC the claims **iss** e **sub** contain the same value (URL).


Entity Configuration Leaves and Intermediaries
++++++++++++++++++++++++++++++++++++++++++++++

In addition to the previously defines claims, the EC of the Leaf and Intermediate Entities, contain also
the following claims:


.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **authority_hints**
     - Array if URLs. It contains a list of URLs of the superior Entities, such as TA or SA, 
       that MAY issue an ES related to this subject.
     - |spid-icon| |cieid-icon|
   * - **trust_marks**
     - A JSON Array containing the Trust Marks. See the Section :ref:`Trust Mark <Trust_Mark>`. 
       Required for all the members except the Trust Anchor.
     - |spid-icon| |cieid-icon|

.. seealso:: 

   - :ref:`Non-normative example of EC of an OP<Esempio_EN1.2>`
   - :ref:`Non-normative example of EC of a RP<Esempio_EN1.1>`
   - :ref:`Non-normative example of EC of a Federation Intermediary (SA)<Esempio_EN1.3>`

.. _entity_configuration_ta:

Entity Configuration Trust Anchor
+++++++++++++++++++++++++++++++++

The ECs of a TA, other than the common claims of all the other members, contain also the following ones:

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **constraints**
     - JSON Object that describes the Trust Chain bounds and MUST contain the attribute **max_path_length**.
       It represents the maximum number of SAs between a Leaf and the TA.
     - |spid-icon| |cieid-icon|
   * - **trust_marks_issuers**
     - JSON Array that indicates which Federation authorities are considered trustworthy
       for issuing specific TMs, assigned with their unique identifiers.
     - |spid-icon| |cieid-icon|

.. seealso:: 

   - :ref:`Non-normative example of EC of a TA<Esempio_EN1.4>`
   
