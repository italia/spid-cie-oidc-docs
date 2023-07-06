.. include:: ../common/common_definitions.rst

Token Endpoint
--------------

Al termine del flusso di autenticazione descritto nel paragrafo precedente, il RP invia una richiesta al Token Endpoint inviando l'authorization code ricevuto dall'OP per ottenere un *ID Token* e un *Access Token* ed eventualmente un *Refresh Token* (se è stata effettuata una richiesta di autenticazione con *scope=offline_access* e *prompt=consent*. Vedi la Sezione :ref:`Refresh Token <Refresh_Token>`). 

I token restituiti devono essere JWT firmati.

.. admonition:: |spid-icon|

  In presenza di una `sessione lunga revocabile`_, il RP PUÒ chiamare il Token Endpoint inviando il *Refresh Token* in suo possesso per ottenere un nuovo *Access Token* e *ID Token*.

.. note::
  Il metodo di autenticazione del RP presso il token endpoint è il **private_key_jwt** (`OpenID.Core#ClientAuthentication`_).


.. seealso:: 

  * https://tools.ietf.org/html/rfc6749#section-3.2
  * https://openid.net/specs/openid-connect-core-1_0.html#TokenEndpoint
  * https://openid.net/specs/openid-igov-oauth2-1_0-03.html#Section-2.1.2 
  * https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#Section-2.2


Request
+++++++

Di seguito i claim che DEVONO essere inseriti nella *Token Request*.


**Esempio di richiesta con authorization code (caso 1)**

  .. code-block:: json

    POST /token HTTP/1.1
    Host: https://op.spid.agid.gov.it
    Content-Type: application/x-www-form-urlencoded

    client_id=https://rp.spid.agid.gov.it&
    client_assertion=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiw
    ibmFtZSI6IlNQSUQiLCJhZG1pbiI6dHJ1ZX0.LVyRDPVJm0S9q7oiXcYVIIqGWY0wWQlqxvFGYswL…&
    client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwtbearer&
    code=usDwMnEzJPpG5oaV8x3j&
    code_verifier=9g8S40MozM3NSqjHnhi7OnsE38jklFv2&
    grant_type=authorization_code

.. seealso::

  - https://openid.net/specs/openid-connect-core-1_0.html#RPAuthentication


**Esempio di richiesta con Refresh Token (caso 2):**

  .. code-block:: json

    POST /token HTTP/1.1
    Host: https://op.spid.agid.gov.it
    Content-Type: application/x-www-form-urlencoded
    
    client_id=https://rp.spid.agid.gov.it&
    client_assertion=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiw
    ibmFtZSI6IlNQSUQiLCJhZG1pbiI6dHJ1ZX0.LVyRDPVJm0S9q7oiXcYVIIqGWY0wWQlqxvFGYswL…&
    client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwtbearer&
    grant_type=refresh_token&
    refresh_token=8xLOxBtZp8


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
     - Obbligatorio solo se **grant_type** è **refresh_token**   
     - |spid-icon| |cieid-icon|
 
 
Response
++++++++

L'OpenID Provider (OP) restituisce un ID Token e Access Token e un eventuale Refresh Token, in formato JWT firmato.

L'Access Token deve essere formato secondo le indicazioni dello standard `"International Government Assurance Profile (iGov) for OAuth 2.0 - Draft 03", section 3.2.1, "JWT Bearer Tokens" <https://openid.net/specs/openid-igov-oauth2-1_0-03.html#Section-3.2.1>`_.

L'ID Token deve essere formato secondo le indicazioni del paragrafo successivo.

La risposta DEVE contenere i seguenti claim.

**Esempio di risposta:**

.. code-block:: http

  HTTP/1.1 200 OK
  Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
  Content-Type: application/json

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

Access Token
++++++++++++

L'Access Token è un JSON Web Token (JWT) firmato che consente l'accesso allo
UserInfo endpoint per ottenere gli attributi dell'utente. 
Di seguito i claim che compongono l'Access Token.

**Esempio del contenuto di intestazione di payload di un Access Token:**

.. code-block:: json

  {
    "alg": "RS256",
    "kid": "dB67gL7ck3TFiIAf7N6_7SHvqk0MDYMEQcoGGlkUAAw",
    "typ": "at+jwt"
  }
  .
  {
    "iss":"https://op.spid.agid.gov.it/",
    "sub": "9sd798asd98asui23hiuds89y798sfyg",
    "aud": [
    "https://rp.spid.example.it"
    ],
    "client_id": "https://rp.spid.example.it",
    "scope": "openid",
    "jti": "9ea42af0-594c-4486-9602-8a1f8dde42d3",
    "exp": 1656859559,
    "iat": 1656857579
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
   * - **client_id** 
     - DEVE essere valorizzato con un HTTPS URL che identifica univocamente il RP.  
     - |spid-icon| |cieid-icon|
   * - **aud** 
     - DEVE coincidere con il valore *client_id*. Il RP DEVE verificare che questo valore corrisponda al proprio client ID.
     - |spid-icon| |cieid-icon|
   * - **scope** 
     - L'OP DOVREBBE inserire il parametro *scope* come previsto in :rfc:`9068` Sezione 2.2.3. DEVE coincidere con il valore presente in fase di richiesta di autenticazione.
     - |spid-icon| |cieid-icon|
   * - **iat** 
     - UNIX Timestamp con l'istante di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **exp**
     - UNIX Timestamp con l'istante di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **jti** 
     - DEVE essere una Stringa in formato *uuid4*. Identificatore unico dell'ID Token che il RP PUÒ utilizzare per prevenirne il riuso, rifiutando l'ID Token se già processato.
     - |spid-icon| |cieid-icon|


ID Token
++++++++

L'ID Token è un JSON Web Token (JWT) firmato che contiene informazioni sull'utente che ha eseguito l'autenticazione. I RP DEVONO eseguire la validazione dell'ID Token.

.. admonition:: |cieid-icon|

  Il RP PUÒ richiedere che L'ID Token sia cifrato (vedere il parametro *id_token_encrypted_response_alg* nel :ref:`Metadata RP <MetadataRP>` ). 
  Se il RP inserisce nel suo metadata il parametro id_token_encrypted_response_alg, l'OP DEVE restituire l'ID Token **firmato e cifrato**. L'ID Token in formato JWT DEVE contenere il parametro *cty* (Content-Type) nell'intestazione JOSE con il valore *JWT* (vedere :rfc:`7519#section-5.2`).

Di seguito i claim disponibili nell'ID Token.

 **Esempio del contenuto di intestazione e di payload di un ID Token:**

.. code-block:: json

  {
    "alg": "RS256",
    "kid": "dB67gL7ck3TFiIAf7N6_7SHvqk0MDYMEQcoGGlkUAAw"
  }
  .
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
     - Livello di autenticazione effettivo. DEVE essere uguale o superiore a quello richiesto dal RP nella Authentication Request.
     - |spid-icon| |cieid-icon|
   * - **at_hash** 
     - Vedi `OpenID.Core#CodeIDToken`_. Il suo valore è la codifica base64url della prima metà dell'hash calcolato sulla rappresentazione ASCII dell'*Access Token*, usando l'algoritmo di hashing indicato in **alg** nell'header dell'ID Token. Il client DEVE verificare che questo valore corrisponda applicando la medesima funzione all'*Access Token* restituito insieme all'ID Token.
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
 - https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#Section-3.1

.. _Refresh_Token:

Refresh Token
+++++++++++++

Il *Refresh Token* è un JWT che PUÒ essere rilasciato dall'OP e che PUÒ essere usato per ottenere un nuovo *Access Token* che abilita il RP ad accedere allo *UserInfo endpoint* senza interazione diretta dell'utente. 

Il *Refresh Token* DEVE essere rilasciato in formato JWT, firmato, e contenere almeno i seguenti parametri.

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **iss** 
     - DEVE essere valorizzato con un HTTPS URL che identifica univocamente l'OP. Il RP DEVE verificare che questo valore corrisponda all'OP chiamato.
     - |spid-icon| |cieid-icon|
   * - **aud** 
     - DEVE coincidere con il valore *client_id*. Il RP DEVE verificare che questo valore corrisponda al proprio client ID.
     - |spid-icon| |cieid-icon|
   * - **iat** 
     - UNIX Timestamp con l'istante di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **exp**
     - UNIX Timestamp con l'istante di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon|
   * - **jti** 
     - DEVE essere una Stringa in formato *uuid4*. Identificatore unico del *Refresh Token* che il RP PUÒ utilizzare per prevenirne il riuso, rifiutando il *Refresh Token* se già processato.
     - |spid-icon| |cieid-icon|

.. admonition:: |cieid-icon|

  Per ottenere un *Refresh Token*, il RP DEVE includere nel parametro *scope* della richiesta di autenticazione il valore *offline_access* e nel parametro *prompt* il valore *consent*. L'utilizzo di questo *scope* può essere utile in scenari nei quali un RP ha la necessità di verificare che l'identità digitale di un utente finale sia ancora valida o vuole mantenere aggiornati gli attributi che ha precedentemente raccolto durante la fase di autenticazione, ad esempio per l'invio di notifiche all'utente finale successive all'autenticazione dello stesso.
  **Il Refresh Token NON DEVE consentire al RP richiedente di ottenere un ID Token, nè quello precedentemente rilasciato in fase di autenticazione nè un nuovo ID Token. L'utilizzo del Refresh Token NON DEVE essere utilizzato dagli RP per ottenere una nuova autenticazione dell'utente con l'OP o rinnovare una sessione preesistente, ma PUÒ essere utilizzato come meccanismo per ottenere dallo UserInfo endpoint esclusivamente il medesimo set di attributi dell'utente richiesti in fase di autenticazione iniziale e per il quale l'utente ha espresso il consenso esplicito.** Tale consenso DEVE essere raccolto dall'OP in fase autenticazione dell'utente finale nella pagina di consenso. L'utente finale DEVE avere la possibilità di abilitare o disabilitare questa opzione prima di inviare il consenso che PUÒ essere soggetto ad un periodo di validità se definito dall'OP in base alle policy sul trattamento dei dati personali. 

  L'OP che riceve una richiesta di un nuovo *Access Token* tramite un *Refresh Token* PUÒ inviare una notifica all'utente tramite uno dei recapiti digitali disponibili (email, sms, notifica mobile app). L'utente che non riconosce legittima questa operazione o che vuole disabilitare questa opzione PUÒ richiedere all'OP una revoca del consenso dato (e quindi dei token emessi a seguito dello stesso) secondo le modalità rese note all'interno della pagina di raccolta del consenso. La notifica DEVE avere solo carattere informativo e non autorizzativo. All'interno della notifica DEVE essere reso noto all'utente le modalità di revoca del consenso dato. L'OP DEVE consentire all'utente di disabilitare in qualsiasi momento questa opzione tramite apposita funzionalità messa a disposizione dall'OP stesso.

  Per ragioni di sicurezza, un OP DEVE restituire, insieme ad un nuovo *Access Token*, anche un nuovo *Refresh Token*, invalidando tutti i token precedentemente rilasciati (*refresh token rotation*) al RP e in relazione al soggetto interessato (utente finale). Il nuovo *Refresh Token* DEVE avere il parametro *exp* non superiore alla durata prevista. 

.. admonition:: |spid-icon|

  Per applicazioni mobili in cui il RP intenda offrire un'esperienza utente che non richieda il reinserimento delle credenziali SPID ad ogni utilizzo dell'applicazione, si POSSONO utilizzare le sessioni lunghe revocabili utilizzando il Refresh Token come normato nelle `LL.GG. OpenID Connect in SPID <https://www.agid.gov.it/sites/default/files/repository_files/linee_guida_openid_connect_in_spid.pdf>`_ e nell' `Avviso n.41 <https://www.agid.gov.it/sites/default/files/repository_files/spid-avviso-n41-integrazione_ll.gg_._openid_connect_in_spid.pdf>`_ .
  Il *Token endpoint* verifica la validità del Refresh Token e, se nella richiesta di autenticazione originaria era presente nell' *acr_values* il valore *https://www.spid.gov.it/SpidL1*, rilascia un nuovo *ID Token* valido esclusivamente per il livello 1 SPID.
  Per maggiori dettagli sull'utilizzo del Refresh Token nel contesto SPID, si vedano i seguenti documenti normativi: 
  
    - `LL.GG. OpenID Connect in SPID <https://www.agid.gov.it/sites/default/files/repository_files/linee_guida_openid_connect_in_spid.pdf>`_
    - `Avviso n.41 - Integrazione LL.GG. OpenID Connect in SPID <https://www.agid.gov.it/sites/default/files/repository_files/spid-avviso-n41-integrazione_ll.gg_._openid_connect_in_spid.pdf>`_ 

  


Periodo di validità di un Refresh Token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il *Refresh Token* NON DEVE avere una validità (differenza tra *iat* e *exp*) superiore a 30 giorni. 

Se allo scadere del periodo di validità l'RP effettua una richiesta all'OP, quest'ultimo DEVE restituire un errore nella risposta (Vedi :ref:`Codici di Errore <codici_errore>`).

.. admonition:: |cieid-icon|

  Fermo restando la validità del token, l'OP PUÒ fissare un periodo di validità relativo al consenso che l'utente ha fornito all'utilizzo dello *scope* *offline_access* e del *Refresh Token*. In prossimità del termine di validità del consenso, qualora tale termine sia previsto nelle policy dell'OP, il valore di *exp* DEVE essere calcolato come il valore minimo tra la durata di validità del token e quella del consenso. 

  .. note::
    Al fine di chiarire il meccanismo di rotazione si riporta di seguito un esempio non normativo dove si descrive l'emissione e il lifecyle del *Refresh Token* con validità di 30 giorni.
    
    - t1: un RP effettua un autenticazione con *scope=offline_access*, quindi ottiene *Refresh Token* RT1 (validità 30gg)
    - t2 = t1 + 4gg: l'RP fa richiesta al *Token endpoint* presentando RT1. L'OP riconosce che la richiesta proviene dallo stesso RP e rilascia un nuovo *Access Token* e nuovo *Refresh Token* RT2 con validità 30gg a partire da t2
    - t3 = t1 + 32gg: dopo 28gg da t2 l'RP fa richiesta al *Token endpoint* presentando RT2. L'OP riconosce che la richiesta proviene dallo stesso RP e rilascia un nuovo *Access Token* e nuovo *Refresh Token* RT3 con validità 30gg da t3
    - t4 = t1 + 64gg: dopo 32gg da t3 l'RP fa richiesta al *Token endpoint* presentando RT3. Questa volta l'OP rifiuta la richiesta con un errore perchè RT3 risulta non più valido. 

.. _TOKEN_ENDPOINT_ERRORS:

Codici di errore
++++++++++++++++

.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Codice HTTP**
    - **Supportato da**

  * - *invalid_client*
    - Problemi durante la client authentication (ad esempio, il client_id è conosciuto, non è fornita l'autenticazione del client o il metodo di autenticazione non è supportato) |br|  (:rfc:`6749#section-5.2`).
    - *401 Unauthorized*
    - |spid-icon| |cieid-icon|

  * - *unsupported_grant_type*
    - Il parametro grant_type contiene un valore non corretto (:rfc:`6749#section-5.2`).
    - *400 Bad Request*
    - |spid-icon| |cieid-icon|

  * - *invalid_grant*
    - I parametri grant_type, code, code_verifier, access_token non sono validi (:rfc:`6749#section-5.2`).
    - *400 Bad Request*
    - |spid-icon| |cieid-icon|

  * - *invalid_request*
    - La richiesta non è valida a causa della mancanza o della non correttezza di uno o più parametri (:rfc:`6749#section-5.2`).
    - *400 Bad Request*
    - |spid-icon| |cieid-icon|

  * - *server_error*
    - L'OP ha riscontrato un problema interno (:rfc:`6749#section-5.2`).
    - *500 Internal Server Error*
    - |spid-icon| |cieid-icon|

  * - *temporarily_unavailable*
    - L'OP ha riscontrato un problema interno temporaneo (:rfc:`6749#section-5.2`).
    - *503 Service Unavailable*
    - |spid-icon| |cieid-icon|
