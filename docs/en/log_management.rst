.. include:: ../common/common_definitions.rst

.. _Log_Management:

Retention Policy
================

Log management of a OP and an RP
------------------------------------

OPs and RPs MUST retain the following. 

1. A transaction log containing the exchanged messages. The messages stored in the log MUST be at least the following:

    - **AuthenticationRequest**
    - **AuthenticationResponse** related to the *AuthenticationRequest**.
    - **TokenRequest** related to the *AuthenticationRequest*.
    - **TokenResponse** related to the *TokenRequest*. 
    - The **UserInfoRequest** related to the *TokenRequest*, if any.
    - The **UserInfoResponse** related to the *UserInfoRequest*, if any.
    - **RevocationRequest** related to the *TokenRequest*, if any.
    - The **RevocationResponse** related to the *RevocationRequest*, if any.
    
.. admonition:: |spid-icon|
    
    For each message, where applicable, the following information could be indexed for research and consultation purposes:
    
        - authorization code
        - client_id
        - jti
        - iss
        - sub
        - iat
        - exp

2. A federation log containing, for each *AuthenticationRequest*, the **Trust Chain** related to the entity which messages are being exchanged with. In the case of a log handled by an OP receiving an authentication request from an RP, it MUST contain the following ordered list of items:

    - The **Entity Configuration** of the requesting RP.
    - The **Entity Statement** of the SA referring to the RP, if any.
    - The **Entity Statement** of the TA referring to the RP (or to the SA, if any).
    - The **Entity Configuration** of the TA.

In the case of a registry handled by an RP making an authentication request to a OP, the registry MUST contain the following ordered list of items:

    - The **Entity Configuration** of the OP.
    - The **Entity Statement** of the TA referring to the OP.
    - The **Entity Configuration** of the TA.

.. warning::
    The information stored in the logs MUST be retained and managed for not less than 24 months in full compliance with national and european privacy regulations. Access to the data MUST be restricted to designated personnel. In order to ensure confidentiality data encryption mechanisms or employed database systems (DBMS) that realize encrypted persistence of information MUST be adopted. Integrity e non-repudiation properties MUST be ensured.


Federation Historical Key registry
----------------------------------

In order to enable the verification of messages exchanged by Entities participating in the federation and their Trust Chains, the TA MUST publish the federation public key history (JWKS) within a registry made available to all participants via the */.well-known/openid-federation-jwks* endpoint. For further technical details, please refer to Section 7.5 of `OIDC-FED`_. 

.. warning::
    Keys that have not been active for more than 24 months MAY be removed from the registry at the TA's convenience. 

