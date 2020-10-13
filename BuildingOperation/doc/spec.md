# Building Operation

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

## Data Model

For a full description of the following attributes refer to GSMA
[IoT Big Data Harmonised Data Model](https://github.com/GSMADeveloper/NGSI-LD-Entities)

-   `id`

-   `type`: Entity type. It must be equal to `BuildingOperation`.`

-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Relationship. [Text](https://schema.org/Text) or
        [URL](https://schema.org/URL)
    -   Optional

-   `dataProvider` : Specifies the URL to information about the provider of this
    information

    -   Attribute type: Property. [URL](https://schema.org/URL)
    -   Optional

-   `description`

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References: `https://uri.etsi.org/ngsi-ld/description`
        equivalent to [description](https://schema.org/description)
    -   Optional

-   `refBuilding`

    -   Required

-   `refOperator`

    -   Required

-   `operationType`

    -   Optional

-   `result`

    -   Optional

-   `result`

    -   Optional

-   `operationSequence`

    -   Optional

-   `refRelatedBuildingOperation`
    -   Optional

These are the modified attributes compared to GSMA model:

-   `startDate` : The planned start date for the operation.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Required

-   `endDate` : The planned end date for the operation.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Required

-   `dateStarted` : The actual start date for the operation.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Optional

-   `dateFinished` : The actual end date for the operation.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Optional

-   `refRelatedDeviceOperation` : Devices related to the current operation.
    -   Attribute type: Relationship. A list of references to an entity of type
        Device.
