.. include:: ../common/common_definitions.rst

Introspection Endpoint (verifica validità token) 
------------------------------------------------

L'Introspection Endpoint esposto dall'OP consente ai RP di ottenere informazioni su un token in loro possesso, come ad esempio la sua validità.

.. seealso::

 - https://tools.ietf.org/html/rfc7662
 - https://openid.net/specs/openid-igov-oauth2-1_0-03.html#rfc.section.3.2.2

Request
+++++++

La richiesta all'Introspection Endpoint consiste nell'invio del token su cui si vogliono ottenere informazioni unitamente a una Client Assertion che consente di autenticare il RP che esegue la richiesta.


**Esempio:**

.. code-block:: 

 POST /introspection?
 client_assertion=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiw
 ibmFtZSI6IlNQSUQiLCJhZG1pbiI6dHJ1ZX0.LVyRDPVJm0S9q7oiXcYVIIqGWY0wWQlqxvFGYswLF88…
 &
 client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwtbearer&
 client_id=https%3A%2F%2Frp.spid.agid.gov.it&
 token=eyJhbGciOiJSUzI1NiJ9.eyJleHAiOjE0MTg3MDI0MTQsImF1ZCI6WyJlNzFmYjcyYS05NzRmLT
 QwMDEtYmNiNy1lNjdjMmJjMDAzN2YiXSwiaXNzIjoiaHR0cHM6XC9cL2FzLXZhLmV4YW1wbGUuY29tXC8
 iLCJqdGkiOiIyMWIxNTk2ZC04NWQzLTQzN2MtYWQ4My1iM2YyY2UyNDcyNDQiLCJpYXQiOjE0MTg2OTg4
 MTR9.FXDtEzDLbTHzFNroW7w27RLk5m0wprFfFH7h4bdFw5fR3pwiqejKmdfAbJvN3_yfAokBv06we5RA
 RJUbdjmFFfRRW23cMbpGQCIk7Nq4L012X_1J4IewOQXXMLTyWQQ_BcBMjcW3MtPrY1AoOcfBOJPx1k2jw
 RkYtyVTLWlff6S5gKciYf3b0bAdjoQEHd_IvssIPH3xuBJkmtkrTlfWR0Q0pdpeyVePkMSI28XZvDaGnxA4j7QI5loZYeyzGR9
 h70xQLVzqwwl1P0-F_0JaDFMJFO1yl4IexfpoZZsB3HhF2vFdL6D_lLeHRyH2g2OzF59eMIsM_Ccs4G47862w…

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
     - String. Valori ammessi: **urn:ietf:params:oauth:clientassertion-type:jwt-bearer**
     - 
   * - **client_id**
     - URI che identifica univocamente il RP. L'OP deve verificare che il client_id sia noto all'interno della Federazione.
     - 
   * - **token**
     - Il token su cui il RP vuole ottenere informazioni.
     - 


Response
++++++++

L'Introspection Endpoint risponde con un oggetto JSON definito come segue. 

**Esempio:**

.. code-block:: 

 {
     "active":true
 }

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **active**
     - Valore booleano che indica la validità del token. Se il token è scaduto, è revocato o non è mai stato emesso per il client_id chiamante, l'Introspection Endpoint deve restituire false.
     - 
