.. include:: ../common/common_definitions.rst

.. _flusso_autenticazione:

Authentication Flow
-------------------

The authentication schemas **"Entra con SPID"** and **"Entra con CIE"** implement the **OpenID Connect Authorization Code Flow** with the **PKCE** (Proof Key for Code Exchange, :rfc:`7636`).
This flow returns an **Authorization Code** that can be used to get an **ID Token**, an **Access Token** 
and possibly a **Refresh Token** too.
The **Authorization Code Flow** gets the **Authorization Code** from the *Authorization Endpoint* of the OpenID Provider and all the tokens are returned by the **Token Endpoint**.

.. image:: ../../images/flusso.svg
    :width: 100%


In the following, the descriptions of the flow steps, with the numbers indicated in the picture.

  #. The User, in the access page of the Relying Party (RP):

     * Clicks on the button "Enter with SPID" or "Enter with CIE";
     
     * In the SPID case, choses the authentication OP.

  #. The RP prepares an Authorization Request and sends it to the *Authorization Endpoint* of the OP.

  #. The OP authenticates the user and received the user's consent to release his attributes to the RP.

  #. The OP redirects the user to the URL contained in the parameter *redirect_uri* specified by the RP, passing an *Authorization Code* in the Authorization Response.

  #. The RP sends the *Authorization Code* received at the OP *Token Endpoint*.

  #. The OP *Token Endpoint* releases an **ID Token**, an **Access Token** and, if expected, a **Refresh Token**.

  #. The RP receives and validates the **Access Token** and the **ID Token**. Then requests the user's attributes to the OP *UserInfo Endpoint* and uses, for the authentication, the **Access Token** contained in the HTTP Authorization header.

  #. The OP *UserInfo Endpoint* checks the **Access Token** validity and releases the required attributes to the RP.
