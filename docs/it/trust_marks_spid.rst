.. include:: ./common_definitions.rst


Trust Mark per SPID
+++++++++++++++++++

I Trust Marks riconoscibili all’interno della Federazione SPID sono emessi e firmati dalla AgID (TA) o suoi intermediari (SA) o dai Gestori di attributi qualificati (AA) se definiti all’interno dell’attributo **trust_mark_issuers** pubblicato all’interno dell’Entity Configuration del TA. Ogni partecipante DEVE esporre nella propria configurazione (EC) i TM rilasciati dalle autorità emittenti. 

I Trust Mark rappresentano il primo filtro per l’instaurazione della fiducia tra le parti, sono elementi indispensabili per avviare la risoluzione dei metadati. *In loro assenza una entità non è riconoscibile come partecipante all’interno della Federazione SPID.*

All’interno della Federazione SPID i Trust Mark presentano degli identificativi univoci in formato URL che adottano la seguente struttura:

<domain> / <entity_type> / <trustmark_profile> /



Validazione dei Trust Mark
^^^^^^^^^^^^^^^^^^^^^^^^^^

Esistono due modi per validare un Trust Mark:

 1. Validazione **statica**. Il Trust Mark viene validato mediante il certificato pubblico dell’autorità che lo ha emesso (attributo **iss**), sulla base della corrispondenza dell’attributo **sub** con il medesimo attributo della Entity Configuration in cui è contenuto e sulla base del valore di scadenza (attributo **exp**).

 2. Validazione **dinamica**. I partecipanti della federazione possono interrogare l’endpoint :ref:`trust mark status<Trust_mark_status_endpoint>` erogato dal suo emittente (attributo iss) per la verifica in tempo reale dei TM da lui emessi. 

Tutti gli emittenti di Trust Mark DEVONO esporre un endpoint di trust mark status per consentire la validazione **dinamica**.


Revoca dei Trust Mark
^^^^^^^^^^^^^^^^^^^^^

Un Trust Mark può essere revocato in qualsiasi momento. In caso di esclusione di un Soggetto Aggregato da parte della Autorità di Federazione, questa comunica al Soggetto Aggregatore l’esclusione dell’Aggregato. Di conseguenza il SA revoca il TM per il suo discendente.


Pubblicazione dei Trust Marks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La TA definisce i TM e gli emittenti di questi abilitati nella Federazione mediante il attributo **trust_mark_issuers**, presente all’interno del proprio Entity Configuration. Il valore dell’attributo **trust_mark_issuers** è composto da un oggetto JSON, avente come chiavi gli id dei TM e come valori la lista degli emittenti abilitati.

Di seguito un esempio non normativo dell’oggetto **trust_mark_issuers** all’interno della Entity Configuration del TA.

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


I TM emessi per le Foglie DEVONO essere pubblicati dalle stesse all’interno della proprie Entity Configuration, all’interno dell’attributo **trust_marks**. Questo è composto da lista di oggetti JSON, ognuno di questi DEVE contenere almeno gli attributi **id** e **trust_mark**, il primo identifica il TM, il secondo contiene il JWT firmato del TM.

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


Composizione dei Trust Mark 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

gli attributi definiti all’interno dei Trust Marks aderiscono a quanto definito all’interno dello standard OIDC Federation 1.0 (documento giunto attualmente al DRAFT 18). Questi sono di seguito riportati.

.. list-table::
    :widths: 20 20 40 20
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
      - **Obbligatorio**
    * - **iss**
      - String
      - URL che identifica univocamente l’Autorità che lo ha emesso.
      - |check-icon|
    * - **sub**
      - String
      - URL che identifica univocamente il soggetto per il quale il Trust Mark è stato emesso.
      - |check-icon|
    * - **id**
      - String
      - Identificativo univoco del Trust Mark.
      - |check-icon|
    * - **iat**
      - UNIX Timestamp
      - Quando è stato emesso questo marchio di fiducia. Espresso come “Seconds Since the Epoch” :rfc:`7519`.
      - |check-icon|
    * - **logo_uri**
      - String
      - Un URL che punta al logo rappresentante il Trust Mark.
      - |check-icon|
    * - **exp**
      - UNIX Timestamp
      - Momento oltre il quale non sarà più valido. Espresso come “Seconds Since the Epoch” :rfc:`7519` e corrispondente o inferiore alla durata della validità della convenzione amministrativa di adesione alla Federazione.
      - |check-icon|
    * - **ref**
      - String
      - URL che punta a informazioni presenti sul web relative a questo marchio di fiducia
      - |uncheck-icon|

La seguente tabella riassume tutti i profili supportati per le entità di tipo RP coinvolte nella Federazione SPID.

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Tipo**
      - **Descrizione**
      - **Entità**
    * - **public**
      - Indica che il RP appartiene ad una Pubblica Amministrazione.
      - All
    * - **private**
      - Indica che il RP appartiene al settore privato.
      - All


Agli attributi dei TM definiti nella tabella precedente, i Trust Mark SPID aggiungono i seguenti.

.. list-table::
    :widths: 20 20 40 20
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
      - **Obbligatorio**
    * - **organization_type**
      - String
      - Specifica se l’ente appartiene alla pubblica amministrazione italiana o al settore privato (**private** o
        **public**).
      - |check-icon|
    * - **id_code**
      - String
      - Codice di identificazione dell’organizzazione. A seconda del valore del tipo di organizzazione, deve essere
        indicato il codice IPA (per il tipo di organizzazione pubblica) o il numero di partita IVA (per quello privato).
      - |check-icon|
    * - **email**
      - String
      - Email istituzionale o PEC dell’organizzazione.
      - |check-icon|
    * - **organization_name**
      - String
      - Il nome completo dell’entità che fornisce i servizi
      - |check-icon|



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

Un’entità intermediaria (SA) è riconoscibile come emittente di Trust Mark. Quello che segue è un esempio non normativo di un Trust Mark emesso da un Soggetto Aggregatore a favore di un RP suo discendente.

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


.. _Trust_mark_status_endpoint:

Trust mark status endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^

L’assegnazione di un Trust Mark ad un soggetto viene effettuato presso questo endpoint secondo le modalità definite all’interno di `OIDC-FED#Section.7.4`_.
