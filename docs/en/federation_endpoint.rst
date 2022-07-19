.. include:: ./common_definitions.rst

.. _federation_endpoint:

Federation Endpoint
-------------------

All the entities MUST contain the following endpoints:

 - **/.well-known/openid-federation**: gives the `Entity Configuration <Entity_Configuration>`__ (for 
   more details, see `OIDC-FED#Section.6`_)
 - **resolve entity statement endpoint**: gives the final Metadata, the Trust Chain and the Trust Marks
   regarding another subject. For more details, see `OIDC-FED#Section.7.2`_)

.. warning::
  The **resolve entity statement endpoint** MUST NOT return any information regarding a subject
  about which it hasn't previously collected the statements and calculated the Trust Chain. 
  In case the TMs are no more valid at the moment of the request, they MUST NOT be included in the
  response.

In addition to the Federation endpoints reported before, the entities of type **TA** or **SA** MUST provide the following endpoints:


 - **fetch entity statement endpoint**: returns the ESs regarding a direct subordinate subject. 
   For obtaining the ES of an entity, at least its entity identifier is needed. (For more details, see `OIDC-FED#Section.7.1`_).
 - **trust mark status endpoint**: allows an entity to test if a TM is still active or not. The query MUST
   be sent to the subject that has released that TM. (For more details, see `OIDC-FED#Section.7.4`_).
 - **entity listing endpoint**: returns the list of the subordinate entities registered by the TA or an SA.
   (For more details, see `OIDC-FED#Section.7.3`_).

An entity of type **AA**, in addition to the common Federation endpoints like all the entities, MUST also include the **trust mark status endpoint** for allowing the dynamic validation of the TMs, released by the AA.


.. warning::
  With respect to what defined in the OIDC-FED, to the **entity listing endpoint** is added the optional
  claim **entity_type**, that is a filter of the entity type of the subordinates.

.. _generic_error_response:

Generic error response
++++++++++++++++++++++

If the request is malformed or errors occur during the request processing, the format defined at `OIDC-FED#Section.7.5`_ SHOULD be used.

