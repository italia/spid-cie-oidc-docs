Configurazione della Federazione
--------------------------------

Nella Federazione OIDC il **Trust Anchor** rappresenta l'implementazione della Autorità della Federazione.

La configurazione della Federazione è pubblicata dal Trust Anchor all'interno della sua :ref:`Entity Configuration<Esempio_EN1.4>`, presso un web path ben noto e corrispondente a **.well-known/openid-federation**.

Tutti i partecipanti DEVONO ottenere prima della fase di esercizio la configurazione della Federazione e mantenere questa aggiornata su base giornaliera. All’interno della Configurazione della Federazione è presente la chiave pubblica del Trust Anchor usata per le operazioni di firma, il numero massimo di Intermediari consentiti tra una Foglia e il Trust Anchor (**max_path length**) e le autorità abilitate all’emissione dei Trust Marks (**trust_marks_issuers**).


# TODO: link/riferimento a appendice con esempio non normativo di EC del trust anchor


Si veda la Sezione dedicata alle :ref:`Entity Configuration<Entity_Configuration>` per ulteriori dettagli.


Modalità di partecipazione
--------------------------

Per aderire alla Federazione SPID una entità di tipo Foglia deve pubblicare la propria configurazione (Entity Configuration) presso il web endpoint :ref:`.well-known/openid-federation<Esempio_EN1>`.

Gli incaricati tecnici ed amministrativi della Foglia completano la procedura amministrativa per la registrazione di una nuova entità o l’aggiornamento di una preesistente definita dalla Autorità di Federazione o da un suo Intermediario (SA).

L’Autorità di Federazione o suo Intermediario dopo aver effettuato tutti i controlli amministrativi e tecnici richiesti, registra le chiavi pubbliche della Foglia e rilascia una prova di adesione alla Federazione sotto forma di Trust Mark (TM).

La Foglia DEVE includere il TM all’interno della propria configurazione di Federazione (Entity Configuration) come prova del buon esito del processo di onboarding. 

L’Autorità di Federazione o suo Intermediario DEVE pubblicare la dichiarazione di riconoscimento della Foglia (Entity Statement) contenente le chiavi pubbliche di federazione della Foglia e i TM a questa rilasciati. L’Autorità di Federazione o suo Intermediario PUÒ pubblicare una politica dei `metadata <https://openid.net/specs/openid-connect-federation-1_0.html#rfc.section.5.1>`_ per forzare la modifica dei metadata OIDC della Foglia, nelle parti in cui questo fosse necessario.


.. _Entity_Configuration:

Entity Statement e Entity Configuration
---------------------------------------

Il componente basilare per costruire una catena di fiducia (trust chain) è l'*Entity Statement*, un JWT crittografico che contiene 
le chiavi di firma delle entità e ulteriori dati usati per controllare il processo di risoluzione della trust chain (come l'*authority_hints* che specifica chi è il superiore di un'entità). Quando uno statement è autofirmato da un'entità, viene chiamato *Entity Configuration.*

Un Entity Configuration è un metadata di federazione in formato Jose e firmato dal soggetto che lo emette e riguardante se stesso, all’interno del quale i valori dei claim **iss** e **sub** contengono il medesimo valore (URL).

Un Entity Statement è un documento di riconoscimento che una Autorità di Federazione o suo Intermediario emette per uno specifico soggetto, suo discendente, individuato all’interno del claim **sub**.


Firma
+++++

La firma dei JWT :rfc:`7515` avviene mediante l'algoritmo RSA SHA-256 (RS256), tutti i partecipanti DEVONO supportare questo algoritmo di firma all’interno della Federazione. Tutte le operazioni di firma relative agli Entity Statements, Entity Configuration e Trust Mark sono condotte con le chiavi pubbliche di Federazione (Distinguiamo le chiavi di Federazione da quelle di OIDC Core, questi ultimi risiedono nei metadata OIDC. Un Entity Statement o Configuration contiene sia le chiavi pubbliche di Federazione che i metadata OIDC).


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
      - RICHIESTO. Un JSON Web Key Set (JWKS) :rfc:`7517` che rappresenta la parte pubblica delle chiavi di firma dell'entità interessata. Ogni JWK nel set JWK DEVE avere un ID chiave (claim kid).
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
      - Un JSON Web Key Set (JWKS) :rfc:`7517` che rappresenta la parte pubblica delle chiavi di firma dell'entità soggetto. Le chiavi
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
          - **naming_constraints**. OPZIONALE. JSON Object. Restrizione sugli identificatori di entità delle entità al di sotto di questa entità. Il comportamento di questo attributo riproduce ciò che è definito in :rfc:`5280#4.2.1.10`. Le restrizioni sono definite in termini di sottoalberi permessi o esclusi.

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

  [OIDC-FED#Section_3.1]_


CIE: Metadati
+++++++++++++

Riguardo a *metadata*, OIDC-FED usa valori di metadati da OpenID Connect Discovery 1.0 e OpenID Connect Dynamic Client Registration 1.0 `[OpenID.Discovery]`_, `[OpenID.Registration]`_ e aggiunge valori aggiuntivi usati per le federazioni descritte nelle seguenti sottosezioni per i ruoli differenti.


CIE: Metadato OP per la Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'identificatore del tipo di metadato è *openid_provider*. La tabella qui sotto presenta i valori del metadato OP definiti in `[OIDC-FED]`_, contestualizzati nella CIE Federation.


.. list-table::
    :widths: 40 20 40
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
    * - **client_registration_types_supported**
      - Array of string
      - OBBLIGATORIO. Array che specifica i tipi di federazione supportati. Nella CIE Federation è supportato solo il valore *automatic*
    * - **organization_name**
      - String
      - OPZIONALE. Un nome umanamente leggibile che rappresenta l'organizzazione proprietaria dell'OP. È inteso che va usato
        nell'interfaccia utente per essere riconosciuto dagli utenti finali che userebbero l'OP per autenticarsi.
    * - **request_authentication_methods_supported**
      - JSON Object
      - OPZIONALE. Un oggetto JSON con membri che rappresentano processi e come valori liste di metodi di request authentication
        supportati dall'authorization endpoint. L'unico metodo supportato nella CIE Federation è *request_object* per il processo Authorization Request (*ar*).
    * - **signed_jwks_uri**
      - URI
      - OPZIONALE. Un URI che punta a un JWT firmato che come payload il JWK Set dell'entità (vedere esempio sotto). Il JWT è firmato
        con una chiave inclusa nel JWK che l'entità ha pubblicato nel suo Entity Statement autofirmato.




CIE: Metadato RP per la Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'identificatore del tipo di metadato è *openid_provider*. La tabella qui sotto presenta i valori del metadato RP definiti in `[OIDC-FED]`_, contestualizzati nella CIE Federation.


.. list-table::
    :widths: 40 20 40
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
    * - **client_registration_types**
      - Array of string
      - OBBLIGATORIO. Array di stringhe che specifica i tipi di registrazione client che RP vuole usare. Nella CIE Federation è supportato solo il valore *automatic*
    * - **organization_name**
      - String
      - OPZIONALE. Un nome umanamente leggibile che rappresenta l'organizzazione proprietaria dell'RP. 



CIE: Metadato FA per la Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'identificatore del tipo di metadato è *federation_entity*. La tabella qui sotto presenta i valori del metadato FA definiti in `[OIDC-FED]`_, contestualizzati nella CIE Federation.


.. list-table::
    :widths: 40 20 40
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
    * - **federation_fetch_endpoint**
      - URL
      - OPZIONALE. Il Fetch Endpoint descritto nella Sezione XX. Entità intermedie e TA DEVONO pubblicare un *federation_fetch_endpoint*. Entità Foglia NON DEVONO.



CIE: Altri metadati per la Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nel contesto OAuth context, `[OIDC-FED]`_ supporta:

 - OAuth AS con identificatore del tipo di metadato *oauth_authorization_server*. Tutti i parametri definiti in :rfc:`8414#section-2` sono applicabili.
 - OAuth Client con identificatore del tipo di metadato *oauth_client*. Tutti i parametri definiti in :rfc:`7591#section-2` sono applicabili.
 - OAuth Protected Resource con identificatore del tipo di metadato *oauth_resource*. Non c'è uno standard che specifichi quali
   parametri possono occorrere nel metadato per questo tipo di entità. Quindi per il momento questo può essere visto come un placeholder.
 - Emittente di Trust Mark con identificatore del tipo di metadato *trust_mark_issuer*. Tutte le entità che partecipano in una
   federazione possono essere di questo tipo. Le seguenti proprietà sono permesse:

    - *status_endpoint*. OPZIONALE. L'endpoint per l'operazione di status è descritto nella Sezione XX. 

   **Esempio**

    .. code-block:: 

       "trust_mark_issuer": {
           "status_endpoint": "https://trust_marks_are_us.example.com/status"
       }




Endpoint per Trust Anchor ed Intermediari
-----------------------------------------
Il Trust Anchor e i suoi Intermediari (federation_entity) DEVONO in aggiunta esporre al pubblico i seguenti endpoint:


Fetch entity statement endpoint
+++++++++++++++++++++++++++++++

Il recupero degli Entity Statement viene effettuato presso questo endpoint secondo le modalità definite all’interno di OIDC-FED “7.1. Fetching Entity Statements”.


.. _Trust_mark_status_endpoint:

Trust mark status endpoint
++++++++++++++++++++++++++

L’assegnazione di un Trust Mark ad un soggetto viene effettuato presso questo endpoint secondo le modalità definite all’interno di OIDC-FED “7.4. Trust Mark Status”.


.. _Entity_Listing_endpoint:

Entity Listing endpoint
+++++++++++++++++++++++

Per ottenere la lista dei discendenti registrati presso la TA o un suo Intermediario è possibile interrogare questo endpoint secondo le modalità descritte in OIDC-FED “7.3. Entity Listings”. Ai parametri esistenti già definiti nella specifica, si aggiunge per SPID il parametro entity_type come filtro sul tipo di entità dei discendenti (<entity-type>).



Differenze con OIDC Federation 1.0
----------------------------------

In questa sezione sono elencate le differenze che intercorrono tra lo standard ufficiale e l’implementazione SPID.


Client Registration
+++++++++++++++++++

SPID supporta esclusivamente **automatic_client_registration**. La modalità **implicit** è da intendersi come non supportata. 


Listing endpoint
++++++++++++++++

In SPID viene adottato il parametro aggiuntivo **entity_type** a quelli esistenti nello Standard [OIDC-FED] per questo endpoint, con lo scopo di ottenere un filtro sulla tipologia delle entità discendenti. Questa esigenza consente nello specifico di filtrare entità di tipo **federation_entity**, **openid_relying_party**, **openid_provider** e **oauth_resource**.


Trust Mark
++++++++++

In OIDC-FED l’uso dei Trust Mark non è obbligatorio. In SPID piuttosto l’esposizione dei Trust Mark è obbligatoria. Per approfondimenti sulla ragione dell’obbligo dei Trust Mark si rimanda alla sezione :ref:`Considerazioni di Sicurezza<Considerazioni_di_Sicurezza>`.


Claim non supportati negli Entity Statement
+++++++++++++++++++++++++++++++++++++++++++

Poiché SPID non necessita di alcun claim aggiuntivo in ambito federativo, non necessita dei claim crit. Inoltre non sono supportati i claim **aud**, **naming_constraints**, **policy_language_crit** e **trust_anchor_id**. L’eventuale presenza di questi claim non presenta alcuna implicazione, questi verranno semplicemente ignorati fino ad ulteriori avvisi che li normino.



.. _Considerazioni_di_Sicurezza:

Considerazioni di Sicurezza
---------------------------

In questa sezione descriviamo alcune considerazioni di sicurezza in ambito OIDC Federation.


Trust Mark come deterrente contro gli abusi
+++++++++++++++++++++++++++++++++++++++++++

L’implementazione dei Trust Mark e il filtro su questi in fase di Metadata Discovery risulta necessario contro gli attacchi destinati al consumo delle risorse. Un OP attaccato con un numero ingente di connessioni presso il suo endpoint di *authorization*, contenenti **client_id** e **authority_hints** fasulli, produrrebbe svariate connessioni verso sistemi di terze parti nel tentativo di trovare un percorso verso la TA e instaurare la fiducia con il richiedente.

L’OP DEVE validare staticamente il TM oppure DEVE escludere a priori la richiesta ove il TM non risultasse presente, in caso di assenza o non validità di un TM la procedura di Metadata Discovery NON DEVE essere avviata e NON DEVE creare di conseguenza connessioni verso sistemi di terze parti.


Numero Massimo di authority_hints
+++++++++++++++++++++++++++++++++

All’interno di una Federazione il Trust Anchor decide quante intermediazioni consentire tra di lui e le Foglie, mediante la constraint denominata **max_path_lenght**. Questo tipo di relazione è di tipo verticale, dalla foglia alla radice. Questo attributo se valorizzato ad esempio con un valore numerico intero pari a 1 indica che soltanto un SA è consentito tra una Foglia e il TA.

Ogni Foglia DEVE pubblicare i suoi superiori all’interno della lista contenuta nel claim **authority_hints**. Una Foglia all’interno della Federazione PUÒ avere superiori afferenti a diverse Federazioni, si pensi a CIE id per esempio. L’analisi dei superiori disponibili introduce un modello di navigazione orizzontale, ad esempio un OP tenta di trovare il percorso più breve verso il Trust Anchor attraverso tutti gli URL contenuti all’interno dell’array **authority_hints** prima di fare un ulteriore movimento verticale, a salire, verso uno degli Intermediari presenti in questo array.

La soglia **max_path_lenght** si applica per la navigazione verticale e superata questa soglia senza aver trovato il TA la procedura di Metadata Discovery DEVE essere interrotta. Si faccia l’esempio di un RP discendente di un 1 SA che quest’ultimo a sua volta è discendente di  un altro SA, essendo il valore di **max_path_lenght** pari a uno e superata questa soglia senza aver trovato il Trust Anchor, la procedura DEVE essere interrotta.

Allo stesso tempo la specifica OIDC Federation 1.0 non definisce un limite per il numero di **authority_hints**, questo perché nessun Trust Anchor può limitare il numero di Federazioni alle quali un partecipante può aderire. Per questa ragione è utile che gli implementatori adottino un limite massimo del numero di elementi consentiti all’interno dell’Array authority_hint. Questo per evitare che un numero esagerato di URL contenuti nella lista di **authority_hints**, dovuto ad una cattiva configurazione di una Foglia, produca un consumo di risorse eccessivo.


Resolve Entity Statement
++++++++++++++++++++++++

Questo endpoint DEVE rilasciare i metadata, i Trust Marks e la Trust Chain già precedentemente elaborata e NON DEVE innescare una procedura di Metadata Discovery ad ogni richiesta pervenuta, a meno che questo endpoint non venga protetto con un meccanismo di autenticazione dei client, come ad esempio private_key_jwt `[SPID-OIDC-CORE]`_.




Buone Pratiche
--------------

In questa sezione descriviamo alcune buone pratiche per ottenere la massima resa dalle entità di Federazione.


Specializzare le chiavi pubbliche OpenID Core e Federation
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

È buona pratica usare chiavi pubbliche specializzate per i due tipi di operazioni, Core e Federation.

Modalità di aggiornamento dei metadata OpenID Core
++++++++++++++++++++++++++++++++++++++++++++++++++

L’interoperabilità tra i partecipanti funziona mediante i metadata ottenuti dal calcolo e dalla conservazione delle Trust Chain. Questo significa che se un OP al tempo T calcola la Trust Chain per un RP e questo al tempo T+n modifica i propri metadata, l’OP di conseguenza potrebbe incorrere in problematiche di validazione delle richieste di autorizzazione del RP, fino a quando non avrà aggiornato la Trust Chain relativa a questo.

La buona pratica per evitare le interruzioni di servizio relative alle operazioni di OIDC Core è quella di aggiungere le nuove chiavi pubbliche all’interno degli oggetti *jwks* senza rimuovere i valori preesistenti. Oppure, ad esempio, i nuovi *redirect_uri*.

In questa maniera dopo il limite massimo di durata delle Trust Chain, definito con il claim **exp** e pubblicato nella Entity Configuration della TA, si ha la certezza che tutti i partecipanti abbiano rinnovato le loro Trust Chain, e sarà possibile agli amministratori della Foglia rimuovere le vecchie definizioni in cima alla lista.

Periodo di grazia per le Trust Chain scadute
++++++++++++++++++++++++++++++++++++++++++++

In una Federazione distribuita come quella di OIDC-FED è possibile che al tempo T+x un OP necessiti di aggiornare alcune Trust Chain, relative a diversi RP, prossime alla scadenza. Si faccia l’esempio che parte di questi RP risultino aggregati da una SA e i servizi di questo risultino temporaneamente non raggiungibili.

In questi casi, ove vi fosse l’impossibilità di aggiornare una Trust Chain a causa di irraggiungibilità dei servizi web di federazione, è possibile continuare ad utilizzare le Trust Chain scadute fino ad un massimo di 24 ore successive al primo tentativo di aggiornamento. All’interno di questo intervallo temporale “di grazia” sono comunque necessari periodici tentativi di aggiornamento.
