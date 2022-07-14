.. include:: ./common_definitions.rst

OpenID Connect Federation Entity Metadata
+++++++++++++++++++++++++++++++++++++++++

È il Metadata che il Trust Anchor, o suo Intermediario, pubblica con l'identificativo **federation_entity**, come segue.

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
     - **Supportato da**
   * - **federation_fetch_endpoint**
     - String. Url presso il quale sono pubblicati gli Entity Statements in formato JWT dei soggetti discendenti. Vedere `OIDC-FED#Section.7.1.1`_
     - |spid-icon| |cieid-icon|
   * - **federation_list_endpoint**
     - String. Url presso il quale è possibile ottenere la lista dei discendenti in formato JSON.
     - |spid-icon| |cieid-icon|
   * - **federation_resolve_endpoint**
     - String. Url presso il quale è possibile ottenere i Trust Mark validati, il Metadata finale e la Trust Chain, relativamente ad un soggetto.
     - |spid-icon| |cieid-icon|
   * - **federation_status_endpoint**
     - String. Url presso il quale è possibile validare l'assegnazione di un Trust Mark ad uno specifico soggetto.
     - |spid-icon| |cieid-icon| 
   * - **homepage_uri**
     - String. Url della pagina web del Trust Anchor o SA.
     - |spid-icon| |cieid-icon|
   * - **organization_name**
     - String. Nome umanamente leggibile di questa entità. 
     - |spid-icon| |cieid-icon|

Vedere `OIDC-FED#Federation_Entity`_

