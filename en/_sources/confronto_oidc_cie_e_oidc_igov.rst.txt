.. include:: ../common/common_definitions.rst

Differences with OIDC iGov
--------------------------

CIE OpenID Connect and e SPID OpenID Connect are based on `iGov.OIDC`_  with the following differences:

 - Section 2.1 of iGov shows **vtr**, **acr_values** and **PKCE** as OPTIONAL, in both SPID and CIE id PKCE and acr_values are REQUIRED. In the both SPID and CIE implementation the acr_values has been adopted instead of vtr. 

 - The Authentication response in the Auth code flow of CIE mandates the usage of the **iss** claim parameter to avoid the mix-up attack `I-D.ietf-OAuth-Security-BCP`_. The usage of this parameter is OPTIONAL in SPID.  

 - Section 2.4 of iGov states "RPs MAY optionally send requests to the Authorization endpoint using request parameter." In both SPID and CIE id the usage of request parameter is REQUIRED.

 - Section 3.1 of iGov states " in the case of using vtr in the authentication request the ID Token MUST contain the following REQUIRED claims, namely: **vot** and **vtm** ". As vtr is not used in both SPID and CIE id, thus the aforementioned claims are not included within the ID Token. 

 - Section 3.1 of iGov states "the auth-time claim in ID Token is RECOMMENDED". The SPID and CIE id do not adopt this claim in the ID Token.

 - ID Token in both SPID and CIE id MUST have the acr claim as REQUIRED, while this is optional in the OpenID iGov specs .

 - ID Token in both SPID and CIE id has the requirement of the **at_hash** claim as mandatory, this is OPTIONAL in OIDC-CORE and not present in iGov.

 - In both SPID and CIE id the subject identifier MUST be pairwised.

 - The UserInfo response in both SPID and CIE id MUST be a Nested JWT, signed with the private key of the issuer and encrypted with the public key of the RP.

 - The signed JWT of the UserInfo response MUST have the claims **iss**, **sub**, **aud**, **iat** and **exp**.

 - Section 3.4 of iGov states "OpenID Providers MAY accept request object by reference using the request_uri parameter". This parameter is interchangeable with the request parameter. SPID and CIE id only adopts the usage of request parameter.

 - Section 3.8. Dynamic Registration of iGOV specifies that dynamic client registration is mandatory. In both CIE id and SPID the OIDC Federation automatic client registration is REQUIRED and the OIDC Dynamic client registration SHOULD NOT be supported.

 - Section 4.2 of iGOV  the scopes **openid**, **offline_access**, **profile** and **email** are used in both SPID and CIE id OpenID Connect proposal and they do not consider the other recommended scopes in the iGov profile, namely: **doc**.

 - Section 4.3 of iGov defines the policy regarding the userinfo object of claim request parameter. In both SPID and CIE id, we define the policy both for the userinfo and ID Token object.

 - Sections 3.7 and 2.5 of iGOV : both SPID and CIE id OP metadata are distributed according to the modalities defined  in Section "3. Metadata".

 - The Access token is a signed jwt in compliance to :rfc:`9068`

