.. include:: ../common/common_definitions.rst

Revocation Endpoint (logout)
----------------------------

Un RP PUÒ chiedere la revoca di un Access Token o di un Refresh Token emesso da un OP.

Quando l'utente esegue il logout il RP DEVE revocare l' Access Token in suo possesso.

.. note::
  La revoca di un Access Token comporta la revoca di tutti i Refresh Token a questo collegati.

L'OP DOVRÀ revocare il token specificato nella richiesta e DOVRÀ terminare la sessione di Single Sign-On se ancora attiva.

.. seealso::

 - https://tools.ietf.org/html/rfc7009
 
Request
+++++++

La richiesta al Revocation Endpoint consiste nell'invio del token che si vuole revocare unitamente a una Client Assertion che consente di identificare il RP che esegue la richiesta.


**Esempio:**

.. code-block::

 POST /revoke?
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

 Host: https://op.spid.agid.gov.it
 HTTP/1.1


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **client_assertion**
     - JWT firmato con la chiave privata del Relying Party contenente gli stessi parametri documentati per le richieste al 
       Token Endpoint. L'OP deve verificare la validità di tutti i campi presenti nel JWT, nonché la validità della sua firma in relazione al parametro **client_id**.
     - 
   * - **client_assertion_type**
     - String. **urn:ietf:params:oauth:clientassertion-type:jwt-bearer**
     - 
   * - **client_id**
     - URL HTTPS che identifica univocamente il RP. 
     - 
   * - **token**
     - Il token su cui il RP vuole ottenere informazioni.
     - 
	 

Response
++++++++

Il Revocation Endpoint risponde con un codice HTTP 200, anche nel caso in cui il token indicato non esista o sia già stato revocato (in modo da non rilasciare informazioni).


