.. include:: ../common/common_definitions.rst

.. _Revocation_Endpoint:

Revocation Endpoint
-------------------

Un RP PUÒ chiedere la revoca di un Access Token o di un Refresh Token emesso da un OP.

L'OP DEVE revocare il token specificato nella richiesta.

.. admonition:: |spid-icon|

  Quando l'utente esegue il logout o quando la sua sessione presso il RP scade (in base alle policy decise da quest'ultimo) il RP DEVE richiedere la revoca dell’Access Token e dell’eventuale Refresh Token in suo possesso, se questi non fossero già scaduti.

  .. note::
    La revoca di un Access Token comporta la revoca di tutti i Refresh Token non ancora scaduti a questo collegati.

  L'OP DEVE revocare il token specificato nella richiesta e DEVE terminare la sessione di Single Sign-On se ancora attiva. Eventuali altri token attivi per l’utente dovranno invece essere mantenuti validi.

.. admonition:: |cieid-icon|
  
  La revoca di un Access Token NON DEVE comportare la revoca di tutti i Refresh Token a questo collegati.

  La revoca di un Refresh Token DEVE comportare la revoca di tutti gli Access Token a questo collegati.

.. note::
  Il metodo di autenticazione del RP presso il *revocation endpoint* DEVE essere **private_key_jwt** (vedi il parametro *revocation_endpoint_auth_methods_supported* nella Sezione :ref:`Metadata OP <MetadataOP>`)


.. seealso::

 - https://tools.ietf.org/html/rfc7009
 
Request
+++++++

La richiesta al Revocation Endpoint consiste nell'invio del token che si vuole revocare unitamente a una Client Assertion che consente di identificare il RP che esegue la richiesta.


**Esempio:**

.. code-block:: http

 POST /revoke HTTP/1.1
 Host: https://op.spid.agid.gov.it
 Content-Type: application/x-www-form-urlencoded

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
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **client_assertion**
     - JWT firmato con la chiave privata OIDC del Relying Party contenente gli stessi parametri inseriti in fase di richiesta al Token Endpoint. L'OP deve verificare la validità di tutti i campi presenti nel JWT, nonché la validità della sua firma in relazione al parametro **client_id**.
     - |spid-icon| |cieid-icon|
   * - **client_assertion_type**
     - String. **urn:ietf:params:oauth:clientassertion-type:jwt-bearer**
     - |spid-icon| |cieid-icon|
   * - **client_id**
     - URL HTTPS che identifica univocamente il RP. 
     - |spid-icon| |cieid-icon|
   * - **token**
     - Il token che il RP chiede di revocare.
     - |spid-icon| |cieid-icon|
	 

Response
++++++++

Il Revocation Endpoint risponde con un codice HTTP 200, anche nel caso in cui il token indicato non esista o sia già stato revocato (in modo da non rilasciare informazioni).


Codici di errore
++++++++++++++++

Come definiti per :ref:`Token endpoint<TOKEN_ENDPOINT_ERRORS>`.
