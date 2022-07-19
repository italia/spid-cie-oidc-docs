.. include:: ./common_definitions.rst


.. _Trust_Mark:

Trust Marks
===========

The **Trust Marks (TM)** are signed JWT :rfc:`7515` and represent the statement of compliance with a well defined set of requirements of trust and/or interoperability, or an agreement among the parties involved in the Federation. 

The main aim of the TMs is exposing information that is not required by the OpenID Connect Core protocol,
but turns out to be useful in the federative context.

Typical examples include the entity's national or international identification code (fiscal code, IPA code, VAT number), institutional contacts and so forth, as defined at `OIDC-FED`_. Further data may be added
by the issuing subject.

During the registration process of a new Leaf Entity (onboarding), the TMs are issued and signed by the TA
or its Intermediaries (SA) or by Attribute Authorities (AA), if they are defined inside the attribute **trust_mark_issuers**, published inside the TA's Entity Configuration.

Each member entity MUST expose, in its own configuration (EC), the TMs released by the issuing authorities.

In the CIE / SPID scenario, a TM is signed by the TA **MinInterno** / **Agid** or their Intermediaries (SA) or by Attribute Authorities (AA).

The TA defines the subjects who are enabled to issue TMs that are recognizable inside the Federation,
and this is done by the claim **trust_marks_issuers**, contained in its own Entity Configuration. 
The value of the claim **trust_marks_issuers** is composed by a JSON Object having as keys the TM identifiers, and as values the list of identifiers (URLs) or the entities who are enabled to issue them.

Following, a non-normative example of the object **trust_marks_issuers** inside the TA's Entity Configuration.


.. code-block::

 {
     "trust_marks_issuers":{
         "https://registry.agid.gov.it/openid_relying_party/public/":[
             "https://registry.spid.agid.gov.it/",
             "https://public.intermediary.spid.it/"
         ],
         "https://registry.agid.gov.it/openid_relying_party/private/":[
             "https://registry.spid.agid.gov.it/",
             "https://private.other.intermediary.it/"
         ]
     }
 }


Trust Mark Validation
---------------------

There are two ways of validating a Trust Mark:

 1. **Static** Validation. The Trust Mark is validated through its issuing authority's public key (claim **iss**), on top of the correspondence of the claim **sub** to the same claim of the Entity Configuration in which it is contained, and on top of the expiry value (claim **exp**)

 2. **Dynamic** Validation. The Federation members can query the endpoint :ref:`trust mark status<federation_endpoint>` supplied by its issuer (claim **iss**), for a real-time checking of the TMs that it has issued.

All the entities that release Trust Marks, MUST expose a Trust Mark status endpoint for allowing the 
**dynamic** validation.

.. seealso:: 

  - `OIDC-FED#Section.5.3.2`_


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

The claims defined inside the TMs, comply to what defined in the OIDC Federation 1.0 (`OIDC-FED`_) standard. Following, the list.

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
      - UNIX Timestamp with the JWT generation time, coded as NumericDate as indicated at :rfc:`7519`
      - |spid-icon| |cieid-icon|
    * - **logo_uri**
      - String. An URL that points to the logo that represents the Trust Mark.
      - |spid-icon| |cieid-icon|
    * - **exp**
      - UNIX Timestamp with the JWT expiry time, coded as NumericDate as indicated at :rfc:`7519`
      - |spid-icon| |cieid-icon|
    * - **ref**
      - String. URL that points to information present on the web, about this Trust Mark
      - |spid-icon| |cieid-icon|
    * - **organization_type**
      - String. Specifies if the entity belongs to the Italian Public Administration or the private sector (**public** or **private**)
      - |spid-icon| |cieid-icon|
    * - **id_code**
      - String. Identification code of the Organization. Depending on the organization type, it must be
        indicated an IPA code (for the public organization type) or the VAT number (for the private type).
      - |spid-icon| |cieid-icon|
    * - **email**
      - String. Institutional e-mail or PEC of the organization.
      - |spid-icon| |cieid-icon|
    * - **organization_name**
      - String. The complete name of the service-supplying entity.
      - |spid-icon| |cieid-icon|

.. warning::
  In case of CIEid, the public organizations that have not only the **IPA code**, but also a **unique AOO code**, MUST include this latter one in the claim **id_code**, in the format *<IPA_code>-<AOO_code>*.
  Furthermore, the value in the claim **exp** MUST NOT be greater than the duration of the specific 
  conventions/agreements concluded in the onboarding phase, between the MinInterno and the organizations 
  that receive the TM.
 

.. seealso::

 * `OIDC-FED#Section.5.3.1`_



.. toctree:: 
   :maxdepth: 1

   trust_marks_spid.rst
   trust_marks_cie.rst
