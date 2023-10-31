.. include:: ../common/common_definitions.rst

.. _Soggetti_aggregatori:

Intermediate Entities
^^^^^^^^^^^^^^^^^^^^^

An Intermediate Entity (SA) can register pre-existing RPs that are compliant to the OIDC-FED standard or mask their subordinates behind it. In the first case, the SA is of type *Transparent* (**Light Aggregator**), and in the second case it is of type *Proxy* (**Full Aggregator**)

The **Light** SAs register pre-existing RPs that are compliant to OIDC-FED and publishes the ESs referred to them.

The **Full** SAs arrange building an authentication and federation interface, on behalf of their own subordinates, by using web resources that are usually exposed inside their own domain. This kind of SAs expose for each of their subordinates, the following resources:

    - **.well-known/openid-federation**, containing the Leaf's Entity Configuration;
    - Authorization callback endpoint for obtaining the auth code by the OP (**redirect_uri**).

The **Full** type SAs MUST add at least one of the available identification code in the **id_code** (as defined in the Section :ref:`Trust Mark Composition <ComposizioneTM>`) inside the web path, which in turn is inside the client_id that identifies the subordinate Entity ``<SA_domain>/<id_code>/``. If more than one identification code is available, the SA MAY include them in the web path as in the following example: ``<SA_domain>/ipa_code/aoo_code/``.

The following table contains some non-normative examples for outlining the differences between the SAs of
types Light and Full:

.. list-table::
    :widths: 10 50 50
    :header-rows: 1

    * - 
      - Mode **Light**
      - Mode **Full**
    * - **client_id**
      - \https://www.rp.it/
      - \https://www.sa.it/<id_code>/
    * - **redirect_uri**
      - \https://www.rp.it/callback/
      - \https://www.sa.it/<id_code>/callback/
    * - **authz endpoint**
      - \https://www.rp.it/authorization/
      - \https://www.sa.it/<id_code>/authorization/
    * - **Entity Configuration**
      - \https://www.rp.it/.well-known/openid-federation
      - \https://www.sa.it/<id_code>/.well-known/openid-federation
