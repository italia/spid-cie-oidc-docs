.. include:: ../common/common_definitions.rst

.. _MetadataTA:

Metadata di Trust Anchor (TA) e Intermediari (SA)
+++++++++++++++++++++++++++++++++++++++++++++++++

Un TA e un SA DEVONO pubblicare all'interno del loro EC un Metadata da *federation_entity* come riportato nel seguente esempio:

.. code-block:: 

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
    - {{TO_VERIFY}}. Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **homepage_uri**
    - {{TO_VERIFY}}Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **policy_uri**
    - {{TO_VERIFY}}Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **logo_uri**
    - {{TO_VERIFY}}URL del logo dell'entità; DEVE essere in formato SVG. Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **contacts**
    - {{TO_VERIFY}}PEC istituzionale dell'ente. Vedi Sezione 4.8 di `OIDC-FED`_
    - |spid-icon| |cieid-icon|
  * - **federation_fetch_endpoint**
    - OBBLIGATORIO. Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **federation_list_endpoint**
    - OBBLIGATORIO. Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **federation_trust_mark_status_endpoint**
    - OBBLIGATORIO. Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **federation_resolve_endpoint**
    - OBBLIGATORIO. Vedi Sezione :ref:`Endpoint di Federazione <federation_endpoint>` e `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|


.. seealso:: 

   - Esempio di EC di un :ref:`OP <Esempio_EN1.4>` e di un SA :ref:`SA <Esempio_EN1.3>`

   
