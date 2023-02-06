.. include:: ../common/common_definitions.rst

Metadata retrieval
------------------

This section explains the ways the participants of a federation have to establish the trust among them, the ways for the Leaves to recognize each other inside the same federation and get each other's Metadata.


Relying Party
+++++++++++++

The RP gets the list of the OPs in JSON format by querying the :ref:`endpoint list<federation_endpoint>`, 
available by the :ref:`Trust Anchor<Esempio_EN3>`. For each subject contained in the :ref:`JSON response<Esempio_EN3.1>` and corresponding to an OP, the RP :ref:`requests<Esempio_EN2>` the Entity Configuration of the OP.

For each EC of the OPs, the RP validates the signature of the OP Entity Configuration using the public key obtained in the Entity
Statement released by the Trust Anchor for that OP. After validating the Entity Configuration signature, the RP establishes the trust with the OP.

Finally, the RP applies the policies published by the Trust Anchor on the OP's Metadata and saves the resulting
Metadata by associating it to an expiry date (claim **exp**). The expiry date corresponds to the lowest 
value of **exp**, obtained from all the elements that compose the **Trust Chain**. Periodically, the RP updates
the Metadata of all the OPs, renewing their related Trust Chain.

After obtaining the final Metadata of all the OpenID Connect Providers, the RP generates the **SPID button** or **CIE button** and publishes it inside its authentication page.

The procedure of Federation Entity Discovery for the RPs gets simplified because, inside the Federation, the existence of Intermediates between the OPs and their Trust Anchor is not allowed.


.. image:: ../../images/metadata_discovery.svg
    :width: 100%

*The Federation Entity Discovery procedure from the Leaf, up to the Trust Anchor. The public key for validating the Entity Configuration of the  subordinate Entity is obtained from the Entity Statement released by a superior*.


OpenID Provider
+++++++++++++++

When a Provider (OP) receives an authorization request from a non-previously-recognized RP, 
the **automatic client registration** procedure occurs. The operations made by the OP to
dynamically register an RP are described below.

.. image:: ../../images/automatic_client_registration.svg
    :width: 100%


*The registration of an RP from the perspective of an OP that, for the first time, receives an authorization
request from the RP and starts the Federation Entity Discovery process and the Trust Chain saving*.


The OP extracts the unique identifier (**client_id**) from the object *request* contained in the 
*Authorization Request* and sends an Entity Configuration request (:ref:`RP<Esempio_EN1.1>`).
The OP obtains the Entity Configuration of the RP and validates the signatures of Trust Mark that are
recognized inside the Federation [1]_. 

If the RP configuration does not expose any Trust Mark that is recognizable by the RP profile (see Section :ref:`Trust Mark<Trust_Mark>`), the Provider MUST refuse the authorization with an error message as defined in Section :ref:`Federation Error Management <errors_federation>`.

If the Provider successfully validates at least a Trust Mark for the RP profile contained inside the
configuration of the requesting RP, it extracts the superior Entities from the claim **authority_hints** and
starts the Federation Entity Discovery process until the **Trust Chain** calculation and the achievement of 
the final Metadata.

During the Federation Entity Discovery, the Provider requests one ore more superior Entities [2]_ for the Entity
Statement regarding the RP, obtains the public key for validating the RP configuration and finally reaches
the Trust Anchor. Then it applies the Metadata policy published by the Trust Anchor and saves the 
resulting final RP Metadata, associating them to an expiry date. After that date, it will
renew the RP Metadata, according to the Trust Chain renewal procedure.

After obtaining the final Metadata, the Provider validates the request sent by RP.

In case an RP has a SA as a superior Entity and not directly the TA, the procedure of achieving and validating the Entity Configuration of the RP occurs through the Entity Statement published
by the SA towards the RP and through validating the Entity Configuration of the SA with the Entity Statement issued by the TA towards the SA. If the threshold of the maximum number of vertical Intermediates, 
defined by the value **max_path_length**, is exceeded, the OP stops the process of Federation Entity Discovery and rejects the RP request.


.. [1] The Federation Trust Marks are configured in the claim **trust_marks_issuers** and contained in the Entity Configuration of the Trust Anchor.

.. [2] An RP can expose more than one superior Entity inside its own claim **authority_hints**. An example is an RP that takes part both in the SPID and in the CIE Federation. Besides, an RP can result as a subordinate of more than one Intermediates, either of SPID or CIE.


.. image:: ../../images/trust_anchor.svg
    :width: 100%

*Each member exposes its own configuration and its own Trust Marks. The link between a Leaf and 
the Trust Anchor occurs directly or through an Intermediate (SA) as in the picture.*


Access to the Entity Configuration
++++++++++++++++++++++++++++++++++

This section describes how to identify the URL :rfc:`3986` in order to download the Entity Configuration of a given subject.

The web path ``.well-known/openid-federation`` is the resource by which an Entity publishes its configuration (Entity Configuration). This web path MUST be appended to the URL which identifies the subject.

Examples:

 - with a subject identifier equal to ``https://rp.example.it`` the resulting Entity Configuration URL is |br|
   ``https://rp.example.it/.well-known/oidc-federation``.

 - with a subject identifier equal to ``https://rp.servizi-spid.it/oidc/`` the resulting 
   Entity Configuration URL is |br|
   ``https://rp.servizi-spid.it/oidc/.well-known/oidc-federation``.

In case of subject identifier URLs lacking the ending slash mark "/", this must be added between the URL and the appended web path resource.

Once the RP is recognized as part in the Federation, it gets the permission to make an Authentication Request.
The OP that doesn't recognize the RP that sent the request, has to resolve the trust for that RP. The OP starts
requesting the Entity Configuration of the RP at the .well-known endpoint of the RP and, following the path
provided by the *authority_hint*, reaches the TA. At each chain step, the OP can perform all the security controls by requesting the Entity Statements to each Entity and validating the Trust Marks and the signatures. The following picture is a representative example of how the Trust Chain works.


.. image:: ../../images/cie_esempio_trust_chain.svg
    :width: 100%


*The Federation Entity Discovery process to build a Trust Chain and obtain the final Metadata.*
