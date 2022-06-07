.. include:: ./common_definitions.rst

Authorization Endpoint (Authentication Request)
===============================================

Per avviare il processo di autenticazione, il RP reindirizza l’utente all’Authorization Endpoint dell’OP selezionato, passando in POST o in GET una richiesta avente nel parametro **request** un oggetto in formato JWT.

Se viene utilizzato il metodo POST i parametri devono essere trasmessi utilizzando la Form Serialization (OIDC Connect Core 1.0 par. 13.2).

I parametri **client_id**, **response_type** e **scope** devono essere trasmessi sia come parametri sulla chiamata HTTP sia all’interno dell’oggetto request e i loro valori devono corrispondere, in ogni caso i parametri all’interno dell’oggetto request prevalgono su quelli indicati sulla chiamata HTTP.

L’oggetto request DEVE essere un token JWT firmato, secondo le modalità definite dall’Agenzia per l’Italia Digitale. 

.. warning::
    |warning-message|

**Esempio (chiamata HTTP):**::

 GET /auth?client_id=https://rp.spid.agid.gov.it&
 response_type=code&scope=openid& code_challenge=qWJlMe0xdbXrKxTm72EpH659bUxAxw80&
 code_challenge_method=S256&request=eyJhbGciOiJSUzI1NiIsImtpZCI6ImsyYmRjIn0.ew0KIC
 Jpc3MiOiAiczZCaGRSa3F0MyIsDQogImF1ZCI6ICJodHRwczovL3NlcnZlci5leGFtcGxlLmNvbSIsDQo
 gInJlc3BvbnNlX3R5cGUiOiAiY29kZSBpZF90b2tlbiIsDQogImNsaWVudF9pZCI6ICJzNkJoZFJrcXQz
 IiwNCiAicmVkaXJlY3RfdXJpIjogImh0dHBzOi8vY2xpZW50LmV4YW1wbGUub3JnL2NiIiwNCiAic2Nvc
 GUiOiAib3BlbmlkIiwNCiAic3RhdGUiOiAiYWYwaWZqc2xka2oiLA0KICJub25jZSI6ICJuLTBTNl9Xek
 EyTWoiLA0KICJtYXhfYWdlIjogODY0MDAsDQogImNsYWltcyI6IA0KICB7DQogICAidXNlcmluZm8iOiA
 NCiAgICB7DQogICAgICJnaXZlbl9uYW1lIjogeyJlc3NlbnRpYWwiOiB0cnVlfSwNCiAgICAgI…

 Host: https://op.spid.agid.gov.it
 HTTP/1.1
 
**Esempio (contenuto del JWT):**:: 

 {
      client_id=https://rp.spid.agid.gov.it
      response_type=code
      scope=openid
      code_challenge=qWJlMe0xdbXrKxTm72EpH659bUxAxw80
      code_challenge_method=S256
      nonce=MBzGqyf9QytD28eupyWhSqMj78WNqpc2
      prompt=login
      redirect_uri=https%3A%2F%2Frp.spid.agid.gov.it%2Fcallback1%2F
      acr_values=https://www.spid.gov.it/SpidL1 https://www.spid.gov.it/SpidL2
      claims={
          "id_token": {
              "nbf": { essential: true },
              "jti": { essential: true }
          },
          "userinfo": {
              "https://attributes.spid.gov.it/name": null,
              "https://attributes.spid.gov.it/familyName": null
          },
      }
      state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd
 }

.. list-table:: 
   :widths: 25 25 25 25
   :header-rows: 1

   * - Parametro
     - Descrizione
     - Valori ammessi
     - Obbligatorio
   * - **client_id**
     - URI che identifica univocamente il RP come da Registro SPID 
     - Deve corrispondere ad un valore nel Registro SPID.
     - |check-icon|
   * - **code_challenge**
     - Un challenge per PKCE da riportare anche nella successiva richiesta al Token endpoint.
     - V. paragrafo "Generazione del code_challenge per PKCE"
     - |check-icon|
   * - **code_challenge_method**
     - Metodo di costruzione del challenge PKCE
     - È obbligatorio specificare il valore **S256**
     - |check-icon|
   * - **nonce**
     - Valore che serve ad evitare attacchi Reply, generato casualmente e non prevedibile da terzi. Questo valore sarà restituito nell’ID Token fornito dal Token Endpoint, in modo da consentire al client di verificare che sia uguale a quello inviato nella richiesta di autenticazione.
     - Stringa di almeno 32 caratteri alfanumerici.
     - |check-icon|
   * - **prompt**
     - Definisce se l’OP deve occuparsi di eseguire una richiesta di autenticazione all’utente o meno
     - consent: l’OP chiederà le credenziali di autenticazione all’utente (se non è già attiva una sessione di Single Sign-On) e successivamente chiederà il consenso al trasferimento degli attributi (valore consigliato). Se è già attiva una sessione di Single Sign-On, chiederà il consenso al trasferimento degli attributi.
	 
	 **consent login**: l’OP chiederà sempre le credenziali di autenticazione all’utente e successivamente chiederà il consenso al trasferimento degli attributi (valore da utilizzarsi limitatamente ai casi in cui si vuole forzare la riautenticazione).
	 
	 **verify**: l’OP verifica la presenza dell’utente tramite una prova di autenticazione, se è già attiva una sessione di Single Sign-On, e, successivamente, chiederà il consenso al trasferimento degli attributi. Se non è già attiva una sessione di Single Sign-On, l’OP chiederà le credenziali di autenticazione all’utente e, successivamente, chiederà il consenso al trasferimento degli attributi (valore facoltativo).
     - |check-icon|
   * - **redirect_uri**
     - URL dove l’OP reindirizzerà l’utente al termine del processo di autenticazione.
     - Deve essere uno degli URL indicati nel client metadata (v. paragrafo 3.2). 
     - |check-icon|
   * - **response_type**
     - Il tipo di credenziali che deve restituire l’OP.
     - **code**
     - |check-icon|
   * - **scope**
     - Lista degli scope richiesti.
     - **openid** (obbligatorio).

       **offline_access**: se specificato, l’OP rilascerà oltre all’access token anche un refresh token necessario per instaurare sessioni lunghe revocabili. L’uso di questo valore è consentito solo se se si intende offrire all’utente una `sessione lunga revocabile <https://www.agid.gov.it/sites/default/files/repository_files/spid-avviso-n41-integrazione_ll.gg_._openid_connect_in_spid.pdf#page=6>`_.
     - |check-icon|
   * - **acr_values**
     - Valori di riferimento della classe di contesto dell’autenticazion e richiesta. Stringa separata da uno spazio, che specifica i valori “acr” richiesti al server di autorizzazione per l’elaborazione della richiesta di autenticazione, con i valori visualizzati in ordine di preferenza. L’OP ha facoltà di utilizzare un’autenticazione ad un livello più alto di quanto richiesto. Tale scelta non deve comportare un esito negativo della richiesta.
     - https://www.spid.gov.it/SpidL1
       https://www.spid.gov.it/SpidL2
       https://www.spid.gov.it/SpidL3
     - |check-icon|
   * - **claims**
     - Lista dei claims (attributi) che un RP intende richiedere.
     - v. paragrafo *Claims*
     - |check-icon|
   * - **state**
     - Valore univoco utilizzato per mantenere lo stato tra la request e il callback. Questo valore verrà restituito al client nella risposta al termine dell’autenticazione. Il valore deve essere significativo esclusivamente per il RP e non deve essere intellegibile ad altri.
     - Stringa di almeno 32 caratteri alfanumerici.
     - |check-icon|
   * - **ui_locales**
     - Lingue preferibili per visualizzare le pagine dell’OP. L’OP può ignorare questo parametro se non dispone di nessuna delle lingue indicate.
     - Lista di codici RFC5646 separati da spazi.
     - |uncheck-icon|	 

.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#FormSerialization
 - https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest
 - https://openid.net/specs/openid-igov-oauth2-1_0-03.html#rfc.section.2.1.1
 - https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#rfc.section.2.1
 - https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#rfc.section.2.4
 - https://openid.net/specs/openid-connect-core-1_0.html#JWTRequests
	 
Claims
++++++

Il parametro claims definisce gli attributi richiesti dal **RP**. Gli attributi SPID sono richiesti all’interno dell’elemento "userinfo", elencando gli attributi da richiedere come chiavi di oggetti JSON, i cui valori devono essere indicati come {"essential": true} o secondo le modalità definite dall’Agenzia per l’Italia Digitale. Non è possibile richiedere attributi SPID nell’id_token. Gli
attributi elencati sotto "userinfo" sono disponibili al momento della chiamata allo UserInfo Endpoint.

.. code-block:: 

 {
    "userinfo": {
        "https://attributes.spid.gov.it/familyName": {"essential": true}
    },
 }


.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#IndividualClaimsRequests


Generazione del code challenge per PKCE
+++++++++++++++++++++++++++++++++++++++

PKCE (Proof Key for Code Exchange, `RFC7636 <https://tools.ietf.org/html/rfc7636>`_) è un’estensione del protocollo OAuth 2.0 finalizzata ad evitare un potenziale attacco attuato con l’intercettazione dell’authorization code, soprattutto nel caso di applicazioni per dispositivi mobili. Consiste nella generazione di un codice (*code verifier*) e del suo hash (*code challenge*). Il *code challenge* viene inviato all’OP nella richiesta di autenticazione.

Quando il client contatta il Token Endpoint al termine del flusso di autenticazione, invia il *code verifier* originariamente creato, in modo che l’OP possa confrontare che il suo hash corrisponda con quello acquisito nella richiesta di autenticazione.

Il *code verifier* e il *code challenge* devono essere generati secondo le modalità definite
dall’Agenzia per l’Italia Digitale


Esempio
*******
.. literalinclude :: ../../static/pkce.py
   :language: python

.. seealso::

 - https://openid.net/specs/openid-igov-oauth2-1_0-03.html#rfc.section.3.1.7
 - https://tools.ietf.org/html/rfc7636
