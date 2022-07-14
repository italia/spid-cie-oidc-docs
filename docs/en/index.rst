.. include:: ./common_definitions.rst

=======================
SPID/CIE OpenID Connect
=======================

`SPID <https://www.spid.gov.it/>`_ and `CIE id <https://www.cartaidentita.interno.gov.it/>`_ are the Italian Systems of Public Digital Identity. They adopt the standards `OpenID Connect Core <https://openid.net/specs/openid-connect-core-1_0.html>`_, `International Government Assurance Profile (iGov) for OpenID Connect 1.0 <https://openid.net/specs/openid-igov-openid-connect-1_0-03.html>`_ and `OpenID Connect Federation 1.0 <https://openid.net/specs/openid-connect-federation-1_0.html>`_.

Thanks to the `digital identity <https://identitadigitale.gov.it/>`_, the Public Administration and the private service suppliers, supply the keys to access the online services through unique access credentials.

This documentation contains the consolidated technical specifications, compliant to the National Guidelines, to improve the experience of integration in the OIDC SPID and CIE id Federations, for the public and private Service Suppliers (RP), Identity Providers (OP) and Intermediate Entities (SA). 

In this documentation you can find:

 - practical examples of Metadata, OpenID Connect requests and responses,
 - how to perform and automatic registration of the RPs to the OpenID Providers, 
 - how an OpenID Provider recognizes and dynamically registers an RP,
 - how to use the endpoints of the Federation APIs,
 - how to authenticate a user to SPID and CIE and get their attributes.


Indix of content
----------------

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
   attributi_utente.rst
