.. include:: ./common_definitions.rst


.. claim_OP_SPID:



OpenID Connect Provider Metadata (OP) per SPID
++++++++++++++++++++++++++++++++++++++++++++++

Segue la tabella dei claim specifici per la Federazione SPID.

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Obbligatorio**
   * - **op_name**
     - Nome dell’OpenID Provider. Può essere specificato in più lingue apponendo al nome dell’elemento il suffisso 
       “#” seguito dal codice :rfc:`5646`. Un nome di default senza indicazione della lingua è sempre presente.
     - |check-icon|
   * - **op_uri**
     - URL dell’OpenID Provider. Può essere specificato in più lingue apponendo al nome dell’elemento il suffisso 
       “#” seguito dal codice :rfc:`5646`. Un valore di default senza indicazione della lingua è sempre presente.
     - |check-icon|


