.. include:: ./common_definitions.rst


.. _Entity_Configuration:

Entity Statement e Entity Configuration
---------------------------------------

Il componente basilare per costruire una Catena di Fiducia (Trust Chain) è l'*Entity Statement (ES)*, un JWT crittografico che contiene le chiavi di firma delle entità e ulteriori dati usati per controllare il processo di risoluzione della Trust Chain (come l'*authority_hints* che specifica chi è il superiore di un'entità). Quando uno statement è autofirmato da un’entità, viene chiamato *Entity Configuration (EC)*.

Un *EC* è un metadata di federazione in formato Jose e firmato dal soggetto che lo emette e riguardante se stesso, all’interno del quale i valori degli attributi **iss** e **sub** contengono il medesimo valore (URL).


Firma
+++++

La firma dei JWT `[RFC7515]`_ avviene mediante l'algoritmo RSA SHA-256 (RS256). Tutti i partecipanti della Federazione DEVONO supportare questo algoritmo di firma. Tutte le operazioni di firma relative agli ES, EC e TM sono eseguite con le chiavi pubbliche di Federazione (distinguiamo le chiavi di Federazione da quelle di OIDC Core. Qujesti ultimi risiedono nei metadata OIDC. Un ES o EC contiene sia le chiavi pubbliche di Federazione che i metadata OIDC).


Attributi (claim)
+++++++++++++++++

EC ed ES contengono i seguenti attributi comuni:

.. list-table::
   :widths: 20 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Tipo**
     - **Descrizione**
     - **Obbligatorio**
   * - **iss**
     - String
     - Identificativo dell'entità che lo emette. 
     - |check-icon|
   * - **sub**
     - String
     - Identificativo del soggetto a cui è riferito. 
     - |check-icon|
   * - **iat**
     - UNIX Timestamp
     - Data di emissione. 
     - |check-icon|
   * - **exp**
     - UNIX Timestamp
     - Data di scadenza.
     - |check-icon|
   * - **jwks**
     - JWKS
     - Un JSON Web Key Set (JWKS) `[RFC7517]`_ che rappresenta la parte pubblica delle chiavi di firma dell'entità interessata. Ogni JWK nel set JWK DEVE avere un ID chiave (claim kid).
     - |check-icon|
   * - **trust_marks**
     - JSON array
     - Un array JSON contenente i Trust Mark. Vedere la Sezione :ref:`Trust Mark <Trust_Mark>`.
     - |check-icon| per tutti i partecipanti fatta esclusione del Trust Anchor. 



Gli EC delle entità di tipo Foglia contengono in aggiunta anche i seguenti attributi:

.. list-table::
   :widths: 20 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Tipo**
     - **Descrizione**
     - **Obbligatorio**
   * - **authority_hints**
     - Array di URLs
     - Contiene una lista di URL delle entità superiori, quali TA o SA che POSSONO emettere un ES relativo a questo soggetto. 
     - |check-icon|
   * - **metadata**
     - JSON Object
     - Ogni chiave dell'oggetto JSON rappresenta un identificatore del tipo di metadati e ogni
       valore DEVE essere un oggetto JSON che rappresenta i metadati secondo lo schema di metadati di quel tipo. 

       Una configurazione di entità PUÒ contenere più dichiarazioni di metadati, ma solo una per ogni tipo di metadati (<**entity_type**>). 

       I tipi consentiti sono i seguenti:

       - openid_relying_party
       - openid_provider
       - federation_entity
       - oauth_resource
       - trust_mark_issue
     - |check-icon|

Gli EC di entrambe le FA contengono anche i seguenti attributi:

.. list-table::
   :widths: 20 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Tipo**
     - **Descrizione**
     - **Obbligatorio**
   * - **constraints**
     - JSON Object
     - Oggetto JSON che descrive un insieme di vincoli della Trust Chain. OBBLIGATORIO in EC per TA. 
       Un vincolo può contenere i seguenti attributi:
          
         - **max_path_length**. OBBLIGATORIO. Numero intero. Il massimo numero di ES fra questo ES e l'ultimo ES nella trust chain.
         - **naming_constraints**. OPZIONALE. JSON Object. Restrizione sugli identificatori delle entità al di sotto di questa. Il comportamento di questo attributo riproduce ciò che è definito in `[RFC5280#Section.4.2.1.10]`_. Le restrizioni sono definite in termini di sottoalberi permessi o esclusi.

       Se un ES subordinato contiene una specifica di vincolo più restrittiva di quella effettiva, allora il vincolo più restrittivo è effettivo da qui in avanti. Se invece il vincolo è meno restrittiva, allora sarà ignorato.
     - |check-icon|
   * - **trust_marks_issuers**
     - JSON array
     - Indica quali autorità sono considerate attendibili nella federazione per l’emissione di specifici TM, questi assegnati mediante il proprio identificativo univoco.
     - |check-icon|



Gli ES emessi dal TA o da un suo Intermediario per i propri diretti discendenti, contengono anche i seguenti attributi:

.. list-table::
   :widths: 20 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Tipo**
     - **Descrizione**
     - **Obbligatorio**
   * - **metadata_policy**
     - JSON Object
     - Oggetto JSON che descrive un criterio di metadati. Ogni chiave dell'oggetto JSON rappresenta un identificatore del tipo di metadati e ogni valore DEVE essere un oggetto JSON che rappresenta la politica dei metadati in base allo schema di quel tipo di metadati. Si rimanda alla specifica `[OIDC-FED#Section.5.1]`_ per i dettagli implementativi.
     - |check-icon|
   * - **trust_marks**
     - JSON Array
     - Un array JSON contenente i Trust Mark emessi da se stesso per il soggetto discendente.
     - |check-icon|


.. seealso:: 

  `[OIDC-FED#Section_3.1]`_




.. _examples_of_entity_configurations:

Esempi di Entity Configuration
++++++++++++++++++++++++++++++

TODO



.. _examples_of_entity_statements:

Esempi di Entity Statement
++++++++++++++++++++++++++

TODO
