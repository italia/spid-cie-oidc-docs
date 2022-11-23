.. include:: ../common/common_definitions.rst

.. _Log_Management:

Retention Policy
================

Gestione dei Log di un OP e di un RP
------------------------------------

Gli OP e gli RP DEVONO mantenere 

1. Un registro delle transazioni contenente i log relativi ai messaggi scambiati. I messaggi memorizzati e mantenuti nel registro DEVONO essere almeno i seguenti:

    - **AuthenticationRequest**
    - **AuthenticationResponse** relativa all'*AuthenticationRequest*
    - **TokenRequest** relativa all'*AuthenticationRequest*
    - **TokenResponse** relativa alla *TokenRequest* 
    - L'eventuale **UserInfoRequest** relativa alla *TokenRequest*
    - L'eventuale **UserInfoResponse** relativa alla *UserInfoRequest*
    - L'eventuale **RevocationRequest** relativa alla *TokenRequest*
    - L'eventuale **RevocationResponse** relativa alla *RevocationRequest*

2. Un registro di federazione contenente, per ogni *AuthenticationRequest*, la **Trust Chain** relativa all'entità con la quale si stanno scambiando i messaggi. Nel caso di registro mantenuto da un OP che riceve una richiesta di autenticazione da un RP, DEVE contenere:

    - L'**Entity Configuration** del RP richiedente.
    - L'eventuale **Entity Configuration** del SA (nel caso di RP aggregato).
    - L'eventuale **Entity Statement** del SA riferito al RP.
    - L'**Entity Configuration** del TA.
    - L'**Entity Statement** del TA riferito al RP.

Nel caso di registro mantenuto da un RP che effettua una richiesta di autenticazione ad un OP, DEVE contenere:

    - L'**Entity Configuration** dell'OP.
    - L'**Entity Configuration** del TA.
    - L'**Entity Statement** del TA riferito all'OP.

.. warning::
    Le informazioni contenute dei registri DEVONO essere mantenute e gestite per una durata non inferiore a 24 mesi in nel pieno rispetto delle vigenti normativa in materia di privacy. L’accesso ai dati DEVE essere riservato a personale incaricato. Al fine di garantire la confidenzialità POSSONO essere adottai meccanismi di cifratura dei dati o impiegati sistemi di basi di dati (DBMS) che realizzano la persistenza cifrata delle informazioni. Infine, DEVONO essere messi in atto meccanismi che garantiscono l’integrità e il non ripudio.


Registro delle chiavi di Federazione
------------------------------------

Al fine di consentire la verifica dei messaggi scambiati dalle entità che partecipano alla federazione e delle relative Trust Chain, il TA DEVE pubblicare lo storico delle chiavi pubbliche (JWKS) di federazioneall'interno di un registro reso disponibile a tutti i partecipanti tramite l'endpoint */.well-known/openid-federation-jwks*. Per ulteriori dettagli tecnici si rimanda alla Sezione 7.5 di `OIDC-FED`_. 

.. warning::
    Le chiavi che non sono sono più attive da più di 24 mesi POSSONO essere rimosse dal registro a discrezione del TA. 


