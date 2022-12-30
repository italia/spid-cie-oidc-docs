=======================
SPID/CIE OpenID Connect
=======================

`SPID <https://www.spid.gov.it/>`_ and `CIE id <https://www.cartaidentita.interno.gov.it/>`_ are the Italian Systems of Public Digital Identity. They adopt the standards `OpenID Connect Core <https://openid.net/specs/openid-connect-core-1_0.html>`_, `International Government Assurance Profile (iGov) for OpenID Connect 1.0 <https://openid.net/specs/openid-igov-openid-connect-1_0-03.html>`_ and `OpenID Connect Federation 1.0 <https://openid.net/specs/openid-connect-federation-1_0.html>`_.

Thanks to the `digital identity <https://identitadigitale.gov.it/>`_ the public and private services provides the keys to access the online services through unique access credentials.

This documentation contains the consolidated technical specifications, compliant to the national guidelines, to improve the experience of integration in the OIDC SPID and CIE id Federations, for the public and private Service Providers (RP), Identity Providers (OP) and Intermediate Entities (SA). 

In this documentation you can find:

 - Practical examples of Metadata, OpenID Connect requests and responses.
 - How to perform and automatic registration of the RPs to the OpenID Providers.
 - How an OpenID Provider recognizes and dynamically registers an RP.
 - How to use the endpoints of the Federation APIs.
 - How to authenticate a user to SPID and CIE id.


Index of content
----------------

.. toctree:: 
   :maxdepth: 2

   standards.rst
   termini_acronimi.rst
   la_federazione_delle_identita.rst
   entity_configuration.rst
   entity_statement.rst
   trust_marks.rst
   soggetti_aggregatori.rst
   trust_negotiation.rst
   federation_endpoint.rst
   errors_federation.rst
   metadata_oidc.rst
   flusso_autenticazione.rst
   authorization_endpoint.rst
   token_endpoint.rst
   userinfo_endpoint.rst
   attributi_utente.rst
   introspection_endpoint.rst
   revocation_endpoint.rst
   logout.rst
   cryptographic_algos.rst
   log_management.rst
   differenze_spid_cie.rst
   confronto_oidc_cie_e_oidc_igov.rst
   differenze_oidc_fed.rst
   seccons_bcps.rst
   esempi.rst
   diventa_fornitore.rst
   come_contribuire.rst
