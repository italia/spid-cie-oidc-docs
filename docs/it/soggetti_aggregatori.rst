.. _Soggetti_aggregatori:

Soggetti Aggregatori
^^^^^^^^^^^^^^^^^^^^

Un SA può registrare RP preesistenti e già conformi allo standard OIDC-FED, afferenti a domini esterni al proprio oppure mascherare dietro di sé i propri discendenti. Nel primo caso il SA è di tipo *Trasparente* (**Aggregatore Light**) mentre nel secondo caso è di tipo *Proxy* (**Aggregatore Full**).

I SA **Light** registrano RP preesistenti e conformi a OIDC-FED e pubblicano gli ES a questi riferiti.

I SA **Full** provvedono a costruire una interfaccia di autenticazione e federazione per conto dei propri aggregati, mediante risorse web solitamente esposte all’interno del proprio dominio. Questa tipologia di Aggregatore espone le seguenti risorse per ogni suo aggregato:

    - **.well-known/openid-federation**, contenente un *subject identifier* del RP univoco;
    - Authorization callback endpoint per l’acquisizione dell’auth code da parte del OP (**redirect_uri**).

Il SA di tipo **Full** DEVE aggiungere l'**id_code** (così come definito nella Sezione :ref:`Composizione dei Trust Mark <ComposizioneTM>`), all’interno del webpath all’interno del client_id che identifica l’aggregato ``<SA_dominio>/<id_code>/``.

Nella seguente tabella sono presenti alcuni esempi non normativi per evidenziare le differenze tra gli aggregati Light e Full:

.. list-table::
    :widths: 10 50 50
    :header-rows: 1

    * - 
      - Modalità **Light**
      - Modalità **Full**
    * - **client_id**
      - \https://www.rp.it/
      - \https://www.rp.it/<id_code>/
    * - **redirect_uri**
      - \https://www.rp.it/callback/
      - \https://www.rp.it/<id_code>/callback/
    * - **authorization endpoint**
      - \https://www.rp.it/authorization/
      - \https://www.rp.it/<id_code>/authorization/
    * - **Entity Configuration**
      - \https://www.rp.it/.well-known/openid-federation
      - \https://www.rp.it/<id_code>/.well-known/openid-federation

