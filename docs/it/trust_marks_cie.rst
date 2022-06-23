.. include:: ./common_definitions.rst


Trust Mark per CIE
++++++++++++++++++

I Trust Mark sono JSON Web Token (JWT) firmati che rappresentano una dichiarazione di conformità ad un insieme ben definito di requisiti di fiducia e/o interoperabilità, oppure ad un accordo fra le parti coinvolte nella Federazione e vengono emessi da entità accreditate, principalmente durante il processo di Onboarding. Lo scopo principale è convogliare alcune informazioni non propriamente richieste dal protocollo stesso OIDC, ma che potrebbero essere utili all’interno della Federazione. Tipici esempi includono il codice di identificazione nazionale dell’entità, contatti istituzionali e caratteristiche supportate disponibili all’interno dell’ecosistema CIE. Dati aggiuntivi possono essere aggiunti dall’emittente e devono essere ben compresi.

Nello scenario CIE, un Trust Mark viene firmato da **MinInterno** (TA) o da un’entità accreditata (es. entità intermedie (SA) o Autorità Attributo (AA) che giocano il ruolo di entità Risorse Protette OAuth - un’entità che agisce come AA all’interno del sistema della Federazione CIE, può essere visto come un tipo di entità Risorsa Protetta OAuth, in accordo a `OIDC-FED#Section.4.5`_) e DEVONO essere incluse nella richiesta (attributo) dei Trust Mark della configurazione di entità delle foglie (RP e OP) e di intermediari (SA). La presenza di un Trust Mark è richiesta prima di iniziare una scoperta di metadati (vedere sezione), altrimenti la federazione può essere soddisfatta da aggressori che cercano di propagare attacchi. to propagate attacks.

Un Trust Mark può essere inoltrato dalla TA o da entità accreditate, come risultato di una procedura di Onboarding di federazione
o come risultato di un accordo fra le parti. Mentre nel secondo caso viene inoltrato solo un Trust Mark, durante il processo di Onboarding la FA deve anche esporre la dichiarazione di entità dell’entità imbarcata nei suoi endpoint di federazione.


Profili dei Trust Mark
^^^^^^^^^^^^^^^^^^^^^^

Si possono definire svariati profili in accordo agli specifici bisogni delle FA e della TA. Nella CIE FED, durante la fase
di Onboarding, DEVONO essere emessi almeno i seguenti *trustmark_profile*:

 - public: l’entità nel claim *sub* appartiene alla pubblica amministrazione italiana
 - private: l’entità nel claim *sub* appartiene al settore privato.

La tabella seguente riassume tutti i profili disponibili supportati per tutte le entità coinvolte nella CIE FED


.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Profilo TM**
      - **Descrizione**
      - **Tipi di entità sub**
    * - **public**
      - l’entità nel claim *sub* appartiene alla pubblica amministrazione italiana
      - Tutte
    * - **private**
      - l’entità nel claim *sub* appartiene al settore privato.
      - Tutte
    * - **web**
      - l’entità nell attributo *sub* è compatibile con CIE-OIDC-CORE
      - RP
    * - **native**
      - l’entità nell attributo *sub* è compatibile con CIE-OIDC-MOBILE – non ancora supportato
      - RP
    * - **underage**
      - l’entità nel claim *sub* fornisce servizi online per underage (non ancora supportato)
      - RP
    * - **aggregator**
      - l’entità nel claim *sub* è un soggetto aggregatore
      - SA


Claim generali dei Trust Mark
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La tabella sottostante riporta gli attributi considerati da OIDC-FED. Le specifiche permettono di aggiungere qualsiasi altro attributo 
personalizzato, se richiesto.



.. list-table::
    :widths: 20 20 40 20
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
      - **Obbligatorio**
    * - **iss**
      - String
      - L’emittente del Trust Mark
      - |check-icon|
    * - **sub**
      - String
      - L’entità alla quale il Trust Mark si applica
      - |check-icon|
    * - **id**
      - String
      - Un identificatore del Trust Mark
      - |check-icon|
    * - **iat**
      - UNIX Timestamp
      - Quando questo Trust Mark è stato emesso. Espresso in seconds dall'inizio dell'epoca :rfc:`7519`
      - |check-icon|
    * - **logo_uri**
      - String
      - Un URL che punta ad un logo che il soggetto può mostrare ad un utente dell’entità.
      - |check-icon|
    * - **exp**
      - UNIX Timestamp
      - Quando questo Trust Mark non è più valido. Espresso in seconds dall'inizio dell'epoca :rfc:`7519`.
        Se non è presente, significa che il Trust Mark è valido per sempre.
      - |check-icon|
    * - **ref**
      - UNIX Timestamp
      - URL che punta alle informazioni connesse all’emissione di questo Trust Mark
      - |uncheck-icon|


Nella Federazione CIE il attributo id è un URL con la struttura seguente:


    <TA_domain> / <entity_type> / <trustmark_profile> 


Un esempio non normativo di id attributo è il seguente:

 - https://registry.servizicie.interno.gov.it/openid_relying_party/public/

.. seealso::

 * `OIDC-FED#Section.5.3.1`_



Claim dei Trust Mark
^^^^^^^^^^^^^^^^^^^^

Oltre ai Trust Mark definiti alla sezione precedente, la tabella sottostante mostra gli attributi che possono essere aggiunti per il processo di Onboarding.


.. list-table::
    :widths: 20 20 40 20
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
      - **Obbligatorio**
    * - **organization_type**
      - String
      - Specifica se l’entità appartiene all’aministrazione pubblica italiana o al settore privato (es. *private*, *public*)
      - |uncheck-icon|
    * - **id_code**
      - String
      - Codice identificativo dell’organizzazione. Dipende dal valore di *organization_type*, deve essere dato il codice IPA (per il tipo pubblica amministrazione) o la Partita Iva (per i provati)
      - |uncheck-icon|
    * - **email**
      - String
      - Email istituzionale o PEC dell’organizzazione
      - 
    * - **organization_name**
      - String
      - Il nome completo dell’entità che fornisce i servizi
      - |uncheck-icon|


Esempi di Trust Mark
^^^^^^^^^^^^^^^^^^^^

Il seguente è un esempio non normativo di un Trust Mark emesso da *MinInterno* per un’entità privata intermediaria.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.servizicie.interno.gov.it/federation_entity/private/",
             "iss":"https://registry.servizicie.interno.gov.it",
             "trust_mark":"$JWT"
         }
     ]
 }


Dove il payload JWT sarebbe come segue:

.. code-block::

 {
     "id":"https://registry.servizicie.interno.gov.it/federation_entity/private/",
     "iss":"https://registry.servizicie.interno.gov.it",
     "sub":"https://intermediate.example.it",
     "iat":1579621160,
     "organization_type":"private",
     "id_code":"12345678900",
     "email":"email_or_pec@intermediate.it",
     "organization_name#it":"Full name of the SA",
     "ref":"https://reference_to_some_documentation.it/"
 }



Un’entità intermediaria dovrebbe essa stessa essere un emettitore di Trust Mark verso entità foglia (RP). Il seguente è un esempio non normativo di un Trust Mark emesso da un’entità intermediaria verso un’entità foglia RP.

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.servizicie.interno.gov.it/openid_relying_party/public/",
             "iss":"https://intermediary.example.it",
             "trust_mark":"$JWT"
         }
     ]
 }


Dove il payload $JWT potrebbe essere come nel seguente esempio non normativo:

.. code-block::

 {
     "id":"https://registry.servizicie.interno.gov.it/openid_relying_party/public/",
     "iss":"https://intermediary.example.it",
     "sub":"https://rp.example.it",
     "iat":1579621160,
     "organization_type":"public",
     "id_code":"123456",
     "email":"email_or_pec@rp.it",
     "organization_name#it":"Full name of the RP",
     "ref":"https://reference_to_some_documentation.it/"
 }



Trust Mark Attribute Authority
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il registro degli AA è gestito da `LG-AA`_ che è responsabile dell’esecuzione del processo di Onboarding per gli AA che forniscono attributi qualificati “protected” e “private”. Come risultato, l’OP e la TA CIE DEVONO riconoscere l’AgID come emettitore di Trust Mark per gli AA. Oltre agli attributi di Trust Mark descritti sopra, vengono aggiunti i seguentgli attributi.



.. list-table::
    :widths: 20 20 40 20
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
      - **Obbligatorio**
    * - **attributos**
      - 
      - attributi utente lookup richiesti dall’AA per fornire gli attributi richiesti.
      - |check-icon|
    * - **service_documentation**
      - String
      - È un URL contenente la documentazione OAS3riferita all’ AA in the attributo *sub*, come definito in `LG-AA`_).
      - |uncheck-icon|
    * - **policy_uri**
      - String
      - URL ad una politica di privacy di AA
      - |check-icon|
    * - **tos_uri**
      - String
      - URL ad una info policy di AA
      - |uncheck-icon|


Un esempio non normativo è dato qui sotto:

.. code-block::

 {
     "trust_marks":[
         {
             "id":"https://registry.spid.gov.it/oauth_resource/aa/",
             "iss":"https://registry.spid.gov.it",
             "trust_mark":"$JWT"
         }
     ]
 } 

Dove il payload di JWT sarebbe come segue:

.. code-block::

 {
     "id":"https://registry.spid.gov.it/oauth_resource/aa/",
     "iss":"https://registry.spid.gov.it",
     "sub":"https://aa.example.it",
     "iat":1579621160,
     "organization_type":"public",
     "id_code":"123456",
     "email":"email_or_pec@aa.it",
     "organization_name#it":"Full name of the AA",
     "policy_uri#it":"url to AA privacy policy",
     "tos_uri#it":"url to AA info policy",
     "service_documentation":"url to AA OAS3 document",
     "attributos":{
         "https://attributes.eid.gov.it/fiscalNumber":{
             "essential":true
         }
     },
     "ref":"https://reference_to_some_documentation.it/"
 }



Convalidare un Trust Mark
^^^^^^^^^^^^^^^^^^^^^^^^^

Un Trust Mark può essere revocato. Nello specifico:

L’emettitore di un Trust Mark PUÒ revocarlo direttamente

 1. TA requests the revocation of an aggregate from the SA, who must revoke its trust mark
 2. Osservazione: Per (1) TA può revocare i Trust Mark di SA direttamente.

Per convalidare un Trust Mark, i membri della Federazione possono interrogare lo status endpoint del Trust Mark, servito da un emettitore di Trust Mark (vedere sezione :ref:`Trust Mark Status<Trust_Mark_Status>`) per verificare se un Trust Mark è ancora valido (può essere revocato
dall’emettitore di Trust Mark).

L’endpoint riceve come input l’*entity_id* per l’entità verso la quale il Trust Mark è stato emesso (sub) e un identificatore del Trust Mark (id). Queste informazioni, assieme all’emettitore, formano la terna che identifica unicamente un Trust Mark.

Un’entità NON DEVE cercare di convalidare un Trust Mark finché non saprà quale TA. Nello scenario CIE, tutti gli emettitori di Trust Mark (*MinInterno* come TA e gli SA come intermediari) DEVONO esporre uno status endpoint di Trust Mark.

.. seealso:: 

  - `OIDC-FED#Section.5.3.2`_
