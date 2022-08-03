.. include:: ../common/common_definitions.rst

Token Endpoint (richiesta token)
--------------------------------

Al termine del flusso di autenticazione descritto nel paragrafo precedente, il RP invia una richiesta al Token Endpoint inviando l'authorization code ricevuto dall'OP per ottenere un *ID Token* e un *Access Token* ed eventualmente un *Refresh Token* (se è stata avviata una `sessione lunga revocabile`_). 

In presenza di una `sessione lunga revocabile`_, il RP PUÒ chiamare il Token Endpoint inviando il *Refresh Token* in suo possesso per ottenere un nuovo *Access Token* e *ID Token*.

.. note::
  Il metodo di autenticazione del RP presso il token endpoint è il **private_key_jwt** (`OpenID.Core#ClientAuthentication`_).


.. seealso:: 

 * https://tools.ietf.org/html/rfc6749#section-3.2
 * https://openid.net/specs/openid-connect-core-1_0.html#TokenEndpoint
 * https://openid.net/specs/openid-igov-oauth2-1_0-03.html#rfc.section.2.1.2 
 * https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#rfc.section.2.2
 
Request
+++++++

Di seguito i claim che DEVONO essere inseriti nella *Token Request*.

.. TODO: move examples in the specific section

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
     - Vedi `OpenID.Registration`_. DEVE essere valorizzato con un HTTPS URL che identifica univocamente il RP. 
     - |spid-icon| |cieid-icon|
   * - **client_assertion**
     - JWT firmato con la chiave privata del Relying Party contenente i seguenti parametri: 
	 
	 **iss**: DEVE corrispondere al valore *client_id* 
	 
	 **sub**: DEVE corrispondere al valore *iss* 
	 
	 **aud**: URL del Token Endpoint dell'OP
	 
	 **iat**: UNIX Timestamp con l'istante di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`. 
	 
	 **exp**: UNIX Timestamp con l'istante di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`
	 
	 **jti**: Identificatore univoco per questa richiesta di autenticazione, generato dal client. Ad esempio in formato *uuid4*.
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
       PUÒ assumere uno dei seguenti valori: 
	 
	   - **authorization_code**
	   - **refresh_token**

     - |spid-icon| |cieid-icon|
   * - **refresh_token**
     - Obbligatorio solo se **grant_type** è **refresh_code**   
     - |spid-icon| |cieid-icon|
 
 
Response
++++++++

L'OpenID Provider (OP) restituisce un ID Token e Access Token e un eventuale Refresh Token, in formato JWT firmato.

L'Access Token deve essere formato secondo le indicazioni dello standard `"International Government Assurance Profile (iGov) for OAuth 2.0 - Draft 03", section 3.2.1, "JWT Bearer Tokens" <https://openid.net/specs/openid-igov-oauth2-1_0-03.html#rfc.section.3.2.1>`_.

L'ID Token deve essere formato secondo le indicazioni del paragrafo successivo.

La risposta DEVE contenere i seguenti claim.

.. TODO: Move examples in the specific section
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
     - Tipo di *Access Token* restituito. DEVE essere valorizzato sempre con **Bearer**
     - |spid-icon| |cieid-icon|
   * - **refresh_token**
     - Disponibile sono nel caso di `sessione lunga revocabile`_. Il *Refresh Token*, in formato JWT firmato, consente di chiamare nuovamente il Token Endpoint per ottenere un nuovo *Access Token* e un nuovo *ID Token*.
     - |spid-icon| |cieid-icon|
   * - **expires_in**
     - Scadenza dell'*Access Token* in secondi.
     - |spid-icon| |cieid-icon|
   * - **id_token**
     - ID Token in formato JWT (vedi paragrafo successivo)
     - |spid-icon| |cieid-icon|


ID Token
++++++++

L'ID Token è un JSON Web Token (JWT) che contiene informazioni sull'utente che ha eseguito l'autenticazione. I RP DEVONO eseguire la validazione dell'ID Token.
Di seguito i claim disponibili nell'ID Token.

.. TODO: Move examples in the specific section
  **Esempio di ID Token:**

  .. code-block:: 

  {
      "iss":"https://op.spid.agid.gov.it/",
      "sub":"9sd798asd98asui23hiuds89y798sfyg",
      "aud":"https://rp.spid.example.it/auth",
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
     - DEVE essere valorizzato con un HTTPS URL che identifica univocamente l'OP. Il client DEVE verificare che questo valore corrisponda all'OP chiamato.
     - |spid-icon| |cieid-icon|
   * - **sub** 
     - Vedi `OpenID.Core#SubjectIDTypes`_. DEVE essere di tipo *pairwise*.  
     - |spid-icon| |cieid-icon|
   * - **aud** 
     - DEVE coincidere con il valore *client_id*. Il RP DEVE verificare che questo valore corrisponda al proprio client ID.
     - |spid-icon| |cieid-icon|
   * - **acr** 
     - Livello di autenticazione effettivo. PUÒ essere uguale o superiore a quello richiesto dal RP nella Authentication Request.
     - |spid-icon| |cieid-icon|
   * - **at_hash** 
     - Vedi `OpenID.Core#CodeIDToken`_. Il client DEVE verificare che questo valore corrisponda all'*Access Token* restituito insieme all'ID Token.
     - |spid-icon| |cieid-icon|
   * - **iat** 
     - UNIX Timestamp con l'istante di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **nbf** 
     - UNIX Timestamp. Istante di inizio validità del JWT in formato NumericDate, come indicato in :rfc:`7519`. DEVE corrispondere con il valore di **iat**.
     - |spid-icon| 
   * - **exp**
     - UNIX Timestamp con l'istante di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **jti** 
     - DEVE essere una Stringa in formato *uuid4*. Identificatore unico dell'ID Token che il RP PUÒ utilizzare per prevenirne il riuso, rifiutando l'ID Token se già processato.
     - |spid-icon| |cieid-icon|
   * - **nonce** 
     - Vedi `OpenID.Core#AuthRequest`_. DEVE essere una stringa casuale di almeno 32 caratteri alfanumerici. Questo valore DEVE coincidere con quello inviato dal RP nella richiesta di autenticazione.
     - |spid-icon| |cieid-icon|


.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#IDToken
 - https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#rfc.section.3.1


