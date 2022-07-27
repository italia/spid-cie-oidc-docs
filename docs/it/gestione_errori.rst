.. include:: ../common/common_definitions.rst

Errori
++++++

In caso di errore, l'OP visualizza i messaggi di anomalia relativi agli scambi OpenID
Connect descritti nelle relative tabelle definite dalle `Linee Guida UX SPID`_. Nei casi in cui tali linee
guida prescrivono un redirect dell'utente verso il RP, l'OP effettua il redirect verso l'URL indicata
nel parametro redirect_uri della richiesta (solo se valido, ovvero presente nel client metadata), con
i seguenti parametri.


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **error**
     - Vedi :ref:`Codici di errori <codici_errore>`
     - |spid-icon| |cieid-icon|
   * - **error_description**
     - Vedi .Descrizione più dettagliata dell'errore, finalizzata ad aiutare lo sviluppatore per eventuale debugging. Questo messaggio non è 
       destinato ad essere visualizzato all'utente (a tal fine si faccia riferimento alle `Linee Guida UX SPID`_
     - |spid-icon| |cieid-icon|
   * - **state**
     - Valore *state* incluso nella Authentication Request.  Il client è tenuto a verificare che corrisponda a quello inviato nella Authentication Request.
     - |spid-icon| |cieid-icon|


.. _codici_errore:

Codici di errore
----------------
TBD


