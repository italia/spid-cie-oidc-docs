.. include:: ../common/common_definitions.rst

.. _user_claims:

Tabella attributi utente
------------------------

.. list-table:: 
   :widths: 20 40 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Supportato da**
   * - **https://attributes.eid.gov.it/spid_code**
     - Codice identificativo (anagrafica). String. Il codice identificativo è assegnato dal gestore dell'identità digitale e deve essere univoco.

       Il formato è il seguente: <codice Identificativo> = <cod_IdP><nr. univoco>

       Dove:

         **<cod_IdP>**: è un codice composto da 4 lettere univocamente assegnato al gestore delle identità;

         **<nr.univoco>**: è una stringa alfanumerica composta da 10 caratteri che il gestore delle identità genera in maniera univoca nell'ambito del proprio dominio.

       Esempio: 

       .. code-block:: json

         "https://attributes.eid.gov.it/spid_cod": "ABCD123456789A"

     - |spid-icon|
   * - **given_name**
     - Nome (anagrafica). String. Stringa composta da una sequenza di parole con carattere iniziale maiuscolo,
       intervallate da spazi singoli.
       
       Esempio:

       .. code-block:: json
      
         "given_name": "Giovanni Mario"

     - |spid-icon| |cieid-icon|
   * - **family_name**
     - Cognome (anagrafica). String. Stringa composta da una sequenza di parole con carattere iniziale maiuscolo,
       intervallate da spazi singoli.

       Esempio:

       .. code-block:: json
       
         "family_name":"Bianchi Verdi"

     - |spid-icon| |cieid-icon|
   * - **place_of_birth**
     - Luogo di nascita, Provincia di nascita (anagrafica). JSON Object: 

       "**locality** : Stringa corrispondente al codice catastale (Codice Belfiore) del Comune 
       o della nazione estera di nascita (Es. "F205" per la città di Milano)

       "**region**" : Stringa corrispondente alla sigla della provincia di nascita

       Esempio:

       .. code-block:: json

        "place_of_birth":{
            "region":"MI",
            "locality":"F205"
        }

     - |spid-icon| |cieid-icon|
   * - **birthdate**
     - Data di nascita (anagrafica). String. Secondo specifica ISO8601-2004 nel formato
       YYYY indica l'anno utilizzando 4 cifre |br|
       MM indica il mese in (due) cifre |br|
       DD indica il giorno in (due) cifre |br|
       Esempio: |br|

       .. code-block:: json

         "birthdate":"2002-09-24"

     - |spid-icon| |cieid-icon|
   * - **gender**
     - Sesso (anagrafica). String. Valori ammessi: |br|
       "female" per sesso femminile |br|
       "male" per sesso maschile |br|
       Esempio: |br|

       .. code-block:: json

         "gender":"female"

     - |spid-icon| |cieid-icon|
   * - **https://attributes.eid.gov.it/company_name**
     - Ragione o denominazione sociale (anagrafica). String. Stringa composta da una sequenza di parole intervallate 
       da spazi singoli.
       In maiuscolo le sottostringhe corrispondenti a nomi (es. “Agenzia per l'Italia Digitale”)

       .. code-block:: json

         "company_name": "Agenzia per l'Italia Digitale"

     - |spid-icon|
   * - **https://attributes.eid.gov.it/registered_office**
     - Sede legale (extra anagrafica). JSON Object: formatted, street_address, locality, region, postal_code, country, 
       country_code.
       Json composto da una stringa composta da una sequenza di parole intervallate da spazi singoli rappresentanti:

       - Tipologia( via, viale, piazza …) 
       - Indirizzo 
       - Nr.civico 
       - CAP 
       - Luogo 
       - Provincia

       la stringa è inserita nel claim "formatted" del JSON Object "address"

       Esempio:

       .. code-block:: json

         "https://attributes.eid.gov.it/registered_office":{
             "formatted":"via Listz 21 00144 Roma"
         }

     - |spid-icon|
   * - **https://attributes.eid.gov.it/fiscal_number**
     - Codice fiscale della persona fisica (anagrafica). String. Per il formato si faccia riferimento alla codifica 
       dell'attributo CF per i certificati, proposta nell'ambito del Draft ETSI EN 319 412-1, 
       che nel caso specifico prevede la seguente composizione:
       TINIT-<CodiceFiscale>
        
       Esempio:

       .. code-block:: json

          "https://attributes.eid.gov.it/fiscal_number": “TINIT-ABCXYZ00W00Z000Z"

     - |spid-icon| |cieid-icon|
   * - **https://attributes.eid.gov.it/**
     - Codice fiscale Persona Giuridica (anagrafica). String. Per il formato si faccia riferimento alla codifica dell'attributo CF per i certificati, proposta
       nell'ambito del Draft ETSI EN 319 412-1, che nel caso specifico prevede la seguente composizione:

       TINIT-segue il codice fiscale

        .. code-block:: json

          "https://attributes.eid.gov.it/company_fiscalNumber":"TINIT-ABCXYZ00W00Z000Z"

     - |spid-icon|
   * - **https://attributes.eid.gov.it/vat_number**
     - Partita IVA (anagrafica). String. Per il formato si faccia riferimento alla codifica dell'attributo Partita IVA per i certificati,
       proposta nell'ambito del Draft ETSI EN 319 412-1, che nel caso specifico prevede la seguente composizione:

       VATIT-<PartitaIVA>

       Esempio:

       .. code-block:: json

          "https://attributes.eid.gov.it/vat_number": "VATIT-12345678901"

     - |spid-icon|
   * - **document_details**
     - Documento d'identità (extra anagrafica). JSON Object (document):

       Json contenente le proprietà che rappresentano:

        - "**type**" : valori ammessi:

          - *cartaIdentita, passaporto, patenteGuida,*

          - *patenteNautica, librettoPensione,*

          - *patentinoImpTermici, portoArmi,*

          - *tesseraRiconoscimento;*

        - "**document_number**" : Numero del documento;
        - "**issuer**" : <ente emettitore> JSON Object:

          - "**name**" stringa ottenuta dalla
            concatenazione dei termini costituenti la
            denominazione dell'ente a meno di
            congiunzioni, articoli e preposizioni.

              Es. regioneLazio ( Regione Lazio);
              provinciaCatania ( Provincia di Catania);
              prefetturaRoma (Prefettura di Roma);
              MinisteroEconomiaFinanze ( Ministero
              dell'Economia e delle Finanze);

        - "**date_of_issuance**" : data di rilascio del documento;

        - "**date_of_expiry**" : data di scadenza del documento;

       Esempio:

       .. code-block:: json

        "document_details":{
            "type":"cartaIdentita",
            "document_number":"AS09452389",
            "issuer":{
                "name":"ComuneRoma"
            },
            "date_of_issuance":"2013-01-02",
            "date_of_expiry":"2013-01-31"
        }

     - |spid-icon| |cieid-icon|
   * - **phone_number**
     - Numero di telefono mobile (extra anagrafica). String. Stringa numerica senza spazi intermedi |br|
       Esempio: |br|
       ``"phone_number": "VATIT-12345678901"``
     - |spid-icon| |cieid-icon|
   * - **email**
     - Indirizzo di posta elettronica (extra anagrafica). String. Formato standard indirizzo di posta elettronica |br|
       Esempio: |br|
       ``"email": "name@domain.it"``
     - |spid-icon| |cieid-icon|
   * - **https://attributes.eid.gov.it/e_delivery_service**
     - Domicilio digitale (extra anagrafica). Indirizzo casella PEC |br|
       Esempio: |br|
       ``"https://attributes.eid.gov.it/e_delivery_service":"nome@pecdomain.it"``
     - |cieid-icon|
   * - **https://attributes.eid.gov.it/eid_exp_date**
     - Data di scadenza identità (extra anagrafica). Secondo specifica ISO8601-2004 nel formato
       "YYYY-MM-DD" dove |br|
       YYYY indica l'anno utilizzando 4 cifre |br|
       MM indica il mese in (due) cifre |br|
       DD indica il giorno in (due) cifre |br|
       Esempio: |br|
       ``"https://attributes.eid.gov.it/id_exp_date":"2002-09-24"``
     - |spid-icon|
   * - **address**
     - (extra anagrafica) Indirizzo domicilio fisico |br|
       CAP domicilio fisico |br|
       Comune domicilio fisico |br|
       Provincia domicilio fisico |br|
       Nazione domicilio fisico |br|.
       JSON Object (address):
       Formatted, **street_address**
       (**obbigatorio**),locality, region, postal_code,country, country_code
       L'attributo contiene la tipologia (via, viale, piazza …), l'indirizzo e il numero civico. 
       Le tre informazioni sono preferibilmente ordinate come d'uso per lo specifico Stato. 

        - "**street_address**":L'attributo contiene la tipologia (via, viale, piazza …), l'indirizzo e il numero civico. Le tre informazioni sono preferibilmente ordinate come d'uso per lo specifico Stato. 
       
        - "**postal_code**": CAP 

        - "**locality**":Comune

        - "**region**": Provincia 

        - "**country_code**" : Nazione

       Esempio: 
       
       .. code-block:: json

         "address":{
             "street_address":"Via Liszt 21",
             "postal_code":"00144",
             "locality":"Roma",
             "region":"RM",
             "country_code":"IT"
         }

     - |spid-icon| |cieid-icon|

.. _user_claims_scopes:


Esempi
++++++

Si riportano per comodità gli esempi che danno luogo alla composizione di un unico JSON Object da parte di più attributi ed in particolare i claim "place_of_birth", "address", "document_details", ``https://attributes.eid.gov.it/registered_office``.

Si riportano a titolo di esempio due indirizzi italiani:


.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - **Attributo**
     - **Esempio codifica OIDC**
   * - Indirizzo domicilio fisico
       CAP domicilio fisico
       Comune domicilio fisico
       Provincia domicilio fisico
       Nazione domicilio fisico
     - .. code-block:: json

        "address": {
            "street_address":"Via Liszt 21",
            "postal_code":"00144",
            "locality":"Roma",
            "region":"RM",
            "country_code":"IT"
        }

   * - Indirizzo domicilio fisico
       CAP domicilio fisico
       Comune domicilio fisico
       Provincia domicilio fisico
       Nazione domicilio fisico
     - .. code-block:: json

        "address": {
            "street_address":"S.S. Salaria Km 23,800",
            "postal_code":"00015",
            "locality":"Monterotondo",
            "region":"RM",
            "country_code":"IT"
        }

Vi sono casi, come per gli Stati Uniti d'America, dove oltre alla nazione (US) esiste uno Stato. 
In tali casi lo Stato è indicato nel campo Provincia.
Si riporta il seguente esempio:

.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - **Attributo**
     - **Esempio codifica OIDC**
   * - Indirizzo domicilio fisico
       CAP domicilio fisico
       Comune domicilio fisico
       Provincia domicilio fisico
       Nazione domicilio fisico
     - .. code-block:: json

        "address":{
            "street_address":"503,Washington Avenue",
            "postal_code":"12401",
            "locality":"Kingston",
            "region":"New york",
            "country_code":"US"
        }

