.. include:: ./common_definitions.rst

Authentication response
-----------------------

Un'Authentication response è un messaggio di risposta di autorizzazione OAuth 2.0
restituito dall'authorization endpoint dell'OpenID Provider (OP) al termine del flusso di
autenticazione. L'OP reindirizzerà l'utente al redirect_uri specificato nella richiesta di
autorizzazione, aggiungendo i parametri della risposta.

.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-4.1.2
 - https://openid.net/specs/openid-connect-core-1_0.html#AuthRequestValidation

Response
++++++++

Se l'autenticazione è avvenuta con successo, l'OpenID Provider (OP),
reindirizza l'utente con i seguenti parametri:


.. code-block:: 

 GET /resp?
 code=usDwMnEzJPpG5oaV8x3j&
 state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd

 Host: https://rp.spid.agid.gov.it
 HTTP/1.1


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **code**
     - codice univoco di autorizzazione (*Authorization Code*) che il client può passare al Token Endpoint per ottenere un ID Token e un Access Token. Questo ha il vantaggio di non esporre alcun token allo User Agent o a malware che accedono allo User Agent. 
     - 
   * - **state**
     - Valore state incluso nell'*Authentication Request*. Il client è tenuto a verificarne la corrispondenza. Deve essere lo stesso valore indicato dal client nella Authorization Request.
     - 


Errori
++++++

In caso di errore, l'OP visualizza i messaggi di anomalia relativi agli scambi OpenID
Connect descritti nelle relative tabelle definite dalle `Linee Guida UX SPID`_. Nei casi in cui tali linee
guida prescrivono un redirect dell'utente verso il RP, l'OP effettua il redirect verso l'URL indicata
nel parametro redirect_uri della richiesta (solo se valido, ovvero presente nel client metadata), con
i seguenti parametri.

**Esempio:**

.. code-block:: 

 GET /resp?
 error=invalid_request&
 error_description=request%20malformata&
 state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd

 Host: https://rp.spid.agid.gov.it
 HTTP/1.1


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **error**
     - Codice dell'errore
     - 
   * - **error_description**
     - Descrizione più dettagliata dell'errore, finalizzata ad aiutare lo sviluppatore per eventuale debugging. Questo messaggio non è 
       destinato ad essere visualizzato all'utente (a tal fine si faccia riferimento alle `Linee Guida UX SPID`_
     - 
   * - **state**
     - Valore *state* incluso nella Authentication Request.  Il client è tenuto a verificare che corrisponda a quello inviato nella Authentication Request.
     - 


.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-4.1.2.1



