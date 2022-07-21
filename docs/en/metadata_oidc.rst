.. include:: ../common/common_definitions.rst

.. _metadata_oidc:

OIDC Metadata
-------------

OIDC-FED uses and extends the Metadata claims as defined in the specifications OpenID Connect Discovery 1.0 and OpenID Connect Dynamic Client Registration 1.0 `OpenID.Discovery`_, `OpenID.Registration`_ respectively for OP and RP. 

In OIDC-FED the OIDC Metadata regarding an RP or OP is defined inside the claim **metadata** and its sub-claim
**<entity-type>**, inside the Entity Configuration, as a JSON Object.


.. toctree:: 
   :maxdepth: 1

   metadata_oidc_op.rst
   metadata_oidc_rp.rst
   metadata_aa.rst
