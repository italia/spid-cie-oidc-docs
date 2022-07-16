.. include:: ./common_definitions.rst

Le Federazioni eID Italiane
---------------------------

Una Federazione delle Identità Digitali è una infrastruttura all'interno della quale tante organizzazioni, afferenti a domini differenti, aderiscono ad un medesimo quadro regolatorio per costruire un meccanismo di fiducia sia amministrativo, mediante la stipula di convenzioni e accreditamento presso una o più autorità super partes, che tecnologico, mediante l'adozione di standard di interoperabilità sicuri che consentono l'interscambio dei dati.

Questa configurazione stabilisce i livelli di garanzia e di sicurezza adeguati affinchè un individuo possa autenticarsi presso un servizio web (Service Provider) mediante la propria identità digitale, rilasciata da un altro servizio web (Identity Provider).

I partecipanti (RP o OP), che si riconoscono all'interno della medesima Federazione, ottengono i Metadata gli uni degli altri. I Metadata contengono le chiavi pubbliche per le operazioni di firma digitale e criptazione e le definizioni necessarie all'interscambio delle informazioni.

I Metadata sono certificati da un parte fidata che all'interno della Federazione SPID è AgID, mentre all'interno della Federazione CIE è il Ministero dell'Interno. Questi corrispondono alla Autorità di Federazione.

SPID e CIE id implementano OpenID Connect Federation 1.0 e ne estendono alcune funzionalità, realizzano una implementazione concreta e producono le buone pratiche per la sua adozione. Per approfondimenti allo standard si rimanda alle specifiche ufficiali `OIDC-FED`_ e alla sezione :ref:`Differenze con OIDC Federation 1.0<differenze_con_oidc_federation>`. 


Perché OIDC Federation
++++++++++++++++++++++

La Federazione OIDC è un modello gerarchico:

 - **Dinamico**. La fiducia può essere stabilita dinamicamente durante la prima richiesta di autenticazione. 
   Le Autorità della Federazione espongono un endpoint che fornisce "dichiarazioni" firmate riguardanti le entità discendenti. Queste contengono le chiavi pubbliche dei discendenti e la politica dei Metadata. Le Autorità della Federazione possono disabilitare un'entità nella Federazione in qualsiasi momento, semplicemente smettendo di emettere le dichiarazioni inerenti a questa.
 - **Distribuito**. La fiducia viene distribuita fra molte parti. È il verificatore che decide quale percorso prendere per risolvere la fiducia (molte parti e due Autorità di Federazione).
 - **Scalabile**. Riduce significativamente i costi di onboarding, in accordo al principio di delega, con l'istituzione di entità intermediarie (SA).
 - **Trasparente**. Qualsiasi entità coinvolta nella Federazione può in ciascun momento costruire la fiducia autonomamente e in modo sicuro. Inoltre, la composizione della Federazione, in tutte le sue parti, diventa navigabile mediante la sua API, in tempo reale.

.. image:: ../../images/spid_cie_oidc_federation_model.svg
    :width: 100%

*Schema ad albero che rappresenta la struttura della Federazione SPID OIDC. Alla Base le Autorità di Federazione SPID e CIE id e, salendo, gli OP che non hanno Intermediari, gli RP e gli Intermediari che a loro volta Aggregano altri RP.*

Configurazione della Federazione
++++++++++++++++++++++++++++++++

La configurazione della Federazione è pubblicata dal Trust Anchor all'interno della sua :ref:`Entity Configuration<entity_configuration_ta>`, disponibile presso un web path ben noto e corrispondente a **.well-known/openid-federation**.

Tutti i partecipanti DEVONO ottenere, prima della fase di esercizio, la configurazione della Federazione e mantenerla aggiornata su base giornaliera. All'interno della Configurazione della Federazione è presente la chiave pubblica del Trust Anchor usata per le operazioni di firma, il numero massimo di Intermediari consentiti tra una Foglia e il Trust Anchor (**max_path length**) e le autorità abilitate all'emissione dei Trust Mark (**trust_marks_issuers**).


Si veda qui un esempio non normativo di :ref:`Entity Configuration response Trust Anchor<Esempio_EN1.4>`


Si veda la Sezione dedicata alle :ref:`Entity Configuration<Entity_Configuration>` per ulteriori dettagli.


Modalità di partecipazione
++++++++++++++++++++++++++

Per aderire alle Federazioni SPID e CIEid una entità di tipo Foglia deve pubblicare la propria configurazione (Entity Configuration) presso il proprio web endpoint :ref:`.well-known/openid-federation<Esempio_EN1>`.

Gli incaricati tecnici ed amministrativi della Foglia completano la procedura amministrativa per la registrazione di una nuova entità o l'aggiornamento di un'entità preesistente definita dalla Autorità di Federazione o da un suo Intermediario (SA).

L'Autorità di Federazione o il suo Intermediario, dopo aver effettuato tutti i controlli amministrativi e tecnici richiesti, registra le chiavi pubbliche della Foglia e rilascia una prova di adesione alla Federazione sotto forma di Trust Mark (TM).

La Foglia DEVE includere il TM all'interno della propria configurazione di Federazione (Entity Configuration) come prova del buon esito del processo di onboarding. 

L'Autorità di Federazione o suo Intermediario DEVE pubblicare la dichiarazione di riconoscimento della Foglia (Entity Statement) contenente le chiavi pubbliche di Federazione della Foglia e i TM a questa rilasciati. L'Autorità di Federazione o suo Intermediario PUÒ pubblicare una `politica dei metadata <https://openid.net/specs/openid-connect-federation-1_0.html#rfc.section.5.1>`_ per forzare la modifica dei metadata OIDC del discendente, nelle parti in cui questo fosse necessario.
