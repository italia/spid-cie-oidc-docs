.. include:: ./common_definitions.rst

Come iniziare
=============


Introduzione
------------

Questo documento definisce le regole di funzionamento della Federazione OpenID Connect SPID (link alla pagina ufficiale) e CIE id (link alla pagina ufficiale) per Fornitori di Servizio pubblici e privati (RP), Identity Providers (OP) e Soggetti Aggregatori (SA). Definisce inoltre gli schemi dei metadati di RP, OP e SA in contesto Federativo, le modalità di registrazione dei RP presso gli OP, le risorse e gli endpoint a supporto della Federazione.


Che cosa sono le identità digitali
----------------------------------

Grazie all’`identità digitale <https://identitadigitale.gov.it/>`_, la Pubblica Amministrazione e i fornitori di servizi privati forniscono la chiave per accedere ai servizi online attraverso una credenziale unica, che si attiva una sola volta ed è sempre valida.

Semplice, veloce e sicuro, l’accesso ai servizi pubblici online è possibile con il `Sistema Pubblico di Identità Digitale (SPID) <https://www.spid.gov.it/>`_ e la `Carta d’Identità Elettronica (CIE) <https://www.cartaidentita.interno.gov.it/>`_. SPID e CIE sono gli strumenti di identificazione per accedere ai servizi online della PA e ai servizi dei privati aderenti.

Grazie a SPID e CIE id diventa uniforme l’accesso ai servizi pubblici in tutto il territorio nazionale.

Si rimanda al Codice dell'`Amministrazione Digitale <https://docs.italia.it/italia/piano-triennale-ict/codice-amministrazione-digitale-docs/it/v2021-07-30/_rst/capo_V-sezione_III-articolo_65.html>`_ in relazione agli obblighi di adozione dei sistemi di identità digitale.


Acronimi IAM e AAI
------------------

In questa sezione sono definiti tutti gli acronimi utilizzati all’interno del testo.

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - **AdF**
      - Autorità di Federazione, che è AgID
    * - **OIDC**
      - OpenID Connect
    * - **OIDC-FED**
      - OIDC Federation 1.0
    * - **IOF**
      - Italian OIDC Federation 1.0
    * - **SPID**
      - Sistema Pubblico di Identità Digitale
    * - **AgID**
      - Agenzia per l’Italia Digitale
    * - **SA**
      - Soggetti Aggregatori
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


Termini utilizzati
------------------

Seguono i termini utilizzati da `[OIDC-FED#Section_1.2]`_ e in questo documento

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - Entity configuration
      - Dichiarazione di una entità emessa per proprio conto, nella forma di JWT auto firmato `[RFC7515]`_ e contenente la configurazione di se stessa. Contiene le chiavi pubbliche di Federazione, il metadata OIDC, gli URL delle autorità sue superiori e i Trust Mark emessi da autorità riconoscibili nella Federazione che attestano l’aderenza del soggetto a determinati profili.
    * - Entity statement
      - Dichiarazione di riconoscimento emessa da un'entità superiore (Trust Anchor o Intermediario) riguardante un'entità discendente (RP, OP o Intermediario) in formato JWT firmato `[RFC7515]`_, contenente la chiave pubblica del soggetto discendente, i Trust Mark emessi per i quali è emittente e la politica dei metadati da applicare ai metadati del soggetto.
    * - Trust Mark
      - JWT firmato `[RFC7515]`_ dall'ente emittente e relativo ad un partecipante. Attesta la conformità di questo ai profili riconoscibili all’interno Federazione (RP pubblico o privato, Soggetto Aggregatore Pubblico o Privato, etc.). La Foglia che acquisisce il marchio di fiducia durante la fase di onboarding DEVE includere questo nella sua Entity Configuration a mò di Badge di riconoscimento.
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



Come diventare fornitore di servizi 
-----------------------------------

Qui di seguito riportiamo gli indirizzi di riferimento per le procedure di "onboarding" di SPID e CIE, cioè per diventare fornitori di servizi.

`Come diventare fornitori di servizi SPID <https://www.spid.gov.it/cos-e-spid/diventa-fornitore-di-servizi/>`_

`Come diventare fornitori di servizi CIE <https://www.cartaidentita.interno.gov.it/esercenti/come-attivare-entra-con-cie/>`_

