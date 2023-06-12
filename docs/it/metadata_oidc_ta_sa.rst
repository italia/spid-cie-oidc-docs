.. include:: ../common/common_definitions.rst

.. _MetadataTA:

Metadata di Trust Anchor (TA) e Intermediari (SA)
+++++++++++++++++++++++++++++++++++++++++++++++++

Un TA e un SA DEVONO pubblicare all'interno del loro EC un Metadata da *federation_entity* come riportato nel seguente esempio:

.. code-block:: json

 {
    "metadata":{
      "federation_entity":{
        ...
      }
    }
 }

L'EC di un TA e di SA DEVE configurare un metadata di tipo **"federation_entity"** e contenere almeno i seguenti parametri obbligatori:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Supportato da**
  * - **organization_name**
    - Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **homepage_uri**
    - Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **policy_uri**
    - Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **logo_uri**
    - URL del logo dell'entità; DEVE essere in formato SVG. Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **contacts**
    - PEC istituzionale dell'ente. Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **federation_fetch_endpoint**
    - Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **federation_list_endpoint**
    - Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **federation_trust_mark_status_endpoint**
    - Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **federation_resolve_endpoint**
    - Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|


.. seealso:: 

   - Esempio di EC di un :ref:`OP <Esempio_EN1.4>` e di un SA :ref:`SA <Esempio_EN1.3>`

   
