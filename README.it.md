# SPID/CIE OIDC Regole Tecniche

[![GitHub release](https://img.shields.io/github/release/italia/spid-cie-oidc-docs.svg?style=plastic)](https://github.com/italia/spid-cie-oidc-docs/releases)
[![Join the #spid openid](https://img.shields.io/badge/Slack%20channel-%23spid%20openid-blue.svg)](https://developersitalia.slack.com/archives/C7E85ED1N/)
[![Get invited](https://slack.developers.italia.it/badge.svg)](https://slack.developers.italia.it/)
[![Docs Italia](https://docs.italia.it/media/static/projects/badges/passing.svg)](https://docs.italia.it/italia/spid-cie-oidc-docs/it/master/index.html)
[![Documentation](https://img.shields.io/badge/Documentation-Docs%20Italia-blue.svg)](https://docs.italia.it/italia/spid-cie-oidc-docs/it/master/index.html)

---

## Table of Contents

- [Descrizione](#descrizione)
- [Documentazione](#documentazione)
- [Versioning](#versioning)
- [Contributing](#come-contribuire)
- [Autori](#autori)
- [License](#licenza)

## Descrizione

Scopo di questo repository


## Documentazione

Questo repository è strutturato per essere compatibile con [Docs Italia](https://docs.italia.it/italia/developers-italia/publiccodeyml/it/master/index.html).
Per questo motivo, il contenuto delle rilevanti cartelle sarà compilato
e renderizzato all'interno di tale piattaforma. `Docs Italia` è progettato per
supportare un documento localizzato in diverse lingue e per questo motivo è la
piattaforma di riferimento per visualizzare questo standard.


## Developers

````
pip install -r requirements.txt
sphinx-build -b html -d html/it/doctrees docs/it/  html/it
````

## Versioning


Questo progetto aderisce al modello di versioning [*Semantic
Versioning*](https://semver.org/).

Inoltre, questo progetto usa i *branch* e i *tag* di git nel seguente modo:
* il branch `master` contiene l'ultima versione stabile dello standard;
* il branch `development` contiene gli aggiornamenti proposti e in discussione
  per la prossima versione dello standard;
* La [release page](https://github.com/italia/publiccode.yml/releases) di
  GitHub contiene tutte le versioni rilasciate dello standard. Le *release*
  sono effettuate seguendo il nome del tag per questioni di coerenza.

Siccome questo repository contiene sia lo schema `core` che quelli contenenti
le estensioni per ogni paese, è necessario adottare una strategia di versioning
più raffinata. Per questo motivo, ogni update al core e/o ad un'estensione
specifica per Paese, sarà taggata come segue:

> core-x.y.z;cc-a.b.c

dove cc rappresenta il codice del paese presente nella chiave
`countryExtensionVersion` dello schema modificato. 

## Come contribuire 

Sentitevi liberi di aprire delle [Pull Requests e di presentare un problema
con una Issues](CONTRIBUTING.md).

## Autori
Le specifiche `publiccode.yml` sono sviluppate dal [Team per la Trasformazione
Digitale](https://teamdigitale.governo.it) e dagli [Autori](AUTHORS.md).

## Licenza

Il progetto è coperto da una licenza [CC-0](LICENSE).
