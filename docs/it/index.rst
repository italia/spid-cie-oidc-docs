.. include:: ./common_definitions.rst

=======================
SPID/CIE OpenID Connect
=======================

`SPID <https://www.spid.gov.it/>`_ e `CIE id <https://www.cartaidentita.interno.gov.it/>`_ sono i Sistemi Pubblici di Identità Digitale Italiani e 
adottano e adottano gli standard OpenID Connect Core e OpenID Connect Federation 1.0. 

Grazie all’`identità digitale <https://identitadigitale.gov.it/>`_, la Pubblica Amministrazione e i fornitori di servizi privati forniscono 
la chiave per accedere ai servizi online attraverso una credenziale unica, che si attiva una sola volta ed è sempre valida.

Questa Documentazione è rivolta agli sviluppatori e agni analisti che devono approcciarsi
al funzionamento delle Federazioni 
OpenID Connect SPID e CIE id 
per i Fornitori di Servizio pubblici e privati (RP), Identity Providers (OP) e 
Soggetti Aggregatori (SA). 

In questa documentazione trovi le risorse necessarie per aderire ai sistemi di identità
nazionali, gli esempi pratici dei metadati, come effettuare  
la registrazione dinamica dei Relying Party presso gli 
OpenID Provider, l'utilizzo degli endpoint della API della Federazione e tutto quello che 
uno sviluppatore deve sapere per effettuare un login con SPID e CIE OpenID.


Indice dei contenuti
--------------------

.. toctree:: 
   :maxdepth: 2

   termini_acronimi.rst
   la_federazione_delle_identita.rst
   configurazione_federazione.rst
   entity_statement_entity_configuration.rst
   trust_marks.rst
   trust_negotiation.rst
   metadata_oidc.rst
   authorization_endpoint.rst
   authentication_response.rst
   token_endpoint.rst
   userinfo_endpoint.rst
   introspection_endpoint.rst
   revocation_endpoint.rst
   federation_endpoint.rst
   trust_anchor_intermediari_endpoint.rst
   differenze_oidc_fed.rst
   come_contribuire.rst
   diventa_fornitore.rst
   standards.rst
   avvisi_spid.rst
   seccons_bcps.rst
   esempi.rst
