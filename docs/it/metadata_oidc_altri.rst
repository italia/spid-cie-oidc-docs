.. include:: ./common_definitions.rst


Altri Metadata
++++++++++++++

Nel contesto OAuth context, `OIDC-FED`_ supporta:

 - OAuth AS con identificatore del tipo di metadato *oauth_authorization_server*. Tutti i parametri definiti in :rfc:`8414#Section_2` sono applicabili.
 - OAuth Client con identificatore del tipo di metadato *oauth_client*. Tutti i parametri definiti in :rfc:`7591#Section_2` sono applicabili.
 - OAuth Protected Resource con identificatore del tipo di metadato *oauth_resource*. Non c’è uno standard che specifichi quali
   parametri possono occorrere nel metadato per questo tipo di entità. Quindi per il momento questo può essere visto come un placeholder.
 - Emittente di Trust Mark con identificatore del tipo di metadato *trust_mark_issuer*. Tutte le entità che partecipano in una
   federazione possono essere di questo tipo. Le seguenti proprietà sono permesse:

    - *status_endpoint*. OPZIONALE. L’endpoint per l’operazione di status è descritto nella Sezione `OIDC-FED#Section.7.4.1`_. 

   **Esempio**

    .. code-block:: 

      {
           "trust_mark_issuer":{
               "status_endpoint":"https://trust_marks_are_us.example.com/status"
           }
      }

