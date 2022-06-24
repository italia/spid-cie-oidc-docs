.. include:: ./common_definitions.rst

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


Se un OP nei propri metadata non ha i claim **client_registration_types_supported** e/o **request_authentication_methods_supported** i valori da intendersi come impliciti sono i seguenti. 

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
     - String
     - Un URI che punta a un JWT firmato che come payload il JWK Set dell'entità (vedere esempio sotto). Il JWT è firmato
       con una chiave inclusa nel JWK che l'entità ha pubblicato nel suo Entity Statement autofirmato.
     - |uncheck-icon|

Vedere `OIDC-FED#OP_metadata`_


Ogni OP DEVE esporre all’interno dei propri metadati i seguenti claim obbligatori.

.. list-table:: 
   :widths: 20 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Tipo**
     - **Descrizione**
     - **Obbligatorio**
   * - **organization_name**
     - String
     - Un nome leggibile che rappresenta l'organizzazione proprietaria dell'OP. 
     - |check-icon|
   * - **jwks**
     - JSON
     - JSON Web Key Set :rfc:`7517#appendix-A.1`
     - |check-icon| in assenza del claim **signed_jwks_uri**. 
   * - **signed_jwks_uri**
     - String
     - URL del JWT auto firmato e verificabile con la chiave pubblica di Federazione (JWK). 
     - |check-icon| in assenza del claim **jwks**. 

Vedere `OIDC-FED#OP_metadata`_


