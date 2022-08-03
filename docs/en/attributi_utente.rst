.. include:: ../common/common_definitions.rst

.. _user_claims:

User attributes
---------------


.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - **Claim**
     - **Category**
     - **Description**
     - **Supported by**
   * - **https://attributes.eid.gov.it/spid_code**
     - registry
     - Identification code. String. The identification code is assigned by the digital identity provider 
       and must be unique.

       The format is the following:

       .. code-block::

         <Identification code> = <cod_IdP><unique number>

       Where:

         **<cod_IdP>**: is a code made by 4 letters, uniquely assigned to the identity provider.

         **<unique number>**: is an alphanumeric string composed by 10 characters that the identity provider 
         uniquely generates in its own domain.

       Example: 

       .. code-block::

         "https://attributes.eid.gov.it/spid_cod":"ABCD123456789A"

     - |spid-icon|
   * - **given_name**
     - registry
     - Name. String. String composed by a sequence of words, separated by single spaces, each starting with a capital letter.
       
       
       Example:

       .. code-block::
      
         "given_name":"Giovanni Mario"

     - |spid-icon| |cieid-icon|
   * - **family_name**
     - registry
     - Last name. String. String composed by a sequence of words, separated by single spaces, each starting with a capital letter.

       Example:

       .. code-block::
       
         "family_name":"Bianchi Verdi"

     - |spid-icon| |cieid-icon|
   * - **place_of_birth**
     - registry
     - Place of birth, province of birth. JSON Object: 

       "**locality** : String corresponding to the real estate registry code (Belfiore Code) of the city or foreign country of birth (e.g. "F205" for the city of Milano)

       "**region**" : String corresponding to the code of the province of birth.

       Example:

       .. code-block::

        "place_of_birth":{
            "region":"MI",
            "locality":"F205"
        }

     - |spid-icon| |cieid-icon|
   * - **birthdate**
     - registry
     - Date of birth. String. Following the specifications ISO8601-2004 in the format
       YYYY indicates the year using 4 (four) digits |br|
       MM indicates the month with 2 (two) digits |br|
       DD indicates the day with 2 (two) digits |br|
       Example: |br|

       .. code-block::

         "birthdate":"2002-09-24"

     - |spid-icon| |cieid-icon|
   * - **gender**
     - registry
     - Gender. String. Values accepted: |br|
       "F" for female |br|
       "M" for male |br|
       Example: |br|

       .. code-block::

         "gender":"F"

     - |spid-icon| |cieid-icon|
   * - **https://attributes.eid.gov.it/company_name**
     - registry
     - Company name. String. String composed by a sequence of words, separated by single spaces.
       In capital letters the substrings corresponding to names (e.g. "Agenzia per l'Italia Digitale")

       .. code-block::

         "company_name":"Agenzia per l'Italia Digitale"

     - |spid-icon|
   * - **https://attributes.eid.gov.it/registered_office**
     - extra registry
     - Registered Office. JSON Object: formatted, street_address, locality, region, postal_code, country, 
       country_code.
       Json made of a string composed by a sequence of words, separated by single spaces, representing:

       - Type of address (via, viale, piazza …) 
       - Address
       - Hiuse number 
       - ZIP
       - City 
       - Province

       the string is included in the claim "formatted" of the JSON Object "address"

       Example:

       .. code-block::

         "https://attributes.eid.gov.it/registered_office":{
             "formatted":"via Listz 21 00144 Roma"
         }

     - |spid-icon|
   * - **https://attributes.eid.gov.it/fiscal_number**
     - registry
     - Fiscal number of the natural person. String. For the format, please refer to the coding of the attribute
       CF for the certificates, proposed in the Draft ETSI EN 319 412-1, that implies, in the specific case, the following format:
       TINIT-<FiscalNumber>
        
       Example:

       .. code-block::

          "https://attributes.eid.gov.it/fiscal_number": "TINIT-ABCXYZ00W00Z000Z"

     - |spid-icon| |cieid-icon|
   * - **https://attributes.eid.gov.it/**
     - registry
     - Fiscal number of the legal person. String. For the format, please refer to the coding of the attribute
       CF for the certificates, proposed in the Draft ETSI EN 319 412-1, that implies, in the specific case, the following format:

       TINIT-<FiscalNumber>

        .. code-block::

          "https://attributes.eid.gov.it/company_fiscalNumber":"TINIT-ABCXYZ00W00Z000Z"

     - |spid-icon|
   * - **https://attributes.eid.gov.it/vat_number**
     - registry
     - VAT number. String. For the format, please refer to the coding of the attribute VAT number for 
       the certificates, proposed in the Draft ETSI EN 319 412-1, that implies, in the specific case, the following format:

       VATIT-<VATnumber>

       Example:

       .. code-block::

          "https://attributes.eid.gov.it/vat_number": "VATIT-12345678901"

     - |spid-icon|
   * - **document_details**
     - extra registry
     - Identity document. JSON Object (document):

       Json contains the proprieties that represent:

        - "**type**" : accepted values:

          - *cartaIdentita, passaporto, patenteGuida,*

          - *patenteNautica, librettoPensione,*

          - *patentinoImpTermici, portoArmi,*

          - *tesseraRiconoscimento;*

        - "**document_number**" : Document number;
        - "**issuer**" : <issuing Entity> JSON Object:

          - "**name**" string obtained from the concatenation
            of the terms that build the Entity name
            unless conjunctions, articles and prepositions.

              E.g. regioneLazio ( Region Lazio);
              provinciaCatania ( Province of Catania);
              prefetturaRoma ( Prefecture of Roma );
              MinisteroEconomiaFinanze ( Ministry 
              of Economy and Finance );

        - "**date_of_issuance**" : date of issuance of the document;

        - "**date_of_expiry**" : expiry date of the document.

       Example:

       .. code-block::

        "document_details":{
            "type":"cartaIdentita",
            "document_number":"AS09452389",
            "issuer":{
                "name":"ComuneRoma"
            },
            "date_of_issuance":"2013-01-02",
            "date_of_expiry":"2013-01-31"
        }

     - |spid-icon| |cieid-icon|
   * - **phone_number**
     - extra registry
     - Mobile phone name. String. Numeric string without internal spaces |br|
       Example: |br|
       ``"phone_number": "VATIT-12345678901"``
     - |spid-icon| |cieid-icon|
   * - **email**
     - extra registry
     - E-mail address. String. Standard e-mail address |br|
       Example: |br|
       ``"email": "name@domain.it"``
     - |spid-icon| |cieid-icon|
   * - **https://attributes.eid.gov.it/e_delivery_service**
     - extra registry
     - Digital domicile. PEC e-mail address |br|
       Example: |br|
       ``"https://attributes.eid.gov.it/e_delivery_service":"name@pecdomain.it"``
     - |cieid-icon|
   * - **https://attributes.eid.gov.it/eid_exp_date**
     - extra registry
     - Identity expiry date. According to the specifications ISO8601-2004 in the format
       "YYYY-MM-DD" where |br|
       YYYY indicates the year using 4 (four) digits |br|
       MM indicates the month with 2 (two) digits |br|
       DD indicates the day with 2 (two) digits |br|
       Example: |br|
       ``"https://attributes.eid.gov.it/id_exp_date":"2002-09-24"``
     - |spid-icon|
   * - **address**
     - extra registry 
     - Physical domicile address |br|
       ZIP code of the physical domicile |br|
       City of the physical domicile |br|
       Province of the physical domicile |br|
       Country of the physical domicile |br|.
       JSON Object (address):
       Formatted, **street_address**
       (**mandatory**), locality, region, postal_code, country, country_code
       The attribute contains the address type (via, viale, piazza …), the address and the house number.
       The three informations are preferably sorted as in the specific countries.

        - "**street_address**": The attribute contains the address type (via, viale, piazza …), the address and the house number. The three informations are preferably sorted as in the specific countries.
       
        - "**postal_code**": ZIP 

        - "**locality**": City

        - "**region**": Province 

        - "**country_code**" : Country

       Example: 
       
       .. code-block:: 

         "address":{
             "street_address":"Via Liszt 21",
             "postal_code":"00144",
             "locality":"Roma",
             "region":"RM",
             "country_code":"IT"
         }

     - |spid-icon| |cieid-icon|

.. _user_claims_scopes:


Non-normative examples
++++++++++++++++++++++

For convenience, we report examples that produce the composition of a unique JSON Object, from
several attributes and in particular the claims "place_of_birth", "address", "document_details", ``https://attributes.eid.gov.it/registered_office``.

As an example, two Italian addresses are reported:


.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - **Attribute**
     - **Example of OIDC coding**
   * - Physical domicile address
       ZIP of the physical domicile
       City of the of the physical domicile
       Province of the physical domicile
       Country of the physical domicile
     - .. code-block::

        "address":{
            "street_address":"Via Liszt 21",
            "postal_code":"00144",
            "locality":"Roma",
            "region":"RM",
            "country_code":"IT"
        }

   * - Physical domicile address
       ZIP of the physical domicile
       City of the of the physical domicile
       Province of the physical domicile
       Country of the physical domicile
     - .. code-block::

        "address":{
            "street_address":"S.S. Salaria Km 23,800",
            "postal_code":"00015",
            "locality":"Monterotondo",
            "region":"RM",
            "country_code":"IT"
        }

There are cases, as for the United States of America, where not only the country (US), but also a State, must be indicated.
In such cases the State is indicated in the field Province.
Following, an example:

.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - **Attribute**
     - **Example of OIDC coding**
   * - Physical domicile address
       ZIP of the physical domicile
       City of the of the physical domicile
       Province of the physical domicile
       Country of the physical domicile
     - .. code-block::

        "address":{
            "street_address":"503,Washington Avenue",
            "postal_code":"12401",
            "locality":"Kingston",
            "region":"New york",
            "country_code":"US"
        }

