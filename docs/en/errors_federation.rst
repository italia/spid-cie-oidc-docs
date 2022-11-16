.. include:: ../common/common_definitions.rst

.. _errors_federation:

Federation error management
+++++++++++++++++++++++++++

In case of errors during Federation operations, entities MUST give anomaly messages as following.


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **error**
     - See :ref:`Federation error codes <codici_errore_federation>`
     - |spid-icon| |cieid-icon|
   * - **error_description**
     - Error description.
     - |spid-icon| |cieid-icon|


.. _codici_errore_federation:

Federation error codes
^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Erro**
    - **Description**
    - **HTTP Code**
    - **Supported by**
  * - *temporarily_unavailable*
    - well-known or Federation endpoint is unreachable.
    - *302 Found*/*400 Bad Request*
    - |spid-icon| |cieid-icon|
  * - *invalid_client*
    - The Trust Chain validation fails and the Client is not authorized.
    - *302 Found*
    - |spid-icon| |cieid-icon|
  * - *unauthorized_client*
    - Applying the metadata policy results in a metadata not compliant or no valid Trust Mark for the requested profile is present within the configuration.  
    - *302 Found*
    - |spid-icon| |cieid-icon|
  * - *invalid_request*
    - The request is incomplete or does not comply with current specifications.
    - *400 Bad Request*
    - |spid-icon| |cieid-icon|
  * - *not_found*
    - The required resource is not found.
    - *404 Not Found*
    - |spid-icon| |cieid-icon|



