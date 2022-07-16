.. include:: ./common_definitions.rst

Termini e Acronimi
------------------

Termini
+++++++

Seguono i termini utilizzati da `OIDC-FED#Section_1.2`_ e in questo documento.

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - **Autorità di Federazione**
      - Un'entità legale che gestisce la fiducia tra le parti coinvolte nella Federazione e norma il funzionamento e le modalità 
        di registrazione e riconoscimento dei partecipanti.
    * - **Trust Anchor**
      - Sistema gestito dalla Autorità di Federazione, che rappresenta la Federazione e la sua configurazione.
    * - **Intermediario**
      - Soggetto Aggregatore (SA), facilita l'ingresso nella Federazione e PUÒ gestire le funzionalità per conto di un 
        suo discendente (Aggregato). Pubblica la propria configurazione all'interno della Federazione e le affermazioni di riconoscimento delle parti sue discendenti (Aggregati) secondo le regole definite dalla Federazione.
    * - **Foglia**
      - Entità definita dal protocollo OIDC come Relying Party e Provider OpenID.
    * - **Entità**
      - Partecipante alla Federazione. Trust Anchor, Intermediario o Foglia.
    * - **Entity configuration**
      - Dichiarazione di un'entità, emessa per proprio conto, nella forma di JWT auto firmato :rfc:`7515` e contenente la sua configurazione. Contiene le chiavi pubbliche di Federazione, i Metadata OIDC, gli URL delle autorità sue superiori e i Trust Mark emessi da autorità riconoscibili nella Federazione che attestano l'aderenza del soggetto a determinati profili.
    * - **Entity statement**
      - Dichiarazione di riconoscimento emessa da un'entità superiore (Trust Anchor o Intermediario) riguardante un'entità discendente (RP, OP o Intermediario) in formato JWT firmato :rfc:`7515`, contenente la chiave pubblica del soggetto discendente, i Trust Mark emessi per i quali è emettitore e la politica dei Metadata da applicare ai Metadata del soggetto.
    * - **Trust Mark**
      - JWT firmato :rfc:`7515` dall'ente emettitore e relativo ad un partecipante. Attesta la conformità di questo ai profili riconoscibili all'interno Federazione (RP pubblico o privato, Soggetto Aggregatore Pubblico o Privato, etc.). La Foglia che acquisisce il marchio di fiducia durante la fase di onboarding DEVE includere questo nella sua Entity Configuration a mo' di Badge di riconoscimento.
    * - **Metadata**
      - Un documento di Metadata descrive una implementazione di una entità OpenID Connect. Le implementazioni di ogni Entità condividono i Metadata per stabilire una base di fiducia e interoperabilità.
    * - **Metadata policy**
      - Il Trust Anchor pubblica le regole e le politiche da applicare sui Metadata dei discendenti, specificando quali valori o sottoinsiemi di valori sono consentiti per un dato parametro di Metadata.
    * - **Authority hint**
      - Un array di valori url corrispondenti agli identificativi delle entità superiori, Trust Anchor o Intermediario, che DEVONO emettere un Entity Statement per i propri discendenti.
    * - **Metadata Discovery**
      - Raccolta di Entity Configuration e Statement. Inizia da un'entità Foglia fino al raggiungimento del Trust Anchor.
    * - **Trust Chain**
      - Procedura di validazione della sequenza di Entity Configuration e Statement raccolta mediante Metadata Discovery, il cui esito positivo è un Metadata finale relativo ad una entità e la data di scadenza entro la quale questo deve essere aggiornato.
    * - **Onboarding**
      - Procedura di registrazione di una nuova entità all'interno della Federazione SPID e CIE
    * - **Federation Endpoint**
      - Endpoint usati per prendere e risolvere gli statement delle entità, interrogare una lista di tutte le entità subordinate e verificare lo stato dei Trust Mark.

Acronimi 
++++++++

In questa sezione sono definiti tutti gli acronimi utilizzati all'interno del testo.

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
      - Agenzia per l'Italia Digitale, FA/TA di SPID
    * - **MinInterno**
      - Ministero dell'Interno, FA/TA di CIEid.
    * - **OP**
      - OpenID Provider (entità Foglia)
    * - **RP**
      - Relying Party (entità Foglia) 
    * - **SA**
      - Soggetti Aggregatori. Sono entità intermediarie che possono gestire tutti gli aspetti della Federazione di uno o più RP.
    * - **AA**
      - Attribute Authority, Gestore degli Attributi qualificati (entità Foglia)
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



Convenzioni e Termini normativi
+++++++++++++++++++++++++++++++

Le parole chiave "DEVE" e "DEVONO", "NON DEVE" e "NON DEVONO", "RICHIEDE" e "RICHIESTO", "NON DEVE", "DOVREBBE", "NON DOVREBBE", "RACCOMANDATO", "PUÒ" e "OPZIONALE" nel presente documento devono essere interpretate come descritte nel BCP 14 :rfc:`2119` :rfc:`8174` quando e solo quando appaiono in maiuscolo.

Le notazioni [...] e ... indicano che il testo è stato troncato per esigenze editoriali.

*base64url* denota la codifica URL-safe base64 senza padding definita in :rfc:`7515#section-2`.

.. warning::
    |warning-message|
