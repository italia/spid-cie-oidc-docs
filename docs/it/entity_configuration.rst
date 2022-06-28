.. include:: ./common_definitions.rst


.. _Entity_Configuration:

Entity Configuration
--------------------

Un **Entity Configuration (EC)** è un metadata di federazione in formato Jose e firmato dal soggetto che lo emette e riguardante se stesso.

.. _firma_EC:

Firma di Configuration
++++++++++++++++++++++

La firma dei JWT :rfc:`7515` avviene mediante l'algoritmo RSA SHA-256 (RS256). Tutti i partecipanti della Federazione DEVONO supportare questo algoritmo di firma. Tutte le operazioni di firma relative agli ES, EC e TM sono eseguite con le chiavi pubbliche di Federazione (distinguiamo le chiavi di Federazione da quelle di OIDC Core. Questi ultimi risiedono nei metadata OIDC. Un ES o EC contiene sia le chiavi pubbliche di Federazione che i metadata OIDC).


Metadata di Federazione
+++++++++++++++++++++++

OIDC Federation definisce i metadata di federazione contenenti le informazioni di seguito definite, e i metadata OIDC per 
ogni tipo di entità.


Entity Configuration comuni
+++++++++++++++++++++++++++

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **iss**
     - String. Identificativo dell'entità che lo emette. 
     - |check-icon|
   * - **sub**
     - String. Identificativo del soggetto a cui è riferito. 
     - |check-icon|
   * - **iat**
     - UNIX Timestamp. Sata di emissione. 
     - |check-icon|
   * - **exp**
     - UNIX Timestamp. Data di scadenza.
     - |check-icon|
   * - **jwks**
     - Un JSON Web Key Set (JWKS) :rfc:`7517` che rappresenta la parte pubblica delle chiavi di firma dell'entità interessata. Ogni JWK nel set JWK DEVE avere un ID chiave (claim kid).
     - |check-icon|
   * - **metadata**
     - JSON Object. Ogni chiave dell'oggetto JSON rappresenta un identificatore del tipo di metadati e ogni
       valore DEVE essere un oggetto JSON che rappresenta i metadati secondo lo schema di metadati di quel tipo. 

       Una configurazione di entità PUÒ contenere più dichiarazioni di metadati, ma solo una per ogni tipo di metadati (<**entity_type**>). 

       I tipi consentiti sono i seguenti:

       - **openid_relying_party**
       - **openid_provider**
       - **federation_entity**
       - **oauth_resource**
       - **trust_mark_issuer**
     - |check-icon|

.. warning::
  All’interno dell'EC i valori degli attributi **iss** e **sub** contengono il medesimo valore (URL).


Entity Configuration Foglia e Intermediari
++++++++++++++++++++++++++++++++++++++++++

Gli EC delle entità Foglia e Intermediari, in aggiunta ai claim precedentemente definiti, contengono anche i seguenti claim:

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **authority_hints**
     - Array di URLs. Contiene una lista di URL delle entità superiori, quali TA o SA che POSSONO emettere un ES relativo a questo soggetto. 
     - |check-icon|
   * - **trust_marks**
     - Un array JSON contenente i Trust Mark. Vedere la Sezione :ref:`Trust Mark <Trust_Mark>`.
     - |check-icon| per tutti i partecipanti fatta esclusione del Trust Anchor. 



.. _entity_configuration_ta:

Entity Configuration Trust Anchor
+++++++++++++++++++++++++++++++++

Gli EC di un TA, in aggiunta ai claim comuni a tutti i partecipanti, contengono anche i seguenti:

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **constraints**
     - JSON Object che descrive un insieme di vincoli della Trust Chain e che DEVE contenere l'attributo **max_path_length**. Rappresenta il numero massimo di ES fra questo ES e l'ultimo ES nella trust chain.
     - |check-icon|
   * - **trust_marks_issuers**
     - JSON array che indica quali autorità sono considerate attendibili nella federazione per l’emissione di specifici TM, questi assegnati mediante il proprio identificativo univoco.
     - |check-icon|
