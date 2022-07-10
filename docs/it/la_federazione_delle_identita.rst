.. include:: ./common_definitions.rst

Le Federazioni eID Italiane
---------------------------

Una Federazione delle Identità Digitali è una infrastruttura all'interno della quale tante organizzazioni, afferenti a domini differenti, aderiscono ad un medesimo quadro regolatorio per costruire un meccanismo di fiducia sia amministrativo, mediante la stipula di convenzioni e accreditamento presso una o più autorità super partes, che tecnologico, mediante l'adozione di standard di interoperabilità sicuri che consentono l'interscambio dei dati.

Questa configurazione stabilisce i livelli di garanzia e di sicurezza adeguati affinchè un individuo possa autenticarsi presso un servizio web (Service Provider) mediante la propria identità digitale, rilasciata da un altro servizio web (Identity Provider).

Affinché i partecipanti, siano essi RP o OP, si riconoscano all'interno della medesima Federazione delle identità è necessario che questi aderiscano ad un medesimo quadro regolatorio e ottengano i Metadata gli uni degli altri. I Metadata contengono le chiavi pubbliche per le operazioni di firma digitale e criptazione e le definizioni necessarie all'interscambio delle informazioni.

I Metadata sono certificati da un parte fidata che all'interno della Federazione SPID è AgID, mentre all'interno della Federazione CIE è il Ministero dell'Interno. Questi corrispondono alla Autorità di Federazione.

SPID e CIE id implementano OpenID Connect Federation 1.0 e ne estendono alcune funzionalità, realizzano una implementazione concreta e producono le buone pratiche per la sua adozione. Per approfondimenti allo standard si rimanda alle specifiche ufficiali `OIDC-FED`_ e alla sezione :ref:`Differenze con OIDC Federation 1.0<differenze_con_oidc_federation>`. 


Perché OIDC Federation
++++++++++++++++++++++

La Federazione OIDC è un modello gerarchico:

 - **Dinamico**. La fiducia può essere stabilita dinamicamente durante la prima richiesta di autenticazione. 
   Le Autorità della Federazione espongono un endpoint che fornisce "dichiarazioni" firmate riguardo alle entità discendenti, contenenti le loro chiavi pubbliche e la politica dei Metadata. In più, le Autorità della Federazione possono disabilitare un'entità nella Federazione in qualsiasi momento.
 - **Distribuito**. La fiducia viene distribuita fra molte parti. È il verificatore che decide quale percorso prendere per risolvere la fiducia (molte parti e due Autorità di Federazione).
 - **Scalabile**. Riduce significativamente i costi di onboarding, in accordo al principio di delega, con l'istituzione di entità intermediarie (SA).
 - **Trasparente**. Qualsiasi entità coinvolta nella Federazione può in ciascun momento costruire la fiducia autonomamente e in modo sicuro.

.. image:: ../../images/spid_cie_oidc_federation_model.svg
    :width: 100%

*Schema ad albero che rappresenta la struttura della Federazione SPID OIDC. Alla Base le Autorità di Federazione SPID e CIE id e, salendo, gli OP che non hanno Intermediari, gli RP e gli Intermediari che a loro volta Aggregano altri RP.*

