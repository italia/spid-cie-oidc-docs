.. include:: ../common/common_definitions.rst

.. _MetadataTA:

Trust Anchor (TA) and Intermediate (SA) Metadata
++++++++++++++++++++++++++++++++++++++++++++++++

A TA and a SA MUST publish in the EC a Metadata of type *federation_entity*, as reported in the following example:

.. code-block:: json

 {
    "metadata":{
      "federation_entity":{
        ...
      }
    }
 }

The EC of a TA and a SA MUST configure a Metadata of type **"federation_entity"** and contain at least the following 
mandatory parameters:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Supported by**
  * - **organization_name**
    - See `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **homepage_uri**
    - See `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **policy_uri**
    - See `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **logo_uri**
    - URL of the entity's logo; it MUST be in SVG format. See `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **contacts**
    - Institutional certified email address (PEC) of the entity. See `OIDC-FED`_ Section 4.8
    - |spid-icon| |cieid-icon|
  * - **federation_fetch_endpoint**
    - See Section :ref:`Federation Endpoint <federation_endpoint>` and `OIDC-FED`_ Section 4.8.
    - |spid-icon| |cieid-icon|
  * - **federation_list_endpoint**
    - See Section :ref:`Federation Endpoint <federation_endpoint>` and `OIDC-FED`_ Section 4.8.
    - |spid-icon| |cieid-icon|
  * - **federation_trust_mark_status_endpoint**
    - See Section :ref:`Federation Endpoint <federation_endpoint>` and `OIDC-FED`_ Section 4.8.
    - |spid-icon| |cieid-icon|
  * - **federation_resolve_endpoint**
    - See Section :ref:`Federation Endpoint <federation_endpoint>` and `OIDC-FED`_ Section 4.8.
    - |spid-icon| |cieid-icon|


.. seealso:: 

   - Example of an EC of a :ref:`TA <Esempio_EN1.4>` and a SA :ref:`SA <Esempio_EN1.3>`

