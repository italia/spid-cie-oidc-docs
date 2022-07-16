.. include:: ./common_definitions.rst

Token Endpoint (richiesta token)
--------------------------------

Il Token Endpoint rilascia un *Access Token, un ID Token e un Refresh Token*. Il RP invia una richiesta al Token Endpoint:

 1. al termine del flusso di autenticazione descritto nel paragrafo precedente, inviando l'authorization code ricevuto dall'OP (esempio, code=usDwMnEzJPpG5oaV8x3j) per ottenere un ID Token e un Access Token ed eventualmente un Refresh Token (se è stata avviata una `sessione lunga revocabile`_)

 2. in presenza di una `sessione lunga revocabile`_, il RP chiama il Token Endpoint inviando il Refresh Token in suo possesso per ottenere un nuovo Access Token.

.. seealso:: 

 * https://tools.ietf.org/html/rfc6749#section-3.2
 * https://openid.net/specs/openid-connect-core-1_0.html#TokenEndpoint
 * https://openid.net/specs/openid-igov-oauth2-1_0-03.html#rfc.section.2.1.2 
 * https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#rfc.section.2.2
 
Request
+++++++

Il metodo di autenticazione del RP presso il token endpoint è il private_key_jwt (OIDC Connect Core 1.0 par. 9)


**Esempio di richiesta con authorization code (caso 1)**

.. code-block:: 

 POST /token?
 client_id=https://rp.spid.agid.gov.it&
 client_assertion=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiw
 ibmFtZSI6IlNQSUQiLCJhZG1pbiI6dHJ1ZX0.LVyRDPVJm0S9q7oiXcYVIIqGWY0wWQlqxvFGYswL…&
 client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwtbearer&
 code=usDwMnEzJPpG5oaV8x3j&
 code_verifier=9g8S40MozM3NSqjHnhi7OnsE38jklFv2&
 grant_type=authorization_code

 Host: https://op.spid.agid.gov.it
 HTTP/1.1


.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#RPAuthentication

**Esempio di richiesta con Refresh Token (caso 2):**

.. code-block:: 

 POST /token?
 client_id=https://rp.spid.agid.gov.it&
 client_assertion=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiw
 ibmFtZSI6IlNQSUQiLCJhZG1pbiI6dHJ1ZX0.LVyRDPVJm0S9q7oiXcYVIIqGWY0wWQlqxvFGYswL…&
 client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwtbearer&
 grant_type=refresh_token&
 refresh_token=8xLOxBtZp8

 Host: https://op.spid.agid.gov.it
 HTT/P1.1

 
.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **client_id**
     - URI che identifica univocamente il RP. 
     - |spid-icon| |cieid-icon|
   * - **client_assertion**
     - JWT firmato con la chiave privata del Relying Party contenente i seguenti parametri: 
	 
	 **iss**: Identificatore del RP registrato presso gli OP e che contraddistingue univocamente l'entità nella Federazione nel formato Uniform Resource Locator (URL). Corrisponde al client_id usato nella richiesta di autenticazione 
	 
	 **sub**: uguale al parametro **iss** 
	 
	 **aud**: URL del Token Endpoint dell'OP
	 
	 **iat**: UNIX Timestamp con l'istante di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`. 
	 
	 **exp**: UNIX Timestamp con l'istante di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`
	 
	 **jti**: Identificatore univoco uuid4 per questa richiesta di autenticazione, generato dal client.
     - |spid-icon| |cieid-icon|
   * - **client_assertion_type**
     - Deve assumere il seguente valore: |br|
       **urn:ietf:params:oauth:client-assertion-type:jwtbearer**
     - |spid-icon| |cieid-icon|
   * - **code**
     - Codice di autorizzazione restituito nell'Authentication response. Obbligatorio solo se **grant_type** è **authorization_code**
     - |spid-icon| |cieid-icon|
   * - **code_verifier**
     - Codice di verifica del code_challenge. Obbligatorio solo se **grant_type** è **authorization_code** 
     - |spid-icon| |cieid-icon|
   * - **grant_type**
     - Tipo di credenziale presentata dal RP per la richiesta corrente.
       Può assumere uno dei seguenti valori: 
	 
	   - **authorization_code**
	   - **refresh_token**

     - |spid-icon| |cieid-icon|
   * - **refresh_token**
     - Obbligatorio solo se **grant_type** è **refresh_code**   
     - |spid-icon| |cieid-icon|
 
 
Response
++++++++

L'OpenID Provider (OP) restituisce un ID Token e Access Token e un eventuale Refresh Token, in formato JWT firmato.

L'Access Token deve essere formato secondo le indicazioni dello standard "International Government Assurance Profile (iGov) for OAuth 2.0 - Draft 03", paragrafo 3.2.1, "JWT Bearer Tokens".

L'ID Token deve essere formato secondo le indicazioni del paragrafo successivo.

.. code-block:: 

 {
     "access_token":"dC34Pf6kdG...",
     "token_type":"Bearer",
     "refresh_token":"wJ848BcyLP...",
     "expires_in":1800,
     "id_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY..."
 }
 
.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **access_token**
     - L'Access Token, in formato JWT firmato, consente l'accesso allo UserInfo endpoint per ottenere gli attributi.
     - |spid-icon| |cieid-icon|
   * - **token_type**
     - Tipo di *Access Token* restituito. Deve essere valorizzato sempre con **Bearer**
     - |spid-icon| |cieid-icon|
   * - **refresh_token**
     - Il *Refresh Token*, in formato JWT firmato, consente di chiamare nuovamente il Token Endpoint per ottenere un nuovo *Access Token* e quindi recuperare una `sessione lunga revocabile`_.
     - |spid-icon| |cieid-icon|
   * - **expires_in**
     - Scadenza dell'*Access Token* in secondi.
     - |spid-icon| |cieid-icon|
   * - **id_token**
     - ID Token in formato JWT (v. paragrafo successivo)
     - |spid-icon| |cieid-icon|


ID Token
++++++++

L'ID Token è un JSON Web Token (JWT) che contiene informazioni sull'utente che ha eseguito l'autenticazione. I RP devono eseguire la validazione dell'ID Token.

**Esempio di ID Token:**

.. code-block:: 

 {
     "iss":"https://op.spid.agid.gov.it/",
     "sub":"OP-1234567890",
     "aud":"https://rp.spid.agid.gov.it/auth",
     "acr":"https://www.spid.gov.it/SpidL2",
     "at_hash":"qiyh4XPJGsOZ2MEAyLkfWqeQ",
     "iat":1519032969,
     "nbf":1519032969,
     "exp":1519033149,
     "jti":"nw4J0zMwRk4kRbQ53G7z",
     "nonce":"MBzGqyf9QytD28eupyWhSqMj78WNqpc2"
 }


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **iss** 
     - Identificatore dell'OP che lo contraddistingue univocamente nella Federazione nel formato Uniform Resource Locator (URL). Il client è tenuto a verificare che questo valore corrisponda all'OP chiamato.
     - |spid-icon| |cieid-icon|
   * - **sub** 
     - Per il valore di questo parametro fare riferimento allo standard "OpenID Connect Core 1.0", "Pairwise Identifier Algorithm". 
     - |spid-icon| |cieid-icon|
   * - **aud** 
     - Contiene il client ID. Il client è tenuto a verificare che questo valore corrisponda al proprio client ID.
     - |spid-icon| |cieid-icon|
   * - **acr** 
     - Livello di autenticazione effettivo. Può essere uguale o superiore a quello richiesto dal client nella Authentication Request.
     - |spid-icon| |cieid-icon|
   * - **at_hash** 
     - Hash dell'Access Token. Il suo valore è la codifica base64url della prima metà dell'hash del valore access_token, usando l'algoritmo di hashing indicato in **alg** nell'header dell'ID Token. Il client è tenuto a verificare che questo valore corrisponda all'*Access Token* restituito insieme all'ID Token.
     - |spid-icon| |cieid-icon|
   * - **iat** 
     - UNIX Timestamp con l'istante di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **nbf** 
     - UNIX Timestamp. Data/ora di inizio validità del JWT in formato NumericDate, come indicato in :rfc:`7519`. Deve corrispondere con il valore di **iat**.

       .. code-block:: 
	   
	    {
              userinfo: {...}
              id_token: {
                acr: {...},
                nbf: { essential: true },
                jti: { essential: true }
              }
	    } 
     - |spid-icon| |cieid-icon|
   * - **exp**
     - UNIX Timestamp con l'istante di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **jti** 
     - String. Identificatore unico dell'ID Token che il client può utilizzare per prevenirne il riuso, rifiutando l'ID Token se già processato. Deve essere di difficile individuazione da parte di un attaccante e composto da una stringa casuale. Si consiglia l'utilizzo del generatore *uuid4*
     - |spid-icon| |cieid-icon|
   * - **nonce** 
     - String. Stringa casuale generata dal RP per ciascuna sessione utente ed inviata nell'Authentication Request (parametro nonce), finalizzata a mitigare attacchi replay. Il client è tenuto a verificare che coincida con quella inviata nell'Authentication Request.
     - |spid-icon| |cieid-icon|


.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#IDToken
 - https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#rfc.section.3.1


Errori
++++++

In caso di errore, l'OP restituisce una response con un JSON nel body costituito dai parametri indicati nella tabella sottostante.

**Esempio:**

.. code-block:: 

 {
     "error":"codice errore",
     "error_description":"descrizione dell'errore"
 }


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **error** 
     - Codice dell'errore (v. tabella sotto)
     - |spid-icon| |cieid-icon|
   * - **error_description** 
     - Descrizione più dettagliata dell'errore, finalizzata ad aiutare lo sviluppatore per eventuale debugging. Questo messaggio non è destinato ad essere visualizzato all'utente (a tal fine si faccia riferimento alle `Linee Guida UX SPID`_).
     - |spid-icon| |cieid-icon|
	
I codici di stato HTTP ed i valori dei parametri *error* e *error_description* sono descritti nelle tabelle relative ai messaggi di anomalia.


.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-5.2
 - https://openid.net/specs/openid-connect-core-1_0.html#TokenErrorResponse
 
