.. include:: ../common/common_definitions.rst


.. _differenze_con_oidc_federation:

Differenze con OIDC Federation
------------------------------

In questa sezione sono elencate le differenze che intercorrono tra lo standard ufficiale e l'implementazione SPID e CIE.


Client Registration
+++++++++++++++++++

SPID e CIE supportano esclusivamente **automatic_client_registration**. La modalità **explicit client registration** non è supportata. 


Trust Mark
++++++++++

L'esposizione dei Trust Mark in SPID e CIE è obbligatoria. Per approfondimenti sulla ragione dell'obbligo dei Trust Mark si rimanda alla sezione :ref:`Considerazioni di Sicurezza<Considerazioni_di_Sicurezza>`.


Claim non supportati negli Entity Statement
+++++++++++++++++++++++++++++++++++++++++++

Poiché SPID e CIE non necessitano di alcun claim aggiuntivo in ambito federativo, non necessitano del claim **crit**. Inoltre non sono supportati i claim **aud**, **naming_constraints**, **policy_language_crit** e **trust_anchor_id**. L'eventuale presenza di questi claim non presenta alcuna implicazione, questi verranno semplicemente ignorati fino ad ulteriori avvisi che li normino.
