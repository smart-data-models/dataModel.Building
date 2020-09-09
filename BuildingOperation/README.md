# BuildingOperation

## Description 

This entity contains a harmonised description of a generic operation (related to
smart buildings) applied to the referenced building. The building operation
contains dynamic data reported by, or associated with a building or operations
applicable to the building. This entity is associated with the vertical segments
of smart homes, smart cities, industry and related IoT applications.

This data model has been partially developed in cooperation with mobile
operators and the [GSMA](https://www.gsma.com/iot/iot-big-data/), compared to
GSMA data model the following changes are introduced:

-   `refRelatedDeviceOperation` replaces `refRelatedOperation`

  **Note**: JSON Schemas only capture the NGSI simplified representation, this
means that to test the JSON schema examples with a
[FIWARE NGSI version 2](http://fiware.github.io/specifications/ngsiv2/stable)
API implementation, you need to use the `keyValues` mode (`options=keyValues`).
  For a full description of the following attributes refer to GSMA
[IoT Big Data Harmonised Data Model](https://github.com/GSMADeveloper/NGSI-LD-Entities)

### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Building/BuildingOperation/swagger.yaml)

Link to the [specification](https://smart-data-models.github.io/dataModel.Building/BuildingOperation/doc/spec.md)
### Examples

Link to the [example](https://smart-data-models.github.io/dataModel.Building/BuildingOperation/examples/example.json) (keyvalues) for NGSI v2

Link to the [example](https://smart-data-models.github.io/dataModel.Building/BuildingOperation/examples/example-normalized.json) (normalized) for NGSI-V2

Link to the [example](https://smart-data-models.github.io/dataModel.Building/BuildingOperation/examples/example-normalized.jsonld) (normalized) for NGSI-LD
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.Building/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.Building/pulls)