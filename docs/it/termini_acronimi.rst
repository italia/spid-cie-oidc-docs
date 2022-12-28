.. include:: ../common/common_definitions.rst

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
        suo discendente (aggregato). Pubblica la propria configurazione all'interno della Federazione e le affermazioni di riconoscimento delle parti sue discendenti (aggregati) secondo le regole definite dall'Autorità di Federazione.
    * - **Foglia**
      - Entità definita dal protocollo OpenID Connect come Relying Party e Provider OpenID. Può anche essere una Attribute Authority (OAuth2 Authorization Server e Resource Server).
    * - **Entità**
      - Partecipante alla Federazione. Trust Anchor, Intermediario o Foglia.
    * - **Entity Configuration**
      - Dichiarazione di un'entità, emessa per proprio conto, nella forma di JWT auto firmato :rfc:`7515` e contenente la sua configurazione. Contiene le chiavi pubbliche di Federazione, i Metadata OIDC, gli URL delle autorità sue superiori e i Trust Mark emessi da autorità riconoscibili nella Federazione che attestano l'aderenza del soggetto a determinati profili.
    * - **Entity Statement**
      - Dichiarazione di riconoscimento emessa da un'entità superiore (Trust Anchor o Intermediario) riguardante un soggetto discendente (RP, OP, AA o Intermediario) in formato JWT firmato :rfc:`7515`, contenente le chiavi pubbliche del soggetto discendente, i Trust Mark emessi per i quali è emettitore e la politica dei Metadata da applicare ai Metadata del soggetto.
    * - **Trust Mark**
      - JWT firmato :rfc:`7515` dall'ente emettitore e relativo ad un partecipante. Attesta la conformità di questo ai profili riconoscibili all'interno Federazione (RP pubblico o privato, Soggetto Aggregatore Pubblico o Privato, etc.). La Foglia che acquisisce il marchio di fiducia durante il processo di onboarding DEVE includere questo nella sua Entity Configuration.
    * - **Metadata**
      - Documento che descrive l'implementazione di una entità OpenID Connect o OAuth2. Le implementazioni di ogni Entità condividono i Metadata per stabilire una base di fiducia e interoperabilità.
    * - **Metadata policy**
      - Il Trust Anchor pubblica le regole e le politiche da applicare sui Metadata dei discendenti, specificando quali valori o sottoinsiemi di valori sono consentiti per un dato parametro di Metadata.
    * - **Authority hint**
      - Array di valori URL contenente gli identificativi delle Entità superiori, Trust Anchor o Intermediario, che emettono un Entity Statement per i propri discendenti.
    * - **Federation Entity Discovery**
      - Raccolta di Entity Configuration e Statement. Inizia da un'Entità Foglia fino al raggiungimento del Trust Anchor.
    * - **Trust Chain**
      - Procedura di validazione della sequenza di Entity Configuration e Statement raccolta mediante Federation Entity Discovery, il cui esito positivo è un Metadata finale relativo ad una Entità e la data di scadenza entro la quale la Trust Chain deve essere aggiornata.
    * - **Onboarding**
      - Procedura di registrazione di una nuova entità all'interno della Federazione SPID e CIE
    * - **Federation Endpoint**
      - Endpoint definit in OIDC Federation 1.0, usati per prendere e risolvere gli statement delle entità, interrogare una lista di tutte le entità subordinate e verificare lo stato dei Trust Mark.
..      * - **Sessione individuale**
..        - Sessione che un fornitore di servizio (RP) può instaurare con un utente al fine di erogare un particolare servizio.


Acronimi 
++++++++

In questa sezione sono definiti tutti gli acronimi utilizzati all'interno del testo.

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - **SPID**
      - Sistema Pubblico di Identità Digitale italiano, la cui Authorità di Federazione è la AgID (Agenzia per l'Italia Digitale).
    * - **CIE id**
      - Sistema Pubblico di Identità Digitale italiano basato sulla Carta d'Identità Elettronica (CIE), di cui il Ministero dell'Interno è l'Autorità di Federazione. La gestione tecnica e operativa è affidata all'Istituto Poligrafico e Zecca dello Stato (IPZS).
    * - **OIDC**
      - OpenID Connect.
    * - **OIDC-FED**
      - `OIDC Federation 1.0 <https://openid.net/specs/openid-connect-federation-1_0.html>`_.
    * - **FA**
      - Autorità di Federazione (Federation Authority).
    * - **TA**
      - OIDC Federation Trust Anchor.
    * - **AgID**
      - Agenzia per l'Italia Digitale, FA/TA di SPID.
    * - **MinInterno**
      - Ministero dell'Interno, FA/TA di CIE id.
    * - **OP**
      - OpenID Provider (Entità Foglia).
    * - **RP**
      - Relying Party (Entità Foglia).
    * - **SA**
      - Soggetti Aggregatori. Entità Intermediarie che possono gestire tutti gli aspetti della Federazione di uno o più RP.
    * - **AA**
      - Attribute Authority, Gestore degli Attributi qualificati (Entità Foglia).
    * - **TM**
      - Trust Mark.
    * - **EC**
      - Entity Configuration.
    * - **ES**
      - Entity Statement.
    * - **URL**
      - Uniform Resource Locator, corrispondente ad un indirizzo web.
    * - **JWT**
      - Vedi :rfc:`7519` Jones, M., Bradley, J. and N. Sakimura, "JSON Web Token (JWT)", RFC 7519, DOI 10.17487/RFC7519, May 2015. 
    * - **RS**
      - OAuth2 Resource Server.
    * - **$JWT**
      - Il valore di un JWT (JSON Web Token).



Convenzioni e Termini normativi
+++++++++++++++++++++++++++++++

Le parole chiave "DEVE" e "DEVONO", "NON DEVE" e "NON DEVONO", "RICHIEDE" e "RICHIESTO", "NON DEVE", "DOVREBBE", "NON DOVREBBE", "RACCOMANDATO", "PUÒ" e "OPZIONALE" nel presente documento devono essere interpretate come descritte nel BCP 14 :rfc:`2119` :rfc:`8174` quando e solo quando appaiono in maiuscolo.

Le notazioni [...] e ... indicano che il testo è stato troncato per esigenze editoriali.

*base64url* denota la codifica URL-safe base64 senza padding definita in :rfc:`7515#section-2`.

Tutti gli esempi contenuti in questo documento sono da considerarsi come non normativi.

.. warning::
    |warning-message-it|
