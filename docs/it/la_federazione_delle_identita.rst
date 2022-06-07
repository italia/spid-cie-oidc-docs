.. include:: ./common_definitions.rst

La Federazione SPID e CIE id
============================


Che cos'è una Federazione
-------------------------

Affinché le parti si riconoscano all’interno della medesima Federazione delle identità è necessario che ognuna di queste ottenga la prova della reciproca aderenza ad un medesimo quadro regolatorio. Le parti ottengono i metadati gli uni degli altri,  contenenti le chiavi pubbliche per le operazioni di firma digitale e criptazione e le definizioni necessarie all'interscambio delle informazioni, secondo le regole prestabilite.

SPID adotta le specifiche di OpenID Connect (OIDC) Federation 1.0 [OIDC-FED] che definiscono come le entità, intese come partecipanti ad una Federazione, possono riconoscersi ed ottenere i metadati di Federazione e i metadati per il protocollo OpenID Connect [OpenID.Core]. I metadati sono certificabili da un parte fidata che all’interno della Federazione SPID è AgID e corrisponde alla Autorità di Federazione.

SPID implementa OpenID Connect Federation 1.0 ed estende alcune funzionalità dello standard, ne realizza una implementazione concreta e produce le buone pratiche per la sua adozione. Per approfondimenti allo standard si rimanda alle specifiche ufficiali [OIDC-FED] e alla sezione “Differenze con OIDC Federation 1.0”. 



Come le parti stabiliscono la fiducia tra di loro
-------------------------------------------------

Affinché le parti si riconoscano all’interno della medesima Federazione delle identità, è necessario che ognuna di queste ottenga la prova della reciproca aderenza ad un medesimo quadro regolatorio. Le parti ottengono i metadati gli uni degli altri, contenenti le chiavi pubbliche per le operazioni di firma digitale e criptazione e le definizioni necessarie all'interscambio delle informazioni, secondo le regole prestabilite.


Entità della Federazione
------------------------

Le parti coinvolte all’interno di una Federazione OpenID Connect sono le seguenti:

.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - **Autorità di Federazione**
     - Agenzia per l'Italia Digitale (AgID). Norma il funzionamento e le modalità di registrazione e riconoscimento dei partecipanti.
   * - **Trust Anchor**
     - Sistema gestito dalla AgID il cui compito è quello di pubblicare la configurazione della Federazione e le affermazioni di riconoscimento delle parti che afferiscono alla Federazione. Il Trust Anchor corrisponde alla Autorità di Federazione e rappresenta la Federazione stessa.
   * - **Intermediario**
     - Soggetto Aggregatore (SA), facilita l'ingresso nella Federazione e PUÒ gestire le funzionalità per conto di un suo discendente (Aggregato), pubblica la propria configurazione all’interno della Federazione e le affermazioni di riconoscimento delle parti sue discendenti (Aggregati) in conformità alle regole definite dalla AgID.
   * - **Foglia**
     - Entità definita dal protocollo OIDC come Relying Party e Provider OpenID.
   * - **Entità**
     - Partecipante alla Federazione. Trust Anchor, Intermediario o Foglia.


Configurazione della Federazione SPID
-------------------------------------

La configurazione della Federazione SPID è pubblicata dal Trust Anchor all'interno della sua :ref:`Entity Configuration <Esempio_EN1.4>`_, presso un web path ben noto e corrispondente a **.well-known/openid-federation**.

Tutti i partecipanti DEVONO ottenere prima della fase di esercizio la configurazione della Federazione e mantenere questa aggiornata su base giornaliera. All’interno della Configurazione della Federazione è presente la chiave pubblica del Trust Anchor usata per le operazioni di firma, il numero massimo di Intermediari consentiti tra una Foglia e il Trust Anchor (**max_path length**) e le autorità abilitate all’emissione dei Trust Marks (**trust_marks_issuers**).










