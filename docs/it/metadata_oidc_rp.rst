.. include:: ./common_definitions.rst

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
     - Un nome leggibile che rappresenta l'organizzazione proprietaria dell'RP. 
     - |check-icon| 
   * - **jwks**
     - JSON
     - JSON Web Key Set :rfc:`7517#appendix-A.1`
     - |check-icon| in assenza del claim **signed_jwks_uri**. 
   * - **signed_jwks_uri**
     - String
     - URL del JWT auto firmato e verificabile con la chiave pubblica di Federazione (JWK). 
     - |check-icon| in assenza del claim **jwks**. 

Vedere `OIDC-FED#RP_metadata`_


