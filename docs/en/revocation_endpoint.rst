.. include:: ../common/common_definitions.rst

Revocation Endpoint (logout)
----------------------------

An RP MAY request the revocation of an Access Token or a Refresh Token issued by an OP.

When the user logs out, the RP MUST revoke the Access Token in its possession.

.. note::
  The Access Token revocation implies revoking all the Refresh Tokens linked to it.

The OP will have to revoke the token specified in the request and will have to end the Single Sign-On session, if it is still active.

.. seealso::

 - https://tools.ietf.org/html/rfc7009
 
Request
+++++++

The request to the Revocation Endpoint consists of sending the token to be revoked, together with a Client Assertion that allows the identification of the RP that makes the request.


**Example:**

.. code-block::

 POST /revoke?
 client_assertion=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiw
 ibmFtZSI6IlNQSUQiLCJhZG1pbiI6dHJ1ZX0.LVyRDPVJm0S9q7oiXcYVIIqGWY0wWQlqxvFGYswLF88&
 client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwtbearer&
 client_id=https%3A%2F%2Frp.spid.agid.gov.it&
 token=eyJhbGciOiJSUzI1NiJ9.eyJleHAiOjE0MTg3MDI0MTQsImF1ZCI6WyJlNzFmYjcyYS05NzRmLT
 QwMDEtYmNiNy1lNjdjMmJjMDAzN2YiXSwiaXNzIjoiaHR0cHM6XC9cL2FzLXZhLmV4YW1wbGUuY29tXC8
 iLCJqdGkiOiIyMWIxNTk2ZC04NWQzLTQzN2MtYWQ4My1iM2YyY2UyNDcyNDQiLCJpYXQiOjE0MTg2OTg4
 MTR9.FXDtEzDLbTHzFNroW7w27RLk5m0wprFfFH7h4bdFw5fR3pwiqejKmdfAbJvN3_yfAokBv06we5RA
 RJUbdjmFFfRRW23cMbpGQCIk7Nq4L012X_1J4IewOQXXMLTyWQQ_BcBMjcW3MtPrY1AoOcfBOJPx1k2jw
 RkYtyVTLWlff6S5gKciYf3b0bAdjoQEHd_IvssIPH3xuBJkmtkrTlfWR0Q0pdpeyVePkMSI28XZvDaGnxA4j7QI5loZYeyzGR9
 h70xQLVzqwwl1P0-F_0JaDFMJFO1yl4IexfpoZZsB3HhF2vFdL6D_lLeHRyH2g2OzF59eMIsM_Ccs4G47862w

 Host: https://op.spid.agid.gov.it
 HTTP/1.1


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Required**
   * - **client_assertion**
     - JWT signed with the Relying Party's private key, containing the same parameters as from the documentation of the Token Endpoint requests. The OP must test the validity of all the fields in the JWT, plus the validity of its signature, according to the parameter **client_id**.
     - 
   * - **client_assertion_type**
     - String. **urn:ietf:params:oauth:clientassertion-type:jwt-bearer**
     - 
   * - **client_id**
     - URL HTTPS that uniquely identifies the RP. 
     - 
   * - **token**
     - The token about which the RP requests information.
     - 
	 

Response
++++++++

The Revocation Endpoint answers with a code HTTP 200, also though the indicated token does not exist or has already been revoked (so that non information is going to be released).


