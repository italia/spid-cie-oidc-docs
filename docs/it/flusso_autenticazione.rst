.. include:: ./common_definitions.rst

Flusso di autenticazione
------------------------

L'immagine qui sotto riportata riproduce il flusso **OpenID Connect Authorization Code Flow**.
Questo flusso restituisce un **Authorization Code** che può essere utilizzato per ottenere un **ID Token**
e/o un **Access Token** e se possibile anche un **Refresh Token**. 
L'Authorization Code Flow ottiene l'**Authorization Code** dall'**Authorization Endpoint** dell'OpenID Provider e tutti i token sono restituiti dal **Token Endpoint**.

.. image:: ../../images/flusso.svg
    :width: 100%


Segue la descrizione dei passaggi, come da numerazione indicata in figura.

.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - **Elementi**

       **Interessati**
     - **Descrizione**
   * - **1: UT->RP**
     - L'Utente, nella pagina di accesso del Relying Party (RP):

       Seleziona, sul pulsante SPID, l'OpenID Provider (OP) con cui autenticarsi

       Invia la richiesta di autenticazione con CIE all'RP
   * - **2: RP->OP/Authorization Endpoint**
     - Il Relying Party (RP) prepara una Richiesta di Autorizzazione per l'Authorization Endpoint dell'OP.
       Per la CIE, RP genera un PKCE e la invia con la Richiesta di Autorizzazione 
   * - **3: OP/Authorization Endpoint<->UT**
     - L'OpendID Provider (OP) autentica l'utente mediante l'inserimento delle credenziali e ottiene
       il consenso per l'accesso alle risorse utente da parte dell'RP.
   * - **4: OP/Authorization Endpoint->RP**
     - L'OP reindirizza l'utente verso il Redirect URI specificato dal RP, passando un Authorization 
       Code nell'Authorization Response
   * - **5: RP->OP/Token Endpoint**
     - Il RP invia l'Authorization Code ricevuto al Token Endpoint dell'OP.
       Per la CIE, l'OP esegue la verifica del PKCE.
   * - **6: OP/Token Endpoint->RP**
     - Il Token Endpoint dell'OP rilascia un ID Token, un Access Token e se richiesto un Refresh Token.
   * - **7: RP->OP/UserInfo Endpoint**
     - Il RP riceve e valida l'Access Token e l'ID Token. Per chiedere gli attributi che erano stati autorizzati
       dall'utente al punto 3, invia una richiesta all'UserInfo Endpoint dell'OP utilizzando l'Access Token per l'autenticazione.
   * - **8: OP/UserInfo Endpoint->RP**
     - Lo UserInfo Endpoint dell'OP verifica la validità dell'Access Token e rilascia gli attributi richiesti all'RP





