.. include:: ./common_definitions.rst

Acronimi 
--------

In questa sezione sono definiti tutti gli acronimi utilizzati all’interno del testo.

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - **AdF**
      - Autorità di Federazione, che è AgID.
    * - **OIDC**
      - OpenID Connect
    * - **OIDC-FED**
      - OIDC Federation 1.0
    * - **IOF**
      - Italian OIDC Federation 1.0.
    * - **SPID**
      - Sistema Pubblico di Identità Digitale
    * - **AgID**
      - Agenzia per l’Italia Digitale
    * - **SA**
      - Soggetti Aggregatori. Sono entità intermediarie che possono gestire tutti gli aspetti della federazione di uno o più 
        RP (entità foglia).
    * - **TA**
      - OIDC Federation Trust Anchor
    * - **OP**
      - OpenID Provider
    * - **RP**
      - Relying Party   
    * - **AA**
      - Attribute Authority, OAuth Resource Server, Gestore degli Attributi qualificati
    * - **TM**
      - Trust Mark
    * - **EC**
      - Entity Configuration
    * - **ES**
      - Entity Statement
    * - **URL**
      - Uniform Resource Locator, corrispondente ad un indirizzo web
    * - **JWT**
      - Vedi `[RFC7519]`_ Jones, M., Bradley, J. and N. Sakimura, "JSON Web Token (JWT)", RFC 7519, DOI 10.17487/RFC7519, May 2015. 
    * - **FA**
      - Autorità di Federazione (Federation Authority). Un'entità legale che gestisce uno schema di identità nazionale basato su 
        un protocollo di federazione.
    * - **OIDC-FED**
      - `OIDC Federation <1.0 https://openid.net/specs/openid-connect-federation-1_0.html>`_.
    * - **IOF**
      - Italian OIDC Federation 1.0.
    * - **CIE id**
      - Il sistema di identità digitale italiano basato sulla Carta d'Identità Elettronica (CIE), il cui proprietario è il Ministero 
        dell'Interno d'Italia ed è gestito dall'Istituto Poligrafico e Zecca dello Stato (IPZS).
    * - **MinInterno**
      - Ministero dell'Interno d'Italia, Federation Authority del sistema CIE id.
    * - **RS**
      - OAuth Resource Server
    * - **$JWT**
      - Il valore di un JWT (JSON Web Token).



Convenzioni e Terminologia
--------------------------

Le parole chiave “DEVE” e “DEVONO”, "NON DEVE” e “NON DEVONO”, “RICHIEDE” e “RICHIESTO”, “NON DEVE”, “DOVREBBE”, “NON DOVREBBE”, “RACCOMANDATO”, “PUÒ” e “OPZIONALE” nel presente documento devono essere interpretate come descritte nel BCP 14 `[RFC2119]`_ `[RFC8174]`_ quando e solo quando appaiono in maiuscolo.

Le notazioni [...] e ... indicano che il testo è stato troncato per esigenze editoriali.

*base64url* denota la codifica URL-safe base64 senza padding definita in `[RFC7515#Section_2]`_.



Termini utilizzati
------------------

Seguono i termini utilizzati da `[OIDC-FED#Section_1.2]`_ e in questo documento

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - **Entity configuration**
      - Dichiarazione di una entità emessa per proprio conto, nella forma di JWT auto firmato `[RFC7515]`_ e contenente la configurazione di se stessa. Contiene le chiavi pubbliche di Federazione, il metadata OIDC, gli URL delle autorità sue superiori e i Trust Mark emessi da autorità riconoscibili nella Federazione che attestano l’aderenza del soggetto a determinati profili.
    * - **Entity statement**
      - Dichiarazione di riconoscimento emessa da un'entità superiore (Trust Anchor o Intermediario) riguardante un'entità discendente (RP, OP o Intermediario) in formato JWT firmato `[RFC7515]`_, contenente la chiave pubblica del soggetto discendente, i Trust Mark emessi per i quali è emittente e la politica dei metadati da applicare ai metadati del soggetto.
    * - **Trust Mark**
      - JWT firmato `[RFC7515]`_ dall'ente emittente e relativo ad un partecipante. Attesta la conformità di questo ai profili riconoscibili all’interno Federazione (RP pubblico o privato, Soggetto Aggregatore Pubblico o Privato, etc.). La Foglia che acquisisce il marchio di fiducia durante la fase di onboarding DEVE includere questo nella sua Entity Configuration a mò di Badge di riconoscimento.
    * - **Metadata**
      - Un documento di metadati descrive una implementazione di una entità OpenID Connect. Le implementazioni di ogni Entità condividono i metadati per stabilire una base di fiducia e interoperabilità.
    * - **Metadata policy**
      - Il Trust Anchor pubblica le regole e le politiche da applicare sui metadata dei discendenti, specificando quali valori o sottoinsiemi di valori sono consentiti per un dato parametro di metadati.
    * - **Authority hint**
      - Un Array di valori url corrispondenti agli identificativi delle entità superiori, Trust Anchor o Intermediario, che DEVONO emettere un Entity Statement per i propri discendenti.
    * - **Metadata Discovery**
      - Raccolta di Entity Configuration e Statement. Inizia da un'entità Foglia fino al raggiungimento del Trust Anchor.
    * - **Trust Chain**
      - Procedura di validazione della sequenza di Entity Configuration e Statement raccolta mediante Metadata Discovery, il cui esito positivo è un metadata finale relativo ad una entità e la data di scadenza entro la quale questo deve essere aggiornato.
    * - **Onboarding**
      - Procedura di registrazione di una nuova entità all’interno della Federazione SPID
    * - **Federation Endpoint**
      - Endpoint usati per prendere e risolvere gli statement delle entità, interrogare una lista di tutte le entità subordinate e verificare lo stato dei trust mark.
