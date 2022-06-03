Revocation Endpoint (logout)
============================

Il Revocation Endpoint consente al RP di chiedere la revoca di un *access token* o di un *refresh token* in suo possesso.

Quando l’utente esegue il logout o quando la sua sessione presso il RP scade (in base alle policy decise da quest’ultimo), il RP deve chiamare questo endpoint per revocare l’*access token* e l’eventuale *refresh token* in suo possesso.

L’OP dovrà revocare il token specificato nella richiesta e dovrà terminare la sessione di Single Sign-On se ancora attiva. Eventuali altri token attivi per l’utente dovranno invece essere mantenuti validi.

.. seealso::

 - https://tools.ietf.org/html/rfc7009
 
Request
+++++++

La richiesta al Revocation Endpoint consiste nell’invio del token che si vuole revocare unitamente a una Client Assertion che consente di identificare il RP che esegue la richiesta.

**Esempio:**

.. code-block::

 POST https://op.spid.agid.gov.it/revoke?
 client_assertion=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiw
 ibmFtZSI6IlNQSUQiLCJhZG1pbiI6dHJ1ZX0.LVyRDPVJm0S9q7oiXcYVIIqGWY0wWQlqxvFGYswLF88&
 client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwtbearer&
 client_id=https%3A%2F%2Frp.spid.agid.gov.it&
 token=eyJhbGciOiJSUzI1NiJ9.eyJleHAiOjE0MTg3MDI0MTQsImF1ZCI6WyJlNzFmYjcyYS05NzRmLT
 QwMDEtYmNiNy1lNjdjMmJjMDAzN2YiXSwiaXNzIjoiaHR0cHM6XC9cL2FzLXZhLmV4YW1wbGUuY29tXC8
 iLCJqdGkiOiIyMWIxNTk2ZC04NWQzLTQzN2MtYWQ4My1iM2YyY2UyNDcyNDQiLCJpYXQiOjE0MTg2OTg4
 MTR9.FXDtEzDLbTHzFNroW7w27RLk5m0wprFfFH7h4bdFw5fR3pwiqejKmdfAbJvN3_yfAokBv06we5RA
 RJUbdjmFFfRRW23cMbpGQCIk7Nq4L012X_1J4IewOQXXMLTyWQQ_BcBMjcW3MtPrY1AoOcfBOJPx1k2jw
 RkYtyVTLWlff6S5gKciYf3b0bAdjoQEHd_IvssIPH3xuBJkmtkrTlfWR0Q0pdpeyVePkMSI28XZvDaGnxA4j7QI5loZYeyzGR9
 h70xQLVzqwwl1P0-F_0JaDFMJFO1yl4IexfpoZZsB3HhF2vFdL6D_lLeHRyH2g2OzF59eMIsM_Ccs4G47862w


.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Parametro
     - Descrizione
     - Valori ammessi
   * - **client_assertion**
     - JWT firmato con la chiave privata del Relying Party contenente gli stessi parametri documentati per le richieste al Token Endpoint.
     - L’OP deve verificare la validità di tutti i campi presenti nel JWT, nonché la validità della sua firma in relazione al parametro **client_id**.
   * - **client_assertion_type**
     - 
     - **urn:ietf:params:oauth:clientassertion-type:jwt-bearer**
   * - **client_id**
     - URI che identifica univocamente il RP come da Registro SPID. 
     - L’OP deve verificare che il client_id sia noto.
   * - **token**
     - Il token su cui il RP vuole ottenere informazioni.
     - 
	 

Response
++++++++

Il Revocation Endpoint risponde con un codice HTTP 200, anche nel caso in cui il token indicato non esista o sia già stato revocato (in modo da non rilasciare informazioni).


