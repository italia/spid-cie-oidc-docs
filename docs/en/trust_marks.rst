.. include:: ../common/common_definitions.rst

.. _Trust_Mark:

Trust Marks
===========

The **Trust Marks (TM)** are signed JWT :rfc:`7515` and represent the statements of compliance with a well defined set of requirements of trust and/or interoperability, or an agreement among the parties involved in the Federation. 

The main aim of the TMs is exposing information that is not required by the OpenID Connect Core protocol,
but turns out to be useful in the federative context.

Typical examples include the Entity's national or international identification code (fiscal code, IPA code, VAT number), institutional contacts and so forth, as defined at `OIDC-FED`_. Further data may be added
by the issuing subject.

During the registration process of a new Leaf Entity (onboarding), the TMs are issued and signed by the TA
or its Intermediates (SA) or by Attribute Authorities (AA), if they are defined inside the attribute **trust_mark_issuers**, published inside the TA's Entity Configuration.

Each member Entity MUST expose, in its own configuration (EC), the TMs released by the issuing authorities.

In the CIE / SPID scenario, a TM is signed by the TA **MinInterno** / **Agid** or their Intermediates (SA) or by Attribute Authorities (AA).

The TA defines the subjects who are enabled to issue TMs that are recognizable inside the Federation,
and this is done by the claim **trust_marks_issuers**, contained in its own Entity Configuration. 
The value of the claim **trust_marks_issuers** is composed by a JSON Object having as keys the TM identifiers, and as values the list of identifiers (URLs) or the Entities who are enabled to issue them.

In the following, a non-normative example of the object **trust_marks_issuers** inside the TA's Entity Configuration.


.. code-block:: json

 {
     "trust_marks_issuers":{
         "https://registry.agid.gov.it/openid_relying_party/public/":[
             "https://registry.spid.agid.gov.it/",
             "https://public.intermediate.spid.it/"
         ],
         "https://registry.agid.gov.it/openid_relying_party/private/":[
             "https://registry.spid.agid.gov.it/",
             "https://private.other.intermediate.it/"
         ]
     }
 }

Each member Entity MUST expose in its configuration (EC), the TMs released by the issuing authority.

In the CIE / SPID scenario, a TM is signed by the TA **MinInterno** / **Agid** or their Intermediates (SA) or
Attribute Authorities (AA).

The TA defines the subjects that are enabled to issue TMs that are recognizable inside the Federation,
and it does it with the claim **trust_marks_issuers**, that is present in its Entity Configuration. 
The value of the attribute **trust_marks_issuers** is composed by a JSON Object whose keys are the TM identifiers and whose values are the list of the identifiers (URLs) of the Entities enabled 
to issue them.

The Trust Marks represent the first filter for establishing the trust among the parties. 
They are essential elements for starting the Metadata resolution. 
In their absence, an Entity is not recognized as a member inside the Federation.

Inside the SPID Federation, the Trust Marks have unique identifiers (claim id) in URL format, that adopt 
the following structure: **https:// <domain> / <entity_role> / <trustmark_profile> / [extension /]**

In the following, some non-normative examples:


 - TM RP public: **\https://registry.agid.gov.it/openid_relying_party/public/**
 - TM SA private: **\https://registry.agid.gov.it/intermediate/private/full/**
 - TM AA: **\https://registry.agid.gov.it/oauth_resource/public/**


The following table defines the <entity_role> that are recognizable inside the SPID and CIE id Federations:


.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Type**
      - **Description**
      - **Entity**
    * - **openid_relying_party**
      - the Entity in the claim *sub* is an RP.
      - RP
    * - **openid_provider**
      - the Entity in the claim *sub* is an OP.
      - OP
    * - **intermediate**
      - the Entity in the claim *sub* is an Intermediate.
      - SA
    * - **oauth_resource**
      - the Entity in the claim *sub* is an Attribute Authority.
      - AA

The following table defines the <trustmark_profile> that are recognizable inside the SPID and CIE id Federations:


.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Profile**
      - **Description**
      - **Entity**
    * - **public**
      - the Entity in the claim *sub* belongs to the Italian Public Administration.
      - RP, OP, SA, AA
    * - **private**
      - the Entity in the claim *sub* belongs to the private sector.
      - RP, OP, SA, AA


**federation_entity** Trust Mark
--------------------------------

In addition to the claims of the **public** and **private** profiles, the profile **intermediate** identifies the SA and adds the extensions **full** and **light** in the **sa_profile** claim, according to the ways of operation towards the subordinate Entities.

.. seealso::

   See Section :ref:`Intermediate Entities in the Federative context <Soggetti_aggregatori>`


**oauth_resource**  Trust Mark
------------------------------

In addition to the claims of the **public** and **private** profiles, the profile **oauth_resource** 
identifies the AA and adds the following mandatory claims:

.. list-table::
    :widths: 20 60
    :header-rows: 1

    * - **Claim**
      - **Description**
    * - **policy_uri**
      - URL where the AA privacy policy is available.
    * - **tos_uri**
      - URL where the AA info policy is available.
    * - **claims**
      - List of JSON Objects that define the user's attributes, required by the AA. 
        Example: |br| ``{"https://attributes.eid.gov.it/fiscal_number":{"essential":true},`` |br| ``"email":{"essential":true},}``
    * - **service_documentation**
      - URL where the OAS3 document, that describes how the AA services works, is available.


Trust Mark Validation
---------------------

There are two ways of validating a Trust Mark:

 1. **Static** Validation. The Trust Mark is validated through its issuing authority's public key (claim **iss**), on top of the correspondence of the claim **sub** to the same claim of the Entity Configuration in which it is contained, and on top of the expiry value (claim **exp**)

 2. **Dynamic** Validation. The Federation members can query the endpoint :ref:`trust mark status<federation_endpoint>` supplied by its issuer (claim **iss**), for a real-time checking of the TMs that it has issued.

All the Entities that release Trust Marks, MUST expose a Trust Mark status endpoint for allowing the **dynamic** validation.

.. seealso:: 

  - `OIDC-FED`_ Section .5.3.2.

Trust Mark Revocation
---------------------

A Trust Mark can be revoked at any moment only and exclusively by the issuing subject. 
For example, in case of exclusion of an Aggregated Subject by the Federation Authority, it communicates the exclusion of the Aggregated Subject to the SA. Consequently, the SA MUST revoke the TM for its subordinate.


.. note::
   
   In case of TM revocation, the **dynamic** validation gives a negative result, while the **static** 
   validation keeps on giving a positive result, unless the signing encryption keys of the TM-releasing subject are rotated.


.. _ComposizioneTM:

Trust Mark Composition
----------------------

The claims defined inside the TMs are compliant with the elements defined in the OIDC Federation 1.0 (`OIDC-FED`_) standard. See the following list.

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Supported by**
    * - **iss**
      - String. URL that uniquely identifies its issuing Authority.
      - |spid-icon| |cieid-icon|
    * - **sub**
      - String. URL that uniquely identifies the subject for which the Trust Mark has been issued.
      - |spid-icon| |cieid-icon|
    * - **id**
      - String. Unique identifier of the Trust Mark. It is an URL with the following structure: |br|
        **<TA domain>/<entity_type>/<trustmark_profile>/** |br|
        non-normative example: ``https://registry.interno.gov.it/openid_relying_party/public/``
      - |spid-icon| |cieid-icon|
    * - **iat**
      - UNIX Timestamp with the JWT issuance time, coded as NumericDate as indicated at :rfc:`7519`
      - |spid-icon| |cieid-icon|
    * - **logo_uri**
      - String. An URL that points to the logo that represents the Trust Mark.
      - |spid-icon| |cieid-icon|
    * - **exp**
      - UNIX Timestamp with the JWT expiry time, coded as NumericDate as indicated at :rfc:`7519`
      - |spid-icon| |cieid-icon|
    * - **ref**
      - String. URL that points to public web information, about this Trust Mark
      - |spid-icon| |cieid-icon|
    * - **organization_type**
      - String. Specifies if the Entity belongs to the Italian Public Administration or the private sector (**public** or **private**)
      - |spid-icon| |cieid-icon|
    * - **id_code**
      - JSON Object. It contains one or more ogranization identification codes. Available claims are: 
        - **ipa_code**: REQUIRED for public organization.
        - **aoo_code**: OPTIONAL.
        - **uo_code**: OPTIONAL. 
        - **vat_number**: REQUIRED for private organization only if *fiscal_number* is not available.
        - **fiscal_number**: REQUIRED for private organization only if *vat_number* is not available.
      - |spid-icon| |cieid-icon|
    * - **email**
      - String. Institutional e-mail or PEC of the Organization.
      - |spid-icon| |cieid-icon|
    * - **organization_name**
      - String. The complete name of the service-supplying Entity.
      - |spid-icon| |cieid-icon|

.. warning::

  The value in the claim **exp** MUST NOT be greater than the duration of the agreements submitted during the onboarding process, between the Trust Mark issuer and the Organizations receiving the TM.
 

.. seealso::

  - `OIDC-FED`_ Section 5.3.1.
  - Non-normative example: :ref:`Trust Mark issued by TA to a RP <Esempio_EN1.5>`, :ref:`Trust Mark issued by TA to a SA <Esempio_EN1.6>`, :ref:`Trust Mark issued by SA to a RP <Esempio_EN1.7>`,


