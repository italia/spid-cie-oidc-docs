.. include:: ../common/common_definitions.rst

Trust Negotiation
-----------------

This section explains the ways of mutual recognition between RP and OP, the ways for the Leaves to recognize each other inside the same Federation and to obtain each other's Metadata.


Relying Party
+++++++++++++

The RP gets the list of the OPs in JSON format by querying the :ref:`endpoint list<federation_endpoint>`, 
available by the :ref:`Trust Anchor<Esempio_EN3>`. For each subject contained in the :ref:`answer<Esempio_EN3.1>` and corresponding to an OP, the RP :ref:`requires<Esempio_EN2>` and obtains the self-signed Entity Configuration by the OP.

For each EC of the OPs, the RP validates the signature by using the public key obtained by the Entity
Statement released by the Trust Anchor. After validating the Entity Configuration signature with the TA's public key, RP recognizes the trust towards the OP.

Finally, the RP applies the policies published by the Trust Anchor on the OP's Metadata and saves the final
Metadata by associating it to an expiry date (claim **exp**). The expiry date corresponds to the lowest 
value of **exp**, obtained from all the elements that compose the **Trust Chain**. Periodically, the RP updates
the Metadata of all the OPs, renewing their related Trust Chain.

After obtaining the final Metadata of all the OpenID Connect Providers, the RP generates the **SPID button** or **CIE button** and publishes it inside the users' authentication page.

The procedure of Metadata Discovery for the SPID RPs gets simplified because, inside the Federation, the existence of Intermediaries between the OPs and their Trust Anchor, is not allowed.


.. image:: ../../images/metadata_discovery.svg
    :width: 100%

*The Metadata Discovery procedure from the Leaf, up to the Trust Anchor. Please note how the public key for validating the Entity Configuration of the  subordinate Entity, is obtained from the Entity Statement released by a superior*.


OpenID Provider
+++++++++++++++

When a Provider (OP) receives an authorization request from a non-previously-recognized RP, 
the **automatic client registration** procedure occurs. Following, the operations made by the OP to
dynamically register an RP, are described.

.. image:: ../../images/automatic_client_registration.svg
    :width: 100%


*The registration of an RP from the perspective of an OP that, for the first time, receives an authorization
request from the RP and starts the Metadata Discovery process and the Trust Chain saving*.


The OP extracts the unique identifier (**client_id**) from the object *request* contained in the 
*Authorization Request* and carries out an Entity Configuration request by the :ref:`RP<Esempio_EN1.1>`.
It obtains the *self-signed* configuration of the RP and validates the signatures of Trust Mark that are
recognized inside the Federation [1]_. 

If the RP configuration does not expose any Trust Mark that is recognizable by the RP profile (see Section :ref:`Trust Mark<Trust_Mark>`), the Provider MUST refuse the authorization with an error message of type *unauthorized_client*.

If the Provider successfully validates at least a Trust Mark for the RP profile contained inside the
configuration of the requesting RP, it extracts the superior Entities from the claim **authority_hints** and
starts the Metadata Discovery process. Following, the **Trust Chain** calculation and the achievement of 
the final Metadata.

During the Metadata Discovery, the Provider requests one ore more superior Entities [2]_ for the Entity
Statement regarding the RP, obtains the public key for validating the RP configuration and finally reaches
the Trust Anchor. Then it applies the Metadata policy published by the Trust Anchor and saves the 
resulting final RP Metadata, associating them to an expiry date. After that date, it will
renew the RP Metadata, according to the Trust Chain renewal procedure.

After obtaining the final Metadata, the Provider validates the RP request, according to the procedures 
defined in the Federation's guidelines.

In case an RP has an SA as a superior Entity and not directly the TA, the procedure of achieving and validating the Entity Configuration of the RP occurs through the Entity Statement published
by the SA towards the RP and through validating the Entity Configuration of the SA with the Entity Statement issued by the TA towards the SA. If the threshold of the maximum number of vertical Intermediaries, 
defined by the value **max_path_length**, is exceeded, the OP stops the process of Metadata Discovery and rejects the RP request.


.. [1] The Federation Trust Marks are configured in the claim **trust_marks_issuers** and contained in the Entity Configuration of the Trust Anchor.

.. [2] An RP can expose more than one superior Entity inside its own claim **authority_hints**. An example is an RP that takes part both in the SPID and in the CIE Federation. Besides, an RP can result as a subordinate of more than one Intermediaries, either of SPID or CIE.


.. image:: ../../images/trust_anchor.svg
    :width: 100%

*Each member exposes its own configuration and its own Trust Marks. The link between a Leaf and 
the Trust Anchor occurs directly or through an Intermediary (SA) as in the picture.*


Access to the Entity Configuration
++++++++++++++++++++++++++++++++++

This section describes how to identify the URL :rfc:`3986` for downloading the Entity Configuration of a given subject.

The resource for member for publishing its configuration (Entity Configuration) corresponds to 
the web path ``.well-known/openid-federation`` and MUST be hung upon the URL the identifies the subject.

Examples:

 - with a subject identifier equal to ``https://rp.example.it`` the resulting Entity Configuration URL is |br|
   ``https://rp.example.it/.well-known/oidc-federation``.

 - with a subject identifier equal to ``https://rp.servizi-spid.it/oidc/`` the resulting 
   Entity Configuration URL is |br|
   ``https://rp.servizi-spid.it/oidc/.well-known/oidc-federation``.

If not present at the end of the URL that identifies a subject, the slash mark ("/") must be added before
concatenating the web path to the .well-known resource.

Once the RP is recognized as part in the Federation, it gets the permission to make an Authentication Request.
An OP that doesn't recognize the RP that makes the request, can correctly resolve the Trust. The OP starts
requesting the Entity Configuration of the RP at the .well-known endpoint of the RP and, following the path
provided by the *authority_hint*, reaches the TA. At each chain step, the OP can perform all the security controls by requesting the Entity Statements to each Entity and validating the Trust Marks and the signatures. The following picture is a representative example of how the Trust Chain works.


.. image:: ../../images/cie_esempio_trust_chain.svg
    :width: 100%


*The Metadata Discovery process to build a Trust Chain and obtain the final Metadata.*


