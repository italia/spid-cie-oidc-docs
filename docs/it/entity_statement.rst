.. include:: ../common/common_definitions.rst

.. _Entity_Statement:

Entity Statement
----------------

Il componente basilare per costruire una Catena di Fiducia (Trust Chain) è l'**Entity Statement (ES)**, un JWT firmato che contiene le chiavi pubbliche delle entità discendenti e ulteriori dati usati per controllare il processo di risoluzione della Trust Chain. 

Una entità pubblica un **ES** relativo ad un suo discendente presso il proprio :ref:`Fetch Endpoint<federation_endpoint>`. L'entità superiore PUÒ definire le policy sui metadata dei soggetti discendenti e pubblicare i TM da lei emessi per questi.



Firma di Entity Statement
+++++++++++++++++++++++++

Si applicano le medesime considerazioni fatte per gli **EC** e riportate nella sezione :ref:`Firma della Entity Configuration<firma_EC>`.


Entity Statement
++++++++++++++++

Gli ES emessi dal TA o da un suo Intermediario per i propri diretti discendenti, contengono anche i seguenti attributi:

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **metadata_policy**
     - JSON Object che descrive un criterio di Metadata. Ogni chiave dell'oggetto JSON rappresenta un identificatore del tipo di Metadata e ogni valore DEVE essere un oggetto JSON che rappresenta la politica dei Metadata in base allo schema di quel tipo di Metadata. Si rimanda alla specifica `OIDC-FED#Section.5.1`_ per i dettagli implementativi.
     - |spid-icon| |cieid-icon|
   * - **trust_marks**
     - JSON Array contenente i Trust Mark emessi da se stesso per il soggetto discendente.
     - |spid-icon| |cieid-icon|


.. seealso:: 

   - `OIDC-FED#Section_3.1`_
   - :ref:`Esempio non normativo di Entity Statement<Esempio_EN2.1>`
