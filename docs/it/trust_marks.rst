.. include:: ./common_definitions.rst


.. _Trust_Mark:

Trust Mark
----------

I Trust Mark, letteralmente tradotti come marchi di fiducia, sono oggetti JSON firmati in formato Jose :rfc:`7515` e rappresentano la dichiarazione di conformità a un insieme ben definito di requisiti di fiducia e/o di interoperabilità o un accordo tra le parti coinvolte all’interno della Federazione. I Trust Marks sono rilasciati principalmente durante il processo di registrazione di una nuova entità di tipo Foglia (onboarding) dal Trust Anchor o suoi Intermediari.

Lo scopo principale dei TM è quello di esporre alcune informazioni non richieste dal protocollo OpenID Connect Core ma che risultano utili in contesto Federativo.

Esempi tipici includono il codice di identificazione nazionale o internazionale dell’entità (Codice Fiscale, IPA Code, Partita IVA, VAT Number, etc.), i contatti istituzionali e altro. Ulteriori dati possono essere aggiunti dall’emittente se resi comprensibili all’interno della Federazione.


.. toctree:: 
   :maxdepth: 2

   trust_marks_spid.rst
   trust_marks_cie.rst
