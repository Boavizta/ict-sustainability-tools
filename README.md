# 🗺️ Boavizta Green IT tools landscape

This project aims at providing a **vendor-neutral**, **fact-based**, **non-judgmental** and exhaustive inventory of the tools and services available to assess the environmental footprint of IT components.

> [!CAUTION]
> Today, data contained in this repository is not validated nor reviewed. It is likely that the data contains false assumptions. It is here as sample data for the sole purpose of development and testing of the model. It should NOT be used for any other purpose.

- [🗺️ Boavizta Green IT tools landscape](#️-boavizta-green-it-tools-landscape)
  - [Getting started 🚀: visualize the data](#getting-started--visualize-the-data)
  - [User manual](#user-manual)
  - [Technical details](#technical-details)
    - [Raw data (CSV)](#raw-data-csv)
    - [Data model](#data-model)
    - [Documentation](#documentation)
  - [Acknowledgments](#acknowledgments)
  - [Licenses](#licenses)

## Getting started 🚀: visualize the data

Visualize or edit the data set at [https://boavizta.github.io/ict-sustainability-tools/](https://boavizta.github.io/ict-sustainability-tools/)

## User manual

Check [how to use the tool](/doc/user-manual/how-to-use-the-tool.md).


## Technical details

### Raw data (CSV)

See the [CSV dataset](ictst/data/tools.csv)

### Data model

This repository proposes a common data model that is used to reference all the tools or services.

The [data model](ictst/model/tools.frictionless-table-schema.json) of the raw data CSV file is described using the [frictionless-table-schema](https://specs.frictionlessdata.io//table-schema/).

> [!WARNING]
> The data model is still very drafty and is expected to evolve.

### Documentation

See [/doc/technical-documentation.md](/doc/technical-documentation.md)

## Acknowledgments

We use a widget provided by [Datami](https://datami-docs.multi.coop/?locale=en) to display data and allow edition of a CSV file stored in Github. Thank you for your support.

## Licenses

- The content of this repository is licensed under [AGPLV3](/LICENSE)
- Datami components are licensed under AGPLV3: <https://gitlab.com/multi-coop/datami-project/datami/-/blob/main/LICENSE>
