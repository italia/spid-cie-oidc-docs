.. include:: ../common/common_definitions.rst

.. _DifferenzeSPID_CIE:

Differences between SPID e CIE id
---------------------------------

This section provides the main differences between SPID and CIE id.

Metadata
++++++++

CIE id allows th ID Token encryption, the OP and RP metadata include the parameters that enable this feature (see section `Metadata OP <MetadataOP>`_ and `Metadata RP <MetadataRP>`_).

SPID does not allow the ID Token encryption. 

Moreover, CIE id requires the parameter *revocation_endpoint_auth_methods_supported* to be included in the OP metadata, while SPID does not. 

Authorization Endpoint
++++++++++++++++++++++

SPID requires the parameters *client_id* and *response_type* in the HTTP request as mandatory, while in CIE id they are recommended. 

Moreover, in CIE id the response requires the presence of the *iss* parameter as mitigation against the mix-up attacks `I-D.ietf-OAuth-Security-BCP`_. SPID does not require it. 


Parameters Scope and Claims
+++++++++++++++++++++++++++

CIE id allows an RP to request user attributes using both the *claims* parameter and the *scope* parameter, enabling in the scope parameter the values *profile* and *email*. 

SPID does not allow *profile* and *email* values in the *scope* parameter.

For further details see section :ref:`Parameters Scope and claims <parametri_scope_claims>`.


ID Token
++++++++

In SPID the user attributes are not available in the ID Token. 

In CIE id the user attributes are available in both ID Token and UserInfo response. 
Moreover, CIE id allows the ID Token encryption.


Refresh Token
+++++++++++++

SPID allows the Refresh Token to enable the revocable long sessions as defined in `LL.GG. OpenID Connect in SPID <https://www.agid.gov.it/sites/default/files/repository_files/linee_guida_openid_connect_in_spid.pdf>`_ e nell' `Avviso n.41 <https://www.agid.gov.it/sites/default/files/repository_files/spid-avviso-n41-integrazione_ll.gg_._openid_connect_in_spid.pdf>`_ . Whith a Refresh Token an RP can obtain an ID Token which only contains the value *https://www.spid.gov.it/SpidL1* in the *acr* parameter. 

In CIE id the Refresh Token does not allow to obtain an ID Token. Thus, an RP can not obtain a new user authentication with the OP or renewing a pre-existing one. The Refresh Token in CIE id may be used to obtain from the UserInfo endpoint the same set of user attributes requested at the initial authentication phase, for which the user has given explicit consent.

For further details see section :ref:`Refresh Token <Refresh_Token>`.


UserInfo Endpoint
+++++++++++++++++

CIE id supports both GET and POST HTTP methods. 

SPID only allows the HTTP GET method.

Introspection Endpoint
++++++++++++++++++++++

In CIE id, only the parameter *active* is given in the introspection response. 

SPID includes additional parameters as defined in section :ref:`Introspection Endpoint <introspection_endpoint>`.


Revocation Endpoint and Logout
++++++++++++++++++++++++++++++

SPID and CIE id require the RP to request an Access Token revocation during the user logout. 
In SPID the Access Token revocation implies the Refresh Token revocation, if any or still active, and the end of the Single Sign-On session if still active.

In CIE id the Access Token revocation does not imply the Refresh Token revocation, if any.
In CIE id the Refresh Token revocation requires all related active token to be revoked.  



