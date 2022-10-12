.. include:: ../common/common_definitions.rst

.. _federation_endpoint:

Federation Endpoint
-------------------

All the Entities MUST contain the following endpoints:

 - **/.well-known/openid-federation**: gives the `Entity Configuration <Entity_Configuration>`__ (for 
   more details, see `OIDC-FED#Section.6`_)
 - **resolve Entity statement endpoint**: gives the final Metadata, the Trust Chain and the Trust Marks
   regarding another subject. For more details, see `OIDC-FED#Section.7.2`_).

.. warning:: 
  The resolve Entity statement endpoint MUST use the very same resolve strategy it uses internally for its own operations (e.g. the RP will expose OP's metadata as it sees them).
  This implies that accordin to the Italian federation's specs:

   - the resolve endpoint MUST NOT return TMs which are not valid at the time of the request;
   - the resolve endpoint MUST validate the chain for the subject.


In addition to the Federation endpoints reported before, the Entities of type **TA** or **SA** MUST provide the following endpoints:


 - **fetch Entity statement endpoint**: returns the ESs regarding a direct subordinate subject. 
   For obtaining the ES of an Entity, at least its Entity identifier is needed. (For more details, see `OIDC-FED#Section.7.1`_).
 - **trust mark status endpoint**: allows an Entity to test if a TM is still active or not. The query MUST
   be sent to the subject that has released that TM. (For more details, see `OIDC-FED#Section.7.4`_).
 - **Entity listing endpoint**: returns the list of the subordinate Entities registered by the TA or an SA.
   (For more details, see `OIDC-FED#Section.7.3`_).

An Entity of type **AA**, in addition to the common Federation endpoints like all the Entities, MUST also include the **trust mark status endpoint** for allowing the dynamic validation of the TMs, released by the AA.


.. warning::
  With respect to what defined in the OIDC-FED, to the **Entity listing endpoint** is added the optional
  claim **entity_type**, that is a filter of the Entity type of the subordinates.

.. _generic_error_response:

Generic error response
++++++++++++++++++++++

If the request is malformed or errors occur during the request processing, the format defined at `OIDC-FED#Section.7.5`_ SHOULD be used.
