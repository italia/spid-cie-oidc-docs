.. include:: ./common_definitions.rst


Trust Mark CIEid
----------------

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


Profilo **sgd**
+++++++++++++++

Per i dettagli tecnici e gli esempi non normativo si veda [INSERIRE LINK ALLA DOCUMENTAZIONE]
