.. include:: ../common/common_definitions.rst

Differenze con OIDC iGov
------------------------

CIE OpenID Connect e SPID OpenID Connect sono basati su `iGov.OIDC`_ con le seguenti differenze:

 - La sezione 2.1 di iGov riporta **vtr**, **acr_values** e **PKCE** come OPZIONALI, sia in SPID che in CIE id **PKCE** e **acr_values** sono RICHIESTI. In entrambe le implementazioni di SPID e CIE, si è adottato **acr_values** al posto di **vtr**.

 - L'Authentication Response nel flusso di autenticazione di CIE impone l'uso del claim **iss** per evitare l'attacco mix-up `I-D.ietf-OAuth-Security-BCP`_. L'uso di questo claim è OPZIONALE in SPID.

 - La sezione 2.4 di iGov stabilisce "Gli RP POSSONO opzionalmente mandare richieste all'Authorization Endpoint usando il parametro request." Sia in SPID che in CIE id, l'uso del parametro request è RICHIESTO.

 - La sezione 3.1 di iGov stabilisce che "in caso di utilizzo di **vtr** nella richiesta di autenticazione, l'ID Token DEVE contenere i seguenti claim RICHIESTI, cioè: **vot** e **vtm** ". Considerando che **vtr** non è usato in SPID e CIE id, i claim appena citati non vengono inclusi all'interno dell'ID Token. 

 - La sezione 3.1 di iGov stabilisce che "il claim **auth-time** nell'ID Token è RACCOMANDATO". SPID e CIE id non adottano questo claim nell'ID Token.

 - L'ID Token, sia in SPID che in CIE id, DEVE avere il claim **acr** RICHIESTO, mentre questo è opzionale nell'iGov draft iGov.

 - L'ID Token, sia in SPID che in CIE id, ha il requisito del claim **at_hash** RICHIESTO. Questo è OPZIONALE in OIDC-CORE è assente in iGOV.

 - Sia in SPID che in CIE id, l'identificatore del soggetto DEVE essere **pairwised**.

 - La UserInfo Response, sia in SPID che in CIE id, DEVE essere un Nested JWT, firmato con la chiave privata dell'emettitore e cifrato con la chiave pubblica del RP.

 - Il JWT firmato della UserInfo Response DEVE avere i claim **iss**, **sub**, **aud**, **iat** e **exp**.

 - La sezione 3.4 di iGov stabilisce "Gli OpenID Provider POSSONO accettare oggetti request by reference usando il parametro request_uri". Questo parametro è intercambiabile con il parametro request. SPID e CIE id adottano solamente il parametro request.

 - Sezione 3.8. La registrazione dinamica di iGOV specifica che la registrazione dinamica del client è obbligatoria. Sia in CIE id che in SPID, la registrazione automatica OIDC del client è OBBLIGATORIA, mentre la registrazione dinamica OIDC del client NON DOVREBBE essere supportata.

 - Nella sezione 4.2 di iGOV gli scope **openid**, **offline_access**, **profile** e **email** vengono usati sia in SPID che in CIE id OpenID Connect proposal e non considerano gli altri scope raccomandatinel profilo iGov, cioè: **doc**.

 - La sezione 4.3 di iGov definisce la politica relativa all'oggetto userinfo del claim request. Sia in SPID che in CIE id, definiamo la politica per entrambi gli oggetti userinfo e ID Token.

 - Nelle sezioni 3.7 e 2.5 di iGOV, i Metadata sia di SPID che di CIE id vengono distribuiti secondo le modalità definite nella sezione "3. Metadata".

 - L'Access Token è un JWT firmato in conformità a :rfc:`9068`.

