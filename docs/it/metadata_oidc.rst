.. include:: ./common_definitions.rst

Metadati OIDC
-------------

OIDC-FED utilizza i claim dei metadati così come definiti all’interno delle specifiche di OpenID Connect Discovery 1.0 e OpenID Connect Dynamic Client Registration 1.0 `OpenID.Discovery`_, `OpenID.Registration`_ rispettivamente per OP e RP. 

In OIDC-FED il metadato OIDC relativo a RP e OP viene definito all’interno del claim **metadata** e del suo sotto claim **<entity_type>**, all’interno dell’Entity Configuration, come oggetto JSON.





Altri metadati
++++++++++++++

Nel contesto OAuth context, `OIDC-FED`_ supporta:

 - OAuth AS con identificatore del tipo di metadato *oauth_authorization_server*. Tutti i parametri definiti in :rfc:`8414#Section_2` sono applicabili.
 - OAuth Client con identificatore del tipo di metadato *oauth_client*. Tutti i parametri definiti in :rfc:`7591#Section_2` sono applicabili.
 - OAuth Protected Resource con identificatore del tipo di metadato *oauth_resource*. Non c'è uno standard che specifichi quali
   parametri possono occorrere nel metadato per questo tipo di entità. Quindi per il momento questo può essere visto come un placeholder.
 - Emittente di Trust Mark con identificatore del tipo di metadato *trust_mark_issuer*. Tutte le entità che partecipano in una
   federazione possono essere di questo tipo. Le seguenti proprietà sono permesse:

    - *status_endpoint*. OPZIONALE. L'endpoint per l'operazione di status è descritto nella Sezione `OIDC-FED#Section.7.4.1`_. 

   **Esempio**

    .. code-block:: 

      {
           "trust_mark_issuer":{
               "status_endpoint":"https://trust_marks_are_us.example.com/status"
           }
      }

