.. include:: ../common/common_definitions.rst

Terms and Acronyms
------------------

Terms
+++++

Following, the terms used by `OIDC-FED#Section_1.2`_ and this documentation.

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - **Fedetarion Authority**
      - A legal Entity that handles the trust among the parties involved in the Federation, regulates the 
        funcional aspects and the onboarding procedures. It is about a **Trust Anchor** (the *trust* root). 
    * - **Trust Anchor**
      - Entity handled by the Federation Authority that represents the Federation, its configuration and the trust root.
    * - **Intermediate Entity** or **Intermediary**
      - An Intermediate Entity (SA), facilitates the onboarding process in the Federation and MAY handle the functionalities on behalf of its subordinate (Aggregated) Entities. Inside the Federation, an SA publishes its own configuration and the Entity statements of its subordinates, according to the rules defined by the Federation.
    * - **Leaf Entity** or **Leaf**
      - Entity defined by OpenID Connect as Relying Party and OpenID Provider.
    * - **Entity**
      - Participant to the the Federation. It may be a Trust Anchor, Intermediary or Leaf.
    * - **Entity Configuration**
      - Federation metadata issued by an Entity about itself, in the form of a self-signed JWT :rfc:`7515` containing the Entity's configuration. It contains the public Federation's signing keys, the OIDC metadata, the URLs of its superiors authorities and the Trust Marks issued by authorities that are recognizable inside the Federation and that certify the Entity's compliance to specific profiles.
    * - **Entity Statement**
      - Statement issued by a superior Entity (Trust Anchor or Intermediary) regarding
        a subordinate Entity (RP, OP or Intermediary), in the form of a signed JWT :rfc:`7515`, containing
        the public key of the Entity, the Trust Marks issued by the Entity itself and the Metadata policy 
        to be applied to the Entity's Metadata.
    * - **Trust Mark**
      - JWT :rfc:`7515` signed by an issuing Entity about a participating Entity. It certifies that this
        Entity complies with profiles that are recognizable inside the Federation (public of private RP, public or private Intermediate Entity, etc.). A Leaf that aquires a Trust Mark during an Onboarding process, MUST include it in its Entity Configuration, such as an identification badge.
    * - **Metadata**
      - A Metadata document describes the implementation of an OpenID Connect Entity. The implementations 
        of all the Entities share the Metadata to establish a common ground of trust and interoperability. 
    * - **Metadata policy**
      - The Trust Anchor publishes rules and policies to be applied to the subordinates' Metadata, 
        specifying what values and values subsets are allowed for a given Metadata claim.
    * - **Authority hint**
      - An array of URLs regarding the identifiers of the superior Entities, Trust Anchor or 
        Intermediary, that MUST issue an Entity Statement for their own subordinates. 
    * - **Metadata Discovery**
      - Collection of Entity Configuration / Statements, from a Leaf Entity up to the Trust Anchor
    * - **Trust Chain**
      - Validation Procedure of the sequence of Entity Configuration / Statements that have
        been collected through the Metadata Discovery, whose positive result is a final Metadata regarding 
        an Entity, and the expiry date before which it must be updated.
    * - **Onboarding**
      - Registration Procedure of a new Entity inside the SPID and CIE Federations.
    * - **Federation Endpoint**
      - Endpoints used to fetch and resolve Entity statements, query a list of all the subordinate Entities and check the trust mark status.


Acronyms
++++++++

In this section are defined all the acronyms that are used throughout the text.

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - **SPID**
      - Public System of Digital Identity
    * - **CIEid**
      - The Italian digital identity system based on the Electronic ID Card (CIE), whose owner is the
        Interior Ministry. The technical and operative management is given to the State Mint and Polygraphic Institute (IPZS).
    * - **OIDC**
      - OpenID Connect
    * - **OIDC-FED**
      - `OIDC Federation 1.0 <https://openid.net/specs/openid-connect-federation-1_0.html>`_.
    * - **IOF**
      - Italian OIDC Federation 1.0.
    * - **FA**
      - Federation Authority.
    * - **TA**
      - OIDC Federation Trust Anchor
    * - **AgID**
      - Agenzia per l'Italia Digitale, FA/TA of SPID
    * - **MinInterno**
      - Ministry of Interior, FA/TA of CIEid.
    * - **OP**
      - OpenID Provider (Leaf Entity)
    * - **RP**
      - Relying Party (Leaf Entity) 
    * - **SA**
      - Intermediate Entity or Intermediary. An intermediate Entity that can handle all the Federation
        aspects of one or more RPs.
    * - **AA**
      - Attribute Authority, handler of the qualified attribues (Leaf Entity)
    * - **TM**
      - Trust Mark
    * - **EC**
      - Entity Configuration
    * - **ES**
      - Entity Statement
    * - **URL**
      - Uniform Resource Locator, it is a web address
    * - **JWT**
      - See :rfc:`7519` Jones, M., Bradley, J. and N. Sakimura, "JSON Web Token (JWT)", RFC 7519, DOI 10.17487/RFC7519, May 2015. 
    * - **RS**
      - OAuth Resource Server
    * - **$JWT**
      - The value of a JWT (JSON Web Token).



Conventions and Normative Terms
+++++++++++++++++++++++++++++++

The keywords "MUST", "MUST NOT", "REQUIRES", "REQUIRE", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" and "OPTIONAL" in the present document must be interpreted as described at BCP 14 :rfc:`2119` :rfc:`8174` when and only when they appear in capital letters.

Le notations [...] and ... mean that the text has been cut off for editor's requirements.

*base64url* denotes the URL-safe base64 coding without padding, defined at :rfc:`7515#section-2`.

.. warning::
    |warning-message-en|
