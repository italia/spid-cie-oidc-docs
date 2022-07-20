.. include:: ./common_definitions.rst


Trust Mark per SPID
+++++++++++++++++++

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



Quello che segue è un esempio non normativo di un marchio di fiducia emesso dalla AgID per un Intermediario privato.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.agid.gov.it/federation_entity/private/light/",
             "trust_mark":"$JWT"
         }
     ]
 }

Dove il contenuto del JWT firmato all'interno dell'attributo **trust_mark** corrisponde a:

.. code-block::

 {
     "id":"https://registry.agid.gov.it/federation_entity/private/light/",
     "iss":"https://registry.agid.gov.it",
     "sub":"https://intermediary.example.it",
     "iat":1579621160,
     "organization_type":"private",
     "id_code":"12345678900",
     "email":"email_or_pec@example.it",
     "organization_name":"Full name of the SA",
     "ref":"https://reference_to_some_documentation.example.it/"
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


Dove il contenuto del JWT firmato all'interno dell'attributo **trust_mark** corrisponde al seguente esempio non normativo.

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


