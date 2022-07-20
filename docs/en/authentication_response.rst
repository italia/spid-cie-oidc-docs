.. include:: ./common_definitions.rst

Authentication response
-----------------------

An Authentication response is an OAuth 2.0 authorization response message, returned by the authorization endpoint of the OpenID Provider (OP) at the end of the authentication flow. The OP redirects the user
to the URL contained in the parameter redirect_uri specified in the authorization request, adding the response parameters.

.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-4.1.2
 - https://openid.net/specs/openid-connect-core-1_0.html#AuthRequestValidation

Response
++++++++

If the authentication has succeded, the OpenID Provider (OP), redirects the user wuth the following parameters:


.. code-block:: 

 GET /resp?
 code=usDwMnEzJPpG5oaV8x3j&
 state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd

 Host: https://rp.spid.agid.gov.it
 HTTP/1.1


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **code**
     - Unique *Authorization Code* that the client can pass to the Token Endpoint for obtaining an ID Token and an Access Token. This has the advantage of not exposing any token to the User Agent or to malware that coud be controlling it.
     - |spid-icon| |cieid-icon|
   * - **state**
     - State value included in the *Authentication Request*. The client is supposed to check its correspondene. It must have the same value indicated by the client in the Authorization Request.
     - |spid-icon| |cieid-icon|
   * - **iss**
     - Unique Identifier of the OP that has created the Authentication Response. The RP MUST validate
       this parameter and MUST NOT allow more OPs to use the same identifier. MANDATORY only for CIE.
     - |cieid-icon|

Errori
++++++

In caso di errore, l'OP visualizza i messaggi di anomalia relativi agli scambi OpenID
Connect descritti nelle relative tabelle definite dalle `Linee Guida UX SPID`_. Nei casi in cui tali linee
guida prescrivono un redirect dell'utente verso il RP, l'OP effettua il redirect verso l'URL indicata
nel parametro redirect_uri della richiesta (solo se valido, ovvero presente nel client metadata), con
i seguenti parametri.

**Esempio:**

.. code-block:: 

 GET /resp?
 error=invalid_request&
 error_description=request%20malformata&
 state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd

 Host: https://rp.spid.agid.gov.it
 HTTP/1.1


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **error**
     - Codice dell'errore
     - |spid-icon| |cieid-icon|
   * - **error_description**
     - Descrizione più dettagliata dell'errore, finalizzata ad aiutare lo sviluppatore per eventuale debugging. Questo messaggio non è 
       destinato ad essere visualizzato all'utente (a tal fine si faccia riferimento alle `Linee Guida UX SPID`_
     - |spid-icon| |cieid-icon|
   * - **state**
     - Valore *state* incluso nella Authentication Request.  Il client è tenuto a verificare che corrisponda a quello inviato nella Authentication Request.
     - |spid-icon| |cieid-icon|


.. seealso::

 - https://tools.ietf.org/html/rfc6749#section-4.1.2.1



