.. include:: ./common_definitions.rst

.. _flusso_autenticazione:

Flusso di autenticazione
------------------------

Gli schemi di autenticazioni **"Entra con SPID"** e **"Entra con CIE"** implementano il flusso **OpenID Connect Authorization Code Flow** di cui l'immagine seguente ne mostra gli aspetti salienti.
Questo flusso restituisce un **Authorization Code** che può essere utilizzato per ottenere un **ID Token**
e/o un **Access Token** e se possibile anche un **Refresh Token**. 
L'**Authorization Code Flow** ottiene l'**Authorization Code** dall'*Authorization Endpoint* dell'OpenID Provider e tutti i token sono restituiti dal **Token Endpoint**.

.. image:: ../../images/flusso.svg
    :width: 100%


Segue la descrizione dei passaggi, come da numerazione indicata in figura.

  #. L'Utente, nella pagina di accesso del Relying Party (RP):

     * Seleziona ill pulsante "Entra con SPID" o "Entra con CIE";
     
     * Nela caso SPID, seleziona l'OP con cui autenticarsi.   

  #. L'RP prepara una Richiesta di Autorizzazione e la invia all'Authorization Endpoint dell'OP.

  #. L'OP autentica l'utente mediante l'inserimento delle credenziali e ottiene il consenso per l'accesso agli attributidell'utente da parte del RP.

  #. L'OP reindirizza l'utente all'URL contenuto nel parametro *redirect_uri* specificato dal RP, passando un *Authorization Code* nell'Authorization Response.

  #. L'RP invia l'*Authorization Code* ricevuto al *Token Endpoint* dell'OP.

  #. Il *Token Endpoint* dell'OP rilascia un **ID Token**, un **Access Token** e se richiesto un **Refresh Token**.

  #. L'RP riceve e valida l'**Access Token** e l'**ID Token**. Per chiedere gli attributi che erano stati autorizzati dall'utente al punto 3, invia una richiesta all'*UserInfo Endpoint* dell'OP utilizzando l'**Access Token** per l'autenticazione.

  #. Lo *UserInfo Endpoint* dell'OP verifica la validità dell'**Access Token** e rilascia gli attributi richiesti all'RP.







