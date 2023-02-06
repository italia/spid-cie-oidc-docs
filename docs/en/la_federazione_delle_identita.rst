.. include:: ../common/common_definitions.rst

The Italian eID Federations
---------------------------

A Digital Identity Federation is an infrastructure inside which many organizations, with different domains,
participate in the same regulatory framework for building a mechanism of trust, both administrative, by 
stipulating conventions and getting accreditation by one or more authorities and technological by 
adopting standards of interoperability.

This configuration establishes the levels of assurance and security that are appropriate for the
citizens in order to authenticate on a web service (Service Provider) using their own digital identity, released 
by another web service (Identity Provider).

The participants (RP or OP) who are recognized inside the same Federation, obtain Metadata from each
other. The Metadata contains the public keys for the operations of digital signature and encryption, 
and the information needed for the data interchange.

The Metadata are certified by a trusted party who is AgID in the SPID Federation and the Ministry of Interior in the CIE Federation. They both correspond to the Federation Authorities.

Both SPID and CIE id implement OpenID Connect Federation 1.0 and extend some functionalities, achieving
a solid implementation and producing the good practices for its adoption. For more details about the 
standard please refer to the official specifications `OIDC-FED`_ and the section :ref:`Differences with OIDC Federation 1.0<differenze_con_oidc_federation>`. 


OpenID Connect Federation
+++++++++++++++++++++++++

The OIDC Federation produces an infrastructure of trust that is:

 - **Dynamic**. The trust may be dynamically established during the first authentication request.
   The Federation Authorities expose an endpoint that supplies signed statements about the subordinate
   Entities. These statements contain the public keys of the subordinate Entities and the Metadata policy.
   The Federation Authorities can disable an Entity in the Federation at every moment, simply by 
   stopping supplying statements about it.
 - **Scalable**. It reduces significantly the onboarding costs, according to the delegation principle, with
   the institution of Intermediate Entities (SA).
 - **Transparent**. Any Entity involved in the Federation can always build the trust towards an Entity
   securely. Furthermore, the federation composition, in all its parts, becomes navigable in real time 
   through the Federation API.

.. image:: ../../images/spid_cie_oidc_federation_model.svg
    :width: 100%

*At the base of the trees there are the Federation Authorities of SPID and CIE id and, going up, the OPs that have no Intermediates, the RPs and the 
Intermediates that, in turn, aggregate other RPs.*

Configuration of the Federation 
+++++++++++++++++++++++++++++++

The configuration of the Federation is published by the Trust Anchor inside its :ref:`Entity Configuration<entity_configuration_ta>`, available at a well known web path and corresponding to a 
**.well-known/openid-federation**.

All the members MUST obtain the Federation configuration before the operational phase and they
MUST keep it up-to-date on a daily basis. The Federation configuration contains the Trust Anchor
public keys for the signature operations, the maximum number of Intermediates allowed between a Leaf and the Trust Anchor (**max_path length**) and the authorities who are enabled to issue the Trust Marks (**trust_marks_issuers**).

Here a non-normative example of :ref:`Entity Configuration response Trust Anchor<Esempio_EN1.4>`.

For further details, please read the section about the :ref:`Entity Configuration<Entity_Configuration>`.

How to participate
++++++++++++++++++

The participant MUST publish its configuration
(Entity Configuration) at the webpath :ref:`.well-known/openid-federation<Esempio_EN1>`.

The technical and administrative representatives complete the onboarding procedure,
defined by the Federation Authority or by an Intermediate (SA),
in order to register a new Entity or for updating a preexisting one. 

The Federation Authority or an Intermediate, after doing all the required technical and administrative controls, registers the public keys of the onboarded Entity and releases a proof of Federation membership, 
in the form of Trust Mark (TM).

The Leaf MUST include the TM inside its own Federation configuration (Entity Configuration) as proof of
success in the Onboarding process.

The Federation Authority or an Intermediate MUST publish the Leaf Entity Statement containing the Federation public keys of the onboarded Entity and the TMs released for it.
