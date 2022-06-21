.. include:: ./common_definitions.rst

Metadati OIDC
-------------

OIDC-FED utilizza i claim dei metadati così come definiti all’interno delle specifiche di OpenID Connect Discovery 1.0 e OpenID Connect Dynamic Client Registration 1.0 `[OpenID.Discovery]`_,`[OpenID.Registration]`_ rispettivamente per OP e RP. 

In OIDC-FED il metadato OIDC relativo a RP e OP viene definito all’interno del claim **metadata** e del suo sotto claim **<entity_type>**, all’interno dell’Entity Configuration, come oggetto JSON.


OpenID Connect Provider Metadata (OP)
+++++++++++++++++++++++++++++++++++++

È il metadato che gli OP pubblicano con l’identificativo **openid_provider**, come segue.

.. code-block:: 

 {
     "metadata":{
         "openid_provider":{
             ...
         }
     }
 }


Dove un OP non disponesse all’interno dei propri metadata dei claim **client_registration_types_supported** e/o **request_authentication_methods_supported** i valori da intendersi come impliciti sono i seguenti.

.. list-table:: 
   :widths: 20 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Tipo**
     - **Descrizione**
     - **Obbligatorio**
   * - **client_registration_types_supported**
     - String
     - Array che specifica i tipi supportati dalla federazione (solo *automatic*)
     - |check-icon|
   * - **organization_name**
     - String
     - Un nome leggibile che rappresenta l'organizzazione proprietaria dell'OP. È inteso per l'utilizzo nell'interfaccia
       utente, per essere riconosciuto dagli utenti finali che usano l'OP per autenticarsi.

       L'unico metodo di richiesta autenticazione supportato **request_object** per le Richieste di Autorizzazione (ar)

       ..code-block::

        {
            "authorization_endpointer":[
                 "request_object"
            ]
        }
     - |uncheck-icon|
   * - **request_authentication_methods_supported**
     - JSON Object
     - Un oggetto JSON con membri che rappresentano metodi di richiesta autenticazione e come valori liste di metodi di
       richieste di autenticazione che sono supportati dall'authorization endpoint.
     - |uncheck-icon|
   * - **signed_jwks_uri**
     - URI
     - Un URI che punta a un JWT firmato che come payload il JWK Set dell'entità (vedere esempio sotto). Il JWT è firmato
       con una chiave inclusa nel JWK che l'entità ha pubblicato nel suo Entity Statement autofirmato.
     - |uncheck-icon|


Ogni OP DEVE esporre all’interno dei propri metadati i seguenti claim come obbligatori.

.. list-table:: 
   :widths: 20 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Tipo**
     - **Descrizione**
     - **Obbligatorio**
   * - **organization_name**
     - String
     - Un nome leggibile che rappresenta l'organizzazione proprietaria dell'OP
     - |check-icon|
   * - **jwks**
     - JSON
     - JSON Web Key Set `[RFC7517#appendix-A.1]`_
     - |check-icon| in assenza del claim **signed_jwks_uri**. 
   * - **signed_jwks_uri**
     - String
     - URL del JWT auto firmato e verificabile con la chiave pubblica di Federazione (JWK).
     - |check-icon| in assenza del claim **jwks**. 



OpenID Connect Relying Party Metadata (RP)
++++++++++++++++++++++++++++++++++++++++++

È il metadata che i RP pubblicano con l’identificativo **openid_relying_party**, come segue.

.. code-block:: 

 {
     "metadata":{
         "openid_relying_party":{
             ...
         }
     }
 }


Dove un RP non disponesse all’interno dei propri metadati dei claim **client_registration_types** i valori da intendersi come impliciti sono i seguenti.

.. list-table:: 
   :widths: 20 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Tipo**
     - **Descrizione**
     - **Obbligatorio** 
   * - **client_registration_types**
     - String
     - Array che specifica i tipi supportati dalla federazione (solo *automatic*)
     - |check-icon| 



Ogni RP DEVE esporre all’interno dei propri Metadata i seguenti claim come obbligatori

.. list-table:: 
   :widths: 20 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Tipo**
     - **Descrizione**
     - **Obbligatorio**
   * - **organization_name**
     - String
     - Un nome leggibile che rappresenta l'organizzazione proprietaria dell'RP
     - |check-icon| 
   * - **jwks**
     - JSON
     - JSON Web Key Set `[RFC7517#appendix-A.1]`_
     - |check-icon| in assenza del claim **signed_jwks_uri**. 
   * - **signed_jwks_uri**
     - String
     - URL del JWT auto firmato e verificabile con la chiave pubblica di Federazione (JWK).
     - |check-icon| in assenza del claim **jwks**. 



OpenID Connect Federation Entity Metadata (FA)
++++++++++++++++++++++++++++++++++++++++++++++

È il metadato che il Trust Anchor, o suo Intermediario, pubblica con l’identificativo **federation_entity**, come segue.

.. code-block:: 

 {
     "metadata":{
         "federation_entity":{
             ...
         }
     }
 }


L’oggetto **federation_entity** è composto dai seguenti claim

.. list-table:: 
   :widths: 20 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Tipo**
     - **Descrizione**
     - **Obbligatorio**
   * - **federation_fetch_endpoint**
     - String
     - Url presso il quale sono pubblicati gli Entity Statements in formato JWT dei soggetti discendenti.
     - |check-icon| 
   * - **federation_list_endpoint**
     - String
     - Url presso il quale è possibile ottenere la lista dei discendenti in formato JSON.
       
       *Non contestualizzato in CIE Federation*
     - |check-icon| 
   * - **federation_resolve_endpoint**
     - String
     - Url presso il quale è possibile ottenere i trust mark validati,il metadata finale e la Trust Chain, 
       relativamente ad un soggetto.
       
       *Non contestualizzato in CIE Federation*
     - |check-icon| 
   * - **federation_status_endpoint**
     - String
     - Url presso il quale è possibile validare l’assegnazione di un Trust Mark ad uno specifico soggetto.

       *Non contestualizzato in CIE Federation*
     - |check-icon| 
   * - **homepage_uri**
     - String
     - Url della pagina web del Trust Anchor o SA.

       *Non contestualizzato in CIE Federation*
     -      
   * - **organization_name**
     - String
     - Nome umanamente leggibile di questa entità.

       *Non contestualizzato in CIE Federation*
     - |uncheck-icon| 

La tabella qui sotto presenta i valori del metadato FA definiti in `[OIDC-FED]`_, contestualizzati nella CIE Federation.


.. list-table::
   :widths: 20 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Tipo**
     - **Descrizione**
     - **Obbligatorio**
   * - **federation_fetch_endpoint**
     - String
     - URL al Fetch Endpoint descritto nella Sezione XX. Entità intermedie e TA DEVONO pubblicare un  *federation_fetch_endpoint*.
       Entità Foglia NON DEVONO.
     - |uncheck-icon| 



Altri metadati
++++++++++++++

Nel contesto OAuth context, `[OIDC-FED]`_ supporta:

 - OAuth AS con identificatore del tipo di metadato *oauth_authorization_server*. Tutti i parametri definiti in `[RFC8414#Section_2]`_ sono applicabili.
 - OAuth Client con identificatore del tipo di metadato *oauth_client*. Tutti i parametri definiti in `[RFC7591#Section_2]`_ sono applicabili.
 - OAuth Protected Resource con identificatore del tipo di metadato *oauth_resource*. Non c'è uno standard che specifichi quali
   parametri possono occorrere nel metadato per questo tipo di entità. Quindi per il momento questo può essere visto come un placeholder.
 - Emittente di Trust Mark con identificatore del tipo di metadato *trust_mark_issuer*. Tutte le entità che partecipano in una
   federazione possono essere di questo tipo. Le seguenti proprietà sono permesse:

    - *status_endpoint*. OPZIONALE. L'endpoint per l'operazione di status è descritto nella Sezione XX. 

   **Esempio**

    .. code-block:: 

      {
           "trust_mark_issuer":{
               "status_endpoint":"https://trust_marks_are_us.example.com/status"
           }
      }

