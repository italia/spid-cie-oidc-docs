.. include:: ./common_definitions.rst

Federation Endpoint
-------------------

Tutte le entità DEVONO contenere i seguenti endpoint:

 - **/.well-known/openid-federation** fornisce la Entity Configuration (vedi sezione  :ref:`Ottenere informazioni di configurazione dell'entità di Federazione<obtaining_federation_entity_configuration_information>`)

Un **FA** (**SA** o **TA**) DEVE, in aggiunta, offrire i seguenti endpoint:

 - **fetch entity statement endpoint** fornisce un FA relativo ad una subordinata, ottenendo così un entity statement (vedi sezione :ref:`Prelevare Entity Statement<fetching_entity_statements>`)  
 - **resolve entity statement endpoint** risolve i Metadata di Federazione (vedi sezione :ref:`Risolvere Entity Statements<resolve_entity_statements>`)
 - **trust mark introspection endpoint** fornisce lo stato del Trust Mark (vedere sezione :ref:`Stato del Trust Mark<trust_mark_status>`)
 - **entity listing endpoint** fornisce una lista di tutte le subordinate di un'entità (vedere sezione :ref:`Elenchi di Entità<entity_listings>`)
 - **resolve endpoint** ottiene dal risolutore dei Metadata risolti e TM di un'entità vista/fidata (vedere sezione
   :ref:`Risolvere i Metadata di Federazione <resolve_entity_statements>`)



.. _obtaining_federation_entity_configuration_information:

Ottenere informazioni di configurazione dell'entità di Federazione
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

La configurazione di entità di ogni Federazione DEVE essere esposta ad un endpoint ben conosciuto con il seguente percorso: **/.well-known/openid-federation**.


Federation Entity Configuration Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: 

 GET /.well-known/openid-federation HTTP/1.1
 Host: openid.sunet.se


Federation Entity Configuration Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una risposta positiva è una configurazione di entità (come descritto in :ref:`Trust Mark<Trust_Mark>`), dove il tipo di contenuto DEVE essere impostato in **application/jose**. In caso di errore, vedere sezione :ref:`Generic Error Response<generic_error_response>`. Il seguente è un esempio non normativo di response:


.. code-block:: 

 HTTP/1.1 200 OK
 Last-Modified: Thu, 29 Aug 2019 08:54:26 GMT
 Content-Type: application/jose 

 $ENTITY_CONFIGURATION

Per esempi di $ENTITY_CONFIGURATION vedere la sezione :ref:`Esempi di Entity Configuration<Esempio_EN1>`.


.. seealso::

 `OIDC-FED#Section.6`_


.. _fetching_entity_statements:

Prelevare Entity Statements
+++++++++++++++++++++++++++

Tutte le entità che pubblicano ES riguardo altre entità (es. **SA** e **TA**) DEVONO esporre un **Fetch Endpoint**. Viene usato da un'entità per ottenere gli ES.



Fetch Entity Statements Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La richiesta DEVE essere una richiesta HTTP che usa il metodo GET ed ha i seguenti parametri di query:

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **sub**
     - String. L'identificatore di entità del soggetto per il quale si vuole l'emissione dell'ES.
     - |spid-icon| |cieid-icon|


Il seguente è un esempio non normativo di una richiesta API per un ES:


.. code-block:: 

 GET /federation_api_endpoint?
 iss=https%3A%2F%2Fedugain.org%2Ffederation&
 sub=https%3A%2F%2Fopenid%2Esunet%2Ese HTTP/1.1
 Host: edugain.org



Fetch Entity Statements Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una risposta positiva è un ES firmato dove il tipo di contenuto DEVE essere impostato a **application/jose**. In caso di errore, vedere sezione :ref:`Generic Error Response<generic_error_response>`.

Segue un esempio non normativo di risposta, prima della serializzazione e dell'aggiunta di una firma:


.. code-block:: 

 HTTP/1.1 200 OK
 Last-Modified: Mon, 17 Dec 2018 11:15:56 GMT
 Content-Type: application/jose

 $ENTITY_STATEMENT 

Per esempi di $ENTITY_STATEMENT vedere la sezione :ref:`Esempi di Entity Statement<Esempio_EN2>`.



.. seealso::

 `OIDC-FED#Section.7.1`_



.. _resolve_entity_statements:

Risolvere i Metadata di Federazione
+++++++++++++++++++++++++++++++++++

Un'entità PUÒ usare il Resolve Endpoint per ottenere dal risolutore dei Metadata risolti e dei TM di un'entità vista/fidata. Il risolutore DEVE prelevare l'ES autofirmato dei soggetti, prelevare una Trust Chain che va dall'ES dei soggetti al TA specificato, verificare la Trust Chain e quindi applicare, ai Metadata degli ES, tutte le politiche presenti nella Trust Chain. DEVE inoltre verificare che i TM presenti siano attivi. Se trova TM non attivi, allora DOVREBBERO essere lasciati fuori dall'insieme di risposta.


Resolve Endpoint Request
^^^^^^^^^^^^^^^^^^^^^^^^

La richiesta DEVE essere una richiesta HTTP che usa un metodo GET e lo schema https al resolve endpoint con i seguenti parametri della stringa di query:

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **sub**
     - String. L'identificatore di entità dell'entità di cui sono richiesti i dati risolti
     - |spid-icon| |cieid-icon|
   * - **anchor**
     - String. Il TA che il peer remoto DEVE usare nella risoluzione dei Metadata. Il valore è un identificatrore di entità.
     - |spid-icon| |cieid-icon|
   * - **type**
     - Un tipo specifico di Metadata da risolvere. Se assente, allora ci si aspetta che tutti i tipi di Metadata vengano ritornati.
     - |spid-icon| |cieid-icon|



Segue un esempio non normativo di **Resolve request**:


.. code-block:: 

 GET /resolve?
 sub=https%3A%2F%2Fop.example.it%2Fspid&
 type=openid_provider&
 anchor=https%3A%2F%2Fswamid.se&
 iss=https%3A%2F%2Ffoodle.uninett.no HTTP/1.1
 Host: openid.sunet.se



Resolve Endpoint Response
^^^^^^^^^^^^^^^^^^^^^^^^^

Il response è un JWT firmato contenente Metadata "risolti", TM verificati e la prova della Trust Chain. La response è un JWT firmato con la chiave utilizzata dal risolutore all'interno della propria Entity Configuration. Questo significa che l'emettitore della richiesta può facilmente trovare e verificare le chiavi di firma del risolutore raccogliendo e verificando l'appropriata Trust Chain.

Segue un esempio non normativo di risposta, prima di serializzare e aggiungere una firma:

.. code-block:: 

 {
     "iss":"https://resolver.example.it/spid",
     "sub":"https://op.example.it/spid",
     "aud":[
         "https://foodle.uninett.no"
     ],
     "iat":1516239022,
     "exp":1516298022,
     "metadata":{
         "openid_provider":{
             ...           
         }
     },
     "trust_marks":[
         {
             "id":"https://www.spid.gov.it/certification/rp",
             "trust_mark":
                 ...
         }
     ]
 }


.. seealso::

 `OIDC-FED#Section.7.2`_




.. _trust_mark_status:

Stato del Trust Mark
++++++++++++++++++++

Permette a un'entità di verificare se un TM è ancora attivo o no. La query DEVE essere mandata all'emettitore del TM.


Status Request
^^^^^^^^^^^^^^

DEVE essere una richiesta HTTP che usa il metodo GET e lo schema https verso uno status endpoint risolto con i seguenti parametri sulla stringa di query:



.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **sub**
     - String. L'identificativo univoco del soggetto per l'entità alla quale è stato inviato il TM.
     - |spid-icon| |cieid-icon|
   * - **id**
     - String. Identifica il TM.
     - |spid-icon| |cieid-icon|
   * - **iat**
     - UNIX Timestamp con l'istante di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|


Segue un esempio non normativo di richiesta che usa **sub** e **id**:


.. code-block:: 

 GET /federation_api?
 operation=trust_mark
 &sub=https%3A%2F%2Fopenid.sunet.se%2FRP
 &id=https%3A%2F%2Frefeds.org%2Fsirtfi
 HTTP/1.1
 Host: operations.swamid.se



Status Response
^^^^^^^^^^^^^^^

IL corpo della risposta HTTP DEVE essere un oggetto JSON contenente i claim di seguito riportati e il tipo di contenuto deve essere impostato a **application/json**:


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **active**
     - Boolean. Indica ae il TM è attivo o no.
     - |spid-icon| |cieid-icon|



Segue un esempio non normativo di risposta:

.. code-block:: 

 HTTP/1.1 200 OK
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/json

 {
   "active"=true
 }



.. seealso::

 `OIDC-FED#Section.7.4`_




.. _entity_listings:

Lista delle Entità di Federazione
+++++++++++++++++++++++++++++++++

UN'entità PUÒ interrogare un'altra entità per ottenere una lista di tutte le entità a lei immediatamente subordinate e di cui è pronta a emettere statement (in alcuni casi PUÒ essere una lista molto lunga).


Entity Listings Request
^^^^^^^^^^^^^^^^^^^^^^^

DEVE essere una richiesta HTTP che usa il metodo GET e lo schema https verso un *resolved list endpoint* con i seguenti parametri nella stringa di richiesta:


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **entity_type**
     - Set (**federation_entity**, **openid_relying_party**, **openid_provider**).  Filtra il tipo di entità. 
     - |spid-icon| |cieid-icon|


Segue un esempio non normativo:

.. code-block:: 

 GET /list HTTP/1.1
 Host: openid.sunet.se


Entity Listings Response
^^^^^^^^^^^^^^^^^^^^^^^^

La risposta DEVE contenere una lista JSON con gli identificatori delle entità conosciute.

Segue un esempio non normativo di risposta:

.. code-block:: 

 HTTP/1.1 200 OK
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/json

 [
   "https://ntnu.andreas.labs.uninett.no/",
   "https://blackboard.ntnu.no/openid/callback",
   "https://serviceprovider.andreas.labs.uninett.no/application17"
 ]


.. seealso::

 `OIDC-FED#Section.7.3`_



Advanced Entity Listings Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: 

 GET /federation_adv_list HTTP/1.1
 Host: registry.servizicie.interno.gov.it



Advanced Entity Listings Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: 

 HTTP/1.1 200 OK
 Last-Modified: Mon, 17 Dec 2018 11:15:56 GMT
 Content-Type: application/json

 {
     "iss":"https://registry.servizicie.interno.gov.it/openid_relying_party/public/",
     "iat":1620050972,
     "entities":[
         {
             "https://rp.example.it/":{
                 "iat":1588455866
             }
         },
         {
             "https://rp.another.it/":{
                 "iat":1588455856
             }
         },
         {
             "https://rp.it/":{
                 "iat":1588355866
             }
         }
         ... # molti altri elementi
     ],
     "page":1,
     "total_pages":2,
     "total_entries":189,
     "next_page_path":"/federation_adv_list/?page=2",
     "prev_page_path":""
 }



.. _generic_error_response:

Generic Error Response
++++++++++++++++++++++

Se la richiesta è malformata o avvengono errori durante l'elaborazione della richiesta, DOVREBBE essere utilizzato il seguente formato di errore indipendentemente dall'operazione specificata.
La risposta HTTP DEVE essere avere un codice nell'intervallo 400/500, che dia un'indicazione del tipo di errore. Il corpo della risposta DEVE essere un oggetto JSON contenente i claim di seguito riportati e il tipo di contenuto DEVE essere di tipo **application/json**.


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **operation**
     - L'operazione della richiesta
     - |spid-icon| |cieid-icon|
   * - **error**
     - Il codice di errore
     - |spid-icon| |cieid-icon|
   * - **error_description**
     - Un breve testo leggibile che descrive l'errore
     - |spid-icon| |cieid-icon|


Segue un esempio non normativo di error response:


.. code-block:: 

 GET /federation_adv_list HTTP/1.1
 Host: registry.servizicie.interno.gov.it


The following is a non-normative example of an error response:


.. code-block:: 

 HTTP/1.1 400 Bad request
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/json

 {
     "operation":"resolve",
     "error":"invalid_request",
     "error_description":"Required request parameter [sub] was missing."
 }


.. seealso::

 `OIDC-FED#Section.7.5`_
