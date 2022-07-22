.. include:: ../common/common_definitions.rst


Trust Mark per SPID
+++++++++++++++++++


Esempi di Trust Mark SPID
^^^^^^^^^^^^^^^^^^^^^^^^^

I TM emessi per le foglie DEVONO essere pubblicati dalle foglie stesse nelle proprie **Entity Configuration**, all'interno dell'attributo **trust_marks**. Questo è composto da liste di oggetti JSON, ognuno dei quali DEVE contenere almeno gli attributi **id** e **trust_mark**, il primo che identifica il TM, il secondo che contiene il JWT firmato del TM.

Di seguito un esempio non normativo dell'oggetto **trust_marks** all'interno della Entity Configuration di una Foglia di tipo RP.


.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://www.spid.gov.it/openid_relying_party/public/",
             "trust_mark":"$JWT"
         }
     ]
 }



Quello che segue è un esempio non normativo di un Trust Mark emesso dalla AgID per un Intermediario privato.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.agid.gov.it/federation_entity/private/",
             "trust_mark":"$JWT"
         }
     ]
 }

Dove il contenuto del JWT firmato all'interno dell'attributo **trust_mark** corrisponde a:

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
     "ref":"https://reference_to_some_documentation.example.it/",
     "sa_profile": "light"
 }



Un'entità Intermediaria o Soggetto Aggregatore (SA) è riconoscibile come emettitore di Trust Mark. Quello che segue è un esempio non normativo di un Trust Mark emesso da un SA a favore di un RP suo discendente.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.agid.gov.it/openid_relying_party/public/",
             "trust_mark":"$JWT"
         }
     ]
 }


Dove il contenuto del JWT firmato all'interno dell'attributo **trust_mark** corrisponde al seguente esempio non normativo:

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


