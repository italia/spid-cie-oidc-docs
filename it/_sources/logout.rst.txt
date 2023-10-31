.. include:: ../common/common_definitions.rst

Logout
------

.. admonition:: |cieid-icon|

  I RP POSSONO instaurare sessioni individuali relative agli utenti autenticati. Nei casi in cui tali sessioni individuali vengano instaurate dai RP, questi ultimi DEVONO fornire agli utenti una funzionalità di logout con lo scopo di eliminare la sessione individuale instaurata. 
  Durante la fase di logout i RP DEVONO revocare tutti gli Access Token ancora attivi e collegati all'autenticazione degli utenti, tramite l'utilizzo del revocation endpoint (:ref:`Revocation Endpoint <Revocation_Endpoint>`).  

  .. note::
    Nel caso sia supportato dall'OP un meccanismo di *offline_access* tramite *Refresh Token*, quest'ultimo NON DEVE essere revocato a seguito di un logout.


