Differenze con OIDC Federation 1.0
----------------------------------

In questa sezione sono elencate le differenze che intercorrono tra lo standard ufficiale e l’implementazione SPID.


Client Registration
+++++++++++++++++++

SPID supporta esclusivamente **automatic_client_registration**. La modalità **implicit** è da intendersi come non supportata. 


Listing endpoint
++++++++++++++++

In SPID viene adottato il parametro aggiuntivo **entity_type** a quelli esistenti nello Standard [OIDC-FED] per questo endpoint, con lo scopo di ottenere un filtro sulla tipologia delle entità discendenti. Questa esigenza consente nello specifico di filtrare entità di tipo **federation_entity**, **openid_relying_party**, **openid_provider** e **oauth_resource**.


Trust Mark
++++++++++

In OIDC-FED l’uso dei Trust Mark non è obbligatorio. In SPID piuttosto l’esposizione dei Trust Mark è obbligatoria. Per approfondimenti sulla ragione dell’obbligo dei Trust Mark si rimanda alla sezione :ref:`Considerazioni di Sicurezza<Considerazioni_di_Sicurezza>`.


Differenze con OIDC Core 1.0
----------------------------

TODO.
