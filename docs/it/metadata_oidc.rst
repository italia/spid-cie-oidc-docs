.. include:: ./common_definitions.rst

Metadati OIDC
=============

OIDC-FED utilizza i claim dei metadati così come definiti all’interno delle specifiche di OpenID Connect Discovery 1.0 e OpenID Connect Dynamic Client Registration 1.0 `[OpenID.Discovery]`_,`[OpenID.Registration]`_ rispettivamente per OP e RP. 

In OIDC-FED il metadato OIDC relativo a RP e OP viene definito all’interno del claim **metadata** e del suo sotto claim **<entity_type>**, all’interno dell’Entity Configuration, come oggetto JSON.


OpenID Connect Provider Metadata (OP)
+++++++++++++++++++++++++++++++++++++

È il metadato che gli OP pubblicano con l’identificativo **openid_provider**, come segue.

.. code-block:: 

 "metadata":{
     "openid_provider": { … }
 }

Dove un OP non disponesse all’interno dei propri metadata dei claim **client_registration_types_supported** e/o **request_authentication_methods_supported** i valori da intendersi come impliciti sono i seguenti.

.. list-table:: 
   :widths: 30 10 60
   :header-rows: 1

   * - Claim
     - Tipo
     - Descrizione
   * - **client_registration_types_supported**
     - String
     - OBBLIGATORIO. Array che specifica i tipi supportati dalla federazione (solo *automatic*)
   * - **organization_name**
     - String
     - OPZIONALE. Un nome leggibile che rappresenta l'organizzazione proprietaria dell'OP. È inteso per l'utilizzo nell'interfaccia
       utente, per essere riconosciuto dagli utenti finali che usano l'OP per autenticarsi.
   * - **request_authentication_methods_supported**
     - JSON Object
     - OPZIONALE. Un oggetto JSON con membri che rappresentano metodi di richiesta autenticazione e come valori liste di metodi di
       richieste di autenticazione che sono supportati dall'authorization endpoint.
       
       L'unico metodo di richiesta autenticazione supportato **request_object** per le Richieste di Autorizzazione (ar)

       ..code-block::

        {
            "authorization_endpointar":[
                "request_object"
            ]
        }


Ogni OP DEVE esporre all’interno dei propri metadati i seguenti claim come obbligatori.

.. list-table:: 
   :widths: 30 10 60
   :header-rows: 1

   * - Claim
     - Tipo
     - Descrizione
   * - **organization_name**
     - String
     - OBBLIGATORIO. Un nome leggibile che rappresenta l'organizzazione proprietaria dell'OP
   * - **jwks**
     - JSON
     - OBBLIGATORIO in assenza del claim **signed_jwks_uri**. JSON Web Key Set `[RFC7517#appendix-A.1]`_
   * - **signed_jwks_uri**
     - String
     - OBBLIGATORIO in assenza del claim **jwks**. URL del JWT auto firmato e verificabile con la chiave pubblica di Federazione (JWK).



OpenID Connect Relying Party Metadata (RP)
++++++++++++++++++++++++++++++++++++++++++

È il metadata che i RP pubblicano con l’identificativo **openid_relying_party**, come segue.

.. code-block:: 

 "metadata":{
     "openid_relying_party":{ … }
 }


Dove un RP non disponesse all’interno dei propri metadati dei claim **client_registration_types** i valori da intendersi come impliciti sono i seguenti.

.. list-table:: 
   :widths: 30 10 60
   :header-rows: 1

   * - Claim
     - Tipo
     - Descrizione
   * - **client_registration_types**
     - String
     - OBBLIGATORIO. Array che specifica i tipi supportati dalla federazione (solo *automatic*)

Ogni RP DEVE esporre all’interno dei propri Metadata i seguenti claim come obbligatori

.. list-table:: 
   :widths: 30 10 60
   :header-rows: 1

   * - Claim
     - Tipo
     - Descrizione
   * - **organization_name**
     - String
     - OBBLIGATORIO. Un nome leggibile che rappresenta l'organizzazione proprietaria dell'RP
   * - **jwks**
     - JSON
     - OBBLIGATORIO in assenza del claim **signed_jwks_uri**. JSON Web Key Set `[RFC7517#appendix-A.1]`_
   * - **signed_jwks_uri**
     - String
     - OBBLIGATORIO in assenza del claim **jwks**. URL del JWT auto firmato e verificabile con la chiave pubblica di Federazione (JWK).



OpenID Connect Federation Entity Metadata (FA)
++++++++++++++++++++++++++++++++++++++++++++++

È il metadato che il Trust Anchor, o suo Intermediario, pubblica con l’identificativo **federation_entity**, come segue.

.. code-block:: 

 "metadata":{
     "federation_entity":{ … }
 }

L’oggetto **federation_entity** è composto dai seguenti claim

.. list-table:: 
   :widths: 30 10 60
   :header-rows: 1

   * - Claim
     - Tipo
     - Descrizione
   * - **federation_fetch_endpoint**
     - URL
     - OBBLIGATORIO. Url presso il quale sono pubblicati gli Entity Statements in formato JWT dei soggetti discendenti.
   * - **federation_list_endpoint**
     - URL
     - OBBLIGATORIO. Url presso il quale è possibile ottenere la lista dei discendenti in formato JSON.

       *Non contestualizzato in CIE Federation*
   * - **federation_resolve_endpoint**
     - URL
     - OBBLIGATORIO. Url presso il quale è possibile ottenere i trust mark validati,il metadata finale e la Trust Chain, 
       relativamente ad un soggetto.

       *Non contestualizzato in CIE Federation*
   * - **federation_status_endpoint**
     - URL
     - OBBLIGATORIO. Url presso il quale è possibile validare l’assegnazione di un Trust Mark ad uno specifico soggetto.

       *Non contestualizzato in CIE Federation*
   * - **homepage_uri**
     - URL
     - Url della pagina web del Trust Anchor o SA.

       *Non contestualizzato in CIE Federation*
   * - **organization_name**
     - String
     - Nome umanamente leggibile di questa entità.

       *Non contestualizzato in CIE Federation*

