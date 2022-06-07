.. include:: ./common_definitions.rst

Token Endpoint (richiesta token)
================================

Il Token Endpoint rilascia *access token, ID Token e refresh token*; vi sono due scenari distinti
in cui il client chiama il Token Endpoint:

 1. al termine del flusso di autenticazione descritto nel paragrafo precedente, il Client chiama il Token Endpoint inviando l’Authorization code ricevuto dall’OP (code=usDwMnEzJPpG5oaV8x3j) per ottenere un ID Token e un access token (necessario per poi chiedere gli attributi/claim allo UserInfo Endpoint) ed eventualmente un refresh token (se è stata avviata una `sessione lunga revocabile <https://www.agid.gov.it/sites/default/files/repository_files/spid-avviso-n41-integrazione_ll.gg_._openid_connect_in_spid.pdf#page=6>`_);

 2. in presenza di una `sessione lunga revocabile <https://www.agid.gov.it/sites/default/files/repository_files/spid-avviso-n41-integrazione_ll.gg_._openid_connect_in_spid.pdf#page=6>`_, il Client chiama il Token Endpoint inviando il refresh token in suo possesso per ottenere un nuovo access token.

.. seealso:: 

 * https://tools.ietf.org/html/rfc6749#section-3.2
 * https://openid.net/specs/openid-connect-core-1_0.html#TokenEndpoint
 * https://openid.net/specs/openid-igov-oauth2-1_0-03.html#rfc.section.2.1.2 
 * https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#rfc.section.2.2
 
Request
+++++++

L’unico metodo di autenticazione all’endpoint token previsto è il private_key_jwt (OIDC Connect Core 1.0 par. 9)

.. warning::
    |warning-message|

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

 - https://openid.net/specs/openid-connect-core-1_0.html#ClientAuthentication

**Esempio di richiesta con refresh token (caso 2):**

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
   :widths: 25 25 25 25
   :header-rows: 1

   * - Parametro
     - Descrizione
     - Valori ammessi
     - Obbligatorio
   * - **client_id**
     - URI che identifica univocamente il RP come da Registro SPID 
     - 
     - |check-icon|
   * - **client_assertion**
     - JWT firmato con la chiave privata del Relying Party contenente i seguenti parametri: 
	 
	 **iss**: Identificatore del RP registrato presso gli OP e che contraddistingue univocamente l’entità nella federazione nel formato Uniform Resource Locator (URL); corrisponde al client_id usato nella richiesta di autenticazione 
	 
	 **sub**: uguale al parametro **iss** 
	 
	 **aud**: URL del Token Endpoint dell’OP
	 
	 **iat**: data/ora in cui è stato rilasciato il JWT in formato NumericDate, come indicato in RFC 7519 JSON Web Token (JWT). 
	 
	 **exp**: data/ora di scadenza della request in formato NumericDate, come indicato in RFC 7519 – JSON Web Token (JWT). 
	 
	 **jti**: Identificatore univoco per questa richiesta di autenticazione, generato dal client casualmente con almeno 128bit di entropia.
     -
     - |check-icon|
   * - **client_assertion_type**
     -  
     - Deve assumere il seguente valore: **urn:ietf:params:oauth:client-assertion-type:jwtbearer**
     - |check-icon|
   * - **code**
     - Codice di autorizzazione restituito nell’Authentication response.
     - 
     - Solo se **grant_type** è **authorization_code**
   * - **code_verifier**
     - Codice di verifica del code_challenge 
     - 
     - Solo se **grant_type** è **authorization_code** 
   * - **grant_type**
     - Tipo di credenziale presentata dal Client per la richiesta corrente.
     - Può assumere uno dei seguenti valori: 
	 
	 **authorization_code** 
	 **refresh_token**
     - |check-icon|
   * - **refresh_token**
     -
     - 
     - Solo se **grant_type** è **refresh_code**   
 
 
Response
++++++++

Dopo avere ricevuto e validato la Token request dal client, il Token endpoint dell’OpenID Provider (OP) restituisce una response che include ID Token e Access Token e un eventuale Refresh Token, in formato JWT e firmati secondo le modalità definite dall’Agenzia per l’Italia Digitale.

L’Access Token deve essere formatosecondo le indicazioni dello standard “International Government Assurance Profile (iGov) for OAuth 2.0 - Draft 03”, paragrafo 3.2.1, “JWT Bearer Tokens”.

L’ID Token deve essere formato secondo le indicazioni del paragrafo successivo.

.. code-block:: 

 {
  "access_token": "dC34Pf6kdG...",
  "token_type": "Bearer",
  "refresh_token": "wJ848BcyLP...",
  "expires_in": 1800,
  "id_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY..."
 }
 
.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Parametro
     - Descrizione
     - Valori ammessi
   * - **access_token**
     - L’access token, in formato JWT firmato, consente l’accesso allo UserInfo endpoint per ottenere gli attributi.
     - 
   * - **token_type**
     - Tipo di *access token* restituito.
     - Deve essere valorizzato sempre con **Bearer**
   * - **refresh_token**
     - Il *refresh token*, in formato JWT firmato, consente di chiamare nuovamente il Token Endpoint per ottenere un nuovo *access token* e quindi recuperare una `sessione lunga revocabile <https://www.agid.gov.it/sites/default/files/repository_files/spid-avviso-n41-integrazione_ll.gg_._openid_connect_in_spid.pdf#page=6>`_.
     - 
   * - **expires_in**
     - Scadenza dell’*access token*, in secondi
     - Secondo le modalità definite dall’Agenzia per l’Italia Digitale.
   * - **id_token**
     - ID Token in formato JWT (v. paragrafo dedicato)
     - 
    

ID Token
++++++++

L’ID Token è un JSON Web Token (JWT) che contiene informazioni sull’utente che ha eseguito l’autenticazione. I Client devono eseguire la validazione dell’ID Token.

**Esempio di ID Token:**

.. code-block:: 

 {
  "iss": "https://op.spid.agid.gov.it/",
  "sub": "OP-1234567890",
  "aud": "https://rp.spid.agid.gov.it/auth",
  "acr": "https://www.spid.gov.it/SpidL2",
  "at_hash": "qiyh4XPJGsOZ2MEAyLkfWqeQ",
  "iat": 1519032969,
  "nbf": 1519032969,
  "exp": 1519033149,
  "jti": "nw4J0zMwRk4kRbQ53G7z",
  "nonce": "MBzGqyf9QytD28eupyWhSqMj78WNqpc2"
 }

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Parametro
     - Descrizione
     - Validazione
   * - **iss** 
     - Identificatore dell’OP che lo contraddistingue univocamente nella federazione nel formato Uniform Resource Locator (URL).
     - Il client è tenuto a verificare che questo valore corrisponda all’OP chiamato.
   * - **sub** 
     - Per il valore di questo parametro fare riferimento allo standard “OpenID Connect Core 1.0”, “Pairwise Identifier Algorithm”. 
     -
   * - **aud** 
     - Contiene il client ID. 
     - Il client è tenuto a verificare che questo valore corrisponda al proprio client ID.
   * - **acr** 
     - Livello di autenticazione effettivo. Può essere uguale o superiore a quello richiesto dal client nella Authentication Request.
     - 
   * - **at_hash** 
     - Hash dell’Access Token; il suo valore è la codifica base64url della prima metà dell’hash del valore access_token, usando l’algoritmo di hashing indicato in **alg** nell’header dell’ID Token.
     - Il client è tenuto a verificare che questo valore corrisponda all’*access token* restituito insieme all’ID Token.
   * - **iat** 
     - Data/ora di emissione del token in formato NumericDate, come indicato in RFC 7519 – JSON Web Token (JWT). 
     - 
   * - **nbf** 
     - Data/ora di inizio validità del token in formato NumericDate, come indicato in RFC 7519–JSON Web Token (JWT). Deve corrispondere con il valore di **iat**.
     - .. code-block:: 
	   
	   {
             userinfo: {...}
             id_token: {
               acr: {...},
               nbf: { essential: true },
               jti: { essential: true }
             }
	   } 
   * - **exp**
     - Data/ora di scadenza del token in formato NumericDate, come indicato in RFC 7519 – JSON Web Token (JWT), secondo le modalità definite dall’Agenzia per l’Italia Digitale.
     - 
   * - **jti** 
     - Identificatore unico dell’ID Token che il client più utilizzare per prevenirne il riuso, rifiutando l’ID Token se già processato. Deve essere di difficile individuazione da parte di un attaccante e composto da una stringa casuale.
     - 
   * - **nonce** 
     - Stringa casuale generata dal Client per ciascuna sessione utente ed inviata nell’Authentication Request (parametro nonce), finalizzata a mitigare attacchi replay.
     - Il client è tenuto a verificare che coincida con quella inviata  nell’Authentication Request.


.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#IDToken
 - https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#rfc.section.3.1


Errori
++++++

In caso di errore, l’OP restituisce una response con un JSON nel body costituito dai parametri indicati nella tabella sottostante.

**Esempio:**

.. code-block:: 

 {
  "error": "codice errore",
  "error_description: "descrizione dell’errore"
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
	
I codici di stato HTTP ed i valori dei parametri *error* e *error_description* sono descritti nelle tabelle relative ai messaggi di anomalia definiti dalle Linee Guida UX SPID.


.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-5.2
 - https://openid.net/specs/openid-connect-core-1_0.html#TokenErrorResponse
 
