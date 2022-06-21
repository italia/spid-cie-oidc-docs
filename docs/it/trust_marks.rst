
Trust Marks
---------------------

I Trust Mark, letteralmente tradotti come marchi di fiducia, sono oggetti JSON firmati in formato Jose :rfc:`7515` e rappresentano la dichiarazione di conformità a un insieme ben definito di requisiti di fiducia e/o di interoperabilità o un accordo tra le parti coinvolte all’interno della Federazione. I Trust Marks sono rilasciati principalmente durante il processo di registrazione di una nuova entità di tipo Foglia (onboarding) dal Trust Anchor o suoi Intermediari.

Lo scopo principale di questi marchi di fiducia è quello di esporre alcune informazioni non richieste dal protocollo OpenID Connect Core ma che risultano utili in contesto Federativo.

Esempi tipici includono il codice di identificazione nazionale o internazionale dell'entità (Codice Fiscale, IPA Code, Partita IVA, VAT Number, etc.), i contatti istituzionali e altro. Ulteriori dati possono essere aggiunti dall'emittente se resi comprensibili all’interno della Federazione.

I Trust Marks riconoscibili all’interno della Federazione SPID sono emessi e firmati dalla AgID (TA) o suoi intermediari (SA) o dai Gestori di attributi qualificati (AA) se definiti all’interno del claim **trust_mark_issuers** pubblicato all’interno dell’Entity Configuration del TA. Ogni partecipante DEVE esporre nella propria configurazione (EC) i Trust Mark rilasciati dalle autorità emittenti. 

I Trust Mark rappresentano il primo filtro per l'instaurazione della fiducia tra le parti, sono elementi indispensabili per avviare la risoluzione dei metadati. *In loro assenza una entità non è riconoscibile come partecipante all’interno della Federazione SPID.*

All’interno della Federazione SPID i Trust Mark presentano degli identificativi univoci in formato URL che adottano la seguente struttura:

<domain> / <entity_type> / <trustmark_profile> /

Alcuni esempi non normativi sono di seguito riportati:

 - profilo RP public: https://registry.agid.gov.it/openid_relying_party/public/
 - profilo SA private: https://registry.agid.gov.it/federation_entity/private/



Validazione dei Trust Mark
++++++++++++++++++++++++++++++++

Esistono due modi per validare un Trust Mark:

 1. Validazione **statica**. Il Trust Mark viene validato mediante il certificato pubblico dell’autorità che lo ha emesso (claim **iss**), sulla base della corrispondenza del claim **sub** con il medesimo claim della Entity Configuration in cui è contenuto e sulla base del valore di scadenza (claim **exp**).

 2. Validazione **dinamica**. I partecipanti della federazione possono interrogare l'endpoint :ref:`trust mark status<Trust_mark_status_endpoint>` erogato dal suo emittente (claim iss) per la verifica in tempo reale dei TM da lui emessi. 

Tutti gli emittenti di Trust Mark DEVONO esporre un endpoint di trust mark status per consentire la validazione **dinamica**.


SPID: Revoca dei Trust Mark
+++++++++++++++++++++++++++

Un Trust Mark può essere revocato in qualsiasi momento. In caso di esclusione di un Soggetto Aggregato da parte della Autorità di Federazione, questa comunica al Soggetto Aggregatore l’esclusione dell'Aggregato. Di conseguenza il SA revoca il TM per il suo discendente.


SPID: Pubblicazione dei Trust Marks
+++++++++++++++++++++++++++++++++++

La TA definisce i TM e gli emittenti di questi abilitati nella Federazione mediante il claim **trust_mark_issuers**, presente all’interno del proprio Entity Configuration. Il valore del claim **trust_mark_issuers** è composto da un oggetto JSON, avente come chiavi gli id dei TM e come valori la lista degli emittenti abilitati.

Di seguito un esempio non normativo dell’oggetto **trust_mark_issuers** all’interno della Entity Configuration del TA.

.. code-block::

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


I TM emessi per le Foglie DEVONO essere pubblicati dalle stesse all’interno della proprie Entity Configuration, all’interno del claim **trust_marks**. Questo è composto da lista di oggetti JSON, ognuno di questi DEVE contenere almeno i claim **id** e **trust_mark**, il primo identifica il TM, il secondo contiene il JWT firmato del TM.

Di seguito un esempio non normativo dell’oggetto **trust_marks** all’interno della Entity Configuration di una Foglia di tipo RP.


.. code-block::

 "trust_marks": [
    {
      "id": "https://www.spid.gov.it/openid-federation/agreement/sp-public/", 
      "trust_mark": …
    }
 ]


SPID: Composizione dei Trust Mark 
+++++++++++++++++++++++++++++++++

I claim definiti all’interno dei Trust Marks aderiscono a quanto definito all’interno dello standard OIDC Federation 1.0 (documento giunto attualmente al DRAFT 18). Questi sono di seguito riportati.

.. list-table::
    :widths: 20 20 60
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
    * - **iss**
      - String
      - RICHIESTO. URL che identifica univocamente l’Autorità che lo ha emesso.
    * - **sub**
      - String
      - RICHIESTO. URL che identifica univocamente il soggetto per il quale il Trust Mark è stato emesso.
    * - **id**
      - String
      - RICHIESTO. Identificativo univoco del Trust Mark.
    * - **iat**
      - UTC Timestamp
      - RICHIESTO. Quando è stato emesso questo marchio di fiducia. Espresso come “Seconds Since the Epoch” :rfc:`7519`.
    * - **logo_uri**
      - String
      - OPZIONALE. Un URL che punta al logo rappresentante il Trust Mark.
    * - **exp**
      - UTC Timestamp
      - RICHIESTO. Momento oltre il quale non sarà più valido. Espresso come “Seconds Since the Epoch” :rfc:`7519` e corrispondente o inferiore alla durata della validità della convenzione amministrativa di adesione alla Federazione.
    * - **ref**
      - String
      - OPZIONALE. URL che punta a informazioni presenti sul web relative a questo marchio di fiducia

La seguente tabella riassume tutti i profili supportati per le entità di tipo RP coinvolte nella Federazione SPID.

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Tipo**
      - **Descrizione**
      - **Entità**
    * - **public**
      - Indica che il RP appartiene ad una Pubblica Amministrazione.
      - All
    * - **private**
      - Indica che il RP appartiene al settore privato.
      - All


Agli attributi dei TM definiti nella tabella precedente, i Trust Mark SPID aggiungono i seguenti.

.. list-table::
    :widths: 30 70 
    :header-rows: 1

    * - **Claims**
      - **Description**
    * - **organization_type**
      - RICHIESTO. Specifica se l'ente appartiene alla pubblica amministrazione italiana o al settore privato (private or public).
    * - **id_code**
      - RICHIESTO. Codice di identificazione dell'organizzazione; a seconda del valore del tipo di organizzazione deve essere indicato il codice IPA (per il tipo di organizzazione pubblica) o il numero di partita IVA (per quello privato).
    * - **email**
      - RICHIESTO. Email istituzionale o PEC dell'organizzazione.
    * - **organization_name**
      - RICHIESTO. Il nome completo dell'entità che fornisce i servizi



Quello che segue è un esempio non normativo di un marchio di fiducia emesso da AgID per un intermediario privato.

.. code-block::

 "trust_marks": [
  {
   "id":"https://registry.agid.gov.it/federation_entity/private/",
   "trust_mark": …
  }
 ]

Dove il contenuto del JWT firmato all’interno del claim **trust_mark** corrisponde a:

.. code-block::

 {
   "id":"https://registry.agid.gov.it/federation_entity/private/",
   "iss": "https://registry.agid.gov.it",
   "sub": "https://intermediary.example.it",
   "iat": 1579621160,
   "organization_type": "private",
   "id_code": "12345678900",
   "email": "email_or_pec@example.it",
   "organization_name": "Full name of the SA",
   "ref": "https://reference_to_some_documentation.example.it/"
 }

Un'entità intermediaria (SA) è riconoscibile come emittente di Trust Mark. Quello che segue è un esempio non normativo di un Trust Mark emesso da un Soggetto Aggregatore a favore di un RP suo discendente.

.. code-block::

 "trust_marks": [
  {
   "id":"https://registry.agid.gov.it/openid_relying_party/public/",
   "trust_mark": …
   }
 ]

Dove il contenuto del JWT firmato all’interno del claim **trust_mark** corrisponde al seguente esempio non normativo.

.. code-block::

 {
   "id":"https://registry.agid.gov.it/openid_relying_party/public/",
   "iss": "https://intermediary.example.it",
   "sub": "https://rp.example.it",
   "iat": 1579621160,
   "organization_type": "public",
   "id_code": "123456",
   "email": "email_or_pec@rp.it",
   "organization_name": "Full name of the RP",
   "ref": "https://reference_to_some_documentation.it/"
 }



Trust Mark della CIE
--------------------

I Trust Mark sono JSON Web Token (JWT) firmati che rappresentano una dichiarazione di conformità ad un insieme ben definito di requisiti di fiducia e/o interoperabilità, oppure ad un accordo fra le parti coinvolte nella Federazione e vengono emessi da entità accreditate, principalmente durante il processo di Onboarding. Lo scopo principale è convogliare alcune informazioni non propriamente richieste dal protocollo stesso OIDC, ma che potrebbero essere utili all'interno della Federazione. Tipici esempi includono il codice di identificazione nazionale dell'entità, contatti istituzionali e caratteristiche supportate disponibili all'interno dell'ecosistema CIE. Dati aggiuntivi possono essere aggiunti dall'emittente e devono essere ben compresi.

Nello scenario CIE, un Trust Mark viene firmato da **MinInterno** (TA) o da un'entità accreditata (es. entità intermedie (SA) o Autorità Attributo (AA) che giocano il ruolo di entità Risorse Protette OAuth - un'entità che agisce come AA all'interno del sistema della Federazione CIE, può essere visto come un tipo di entità Risorsa Protetta OAuth, in accordo a `[OIDC-FED#Section.4.5]`_) e DEVONO essere incluse nella richiesta (claim) dei Trust Mark della configurazione di entità delle foglie (RP e OP) e di intermediari (SA). La presenza di un Trust Mark è richiesta prima di iniziare una scoperta di metadati (vedere sezione), altrimenti la federazione può essere soddisfatta da aggressori che cercano di propagare attacchi. to propagate attacks.

Un Trust Mark può essere inoltrato dalla TA o da entità accreditate, come risultato di una procedura di Onboarding di federazione
o come risultato di un accordo fra le parti. Mentre nel secondo caso viene inoltrato solo un Trust Mark, durante il processo di Onboarding la FA deve anche esporre la dichiarazione di entità dell'entità imbarcata nei suoi endpoint di federazione.

CIE: Profili dei Trust Mark
+++++++++++++++++++++++++++

Si possono definire svariati profili in accordo agli specifici bisogni delle FA e della TA. Nella CIE FED, durante la fase
di Onboarding, DEVONO essere emessi almeno i seguenti *trustmark_profile*:

 - public: l'entità nel claim *sub* appartiene alla pubblica amministrazione italiana
 - private: l'entità nel claim *sub* appartiene al settore privato.

La tabella seguente riassume tutti i profili disponibili supportati per tutte le entità coinvolte nella CIE FED


.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Profilo TM**
      - **Descrizione**
      - **Tipi di entità sub**
    * - **public**
      - l'entità nel claim *sub* appartiene alla pubblica amministrazione italiana
      - Tutte
    * - **private**
      - l'entità nel claim *sub* appartiene al settore privato.
      - Tutte
    * - **web**
      - l'entità nel claim *sub* è compatibile con `[CIE-OIDC-CORE]`_
      - RP
    * - **native**
      - l'entità nel claim *sub* è compatibile con `[CIE-OIDC-MOBILE]`_ – non ancora supportato
      - RP
    * - **underage**
      - l'entità nel claim *sub* fornisce servizi online per underage in accordo a [] – non ancora supportato
      - RP
    * - **aggregator**
      - l'entità nel claim *sub* è un soggetto aggregatore in accordo a []
      - SA


CIE: Claim generali dei Trust Mark
++++++++++++++++++++++++++++++++++

La tabella sottostante riporta i claim considerati da OIDC-FED. Le specifiche permettono di aggiungere qualsiasi altro claim 
personalizzato, se richiesto.



.. list-table::
    :widths: 20 20 60
    :header-rows: 1

    * - **Claim**
      - **Tipo**
      - **Descrizione**
    * - **iss**
      - String
      - OBBLIGATORIO. L'emittente del Trust Mark
    * - **sub**
      - String
      - OBBLIGATORIO. L'entità alla quale il Trust Mark si applica
    * - **id**
      - String
      - OBBLIGATORIO. Un identificatore del Trust Mark
    * - **iat**
      - UTC Timestamp
      - OBBLIGATORIO. Quando questo Trust Mark è stato emesso. Espresso in seconds dall'inizio dell'epoca :rfc:`7519`
    * - **logo_uri**
      - String
      - OPZIONALE. Un URL che punta ad un logo che il soggetto può mostrare ad un utente dell'entità.
    * - **exp**
      - UTC Timestamp
      - OPZIONALE. Quando questo Trust Mark non è più valido. Espresso in seconds dall'inizio dell'epoca :rfc:`7519`.
        Se non è presente, significa che il Trust Mark è valido per sempre.
    * - **ref**
      - UTC Timestamp
      - OPZIONALE. URL che punta alle informazioni connesse all'emissione di questo Trust Mark


Nella Federazione CIE il claim id è un URL con la struttura seguente:


    <TA_domain> / <entity_type> / <trustmark_profile> 


Un esempio non normativo di id claim è il seguente:

 - https://registry.servizicie.interno.gov.it/openid_relying_party/public/

.. seealso::

 * `[OIDC-FED#Section.5.3.1]`_



CIE: Claim dei Trust Mark
+++++++++++++++++++++++++

Oltre ai Trust Mark definiti alla sezione precedente, la tabella sottostante mostra i claim che possono essere aggiunti per il processo di Onboarding.


.. list-table::
    :widths: 20 80
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
    * - **organization_type**
      - Specifica se l'entità appartiene all'aministrazione pubblica italiana on al settore privato (es. *private*, *public*)
    * - **id_code**
      - Codice identificativo dell'organizzazione; dipende dal valore di *organization_type*, deve essere dato il codice IPA (per il tipo pubblica amministrazione) o la Partita Iva (per i provati)
    * - **email**
      - Email istituzionale o PEC dell'organizzazione
    * - **organization_name**
      - Il nome completo dell'entità che fornisce i servizi


CIE: Esempi di Trust Mark
+++++++++++++++++++++++++

Il seguente è un esempio non normativo di un Trust Mark emesso da *MinInterno* per un'entità privata intermediaria.

.. code-block::

 "trust_marks": [
  {
   "id":"https://registry.servizicie.interno.gov.it/federation_entity/private/",
   "iss": "https://registry.servizicie.interno.gov.it",
   "trust_mark": $JWT
  }
 ]


Dove il payload JWT sarebbe come segue:

.. code-block::

 {
   "id":"https://registry.servizicie.interno.gov.it/federation_entity/private/",
   "iss": "https://registry.servizicie.interno.gov.it",
   "sub": "https://intermediate.example.it",
   "iat": 1579621160,
   "organization_type": "private",
   "id_code": "12345678900",
   "email": "email_or_pec@intermediate.it",
   "organization_name#it": "Full name of the SA",
   "ref": "https://reference_to_some_documentation.it/"
 }



Un'entità intermediaria dovrebbe essa stessa essere un emettitore di Trust Mark verso entità foglia (RP). Il seguente è un esempio non normativo di un Trust Mark emesso da un'entità intermediaria verso un'entità foglia RP.

.. code-block::

 "trust_marks": [
  {
   "id":"https://registry.servizicie.interno.gov.it/openid_relying_party/public/",
   "iss": "https://intermediary.example.it",
   "trust_mark": $JWT
   }
 ]


Dove il payload $JWT potrebbe essere come nel seguente esempio non normativo:

.. code-block::

 {
   "id":"https://registry.servizicie.interno.gov.it/openid_relying_party/public/",
   "iss": "https://intermediary.example.it",
   "sub": "https://rp.example.it",
   "iat": 1579621160,
   "organization_type": "public",
   "id_code": "123456",
   "email": "email_or_pec@rp.it",
   "organization_name#it": "Full name of the RP",
   "ref": "https://reference_to_some_documentation.it/"
 }



CIE: Trust Mark Attribute Authority
+++++++++++++++++++++++++++++++++++

Il registro degli AA è gestito da `[LG-AA]`_ che è responsabile dell'esecuzione del processo di Onboarding per gli AA che forniscono attributi qualificati “protected” e “private”. Come risultato, l'OP e la TA CIE DEVONO riconoscere l'AgID come emettitore di Trust Mark per gli AA. Oltre ai claim di Trust Mark descritti sopra, vengono aggiunti i seguenti claim.



.. list-table::
    :widths: 20 80
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
    * - **claims**
      - OBBLIGATORIO. attributi utente lookup richiesti dall'AA per fornire gli attributi richiesti.
    * - **service_documentation**
      - OPZIONALE. È un URL contenente la documentazione OAS3riferita all' AA in the claim *sub*, come definito in `[LG-AA]`_).
    * - **policy_uri**
      - OPZIONALE. URL ad una politica di privacy di AA
    * - **tos_uri**
      - OPZIONALE. URL ad una info policy di AA


Un esempio non normativo è dato qui sotto:

.. code-block::

 "trust_marks": [
  {
   "id":"https://registry.spid.gov.it/oauth_resource/aa/",
   "iss": "https://registry.spid.gov.it",
   "trust_mark": $JWT
  }
 ]

Dove il payload di JWT sarebbe come segue:

.. code-block::

 {
   "id":"https://registry.spid.gov.it/oauth_resource/aa/",
   "iss": "https://registry.spid.gov.it",
   "sub": "https://aa.example.it",
   "iat": 1579621160,
   "organization_type": "public",
   "id_code": "123456",
   "email": "email_or_pec@aa.it",
   "organization_name#it": "Full name of the AA",
   "policy_uri#it": "url to AA privacy policy",
   "tos_uri#it": "url to AA info policy",
   "service_documentation": "url to AA OAS3 document",
   "claims": {
      "https://attributes.eid.gov.it/fiscalNumber": {"essential": true},
      }  
   "ref": "https://reference_to_some_documentation.it/"
 }



CIE: Convalidare un Trust Mark
++++++++++++++++++++++++++++++

Un Trust Mark può essere revocato. Nello specifico:

L'emettitore di un Trust Mark PUÒ revocarlo direttamente

 1. TA requests the revocation of an aggregate from the SA, who must revoke its trust mark
 2. Osservazione: Per (1) TA può revocare i Trust Mark di SA direttamente.

Per convalidare un Trust Mark, i membri della Federazione possono interrogare lo status endpoint del Trust Mark, servito da un emettitore di Trust Mark (vedere sezione :ref:`Trust Mark Status<Trust_Mark_Status>`) per verificare se un Trust Mark è ancora valido (può essere revocato
dall'emettitore di Trust Mark).

L’endpoint riceve come input l’*entity_id* per l’entità verso la quale il Trust Mark è stato emesso (sub) e un identificatore del Trust Mark (id). Queste informazioni, assieme all'emettitore, formano la terna che identifica unicamente un Trust Mark.

Un’entità NON DEVE cercare di convalidare un Trust Mark finché non saprà quale TA. Nello scenario CIE, tutti gli emettitori di Trust Mark (*MinInterno* come TA e gli SA come intermediari) DEVONO esporre uno status endpoint di Trust Mark.

.. seealso:: 

  - `[OIDC-FED#Section.5.3.2]`_
