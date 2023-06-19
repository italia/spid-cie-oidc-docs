.. include:: ../common/common_definitions.rst

.. _user_claims:

User attributes
---------------

The following table shows the list of user attributes supported by SPID and/or CIE. The variable ``$PREFIX=https://attributes.eid.gov.it`` represents the namespace.

.. list-table:: 
   :widths: 20 40 1
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **$PREFIX/spid_code** |br| Category:registry
     - Identification code. String. The identification code is assigned by the digital identity provider 
       and must be unique.

       The format is the following:

       ``<Identification code> = <cod_IdP><unique_number>``

       Where:

         **<cod_IdP>**: is a code made by 4 letters, uniquely assigned to the identity provider.

         **<unique_number>**: is an alphanumeric string composed by 10 characters that the identity provider 
         uniquely generates in its own domain.

       Example: 

       ``"$PREFIX/spid_code":"ABCD123456789A"``

     - |spid-icon|
   * - **given_name** |br| Category:registry
     - Name. String. String composed by a sequence of words, separated by single spaces, each starting with a capital letter.
       
       
       Example:

       ``"given_name":"Giovanni Mario"``

     - |spid-icon| |cieid-icon|
   * - **family_name** |br| Category:registry
     - Last name. String. String composed by a sequence of words, separated by single spaces, each starting with a capital letter.

       Example:

       ``"family_name":"Bianchi Verdi"``

     - |spid-icon| |cieid-icon|
   * - **place_of_birth** |br| Category:registry
     - Place of birth, province of birth. JSON Object: 

       "**locality** : String corresponding to the real estate registry code (Belfiore Code) of the city or foreign country of birth (e.g. "F205" for the city of Milano)

       "**region**" : String corresponding to the code of the province of birth.

       Example:

       .. code-block:: json

        "place_of_birth": {
            "region":"MI",
            "locality":"F205"
        }

     - |spid-icon| |cieid-icon|
   * - **birthdate** |br| Category:registry
     - Date of birth. String. Following the specifications ISO8601-2004 in the format
       YYYY indicates the year using 4 (four) digits |br|
       MM indicates the month with 2 (two) digits |br|
       DD indicates the day with 2 (two) digits |br|
       Example: |br|

       ``"birthdate":"2002-09-24"``

     - |spid-icon| |cieid-icon|
   * - **gender** |br| Category:registry
     - Gender. String. Values accepted: |br|
       "female" for female |br|
       "male" for male |br|
       Example: |br|

       ``"gender":"female"``

     - |spid-icon| |cieid-icon|
   * - **$PREFIX/company_name** |br| Category:registry
     - Company name. String. String composed by a sequence of words, separated by single spaces.
       In capital letters the substrings corresponding to names (e.g. "Agenzia per l'Italia Digitale")

       .. code-block:: json

         "$PREFIX/company_name": "Agenzia per l'Italia Digitale"

     - |spid-icon|
   * - **$PREFIX/registered_office** |br| Category: extra registry
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

       .. code-block:: json

         "$PREFIX/registered_office":{
             "formatted":"via Listz 21 00144 Roma"
         }

     - |spid-icon|
   * - **$PREFIX/fiscal_number** |br| Category:registry
     - Fiscal number of the natural person. String. For the format, please refer to the coding of the attribute
       CF for the certificates, proposed in the Draft ETSI EN 319 412-1, that implies, in the specific case, the following format:
       TINIT-<fiscal_number>
        
       Example:

       ``"$PREFIX/fiscal_number":“TINIT-ABCXYZ00W00Z000Z"``

     - |spid-icon| |cieid-icon|
   * - **$PREFIX/company_fiscal_number** |br| Category:registry
     - Fiscal number of the legal person. String. For the format, please refer to the coding of the attribute
       CF for the certificates, proposed in the Draft ETSI EN 319 412-1, that implies, in the specific case, the following format:

       ``TINIT-<fiscal_number>``

       Example:

       ``"$PREFIX/company_fiscal_number":"TINIT-ABCXYZ00W00Z000Z"``

     - |spid-icon|
   * - **$PREFIX/vat_number** |br| Category:registry
     - VAT number. String. For the format, please refer to the coding of the attribute VAT number for 
       the certificates, proposed in the Draft ETSI EN 319 412-1, that implies, in the specific case, the following format:

       ``VATIT-<PartitaIVA>``

       Example:

       ``"$PREFIX/vat_number": "VATIT-12345678901"``

     - |spid-icon|
   * - **document_details** |br| Category: extra registry
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

       .. code-block:: json

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
   * - **phone_number** |br| Category: extra registry
     - Mobile phone name. String. Numeric string without internal spaces |br|
       Example: |br|
       ``"phone_number": "VATIT-12345678901"``
     - |spid-icon| |cieid-icon|
   * - **phone_number_verified** |br| Category: extra registry
     - Boolean value indicating whether the user's mobile phone number has been verified by the OP. 
     - |cieid-icon|
   * - **$PREFIX/landline_number** |br| Category: extra registry
     - Landline number. String. Numeric string without internal spaces |br|
       Example: |br|
       ``"$PREFIX/landline_number":"VATIT-12345678901"``
     - |cieid-icon|
   * - **email** |br| Category: extra registry
     - E-mail address. String. Standard e-mail address |br|
       Example: |br|
       ``"email":"name@domain.it"``
     - |spid-icon| |cieid-icon|
   * - **email_verified** |br| Category: extra registry
     - Boolean value indicating whether the user's e-mail has been verified by the OP.
     - |cieid-icon|
   * - **$PREFIX/e_delivery_service** |br| Category: extra registry
     - Qualified electronic registered delivery. PEC e-mail address |br|
       Example: |br|
       ``"$PREFIX/e_delivery_service":"name@pecdomain.it"``
     - |spid-icon| |cieid-icon|
   * - **$PREFIX/eid_exp_date** |br| Category: extra registry
     - Identity expiry date. According to the specifications ISO8601-2004 in the format
       "YYYY-MM-DD" where |br|
       YYYY indicates the year using 4 (four) digits |br|
       MM indicates the month with 2 (two) digits |br|
       DD indicates the day with 2 (two) digits |br|
       Example: |br|
       ``"$PREFIX/eid_exp_date":"2002-09-24"``
     - |spid-icon|
   * - **address** |br| Category: extra registry
     - JSON Object (address):

        - "**street_address**": The attribute contains the address type (via, viale, piazza …), the address and the house number. The three informations are preferably sorted as in the specific countries.
       
        - "**postal_code**": ZIP 

        - "**locality**": City

        - "**region**": Province 

        - "**country_code**": Country

       Example: 
       
       .. code-block:: json

         "address": {
             "street_address":"Via Liszt 21",
             "postal_code":"00144",
             "locality":"Roma",
             "region":"RM",
             "country_code":"IT"
         }

     - |spid-icon| |cieid-icon|

.. _user_claims_scopes:


Examples
++++++++

For convenience, we report examples that produce the composition of a unique JSON Object, from
several attributes and in particular the claims ``"place_of_birth"``, ``"address"``, ``"document_details"``, ``$PREFIX/registered_office``.

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
     - .. code-block:: json

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
     - .. code-block:: json

        "address":{
            "street_address":"S.S. Salaria Km 23,800",
            "postal_code":"00015",
            "locality":"Monterotondo",
            "region":"RM",
            "country_code":"IT"
        }

There are cases, as for the United States of America, where both the country (US) and a State must be indicated.
In such cases the State is indicated in the field Province.
In the following, an example:

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
     - .. code-block:: json

        "address":{
            "street_address":"503,Washington Avenue",
            "postal_code":"12401",
            "locality":"Kingston",
            "region":"New york",
            "country_code":"US"
        }
