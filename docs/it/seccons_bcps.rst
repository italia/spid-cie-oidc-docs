.. include:: ../common/common_definitions.rst

.. _Considerazioni_di_Sicurezza:

Considerazioni di Sicurezza
---------------------------

In questa sezione descriviamo alcune considerazioni di sicurezza in ambito OIDC Federation.


Trust Mark come deterrente contro gli abusi
+++++++++++++++++++++++++++++++++++++++++++

L'implementazione dei Trust Mark e il filtro su questi in fase di Metadata Discovery risulta necessario contro gli attacchi destinati al consumo delle risorse. Un OP attaccato con un numero ingente di connessioni presso il suo endpoint di *authorization*, contenenti **client_id** e **authority_hints** fasulli, produrrebbe svariate connessioni verso sistemi di terze parti nel tentativo di trovare un percorso verso la TA e instaurare la fiducia con il richiedente.

L'OP DEVE validare staticamente il TM oppure DEVE escludere a priori la richiesta ove il TM non risultasse presente, in caso di assenza o non validità di un TM la procedura di Metadata Discovery NON DEVE essere avviata e NON DEVE creare di conseguenza connessioni verso sistemi di terze parti.


Numero Massimo di authority_hints
+++++++++++++++++++++++++++++++++

All'interno di una Federazione il Trust Anchor decide quante intermediazioni consentire tra di lui e le Foglie, mediante la constraint denominata **max_path_lenght**. Questo tipo di relazione è di tipo verticale, dalla Foglia alla radice. Questo attributo se valorizzato ad esempio con un valore numerico intero pari a 1 indica che soltanto un SA è consentito tra una Foglia e il TA.

Ogni Foglia DEVE pubblicare i suoi superiori all'interno della lista contenuta nel claim **authority_hints**. Una Foglia all'interno della Federazione PUÒ avere superiori afferenti a diverse Federazioni. L'analisi dei superiori disponibili introduce un modello di navigazione orizzontale, ad esempio un OP tenta di trovare il percorso più breve verso il Trust Anchor attraverso tutti gli URL contenuti all'interno dell'array **authority_hints** prima di fare un ulteriore movimento verticale, a salire, verso uno degli Intermediari presenti in questo array.

La soglia **max_path_lenght** si applica per la navigazione verticale e superata questa soglia senza aver trovato il TA, la procedura di Metadata Discovery DEVE essere interrotta. Si faccia l'esempio di un RP discendente di un SA che a sua volta è discendente di un altro SA, essendo il valore di **max_path_lenght** pari a 1 e, superata questa soglia senza aver trovato il Trust Anchor, la procedura DEVE essere interrotta.

Allo stesso tempo la specifica OIDC Federation 1.0 non definisce un limite per il numero di **authority_hints**, questo perché nessun Trust Anchor può limitare il numero di Federazioni alle quali un partecipante può aderire. Per questa ragione è utile che gli implementatori adottino un limite massimo del numero di elementi consentiti all'interno dell'Array authority_hint. Questo per evitare che un numero esagerato di URL contenuti nella lista di **authority_hints**, dovuto ad una cattiva configurazione di una Foglia, produca un consumo di risorse eccessivo.


Resolve Entity Statement
++++++++++++++++++++++++

Questo endpoint DEVE rilasciare i Metadata, i Trust Mark e la Trust Chain già precedentemente elaborata e NON DEVE innescare una procedura di Metadata Discovery ad ogni richiesta pervenuta.


Buone Pratiche
--------------

In questa sezione descriviamo alcune buone pratiche per ottenere la massima resa dalle entità di Federazione.


Specializzare le chiavi pubbliche OpenID Core e Federation
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

È buona pratica usare chiavi pubbliche specializzate per i due tipi di operazioni, Core e Federation.

Modalità di aggiornamento dei Metadata OpenID Core
++++++++++++++++++++++++++++++++++++++++++++++++++

L'interoperabilità tra i partecipanti funziona mediante i Metadata ottenuti dal calcolo e dalla conservazione delle Trust Chain. Questo significa che se un OP al tempo T calcola la Trust Chain per un RP e questo al tempo T+n modifica i propri Metadata, l'OP di conseguenza potrebbe incorrere in problematiche di validazione delle richieste di autorizzazione del RP, fino a quando non avrà aggiornato la Trust Chain relativa a questo.

La buona pratica per evitare le interruzioni di servizio relative alle operazioni di OIDC Core è quella di aggiungere le nuove chiavi pubbliche all'interno degli oggetti *jwks* senza rimuovere i valori preesistenti. Oppure, ad esempio, i nuovi *redirect_uri*.

In questa maniera dopo il limite massimo di durata delle Trust Chain, definito con il claim **exp** e pubblicato nella Entity Configuration della TA, si ha la certezza che tutti i partecipanti abbiano rinnovato le loro Trust Chain, e sarà possibile agli amministratori della Foglia rimuovere le vecchie definizioni in cima alla lista.

Politica dei Metadata
+++++++++++++++++++++

L'Autorità di Federazione o il suo Intermediario PUÒ pubblicare una politica dei Metadata (vedi `OIDC-FED#Section.5.1`_) per forzare la modifica dei Metadata OIDC della Foglia, nelle parti in cui questo fosse necessario.
