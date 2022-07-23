# SPID/CIE OIDC Technical Rules

[![GitHub release](https://img.shields.io/github/release/italia/spid-cie-oidc-docs.svg?style=plastic)](https://github.com/italia/spid-cie-oidc-docs/releases)
[![Join the #spid openid](https://img.shields.io/badge/Slack%20channel-%23spid%20openid-blue.svg)](https://developersitalia.slack.com/archives/C7E85ED1N/)
[![Get invited](https://slack.developers.italia.it/badge.svg)](https://slack.developers.italia.it/)
[![Docs Italia](https://docs.italia.it/media/static/projects/badges/passing.svg)](https://docs.italia.it/italia/spid-cie-oidc-docs/it/master/index.html)
[![Documentation](https://img.shields.io/badge/Documentation-Docs%20Italia-blue.svg)](https://docs.italia.it/italia/spid-cie-oidc-docs/it/master/index.html)

---

## Table of Contents

- [Description](#description)
- [Documentation](#documentation)
- [Versioning](#versioning)
- [Contributing](#how-to-contribute)
- [Authors](#authors)
- [License](#license)

## Documentation

This repository is structured to be compliant with [Docs Italia](https://docs.italia.it/italia/developers-italia/publiccodeyml/it/master/index.html).
This is why the content of the relevant folders will be compiled and rendered inside such patform.
`Docs Italia` is designed to support documents, localized in different languages and for this
reason it is the reference platform for displaying this standard.


## Developers

````
pip install -r requirements.txt

# italian version
sphinx-build -b html -d html/it/doctrees docs/it/  html/it

# english version
sphinx-build -b html -d html/en/doctrees docs/en/  html/en
````

## Versioning


This project participates in the versioning model  [*Semantic
Versioning*](https://semver.org/).

Furthermore, this project uses the git *branches* and *tags* in the following way:
* the branch `master` contains the last stable version of the standard;
* the branch `development` contains the proposed updates to be discussed in the next version of the standard;
* The [release page](https://github.com/italia/publiccode.yml/releases) of
  GitHub contains all the released versions of the standard. For the sake of coherence, the *releases* are made according to the tag names.

Since this repository contains both the `core` schema and the schemas with the extensions for each country,
a more refined versioning strategy must be adopted. For this reason, each update of the core and/or the specific country extensions, will be tagged as follows:

> core-x.y.z;cc-a.b.c

where cc represents the country code in the key `countryExtensionVersion` of the changed schema.

## How to contribute

Feel free to open [Pull Requests and to present a problem with an Issue](CONTRIBUTING.md).

## Authors

The `publiccode.yml` specifications are developed by the [Team per la Trasformazione
Digitale](https://teamdigitale.governo.it) and by the [Authors](AUTHORS.md).

## License

The project is covered by a [CC-0](LICENSE) license.
