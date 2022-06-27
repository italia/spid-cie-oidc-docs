.. include:: ./common_definitions.rst

Metadati OIDC
-------------

OIDC-FED utilizza i claim dei metadati così come definiti all’interno delle specifiche di OpenID Connect Discovery 1.0 e OpenID Connect Dynamic Client Registration 1.0 `OpenID.Discovery`_, `OpenID.Registration`_ rispettivamente per OP e RP. 

In OIDC-FED il metadato OIDC relativo a RP e OP viene definito all’interno del claim **metadata** e del suo sotto claim **<entity_type>**, all’interno dell’Entity Configuration, come oggetto JSON.


.. toctree:: 
   :maxdepth: 2

   metadata_oidc_op.rst
   metadata_oidc_rp.rst
   metadata_oidc_fa.rst
   metadata_oidc_altri.rst
