.. include:: ./common_definitions.rst


.. _Trust_Mark:

Trust Mark
==========

I **Trust Mark (TM)**, letteralmente tradotti come *Marchi di Fiducia*, sono JWT firmati :rfc:`7515` e rappresentano la dichiarazione di conformità ad un insieme ben definito di requisiti di fiducia e/o di interoperabilità o un accordo tra le parti coinvolte all'interno della Federazione. 

Lo scopo principale dei TM è quello di esporre alcune informazioni non richieste dal protocollo OpenID Connect Core ma che risultano utili in contesto Federativo.

Esempi tipici includono il codice di identificazione nazionale o internazionale dell'entità (Codice Fiscale, IPA Code, Partita IVA, VAT Number), i contatti istituzionali e altro, come definito in `OIDC-FED`_. Ulteriori dati possono essere aggiunti dal soggetto che li emette.

I TM sono emessi e firmati, durante il processo di registrazione di una nuova entità di tipo Foglia (Onboarding), dal (TA) o suoi Intermediari (SA) o da Gestori Qualificati di Attributi (AA), se definiti all'interno dell'attributo **trust_mark_issuers**, pubblicato all'interno dell'Entity Configuration del TA. 

Di seguito un esempio non normativo dell'oggetto **trust_marks_issuers** all'interno della Entity Configuration del TA.

.. code-block::

 {
     "trust_marks_issuers":{
         "https://registry.agid.gov.it/openid_relying_party/public/":[
             "https://registry.spid.agid.gov.it/",
             "https://public.intermediary.spid.it/"
         ],
         "https://registry.agid.gov.it/openid_relying_party/private/":[
             "https://registry.spid.agid.gov.it/",
             "https://private.other.intermediary.it/"
         ]
     }
 }


Ogni entità partecipante DEVE esporre nella propria configurazione (EC) i TM rilasciati dalle autorità che li emettono. 

Nello scenario CIE / SPID, un TM viene firmato dal TA **MinInterno** / **Agid** o loro Intermediari (SA) o Gestori Qualificati di Attributi (AA). 

Il TA definisce i soggetti abilitati all'emissione dei TM riconoscibili all'interno della Federazione, mediante il claim **trust_marks_issuers**, presente all'interno del proprio Entity Configuration. Il valore dell'attributo **trust_marks_issuers** è composto da un oggetto JSON avente come chiavi gli identificativi dei TM e come valori la lista degli identificativi (URL) delle entità abilitate ad emetterli.

I Trust Mark rappresentano il primo filtro per l'instaurazione della fiducia tra le parti, sono elementi indispensabili per avviare la risoluzione dei metadati. In loro assenza una entità non è riconoscibile come partecipante all’interno della Federazione.

All’interno della Federazione SPID i Trust Mark presentano degli identificativi univoci (claim id) in formato URL che adottano la seguente struttura: **https:// <domain> / <entity_type> / <trustmark_profile> / [estensione /]**

Alcuni esempi non normativi sono di seguito riportati:


 - TM RP public: **\https://registry.agid.gov.it/openid_relying_party/public/**
 - TM SA private: **\https://registry.agid.gov.it/federation_entity/private/full/**
 - TM AA: **\https://registry.agid.gov.it/oauth_resource/public/**


La tabella seguente definisce gli <entity_type> riconoscibili all'interno delle Federazioni SPID e CIE id:


.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - tipo
      - descrizione
      - entità
    * - **openid_relying_party**
      - l'entità nel claim *sub* è un RP.
      - RP
    * - **openid_provider**
      - l'entità nel claim *sub* è un OP.
      - OP
    * - **federation_entity**
      - l'entità nel claim *sub* è un Soggetto Aggregatore.
      - SA
    * - **oauth_resource**
      - l'entità nel claim *sub* è una Attribute Authority.
      - AA

La tabella seguente definisce i <trustmark_profile> riconoscibili all'interno delle Federazioni SPID e CIE id:


.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **profilo**
      - **descrizione**
      - **Entità**
    * - **public**
      - l'entità nel claim *sub* appartiene alla pubblica amministrazione italiana.
      - RP, OP, SA, AA
    * - **private**
      - l'entità nel claim *sub* appartiene al settore privato.
      - RP, OP, SA, AA


**federation_entity** Trust Mark
--------------------------------

In aggiunta ai claim dei profili **public** e **private**, il profilo **federation_entity** individua i SA e aggiungendo le estensioni **full** e **light**, 
a seconda della modalità con cui operano rispetto ai Soggetti Aggregati

.. seealso::

    Si veda Sezione :ref:`Soggetti aggregatori nel contesto Federativo <Soggetti_aggregatori>`

**oauth_resource**  Trust Mark
------------------------------------------

In aggiunta ai claim dei profili **public** e **private**, il profilo **oauth_resource** individua le AA e aggiunge i seguenti claim obbligatori:

.. list-table::
    :widths: 20 60
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
    * - **policy_uri**
      - URL dove è disponibile la privacy policy dell'AA. 
    * - **tos_uri**
      - URL dove è disponibile la info policy dell'AA. 
    * - **claims**
      - Lista di JSON Object che definiscono gli attributi dell’utente richiesti dall'AA. Esempio: |br| ``{"https://attributes.eid.gov.it/fiscal_number":{"essential":true},`` |br| ``"email":{"essential":true},}``
    * - **service_documentation**
      - URL dove è disponibile il documento OAS3 che descrive il funzionamento dei servizi dell'AA.

Validazione dei Trust Mark
--------------------------

Esistono due modi per validare un Trust Mark:

 1. Validazione **statica**. Il Trust Mark viene validato mediante la chiave pubblica dell'autorità che lo ha emesso (attributo **iss**), sulla base della corrispondenza dell'attributo **sub** con il medesimo attributo della Entity Configuration in cui è contenuto e sulla base del valore di scadenza (attributo **exp**).

 2. Validazione **dinamica**. I partecipanti della Federazione possono interrogare l'endpoint :ref:`trust mark status<federation_endpoint>` erogato dal suo emettitore (attributo iss) per la verifica in tempo reale dei TM da lui emessi. 

Tutte le entità che rilasciano Trust Mark DEVONO esporre un endpoint di Trust Mark status per consentire la validazione **dinamica**.

.. seealso:: 

  - `OIDC-FED#Section.5.3.2`_


Revoca dei Trust Mark
---------------------

Un Trust Mark può essere revocato in qualsiasi momento solo ed esclusivamente dal soggetto che lo ha emesso. Ad esempio, in caso di esclusione di un Soggetto Aggregato da parte della Autorità di Federazione, questa comunica al Soggetto Aggregatore l'esclusione dell'Aggregato. Di conseguenza il SA DEVE revocare il TM per il suo discendente. 

.. note::
  Nel caso di revoca di un TM, la validazione **dinamica** darà esito negativo, mentre la validazione **statica** continuerà a dare esito positivo, a meno di rotazioni delle chiavi crittografiche di firma del soggetto che ha rilasciato il TM. 

.. _ComposizioneTM:

Composizione dei Trust Mark 
---------------------------

Gli attributi definiti all'interno dei TM aderiscono a quanto definito all'interno dello standard OIDC Federation 1.0 (`OIDC-FED`_). Segue la lista.

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Supportato da**
    * - **iss**
      - String. URL che identifica univocamente l'Autorità che lo ha emesso.
      - |spid-icon| |cieid-icon|
    * - **sub**
      - String. URL che identifica univocamente il soggetto per il quale il Trust Mark è stato emesso.
      - |spid-icon| |cieid-icon|
    * - **id**
      - String. Identificativo univoco del Trust Mark. È un URL con la seguente struttura: |br|
        **<TA domain>/<entity_type>/<trustmark_profile>/** |br|
        es. non normativo: ``https://registry.interno.gov.it/openid_relying_party/public/``
      - |spid-icon| |cieid-icon|
    * - **iat**
      - UNIX Timestamp con l'istante di geerazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`
      - |spid-icon| |cieid-icon|
    * - **logo_uri**
      - String. Un URL che punta al logo rappresentante il Trust Mark.
      - |spid-icon| |cieid-icon|
    * - **exp**
      - UNIX Timestamp con l'istante di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`
      - |spid-icon| |cieid-icon|
    * - **ref**
      - String. URL che punta a informazioni presenti sul web relative a questo marchio di fiducia
      - |spid-icon| |cieid-icon|
    * - **organization_type**
      - String. Specifica se l'ente appartiene alla pubblica amministrazione italiana o al settore privato (**public** o **private**)
      - |spid-icon| |cieid-icon|
    * - **id_code**
      - String. Codice di identificazione dell'organizzazione. A seconda del valore del tipo di organizzazione, deve essere
        indicato il codice IPA (per il tipo di organizzazione pubblica) o il numero di partita IVA (per quello privato).
      - |spid-icon| |cieid-icon|
    * - **email**
      - String. Email istituzionale o PEC dell'organizzazione.
      - |spid-icon| |cieid-icon|
    * - **organization_name**
      - String. Il nome completo dell'entità che fornisce i servizi
      - |spid-icon| |cieid-icon|

.. warning::
  Nel caso di CIEid, le organizzazioni pubbliche che oltre al **codice IPA** dispongono anche di un **codice univoco AOO** DEVONO riportare quest'ultimo all'interno del parametro **id_code** secondo il seguente formato *"<IPA_code>-<AOO_code>"*.  Inoltre, il valore contenuto nel parametro **exp** NON DEVE essere superiore alla durata delle specifiche convenzioni/accordi stipulati in fase di onboarding tra il MinInterno e le organizzazioni che ricevono il TM.  

.. seealso::

 * `OIDC-FED#Section.5.3.1`_



.. toctree:: 
   :maxdepth: 1

   trust_marks_spid.rst
   trust_marks_cie.rst
