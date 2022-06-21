.. include:: ./common_definitions.rst


Configurazione della Federazione
--------------------------------

Nella Federazione OIDC il **Trust Anchor** è il servizio gestito dalla Autorità della Federazione.

La configurazione della Federazione è pubblicata dal Trust Anchor all’interno della sua :ref:`Entity Configuration<Esempio_EN1.4>`, disponibile presso un web path ben noto e corrispondente a **.well-known/openid-federation**.

Tutti i partecipanti DEVONO ottenere prima della fase di esercizio la configurazione della Federazione e mantenere questa aggiornata su base giornaliera. All’interno della Configurazione della Federazione è presente la chiave pubblica del Trust Anchor usata per le operazioni di firma, il numero massimo di Intermediari consentiti tra una Foglia e il Trust Anchor (**max_path length**) e le autorità abilitate all’emissione dei Trust Marks (**trust_marks_issuers**).


Si veda qui un esempio non normativo di :ref:`Entity Configuration response Trust Anchor<Esempio_EN1.4>`


Si veda la Sezione dedicata alle :ref:`Entity Configuration<Entity_Configuration>` per ulteriori dettagli.


Modalità di partecipazione
--------------------------

Per aderire alla Federazione SPID una entità di tipo Foglia deve pubblicare la propria configurazione (Entity Configuration) presso il proprio web endpoint :ref:`.well-known/openid-federation<Esempio_EN1>`.

Gli incaricati tecnici ed amministrativi della Foglia completano la procedura amministrativa per la registrazione di una nuova entità o l’aggiornamento di un’entità preesistente definita dalla Autorità di Federazione o da un suo Intermediario (SA).

L’Autorità di Federazione o il suo Intermediario, dopo aver effettuato tutti i controlli amministrativi e tecnici richiesti, registra le chiavi pubbliche della Foglia e rilascia una prova di adesione alla Federazione sotto forma di Trust Mark (TM).

La Foglia DEVE includere il TM all’interno della propria configurazione di Federazione (Entity Configuration) come prova del buon esito del processo di onboarding. 

L’Autorità di Federazione o suo Intermediario DEVE pubblicare la dichiarazione di riconoscimento della Foglia (Entity Statement) contenente le chiavi pubbliche di federazione della Foglia e i TM a questa rilasciati. L’Autorità di Federazione o suo Intermediario PUÒ pubblicare una politica dei `metadata <https://openid.net/specs/openid-connect-federation-1_0.html#rfc.section.5.1>`_ per forzare la modifica dei metadata OIDC della Foglia, nelle parti in cui questo fosse necessario.


.. _Entity_Configuration:

Entity Statement e Configuration
---------------------------------------

Il componente basilare per costruire una catena di fiducia (trust chain) è l'*Entity Statement*, un JWT crittografico che contiene 
le chiavi di firma delle entità e ulteriori dati usati per controllare il processo di risoluzione della trust chain (come l'*authority_hints* che specifica chi è il superiore di un'entità). Quando uno statement è autofirmato da un'entità, viene chiamato *Entity Configuration.*

Un Entity Configuration è un metadata di federazione in formato Jose e firmato dal soggetto che lo emette e riguardante se stesso, all’interno del quale i valori dei claim **iss** e **sub** contengono il medesimo valore (URL).

Un Entity Statement è un documento di riconoscimento che una Autorità di Federazione o suo Intermediario emette per uno specifico soggetto, suo discendente, individuato all’interno del claim **sub**.


Firma
+++++

La firma dei JWT :rfc:`7515` avviene mediante l'algoritmo RSA SHA-256 (RS256), tutti i partecipanti DEVONO supportare questo algoritmo di firma all’interno della Federazione. Tutte le operazioni di firma relative agli Entity Statements, Entity Configuration e Trust Mark sono condotte con le chiavi pubbliche di Federazione (Distinguiamo le chiavi di Federazione da quelle di OIDC Core, questi ultimi risiedono nei metadata OIDC. Un Entity Statement o Configuration contiene sia le chiavi pubbliche di Federazione che i metadata OIDC).


Attributi (claim)
+++++++++++++++++

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
      - Unix Timestamp
      - RICHIESTO. Data di emissione. 
    * - **exp**
      - Unix Timestamp
      - RICHIESTO. Data di scadenza.
    * - **jwks**
      - JWKS
      - RICHIESTO. Un JSON Web Key Set (JWKS) :rfc:`7517` che rappresenta la parte pubblica delle chiavi di firma. Ogni JWK nel set JWK DEVE avere un ID chiave (claim kid).
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


Metadati OpenID
+++++++++++++++

OIDC-FED usa valori di metadati da OpenID Connect Discovery 1.0 e OpenID Connect Dynamic Client Registration 1.0 `[OpenID.Discovery]`_, `[OpenID.Registration]`_ e aggiunge valori aggiuntivi usati per le federazioni descritte nelle seguenti sottosezioni per i ruoli differenti.


Metadata OP per la Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'identificatore del tipo di metadato è *openid_provider*. La tabella qui sotto presenta i valori del metadato OP definiti in `[OIDC-FED]`_.


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




Metadata RP per la Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'identificatore del tipo di metadato è *openid_relying_party*. La tabella qui sotto presenta i valori del metadato RP definiti in `[OIDC-FED]`_.


.. list-table::
    :widths: 40 20 40
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
    * - **client_registration_types**
      - Array of string
      - OBBLIGATORIO. Array di stringhe che specifica i tipi di registrazione client che un RP vuole usare. In SPID e CIE Federation è supportato solo il valore *automatic*
    * - **organization_name**
      - String
      - OPZIONALE. Il nome dell'organizzazione dell'RP. 



Metadata di Soggetto Aggregatore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'identificatore del tipo di metadato è *federation_entity*. La tabella qui sotto presenta i valori del metadato FA definiti in `[OIDC-FED]`_.


.. list-table::
    :widths: 40 20 40
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
    * - **federation_fetch_endpoint**
      - URL
      - OPZIONALE. Il Fetch Endpoint descritto nella Sezione XX. Entità intermedie e TA DEVONO pubblicare un *federation_fetch_endpoint*. Entità Foglia NON DEVONO.



Altri Metadata
^^^^^^^^^^^^^^

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


Claim non supportati negli Entity Statement
+++++++++++++++++++++++++++++++++++++++++++

Poiché SPID non necessita di alcun claim aggiuntivo in ambito federativo, non necessita dei claim crit. Inoltre non sono supportati i claim **aud**, **naming_constraints**, **policy_language_crit** e **trust_anchor_id**. L’eventuale presenza di questi claim non presenta alcuna implicazione, questi verranno semplicemente ignorati fino ad ulteriori avvisi che li normino.

