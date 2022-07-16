.. include:: ./common_definitions.rst

UserInfo Endpoint (attributi)
-----------------------------

Lo UserInfo Endpoint è una risorsa protetta OIDC che restituisce gli attributi dell'utente autenticato. Per ottenere gli attributi richiesti, il RP inoltra una richiesta allo UserInfo Endpoint utilizzando l'Access Token.

Lo UserInfo Endpoint DEVE supportare l'uso del solo metodo HTTP GET :rfc:`2616` e DEVE accettare e validare l'Access Token inviato all'interno del campo Authorization dell'Header, di tipo Bearer :rfc:`6750`.


.. code-block:: 

 GET https://op.spid.agid.gov.it/userinfo
  Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImRCNjdnTDdja ...
  
.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#UserInfo
 - https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#rfc.section.4


.. _userinfo_response:

Response
++++++++

La response dello UserInfo Endpoint DEVE specificare nel "Content-Type" il valore "application/jwt".

Il contenuto del corpo della Response DEVE essere un `JWT firmato e cifrato. <https://openid.net/specs/openid-connect-core-1_0.html#UserInfoResponse>`_

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
     - String. Identificatore del soggetto, coincidente con quello già rilasciato nell'ID Token.
       Il RP DEVE verificare che il valore coincida con quello contenuto nell'ID Token.
     - 
   * - **aud**
     - String. Identificatore del soggetto destinatario della response (RP).
       Il RP DEVE verificare che il valore coincida con il proprio client_id.
     - 
   * - **iss**
     - String. URI che identifica univocamente l'OP.
     - 
   * - **<attributo>**
     - I claim richiesti al momento dell'autenticazione.
     - 


In caso di errore di autenticazione, lo UserInfo Endpoint restituisce un errore HTTP in accordo con quanto indicato in `OpenID Connect Core 1.0 al paragrafo 5.3.3 <https://openid.net/specs/openid-connect-core-1_0.html#UserInfoError>`_

.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#UserInfoError
