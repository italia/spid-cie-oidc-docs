.. include:: ../common/common_definitions.rst

.. _user_claims:

Tabella attributi utente
------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - **Claim**
     - **Categoria**
     - **Descrizione**
     - **Supportato da**
   * - **https://attributes.eid.gov.it/spid_code**
     - anagrafica
     - Codice identificativo. String. Il codice identificativo è assegnato dal gestore dell'identità digitale e deve essere univoco.

       Il formato è il seguente:

       .. code-block::

         <codice Identificativo> = <cod_IdP><nr. univoco>

       Dove:

         **<cod_IdP>**: è un codice composto da 4 lettere univocamente assegnato al gestore delle identità;

         **<nr.univoco>**: è una stringa alfanumerica composta da 10 caratteri che il gestore delle identità genera in maniera univoca nell'ambito del proprio dominio.

       Esempio: 

       .. code-block::

         "https://attributes.eid.gov.it/spid_cod":"ABCD123456789A"

     - |spid-icon|
   * - **given_name**
     - anagrafica
     - Nome. String. Stringa composta da una sequenza di parole con carattere iniziale maiuscolo,
       intervallate da spazi singoli.
       
       Esempio:

       .. code-block::
      
         "given_name":"Giovanni Mario"

     - |spid-icon| |cieid-icon|
   * - **family_name**
     - anagrafica
     - Cognome. String. Stringa composta da una sequenza di parole con carattere iniziale maiuscolo,
       intervallate da spazi singoli.

       Esempio:

       .. code-block::
       
         "family_name":"Bianchi Verdi"

     - |spid-icon| |cieid-icon|
   * - **place_of_birth**
     - anagrafica
     - Luogo di nascita, Provincia di nascita. JSON Object: 

       "**locality** : Stringa corrispondente al codice catastale (Codice Belfiore) del Comune 
       o della nazione estera di nascita (Es. "F205" per la città di Milano)

       "**region**" : Stringa corrispondente alla sigla della provincia di nascita

       Esempio:

       .. code-block::

        "place_of_birth":{
            "region":"MI",
            "locality":"F205"
        }

     - |spid-icon| |cieid-icon|
   * - **birthdate**
     - anagrafica
     - Data di nascita. String. Secondo specifica ISO8601-2004 nel formato
       YYYY indica l'anno utilizzando 4 cifre |br|
       MM indica il mese in (due) cifre |br|
       DD indica il giorno in (due) cifre |br|
       Esempio: |br|

       .. code-block::

         "birthdate":"2002-09-24"

     - |spid-icon| |cieid-icon|
   * - **gender**
     - anagrafica
     - Sesso. String. Valori ammessi: |br|
       "F" per sesso femminile |br|
       "M" per sesso maschile |br|
       Esempio: |br|

       .. code-block::

         "gender":"F"

     - |spid-icon| |cieid-icon|
   * - **https://attributes.eid.gov.it/company_name**
     - anagrafica
     - Ragione o denominazione sociale. String. Stringa composta da una sequenza di parole intervallate 
       da spazi singoli.
       In maiuscolo le sottostringhe corrispondenti a nomi (es. “Agenzia per l'Italia Digitale”)

       .. code-block::

         "company_name":"Agenzia per l'Italia Digitale"

     - |spid-icon|
   * - **https://attributes.eid.gov.it/registered_office**
     - extra anagrafica
     - Sede legale. JSON Object: formatted, street_address, locality, region, postal_code, country, 
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

       .. code-block::

         "https://attributes.eid.gov.it/registered_office":{
             "formatted":"via Listz 21 00144 Roma"
         }

     - |spid-icon|
   * - **https://attributes.eid.gov.it/fiscal_number**
     - anagrafica
     - Codice fiscale della persona fisica. String. Per il formato si faccia riferimento alla codifica 
       dell'attributo CF per i certificati, proposta nell'ambito del Draft ETSI EN 319 412-1, 
       che nel caso specifico prevede la seguente composizione:
       TINIT-<CodiceFiscale>
        
       Esempio:

       .. code-block::

          "https://attributes.eid.gov.it/fiscal_number": “TINIT-ABCXYZ00W00Z000Z"

     - |spid-icon| |cieid-icon|
   * - **https://attributes.eid.gov.it/**
     - anagrafica
     - Codice fiscale Persona Giuridica. String. Per il formato si faccia riferimento alla codifica dell'attributo CF per i certificati, proposta
       nell'ambito del Draft ETSI EN 319 412-1, che nel caso specifico prevede la seguente composizione:

       TINIT-segue il codice fiscale

        .. code-block::

          "https://attributes.eid.gov.it/company_fiscalNumber":"TINIT-ABCXYZ00W00Z000Z"

     - |spid-icon|
   * - **https://attributes.eid.gov.it/vat_number**
     - anagrafica
     - Partita IVA. String. Per il formato si faccia riferimento alla codifica dell'attributo Partita IVA per i certificati,
       proposta nell'ambito del Draft ETSI EN 319 412-1, che nel caso specifico prevede la seguente composizione:

       VATIT-<PartitaIVA>

       Esempio:

       .. code-block::

          "https://attributes.eid.gov.it/vat_number": "VATIT-12345678901"

     - |spid-icon|
   * - **document_details**
     - extra anagrafica
     - Documento d'identità. JSON Object (document):

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

       .. code-block::

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
     - extra anagrafica
     - Numero di telefono mobile. String. Stringa numerica senza spazi intermedi |br|
       Esempio: |br|
       ``"phone_number": "VATIT-12345678901"``
     - |spid-icon| |cieid-icon|
   * - **email**
     - extra anagrafica
     - Indirizzo di posta elettronica. String. Formato standard indirizzo di posta elettronica |br|
       Esempio: |br|
       ``"email": "name@domain.it"``
     - |spid-icon| |cieid-icon|
   * - **https://attributes.eid.gov.it/e_delivery_service**
     - extra anagrafica
     - Domicilio digitale. Indirizzo casella PEC |br|
       Esempio: |br|
       ``"https://attributes.eid.gov.it/e_delivery_service":"nome@pecdomain.it"``
     - |cieid-icon|
   * - **https://attributes.eid.gov.it/eid_exp_date**
     - extra anagrafica
     - Data di scadenza identità. Secondo specifica ISO8601-2004 nel formato
       "YYYY-MM-DD" dove |br|
       YYYY indica l'anno utilizzando 4 cifre |br|
       MM indica il mese in (due) cifre |br|
       DD indica il giorno in (due) cifre |br|
       Esempio: |br|
       ``"https://attributes.eid.gov.it/id_exp_date":"2002-09-24"``
     - |spid-icon|
   * - **address**
     - extra anagrafica 
     - Indirizzo domicilio fisico |br|
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
       
       .. code-block:: 

         "address":{
             "street_address":"Via Liszt 21",
             "postal_code":"00144",
             "locality":"Roma",
             "region":"RM",
             "country_code":"IT"
         }

     - |spid-icon| |cieid-icon|

.. _user_claims_scopes:


Esempi non normativi
++++++++++++++++++++

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
     - .. code-block::

        "address":{
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
     - .. code-block::

        "address":{
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
     - .. code-block::

        "address":{
            "street_address":"503,Washington Avenue",
            "postal_code":"12401",
            "locality":"Kingston",
            "region":"New york",
            "country_code":"US"
        }

