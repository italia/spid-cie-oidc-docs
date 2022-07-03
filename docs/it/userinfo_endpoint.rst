.. include:: ./common_definitions.rst

UserInfo Endpoint (attributi)
-----------------------------

Lo UserInfo Endpoint è una risorsa protetta OAuth 2.0 che restituisce attributi dell’utente autenticato. Per ottenere gli attributi richiesti, il Relying Party inoltra una richiesta allo UserInfo endpoint utilizzando l’Access token.

Lo UserInfo Endpoint deve supportare l’uso del solo metodo HTTP GET :rfc:`2616`, deve accettare il token di accesso, inviato all’interno del campo Authorization dell’Header, come token bearer OAuth 2.0 :rfc:`6750`.


.. code-block:: 

 GET https://op.spid.agid.gov.it/userinfo
  Authorization: Bearer dC34Pf6kdG
  
.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#UserInfo
 - https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#rfc.section.4


Response
++++++++

La response dello UserInfo Endpoint deve specificare nel "Content-Type" il valore "application/jwt".

Il contenuto trasmesso nel body della Response deve essere un JWT firmato e cifrato secondo le modalità definite dall’Agenzia per l’Italia Digitale.

Lo UserInfo Endpoint restituisce i claim autorizzati nella Authentication Request.

**Esempio:**

.. code-block:: 

 {
     "iss":"https://op.fornitore_identita.it",
     "aud":"https://rp.fornitore_servizio.it",
     "iat":1519032969,
     "nbf":1519032969,
     "exp":1519033149,
     "sub":"OP-1234567890",
     "name":"Mario",
     "https://attributes.spid.gov.it/familyName":"Rossi",
     "https://attributes.spid.gov.it/fiscalNumber":"MROXXXXXXXXXXXXX"
 }


Il payload del JWT è un JSON contenente i seguenti parametri:

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **sub**
     - String. Identificatore del soggetto, coincidente con quello già rilasciato nell’ID Token
       Il RP deve verificare che il valore coincida con quello contenuto nell’ID Token.
     - 
   * - **aud**
     - String. Identificatore del soggetto destinatario della response (RP)
       Il RP deve verificare che il valore coincida con il proprio client_id.
     - 
   * - **iss**
     - String. URI che identifica univocamente l’OP.
     - 
   * - **<attributo>**
     - I claim richiesti al momento dell’autenticazione
     - 


In caso di errore di autenticazione, lo UserInfo Endpoint restituisce un errore HTTP in accordo con quanto indicato nel par. 5.3.3., "UserInfo Error Response" di "OpenID Connect Core 1.0".

.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#UserInfoError
