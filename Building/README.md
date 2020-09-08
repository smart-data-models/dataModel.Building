# Building

## Description 

This entity contains a harmonised description of a Building. This entity is associated with the vertical segments of smart homes, smart cities, industry and related IoT applications.
This data model has been partially developed in cooperation with mobile operators and the [GSMA](https://www.gsma.com/iot/iot-big-data/), compared to GSMA data model following changes are introduced:
  -   the reference to `BuildingType` is removed, since `BuildingType` compared to
    `category` attribute does not introduce significant information.

  -   `category` attribute is required.
  -   `openingHours` is introduced following schema.org data model to allow
    fine-grained on building opening times. GSMA supported this as free text in
    the `notes` attribute (removed as well).
  -   `refSubscriptionService` is not supported, since `SubscriptionService` model
    is not supported currently.
  - For a full description of the following attributes refer to GSMA [IoT Big Data Harmonised Data Model](https://github.com/GSMADeveloper/NGSI-LD-Entities)

### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Building/Building/swagger.yaml)

Link to the [specification](https://smart-data-models.github.io/dataModel.Building/Building/doc/spec.md)
### Examples

Link to the [example](https://smart-data-models.github.io/dataModel.Building/Building/examples/example.json) (keyvalues) for NGSI v2

Link to the [example](https://smart-data-models.github.io/dataModel.Building/Building/examples/example-normalized.json) (normalized) for NGSI-V2
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.Building/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.Building/pulls)