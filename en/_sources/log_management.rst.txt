.. include:: ../common/common_definitions.rst

.. _Log_Management:

Retention Policy
================

Log management of a OP and an RP
--------------------------------

OPs and RPs MUST retain the following. 

1. A transaction log containing the exchanged messages. The messages stored in the log MUST be at least the following:
    
    - **Trust Chain** related to the Entity which messages are being exchanged with, composed as follows:
        
        1. The **Entity Configuration** of the Entity which messages are being exchanged with.
        2. [Only for OP] The **Entity Statement** of the SA referring to the RP, if any.
        3. The **Entity Statement** of the TA referring to the descendant Entity.
        4. The **Entity Configuration** of the TA.

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

.. warning::
    The information stored in the logs MUST be retained and managed for not less than 24 months in full compliance with national and european privacy regulations. Access to the data MUST be restricted to designated personnel. In order to ensure confidentiality data encryption mechanisms or employed database systems (DBMS) that realize encrypted persistence of information MUST be adopted. Integrity e non-repudiation properties MUST be ensured.


Federation Historical Key registry
----------------------------------

In order to enable the verification of messages exchanged by Entities participating in the federation and their Trust Chains, the TA MUST publish its federation public key history (JWKS) within a registry made available to all participants via the */.well-known/openid-federation-historical-jwks* endpoint. For further technical details, please refer to Section 7.5 of `OIDC-FED`_. 

.. warning::
    Keys that have not been active more than 24 months MAY be removed from the registry at the TA's convenience. 

