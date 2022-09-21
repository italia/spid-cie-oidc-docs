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

.. admonition:: |spid-icon|

  The attributes requested by the parameter **scope** are available in the response to the *userinfo endpoint*.

.. admonition:: |cieid-icon|

  The attributes requested by the parameter **scope** are available both in the ID Token and in the response to the *userinfo endpoint*.

.. note::
   The parameter **scope** MAY contain one or more values, with single spaces as separators. For example, using both *profile* and *email* in the **scope** parameter gives the Minimum Dataset eIDAS and the email.

In case of requests of single user-attributes or specific combinations of them, the RP MAY use the parameter **claims**. 
For the definition of the parameter **claims** and its usage modes for requesting the user attributes, please refer to `OpenID.Core#ClaimsParameter`_. 

.. warning::
  If the parameter **claims** is not present or has no value and the only scope openid has been requested, only the claim *sub* is returned in the response to the *userinfo endpoint*. 

.. admonition:: |spid-icon|

  The user attributes requested by **claims** parameter will be available in the *userinfo endpoint*. 

.. admonition:: |cieid-icon|

  The user attributes requested by **scope** or **claims** parameters will be available in both *userinfo endpoint* and *ID Token*.  
