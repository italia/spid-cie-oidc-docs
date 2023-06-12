.. include:: ../common/common_definitions.rst

Authorization endpoint
----------------------

Request
+++++++

The Authorization request is initiated by the user that selects the OP for the authentication. 
The RP redirects the user to the *Authorization Endpoint* of the selected OP, including in the request the parameter **request** that is a signed JWT containing the *Authorization Request*.

For conveying the request, the RP MAY use the methods **POST** and **GET**. With the method **POST** the parameters MUST be sent using the *Form Serialization*. 
With the method **GET** the parameters MUST be sent using the *Query String Serialization*. For more details see `OpenID.Core#Serializations`_.

.. warning::
  The parameter **scope** MUST be sent both as a parameter in the HTTP request, and inside the request object. The two values MUST be the same.

  |cieid-icon|
  The parameters **client_id** and **response_type** SHOULD be sent both as parameters in the HTTP request, and inside the request object.

  |spid-icon|
  The parameters **client_id** and **response_type** MUST be sent both as parameters in the HTTP request, and inside the request object
  and MUST be the same, in case of mismatching the values inside the request object MUST be considered.

.. seealso:: 

   - :ref:`Example of Authorization Request <Esempio_EN6>`


In the following the mandatory parameters in the *HTTP* authentication request.

.. _tabella_parametri_http_req:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Supported by**
  * - **scope**
    - It contains values of *scope* that are supported by the OP and defined by the parameter
      **scopes_supported** in the :ref:`Metadata OP <MetadataOP>`. 
      At least the value *openid* MUST be present.
    - |spid-icon| |cieid-icon|
  * - **code_challenge**
    - See :rfc:`7636#section-4.2`.
    - |spid-icon| |cieid-icon|
  * - **code_challenge_method**
    - As defined by the parameter **code_challenge_methods_supported** in the :ref:`Metadata OP <MetadataOP>`.
    - |spid-icon| |cieid-icon|
  * - **request**
    - See `OpenID.Core#JWTRequests`_. It MUST be a signed **JWT**.
    - |spid-icon| |cieid-icon|

In the following, a table that reports the composition of the **JWT** header.

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Jose Header**
    - **Description**
    - **Supported by**
  * - **alg**
    - See :rfc:`7516#section-4.1.1`. See :ref:`supported_algs`.
    - |spid-icon| |cieid-icon|
  * - **kid**
    - See :rfc:`7638#section_3`. 
    - |spid-icon| |cieid-icon|

.. note::
  The parameter **typ**, if omitted, assumes the implicit value **JWT**.


The **JWT** payload contains the following mandatory claims:


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **client_id**
     - See `OpenID.Registration`_. It MUST contain an HTTPS URL that uniquely identifies the RP.
     - |spid-icon| |cieid-icon|
   * - **code_challenge**
     - As defined in the :ref:`Table of the HTTP parameters <tabella_parametri_http_req>`.
     - |spid-icon| |cieid-icon|
   * - **code_challenge_method**
     - As defined in the :ref:`Table of the HTTP parameters <tabella_parametri_http_req>`.
     - |spid-icon| |cieid-icon|
   * - **nonce**
     - See `OpenID.Core#AuthRequest`_. It MUST be a casual string with at least 32 alphanumeric characters.
       This value will be returned in the ID Token provided by the Token Endpoint, so that the client can test that it is equals as in the authentication request.
     - |spid-icon| |cieid-icon|
   * - **prompt**
     - See `OpenID.Core#AuthRequest`_. The allowed values are:
       
       **consent**: If a Single Sign On session is not yet active,
       the OP makes an Authentication Request to the user.
       Then it asks permission to transfer the claims.

       **consent login**: The OP forces an authentication request to the user.
       Then it asks permission to transfer the claims.

     - |spid-icon| |cieid-icon|
   * - **redirect_uri**
     - See `OpenID.Core#AuthRequest`_. It MUST be an URL included in the :ref:`Metadata RP <MetadataRP>`. 
     - |spid-icon| |cieid-icon|
   * - **response_type**
     - See `OpenID.Core#AuthRequest`_. As defined by the parameter **response_types_supported** in the
       :ref:`Metadata OP <MetadataOP>`.
     - |spid-icon| |cieid-icon|
   * - **scope**
     - As defined in the :ref:`Table of the HTTP parameters <tabella_parametri_http_req>`.
     - |spid-icon| |cieid-icon|
   * - **acr_values**
     - See `OpenID.Core#AuthRequest`_. As defined by the parameter **acr_values_supported** in the
       :ref:`Metadata OP <MetadataOP>`.
       Reference values of the contest class of the Authentication Request. 
       It MUST be a string with the requested "acr" values, each of them separated by a single space, appearing in order of preference. The OP MAY use an authentication at a higher level than requested. Such a choice MUST NOT cause a negative result of the request.
     - |spid-icon| |cieid-icon|
   * - **claims**
     - See `OpenID.Core#ClaimsRequestParameter`_. See Section "Parameters scope and claims".
     - |spid-icon| |cieid-icon|
   * - **state**
     - See `OpenID.Core#AuthRequest`_. It must be a casual string with at least 32 alphanumeric characters.
       Unique session identifier at the RP side. This value will be returned to the client in the response, at the end of the authentication.
     - |spid-icon| |cieid-icon|
   * - **exp**
     - UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **iat**
     - UNIX Timestamp with the generation time of the JWT, coded as NumericDate as indicated in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **iss**
     - It MUST correspond to *client_id*. 
     - |spid-icon| |cieid-icon|
   * - **aud**
     - It MUST correspond to the OP identifier (parameter *issuer*, present in the :ref:`Metadata OP <MetadataOP>`.)
     - |spid-icon| |cieid-icon|
   * - **ui_locales**
     - OPTIONAL. End-User's preferred languages and scripts for the user interface. Represented as a space-separated list of BCP47 [RFC5646].
     - |spid-icon| |cieid-icon|

.. note::
  **PKCE** is an extension of the protocol *OAuth 2.0* also provided in the profile *iGov* (`International Government Assurance Profile for OAuth 2.0 <https://openid.net/specs/openid-igov-oauth2-1_0-03.html#Section-3.1.7>`_) and aimed at avoiding possible attacks from intercepting the *authorization code*. It consists of the generation of a code (**code verifier**) and its hash (**code challenge**). The **code challenge** is sent to the OP in the authentication request.
  
  When the RP contacts the *Token Endpoint* at the end of the authentication flow, it sends the **code verifier** created initially, so that the OP can check if its hash is the same as in the authentication request.

  An example of a Python script for generating the requested parameters is shown.

  .. literalinclude :: ../../static/pkce.py
   :language: python


.. _parametri_scope_claims:

Parameters **scope** and **claims**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: |spid-icon|

  The attributes of the user MAY be requested by the RP using the **claims** parameter in the Authorization Request.

  SPID doesn't allow the user attributes in ID Token, they are only available at the "userinfo" endpoint.  


.. admonition:: |cieid-icon|

  The user attributes MAY be requested by the RP using the **scope** or **claims** parameters in the Authorization Request.

  When the **scope** parameter is used, the following values are supported:

  - **profile**: requests the user attributes equivalent to the eIDAS Minimum Dataset: 

      - *family_name*, 
      - *given_name*,
      - *birthdate*, 
      - *\https://attributes.eid.gov.it/fiscal_number* (National Unique Identifier).

  - **email**: requests the following attributes:

      - *email*;
      - *email_verified*.


  The parameter **scope** MAY contain one or more values, with single spaces as separators. For example, using both profile and email in the scope parameter returns the Minimum eIDAS Dataset and the email.
  In case of requests of single user-attributes or specific combinations of them, the RP SHOULD use the parameter **claims**.

  The attributes requested by the parameter **scope** are available both in the ID Token and in the *userinfo endpoint* response.

  .. warning::

    If in the **scope** parameter there was only the *openid* value and the **claims** parameter was not present or valued, the response of the userinfo endpoint would not have any user attributes but only the claim **sub**.

For the definition of the parameter **claims** and its usage modes for requesting the user attributes, please refer to `OpenID.Core#ClaimsParameter`_.


Response
++++++++

An Authentication response is returned by the authorization endpoint of the OpenID Provider (OP) at the end of the authentication flow. The OP redirects the user
to the URL contained in the parameter redirect_uri specified in the authorization request, adding the response parameters.

.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-4.1.2
 - https://openid.net/specs/openid-connect-core-1_0.html#AuthRequestValidation

If the authentication is successful the OpenID Provider (OP) redirects the user by adding the following parameters required as query parameters to the *redirect_uri* (as defined in `OpenID.Core#AuthResponse`_): 


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
       this parameter and MUST NOT allow more OPs to use the same identifier.
     - |cieid-icon|

Authorization Response example:

  .. code-block:: http

    http://rp-test.it/oidc/rp/callback/?code=a032faf23d986353019ff8eda96cadce2ea1c368f04bf4c5e1759d559dda1c08056c7c4d4e8058cb002a0c8fa9a920272350aa102548523a8aff4ccdb44cb3fa&state=2Ujz3tbBHWQEL4XPFSJ5ANSjkhd7IlfC&iss=http%3A%2F%2Fop-test%2Foidc%2Fop%2F

Error Management
++++++++++++++++

In the event of an error, the OP or RP represent the anomaly message 
as described in the related tables defined by the `Linee Guida UX SPID`_. 


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **error**
     - See :ref:`Error codes <codici_errore>`
     - |spid-icon| |cieid-icon|
   * - **error_description**
     - Error description.
     - |spid-icon| |cieid-icon|
   * - **state**
     - It MUST be equal to the *status* value included in the *Authentication Request*. The RP MUST verify that it matches the one sent in the *Authentication Request*.
     - |spid-icon| |cieid-icon|


.. _codici_errore:

Error Codes
^^^^^^^^^^^

.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Error Code**
    - **Description**
    - **HTTP Code**
    - **Supported by**

  * - *access_denied*
    - The OP denied access due to invalid or unsuitable credentials for the required SPID level (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *unauthorized_client*
    - The client is not authorized to request an authorization code (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *invalid_request*
    - The request is not valid due to the lack or incorrectness of one or more parameters (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *invalid_scope*
    - Invalid scopes in the Authorization request (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *server_error*
    - The OP encountered an internal problem (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *temporarily_unavailable*
    - The OP encountered a temporary internal problem (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *unsupported_response_type*
    - The OP does not support the requested response_type. (:rfc:`6749#section-4.1.2.1`).
    - *302 Found*
    - |spid-icon| |cieid-icon|
    
  * - *login_required*
    - The OP requires End-User authentication (`OpenID.Core#AuthError`_).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *consent_required*
    - The OP requires End-User consent (`OpenID.Core#AuthError`_).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *request_uri_not_supported*
    - The OP does not support use of the request_uri parameter (`OpenID.Core#AuthError`_).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *registration_not_supported*
    - The OP does not support use of the *registration* parameter (`OpenID.Core#AuthError`_).
    - *302 Found*
    - |spid-icon| |cieid-icon|

  * - *invalid_request_object*
    - The *request* parameter contains an invalid *Request Object* (`OpenID.Core#AuthError`_).
    - *302 Found*
    - |spid-icon| |cieid-icon|


.. warning::

  In case of invalid, mismatching, or missing redirection URI, the OP will return *400 Bad Request* as the HTTP code.
  

