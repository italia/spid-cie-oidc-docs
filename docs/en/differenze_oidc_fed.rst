.. include:: ../common/common_definitions.rst

.. _differenze_con_oidc_federation:

Differences with OIDC Federation
--------------------------------

This section lists the differences between the official standard and the SPID / CIE implementation.


Client Registration
+++++++++++++++++++

SPID supports only **automatic_client_registration**. The **implicit** flow is not supported.


Listing endpoint
++++++++++++++++

In the SPID / CIE Federations, for this endpoint, the claim **entity_type** is added to all the other `OIDC-FED`_ standard claims, in order to obtain a filter on the type of subordinate Entities. This need apecifically allows filtering Entities of type **federation_entity**, **openid_relying_party**, **openid_provider** and **oauth_resource**.


Trust Mark
++++++++++

In the SPID and CIE id Federations, using Trust Marks is not mandatory. Rather, in the SPID Federation it is mandatory to expose them. For more details about the reasons why the Trust Marks are required, please see the section :ref:`Security Considerations <Considerazioni_di_Sicurezza>`.


Unsupported Claims in the Entity Statements
+++++++++++++++++++++++++++++++++++++++++++

Since SPID and CIE don't need any additional claim of the Federation scope, they don't need the claim **crit**. Likewise, the claims **aud**, **naming_constraints**, **policy_language_crit** and **trust_anchor_id** are not supported. Any possible presence of these claims does not have implications, they are simply ignored until possible future communications about their regulation.
