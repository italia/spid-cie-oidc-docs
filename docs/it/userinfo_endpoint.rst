.. include:: ../common/common_definitions.rst

UserInfo Endpoint
-----------------

Lo UserInfo Endpoint è una risorsa protetta che restituisce gli attributi dell'utente autenticato. Per ottenere gli attributi richiesti, il RP inoltra una richiesta allo UserInfo Endpoint utilizzando l'Access Token.

Request
+++++++

.. admonition:: |spid-icon|

  Lo UserInfo Endpoint DEVE supportare l'uso del solo metodo HTTP GET :rfc:`2616` e DEVE accettare e validare l'Access Token inviato all'interno del campo Authorization dell'Header, di tipo Bearer :rfc:`6750`.

.. admonition:: |cieid-icon|

  Lo UserInfo Endpoint DEVE supportare l'uso dei metodi HTTP GET e POST :rfc:`2616` e DEVE accettare e validare l'Access Token inviato all'interno del campo Authorization dell'Header, di tipo Bearer :rfc:`6750`. 


.. code-block::  http

  GET https://op.spid.agid.gov.it/userinfo
  Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImRCNjdnTDdja ...
  
.. seealso::

 - https://openid.net/specs/openid-connect-core-1_0.html#UserInfo
 - https://openid.net/specs/openid-igov-openid-connect-1_0-03.html#Section-4


.. _userinfo_response:

Response
++++++++

.. admonition:: |spid-icon|

  La response dello UserInfo Endpoint DEVE specificare nel "Content-Type" il valore "application/jwt".

Il contenuto del corpo della Response DEVE essere un `JWT firmato e cifrato. <https://openid.net/specs/openid-connect-core-1_0.html#UserInfoResponse>`_.

L'header JOSE DEVE contenere il parametro *cty* (Content Type) valorizzato con *JWT* (vedi :rfc:`7519#section-5.2`).

Lo UserInfo Endpoint restituisce gli attributi utente esplicitamente richiesti tramite il parametro **claims** o tramite l'utilizzo del parametro **scope** nella Authentication Request.

**Esempio:**

.. code-block:: http

  HTTP/1.1 200 OK
  Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
  Content-Type: application/jose 

  {
    "alg": "RSA-OAEP",
    "enc": "A256CBC-HS512",
    "kid": "HIvo33-Km7n03ZqKDJfWVnlFudsW28YhQZx5eaXtAKA",
    "cty": "JWT"
  }
  .
  {
     "iss": "https://op.fornitore_identita.it",
     "aud": "https://rp.fornitore_servizio.it",
     "iat": 1519032969,
     "nbf": 1519032969,
     "exp": 1519033149,
     "sub": "OP-1234567890",
     "name": "Mario",
     "family_name": "Rossi",
     "https://attributes.spid.gov.it/fiscal_number": "MROXXXXXXXXXXXXX"
  }

L'intestazione del JWE DEVE contenere i seguenti parametri:

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **alg**
     - String. Vedi :ref:`supported_algs`..
     - |spid-icon| |cieid-icon|
   * - **kid**
     - Vedi :rfc:`7638#section_3`. 
     - |spid-icon| |cieid-icon|
   * - **enc**
     - String. Vedi :ref:`supported_algs`..
     - |spid-icon| |cieid-icon|
   * - **cty**
     - String. DEVE essere valorizzato con "JWT".
     - |spid-icon| |cieid-icon|


Il payload del JWE è un JWS contenente all'interno del suo payload i seguenti parametri:

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **sub**
     - String. Identificatore del soggetto, coincidente con quello già rilasciato nell'ID Token.
       Il RP DEVE verificare che il valore coincida con quello contenuto nell'ID Token.
     - |spid-icon| |cieid-icon|
   * - **iat**
     - UNIX Timestamp con l'istante di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`. 
     - |spid-icon| |cieid-icon|
   * - **exp**
     - UNIX Timestamp con l'istante di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
     - |spid-icon| |cieid-icon|
   * - **aud**
     - String. Identificatore del soggetto destinatario della response (RP).
       Il RP DEVE verificare che il valore coincida con il proprio client_id.
     - |spid-icon| |cieid-icon|
   * - **iss**
     - String. URI che identifica univocamente l'OP.
     - |spid-icon| |cieid-icon|
   * - **<attributo>**
     - I claim richiesti al momento dell'autenticazione.
     - |spid-icon| |cieid-icon|

L'intestazione del JWS DEVE contenere i seguenti parametri:

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **alg**
     - String. Vedi :ref:`supported_algs`..
     - |spid-icon| |cieid-icon|
   * - **kid**
     - Vedi :rfc:`7638#section_3`. 
     - |spid-icon| |cieid-icon|
   * - **cty**
     - String. DEVE essere valorizzato con "JWT".
     - |spid-icon| |cieid-icon|

Codici di errore
++++++++++++++++

Come definiti per :ref:`Token endpoint<TOKEN_ENDPOINT_ERRORS>`.

