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
    
.. admonition:: |spid-icon|
    
    Per ogni messaggio, ove applicabili, potrebbero essere indicizzate ai fini di ricerca e consultazione le seguenti
    informazioni:

        - authorization code
        - client_id
        - jti
        - iss
        - sub
        - iat
        - exp

2. Un registro di federazione contenente, per ogni *AuthenticationRequest*, la **Trust Chain** relativa all'entità con la quale si stanno scambiando i messaggi. Nel caso di registro mantenuto da un OP che riceve una richiesta di autenticazione da un RP, DEVE contenere la seguente lista ordinata di oggetti:

    - L'**Entity Configuration** del RP richiedente.
    - L'**Entity Statement** del SA riferito al RP (se presente).
    - L'**Entity Statement** del TA riferito al RP (o al SA se presente).
    - L'**Entity Configuration** del TA.

Nel caso di registro mantenuto da un RP che effettua una richiesta di autenticazione ad un OP, DEVE contenere la seguente lista ordinata di oggetti:

    - L'**Entity Configuration** dell'OP.
    - L'**Entity Statement** del TA riferito all'OP.
    - L'**Entity Configuration** del TA.

.. warning::
    Le informazioni contenute nei registri DEVONO essere mantenute e gestite per una durata non inferiore a 24 mesi nel pieno rispetto delle vigenti normative nazionali ed europee in materia di privacy. L’accesso ai dati DEVE essere riservato a personale incaricato. Al fine di garantire la confidenzialità DEVONO essere adottai meccanismi di cifratura dei dati o impiegati sistemi di basi di dati (DBMS) che realizzano la persistenza cifrata delle informazioni. Infine, nella memorizzazione dei dati DEVONO essere garantite le proprietà di integrità e non ripudio.


Registro storico delle chiavi pubbliche di Federazione
------------------------------------------------------

Al fine di consentire la verifica dei messaggi scambiati dalle Entità che partecipano alla federazione e delle relative Trust Chain, il TA DEVE pubblicare lo storico delle proprie chiavi pubbliche (JWKS) di federazione all'interno di un registro reso disponibile a tutti i partecipanti tramite l'endpoint */.well-known/openid-federation-jwks*. Per ulteriori dettagli tecnici si rimanda alla Sezione 7.5 di `OIDC-FED`_. 

.. warning::
    Le chiavi che non sono sono più attive da più di 24 mesi POSSONO essere rimosse dal registro a discrezione del TA. 


