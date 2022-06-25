.. include:: ./common_definitions.rst

Termini utilizzati
------------------

Seguono i termini utilizzati da `OIDC-FED#Section_1.2`_ e in questo documento.

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - **Autorità di Federazione (Federation Authority)**
      - Un'entità legale che gestisce uno schema di identità digitale su un protocollo di federazione.
    * - **Trust Anchor**
      - Una Autorità di Federazione che stabilisce la fiducia tra le parti della federazione. 
    * - **Entity configuration**
      - Dichiarazione di una entità emessa per proprio conto, nella forma di JWT auto firmato :rfc:`7515` e contenente la configurazione di se stessa. Contiene le chiavi pubbliche di Federazione, il metadata OIDC, gli URL delle autorità sue superiori e i Trust Mark emessi da autorità riconoscibili nella Federazione che attestano l’aderenza del soggetto a determinati profili.
    * - **Entity statement**
      - Dichiarazione di riconoscimento emessa da un'entità superiore (Trust Anchor o Intermediario) riguardante un'entità discendente (RP, OP o Intermediario) in formato JWT firmato :rfc:`7515`, contenente la chiave pubblica del soggetto discendente, i Trust Mark emessi per i quali è emittente e la politica dei metadati da applicare ai metadati del soggetto.
    * - **Trust Mark**
      - JWT firmato :rfc:`7515` dall'ente emittente e relativo ad un partecipante. Attesta la conformità di questo ai profili riconoscibili all’interno Federazione (RP pubblico o privato, Soggetto Aggregatore Pubblico o Privato, etc.). La Foglia che acquisisce il marchio di fiducia durante la fase di onboarding DEVE includere questo nella sua Entity Configuration a mò di Badge di riconoscimento.
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
      - Procedura di registrazione di una nuova entità all’interno della Federazione SPID e CIE
    * - **Federation Endpoint**
      - Endpoint usati per prendere e risolvere gli statement delle entità, interrogare una lista di tutte le entità subordinate e verificare lo stato dei trust mark.

Acronimi 
--------

In questa sezione sono definiti tutti gli acronimi utilizzati all’interno del testo.

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - **SPID**
      - Sistema Pubblico di Identità Digitale
    * - **CIEid**
      - Il sistema di identità digitale italiano basato sulla Carta d'Identità Elettronica (CIE), di cui il Ministero dell'Interno è il titolare. La gestione tecnica e operativa è affidata all'Istituto Poligrafico e Zecca dello Stato (IPZS).
    * - **OIDC**
      - OpenID Connect
    * - **OIDC-FED**
      - `OIDC Federation 1.0 <https://openid.net/specs/openid-connect-federation-1_0.html>`_.
    * - **IOF**
      - Italian OIDC Federation 1.0.
    * - **FA**
      - Autorità di Federazione (Federation Authority).
    * - **TA**
      - OIDC Federation Trust Anchor
    * - **AgID**
      - Agenzia per l’Italia Digitale, FA/TA di SPID
    * - **MinInterno**
      - Ministero dell'Interno, FA/TA di CIEid.
    * - **OP**
      - OpenID Provider (entità foglia)
    * - **RP**
      - Relying Party (entità foglia) 
    * - **SA**
      - Soggetti Aggregatori. Sono entità intermediarie che possono gestire tutti gli aspetti della federazione di uno o più RP.
    * - **AA**
      - Attribute Authority, Gestore degli Attributi qualificati (entità foglia)
    * - **TM**
      - Trust Mark
    * - **EC**
      - Entity Configuration
    * - **ES**
      - Entity Statement
    * - **URL**
      - Uniform Resource Locator, corrispondente ad un indirizzo web
    * - **JWT**
      - Vedi :rfc:`7519` Jones, M., Bradley, J. and N. Sakimura, "JSON Web Token (JWT)", RFC 7519, DOI 10.17487/RFC7519, May 2015. 
    * - **RS**
      - OAuth Resource Server
    * - **$JWT**
      - Il valore di un JWT (JSON Web Token).



Convenzioni e Terminologia
--------------------------

Le parole chiave “DEVE” e “DEVONO”, "NON DEVE” e “NON DEVONO”, “RICHIEDE” e “RICHIESTO”, “NON DEVE”, “DOVREBBE”, “NON DOVREBBE”, “RACCOMANDATO”, “PUÒ” e “OPZIONALE” nel presente documento devono essere interpretate come descritte nel BCP 14 :rfc:`2119` :rfc:`8174` quando e solo quando appaiono in maiuscolo.

Le notazioni [...] e ... indicano che il testo è stato troncato per esigenze editoriali.

*base64url* denota la codifica URL-safe base64 senza padding definita in :rfc:`7515#section-2`.

.. warning::
    |warning-message|
