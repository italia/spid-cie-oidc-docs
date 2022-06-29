.. include:: ./common_definitions.rst


.. _Trust_Mark:

Trust Mark
----------

I **Trust Mark (TM)**, letteralmente tradotti come *Marchi di Fiducia*, sono JWT firmati :rfc:`7515` e rappresentano la dichiarazione di conformità a un insieme ben definito di requisiti di fiducia e/o di interoperabilità o un accordo tra le parti coinvolte all’interno della Federazione. 

Lo scopo principale dei TM è quello di esporre alcune informazioni non richieste dal protocollo OpenID Connect Core ma che risultano utili in contesto Federativo.

Esempi tipici includono il codice di identificazione nazionale o internazionale dell’entità (Codice Fiscale, IPA Code, Partita IVA, VAT Number), i contatti istituzionali e altro, come definito in `OIDC-FED`_. Ulteriori dati possono essere aggiunti dall’emettitore, se resi comprensibili all’interno della Federazione.

I TM sono emessi e firmati, durante il processo di registrazione di una nuova entità di tipo **Foglia** (Onboarding), dal (TA) o suoi Intermediari (SA) o da Gestori Qualificati di Attributi (AA), se definiti all’interno dell’attributo **trust_mark_issuers**, pubblicato all’interno dell’Entity Configuration del TA. 

Ogni entità partecipante DEVE esporre nella propria configurazione (EC) i TM rilasciati dalle autorità emittenti. 


Validazione dei Trust Mark
++++++++++++++++++++++++++

Esistono due modi per validare un Trust Mark:

 1. Validazione **statica**. Il Trust Mark viene validato mediante la chiave pubblica dell’autorità che lo ha emesso (attributo **iss**), sulla base della corrispondenza dell’attributo **sub** con il medesimo attributo della Entity Configuration in cui è contenuto e sulla base del valore di scadenza (attributo **exp**).

 2. Validazione **dinamica**. I partecipanti della federazione possono interrogare l’endpoint :ref:`trust mark status<Trust_mark_status_endpoint>` erogato dal suo emittente (attributo iss) per la verifica in tempo reale dei TM da lui emessi. 

Tutti gli emittenti di Trust Mark DEVONO esporre un endpoint di trust mark status per consentire la validazione **dinamica**.

.. seealso:: 

  - `OIDC-FED#Section.5.3.2`_


Revoca dei Trust Mark
+++++++++++++++++++++

Un Trust Mark può essere revocato in qualsiasi momento. In caso di esclusione di un Soggetto Aggregato da parte della Autorità di Federazione, questa comunica al Soggetto Aggregatore l’esclusione dell’Aggregato. Di conseguenza il SA revoca il TM per il suo discendente.


Composizione dei Trust Mark 
+++++++++++++++++++++++++++

Gli attributi definiti all’interno dei TM aderiscono a quanto definito all’interno dello standard OIDC Federation 1.0 (`OIDC-FED`_). Segue la lista.

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Obbligatorio**
    * - **iss**
      - String. URL che identifica univocamente l’Autorità che lo ha emesso.
      - |check-icon|
    * - **sub**
      - String. URL che identifica univocamente il soggetto per il quale il Trust Mark è stato emesso.
      - |check-icon|
    * - **id**
      - String. Identificativo univoco del Trust Mark. È un URL con la seguente struttura:
        **<TA domain> / <entity_type> / <trustmark_profile> /**
        es non normativo: https://registry.servizicie.interno.gov.it/openid_relying_party/public/
      - |check-icon|
    * - **iat**
      - UNIX Timestamp. Quando è stato emesso questo marchio di fiducia. Espresso come “Seconds Since the Epoch” :rfc:`7519`.
      - |check-icon|
    * - **logo_uri**
      - String. Un URL che punta al logo rappresentante il Trust Mark.
      - |check-icon|
    * - **exp**
      - UNIX Timestamp. Momento oltre il quale non sarà più valido. Espresso come “Seconds Since the Epoch” :rfc:`7519` e corrispondente o inferiore alla durata della validità della convenzione amministrativa di adesione alla Federazione.
      - |check-icon|
    * - **ref**
      - String. URL che punta a informazioni presenti sul web relative a questo marchio di fiducia
      - |uncheck-icon|
    * - **organization_type**
      - String. Specifica se l’ente appartiene alla pubblica amministrazione italiana o al settore privato (**public** o **private**)
      - |check-icon|
    * - **id_code**
      - String. Codice di identificazione dell’organizzazione. A seconda del valore del tipo di organizzazione, deve essere
        indicato il codice IPA (per il tipo di organizzazione pubblica) o il numero di partita IVA (per quello privato).
      - |check-icon|
    * - **email**
      - String. Email istituzionale o PEC dell’organizzazione.
      - |check-icon|
    * - **organization_name**
      - String. Il nome completo dell’entità che fornisce i servizi
      - |check-icon|


.. seealso::

 * `OIDC-FED#Section.5.3.1`_



.. _Trust_mark_status_endpoint:

Trust mark status endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^

L’assegnazione di un Trust Mark ad un soggetto viene effettuato presso questo endpoint secondo le modalità definite all’interno di `OIDC-FED#Section.7.4`_.


.. toctree:: 
   :maxdepth: 1

   trust_marks_spid.rst
   trust_marks_cie.rst
