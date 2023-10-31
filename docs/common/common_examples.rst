
.. _Esempio_EN1:

EN 1. Entity Configuration Request
++++++++++++++++++++++++++++++++++

.. code-block:: python

 GET /.well-known/openid-federation HTTP/1.1
 Host: rp.example.it


.. _Esempio_EN1.1:

EN 1.1. Entity Configuration Response Relying Party
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python

 HTTP/1.1 200 OK
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/entity-statement+jwt 
 
 {
     "alg": "RS256",
     "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs",
     "typ": "entity-statement+jwt"
 }
 .
 {
     "exp": 1649590602,
     "iat": 1649417862,
     "iss": "https://rp.example.it/",
     "sub": "https://rp.example.it/",
     "jwks": {
         "keys": [
             {
                 "kty": "RSA",
                 "n": "5s4qi …",
                 "e": "AQAB",
                 "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
             }
         ]
     },
     "metadata": {
         "openid_relying_party": {
             "application_type": "web",
             "client_id": "https://rp.example.it/",
             "client_registration_types": [
                 "automatic"
             ],
             "jwks": {
                 "keys": [
                     {
                         "kty": "RSA",
                         "use": "sig",
                         "n": "1Ta-sE …",
                         "e": "AQAB",
                         "kid": "YhNFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
                     }
                 ]
             },
             "client_name": "Name of an example organization",
             "contacts": [
                 "ops@rp.example.it"
             ],
             "grant_types": [
                 "refresh_token",
                 "authorization_code"
             ],
             "redirect_uris": [
                 "https://rp.example.it/oidc/rp/callback/"
             ],
             "response_types": [
                 "code"
             ],
             "subject_type": "pairwise"
         },
         "federation_entity": {
             "federation_resolve_endpoint": "https://rp.example.it/resolve/",
             "organization_name": "PA OIDC Service Provider",
             "homepage_uri": "https://rp.example.it",
             "policy_uri": "https://rp.example.it/policy",
             "logo_uri": "https://rp.example.it/static/logo.svg",
             "contacts": [
                "tech@example.it"
              ]
         }
     },
     "trust_marks": [
         {
             "id": "https://registry.agid.gov.it/openid_relying_party/public/",
             "trust_mark": "eyJh …"
         }
     ],
     "authority_hints": [
         "https://registry.agid.gov.it/"
     ]
 }


.. _Esempio_EN1.2:

EN 1.2. Entity Configuration Response Openid Provider
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python

 HTTP/1.1 200 OK
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/entity-statement+jwt 
 
 {
     "alg": "RS256",
     "kid": "dB67gL7ck3TFiIAf7N6_7SHvqk0MDYMEQcoGGlkUAAw",
     "typ": "entity-statement+jwt"
 }
 .
 {
     "exp": 1649610249,
     "iat": 1649437449,
     "iss": "https://openid.provider.it/",
     "sub": "https://openid.provider.it/",
     "jwks": {
         "keys": [
             {
                 "kty": "RSA",
                 "e": "AQAB",
                 "n": "01_4a …",
                 "kid": "dB67gL7ck3TFiIAf7N6_7SHvqk0MDYMEQcoGGlkUAAw"
             }
         ]
     },
     "metadata": {
         "openid_provider": {
             "authorization_endpoint": "https://openid.provider.it/authorization",
             "revocation_endpoint": "https://openid.provider.it/revocation/",
             "id_token_encryption_alg_values_supported": [
                 "RSA-OAEP"
             ],
             "id_token_encryption_enc_values_supported": [
                 "A128CBC-HS256"
             ],
             "token_endpoint": "https://openid.provider.it/token/",
             "userinfo_endpoint": "https://openid.provider.it/userinfo/",
             "introspection_endpoint": "https://openid.provider.it/introspection/",
             "claims_parameter_supported":true,
             "contacts": [
                 "ops@https://idp.it"
             ],
             "client_registration_types_supported": [
                 "automatic"
             ],
             "code_challenge_methods_supported": [
                 "S256"
             ],
             "request_authentication_methods_supported": {
                 "ar": [
                     "request_object"
                 ]
             },
             "acr_values_supported": [
                 "https://www.spid.gov.it/SpidL1",
                 "https://www.spid.gov.it/SpidL2",
                 "https://www.spid.gov.it/SpidL3"
             ],
             "claims_supported": [
                 "https://attributes.eid.gov.it/spid_code",
                 "given_name",
                 "family_name",
                 "place_of_birth",
                 "birthdate",
                 "gender",
                 "https://attributes.eid.gov.it/company_name",
                 "https://attributes.eid.gov.it/registered_office",
                 "https://attributes.eid.gov.it/fiscal_number",
                 "https://attributes.eid.gov.it/vat_number",
                 "https://attributes.eid.gov.it/document_details",
                 "phone_number",
                 "email",
                 "address",
                 "https://attributes.eid.gov.it/eid_exp_date",
                 "https://attributes.eid.gov.it/e_delivery_service"
             ],
             "grant_types_supported": [
                 "authorization_code",
                 "refresh_token"
             ],
             "id_token_signing_alg_values_supported": [
                 "RS256",
                 "ES256"
             ],
             "issuer": "https://openid.provider.it/",
             "jwks": {
                 "keys": [
                     { 
                         "kty": "RSA",
                         "use": "sig",
                         "n": "1Ta-sE …",
                         "e": "AQAB",
                         "kid": "FANFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
                     }
                 ]
             },
             "scopes_supported": [
                 "openid",
                 "offline_access"
             ],
             "logo_uri": "https://openid.provider.it/static/svg/spid-logo-c-lb.svg",
             "organization_name": "SPID OIDC identity provider",
             "op_policy_uri": "https://openid.provider.it/it/website/legal-information/",
             "request_parameter_supported":true,
             "request_uri_parameter_supported":true,
             "require_request_uri_registration":true,
             "response_types_supported": [
                 "code"
             ],
             "subject_types_supported": [
                 "pairwise",
                 "public"
             ],
             "token_endpoint_auth_methods_supported": [
                 "private_key_jwt"
             ],
             "token_endpoint_auth_signing_alg_values_supported": [
                 "RS256",
                 "RS384",
                 "RS512",
                 "ES256",
                 "ES384",
                 "ES512"
             ],
             "userinfo_encryption_alg_values_supported": [
                 "RSA-OAEP",
                 "RSA-OAEP-256"
             ],
             "userinfo_encryption_enc_values_supported": [
                 "A128CBC-HS256",
                 "A192CBC-HS384",
                 "A256CBC-HS512",
                 "A128GCM",
                 "A192GCM",
                 "A256GCM"
             ],
             "userinfo_signing_alg_values_supported": [
                 "RS256",
                 "RS384",
                 "RS512",
                 "ES256",
                 "ES384",
                 "ES512"
             ],
             "request_object_signing_alg_values_supported": [
                 "RS256",
                 "RS384",
                 "RS512",
                 "ES256",
                 "ES384",
                 "ES512"
             ]
         },
         "federation_entity": {
             "federation_resolve_endpoint": "https://openid.provider.it/resolve/",
             "organization_name": "SPID OIDC identity provider",
             "homepage_uri": "https://provider.it",
             "policy_uri": "https://provider.it/policy",
             "logo_uri": "https://provider.it/static/logo.svg",
             "contacts": [
                "tech@provider.it"
              ]
         }
     },
     "authority_hints": [
         "https://registry.agid.gov.it/"
     ]
 }

.. _Esempio_EN1.3:

EN 1.3. Entity Configuration Response Intermediary 
++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python

 HTTP/1.1 200 OK
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/entity-statement+jwt 

 {
     "alg": "RS256",
     "kid": "em3cmnZgHIYFsQ090N6B3Op7LAAqj8rghMhxGmJstqg",
     "typ": "entity-statement+jwt"
 }
 .
 {
     "exp": 1649631824,
     "iat": 1649459024,
     "iss": "https://aggregatore.it/",
     "sub": "https://aggregatore.it/",
     "jwks": {
         "keys": [
             {
                 "kty": "RSA",
                 "e": "AQAB",
                 "n": "14aW …",
                 "kid": "em3cmnZgHIYFsQ090N6B3Op7LAAqj8rghMhxGmJstqg"
             }
         ]
     },
     "metadata": {
         "federation_entity": {
             "contacts": [
                 "soggetto@aggregatore.it"
             ],
             "federation_fetch_endpoint": "https://aggregatore.it/fetch/",
             "federation_resolve_endpoint": "https://aggregatore.it/resolve/",
             "federation_list_endpoint": "https://aggregatore.it/list/",
             "homepage_uri": "https://soggetto.aggregatore.it",
             "name": "Soggetto Aggregatore di esempio"
         },
         "trust_mark_issuer": {
             "federation_status_endpoint": "https://aggregatore.it/trust_mark_status/",

         }
     },
     "trust_marks": [
         {
             "id": "https://registry.gov.it/intermediate/private/full/",
             "trust_mark": "eyJh …"
         }
     ],
     "authority_hints": [
         "https://registry.agid.gov.it/"
     ]
 }



.. _Esempio_EN1.4:

EN 1.4. Entity Configuration Response Trust Anchor
++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python

 HTTP/1.1 200 OK
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/entity-statement+jwt
 
 {
     "alg": "RS256",
     "kid": "FifYx03bnosD8m6gYQIfNHNP9cM_Sam9Tc5nLloIIrc",
     "typ": "entity-statement+jwt"
 }
 .
 {
     "exp": 1649375259,
     "iat": 1649373279,
     "iss": "https://registry.agid.gov.it/",
     "sub": "https://registry.agid.gov.it/",
     "jwks": {
         "keys": [
             {
                 "kty": "RSA",
                 "n": "3i5vV-_ …",
                 "e": "AQAB",
                 "kid": "FifYx03bnosD8m6gYQIfNHNP9cM_Sam9Tc5nLloIIrc"
             }
         ]
     },
     "metadata": {
         "federation_entity": {
             "organization_name": "example TA"
             "contacts":[
                 "spid.tech@agid.gov.it"
             ],
             "policy_uri": "https://registry.agid.gov.it/policy",
             "homepage_uri": "https://registry.agid.gov.it/",
             "logo_uri":"https://registry.agid.gov.it/static/svg/logo.svg",
             "federation_fetch_endpoint": "https://registry.agid.gov.it/fetch/",
             "federation_resolve_endpoint": "https://registry.agid.gov.it/resolve/",
             "federation_list_endpoint": "https://registry.agid.gov.it/list/",
             "federation_trust_mark_status_endpoint": "https://registry.agid.gov.it/trust_mark_status/"
         }
     },
     "trust_marks_issuers": {
         "https://registry.agid.gov.it/openid_relying_party/public/": [
             "https://registry.spid.agid.gov.it/",
             "https://public.intermediary.spid.it/"
         ],
         "https://registry.agid.gov.it/openid_relying_party/private/": [
             "https://registry.spid.agid.gov.it/",
             "https://private.other.intermediary.it/"
         ]
     },
     "constraints": {
         "max_path_length": 1
     }
 }

.. _Esempio_EN1.5:

EN 1.5. Trust Mark issued by TA to a RP
+++++++++++++++++++++++++++++++++++++++

.. code-block:: json

 {
     "trust_marks": [
         {
             "id": "https://registry.interno.gov.it/openid_relying_party/public/",
             "iss": "https://registry.interno.gov.it/",
             "trust_mark": "$JWT"
         }
     ]
 }


Where the $JWT payload is:

.. code-block:: json

 {
     "id": "https://registry.interno.gov.it/openid_relying_party/public/",
     "iss": "https://sa.esempio.it/",
     "sub": "https://rp.esempio.it/",
     "iat": 1579621160,
     "organization_type": "public",
     "id_code": {
        "ipa_code": "123456",
        "aoo_code": "Uff_protocollo"
     }
     "email": "email_or_pec@rp.it",
     "organization_name#it": "Denominazione del RP",
     "ref": "https://documentazione_di_riferimento.it/"
 }


.. _Esempio_EN1.6:

EN 1.6. Trust Mark issued by TA to a SA
+++++++++++++++++++++++++++++++++++++++

.. code-block:: json

 {
     "trust_marks": [
         {
             "id": "https://registry.interno.gov.it/intermediate/private/full/",
             "iss": "https://registry.interno.gov.it/",
             "trust_mark": "$JWT"
         }
     ]
 }


Where the $JWT payload is:

.. code-block:: json

 {
     "id": "https://registry.interno.gov.it/intermediate/private/full/",
     "iss": "https://registry.interno.gov.it/",
     "sub": "https://sa.esempio.it/",
     "iat": 1579621160,
     "organization_type": "private",
     "id_code": {
        "fiscal_number": "1234567890"
     }
     "email": "email_or_pec@intermediate.it",
     "organization_name#it": "Denominazione del SA",
     "sa_profile": "full",
     "ref": "https://documentazione_di_riferimento.it/"
 }

.. _Esempio_EN1.7:

EN 1.7. Trust Mark issued by SA to a RP
+++++++++++++++++++++++++++++++++++++++

.. code-block:: json

 {
     "trust_marks": [
         {
             "id": "https://registry.interno.gov.it/openid_relying_party/public/",
             "iss": "https://sa.esempio.it",
             "trust_mark": "$JWT"
         }
     ]
 }


Where the $JWT payload is:

.. code-block:: json

 {
     "id": "https://registry.interno.gov.it/openid_relying_party/public/",
     "iss": "https://sa.esempio.it/",
     "sub": "https://rp.esempio.it/",
     "iat": 1579621160,
     "organization_type": "public",
     "id_code": {
        "ipa_code": "987654",
     }
     "email": "email_or_pec@rp.it",
     "organization_name#it": "Denominazione del RP",
     "ref": "https://documentazione_di_riferimento.it/"
 }


 
.. _Esempio_EN2:

EN 2. Entity Statement Request
++++++++++++++++++++++++++++++

.. code-block:: 

 GET /fetch?sub=https://rp.example.it/
 HTTP/1.1
 Host: registry.agid.gov.it


.. _Esempio_EN2.1:


EN 2.1 Entity Statement Response
++++++++++++++++++++++++++++++++

.. code-block:: http

 HTTP/1.1 200 OK
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/entity-statement+jwt
 
 {
     "alg": "RS256",
     "kid": "FifYx03bnosD8m6gYQIfNHNP9cM_Sam9Tc5nLloIIrc",
     "typ": "entity-statement+jwt"
 }
 .
 {
     "exp": 1649623546,
     "iat": 1649450746,
     "iss": "https://registry.agid.gov.it/",
     "sub": "https://rp.example.it/",
     "jwks": {
         "keys": [
             {
                 "kty": "RSA",
                 "n": "5s4qi …",
                 "e": "AQAB",
                 "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
             }
         ]
     },
     "metadata_policy": {
         "openid_relying_party": {
             "scope": {
                 "superset_of": [
                     "openid"
                 ],
                 "subset_of": [
                     "openid",
                     "offline_access"
                 ]
             },
             "contacts": {
                 "add": [
                     "tech@example.it"
                 ]
             }
         }
     },
     "trust_marks": [
         {
             "id": "https://registry.agid.gov.it/openid_relying_party/public/",
             "trust_mark": "eyJhb …"
         }
     ]
 } 



.. _Esempio_EN3:

EN 3. Entity List Request
+++++++++++++++++++++++++

.. code-block:: 

 GET /list?entity_type=openid_provider
 HTTP/1.1
 Host: registry.agid.gov.it



.. _Esempio_EN3.1:

EN 3.1. Entity List Response
++++++++++++++++++++++++++++

.. code-block:: 

 HTTP/1.1 200 OK
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/json
 
 ["https://openid-provider.it/", "https://spid.provider.it", … ]



EN 4. Resolve Entity Statement Endpoint Request
+++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: 

 GET /resolve/?sub=https://openid.provider.it/&anchor=https://registry.agid.gov.it/
 HTTP/1.1
 Host: registry.agid.gov.it



EN 4.1. Resolve Entity Statement Endpoint Response
++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python

 HTTP/1.1 200 OK
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/entity-statement+jwt 
 
 {
     "alg": "RS256",
     "kid": "FifYx03bnosD8m6gYQIfNHNP9cM_Sam9Tc5nLloIIrc",
     "typ": "entity-statement+jwt"
 }
 .
 {
     "iss": "https://registry.agid.gov.it/",
     "sub": "https://rp.example.it/",
     "iat": 1649355587,
     "exp": 1649410329,
     "trust_marks": [
         {
             "id": "https://registry.agid.gov.it/openid_relying_party/public/",
             "trust_mark": "eyJh …"
         }
     ],
     "metadata": {
         "openid_relying_party": {
             "application_type": "web",
             "client_id": "https://rp.example.it/",
             "client_registration_types": [
                 "automatic"
             ],
             "jwks": {
                 "keys": [
                     {
                         "kty": "RSA",
                         "use": "sig",
                         "n": "…",
                         "e": "AQAB",
                         "kid": "5NNNoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
                     }
                 ]
             },
             "client_name": "Name of an example organization",
             "contacts": [
                 "ops@rp.example.it"
             ],
             "grant_types": [
                 "refresh_token",
                 "authorization_code"
             ],
             "redirect_uris": [
                 "https://rp.example.it/oidc/rp/callback/"
             ],
             "response_types": [
                 "code"
             ],
             "subject_type": "pairwise"
         }
     },
     "trust_chain": [
         "eyJhbGciOiJSUzI1NiIsImtpZCI6Ims1NEhRdERpYnlHY3M5WldWTWZ2aUhm ...",
         "eyJhbGciOiJSUzI1NiIsImtpZCI6IkJYdmZybG5oQU11SFIwN2FqVW1BY0JS ...",
         "eyJhbGciOiJSUzI1NiIsImtpZCI6IkJYdmZybG5oQU11SFIwN2FqVW1BY0JS ..."
     ]
 }

EN 5. Trust Mark Status Request
+++++++++++++++++++++++++++++++

.. code-block:: http

 POST /trust_mark_status HTTP/1.1
 Host: registry.agid.gov.it
 Content-Type: application/x-www-form-urlencoded
 
 id=https%3A%2F%2registry.agid.gov.it%2Fopenid_relying_party%2Fpublic%2F
 &sub=https%3A%2F%2rp.example.it%2F
 

EN 5.1. Trust Mark Status Response
++++++++++++++++++++++++++++++++++

.. code-block:: python

 HTTP/1.1 200 OK
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/json
 
 {"active": true}

.. _Esempio_EN6:

EN 6. Authorization Request
++++++++++++++++++++++++++++

**Example (HTTP request):**

.. code-block:: 

  GET /auth?client_id=https://rp.spid.agid.gov.it&
  response_type=code&scope=openid& code_challenge=qWJlMe0xdbXrKxTm72EpH659bUxAxw80&
  code_challenge_method=S256&
  request=eyJhbGciOiJSUzI1NiIsImtpZCI6IjJIbm9GUzNZbkM5dGppQ2FpdmhXTFZVSj
  NBeHdHR3pfOTh1UkZhcU1FRXMifQ.eyJpc3MiOiJodHRwczovL3RydXN0LWFuY2hvci5va
  WRjLWZlZGVyYXRpb24ub25saW5lL29pZGMvcnAvIiwic2NvcGUiOiJvcGVuaWQiLCJyZWR
  pcmVjdF91cmkiOiJodHRwczovL3RydXN0LWFuY2hvci5vaWRjLWZlZGVyYXRpb24ub25sa
  W5lL29pZGMvcnAvY2FsbGJhY2siLCJyZXNwb25zZV90eXBlIjoiY29kZSIsIm5vbmNlIjo
  iOXhnTWc4NHpsTG12OFJvRjg1RjJ5WExmdDQ1U3ZGUXciLCJzdGF0ZSI6InplaTJ6Mnh4e
  jZYQUFZUHM0eUlxRzZ2aWpQNDJyTVpHIiwiY2xpZW50X2lkIjoiaHR0cHM6Ly90cnVzdC1
  hbmNob3Iub2lkYy1mZWRlcmF0aW9uLm9ubGluZS9vaWRjL3JwLyIsImVuZHBvaW50Ijoia
  HR0cHM6Ly90cnVzdC1hbmNob3Iub2lkYy1mZWRlcmF0aW9uLm9ubGluZS9vaWRjL29wL2F
  1dGhvcml6YXRpb24iLCJhY3JfdmFsdWVzIjoiaHR0cHM6Ly93d3cuc3BpZC5nb3YuaXQvU
  3BpZEwyIiwiaWF0IjoxNjg2NTc2OTI2LCJleHAiOjE2ODY1NzY5ODYsImp0aSI6IjAxMjZ
  lZWRlLWUwZjMtNDE3My05NzE3LTQ0NzUyMmI2NmI2NyIsImF1ZCI6WyJodHRwczovL3Ryd
  XN0LWFuY2hvci5vaWRjLWZlZGVyYXRpb24ub25saW5lL29pZGMvb3AvIiwiaHR0cHM6Ly9
  0cnVzdC1hbmNob3Iub2lkYy1mZWRlcmF0aW9uLm9ubGluZS9vaWRjL29wL2F1dGhvcml6Y
  XRpb24iXSwiY2xhaW1zIjp7ImlkX3Rva2VuIjp7ImdpdmVuX25hbWUiOnsiZXNzZW50aWF
  sIjp0cnVlfSwiZW1haWwiOnsiZXNzZW50aWFsIjp0cnVlfX0sInVzZXJpbmZvIjp7Imdpd
  mVuX25hbWUiOm51bGwsImZhbWlseV9uYW1lIjpudWxsLCJlbWFpbCI6bnVsbCwiaHR0cHM
  6Ly9hdHRyaWJ1dGVzLnNwaWQuZ292Lml0L2Zpc2NhbF9udW1iZXIiOm51bGx9fSwicHJvb
  XB0IjoiY29uc2VudCBsb2dpbiIsImNvZGVfY2hhbGxlbmdlIjoidllobWRZcUNtMW1tZTJ
  HcUZkRFdweHlvdEFPc3dlX0RFV0lNYUlUcHlOTSIsImNvZGVfY2hhbGxlbmdlX21ldGhvZ
  CI6IlMyNTYifQ.r1ei1Wep3p---8XFXEwptev-tlyzNBPnOiYk5Z11OY7cvHuRhExmMFmN
  vyztwjQZRB92LsDMEaOs3bTfj_19S_L28o8MAMmjD5BO-obE8b_8rMNY4uVCAyNwzC6NVC
  XnGQymH1UJWHvWGGUF_xO-8JVbWhV7cGJiwCrfaX3H-ZPyFQInHJh3NQ9uN2vk-FZvKl1I
  urWVC4kUpe4FZKHX-2FjRe5kBKwPCw2eCMJgY-eSG0zEzukyHz5l3oUPQdk-olg3gowbNm
  AB6nkURsiJqxu1clrEgnDIeM4yN0m-sEGXLehS40Iqds75e8IMfYBYqCQ2LgU9PwF5gr7e
  iSQD8A

  Host: https://op.spid.agid.gov.it
  HTTP/1.1
  
**Example of JWT payload:**

.. code-block:: python

  {
  "alg": "RS256",
  "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
  }
  .
  {
      "client_id": "https://rp.spid.agid.gov.it",
      "response_type": "code",
      "scope": "openid",
      "code_challenge": "qWJlMe0xdbXrKxTm72EpH659bUxAxw80",
      "code_challenge_method": "S256",
      "nonce": "MBzGqyf9QytD28eupyWhSqMj78WNqpc2",
      "prompt": "login",
      "redirect_uri": "https://rp.spid.agid.gov.it/callback1",
      "acr_values": {
        "https://www.spid.gov.it/SpidL1":null,
        "https://www.spid.gov.it/SpidL2":null
      },
      "claims": {
        "userinfo": {
            "given_name":null,
            "family_name":null
        }
      },
      "state": "fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd"
  }

.. _Esempio_EN7:

EN 7. Metadata Policy
+++++++++++++++++++++

The following example shows a Metadata policy in the Entity Statement provided by a TA and related to an RP

.. code-block:: python

    "metadata_policy": {
        "openid_relying_party": {
            "jwks": {
                "value": {
                    "keys": [
                        {
                            "kty": "RSA",
                            "e": "AQAB",
                            "use": "sig",
                            "kid": "....",
                            "n": "....."
                        },
                        {
                            "kty": "RSA",
                            "e": "AQAB",
                            "use": "enc",
                            "kid": "....",
                            "n": "....."
                        }
                    ]
            },
            "grant_types": {
                "subset_of": [
                    "authorization_code",
                    "refresh_token"
                ],
                "superset_of": [
                    "authorization_code"
                ]
            },
            "id_token_signed_response_alg": {
                "one_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "essential": true
            },
            "id_token_encrypted_response_alg": {
                "one_of": [
                    "RSA-OAEP",
                    "RSA-OAEP-256",
                    "ECDH-ES",
                    "ECDH-ES+A128KW",
                    "ECDH-ES+A256KW"
                ],
                "essential": false
            },
            "id_token_encrypted_response_enc": {
                "one_of": [
                    "A128CBC-HS256",
                    "A256CBC-HS512"
                ],
                "essential": false
            },
            "userinfo_signed_response_alg": {
                "one_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "essential": true
            },
            "userinfo_encrypted_response_alg": {
                "one_of": [
                    "RSA-OAEP",
                    "RSA-OAEP-256",
                    "ECDH-ES",
                    "ECDH-ES+A128KW",
                    "ECDH-ES+A256KW"
                ],
                "essential": true
            },
            "userinfo_encrypted_response_enc": {
                "one_of": [
                    "A128CBC-HS256",
                    "A256CBC-HS512"
                ],
                "essential": true
            },
            "token_endpoint_auth_method": {
                "one_of": [
                    "private_key_jwt"
                ],
                "essential": true
            },
            "client_registration_types": {
                "subset_of": [
                    "automatic"
                ],
                "essential": true
            },
            "redirect_uris": {
                "essential": true
            },
            "client_id": {
                "essential": true
            },
            "response_types": {
                "value": [
                    "code"
                ]
            }
        }
    }

The following example shows a Metadata policy in the Entity Statement provided by a TA and related to an SA

.. code-block:: python

    "metadata_policy": {
        "openid_relying_party": {
            "grant_types": {
                "subset_of": [
                    "authorization_code",
                    "refresh_token"
                ],
                "superset_of": [
                    "authorization_code"
                ]
            },
            "id_token_signed_response_alg": {
                "one_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "essential": true
            },
            "id_token_encrypted_response_alg": {
                "one_of": [
                    "RSA-OAEP",
                    "RSA-OAEP-256",
                    "ECDH-ES",
                    "ECDH-ES+A128KW",
                    "ECDH-ES+A256KW"
                ],
                "essential": false
            },
            "id_token_encrypted_response_enc": {
                "one_of": [
                    "A128CBC-HS256",
                    "A256CBC-HS512"
                ],
                "essential": false
            },
            "userinfo_signed_response_alg": {
                "one_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "essential": true
            },
            "userinfo_encrypted_response_alg": {
                "one_of": [
                    "RSA-OAEP",
                    "RSA-OAEP-256",
                    "ECDH-ES",
                    "ECDH-ES+A128KW",
                    "ECDH-ES+A256KW"
                ],
                "essential": true
            },
            "userinfo_encrypted_response_enc": {
                "one_of": [
                    "A128CBC-HS256",
                    "A256CBC-HS512"
                ],
                "essential": true
            },
            "token_endpoint_auth_method": {
                "one_of": [
                    "private_key_jwt"
                ],
                "essential": true
            },
            "client_registration_types": {
                "subset_of": [
                    "automatic"
                ],
                "essential": true
            },
            "redirect_uris": {
                "essential": true
            },
            "client_id": {
                "essential": true
            },
            "response_types": {
                "value": [
                    "code"
                ]
            }
        }
    }


The following example shows a Metadata policy in the Entity Statement provided by a SA and related to an RP

.. code-block:: python

    "metadata_policy": {
        "openid_relying_party": {
            "jwks": {
                "value": {
                    "keys": [
                        {
                            "kty": "RSA",
                            "e": "AQAB",
                            "use": "sig",
                            "kid": "....",
                            "n": "....."
                        },
                        {
                            "kty": "RSA",
                            "e": "AQAB",
                            "use": "enc",
                            "kid": "....",
                            "n": "....."
                        }
                    ]
            },
        }
    }

The following example shows a Metadata policy in the Entity Statement provided by a TA and related to an OP.

.. code-block:: python

    "metadata_policy": {
        "openid_relying_party": {
            "jwks": {
                "value": {
                    "keys": [
                        {
                            "kty": "RSA",
                            "e": "AQAB",
                            "use": "sig",
                            "kid": "....",
                            "n": "....."
                        },
                        {
                            "kty": "RSA",
                            "e": "AQAB",
                            "use": "enc",
                            "kid": "....",
                            "n": "....."
                        }
                    ]
            },
            "revocation_endpoint_auth_methods_supported": {
                "subset_of": [
                    "private_key_jwt"
                ],
                "essential": true
            },
            "code_challenge_methods_supported": {
                "subset_of": [
                    "S256"
                ],
                "essential": true
            },
            "scopes_supported": {
                "subset_of": [
                    "openid",
                    "offline_access",
                    "profile",
                    "email"
                ],
                "superset_of": [
                    "openid",
                    "offline_access"
                ]
            },
            "response_types_supported": {
                "subset_of": [
                    "code"
                ],
                "essential": true
            },
            "response_modes_supported": {
                "subset_of": [
                    "form_post",
                    "query"
                ],
                "superset_of": [
                    "form_post",
                    "query"
                ],
                "essential": true
            },
            "grant_types_supported": {
                "subset_of": [
                    "authorization_code",
                    "refresh_token"
                ],
                "superset_of": [
                    "authorization_code",
                    "refresh_token"
                ],
                "essential": true
            },
            "acr_values_supported": {
                "subset_of": [
                    "https://www.spid.gov.it/SpidL1",
                    "https://www.spid.gov.it/SpidL2",
                    "https://www.spid.gov.it/SpidL3"
                ],
                "superset_of": [
                    "https://www.spid.gov.it/SpidL1",
                    "https://www.spid.gov.it/SpidL2",
                    "https://www.spid.gov.it/SpidL3"
                ],
                "essential": true
            },
            "subject_types_supported": {
                "subset_of": [
                    "pairwise"
                ],
                "essential": true
            },
            "id_token_signing_alg_values_supported": {
                "subset_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "superset_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "essential": true
            },
            "id_token_encryption_alg_values_supported": {
                "subset_of": [
                    "RSA-OAEP",
                    "RSA-OAEP-256",
                    "ECDH-ES",
                    "ECDH-ES+A128KW",
                    "ECDH-ES+A256KW"
                ],
                "superset_of": [
                    "RSA-OAEP",
                    "RSA-OAEP-256",
                    "ECDH-ES",
                    "ECDH-ES+A128KW",
                    "ECDH-ES+A256KW"
                ],
                "essential": true
            },
            "id_token_encryption_enc_values_supported": {
                "subset_of": [
                    "A128CBC-HS256",
                    "A256CBC-HS512"
                ],
                "superset_of": [
                    "A128CBC-HS256",
                    "A256CBC-HS512"
                ],
                "essential": true
            },
            "userinfo_signing_alg_values_supported": {
                "subset_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "superset_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "essential": true
            },
            "userinfo_encryption_alg_values_supported": {
                "subset_of": [
                    "RSA-OAEP",
                    "RSA-OAEP-256",
                    "ECDH-ES",
                    "ECDH-ES+A128KW",
                    "ECDH-ES+A256KW"
                ],
                "superset_of": [
                    "RSA-OAEP",
                    "RSA-OAEP-256",
                    "ECDH-ES",
                    "ECDH-ES+A128KW",
                    "ECDH-ES+A256KW"
                ],
                "essential": true
            },
            "userinfo_encryption_enc_values_supported": {
                "subset_of": [
                    "A128CBC-HS256",
                    "A256CBC-HS512"
                ],
                "superset_of": [
                    "A128CBC-HS256",
                    "A256CBC-HS512"
                ],
                "essential": true
            },
            "token_endpoint_auth_methods_supported": {
                "subset_of": [
                    "private_key_jwt"
                ],
                "essential": true
            },
            "token_endpoint_auth_signing_alg_values_supported": {
                "subset_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "superset_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "essential": true
            },
            "claims_parameter_supported": {
                "value": true
            },
            "request_parameter_supported": {
                "value": true
            },
            "authorization_response_iss_parameter_supported": {
                "value": true
            },
            "client_registration_types_supported": {
                "subset_of": [
                    "automatic"
                ],
                "essential": true
            },
            "request_authentication_methods_supported": {
                "value": {
                    "authorization_endpoint": [
                        "request_object"
                    ]
                }
            },
            "request_authentication_signing_alg_values_supported": {
                "subset_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "superset_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "essential": true
            },
            "request_object_signing_alg_values_supported": {
                "subset_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "superset_of": [
                    "RS256",
                    "RS512",
                    "ES256",
                    "ES512",
                    "PS256",
                    "PS512"
                ],
                "essential": true
            },
            "issuer": {
                "essential": true
            },
            "authorization_endpoint": {
                "essential": true
            },
            "token_endpoint": {
                "essential": true
            },
            "userinfo_endpoint": {
                "essential": true
            },
            "introspection_endpoint": {
                "essential": true
            },
            "revocation_endpoint": {
                "essential": true
            }
        }
    }
