.. include:: ./common_definitions.rst


Profili dei Trust Mark riconusciuti da CIEid
--------------------------------------------

La tabella seguente riassume tutti i profili disponibili per tutte le entità coinvolte e supportate dalla Federazione CIEid.


.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Profilo TM**
      - **Descrizione**
      - **Tipi di entità sub**
    * - **public**
      - l'entità nel claim *sub* appartiene alla pubblica amministrazione italiana
      - RP, OP
    * - **private**
      - l'entità nel claim *sub* appartiene al settore privato.
      - RP
    * - **intermediary**
      - l'entità nel claim *sub* è un Soggetto Aggregatore
      - SA
    * - **attribute-authority**
      - l'entità nel claim *sub* è una Attribute Authority
      - AA
    * - **sgd**
      - l'entità nel claim *sub* è un RP o un SA che ha aderito alla AA Sistema di Gestione Deleghe
      - RP

Profili **public** e **private**
++++++++++++++++++++++++++++++++

Si applicano i claim presenti nella tabella riportata nella Sezione :ref:`Composizione dei Trust Mark <ComposizioneTM>`

Profilo **intermediary**
++++++++++++++++++++++++

In aggiunta ai claim dei profili **public** e **private**, il profilo **intermediary** aggiunge il seguente claim:

.. list-table::
    :widths: 20 60
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
    * - **sa_type**
      - DEVE essere valorizzata con **"full"** o **"light"** a seconda della modalità con cui operano rispetto ai Soggetti Aggregati

.. seealso::

    Si veda Sezione :ref:`Soggetti aggregatori nel contesto Federativo <Soggetti_aggregatori>`

Profilo **attribute-authority**
+++++++++++++++++++++++++++++++

Per i dettagli tecnici e gli esempi non normativo si veda [INSERIRE LINK ALLA DOCUMENTAZIONE]

Profilo **sgd**
+++++++++++++++

Per i dettagli tecnici e gli esempi non normativo si veda [INSERIRE LINK ALLA DOCUMENTAZIONE]

Esempi di Trust Mark CIE
++++++++++++++++++++++++

Il seguente è un esempio non normativo di un Trust Mark emesso da *MinInterno* per SA di tipo **full** afferente all pubblica amministrazione.

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


Dove il payload JWT è il seguente:

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



Il seguente è un esempio non normativo di un TM emesso da un SA a un'entità Foglia RP afferente alla Pubblica Amministrazione.

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


Dove il payload $JWT potrebbe essere come nel seguente esempio non normativo:

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
