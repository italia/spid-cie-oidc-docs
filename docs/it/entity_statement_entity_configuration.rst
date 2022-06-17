.. include:: ./common_definitions.rst


.. _Entity_Configuration:

Entity Statement e Entity Configuration
---------------------------------------

Il componente basilare per costruire una catena di fiducia (trust chain) è l'*Entity Statement*, un JWT crittografico che contiene 
le chiavi di firma delle entità e ulteriori dati usati per controllare il processo di risoluzione della trust chain (come l'*authority_hints* che specifica chi è il superiore di un'entità). Quando uno statement è autofirmato da un'entità, viene chiamato *Entity Configuration.*

Un Entity Configuration è un metadata di federazione in formato Jose e firmato dal soggetto che lo emette e riguardante se stesso, all’interno del quale i valori dei claim **iss** e **sub** contengono il medesimo valore (URL).

Un Entity Statement è un documento di riconoscimento che una Autorità di Federazione o suo Intermediario emette per uno specifico soggetto, suo discendente, individuato all’interno del claim **sub**.


Firma
+++++

La firma dei JWT `[RFC7515]`_ avviene mediante l'algoritmo RSA SHA-256 (RS256), tutti i partecipanti DEVONO supportare questo algoritmo di firma all’interno della Federazione. Tutte le operazioni di firma relative agli Entity Statements, Entity Configuration e Trust Mark sono condotte con le chiavi pubbliche di Federazione (Distinguiamo le chiavi di Federazione da quelle di OIDC Core, questi ultimi risiedono nei metadata OIDC. Un Entity Statement o Configuration contiene sia le chiavi pubbliche di Federazione che i metadata OIDC).


SPID: Attributi (claim)
+++++++++++++++++++++++

Entity Configuration e Statement presentano i seguenti attributi (claim) comuni:

.. list-table::
    :widths: 20 20 60
    :header-rows: 1

    * - **Nome**
      - **Tipo**
      - **Descrizione**
    * - **iss**
      - String
      - RICHIESTO. Identificativo dell'entità che lo emette. 
    * - **sub**
      - String
      - RICHIESTO. Identificativo del soggetto a cui è riferito. 
    * - **iat**
      - UTC Timestamp
      - RICHIESTO. Data di emissione. 
    * - **exp**
      - UTC Timestamp
      - RICHIESTO. Data di scadenza.
    * - **jwks**
      - JWKS
      - RICHIESTO. Un JSON Web Key Set (JWKS) `[RFC7517]`_ che rappresenta la parte pubblica delle chiavi di firma dell'entità interessata. Ogni JWK nel set JWK DEVE avere un ID chiave (claim kid).
    * - **trust_marks**
      - JSON array
      - RICHIESTO per tutti i partecipanti fatta esclusione del Trust Anchor. Un array JSON contenente i Trust Mark. Vedere la Sezione :ref:`Trust Mark <Trust_Mark>`.



Gli oggetti Entity Configuration delle Entità di tipo Foglia contengono in aggiunta ai claim comuni anche i seguenti:

.. list-table::
    :widths: 10 10 80
    :header-rows: 1

    * - **Nome**
      - **Tipo**
      - **Descrizione**
    * - **authority_hints**
      - Array di URLs
      - RICHIESTO. Contiene una lista di URL delle entità superiori, quali TA o SA che POSSONO emettere un Entity Statement relativo a questo soggetto. 
    * - **metadata**
      - JSON object
      - RICHIESTO. Ogni chiave dell'oggetto JSON rappresenta un identificatore del tipo di metadati e ogni valore DEVE essere un oggetto JSON che rappresenta i metadati secondo lo schema di metadati di quel tipo. 

        Una configurazione di entità PUÒ contenere più dichiarazioni di metadati, ma solo una per ogni tipo di metadati (<**entity_type**>). 

        I tipi consentiti sono i seguenti:

        - openid_relying_party
        - openid_provider
        - federation_entity
        - oauth_resource
        - trust_mark_issue
 

Gli oggetti Entity Configuration della Federation Authority che è AgID, contiene in aggiunta ai claim comuni anche i seguenti:

.. list-table::
    :widths: 20 10 70
    :header-rows: 1

    * - **Nome**
      - **Tipo**
      - **Descrizione**
    * - **constraints**
      - JSON object
      - RICHIESTO e include l’elemento max_path_length al quale viene assegnato un valore Integer. 
        
        Indica il numero massimo di intermediari consentiti tra una Foglia e il suo Trust Anchor.
    * - **trust_marks_issuers**
      - JSON array
      - RICHIESTO. Indica quali autorità sono considerate attendibili nella federazione per l’emissione di specifici Trust Mark, questi assegnati mediante il proprio identificativo univoco.


Gli Entity Statement emessi dal Trust Ancor o suo Intermediario per i propri diretti discendenti, contengono in aggiunta ai claim comuni anche i seguenti:

.. list-table::
    :widths: 20 10 70
    :header-rows: 1

    * - **Nome**
      - **Tipo**
      - **Descrizione**
    * - **metadata_policy**
      - JSON object
      - OPZIONALE. Oggetto JSON che descrive un criterio di metadati. Ogni chiave dell'oggetto JSON rappresenta un identificatore del tipo di metadati e ogni valore DEVE essere un oggetto JSON che rappresenta la politica dei metadati in base allo schema di quel tipo di metadati. Si rimanda alla specifica `[OIDC-FED#Section.5.1]`_ per i dettagli implementativi.
    * - **trust_marks**
      - JSON array
      - RICHIESTO. Un array JSON contenente i Trust Mark emessi da se stesso per il soggetto discendente.


CIE: Attributi (claim)
++++++++++++++++++++++

La tabella sottostante riporta gli attributi considerati da OIDC-FED e contestualizzati nella CIE Federation. Nella colonna “Obbligatorio/Opzionale”, specifichiamo se l'attributo deve essere presente in un *Entity Statement* (ES), *Entity Configuration* (EC) o entrambi (ES/EC) e per quali tipi di entità (L=foglia/leaf, I=intermediate, TA o tutte).


.. note::
   Quando un Entity Statement è relativo ad una subordinata, le entità foglia espongono solo Entity Configuration (attraverso l'endpointil /.well-known/openid-federation).


.. list-table::
    :widths: 20 20 40 20
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
      - **Obbligatorio/Opzionale**
    * - **iss**
      - String
      - L'identificatore di entità dell'emittente dello statement
      - OBBLIGATORIO in ES/EC per tutte le entità. 
    * - **sub**
      - String
      - L'identificatore di entità del soggetto. Se l'*iss* e il *sub* sono identici, l'emittente sta facendo uno statement relativo a se stessa e questo Entity Statement è un Entity Configuration
      - OBBLIGATORIO in ES/EC per tutte le entità. 
    * - **iat**
      - UTC Timestamp
      - Data/ora nella quale lo statement è stato emesso
      - OBBLIGATORIO in ES/EC per tutte le entità. 
    * - **exp**
      - UTC Timestamp
      - Data/ora di scandenza o dopo la quale lo statement NON DEVE PIÙ essere accettato per l'elaborazione
      - OBBLIGATORIO in ES/EC per tutte le entità. 
    * - **jwks**
      - JWKS
      - Un JSON Web Key Set (JWKS) `[RFC7517]`_ che rappresenta la parte pubblica delle chiavi di firma dell'entità soggetto. Le chiavi
        di questo set sono per firmare statement e NON DEVONO essere usate in altri protocolli (chiavi da usare in altri protocolli, p.es. OpenID Connect, vengono passate nell'elemento metadata del rispettivo ES). Ogni JWK nell'insieme JWKS DEVE avere un Key ID (*kid*)
      - OBBLIGATORIO in ES/EC per tutte le entità. 
    * - **aud**
      - String
      - L'ES  PUÒ essere specificatamente creato per un'entità. L'identificatore di entità per quell'entità DEVE apparire in questo claim.
      - OPZIONALE in ES/EC per tutte le entità. 
    * - **authority_hints**
      - Array di stringhe
      - Rappresenta gli identificatori di entità delle entità intermedie o delle TA che POSSONO emettere un ES riguardo l'entità
        emittente.
      - OBBLIGATORIO (NON DEVE essere una lista vuota []) in EC per tutte le entità eccetto per le TA che non hanno alcun superiore.
    * - **metadata**
      - JSON Object
      - Oggetto JSON che include attributi di metadata specifici di protocollo che rappresentano i metadati dell'entità. Ogni chiave
        dell'oggetto JSON rappresenta un identificatore del tipo di metadato, ed ogni valore DEVE essere un Oggetto JSON che rappresenta il metadato in acvcordo allo schema di metadati del tipo di metadato. Un EC PUÒ contenere statement multipli diu metadato, ma uno solo per ciascun tipo di metadato.
      - OPZIONALE in ES per Is e TA (le entità L NON DEVONO contenere un claim *metadata_policy*)
    * - **constraints**
      - JSON Object
      - Oggetto JSON che descrive un insieme di vincoli della Trust Chain. Un vincolo può contenere i seguenti attributi:
          
          - **max_path_length**. OBBLIGATORIO. Numero intero. Il massimo numero di ES fra questo ES e l'ultimo ES nella trust chain.
            Nella CIE FED questo attributo è XX
          - **naming_constraints**. OPZIONALE. JSON Object. Restrizione sugli identificatori di entità delle entità al di sotto di questa entità. Il comportamento di questo attributo riproduce ciò che è definito in `[RFC5280#Section.4.2.1.10]`_. Le restrizioni sono definite in termini di sottoalberi permessi o esclusi.

        Se un ES subordinato contiene una specifica di vincolo più restrittiva di quella effettiva, allora il vincolo più
        restrittivo è effettivo da qui in avanti. Se un ES subordinato contiene una specifica di vincolo meno restrittiva di quella
        in effetto, allora DEVE essere ignorata.

      - OBBLIGATORIO in EC per TA
    * - **trust_marks**
      - JSON Array
      - Un array JSON di Web Token JSON firmati, ciascuno che rappresenta un marchio di certificazione. Vedere sezione XX.
      - OBBLIGATORIO in EC per entità L e I. OPZIONALE in ES per entità L e I.
    * - **trust_marks_issuers**
      - JSON Array
      - TA PUÒ usare questo attributo per dire quali identificatori di Trust Mark e i loro emettitori sono fidati nella Federazione.
        Questo attributo DEVE essere ignorato se presente in un ES di altre entità rispetto alla TA. È un array JSON con chiavi che rappresentano identificatori Trust Mark e valori che sono un array di entità fidate che rappresentano l'autorità di accreditazione. Un valore speciale * permette TRust Mark auto firmati.
      - OPZIONALE in EC per TA.


.. seealso:: 

  `[OIDC-FED#Section_3.1]`_
