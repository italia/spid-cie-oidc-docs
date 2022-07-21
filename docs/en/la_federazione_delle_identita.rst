.. include:: ../common/common_definitions.rst

The Italian eID Federations
---------------------------

A Digital Identity Federation is an infrastructure inside which many organizations, with different domains,
participate in the same regulatory framework for building a mechanism of trust, both administrative, by 
stipulating conventions and getting accreditation by one or more impartial authorities, and technological, by 
adopting standards of interoperability that allow safe data interchange.

This configuration establishes the levels of guarantee and security that are appropriate for an individual, in order to authenticate on a web service (Service Provider) using their own digital identity, released 
by another web service (Identity Provider).

The members (RP or OP) who are recognized inside the same Federation, obtain Metadata from each
other. The Metadata contains the public keys for the operations of digital signature and encryption, 
and the information needed for the data interchange.

The Metadata are certified by a trusted party who is AgID in the SPID Federation and the Ministry of Interior in the CIE Federation. They both correspond to the Federation Authorities.

Both SPID and CIE id implement OpenID Connect Federation 1.0 and extend some functionalities, achieving
a solid implementation and producing the good practices for its adoption. For more details about the 
standard please refer to the official specifications `OIDC-FED`_ and the section :ref:`Differences with OIDC Federation 1.0<differenze_con_oidc_federation>`. 


Why OIDC Federation
+++++++++++++++++++

The OIDC Federation is a hierarchical model:

 - **Dynamic**. The trust may be dynamically established during the first authentication request.
   The Federation Authorities expose an endpoint that supplies signed statements about the subordinate
   Entities. These statements contain the public keys of the subordinat Entities and the Metadata policy.
   The Federation Authorities can disable an Entity in the Federation at every moment, simply by 
   stopping supplying statements about it.
 - **Distributed**. The trust is distributed among several parties. It is up to the verifier to decide
   what path to take for solving the trust (many parties and two Federation Authorities).
 - **Scalable**. It reduces significantly the onboarding costs, according to the delegation principle, with
   the institution of Intermediate Entities (SA).
 - **Transparent**. Any Entity involved in the Federation can always build the trust independently and
   securely. Furthermore, the Federation composition, in all its parts, becomes navigable in real time 
   through its API.

.. image:: ../../images/spid_cie_oidc_federation_model.svg
    :width: 100%

*Tree scheme representing the structure of the SPID and CIE id Federations. At the base there are the Federation Authorities of SPID and CIE id and, going up, the OPs that have no Intermediaries, the RPs and the 
Intermediaries that, in turn, aggregate othe RPs.*

Configuration of the Federation 
+++++++++++++++++++++++++++++++

The configuration of the Federation is published by the Trust Anchor inside its :ref:`Entity Configuration<entity_configuration_ta>`, available at a well known web path and corresponding to a 
**.well-known/openid-federation**.

All the members MUST obtain the Federation configuration before the operational phase and they
MUST keep it up-to-date on a daily basis. The Federation configuration contains the Trust Anchor
public key for the signature operations, the maximum number if Intermediaries allowed between a Leaf and the Trust Anchor (**max_path length**) and the authorities who are enabled to issue the Trust Marks (**trust_marks_issuers**).

Please find a non-normative example of :ref:`Entity Configuration response Trust Anchor<Esempio_EN1.4>` here.

For further details, please read the Section about the :ref:`Entity Configuration<Entity_Configuration>`.

How to participate
++++++++++++++++++

To take part in the SPID and CIEid Federations, a Leaf Entity must publish its own configuration
(Entity Configuration) at its own web endpoint :ref:`.well-known/openid-federation<Esempio_EN1>`.

The technical and administrative representatives complete the administrative procedure,
defined by the Federation Authority or by an Intermediary (SA),
for registering a new Entity or for updating a preexisting one. 

The Federation Authority or an Intermediary, after doing all the required technical and administrative controls, registers the public keys of the Leaf and releases a proof of Federation membership, 
in the form of Trust Mark (TM).

The Leaf MUST include the TM inside its own Federation configuration (Entity Configuration) as proof of
success in the Onboarding process.

The Federation Authority or an Intermediary MUST publish the Leaf Entity Statement containing the Federation public keys of the Leaf and the TMs released for it.
The Federation Authority or an Intermediary CAN publish a `Metadata policy <https://openid.net/specs/openid-connect-federation-1_0.html#rfc.section.5.1>`_ to force the change
to the OIDC Metadata of the subordinate Entity, in the parts where it might be needed.



