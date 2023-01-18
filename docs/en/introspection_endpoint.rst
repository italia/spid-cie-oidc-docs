.. include:: ../common/common_definitions.rst

Introspection Endpoint
----------------------

The Introspection Endpoint exposed by the OP, allows the RPs to obtain information 
about a token in their possession, as for example its validity.

.. seealso::

 - https://tools.ietf.org/html/rfc7662
 - https://openid.net/specs/openid-igov-oauth2-1_0-03.html#Section-3.2.2

Request
+++++++

The request to the Introspection Endpoint contains the token,
together with a Client Assertion that allows authenticating the RP that makes the request.


**Example:**

.. code-block:: http

 POST /introspection HTTP/1.1
 Host: https://op.spid.agid.gov.it
 Content-Type: application/x-www-form-urlencoded

 client_assertion=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiw
 ibmFtZSI6IlNQSUQiLCJhZG1pbiI6dHJ1ZX0.LVyRDPVJm0S9q7oiXcYVIIqGWY0wWQlqxvFGYswLF88…
 &
 client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwtbearer&
 client_id=https%3A%2F%2Frp.spid.agid.gov.it&
 token=eyJhbGciOiJSUzI1NiJ9.eyJleHAiOjE0MTg3MDI0MTQsImF1ZCI6WyJlNzFmYjcyYS05NzRmLT
 QwMDEtYmNiNy1lNjdjMmJjMDAzN2YiXSwiaXNzIjoiaHR0cHM6XC9cL2FzLXZhLmV4YW1wbGUuY29tXC8
 iLCJqdGkiOiIyMWIxNTk2ZC04NWQzLTQzN2MtYWQ4My1iM2YyY2UyNDcyNDQiLCJpYXQiOjE0MTg2OTg4
 MTR9.FXDtEzDLbTHzFNroW7w27RLk5m0wprFfFH7h4bdFw5fR3pwiqejKmdfAbJvN3_yfAokBv06we5RA
 RJUbdjmFFfRRW23cMbpGQCIk7Nq4L012X_1J4IewOQXXMLTyWQQ_BcBMjcW3MtPrY1AoOcfBOJPx1k2jw
 RkYtyVTLWlff6S5gKciYf3b0bAdjoQEHd_IvssIPH3xuBJkmtkrTlfWR0Q0pdpeyVePkMSI28XZvDaGnxA4j7QI5loZYeyzGR9
 h70xQLVzqwwl1P0-F_0JaDFMJFO1yl4IexfpoZZsB3HhF2vFdL6D_lLeHRyH2g2OzF59eMIsM_Ccs4G47862w…


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **client_assertion**
     - JWT signed with the Relying Party's private key, containing the same parameters as documented 
       for the requests to the Token Endpoint. The OP must test the validity of all the fields that
       are present in the JWT, plus the validity of its signature, 
       with respect to the parameter **client_id**.
     - |spid-icon| |cieid-icon|
   * - **client_assertion_type**
     - String. Allowed values: **urn:ietf:params:oauth:clientassertion-type:jwt-bearer**
     - |spid-icon| |cieid-icon| 
   * - **client_id**
     - URI that unquely identifies the RP. The OP must check that the client_id is known inside the 
       Federation.
     - |spid-icon| |cieid-icon| 
   * - **token**
     - The token about which the RP wants to obtain information.
     - |spid-icon| |cieid-icon|  


Response
++++++++

The Introspection Endpoint responds with a JSON Object defined as follows.

**Example:**

.. code-block:: json

 {
     "active":true
 }

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **active**
     - Boolean value that indicates the token validity. If the token is expired, it has been revoked or it
       has never been issued for the calling client_id, the Introspection Endpoint must return false.
     -  |spid-icon| |cieid-icon|
   * - **scope**
     - List of scopes required in the Authorization Request.
     -  |spid-icon|
   * - **exp**
     - Token expiration.
     -  |spid-icon|
   * - **sub**
     - Subject identifier. The same released in the ID Token. The RP MUST verify that the value is the same contained in the ID Token.
     -  |spid-icon|
   * - **client_id**
     - URI of the RP registered in the federation. The RP MUST verify that the value is the same of the own client_id.
     -  |spid-icon|
   * - **iss**
     - OP identified registered in the federation in Uniform Resource Locator (URL) format. The RP MUST verify that the value is the same of the OP queried.
     -  |spid-icon|
   * - **aud**
     - RP client ID. The RP MUST verify that the value is the same of the own client ID.
     -  |spid-icon|

Error Codes
+++++++++++

As defined for :ref:`Token endpoint<TOKEN_ENDPOINT_ERRORS>`.
