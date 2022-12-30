.. include:: ../common/common_definitions.rst

.. _DifferenzeSPID_CIE:

Differenze tra SPID e CIE id
----------------------------

In questa sezione sono riportate le principali differenze tra i profili implementativi SPID e CIE id.

Metadata
++++++++

Nei metadata OP e RP per CIE id sono presenti i parametri che abilitano la cifratura dell'ID Token (vedi le sezioni relative al `Metadata OP <MetadataOP>`_ e al `Metadata RP <MetadataRP>`_). SPID non consente la cifratura dell'ID Token, dunque tali parametri non sono richiesti. 

Inoltre, il metadata OP per CIE id richiede anche il parametro *revocation_endpoint_auth_methods_supported*, non richiesto da SPID.

Authorization Endpoint
++++++++++++++++++++++

SPID, al contrario di CIE id, prevede l'inserimento obbligatorio dei parametri *client_id* e *response_type* nella richiesta HTTP. 
Inoltre, CIE id prevede come obbligatorio il parametro *iss* nella response per mitigare gli attacchi di tipo mix-up `I-D.ietf-OAuth-Security-BCP`_.


Parametri Scope e Claims
++++++++++++++++++++++++

CIE id consente di richiedere gli attributi dell'utente sia tramite il parametro *claims* nella richiesta di autenticazione e sia tramite il parametro *scope*, abilitando in quest'ultimo i valori *profile* e *email*. 

SPID non consente l'utilizzo di *profile* e *email* nel parametro *scope*. 

Per ulteriori dettagli vedi la sezione :ref:`Parametri Scope e claims <parametri_scope_claims>`.


ID Token
++++++++

SPID non consente di rilasciare gli attributi dell'utente all'interno dell'ID Token. 
In CIE id gli attributi dell'utente sono disponibili sia nell'ID Token e sia nella UserInfo response. Inoltre, il CIE id supporta la criptazione dell'ID Token.


Refresh Token
+++++++++++++

SPID prevede l'utilizzo del Refresh Token per abilitare le sessioni lunghe rinnovabili così come definito nelle `LL.GG. OpenID Connect in SPID <https://www.agid.gov.it/sites/default/files/repository_files/linee_guida_openid_connect_in_spid.pdf>`_ e nell' `Avviso n.41 <https://www.agid.gov.it/sites/default/files/repository_files/spid-avviso-n41-integrazione_ll.gg_._openid_connect_in_spid.pdf>`_ . Consente, infatti, di ottenere, oltre all'Access Token, l'ID Token valido esclusivamente per SPID livello 1. 

In CIE id il Refresh Token non consente di ottenere l'ID Token e non è utilizzabile dagli RP per ottenere una nuova autenticazione dell'utente con l'OP o rinnovare una sessione preesistente. In CIE id il Refresh Token è usato per ottenere dallo UserInfo endpoint esclusivamente il medesimo set di attributi dell'utente richiesti in fase di autenticazione iniziale, per il quale l'utente ha espresso il consenso esplicito.
Per ulteriori dettagli si veda la sezione :ref:`Refresh Token <Refresh_Token>`.

UserInfo Endpoint
+++++++++++++++++

CIE id supporta entrambi i metodi HTTP GET e HTTP POST per le richieste allo UserInfo endpoint.
SPID consente solo l'utilizzo del metodo HTTP GET.

Introspection Endpoint
++++++++++++++++++++++

CIE id prevede il solo parametro *active* nella risposta dell'Introspection endpoint. SPID aggiunge ulteriori parametri come specificato nella sezione :ref:`Introspection Endpoint <introspection_endpoint>`.


Revocation Endpoint e Logout
++++++++++++++++++++++++++++

Entrambi SPID e CIE id prevedono che il RP effettui una richiesta di revoca dell'Access Token in fase di logout dell'utente. 
In SPID la revoca di un Access Token implica anche la revoca dell'eventuale Refresh Token ancora attivo ad esso collegato e la scadenza della sessione di Single Sign-On se ancora attiva. 

In CIE id, invece, la revoca di un Access Token non prevede la revoca del relativo Refresh Token, allo stesso tempo la richiesta di revoca di un Refresh Token determina anche la revoca di tutti i relativi token ancora attivi. 

