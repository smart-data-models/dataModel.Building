# dataModel.Building
This folders contains a number of data models related to the modelling of Building and its management based on [GSMA](https://www.gsma.com/iot/iot-big-data/) activities.

### List of data models

The following entity types are available:
- [Building](https://github.com/smart-data-models/dataModel.Building/blob/master/Building/README.md). This entity contains a harmonised description of a Building. This entity is associated with the vertical segments of smart homes, smart cities, industry and related IoT applications.
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


- [BuildingOperation](https://github.com/smart-data-models/dataModel.Building/blob/master/BuildingOperation/README.md). This entity contains a harmonised description of a generic operation (related to
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




### Incubated data models
The list of incubated (on development) data models are:

[BuildingType_incubated](https://github.com/smart-data-models/dataModel.Building/tree/master/BuildingType_incubated)

[Floor_incubated](https://github.com/smart-data-models/dataModel.Building/tree/master/Floor_incubated)


### Contributors
[Link](https://github.com/smart-data-models/dataModel.Building/blob/master/CONTRIBUTORS.yaml) to the 3 current contributors of the data models of this Subject.


### Contribution
You can raise an [issue](https://github.com/smart-data-models/dataModel.Building/issues) or submit your [PR](https://github.com/smart-data-models/dataModel.Building/pulls) on existing data models


