.. include:: ../common/common_definitions.rst

.. _metadata_oidc:

Metadata
--------

OIDC-FED utilizza ed estende i claim dei Metadata così come definiti all'interno delle specifiche di OpenID Connect Discovery 1.0 (`OpenID.Discovery`_) e OpenID Connect Dynamic Client Registration 1.0 (`OpenID.Registration`_) rispettivamente per OP e RP. 

In OIDC-FED il Metadata OIDC relativo a RP e OP viene definito all'interno del claim **metadata** e del suo sotto claim **<entity_type>**, all'interno dell'Entity Configuration, come oggetto JSON.


.. toctree:: 
   :maxdepth: 1

   metadata_oidc_op.rst
   metadata_oidc_rp.rst
   metadata_oidc_ta_sa.rst
   metadata_aa.rst


