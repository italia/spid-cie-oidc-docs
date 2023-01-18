.. include:: ../common/common_definitions.rst

.. _errors_federation:

Gestione degli errori di federazione
++++++++++++++++++++++++++++++++++++

In caso di errore durante le operazioni di federazione, le entità DEVONO rappresentare i messaggi di anomalia come descritto di seguito.


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **Errore**
     - Vedi :ref:`Codici di errori <codici_errore_federation>`
     - |spid-icon| |cieid-icon|
   * - **Descrizione dell'errore**
     - Descrizione più dettagliata dell'errore, finalizzata ad aiutare lo sviluppatore per eventuale debugging. 
     - |spid-icon| |cieid-icon|


.. _codici_errore_federation:

Codici di errore di Federation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Errore**
    - **Descrizione**
    - **Codice HTTP**
    - **Supportato da**
  * - *temporarily_unavailable*
    - Uno degli endpoint di well-known o di Federation non è raggiungibile.
    - *302 Found* or *400 Bad Request*
    - |spid-icon| |cieid-icon|
  * - *invalid_client*
    - Il Client non è autorizzato perchè la validazione della Trust Chain fallisce.
    - *302 Found*
    - |spid-icon| |cieid-icon|
  * - *unauthorized_client*
    - L'applicazione del metadata policy produce un metadata non conforme o nessun Trust Mark valido per il profilo richiesto è presente all'interno della configurazione.
    - *302 Found*
    - |spid-icon| |cieid-icon|
  * - *invalid_request*
    - La richiesta non è completa o non è conforme a quanto definito dalle presenti specifiche tecniche.
    - *400 Bad Request*
    - |spid-icon| |cieid-icon|
  * - *not_found*
    - La risorsa richiesta non è stata trovata.
    - *404 Not Found*
    - |spid-icon| |cieid-icon|



