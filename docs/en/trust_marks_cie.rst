.. include:: ./common_definitions.rst


Trust Mark for CIEid
---------------------

The following table summarizes all the available profiles for all the entities involved and supported by the CIEid Federation.


.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **TM Profile**
      - **Description**
      - **Type of sub entity**
    * - **public**
      - the entity in the claim *sub* belongs to the Italian Public Administration.
      - RP, OP
    * - **private**
      - the entity in the claim *sub* belongs to the private sector.
      - RP
    * - **intermediary**
      - the entity in the claim *sub* is an SA.
      - SA
    * - **attribute-authority**
      - the entity in the claim *sub* is an Attribute Authority.
      - AA
    * - **sgd**
      - the entity in the claim *sub* is an RP or an SA that participates in the AA's System of Delegation Management.
      - RP

Profiles **public** and **private**
+++++++++++++++++++++++++++++++++++

Here the claims of the Section :ref:`Composizione dei Trust Mark <ComposizioneTM>` apply.


Profile **intermediary**
++++++++++++++++++++++++

In addition to the claims of the profiles **public** and **private**, the profile **intermediary** adds the following claims:

.. list-table::
    :widths: 20 60
    :header-rows: 1

    * - **Claim**
      - **Description**
    * - **sa_type**
      - it MUST have the values **"full"** or **"light"** according to the way they operate with respect to the Aggregated Subjects.

.. seealso::

    See Section :ref:`Intermediate Entities in the Federative context <Soggetti_aggregatori>`

Profile **attribute-authority**
+++++++++++++++++++++++++++++++

In addition to the claims of the profiles **public** and **private**, the profile **attribute-authority** adds the following claims:


.. list-table::
    :widths: 20 60
    :header-rows: 1

    * - **Claim**
      - **Description**
    * - **policy_uri**
      - URL at which the privacy policy of the AA is available.
    * - **tos_uri**
      - URL at which the info policy of the AA is available. 
    * - **claims**
      - List of JSON Objects that define the user's attributes required by the AA. Example: |br| ``{"https://attributes.eid.gov.it/fiscal_number":{"essential":true},`` |br| ``"email":{"essential":true},}``
    * - **service_documentation**
      - URL at which it is available the OAS3 document that describes how the AA services work.



Profile **sgd**
+++++++++++++++

For technical details and non-normative examples, see [LINK TO BE INSERTED HERE]


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
