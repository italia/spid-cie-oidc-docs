.. include:: ./common_definitions.rst


Altri Metadata
++++++++++++++

Nel contesto OAuth context, `OIDC-FED`_ supporta:

 - OAuth AS con identificatore del tipo di Metadata *oauth_authorization_server*. Tutti i parametri definiti in :rfc:`8414#Section_2` sono applicabili.
 - OAuth Client con identificatore del tipo di Metadata *oauth_client*. Tutti i parametri definiti in :rfc:`7591#Section_2` sono applicabili.
 - OAuth Protected Resource con identificatore del tipo di Metadata *oauth_resource*. Non c'è uno standard che specifichi quali
   parametri possono occorrere nel Metadata per questo tipo di entità. Quindi per il momento questo può essere visto come un placeholder.
 - Emittente di Trust Mark con identificatore del tipo di Metadata *trust_mark_issuer*. Tutte le entità che partecipano in una
   Federazione possono essere di questo tipo. 


