.. include:: ../common/common_definitions.rst

.. _parametri_scope_claims:

Utilizzo dei parametri **scope** e **claims**
---------------------------------------------

Gli attributi dell'utente POSSONO essere richiesti dal RP nell'Authorization Request usando i parametri **scope** o **claims**.
Nel caso di utilizzo del parametro **scope** i seguenti valori sono supportati:

- **profile**: usando questo valore è possibile ottenere il profilo utente di default che corrisponde al Minimum Dataset eIDAS: 

    - *family_name*, 
    - *given_name*,
    - *birthdate*, 
    - *\https://attributes.eid.gov.it/fiscal_number* (National Unique Identifier).

- **email**: questo valore permette di ottenere, se resi disponibili dall'utente, i seguenti attributi:

    - *email*,
    - *email_verified*.

Gli attributi richiesti tramite il parametro **scope** sono disponibili sia nell'ID Token e sia nella risposta allo userinfo endpoint.

.. note::
    Il parametro **scope** PUÒ contenere uno o più valori separati da uno spazio. Ad esempio l'utilizzo congiunto di *profile* e *email* permette di ottenere l'unione degli insiemi degli attributi (Minimum Dataset eIDAS e l'email).

Nel caso di richiesta di singoli attributi dell'utente o specifiche combinazioni di essi, Il RP PUÒ usare il parametro **claims**. 
Per la definizione del parametro **claims** e la modalità di utilizzo per la richiesta degli attributi dell'utente si può fare riferimento a `OpenID.Core#ClaimsParameter`_. 

.. warning::
  Se il parametro **claims** non è presente o non è valorizzato, viene restituito solo il claim *sub* nella risposta allo userinfo endpoint. 

  Tutt gli attributi dell'utente richiesti tramite parametro **scope** o tramite parametro **claims** sono disponibili anche nell'*ID Token* oltre che allo *userinfo endpoint*.
  

