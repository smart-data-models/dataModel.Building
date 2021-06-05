Entity: Building  
================  
[Open License](https://github.com/smart-data-models//dataModel.Building/blob/master/Building/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **Information on a given Building**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `category`: Category of the building. Enum:'apartments, bakehouse, barn, bridge, bungalow, bunker, cathedral, cabin, carport, chapel, church, civic, commercial, conservatory, construction, cowshed, detached, digester, dormitory, farm, farm_auxiliary, garage, garages, garbage_shed, grandstand, greenhouse, hangar, hospital, hotel, house, houseboat, hut, industrial, kindergarten, kiosk, mosque, office, parking, pavilion, public, residential, retail, riding_hall, roof, ruins, school, service, shed, shrine, stable, stadium, static_caravan, sty, synagogue, temple, terrace, train_station, transformer_tower, transportation, university, warehouse, water_tower'  - `collapseRisk`: Probability of total collapse of the building.  - `containedInPlace`:   - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `floorsAboveGround`: Floors above the ground level  - `floorsBelowGround`: Floors below the ground level  - `id`: Unique identifier of the entity  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `occupier`: Person or entity using the building  - `openingHours`: Opening hours of this building.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `peopleCapacity`: Allowed people present at the building  - `peopleOccupancy`: People present at the building  - `refMap`: Reference to the map containing the building  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity type    
Required properties  
- `address`  - `category`  - `id`  - `type`    
This entity contains a harmonised description of a Building. This entity is associated with the vertical segments of smart homes, smart cities, industry and related IoT applications. This data model has been partially developed in cooperation with mobile operators and the [GSMA](https://www.gsma.com/iot/iot-big-data/), compared to GSMA data model following changes are introduced the reference to `BuildingType` is removed, since `BuildingType` compared to `category` attribute does not introduce significant information. `category` attribute is required. `openingHours` is introduced following schema.org data model to allow fine-grained on building opening times. GSMA supported this as free text in the `notes` attribute (removed as well). `refSubscriptionService` is not supported, since `SubscriptionService` model is not supported currently  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Building:    
  description: 'Information on a given Building'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    category:    
      description: 'Category of the building. Enum:''apartments, bakehouse, barn, bridge, bungalow, bunker, cathedral, cabin, carport, chapel, church, civic, commercial, conservatory, construction, cowshed, detached, digester, dormitory, farm, farm_auxiliary, garage, garages, garbage_shed, grandstand, greenhouse, hangar, hospital, hotel, house, houseboat, hut, industrial, kindergarten, kiosk, mosque, office, parking, pavilion, public, residential, retail, riding_hall, roof, ruins, school, service, shed, shrine, stable, stadium, static_caravan, sty, synagogue, temple, terrace, train_station, transformer_tower, transportation, university, warehouse, water_tower'''    
      items:    
        enum:    
          - apartments    
          - bakehouse    
          - barn    
          - bridge    
          - bungalow    
          - bunker    
          - cathedral    
          - cabin    
          - carport    
          - chapel    
          - church    
          - civic    
          - commercial    
          - conservatory    
          - construction    
          - cowshed    
          - detached    
          - digester    
          - dormitory    
          - farm    
          - farm_auxiliary    
          - garage    
          - garages    
          - garbage_shed    
          - grandstand    
          - greenhouse    
          - hangar    
          - hospital    
          - hotel    
          - house    
          - houseboat    
          - hut    
          - industrial    
          - kindergarten    
          - kiosk    
          - mosque    
          - office    
          - parking    
          - pavilion    
          - public    
          - residential    
          - retail    
          - riding_hall    
          - roof    
          - ruins    
          - school    
          - service    
          - shed    
          - shrine    
          - stable    
          - stadium    
          - static_caravan    
          - sty    
          - synagogue    
          - temple    
          - terrace    
          - train_station    
          - transformer_tower    
          - transportation    
          - university    
          - warehouse    
          - water_tower    
        type: string    
      type: Property    
    collapseRisk:    
      description: 'Probability of total collapse of the building.'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    containedInPlace:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    floorsAboveGround:    
      description: 'Floors above the ground level'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    floorsBelowGround:    
      description: 'Floors below the ground level'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    occupier:    
      description: 'Person or entity using the building'    
      items:    
        oneOf:    
          - format: uri    
            type: string    
          - anyOf: *anyof    
            description: 'Property. Unique identifier of the entity'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    openingHours:    
      description: 'Opening hours of this building.'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/openingHours    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    peopleCapacity:    
      description: 'Allowed people present at the building'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    peopleOccupancy:    
      description: 'People present at the building'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    refMap:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the map containing the building'    
      type: Relationship    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - Building    
      type: Property    
  required:    
    - type    
    - id    
    - category    
    - address    
  type: object    
```  
</details>    
## Example payloads    
#### Building NGSI-v2 key-values Example    
Here is an example of a Building in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "building-a85e3da145c1",  
  "type": "Building",  
  "dateCreated": "2016-08-08T10:18:16Z",  
  "dateModified": "2016-08-08T10:18:16Z",  
  "source": "http://www.example.com",  
  "dataProvider": "OperatorA",  
  "category": ["office"],  
  "containedInPlace": {  
    "type": "Polygon",  
    "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]  
  },  
  "location": {  
    "type": "Polygon",  
    "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]  
  },  
  "address": {  
    "addressLocality": "London",  
    "postalCode": "EC4N 8AF",  
    "streetAddress": "25 Walbrook"  
  },  
  "owner": [  
    "cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
    "1be9cd61-ef59-421f-a326-4b6c84411ad4"  
  ],  
  "occupier": ["9830f692-7677-11e6-838b-4f9fb3dc5a4f"],  
  "floorsAboveGround": 7,  
  "floorsBelowGround": 0,  
  "description": "Office block",  
  "mapUrl": "http://www.example.com",  
  "openingHours": ["Mo-Fr 10:00-19:00", "Sa 10:00-22:00", "Su 10:00-21:00"]  
}  
```  
#### Building NGSI-v2 normalized Example    
Here is an example of a Building in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "building-a85e3da145c1",  
  "type": "Building",  
  "category": {  
    "value": ["office"]  
  },  
  "floorsBelowGround": {  
    "value": 0  
  },  
  "description": {  
    "value": "Office block"  
  },  
  "floorsAboveGround": {  
    "value": 7  
  },  
  "occupier": {  
    "type": "Relationship",  
    "value": ["9830f692-7677-11e6-838b-4f9fb3dc5a4f"]  
  },  
  "mapUrl": {  
    "type": "URL",  
    "value": "http://www.example.com"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2016-08-08T10:18:16Z"  
  },  
  "source": {  
    "value": "http://www.example.com"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "London",  
      "postalCode": "EC4N 8AF",  
      "streetAddress": "25 Walbrook"  
    }  
  },  
  "owner": {  
    "type": "Relationship",  
    "value": [  
      "cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "1be9cd61-ef59-421f-a326-4b6c84411ad4"  
    ]  
  },  
  "openingHours": {  
    "value": ["Mo-Fr 10:00-19:00", "Sa 10:00-22:00", "Su 10:00-21:00"]  
  },  
  "dataProvider": {  
    "value": "OperatorA"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2016-08-08T10:18:16Z"  
  },  
  "containedInPlace": {  
    "value": {  
      "type": "Polygon",  
      "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]  
    }  
  }  
}  
```  
#### Building NGSI-LD key-values Example    
Here is an example of a Building in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Building:building-a85e3da145c1",  
  "type": "Building",  
  "modifiedAt": "2016-08-08T10:18:16Z",  
  "createdAt": "2016-08-08T10:18:16Z",  
  "category": {  
    "type": "Property",  
    "value": [  
      "office"  
    ]  
  },  
  "floorsBelowGround": {  
    "type": "Property",  
    "value": 0  
  },  
  "description": {  
    "type": "Property",  
    "value": "Office block"  
  },  
  "floorsAboveGround": {  
    "type": "Property",  
    "value": 7  
  },  
  "occupier": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Person:9830f692-7677-11e6-838b-4f9fb3dc5a4f"  
    ]  
  },  
  "mapUrl": {  
    "type": "Property",  
    "value": "http://www.example.com"  
  },  
  "source": {  
    "type": "Property",  
    "value": "http://www.example.com"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            100,  
            0  
          ],  
          [  
            101,  
            0  
          ],  
          [  
            101,  
            1  
          ],  
          [  
            100,  
            1  
          ],  
          [  
            100,  
            0  
          ]  
        ]  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressLocality": "London",  
      "postalCode": "EC4N 8AF",  
      "streetAddress": "25 Walbrook",  
      "type": "PostalAddress"  
    }  
  },  
  "owner": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld::cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "urn:ngsi-ld::1be9cd61-ef59-421f-a326-4b6c84411ad4"  
    ]  
  },  
  "openingHours": {  
    "type": "Property",  
    "value": [  
      "Mo-Fr 10:00-19:00",  
      "Sa 10:00-22:00",  
      "Su 10:00-21:00"  
    ]  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "OperatorA"  
  },  
  "containedInPlace": {  
    "type": "Property",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            100,  
            0  
          ],  
          [  
            101,  
            0  
          ],  
          [  
            101,  
            1  
          ],  
          [  
            100,  
            1  
          ],  
          [  
            100,  
            0  
          ]  
        ]  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Building NGSI-LD normalized Example    
Here is an example of a Building in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "address": {  
    "addressLocality": "London",  
    "postalCode": "EC4N 8AF",  
    "streetAddress": "25 Walbrook",  
    "type": "PostalAddress"  
  },  
  "category": [  
    "office"  
  ],  
  "containedInPlace": {  
    "coordinates": [  
      [  
        [  
          100,  
          0  
        ],  
        [  
          101,  
          0  
        ],  
        [  
          101,  
          1  
        ],  
        [  
          100,  
          1  
        ],  
        [  
          100,  
          0  
        ]  
      ]  
    ],  
    "type": "Polygon"  
  },  
  "createdAt": "2016-08-08T10:18:16Z",  
  "dataProvider": "OperatorA",  
  "description": "Office block",  
  "floorsAboveGround": 7,  
  "floorsBelowGround": 0,  
  "id": "urn:ngsi-ld:Building:building-a85e3da145c1",  
  "location": {  
    "coordinates": [  
      [  
        [  
          100,  
          0  
        ],  
        [  
          101,  
          0  
        ],  
        [  
          101,  
          1  
        ],  
        [  
          100,  
          1  
        ],  
        [  
          100,  
          0  
        ]  
      ]  
    ],  
    "type": "Polygon"  
  },  
  "mapUrl": "http://www.example.com",  
  "modifiedAt": "2016-08-08T10:18:16Z",  
  "occupier": [  
    "urn:ngsi-ld:Person:9830f692-7677-11e6-838b-4f9fb3dc5a4f"  
  ],  
  "openingHours": [  
    "Mo-Fr 10:00-19:00",  
    "Sa 10:00-22:00",  
    "Su 10:00-21:00"  
  ],  
  "owner": [  
    "urn:ngsi-ld::cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
    "urn:ngsi-ld::1be9cd61-ef59-421f-a326-4b6c84411ad4"  
  ],  
  "source": "http://www.example.com",  
  "type": "Building"  
}  
```  
