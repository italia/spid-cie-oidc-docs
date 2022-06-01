Introspection Endpoint (verifica validità token) 
================================================

L’Introspection Endpoint esposto dall’OP consente ai RP di ottenere informazioni su un token in loro possesso, come ad esempio la sua validità.

**Riferimenti:**

.. code-block::

 - https://tools.ietf.org/html/rfc7662
 - https://openid.net/specs/openid-igov-oauth2-1_0-03.html#rfc.section.3.2.2

Request
+++++++

La richiesta all’Introspection Endpoint consiste nell’invio del token su cui si vogliono ottenere informazioni unitamente a una Client Assertion che consente di identificare il RP che esegue la richiesta.

**Esempio:**

.. code-block:: 

 POST https://op.spid.agid.gov.it/introspection?
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

L’Introspection Endpoint risponde con un oggetto JSON definito come segue. 

**Esempio:**

.. code-block:: 

 {
  "active": true,
  "scope": "foo bar",
  "exp": 1519033149,
  "sub": "OP-1234567890",
  "client_id": https://rp.agid.gov.it/
  "iss": "https://op.spid.agid.gov.it/",
  "aud": "https://rp.spid.agid.gov.it/auth",
 }

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Parametro
     - Descrizione
     - Valori ammessi
   * - **active**
     - Valore booleano che indica la validità del token. Se il token è scaduto, è revocato o non è mai stato emesso per il client_id chiamante, l’Introspection Endpoint deve restituire false.
     - 
   * - **scope**
     - Lista degli scope richiesti al momento dell’Authorization Request
     - 
   * - **exp**
     - Scadenza del token.
     - 
   * - **sub**
     - Identificatore del soggetto, coincidente con quello già rilasciato nell’ID Token 
     - Il RP deve verificare che il valore coincida con quello contenuto nell’ID Token.
   * - **client_id**
     - URI che identifica univocamente il RP come da Registro SPID. 
     - Il RP deve verificare che il valore coincida con il proprio client_id.
   * - **iss**
     - Identificatore dell’OP che lo contraddistingue univocamente nella federazione nel formato Uniform Resource Locator (URL).
     - Il client è tenuto a verificare che questo valore corrisponda all’OP chiamato.
   * - **aud**
     - Contiene il client ID.
     - Il client è tenuto a verificare che questo valore corrisponda al proprio client ID. 
	 
Errori
++++++

In caso di errore, l’OP restituisce un codice HTTP 401 con un JSON nel body avente gli elementi di seguito indicati

**Esempio:**

.. code-block:: 

 {
  "error": "invalid_client",
  "error_description: "client_id non riconosciuto."
 }

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Parametro
     - Descrizione
     - Valori ammessi
   * - **error**
     - Codice dell’errore (v. tabella sotto)
     - 
   * - **error_description**
     - Descrizione più dettagliata dell’errore, finalizzata ad aiutare lo sviluppatore per eventuale debugging. Questo messaggio non è destinato ad essere visualizzato all’utente (a tal fine si faccia riferimento alle Linee Guida UX SPID).
     - 

Di seguito i codici di errore:

.. list-table:: 
   :widths: 70 30
   :header-rows: 1

   * - Scenario
     - Codice errore
   * - Il client_id indicato nella richiesta non è riconosciuto.
     - **invalid_client**
   * - La richiesta non è valida a causa della mancanza o della non correttezza di uno o più parametri
     - **invalid_request**
   * - L’OP ha riscontrato un problema interno.
     - **server_error**
   * - L’OP ha riscontrato un problema interno temporaneo.
     - **temporarily_unavailable**

Eventuali ulteriori codici di errore possono essere definiti dall’Agenzia per l’Italia Digitale con
proprio atto. 

**Riferimenti:**

.. code-block:: 

 - https://tools.ietf.org/html/rfc7662#section-2.3

