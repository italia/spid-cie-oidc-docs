.. include:: ../common/common_definitions.rst


Trust Marks for SPID
++++++++++++++++++++


Examples of Trust Marks for SPID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The TMs issued for the Leaves MUST be published by the Leaves themselves in their own **Entity Configuration**,
inside the claim **trust_marks**. This is composed by lists of JSON objects, each of them MUST contain at least
the claims **id** and **trust_mark**, where the first identifies the TM, and the second contains the signed JWT of the TM.

Following, a non-normative example of the object **trust_marks** inside the Entity Configuration of an RP-type Leaf.


.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://www.spid.gov.it/openid-federation/agreement/sp-public/",
             "trust_mark":"$JWT"
         }
     ]
 }



Following, a non-normative example of a Trust Mark issued by AgID for a private Intermediary.


.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.agid.gov.it/federation_entity/private/",
             "trust_mark":"$JWT"
         }
     ]
 }

Where the content of the signed JWT inside the claim **trust_mark**, corresponds to:

.. code-block::

 {
     "id":"https://registry.agid.gov.it/federation_entity/private/",
     "iss":"https://registry.agid.gov.it",
     "sub":"https://intermediary.example.it",
     "iat":1579621160,
     "organization_type":"private",
     "id_code":"12345678900",
     "email":"email_or_pec@example.it",
     "organization_name":"Full name of the SA",
     "ref":"https://reference_to_some_documentation.example.it/"
 }



An Intermediate Entity or Intermediary (SA) is recognizable as Trust Mark issuer. What follows, is a 
non-normative example of a Trust Mark, issued by an SA in favor of its subordinate RP.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.agid.gov.it/openid_relying_party/public/",
             "trust_mark":"$JWT"
         }
     ]
 }


Where the content of the signed JWT inside the claim **trust_mark**, corresponds to the following non-normative example:


.. code-block::

 {
     "id":"https://registry.agid.gov.it/openid_relying_party/public/",
     "iss":"https://intermediary.example.it",
     "sub":"https://rp.example.it",
     "iat":1579621160,
     "organization_type":"public",
     "id_code":"123456",
     "email":"email_or_pec@rp.it",
     "organization_name":"Full name of the RP",
     "ref":"https://reference_to_some_documentation.it/"
 }


