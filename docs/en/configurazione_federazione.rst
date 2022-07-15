.. include:: ./common_definitions.rst


Configuration of the Federation 
-------------------------------

The configuration of the Federation is published by the Trust Anchor inside its :ref:`Entity Configuration<entity_configuration_ta>`, available at a well known web path and corresponding to a 
**.well-known/openid-federation**.

All the members MUST obtain the Federation configuration before the operational phase and they
MUST keep it up-to-date on a daily basis. The Federation configuration contains the Trust Anchor
public key for the signature operations, the maximum number if Intermediaries allowed between a Leaf and the Trust Anchor (**max_path length**) and the authorities who are enabled to issue the Trust Marks (**trust_marks_issuers**).

Please find a non-normative example of :ref:`Entity Configuration response Trust Anchor<Esempio_EN1.4>` here.

For further details, please read the Section about the :ref:`Entity Configuration<Entity_Configuration>`.


How to participate
------------------

To take part in the SPID and CIEid Federations, a Leaf Entity must publish its own configuration
(Entity Configuration) at its own web endpoint :ref:`.well-known/openid-federation<Esempio_EN1>`.

The technical and administrative representatives complete the administrative procedure,
defined by the Federation Authority or by an Intermediary (SA),
for registering a new entity or for updating a preexisting one. 

The Federation Authority or an Intermediary, after doing all the required technical and administrative controls, registers the public keys of the Leaf and releases a proof of Federation membership, 
in the form of Trust Mark (TM).

The Leaf MUST include the TM inside its own Federation configuration (Entity Configuration) as proof of
success in the Onboarding process.

The Federation Authority or an Intermediary MUST publish the Leaf statement of recognition 
(Entity Statement) containing the Federation public keys of the Leaf and the TMs released for it.
The Federation Authority or an Intermediary CAN publish a `Metadata policy <https://openid.net/specs/openid-connect-federation-1_0.html#rfc.section.5.1>`_ to force the change
if the OIDC Metadata of the subordinate entity, in the parts where it might be needed.
