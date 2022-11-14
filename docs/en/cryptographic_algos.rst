.. include:: ../common/common_definitions.rst
  
.. _supported_algs:

Cryptographic algorithms
++++++++++++++++++++++++

All the participants MUST expose the supported 
signature and encryption algorithms in their metadata. They are used for all encryption and signature operations required by OIDC core and Federation.

.. note:: 

  The length of the RSA keys must be equal to or greater than 2048 bits.
  A length of 4096 bits is recommended.

In the SPID and CIE id the following algorithms MUST be supported:
    
.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algorithm**
    - **Operations**
    - **References**
    - **Applicable to**
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
    - **Applicable to**
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
  * - **ECDH-ES**
    - Key Encryption
    - `RFC7518`_.
    - |cieid-icon|
  * - **ECDH-ES+A128KW**
    - Key Encryption
    - `RFC7518`_.
    - |cieid-icon|
  * - **ECDH-ES+A256KW**
    - Key Encryption
    - `RFC7518`_.
    - |cieid-icon|


In the SPID and CIE id the following algorithms MUST NOT be supported:
    
.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algorithm**
    - **Operations**
    - **References**
    - **Applicable to**
  * - **none** 
    - Signature
    - `RFC7518`_.
    - |spid-icon| |cieid-icon|
  * - **RSA_1_5**
    - Key Encryption
    - `RFC7516`_.
    - |spid-icon| |cieid-icon|
  * - **HS256** 
    - Signature
    - `RFC7518`_.
    - |spid-icon| |cieid-icon|
  * - **HS384** 
    - Signature
    - `RFC7518`_.
    - |spid-icon| |cieid-icon|
  * - **HS512** 
    - Signature
    - `RFC7518`_.
    - |spid-icon| |cieid-icon|
