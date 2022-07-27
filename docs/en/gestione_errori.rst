.. include:: ../common/common_definitions.rst

Error Management
================

In case of errors, the OP displays error messages about the OpenID Connect interchanges, 
as described in the tables defined in the `SPID UX Guidelines`_. 
In case the guidelines require a user's redirect to the RP, the OP performs a redirect to the URL indicated 
in the parameter redirect_uri of the request (only if it is valid, i.e. it is present in the client Metadata), with the following parameters.


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **error**
     - Error code
     - |spid-icon| |cieid-icon|
   * - **error_description**
     - More detailed error description, aimed at helping the developers to debug. This message is not supposed
       to be displayed to the user (for this purpose, please see the `SPID UX Guidelines`_
     - |spid-icon| |cieid-icon|
   * - **state**
     - *state* value included in the Authentication Request. It is up to the client to test its
       correspondence to the one that has been sent in the Authentication Request.
     - |spid-icon| |cieid-icon|

Error codes 
-----------
TBD