.. include:: ../common/common_definitions.rst

.. _Considerazioni_di_Sicurezza:

Security Considerations
-----------------------

In this section we describe some security considerations in the OIDC Federation scope.


Trust Marks as deterrent against abuses
+++++++++++++++++++++++++++++++++++++++

The TM implementation and the filter on the TMs in the process of Metadata Discovery, turn out to be necessary
against attacks aimed at the resource consumption. If an OP suffers an attack at the *authorization* endpoint and the attack consists of an high number of connections with fake **client_id** and **authority_hints**, then the OP, trying to find a path to the TA for establishing the trust with the requester, would produce several connections to third-party systems.

The OP MUST statically validate the TM or a-priori exclude the request whenever the TM is not present.
In case the TM is not present or not valid, the procedure of Metadata Discovery MUST NOT be started and consequently MUST NOT create connections to third party systems.


Maximum Number of authority_hints
+++++++++++++++++++++++++++++++++

Inside a Federation, through the constraint named **max_path_lenght**, the Trust Anchor decides how many intermediaries are allowed between it and the Leaves. This kind of relationship is vertical, from the Leaf to the root. As an example, if this attribute has the value equal to 1, it means that only one SA is allowed between a Leaf and the TA.

Every Leaf MUST publish its superiors inside the list contained in the claim **authority_hints**. A Leaf in the Federation CAN have superiors belonging to different Federations. The analysis of the available superiors introduces an horizontal navigation model. As an example, an OP tries to find the shortest path to the Trust Anchor through all the URLs contained in the array **authority_hints**, before doing a further vertical move upwards, to one of the Intermediaries that are present in this array.

The threshold **max_path_lenght** is applied to the vertical navigation and, after exceeding this threshold without finding a TA, the procedure of Metadata Discovery MUST be stopped. Consider the example of an RP that's a subordinate of an SA that's in turn a subordinate of another SA, while the **max_path_lenght** claim is equal to 1 and, after exceeding this threshold without finding the Trust Anchor, the procedure MUST be stopped.

At the same time, the specifications of OIDC Federation 1.0 don't define a limit of the number of **authority_hints**, and this is because no TA can limit the number of Federations in which a member can take part. For this reason, it is useful that implementers adopt a maximum limit to the number of elements allowed inside the array authority_hints. The reason is avoiding that an exaggerated number of URLs contained in the list **authority_hints**, due to a bad configuration of a Leaf, produce an excessive resource consumption.



Resolve Entity Statement
++++++++++++++++++++++++

This endpoint MUST release the Metadata, the Trust Marks and the previously processed Trust Chain, and MUST
NOT trigger a procedure of Metadata Discovery for each request arrival.



Good Practices
--------------

In this section we describe some good practices. 


Specializing the OpenID Core and Federation public keys
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

It is a good practice to use public keys that are specialized for the two kinds of operations, Core and Federation.

Upgrading strategy of the OpenID Metadata
+++++++++++++++++++++++++++++++++++++++++

The interoperability among members works through the Metadata obtained from the Trust Chain calculation and preservation. This means that if an OP at the time T calculates the Trust Chain for an RP and this, at the time T+n, changes its own Metadata, the OP could consequently run into problems of validating the RP authorization requests, until the OP will have once again updated the RP-related Trust Chain.

A good practice to avoid service stops on the OIDC Core operations, is adding the new public keys inside the objects *jwks* without removing the previous values. Or, for example, the new *redirect_uri*.

In this way, after exceeding the maximum duration limit of the Trust Chain, defined in the claim **exp** and published in the TA Entity Configuration, it is certain that all the members have renewed their Trust Chain and it is possible, for the Leaf administrators, to remove the old definitions from the top of the list.



Metadata Policy
+++++++++++++++

The Federation Authority or its Intermediary CAN publish a Metadata policy (see `OIDC-FED#Section.5.1`_) 
to force the change of the OIDC Metadata of the Leaf, in the parts where this might be needed.

