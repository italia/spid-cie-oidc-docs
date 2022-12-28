.. include:: ../common/common_definitions.rst

.. _federation_endpoint:

Federation Endpoints
--------------------

All the Entities MUST contain the following endpoints:

 - **/.well-known/openid-federation**: gives the `Entity Configuration <Entity_Configuration>`__ (for 
   more details, see `OIDC-FED`_ Section 6)
 - **resolve Entity statement endpoint**: gives the final Metadata, the Trust Chain and the Trust Marks
   regarding another subject. For more details, see `OIDC-FED`_ Section 7.2).

.. warning:: 

   - the resolve endpoint MUST NOT return TMs which are not valid at the time of the request;
   - the resolve endpoint MUST return the serialized Trust Chain for the subject.


In addition to the Federation endpoints reported before, the Entities of type **TA** or **SA** MUST provide the following endpoints:


 - **fetch Entity statement endpoint**: returns the ESs regarding a direct subordinate subject. 
   For obtaining the ES of an Entity, at least its Entity identifier is needed. (For more details, see `OIDC-FED`_ Section 7.1).
 - **trust mark status endpoint**: allows an Entity to test if a TM is still active or not. The request MUST
   be sent to the subject that has released that TM. (For more details, see `OIDC-FED`_ Section 7.4).
 - **Entity listing endpoint**: returns the list of the subordinate Entities registered by the TA or an SA.
   (For more details, see `OIDC-FED`_ Section 7.3).

An Entity of type **AA**, in addition to the common Federation endpoints like all the Entities, MUST also include the **trust mark status endpoint** for allowing the dynamic validation of the TMs, released by the AA.
