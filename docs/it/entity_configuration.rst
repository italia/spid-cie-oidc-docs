.. include:: ./common_definitions.rst


.. _Entity_Configuration:

Entity Configuration
--------------------

Un'**Entity Configuration (EC)** è un Metadata di Federazione in formato Jose e firmato dal soggetto che lo emette e riguardante se stesso.

.. _firma_EC:

Firma della Entity Configuration
++++++++++++++++++++++++++++++++

La firma dei JWT :rfc:`7515` avviene mediante l'algoritmo RSA SHA-256 (RS256). Tutti i partecipanti della Federazione DEVONO supportare questo algoritmo di firma. Tutte le operazioni di verifica della firma relative agli ES, EC e TM sono eseguite con le chiavi pubbliche di Federazione (distinguiamo le chiavi di Federazione da quelle di OIDC Core. Questi ultimi risiedono nei Metadata OIDC. Un ES o EC contiene sia le chiavi pubbliche di Federazione che i Metadata OIDC).



Entity Configuration - claim comuni
+++++++++++++++++++++++++++++++++++

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **iss**
     - String. Identificativo dell'entità che lo emette. 
     - |spid-icon| |cieid-icon|
   * - **sub**
     - String. Identificativo del soggetto a cui è riferito. 
     - |spid-icon| |cieid-icon|
   * - **iat**
     - UNIX Timestamp con l'istante di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`
     - |spid-icon| |cieid-icon| 
   * - **exp**
     - UNIX Timestamp con l'istante di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
     - |spid-icon| |cieid-icon|
   * - **jwks**
     - Un JSON Web Key Set (JWKS) :rfc:`7517` che rappresenta la parte pubblica delle chiavi di firma dell'entità interessata. Ogni JWK nel set JWK DEVE avere un ID di chiave (claim kid).
     - |spid-icon| |cieid-icon|
   * - **metadata**
     - JSON Object. Ogni chiave dell'oggetto JSON rappresenta un identificatore del tipo 
       di :ref:`Metadata<metadata_oidc>` e ogni valore DEVE essere un oggetto JSON 
       che rappresenta i Metadata secondo lo schema di Metadata di quel tipo. 

       Una configurazione di entità PUÒ contenere più dichiarazioni di Metadata, ma solo una per ogni tipo di Metadata (<**entity_type**>). 

       I tipi consentiti sono i seguenti:

       - openid_relying_party
       - openid_provider
       - federation_entity
       - oauth_authorization_server
       - oauth_resource
       - trust_mark_issuer
     - |spid-icon| |cieid-icon|

.. warning::
  All'interno dell'EC i valori degli attributi **iss** e **sub** contengono il medesimo valore (URL).


Entity Configuration Foglia e intermediari
++++++++++++++++++++++++++++++++++++++++++

Gli EC delle entità Foglia e intermediari, in aggiunta ai claim precedentemente definiti, contengono anche i seguenti claim:

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **authority_hints**
     - Array di URL. Contiene una lista di URL delle entità superiori, quali TA o SA che POSSONO emettere un ES relativo a questo soggetto. 
     - |spid-icon| |cieid-icon|
   * - **trust_marks**
     - Un array JSON contenente i Trust Mark. Vedere la Sezione :ref:`Trust Mark <Trust_Mark>`. 
       Obbligatorio per tutti i partecipanti fatta esclusione del Trust Anchor. 
     - |spid-icon| |cieid-icon|



.. _entity_configuration_ta:

Entity Configuration Trust Anchor
+++++++++++++++++++++++++++++++++

Gli EC di un TA, in aggiunta ai claim comuni a tutti i partecipanti, contengono anche i seguenti:

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **constraints**
     - JSON Object che descrive un insieme di vincoli della Trust Chain e che DEVE contenere l'attributo **max_path_length**. Rappresenta il numero massimo di SA tra una Foglia e il TA. 
     - |spid-icon| |cieid-icon|
   * - **trust_marks_issuers**
     - JSON Array che indica quali autorità sono considerate attendibili nella Federazione per l'emissione di specifici TM, questi assegnati mediante il proprio identificativo univoco.
     - |spid-icon| |cieid-icon|

.. seealso:: 

   - :ref:`Esempio non normativo <Esempio_EN1.4>`
   
