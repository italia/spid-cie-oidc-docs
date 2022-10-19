.. include:: ../common/common_definitions.rst

.. _metadata_oidc:

Metadata
--------

OIDC-FED uses and extends the Metadata claims as defined in the specifications OpenID Connect Discovery 1.0 and OpenID Connect Dynamic Client Registration 1.0 `OpenID.Discovery`_, `OpenID.Registration`_ respectively for OP and RP. 

In OIDC-FED the OIDC Metadata regarding an RP or OP is defined inside the claim **metadata** and its sub-claim
**<entity-type>**, inside the Entity Configuration, as a JSON Object.


.. toctree:: 
   :maxdepth: 1

   metadata_oidc_op.rst
   metadata_oidc_rp.rst
   metadata_aa.rst


.. _supported_algs:

Supported algorithms
++++++++++++++++++++

All the participants MUST expose the supported 
signature and encryption algorithms in their metadata.


In the SPID and CIE id the following algorithms MUST be supported:
    
.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algorithm**
    - **Operations**
    - **References**
    - **Supported by**
  * - **RS256** 
    - Signature
    - `OpenID.Core`_ and `RFC7518 <https://www.rfc-editor.org/rfc/rfc7518>`_.
    - |spid-icon| |cieid-icon|
  * - **RS512**
    - Signature
    - `RFC7518 <https://www.rfc-editor.org/rfc/rfc7518>`_
    - |spid-icon| |cieid-icon|
  * - **RSA-OAEP**
    - Key Encryption
    - `RFC7518`_.
    - |spid-icon| |cieid-icon|
  * - **RSA-OAEP-256**
    - Key Encryption
    - `RFC7516`_.
    - |spid-icon| |cieid-icon|
  * - **A128CBC-HS256**
    - Content Encryption 
    - `RFC7516`_.
    - |spid-icon| |cieid-icon|
  * - **A256CBC-HS512**
    - Content Encryption 
    - `RFC7516`_.
    - |spid-icon| |cieid-icon|

In the SPID and CIE id the following algorithms are RECOMMENDED to be supported:
    
.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algorithm**
    - **Operations**
    - **References**
    - **Supported by**
  * - **ES256** 
    - Signature
    - `OpenID.Core`_ and `RFC7518`_.
    - |spid-icon| |cieid-icon|
  * - **ES512**
    - Signature
    - `RFC7518`_.
    - |spid-icon| |cieid-icon|
  * - **PS256** 
    - Signature
    - `RFC7518`_.
    - |spid-icon| |cieid-icon|
  * - **PS512**
    - Signature
    - `RFC7518`_.
    - |spid-icon| |cieid-icon|


In the SPID and CIE id the following algorithms MUST NOT be supported:
    
.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algorithm**
    - **Operations**
    - **References**
    - **Supported by**
  * - **none** 
    - Signature
    - `RFC7518`_.
    - |spid-icon| |cieid-icon|
  * - **RSA_1_5**
    - Key Encryption
    - `RFC7516`_.
    - |spid-icon| |cieid-icon|


