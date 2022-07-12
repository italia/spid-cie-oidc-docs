.. include:: ./common_definitions.rst


.. _Entity_Statement:

Entity Statement
----------------

Il componente basilare per costruire una Catena di Fiducia (Trust Chain) è l'**Entity Statement (ES)**, un JWT firmato che contiene le chiavi di firma delle entità e ulteriori dati usati per controllare il processo di risoluzione della Trust Chain. Quando uno statement è firmato da un'entità, viene chiamato *Entity Configuration (EC)*.

Firma di Entity Statement
+++++++++++++++++++++++++

Vedere :ref:`Firma della Entity Configuration<firma_EC>`


Metadata di Federazione
+++++++++++++++++++++++

OIDC Federation definisce i Metadata di Federazione contenenti le informazioni di seguito definite, e i Metadata OIDC per 
ogni tipo di entità.


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
   - :ref:`Esempio non normativo <Esempio_EN1.4>`

