Come iniziare
=============


Introduzione e scopo di questa documentazione
---------------------------------------------

Questo documento definisce le regole di funzionamento della Federazione OpenID Connect SPID per Fornitori di Servizio pubblici e privati (RP), Identity Providers (OP) e Soggetti Aggregatori (SA). Definisce inoltre gli schemi dei metadati di RP, OP e SA in contesto Federativo, le modalità di registrazione dei RP presso gli OP, le risorse e gli endpoint a supporto della Federazione.


Che cosa sono le identità digitali
----------------------------------

Grazie all’`identità digitale <https://identitadigitale.gov.it/>`_, la Pubblica Amministrazione fornisce la chiave per accedere ai servizi online attraverso una credenziale unica, che si attiva una sola volta ed è sempre valida.

Semplice, veloce e sicuro, l’accesso ai servizi pubblici online è possibile con il `Sistema Pubblico di Identità Digitale (SPID) <https://www.spid.gov.it/>`_ e la `Carta d’Identità Elettronica (CIE) <https://www.cartaidentita.interno.gov.it/>`_. SPID e CIE sono gli strumenti di identificazione per accedere ai servizi online della PA e ai servizi dei privati aderenti.

Tutte le pubbliche amministrazioni devono integrare nei propri sistemi informativi SPID e CIE, come unici sistemi di identità digitale per l'accesso ai servizi digitali, abbandonando le vecchie credenziali. Grazie a SPID e CIE diventa uniforme l’accesso ai servizi pubblici in tutto il territorio nazionale.

Secondo l’`articolo 65 <https://docs.italia.it/italia/piano-triennale-ict/codice-amministrazione-digitale-docs/it/v2021-07-30/_rst/capo_V-sezione_III-articolo_65.html>`_ del Codice dell’Amministrazione digitale, i cittadini possono presentare per via telematica istanze e dichiarazioni alla Pubblica Amministrazione esclusivamente identificandosi attraverso SPID, CIE o CNS. In questo caso le istanze e dichiarazioni sono equivalenti alle istanze e alle dichiarazioni sottoscritte con firma autografa apposta in presenza del dipendente addetto al procedimento.


Acronimi IAM e AAI
------------------

In questa sezione sono definiti tutti gli acronimi utilizzati all’interno del testo.

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - AdF
      - Autorità di Federazione, che è AgID
    * - OIDC
      - OpenID Connect
    * - OIDC-FED
      - OIDC Federation 1.0
    * - IOF
      - Italian OIDC Federation 1.0
    * - SPID
      - Sistema Pubblico di Identità Digitale
    * - AgID
      - Agenzia per l’Italia Digitale
    * - SA
      - Soggetti Aggregatori
    * - TA
      - OIDC Federation Trust Anchor
    * - OP
      - OpenID Provider
    * - RP
      - Relying Party	
    * - AA
      - Attribute Authority, OAuth Resource Server, Gestore degli Attributi qualificati
    * - TM
      - Trust Mark
    * - EC
      - Entity Configuration
    * - ES
      - Entity Statement
    * - URL
      - Uniform Resource Locator, corrispondente ad un indirizzo web
    * - JWT
      - Vedi [RFC7519]	


Termini utilizzati
------------------

Seguono i termini utilizzati da [OIDC-FED#Section_1.2] e in questo documento

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - Entity configuration
      - Dichiarazione di una entità emessa per proprio conto, nella forma di JWT auto firmato [RFC7515] e contenente la configurazione di se stessa. Contiene le chiavi pubbliche di Federazione, il metadata OIDC, gli URL delle autorità sue superiori e i Trust Mark emessi da autorità riconoscibili nella Federazione che attestano l’aderenza del soggetto a determinati profili.
    * - Entity statement
      - Dichiarazione di riconoscimento emessa da un'entità superiore (Trust Anchor o Intermediario) riguardante un'entità discendente (RP, OP o Intermediario) in formato JWT firmato [RFC7515], contenente la chiave pubblica del soggetto discendente, i Trust Mark emessi per i quali è emittente e la politica dei metadati da applicare ai metadati del soggetto.
    * - Trust Mark
      - JWT firmato [RFC7515] dall'ente emittente e relativo ad un partecipante. Attesta la conformità di questo ai profili riconoscibili all’interno Federazione (RP pubblico o privato, Soggetto Aggregatore Pubblico o Privato, etc.). La Foglia che acquisisce il marchio di fiducia durante la fase di onboarding DEVE includere questo nella sua Entity Configuration a mò di Badge di riconoscimento.
    * - Metadata
      - Un documento di metadati descrive una implementazione di una entità OpenID Connect. Le implementazioni di ogni Entità condividono i metadati per stabilire una base di fiducia e interoperabilità.
    * - Metadata policy
      - Il Trust Anchor pubblica le regole e le politiche da applicare sui metadata dei discendenti, specificando quali valori o sottoinsiemi di valori sono consentiti per un dato parametro di metadati.
    * - Authority hint
      - Un Array di valori url corrispondenti agli identificativi delle entità superiori, Trust Anchor o Intermediario, che DEVONO emettere un Entity Statement per i propri discendenti.
    * - Metadata Discovery
      - Raccolta di Entity Configuration e Statement. Inizia da un'entità Foglia fino al raggiungimento del Trust Anchor.
    * - Trust Chain
      - Procedura di validazione della sequenza di Entity Configuration e Statement raccolta mediante Metadata Discovery, il cui esito positivo è un metadata finale relativo ad una entità e la data di scadenza entro la quale questo deve essere aggiornato.
    * - onboarding
      - Procedura di registrazione di una nuova entità all’interno della Federazione SPID



Standard di riferimento
-----------------------

testo


Come diventare fornitore di servizi (link a onboarding SPID e CIE)
------------------------------------------------------------------

testo


Come usare questa documentazione
--------------------------------

testo