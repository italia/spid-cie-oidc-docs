.. include:: ../common/common_definitions.rst
  
.. _supported_algs:

Algoritmi crittografici
+++++++++++++++++++++++

Tutti i partecipanti devono pubblicare gli algoritmi supportati 
di criptazione e firma all'interno dei propri metadata. Tali agoritmi sono utilizzati per tutte le operazioni di cifratura e firma previsti da OIDC core e di Federation.

.. note:: 

  La lunghezza delle chiavi RSA deve essere pari o superiore a 2048 bit.
  Si raccomanda una lunghezza di 4096 bit.

In SPID e CIE id i seguenti algoritmi DEVONO essere supportati:
    
.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algoritmi**
    - **Operazioni**
    - **Riferimento**
    - **Supportato da**
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

In SPID e CIE id è RACCOMANDATO il supporto per i seguenti algoritmi:
    
.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algoritmi**
    - **Operazioni**
    - **Riferimento**
    - **Applicabile a**
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


In SPID e CIE id i seguenti algoritmi NON DEVONO essere supportati:
    
.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algoritmi**
    - **Operazioni**
    - **Riferimenti**
    - **Applicabile a**
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
