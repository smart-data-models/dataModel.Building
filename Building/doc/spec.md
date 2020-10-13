# Building

This entity contains a harmonised description of a Building. This entity is
associated with the vertical segments of smart homes, smart cities, industry and
related IoT applications.


This data model has been partially developed in cooperation with mobile
operators and the [GSMA](https://www.gsma.com/iot/iot-big-data/), compared to
GSMA data model following changes are introduced:

-   the reference to `BuildingType` is removed, since `BuildingType` compared to
    `category` attribute does not introduce significant information.

-   `category` attribute is required.

-   `openingHours` is introduced following schema.org data model to allow
    fine-grained on building opening times. GSMA supported this as free text in
    the `notes` attribute (removed as well).

-   `refSubscriptionService` is not supported, since `SubscriptionService` model
    is not supported currently.

## Data Model

For a full description of the following attributes refer to GSMA
[IoT Big Data Harmonised Data Model](https://github.com/GSMADeveloper/NGSI-LD-Entities)

-   `id`

-   `type`

-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Property. [Text](https://schema.org/Text) or
        [URL](https://schema.org/URL)
    -   Optional

-   `dataProvider` : Specifies the URL to information about the provider of this
    information

    -   Attribute type: Property. [URL](https://schema.org/URL)
    -   Optional

-   `dateModified` : Last update timestamp of this entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dateCreated` : Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `owner`

    -   Optional

-   `category`

    -   Required

-   `location`

    -   Attribute type: GeoProperty. `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Optional.

-   `containedInPlace`

    -   Optional.

-   `address`

    -   Attribute type: Property. [Address](https://schema.org/address)
    -   Normative References:
        [https://schema.org/address](https://schema.org/address)
    -   Required

-   `description`

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References: `https://uri.etsi.org/ngsi-ld/description`
        equivalent to [description](https://schema.org/description)
    -   Optional

-   `occupier`

    -   Optional

-   `floorsAboveGround`

    -   Optional

-   `floorsBelowGround`

    -   Optional

-   `refMap`
    -   Optional

The following attribute has been introduced:

-   `openingHours` : Opening hours of this building.
    -   Normative references:
        [https://schema.org/openingHours](https://schema.org/openingHours)
    -   Optional
