.. include:: ./common_definitions.rst



Endpoint per Trust Anchor ed Intermediari
-----------------------------------------
Il Trust Anchor e i suoi Intermediari (federation_entity) DEVONO in aggiunta esporre al pubblico i seguenti endpoint:


Fetch entity statement endpoint
+++++++++++++++++++++++++++++++

Il recupero degli Entity Statement viene effettuato presso questo endpoint secondo le modalità definite all’interno di OIDC-FED “7.1. Fetching Entity Statements”.


.. _Trust_mark_status_endpoint:

Trust mark status endpoint
++++++++++++++++++++++++++

L’assegnazione di un Trust Mark ad un soggetto viene effettuato presso questo endpoint secondo le modalità definite all’interno di OIDC-FED “7.4. Trust Mark Status”.


.. _Entity_Listing_endpoint:

Entity Listing endpoint
+++++++++++++++++++++++

Per ottenere la lista dei discendenti registrati presso la TA o un suo Intermediario è possibile interrogare questo endpoint secondo le modalità descritte in `[OIDC-FED#Section.7.3]`_. Ai parametri esistenti già definiti nella specifica, si aggiunge per SPID il parametro entity_type come filtro sul tipo di entità dei discendenti (<entity-type>).


