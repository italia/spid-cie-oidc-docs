
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
             "federation_resolve_endpoint": "https://rp.example.it/resolve/"
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
                 "https://attributes.spid.gov.it/spidCode",
                 "https://attributes.spid.gov.it/name",
                 "https://attributes.spid.gov.it/familyName",
                 "https://attributes.spid.gov.it/placeOfBirth",
                 "https://attributes.spid.gov.it/countyOfBirth",
                 "https://attributes.spid.gov.it/dateOfBirth",
                 "https://attributes.spid.gov.it/gender",
                 "https://attributes.spid.gov.it/companyName",
                 "https://attributes.spid.gov.it/registeredOffice",
                 "https://attributes.spid.gov.it/fiscalNumber",
                 "https://attributes.spid.gov.it/ivaCode",
                 "https://attributes.spid.gov.it/idCard",
                 "https://attributes.spid.gov.it/mobilePhone",
                 "https://attributes.spid.gov.it/email",
                 "https://attributes.spid.gov.it/address",
                 "https://attributes.spid.gov.it/expirationDate",
                 "https://attributes.spid.gov.it/digitalAddress"
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
..               "request_object_encryption_alg_values_supported": [
..                   "RSA-OAEP",
..                   "RSA-OAEP-256"
..               ],
..               "request_object_encryption_enc_values_supported": [
..                   "A128CBC-HS256",
..                   "A192CBC-HS384",
..                   "A256CBC-HS512",
..                   "A128GCM",
..                   "A192GCM",
..                   "A256GCM"
..               ],
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
             "federation_resolve_endpoint": "https://openid.provider.it/resolve/"
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
             "id": "https://registry.gov.it/federation_entity/private/",
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
             "id": "https://registry.interno.gov.it/intermediary/",
             "iss": "https://registry.interno.gov.it/",
             "trust_mark": "$JWT"
         }
     ]
 }


Where the $JWT payload is:

.. code-block:: json

 {
     "id": "https://registry.interno.gov.it/intermediary/",
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

.. code-block:: http

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

.. code-block:: http

 GET /list?entity_type=openid_provider
 HTTP/1.1
 Host: registry.agid.gov.it



.. _Esempio_EN3.1:

EN 3.1. Entity List Response
++++++++++++++++++++++++++++

.. code-block:: http

 HTTP/1.1 200 OK
 Last-Modified: Wed, 22 Jul 2018 19:15:56 GMT
 Content-Type: application/json
 
 ["https://openid-provider.it/", "https://spid.provider.it", … ]



EN 4. Resolve Entity Statement Endpoint Request
+++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: http

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

.. code-block:: http

  GET /auth?client_id=https://rp.spid.agid.gov.it&
  response_type=code&scope=openid& code_challenge=qWJlMe0xdbXrKxTm72EpH659bUxAxw80&
  code_challenge_method=S256&request=eyJhbGciOiJSUzI1NiIsImtpZCI6ImsyYmRjIn0.ew0KIC
  Jpc3MiOiAiczZCaGRSa3F0MyIsDQogImF1ZCI6ICJodHRwczovL3NlcnZlci5leGFtcGxlLmNvbSIsDQo
  gInJlc3BvbnNlX3R5cGUiOiAiY29kZSBpZF90b2tlbiIsDQogImNsaWVudF9pZCI6ICJzNkJoZFJrcXQz
  IiwNCiAicmVkaXJlY3RfdXJpIjogImh0dHBzOi8vY2xpZW50LmV4YW1wbGUub3JnL2NiIiwNCiAic2Nvc
  GUiOiAib3BlbmlkIiwNCiAic3RhdGUiOiAiYWYwaWZqc2xka2oiLA0KICJub25jZSI6ICJuLTBTNl9Xek
  EyTWoiLA0KICJtYXhfYWdlIjogODY0MDAsDQogImNsYWltcyI6IA0KICB7DQogICAidXNlcmluZm8iOiA
  NCiAgICB7DQogICAgICJnaXZlbl9uYW1lIjogeyJlc3NlbnRpYWwiOiB0cnVlfSwNCiAgICAgI…

  Host: https://op.spid.agid.gov.it
  HTTP/1.1
  
**Example of JWT payload:**

.. code-block:: python

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
            "https://attributes.spid.gov.it/name":null,
            "https://attributes.spid.gov.it/familyName":null
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
              "keys": [{
                "subset_of": [{
                    "kty": "RSA",
                    "use": "sig",
                    "n": "…",
                    "e": "AQAB",
                    "kid": "5NNNoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
                }]
              }]
            }
            "grant_types": {
                "subset_of": ["authorization_code", "refresh_token"]
            }
            "id_token_signed_response_alg": {
                "subset_of": ["RS256", "RS512", "ES256", "ES512", "PS256", "PS512"]
            }
            "id_token_encrypted_response_alg": {
                "subset_of": ["RSA-OAEP", "RSA-OAEP-256", "ECDH-ES", "ECDH-ES+A128KW", "ECDH-ES+A256KW"]
            }
            "id_token_encrypted_response_enc": {
                "subset_of": ["A128CBC-HS256", "A256CBC-HS512"]
            }
            "userinfo_signed_response_alg": {
                "subset_of": ["RS256", "RS512", "ES256", "ES512", "PS256", "PS512"]
            }
            "userinfo_encrypted_response_alg": {
                "subset_of": ["RSA-OAEP", "RSA-OAEP-256", "ECDH-ES", "ECDH-ES+A128KW", "ECDH-ES+A256KW"]
            }
            "userinfo_encrypted_response_enc": {
                "subset_of": ["A128CBC-HS256", "A256CBC-HS512"]
            }
            "token_endpoint_auth_method": {
                "one_of": ["private_key_jwt"]
            }
            "client_registration_types": {
                "one_of": ["automatic"]
            }
        }
    }

The following example shows a Metadata policy in the Entity Statement provided by a TA and related to an SA

.. code-block:: python

    "metadata_policy": {
        "openid_relying_party": {
            "grant_types": {
                "subset_of": ["authorization_code", "refresh_token"]
            }
            "id_token_signed_response_alg": {
                "subset_of": ["RS256", "RS512", "ES256", "ES512", "PS256", "PS512"]
            }
            "id_token_encrypted_response_alg": {
                "subset_of": ["RSA-OAEP", "RSA-OAEP-256", "ECDH-ES", "ECDH-ES+A128KW", "ECDH-ES+A256KW"]
            }
            "id_token_encrypted_response_enc": {
                "subset_of": ["A128CBC-HS256", "A256CBC-HS512"]
            }
            "userinfo_signed_response_alg": {
                "subset_of": ["RS256", "RS512", "ES256", "ES512", "PS256", "PS512"]
            }
            "userinfo_encrypted_response_alg": {
                "subset_of": ["RSA-OAEP", "RSA-OAEP-256", "ECDH-ES", "ECDH-ES+A128KW", "ECDH-ES+A256KW"]
            }
            "userinfo_encrypted_response_enc": {
                "subset_of": ["A128CBC-HS256", "A256CBC-HS512"]
            }
            "token_endpoint_auth_method": {
                "one_of": ["private_key_jwt"]
            }
            "client_registration_types": {
                "one_of": ["automatic"]
            }
        }
    }


The following example shows a Metadata policy in the Entity Statement provided by a SA and related to an RP

.. code-block:: python

    "metadata_policy": {
        "openid_relying_party": {
            "jwks": {
                "subset_of": [{
                    "kty": "RSA",
                    "use": "sig",
                    "n": "…",
                    "e": "AQAB",
                    "kid": "5NNNoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
                }]
            }
        }
    }

The following example shows a Metadata policy in the Entity Statement provided by a TA and related to an OP.

.. code-block:: python

    "metadata_policy": {
        "openid_relying_party": {
            "jwks": {
                "subset_of": [{
                    "kty": "RSA",
                    "use": "sig",
                    "n": "…",
                    "e": "AQAB",
                    "kid": "5NNNoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs"
                }]
            }
            "revocation_endpoint_auth_methods_supported": {
                "one_of": ["private_key_jwt"]
            }
            "code_challenge_methods_supported": {
                "subset_of": ["authorization_code", "refresh_token"]
            }
            "scopes_supported": {
                "subset_of": ["openid", "offline_access", "profile", "email"]
            }
            "response_types_supported": {
                "one_of": ["code"]
            }
            "response_modes_supported": {
                "subset_of": ["form_post", "query"]
            }
            "grant_types_supported": {
                "subset_of": ["authorization_code", "refresh_token"]
            }
            }
            "acr_values_supported": {
                "subset_of": ["https://www.spid.gov.it/SpidL1", "https://www.spid.gov.it/SpidL2", "https://www.spid.gov.it/SpidL3"]
            }
            }
            "subject_types_supported": {
                "one_of": ["pairwise"]
            }
            "id_token_signing_alg_values_supported": {
                "subset_of": ["RS256", "RS512", "ES256", "ES512", "PS256", "PS512"]
            }
            "id_token_encryption_alg_values_supported": {
                "subset_of": ["RSA-OAEP", "RSA-OAEP-256", "ECDH-ES", "ECDH-ES+A128KW", "ECDH-ES+A256KW"]
            }
            "id_token_encryption_enc_values_supported": {
                "subset_of": ["A128CBC-HS256", "A256CBC-HS512"]
            }
            "userinfo_signing_alg_values_supported": {
                "subset_of": ["RS256", "RS512", "ES256", "ES512", "PS256", "PS512"]
            }
            "userinfo_encryption_alg_values_supported": {
                "subset_of": ["RSA-OAEP", "RSA-OAEP-256", "ECDH-ES", "ECDH-ES+A128KW", "ECDH-ES+A256KW"]
            }
            "userinfo_encryption_enc_values_supported": {
                "subset_of": ["A128CBC-HS256", "A256CBC-HS512"]
            }
            "token_endpoint_auth_methods_supported": {
                "one_of": ["private_key_jwt"]
            }
            "token_endpoint_auth_signing_alg_values_supported": {
                "subset_of": ["RS256", "RS512", "ES256", "ES512", "PS256", "PS512"]
            }
            "claims_parameter_supported": {
                "one_of": ["true"]
            }
            "request_parameter_supported": {
                "one_of": ["true"]
            }
            "authorization_response_iss_parameter_supported": {
                "one_of": ["true"]
            }
            "client_registration_types_supported": {
                "one_of": ["automatic"]
            }
            "request_authentication_methods_supported": {
                "one_of": ["request_object"]
            }
            "request_authentication_signing_alg_values_supported": {
                "subset_of": ["RS256", "RS512", "ES256", "ES512", "PS256", "PS512"]
            }
        }
    }
