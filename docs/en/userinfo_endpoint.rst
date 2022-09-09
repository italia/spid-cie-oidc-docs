.. include:: ../common/common_definitions.rst

UserInfo Endpoint (attributes)
------------------------------

The UserInfo Endpoint is an OIDC protected resource that returns the authenticated user's claims. To obtain 
the requested claims, the RP sends a request to the UserInfo Endpoint using the Access Token.

Request
+++++++

.. admonition:: |spid-icon|

  The UserInfo Endpoint MUST only support the method HTTP GET :rfc:`2616` and MUST accept and validate the Access Token sent in the Authorization field of the Header, whose type is Bearer :rfc:`6750`.

.. admonition:: |cieid-icon|
  
  The UserInfo Endpoint MUST support the method HTTP GET and HTTP POST :rfc:`2616` and MUST accept and validate the Access Token sent in the Authorization field of the Header, whose type is Bearer :rfc:`6750`.

.. TODO: Move examples in the specific section
  .. code-block:: 

    GET https://op.spid.agid.gov.it/userinfo
    Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImRCNjdnTDdja ...
  
.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#UserInfo
 - https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#rfc.section.4


.. _userinfo_response:

Response
++++++++

The content of the Response body MUST be a `signed and encrypted JWT. <https://openid.net/specs/openid-connect-core-1_0.html#UserInfoResponse>`_

The JOSE header MUST contain the *cty* parameter (Content Type) with the value *JWT* (see :rfc:`7515#section-4`).



The UserInfo Endpoint returns user attributes explicitly requested through the **claims** parameter or through the use of the **scope** parameter in the Authentication Request.

.. TODO: Move examples in the specific section
  **Example:**

  .. code-block:: 

  {
      "iss":"https://op.fornitore_identita.it",
      "aud":"https://rp.fornitore_servizio.it",
      "iat":1519032969,
      "nbf":1519032969,
      "exp":1519033149,
      "sub":"OP-1234567890",
      "name":"Mario",
      "https://attributes.spid.gov.it/familyName":"Rossi",
      "https://attributes.spid.gov.it/fiscalNumber":"MROXXXXXXXXXXXXX"
  }


The JWT payload is a JSON containing the following parameters:

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **sub**
     - String. Subject identifier, equal to the identifier already released in the ID Token.
       The RP MUST check that the value is equal to the one, contained in the ID Token.
     - |spid-icon| |cieid-icon|
   * - **aud**
     - String. Subject Identifier of the response recipient (RP).
       The RP MUST check that the value is equal to its own client_id.
     - |spid-icon| |cieid-icon|
   * - **iss**
     - String. URI that uniquely identifies the OP.
     - |spid-icon| |cieid-icon|
   * - **<user claims>**
     - The requested user claims.
     - |spid-icon| |cieid-icon|


In case of authentication errors, the UserInfo Endpoint returns an HTTP error, according to :ref:`Error Management <gestione_errori>`


