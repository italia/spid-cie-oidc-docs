.. include:: ./common_definitions.rst

Le Federazioni eID Italiane
---------------------------

Una Federazione delle Identità Digitali è una infrastruttura che consente ad un individuo di autenticarsi presso un servizio web (RP), 
utilizzando le proprie credenziali emesse da un provider di identità (OP). 

Affinché i partecipanti, siano essi RP o OP, si riconoscano all’interno della medesima Federazione delle identità è necessario che questi aderiscano ad un medesimo quadro regolatorio e ottengano i metadati gli uni degli altri. I Metadata contengono le chiavi pubbliche per le operazioni di firma digitale e criptazione e le definizioni necessarie all'interscambio delle informazioni.

I metadati sono certificati da un parte fidata che all’interno della Federazione SPID è AgID, mentre all'interno della Federazione CIE è il Ministero dell'Interno. Questi corrispondono alla Autorità di Federazione.

SPID e CIE id implementano OpenID Connect Federation 1.0 e ne estendono alcune funzionalità, realizzano una implementazione concreta e producono le buone pratiche per la sua adozione. Per approfondimenti allo standard si rimanda alle specifiche ufficiali `[OIDC-FED]`_ e alla sezione “Differenze con OIDC Federation 1.0”. 


Perché OIDC Federation
++++++++++++++++++++++

La Federazione OIDC è un modello gerarchico basato su un meccanismo di delega dinamica. Il modello di fiducia dietro la Federazione OIDC è:

 - **Dinamico**. La fiducia può essere stabilita dinamicamente durante la prima richiesta di autenticazione. 
   Le Autorità della Federazione espongono un endpoint che fornisce “dichiarazioni” firmate riguardo alle entità discendenti, contenenti le loro chiavi pubbliche e la politica dei metadati. In più, le Autorità della Federazione possono disabilitare un'entità nella Federazione in qualsiasi momento, senza esplicite comunicazioni agli altri membri.
 - **Distribuito**. La fiducia viene distribuita fra molte parti. È il verificatore che decide quale percorso prendere per risolvere la fiducia (molte parti e due Autorità di Federazione).
 - **Scalabile**. Riduce significativamente i costi di onboarding, in accordo al principio di delega, con l'istituzione di entità intermediatrici (SA).
 - **Trasparente**. Qualsiasi entità coinvolta nella Federazione può in ciascun momento costruire la fiducia autonomamente e in modo sicuro.

.. image:: ../../images/spid_cie_oidc_federation_model.svg
    :width: 100%

*Schema ad albero che rappresenta la struttura della Federazione SPID OIDC. Alla Base le Autorità di Federazione SPID e CIE id e, salendo, gli OP che non hanno intermediari, gli RP e gli Intermediari che a loro volta Aggregano altri RP.*


Entità della Federazione
++++++++++++++++++++++++

Le parti coinvolte all’interno di una Federazione OpenID Connect sono le seguenti:

.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - **Autorità di Federazione**
     - Un'entità che gestisce la fiducia tra le parti coinvolte nella Federazione e norma il funzionamento e le modalità 
       di registrazione e riconoscimento dei partecipanti. Si tratta di un **Trust Anchor** (la radice del *trust*) o di un **Intermediario**. 
   * - **Trust Anchor**
     - Un'Autorità della Federazione, che rappresenta una terza parte fidata e può delegare altre Autorità della Federazione
       (**Intermediari**) a portare avanti l'**onboarding** delle **Foglie**.
   * - **Intermediario**
     - Soggetto Aggregatore (SA), facilita l'ingresso nella Federazione e PUÒ gestire le funzionalità per conto di un 
       suo discendente (Aggregato). Pubblica la propria configurazione all’interno della Federazione e le affermazioni di riconoscimento delle parti sue discendenti (Aggregati) secondo le regole definite dalla Federazione.
   * - **Foglia**
     - Entità definita dal protocollo OIDC come Relying Party e Provider OpenID.
   * - **Entità**
     - Partecipante alla Federazione. Trust Anchor, Intermediario o Foglia.
