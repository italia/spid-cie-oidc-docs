.. include:: ../common/common_definitions.rst

Logout
------

.. admonition:: |cieid-icon|

  RPs MAY establish individual sessions related to authenticated users. In cases where such individual sessions are instaurated by the RPs, the RPs MUST provide users with a logout functionality for the purpose of deleting the established individual session. 
  During the logout phase the RPs MUST revoke all the Access Tokens still active and related to user authentication, through the use of the revocation endpoint ( :ref:`Revocation Endpoint <Revocation_Endpoint>` ).  

  .. note::
    In case an *offline_access* mechanism via *Refresh Token* is supported by the OP, the latter MUST NOT be revoked following a logout.

