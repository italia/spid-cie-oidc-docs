.. include:: ./common_definitions.rst

Authorization Request (Authentication Endpoint)
-----------------------------------------------

For starting the authentication process, the RP redirects the user to the *Authorization Endpoint* of the selected OP, and sends an *HTTP* request with the parameter **request**, an object in **JWT** format that contains the *Authorization Request* signed by the RP.

For conveying the request, the RP CAN use the methods **POST** and **GET**. With the method **POST** the parameters MUST be sent using the *Form Serialization*. 
With the method **GET** the parameters MUST be sent using the *Query String Serialization*. For more details see `OpenID.Core#Serializations`_.

.. warning::
  The parameter **scope** MUST be sent both as a parameter in the HTTP call, and inside the request object. The two values MUST be the same.

  The parameters **client_id** and **response_type** SHOULD be sent both as parameters in the HTTP call, and inside the request object. In this case, the parameters of the request object prevail over those in the HTTP call.

.. seealso:: 

   - :ref:`Example of Authorization Request <Esempio_EN6>`

Following, the mandatory parameters in the *HTTP* authentication request.

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

Following, a table that reports the composition of the **JWT** header.

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Jose Header**
    - **Description**
    - **Supported by**
  * - **alg**
    - See :rfc:`7516#section-4.1.1`. It MUST have one of the values that are present in the parameter
      **request_object_encryption_alg_values_supported** in the :ref:`Metadata OP <MetadataOP>`.
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
       It MUST be a string with the requested "acr" values, each of them separated by a single space, appearing in order of preference. The OP CAN use an authentication at a higher level than requested. Such a choice MUST NOT cause a negative result of the request.
     - |spid-icon| |cieid-icon|
   * - **claims**
     - See `OpenID.Core#AuthRequest`_. See Section :ref:`Use of the scope and claims parameters <parametri_scope_claims>`
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




..
  FIXME: Made an ad hoc section for the ways of using the parameters claims e scope
	 
  Claims
  ++++++

  The parameter claims defines the attributes required by the **RP**. The SPID attributes are requested in the element "userinfo" by listing the attributes to be requested as keys of JSON Objects, whose values must be indicated as {"essential": true}. For SPID, it is not possible to request attributes in the id_token, while it is possible for CIE. The listed attributes under "userinfo" are available at the moment of the call to the UserInfo Endpoint.

  .. code-block:: 

  {
      "userinfo":{
          "https://attributes.spid.gov.it/familyName":{
              "essential":true
          }
      }
  }


  .. seealso::

  - https://openid.net/specs/openid-connect-core-1_0.html#IndividualClaimsRequests


