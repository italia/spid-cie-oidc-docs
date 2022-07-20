.. include:: ./common_definitions.rst

Authentication response
-----------------------

An Authentication response is an OAuth 2.0 authorization response message, returned by the authorization endpoint of the OpenID Provider (OP) at the end of the authentication flow. The OP redirects the user
to the URL contained in the parameter redirect_uri specified in the authorization request, adding the response parameters.

.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-4.1.2
 - https://openid.net/specs/openid-connect-core-1_0.html#AuthRequestValidation


Response
++++++++

If the authentication is successful, the OpenID Provider (OP), redirects the user with the following parameters:


.. code-block:: 

 GET /resp?
 code=usDwMnEzJPpG5oaV8x3j&
 state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd

 Host: https://rp.spid.agid.gov.it
 HTTP/1.1


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **code**
     - Unique *Authorization Code* that the client can pass to the Token Endpoint for obtaining an ID Token and an Access Token. This has the advantage of not exposing any token to the User Agent or to malware that could be controlling it.
     - |spid-icon| |cieid-icon|
   * - **state**
     - State value included in the *Authentication Request*. The client is supposed to check its correspondence. It must have the same value indicated by the client in the Authorization Request.
     - |spid-icon| |cieid-icon|
   * - **iss**
     - Unique Identifier of the OP that has created the Authentication Response. The RP MUST validate
       this parameter and MUST NOT allow more OPs to use the same identifier. MANDATORY only for CIE.
     - |cieid-icon|

Errors
++++++

In case of errors, the OP displays error messages about the OpenID Connect interchanges, 
as described in the tables defined in the `SPID UX Guidelines`_. 
In case the guidelines require a user's redirect to the RP, the OP performs a redirect to the URL indicated 
in the parameter redirect_uri of the request (only if it is valid, i.e. it is present in the client Metadata), with the following parameters.


**Example:**

.. code-block:: 

 GET /resp?
 error=invalid_request&
 error_description=request%20malformata&
 state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd

 Host: https://rp.spid.agid.gov.it
 HTTP/1.1


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **error**
     - Error code
     - |spid-icon| |cieid-icon|
   * - **error_description**
     - More detailed error description, aimed at helping the developers to debug. This message is not supposed
       to be displayed to the user (for this purpose, please see the `SPID UX Guidelines`_
     - |spid-icon| |cieid-icon|
   * - **state**
     - *state* value included in the Authentication Request. It is up to the client to test its
       correspondence to the one that has been sent in the Authentication Request.
     - |spid-icon| |cieid-icon|


.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-4.1.2.1


