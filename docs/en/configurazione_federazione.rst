.. include:: ./common_definitions.rst


Configurazione della Federazione
--------------------------------

La configurazione della Federazione è pubblicata dal Trust Anchor all'interno della sua :ref:`Entity Configuration<entity_configuration_ta>`, disponibile presso un web path ben noto e corrispondente a **.well-known/openid-federation**.

Tutti i partecipanti DEVONO ottenere, prima della fase di esercizio, la configurazione della Federazione e mantenerla aggiornata su base giornaliera. All'interno della Configurazione della Federazione è presente la chiave pubblica del Trust Anchor usata per le operazioni di firma, il numero massimo di Intermediari consentiti tra una Foglia e il Trust Anchor (**max_path length**) e le autorità abilitate all'emissione dei Trust Mark (**trust_marks_issuers**).


Si veda qui un esempio non normativo di :ref:`Entity Configuration response Trust Anchor<Esempio_EN1.4>`


Si veda la Sezione dedicata alle :ref:`Entity Configuration<Entity_Configuration>` per ulteriori dettagli.


Modalità di partecipazione
--------------------------

Per aderire alle Federazioni SPID e CIEid una entità di tipo Foglia deve pubblicare la propria configurazione (Entity Configuration) presso il proprio web endpoint :ref:`.well-known/openid-federation<Esempio_EN1>`.

Gli incaricati tecnici ed amministrativi della Foglia completano la procedura amministrativa per la registrazione di una nuova entità o l'aggiornamento di un'entità preesistente definita dalla Autorità di Federazione o da un suo Intermediario (SA).

L'Autorità di Federazione o il suo Intermediario, dopo aver effettuato tutti i controlli amministrativi e tecnici richiesti, registra le chiavi pubbliche della Foglia e rilascia una prova di adesione alla Federazione sotto forma di Trust Mark (TM).

La Foglia DEVE includere il TM all'interno della propria configurazione di Federazione (Entity Configuration) come prova del buon esito del processo di onboarding. 

L'Autorità di Federazione o suo Intermediario DEVE pubblicare la dichiarazione di riconoscimento della Foglia (Entity Statement) contenente le chiavi pubbliche di Federazione della Foglia e i TM a questa rilasciati. L'Autorità di Federazione o suo Intermediario PUÒ pubblicare una `politica dei metadata <https://openid.net/specs/openid-connect-federation-1_0.html#rfc.section.5.1>`_ per forzare la modifica dei metadata OIDC del discendente, nelle parti in cui questo fosse necessario.
