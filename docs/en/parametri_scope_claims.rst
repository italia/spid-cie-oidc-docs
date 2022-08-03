.. include:: ../common/common_definitions.rst

.. _parametri_scope_claims:

Usage of the parameters **scope** and **claims**
------------------------------------------------

The user attributes MAY be requested by the RP using the **scope** or **claims** parameters in the Authorization Request.

In case of using the **scope** parameter, the following values are supported:

- **profile**: using this value it is possible to obtain the default user profile that corresponds to the eIDAS Minimum Dataset: 

    - *family_name*, 
    - *given_name*,
    - *birthdate*, 
    - *\https://attributes.eid.gov.it/fiscal_number* (National Unique Identifier).

- **email**: this values allows obtaining, if made available by the user, the following attributes:

    - *email*;
    - *email_verified*.

The attributes requested by the parameter **scope** are available both in the ID Token and in the response to the Userinfo Endpoint.

.. note::
   The parameter **scope** MAY contain one or more values, with single spaces as separators. For example, using both *profile* and *email* in the **scope** parameter gives the Minimum Dataset eIDAS and the email.

In case of requests of single user-attributes or specific combinations of them, the RP MAY use the parameter **claims**. 
For the definition of the parameter **claims** and its usage modes for requesting the user attributes, please refer to `OpenID.Core#ClaimsParameter`_. 

.. warning::
    - Only for CIE id: In the object *id_token* of the parameter **claims**, it is possible to request only the eIDAS Minimum Dataset. The other user attributes MUST be requested in the object *userinfo* of the parameter **claims**. Moreover, the user attributes requested in the *id_token* object are also available at the *userinfo endpoint*.  

.. warning::
    - If the parameter **claims** is not present or has no value and the only scope openid has been requested, only the claim *sub* is returned
      in the response to the Userinfo Endpoint. 


The following table shows some usage examples.

.. list-table:: 
    :widths: 10 10 20 20
    :header-rows: 1

    * - **Claims**
      - **Scope**
      - **Attributes in the Userinfo Response**
      - **Attributes in the ID Token**
    * - *userinfo*: \- |br| *id_token*: \-
      - *openid*
      - *sub*
      - *sub*
    * - *userinfo*: \- |br| *id_token*: \-
      - *openid* |br| *profile*
      - *sub*, |br| *given_name*, |br| *family_name*, |br| *birthdate*, |br| *\https://attributes.eid.gov.it/fiscal_number*
      - *sub*, |br| *given_name*, |br| *family_name*, |br| *birthdate*, |br| *\https://attributes.eid.gov.it/fiscal_number*
    * - *userinfo*: \- |br| *id_token*:"birthdate":{essential:true}
      - *openid* 
      - *sub*, |br|  *birthdate*
      - *sub*, |br|  *birthdate*
    * - *userinfo*: \- |br| *id_token*: \-
      - *openid* |br| *email*
      - *sub*, |br| *email*, |br| *email_verified*
      - *sub*, |br| *email*, |br| *email_verified*
    * - *userinfo*:"family_name":null |br| *id_token*:"given_name":{essential:true}
      - *openid* 
      - *sub*, |br|  *family_name*, |br| *given_name* 
      - *sub*, |br|  *given_name*
    * - *userinfo*:\- |br| *id_token*:"birthdate":{essential:true} "gender":{essential:true}
      - *openid* 
      - *sub*, |br|  *birthdate*, |br|  *gender*
      - *sub*, |br|  *birthdate*


