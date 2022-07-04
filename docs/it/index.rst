.. include:: ./common_definitions.rst

=======================
SPID/CIE OpenID Connect
=======================

`SPID <https://www.spid.gov.it/>`_ e `CIE id <https://www.cartaidentita.interno.gov.it/>`_ sono i Sistemi Pubblici di Identità Digitale Italiani e 
adottano gli standard `OpenID Connect Core <https://openid.net/specs/openid-connect-core-1_0.html>`_, `OpenID Connect Federation 1.0 <https://openid.net/specs/openid-connect-federation-1_0.html>`_ e `International Government Assurance Profile (iGov) for OpenID Connect 1.0 <https://openid.net/specs/openid-igov-openid-connect-1_0-03.html>`_

Grazie all'`identità digitale <https://identitadigitale.gov.it/>`_, la Pubblica Amministrazione e i fornitori di servizi privati forniscono 
la chiave per accedere ai servizi online attraverso una credenziale unica.

Questa documentazione contiene le specifiche tecniche consolidate, conformi alle Linee Guida Nazionali, 
per migliorare l'esperienza di integrazione alle Federazioni OIDC SPID e CIE id per i Fornitori di Servizio
pubblici e privati (RP), Identity Providers (OP) e Soggetti Aggregatori (SA). 

Contiene inoltre le risorse necessarie per aderire ai sistemi di identità nazionali, 
gli esempi pratici dei metadata, come effettuare la registrazione automatica dei Relying Party presso gli 
OpenID Provider, l'utilizzo degli endpoint della API della Federazione e tutto quello che uno sviluppatore 
deve sapere per effettuare un login con SPID e CIE OpenID.


Indice dei contenuti
--------------------

.. toctree:: 
   :maxdepth: 2

   termini_acronimi.rst
   la_federazione_delle_identita.rst
   configurazione_federazione.rst
   entity_configuration.rst
   entity_statement.rst
   trust_marks.rst
   trust_negotiation.rst
   metadata_oidc.rst
   flusso_autenticazione.rst
   authorization_endpoint.rst
   authentication_response.rst
   token_endpoint.rst
   userinfo_endpoint.rst
   introspection_endpoint.rst
   revocation_endpoint.rst
   federation_endpoint.rst
   differenze_oidc_fed.rst
   come_contribuire.rst
   diventa_fornitore.rst
   standards.rst
   avvisi_spid.rst
   seccons_bcps.rst
   esempi.rst
