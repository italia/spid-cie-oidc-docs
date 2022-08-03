.. include:: ../common/common_definitions.rst

.. _gestione_errori:

Gestione degli errori
+++++++++++++++++++++

In caso di errore, l'OP o il RP rappresentano i messaggi di anomalia relativi agli scambi OpenID
Connect, come descritti nelle relative tabelle definite dalle `Linee Guida UX SPID`_. Nei casi in cui tali linee
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
     - Descrizione più dettagliata dell'errore, finalizzata ad aiutare lo sviluppatore per eventuale debugging. Questo messaggio non è 
       destinato ad essere visualizzato all'utente (a tal fine si faccia riferimento alle `Linee Guida UX SPID`_)
     - |spid-icon| |cieid-icon|
   * - **state**
     - Parametro obbligatorio solo nel caso di risposta di errore alla *Authentication Request* e DEVE essere uguale al valore *state* incluso nella *Authentication Request*.  Il RP DEVE verificare che corrisponda a quello inviato nella *Authentication Request*.
     - |spid-icon| |cieid-icon|


.. _codici_errore:

Codici di errore
----------------

.. warning::
  Sezione da completare

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - **Error Code**
     - **Endpoint**
     - **Reference**
     - **Supportato da**
   * - *invalid_request*
     - *Authorization*
     - :rfc:`6749#section-4.1.2.1`.
     - |cieid-icon|


