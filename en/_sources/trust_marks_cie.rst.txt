.. include:: ../common/common_definitions.rst

Trust Marks for CIEid
----------------------

Examples of Trust Marks for CIE
+++++++++++++++++++++++++++++++

Following, a non-normative example of a Trust Mark, issued by *MinInterno* for SAs of type **full**, belonging to the Public Administration.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.interno.gov.it/federation_entity/intermediary/",
             "iss":"https://registry.interno.gov.it",
             "trust_mark":"$JWT"
         }
     ]
 }


Where the JWT payload is the following:

.. code-block::

 {
     "id":"https://registry.interno.gov.it/federation_entity/intermediary/",
     "iss":"https://registry.interno.gov.it/",
     "sub":"https://sa.esempio.it/",
     "iat":1579621160,
     "organization_type":"public",
     "id_code":"123456",
     "email":"email_or_pec@intermediate.it",
     "organization_name#it":"Denominazione del SA",
     "sa_type":"full",
     "ref":"https://documentazione_di_riferimento.it/"
 }


Following, a non-normative example of a TM, issued by an SA of type RP Leaf, belonging to the Public Administration.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.interno.gov.it/openid_relying_party/public/",
             "iss":"https://sa.esempio.it",
             "trust_mark":"$JWT"
         }
     ]
 }


Where the payload $JWT could be as in the following non-normative example:


.. code-block::

 {
     "id":"https://registry.interno.gov.it/openid_relying_party/public/",
     "iss":"https://sa.esempio.it/",
     "sub":"https://rp.esempio.it/",
     "iat":1579621160,
     "organization_type":"public",
     "id_code":"123456",
     "email":"email_or_pec@rp.it",
     "organization_name#it":"Denominazione del RP",
     "ref":"https://documentazione_di_riferimento.it/"
 }


Profile **sgd**
+++++++++++++++

For technical details and non-normative examples, see [LINK TO BE INSERTED HERE]
