.. include:: ./common_definitions.rst


Trust Mark per SPID
+++++++++++++++++++

I Trust Mark riconoscibili all’interno della Federazione SPID sono emessi e firmati dalla AgID (TA) o suoi intermediari (SA) o Gestori Qualificati di Attributi (AA-Attribute Authority), se definiti all’interno dell’attributo **trust_marks_issuers** pubblicato all’interno dell’Entity Configuration del TA. Ogni partecipante DEVE esporre nella propria configurazione (EC) i TM rilasciati dalle autorità emittenti. 



Pubblicatori dei Trust Mark SPID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La TA definisce i TM e gli emettitori abilitati dalla Federazione, mediante il claim **trust_marks_issuers**, presente all’interno del proprio Entity Configuration. Il valore dell’attributo **trust_marks_issuers** è composto da un oggetto JSON avente come chiavi gli id dei TM e come valori la lista degli emittenti abilitati.

Di seguito un esempio non normativo dell’oggetto **trust_marks_issuers** all’interno della Entity Configuration del TA.

.. code-block::

 {
     "trust_marks_issuers":{
         "https://registry.agid.gov.it/openid_relying_party/public/":[
             "https://registry.spid.agid.gov.it/",
             "https://public.intermediary.spid.it/"
         ],
         "https://registry.agid.gov.it/openid_relying_party/private/":[
             "https://registry.spid.agid.gov.it/",
             "https://private.other.intermediary.it/"
         ]
     }
 }



Esempi di Trust Mark SPID
^^^^^^^^^^^^^^^^^^^^^^^^^

I TM emessi per le Foglie DEVONO essere pubblicati dalle Foglie stesse nelle proprie **Entity Configuration**, all’interno dell’attributo **trust_marks**. Questo è composto da liste di oggetti JSON, ognuno dei quali DEVE contenere almeno gli attributi **id** e **trust_mark**, il primo identifica il TM, il secondo contiene il JWT firmato del TM.

Di seguito un esempio non normativo dell’oggetto **trust_marks** all’interno della Entity Configuration di una Foglia di tipo RP.


.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://www.spid.gov.it/openid-federation/agreement/sp-public/",
             "trust_mark":"…"
         }
     ]
 }



Quello che segue è un esempio non normativo di un marchio di fiducia emesso da AgID per un intermediario privato.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.agid.gov.it/federation_entity/private/",
             "trust_mark":"…"
         }
     ]
 }

Dove il contenuto del JWT firmato all’interno dell’attributo **trust_mark** corrisponde a:

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



Un’entità intermediaria o Soggetto Aggregatore (SA) è riconoscibile come emettitore di Trust Mark. Quello che segue è un esempio non normativo di un Trust Mark emesso da un SA a favore di un RP suo discendente.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.agid.gov.it/openid_relying_party/public/",
             "trust_mark":"…"
         }
     ]
 }


Dove il contenuto del JWT firmato all’interno dell’attributo **trust_mark** corrisponde al seguente esempio non normativo.

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


