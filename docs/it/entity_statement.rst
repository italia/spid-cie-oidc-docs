.. include:: ./common_definitions.rst


.. _Entity_Statement:

Entity Statement
----------------

Il componente basilare per costruire una Catena di Fiducia (Trust Chain) è l'**Entity Statement (ES)**, un JWT crittografico che contiene le chiavi di firma delle entità e ulteriori dati usati per controllare il processo di risoluzione della Trust Chain (come l'*authority_hints* che specifica chi è il superiore di un'entità). Quando uno statement è autofirmato da un’entità, viene chiamato *Entity Configuration (EC)*.

Firma di Entity Statement
+++++++++++++++++++++++++

Vedere :ref:`Firma di Entity Configuration<firma_EC>`


Metadata di Federazione
+++++++++++++++++++++++

OIDC Federation definisce i metadata di federazione contenenti le informazioni di seguito definite, e i metadata OIDC per 
ogni tipo di entità.


Entity Statement
++++++++++++++++

Gli ES emessi dal TA o da un suo Intermediario per i propri diretti discendenti, contengono anche i seguenti attributi:

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **metadata_policy**
     - JSON Object che descrive un criterio di metadati. Ogni chiave dell'oggetto JSON rappresenta un identificatore del tipo di metadati e ogni valore DEVE essere un oggetto JSON che rappresenta la politica dei metadati in base allo schema di quel tipo di metadati. Si rimanda alla specifica `OIDC-FED#Section.5.1`_ per i dettagli implementativi.
     - |check-icon|
   * - **trust_marks**
     - JSON Array contenente i Trust Mark emessi da se stesso per il soggetto discendente.
     - |check-icon|


.. seealso:: 

   - `OIDC-FED#Section_3.1`_
   - :ref:`Esempio non normativo <Esempio_EN1.4>`

