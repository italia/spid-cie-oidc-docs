.. include:: ./common_definitions.rst


Trust Mark per CIE
++++++++++++++++++

TBD esempi non normativi


Profili dei Trust Mark
^^^^^^^^^^^^^^^^^^^^^^

Si possono definire svariati profili in accordo agli specifici bisogni delle FA e della TA. Nella CIE FED, durante la fase
di Onboarding, DEVONO essere emessi almeno i seguenti *trustmark_profile*:

 - **public**: l'entità nel claim *sub* appartiene alla pubblica amministrazione italiana.
 - **private**: l'entità nel claim *sub* appartiene al settore privato.

La tabella seguente riassume tutti i profili disponibili supportati per tutte le entità coinvolte nella CIE FED


.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Profilo TM**
      - **Descrizione**
      - **Tipi di entità sub**
    * - **public**
      - l'entità nel claim *sub* appartiene alla pubblica amministrazione italiana
      - Tutte
    * - **private**
      - l'entità nel claim *sub* appartiene al settore privato.
      - Tutte
    * - **native**
      - l'entità nell attributo *sub* è compatibile con CIE-OIDC-MOBILE – non ancora supportato
      - RP
    * - **underage**
      - l'entità nel claim *sub* fornisce servizi online per underage (non ancora supportato)
      - RP
    * - **aggregator**
      - l'entità nel claim *sub* è un soggetto aggregatore
      - SA




Esempi di Trust Mark CIE
^^^^^^^^^^^^^^^^^^^^^^^^

Il seguente è un esempio non normativo di un Trust Mark emesso da *MinInterno* per un'entità privata intermediaria.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.servizicie.interno.gov.it/federation_entity/private/",
             "iss":"https://registry.servizicie.interno.gov.it",
             "trust_mark":"$JWT"
         }
     ]
 }


Dove il payload JWT è il seguente:

.. code-block::

 {
     "id":"https://registry.servizicie.interno.gov.it/federation_entity/private/",
     "iss":"https://registry.servizicie.interno.gov.it",
     "sub":"https://intermediate.example.it",
     "iat":1579621160,
     "organization_type":"private",
     "id_code":"12345678900",
     "email":"email_or_pec@intermediate.it",
     "organization_name#it":"Full name of the SA",
     "ref":"https://reference_to_some_documentation.it/"
 }



Il seguente è un esempio non normativo di un TM emesso da un'entità Intermediaria verso un'entità Foglia RP.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.servizicie.interno.gov.it/openid_relying_party/public/",
             "iss":"https://intermediary.example.it",
             "trust_mark":"$JWT"
         }
     ]
 }


Dove il payload $JWT potrebbe essere come nel seguente esempio non normativo:

.. code-block::

 {
     "id":"https://registry.servizicie.interno.gov.it/openid_relying_party/public/",
     "iss":"https://intermediary.example.it",
     "sub":"https://rp.example.it",
     "iat":1579621160,
     "organization_type":"public",
     "id_code":"123456",
     "email":"email_or_pec@rp.it",
     "organization_name#it":"Full name of the RP",
     "ref":"https://reference_to_some_documentation.it/"
 }




Un esempio non normativo è dato qui sotto:

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.spid.gov.it/oauth_resource/aa/",
             "iss":"https://registry.spid.gov.it",
             "trust_mark":"$JWT"
         }
     ]
 } 

Dove il payload di JWT sarebbe come segue:

.. code-block::

 {
     "id":"https://registry.spid.gov.it/oauth_resource/aa/",
     "iss":"https://registry.spid.gov.it",
     "sub":"https://aa.example.it",
     "iat":1579621160,
     "organization_type":"public",
     "id_code":"123456",
     "email":"email_or_pec@aa.it",
     "organization_name#it":"Full name of the AA",
     "policy_uri#it":"url to AA privacy policy",
     "tos_uri#it":"url to AA info policy",
     "service_documentation":"url to AA OAS3 document",
     "attributos":{
         "https://attributes.eid.gov.it/fiscalNumber":{
             "essential":true
         }
     },
     "ref":"https://reference_to_some_documentation.it/"
 }

