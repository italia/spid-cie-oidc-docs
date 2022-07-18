.. include:: ./common_definitions.rst

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

    - *email*;
    - *email_verified*.

Gli attributi richiesti tramite il parametro **scope** sono disponibili sia nell'ID Token e sia nella risposta allo userinfo endpoint.

.. note::
    Il parametro **scope** PUÒ contenere uno o più valori separati da uno spazio.

Nel caso di richiesta di singoli attributi dell'utente o specifiche combinazioni di essi, l'RP PUÒ usare il parametro **claims**. 
Per la definizione del parametro **claims** e la modalità di utilizzo per la richiesta degli attributi dell'utente si può fare riferimento a `OpenID.Core#ClaimsParameter`_. 

.. warning::
    - Nell'oggetto *id_token* del parametro **claims** è possibile richiedere solo il Minimum Dataset eIDAS. Gli altri attributi dell'utente DEVONO essere richiesti nell'oggetto *userinfo* del parametro **claims**.  
    
    - Se il parametro **claims** non è presente o non è valorizzato, viene restituito solo il claim *sub* nella risposta allo userinfo endpoint e nell'ID Token. 

La tabella seguente mostra alcuni esempi di utilizzo.

.. list-table:: 
    :widths: 10 10 20 20
    :header-rows: 1

    * - **claims**
      - **scope**
      - **Attributi nella Userinfo Response**
      - **Attributi nell'ID Token**
    * - *userinfo*: \- |br| *id_token*: \-
      - *openid*
      - *sub*
      - *sub*
    * - *userinfo*: \- |br| *id_token*: \-
      - *openid* |br| *profile*
      - *sub*, |br| *given_name*, |br| *family_name*, |br| *birthdate*, |br| *\https://attributes.eid.gov.it/fiscal_number*
      - *sub*, |br| *given_name*, |br| *family_name*, |br| *birthdate*, |br| *\https://attributes.eid.gov.it/fiscal_number*
    * - *userinfo*: \- |br| *id_token*:"birthdate":{essential:true}
      - *openid* 
      - *sub*
      - *sub*, |br|  *birthdate*
    * - *userinfo*: \- |br| *id_token*: \-
      - *openid* |br| *email*
      - *sub*, |br| *email*, |br| *email_verified*
      - *sub*, |br| *email*, |br| *email_verified*
    * - *userinfo*:"family_name":null |br| *id_token*:"given_name":{essential:true}
      - *openid* 
      - *sub*, |br|  *family_name*
      - *sub*, |br|  *given_name*
    * - *userinfo*:"gender":{essential:true} |br| *id_token*:"given_name":{essential:true}
      - *openid* 
      - *sub*, |br|  *gender*
      - *sub*, |br|  *given_name*
    * - *userinfo*:\- |br| *id_token*:"birthdate":{essential:true} "gender":{essential:true}
      - *openid* 
      - *sub*
      - *sub*, |br|  *birthdate*


