.. include:: ../common/common_definitions.rst

.. _gestione_errori: 

Error Management
================

In case of errors the OP or the RP adopts the error messages described in the tables defined in the `SPID UX Guidelines`_. 
In case the guidelines require a user's redirect to the RP, the OP performs a redirect to the URL indicated 
in the parameter redirect_uri of the request (only if it is valid, i.e. it is present in the client Metadata), with the following parameters.


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **error**
     - Error code. See :ref:`Codici di errori <codici_errore>`
     - |spid-icon| |cieid-icon|
   * - **error_description**
     - More detailed error description, aimed at helping the developers to debug. This message is not supposed
       to be displayed to the user (for this purpose, please see the `SPID UX Guidelines`_
     - |spid-icon| |cieid-icon|
   * - **state**
     - REQUIRED only in case of error response in an Authentication Request. It MUST match the *state* value included in the Authentication Request. The RP MUST verify its
       correspondence to the one that has been sent in the Authentication Request.
     - |spid-icon| |cieid-icon|

.. _codici_errore:

Error codes 
-----------

.. warning::
  To Be Completed

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - **Error Code**
     - **Endpoint**
     - **Reference**
     - **Supported by**
   * - *invalid_request*
     - *Authorization*
     - :rfc:`6749#section-4.1.2.1`.
     - |cieid-icon|


