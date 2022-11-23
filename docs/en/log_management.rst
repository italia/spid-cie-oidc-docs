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

2. A federation log containing, for each *AuthenticationRequest*, the **Trust Chain** related to the entity which messages are being exchanged with. In the case of a log handled by an OP receiving an authentication request from an RP, it MUST contain:

    - The **Entity Configuration** of the requesting RP.
    - The **Entity Configuration** of the SA (in the case of an aggregated RP), if any.
    - The **Entity Statement** of the SA referring to the RP, if any.
    - The **Entity Configuration** of the TA.
    - The **Entity Statement** of the TA referring to the RP.

In the case of a registry handled by an RP making an authentication request to a OP, it MUST contain:

    - The **Entity Configuration** of the OP.
    - The **Entity Configuration** of the TA.
    - The **Entity Statement** of the TA referring to the OP.

.. warning::
    The information stored in the logs MUST be retained and managed for not less than 24 months in full compliance with current privacy regulations. Access to the data MUST be restricted to designated personnel. In order to ensure confidentiality data encryption mechanisms or employed database systems (DBMS) that realize encrypted persistence of information MAY be adopted. Mechanisms that ensure integrity and non-repudiation MUST be put in place.


Federation Key registry
-----------------------

In order to enable the verification of messages exchanged by entities participating in the federation and their Trust Chains, the TA MUST publish the federation public key history (JWKS) within a registry made available to all participants via the */.well-known/openid-federation-jwks* endpoint. For further technical details, please refer to Section 7.5 of `OIDC-FED`_. 

.. warning::
    Keys that have not been active for more than 24 months MAY be removed from the registry at the TA's convenience. 

