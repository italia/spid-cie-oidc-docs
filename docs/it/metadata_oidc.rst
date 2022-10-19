.. include:: ../common/common_definitions.rst

.. _metadata_oidc:

Metadata
--------

OIDC-FED utilizza ed estende i claim dei Metadata così come definiti all'interno delle specifiche di OpenID Connect Discovery 1.0 e OpenID Connect Dynamic Client Registration 1.0 `OpenID.Discovery`_, `OpenID.Registration`_ rispettivamente per OP e RP. 

In OIDC-FED il Metadata OIDC relativo a RP e OP viene definito all'interno del claim **metadata** e del suo sotto claim **<entity_type>**, all'interno dell'Entity Configuration, come oggetto JSON.


.. toctree:: 
   :maxdepth: 1

   metadata_oidc_op.rst
   metadata_oidc_rp.rst
   metadata_aa.rst


.. _supported_algs:

Algoritmi supportati
++++++++++++++++++++

Tutti i partecipanti devono pubblicare gli algoritmi supportati 
di criptazione e firma all'interno dei propri metadata.

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
