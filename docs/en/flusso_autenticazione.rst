.. include:: ../common/common_definitions.rst

.. _flusso_autenticazione:

Authentication Flow
-------------------

The authentication schemas **"Entra con SPID"** and **"Entra con CIE"** implement the **OpenID Connect Authorization Code Flow** with the extension **PKCE** (Proof Key for Code Exchange, :rfc:`7636`).
This flow returns an **Authorization Code** that can be used to get an **ID Token**, an **Access Token** 
and possibly a **Refresh Token** too.
The **Authorization Code Flow** gets the **Authorization Code** from the *Authorization Endpoint* of the OpenID Provider and all the tokens are returned by the **Token Endpoint**.

.. image:: ../../images/flusso.svg
    :width: 100%


Following, the descriptions of the flow steps, with the numbers indicated in the picture.

  #. The User, in the access page of the Relying Party (RP):

     * Clicks on the button "Enter with SPID" or "Enter with CIE";
     
     * In the SPID case, choses the authentication OP.

  #. The RP prepares an Authorization Request with the parameters needed by *PKCE* and sends it to the *Authorization Endpoint* of the OP.

  #. The OP authenticates the user by the credentials input and obtains, from the RP, the permission to access the user's attributes.

  #. The OP redirects the user to the URL contained in the parameter *redirect_uri* specified by the RP, passing an *Authorization Code* in the Authorization Response.

  #. The RP sends the *Authorization Code* received at the OP *Token Endpoint*.

  #. The OP *Token Endpoint* releases an **ID Token**, an **Access Token** and, if expected, a **Refresh Token**.

  #. The RP receives and validates the **Access Token** and the **ID Token**. For asking the attributes that the user has authorized at the point 3, it sends a request to the OP *UserInfo Endpoint* ans uses, for the authentication, the **Access Token** contained in the HTTP Authorization header.

  #. The OP *UserInfo Endpoint* checks the **Access Token** validity and releases the required attributes to the RP.


.. note::
  **PKCE** is an extension of the protocol *OAuth 2.0* also provided in the profile *iGov* (`International Government Assurance Profile for OAuth 2.0 <https://openid.net/specs/openid-igov-oauth2-1_0-03.html#rfc.section.3.1.7>`_) and aimed at avoiding possible attacks from intercepting the *authorization code*. It consists of the generation of a code (**code verifier**) and its hash (**code challenge**). The **code challenge** is sent to the OP in the authentication request.
  
  When the RP contacts the *Token Endpoint* at the end of the authentication flow, it sends the **code verifier** created initially, so that the OP can check if its hash is the same as in the authentication request.

  Following, an example of a Python script for generating the requested parameters.

  .. literalinclude :: ../../static/pkce.py
   :language: python




