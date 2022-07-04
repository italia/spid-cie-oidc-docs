.. include:: ./common_definitions.rst

OpenID Connect Federation Entity Metadata (FA)
++++++++++++++++++++++++++++++++++++++++++++++

È il metadata che il Trust Anchor, o suo Intermediario, pubblica con l'identificativo **federation_entity**, come segue.

.. code-block:: 

 {
     "metadata":{
         "federation_entity":{
             ...
         }
     }
 }


L'oggetto **federation_entity** è composto dai seguenti claim

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **federation_fetch_endpoint**
     - String. Url presso il quale sono pubblicati gli Entity Statements in formato JWT dei soggetti discendenti. Vedere `OIDC-FED#Section.7.1.1`_
     - |check-icon| 
   * - **federation_list_endpoint**
     - String. Url presso il quale è possibile ottenere la lista dei discendenti in formato JSON.
     - |check-icon| 
   * - **federation_resolve_endpoint**
     - String. Url presso il quale è possibile ottenere i Trust Mark validati, il metadata finale e la Trust Chain, 
       relativamente ad un soggetto.
     - |check-icon| 
   * - **federation_status_endpoint**
     - String. Url presso il quale è possibile validare l'assegnazione di un Trust Mark ad uno specifico soggetto.
     - |check-icon| 
   * - **homepage_uri**
     - String. Url della pagina web del Trust Anchor o SA.
     -      
   * - **organization_name**
     - String. Nome umanamente leggibile di questa entità. 
     - |check-icon| 

Vedere `OIDC-FED#Federation_Entity`_

