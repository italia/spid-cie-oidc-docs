.. include:: ../common/common_definitions.rst

Introspection Endpoint (token validity check) 
---------------------------------------------

The Introspection Endpoint exposed by the OP, allows the RPs to obtain information 
about a token in their possession, as for example its validity.

.. seealso::

 - https://tools.ietf.org/html/rfc7662
 - https://openid.net/specs/openid-igov-oauth2-1_0-03.html#rfc.section.3.2.2

Request
+++++++

The request to the Introspection Endpoint consists of sending the token about which to obtain information,
together with a Client Assertion that allows authenticating the RP that makes the request.


**Example:**

.. code-block:: 

 POST /introspection?
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

 Host: https://op.spid.agid.gov.it
 HTTP/1.1
 

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Required**
   * - **client_assertion**
     - JWT signed with the Relying Party's private key, containing the same parameters as documented 
       for the requests to the Token Endpoint. The OP must test the validity of all the fields that
       are present in the JWT, plus the validity of its signature, 
       with respect to the parameter **client_id**.
     - 
   * - **client_assertion_type**
     - String. Allowed values: **urn:ietf:params:oauth:clientassertion-type:jwt-bearer**
     - 
   * - **client_id**
     - URI that unquely identifies the RP. The OP must check that the client_id is known inside the 
       Federation.
     - 
   * - **token**
     - The token about which the RP wants to obtain information.
     - 


Response
++++++++

The Introspection Endpoint responds with a JSON Object defined as follows.

**Example:**

.. code-block:: 

 {
     "active":true
 }

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Required**
   * - **active**
     - Boolean value that indicates the token validity. If the token is expired, it has been revoked or it
       has never been issued for the calling client_id, the Introspection Endpoint must return false.
     - 

	 
Errors
++++++

In case of errors, the OP returns an HTTP 401 code with a JSON in the body, having the elements indicated below.

**Example:**

.. code-block:: 

 {
     "error":"invalid_client",
     "error_description":"client_id not recognized."
 }


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Required**
   * - **error**
     - Error code (see table below)
     - 
   * - **error_description**
     - More detailed error description, aimed at helping the developers to debug. This message is not intended
       to be displayed to the users (for this purpose, please refer to the `SPID UX Guidelines`_).
     - 


Following, the error codes:

.. list-table:: 
   :widths: 70 30
   :header-rows: 1

   * - Scenario
     - Error code
   * - The client_id indicated in the request is not recognized.
     - **invalid_client**
   * - The request is not valid because of lack or incorrectness of one or more parameters.
     - **invalid_request**
   * - The OP has encountered an internal problem.
     - **server_error**
   * - The OP has encountered a temporary internal problem. 
     - **temporarily_unavailable**


.. seealso:: 

 - https://tools.ietf.org/html/rfc7662#section-2.3

