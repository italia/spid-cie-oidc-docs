.. include:: ../common/common_definitions.rst

.. _federation_endpoint:

Endpoint di Federazione
-----------------------

Tutte le entità DEVONO contenere i seguenti endpoint:

 - **/.well-known/openid-federation**: fornisce l'`Entity Configuration <Entity_Configuration>`__ (per maggiori dettagli vedi `OIDC-FED`_ Section 6)
 - **resolve entity statement endpoint**: fornisce il metadata finale, la Trust Chain e i Trust Mark relativi ad un altro soggetto. Per maggiori dettagli vedi `OIDC-FED`_ Section 7.2.

.. warning::
  Il **resolve entity statement endpoint** NON DEVE restituire alcuna informazione relativa ad un soggetto del quale non ha precedentemente raccolto gli statement e calcolato la Trust Chain. Nel caso in cui i TM non siano più validi al momento della richiesta, questi NON DEVONO essere inclusi nella risposta.


Le Entità di tipo **TA** o **SA** DEVONO offrire i seguenti endpoint, in aggiunta agli endpoint di federazione sopra riportati:

 - **fetch entity statement endpoint**: fornisce gli ES relativi ad un soggetto discendente diretto. Per ottenere un ES è necessario indicare almeno l'identificativo dell'entità di cui si vuole ottenere lo statement. (per maggiori dettagli vedi `OIDC-FED`_ Section 7.1)  
 - **trust mark status endpoint**: permette a un'entità di verificare se un TM è ancora attivo o no. La query DEVE essere inviata al soggetto che ha rilasciato quel TM. (per maggiori dettagli vedi `OIDC-FED`_ Section 7.4)
 - **entity listing endpoint**: fornisce la lista delle entità discendenti registrate presso il TA o un SA (per maggiori dettagli vedi `OIDC-FED`_ Section 7.3)

Un'entità di tipo **AA**, oltre agli endpoint di Federazione comuni a tutte le entità, DEVE riportare anche il **trust mark status endpoint** per consentire la validazione dinamica dei TM rilasciati dall'AA.
