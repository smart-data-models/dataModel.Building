Entität: Gebäude  
================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Building/blob/master/Building/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Informationen über ein bestimmtes Gebäude**  
Version: 0.0.2  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `category`: Kategorie des Gebäudes. Enum:Wohnungen, Backhaus, Scheune, Brücke, Bungalow, Bunker, Kathedrale, Hütte, Carport, Kapelle, Kirche, Gewerbehaus, Wintergarten, Bau, Kuhstall, freistehend, Faulbehälter, Schlafsaal, Bauernhof, Bauernhof_Hilfsgebäude, Garage, Garagen, Garagenschuppen, Tribüne, Gewächshaus, Hangar, Krankenhaus, Hotel, Haus, Hausboot, Hütte, Industrie, Kindergarten, Kiosk, Moschee, Büro, Parkplatz, Pavillon, öffentlich, Wohnhaus, Einzelhandel, Reithalle, Dach, Ruine, Schule, Service, Schuppen, Schrein, Stall, Stadion, Wohnwagen, Stall, Synagoge, Tempel, Terrasse, Bahnhof, Trafoturm, Transport, Universität, Lager, Wasserturm'  - `collapseRisk`: Wahrscheinlichkeit des vollständigen Einsturzes des Gebäudes.  - `containedInPlace`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `floorsAboveGround`: Stockwerke über dem Erdgeschoss  - `floorsBelowGround`: Stockwerke unterhalb des Erdgeschosses  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `occupier`: Person oder Organisation, die das Gebäude nutzt  - `openingHours`: Öffnungszeiten des Gebäudes.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `peopleCapacity`: Erlaubte Personen, die im Gebäude anwesend sind  - `peopleOccupancy`: Im Gebäude anwesende Personen  - `refMap`: Verweis auf die Karte, auf der das Gebäude verzeichnet ist  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type`: NGSI Entitätstyp    
Erforderliche Eigenschaften  
- `address`  - `category`  - `id`  - `type`    
Diese Entität enthält eine harmonisierte Beschreibung eines Gebäudes. Diese Entität ist mit den vertikalen Segmenten intelligente Häuser, intelligente Städte, Industrie und damit verbundene IoT-Anwendungen verbunden. Dieses Datenmodell wurde teilweise in Zusammenarbeit mit Mobilfunkbetreibern und der [GSMA] (https://www.gsma.com/iot/iot-big-data/) entwickelt. Im Vergleich zum GSMA-Datenmodell wurden folgende Änderungen vorgenommen Der Verweis auf das Attribut "BuildingType" wurde entfernt, da das Attribut "BuildingType" im Vergleich zum Attribut "Category" keine wichtigen Informationen enthält. Das Attribut "Kategorie" ist erforderlich. OpeningHours" wird in Anlehnung an das schema.org-Datenmodell eingeführt, um eine feinkörnige Angabe der Öffnungszeiten von Gebäuden zu ermöglichen. GSMA unterstützte dies als freien Text im Attribut `notes` (ebenfalls entfernt). refSubscriptionService" wird nicht unterstützt, da das Modell `SubscriptionService` derzeit nicht unterstützt wird.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Building:    
  description: 'Information on a given Building'    
  modelTags: ""    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      type: array    
      x-ngsi:    
        type: Property    
    collapseRisk:    
      description: 'Probability of total collapse of the building.'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    containedInPlace:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &building_-_properties_-_location_-_oneof    
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
      x-ngsi:    
        type: Geoproperty    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    floorsAboveGround:    
      description: 'Floors above the ground level'    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    floorsBelowGround:    
      description: 'Floors below the ground level'    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *building_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    occupier:    
      description: 'Person or entity using the building'    
      items:    
        oneOf:    
          - format: uri    
            type: string    
          - anyOf: *anyof    
            description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    openingHours:    
      description: 'Opening hours of this building.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHours    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    peopleCapacity:    
      description: 'Allowed people present at the building'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    peopleOccupancy:    
      description: 'People present at the building'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - Building    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - type    
    - id    
    - category    
    - address    
  type: object    
  version: 0.0.2    
```  
</details>    
## Beispiel-Nutzlasten  
#### Aufbau von NGSI-v2-Schlüsselwerten Beispiel  
Hier ist ein Beispiel für ein Gebäude im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "building-a85e3da145c1",  
  "type": "Building",  
  "dateCreated": "2016-08-08T10:18:16Z",  
  "dateModified": "2016-08-08T10:18:16Z",  
  "source": "http://www.example.com",  
  "dataProvider": "OperatorA",  
  "category": [  
    "office"  
  ],  
  "containedInPlace": {  
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
  },  
  "location": {  
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
  "occupier": [  
    "9830f692-7677-11e6-838b-4f9fb3dc5a4f"  
  ],  
  "floorsAboveGround": 7,  
  "floorsBelowGround": 0,  
  "description": "Office block",  
  "mapUrl": "http://www.example.com",  
  "openingHours": [  
    "Mo-Fr 10:00-19:00",  
    "Sa 10:00-22:00",  
    "Su 10:00-21:00"  
  ]  
}  
```  
#### Gebäude NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Gebäude im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "building-a85e3da145c1",  
  "type": "Building",  
  "category": {  
    "type": "Array",  
    "value": [  
      "office"  
    ]  
  },  
  "floorsBelowGround": {  
    "type": "Integer",  
    "value": 0  
  },  
  "description": {  
    "type": "Text",  
    "value": "Office block"  
  },  
  "floorsAboveGround": {  
    "type": "Integer",  
    "value": 7  
  },  
  "occupier": {  
    "type": "Relationship",  
    "value": [  
      "9830f692-7677-11e6-838b-4f9fb3dc5a4f"  
    ]  
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
    "type": "Text",  
    "value": "http://www.example.com"  
  },  
  "location": {  
    "type": "geo:json",  
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
    "type": "Array",  
    "value": [  
      "Mo-Fr 10:00-19:00",  
      "Sa 10:00-22:00",  
      "Su 10:00-21:00"  
    ]  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "OperatorA"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2016-08-08T10:18:16Z"  
  },  
  "containedInPlace": {  
    "type": "geo:json",  
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
  }  
}  
```  
#### Aufbau von NGSI-LD-Schlüsselwerten Beispiel  
Hier ist ein Beispiel für ein Gebäude im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Building:building-a85e3da145c1",  
  "type": "Building",  
  "modifiedAt": "2016-08-08T10:18:16Z",  
  "createdAt": "2016-08-08T10:18:16Z",  
  "category": "office",  
  "floorsBelowGround": 0,  
  "description": "Office block",  
  "floorsAboveGround": 7,  
  "occupier": [  
    "urn:ngsi-ld:Person:9830f692-7677-11e6-838b-4f9fb3dc5a4f"  
  ],  
  "mapUrl": "http://www.example.com",  
  "source": "http://www.example.com",  
  "location": {  
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
  },  
  "address": {  
    "addressLocality": "London",  
    "postalCode": "EC4N 8AF",  
    "streetAddress": "25 Walbrook",  
    "type": "PostalAddress"  
  },  
  "owner": [  
    "urn:ngsi-ld::cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
    "urn:ngsi-ld::1be9cd61-ef59-421f-a326-4b6c84411ad4"  
  ],  
  "openingHours": [  
    "Mo-Fr 10:00-19:00",  
    "Sa 10:00-22:00",  
    "Su 10:00-21:00"  
  ],  
  "dataProvider": "OperatorA",  
  "containedInPlace": {  
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
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Gebäude NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Gebäude im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Building:building-a85e3da145c1",  
  "type": "Building",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressLocality": "London",  
      "postalCode": "EC4N 8AF",  
      "streetAddress": "25 Walbrook",  
      "type": "PostalAddress"  
    }  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "office"  
    ]  
  },  
  "containedInPlace": {  
    "type": "Property",  
    "value": {  
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
    }  
  },  
  "createdAt": {  
    "type": "Property",  
    "value": "2016-08-08T10:18:16Z"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "OperatorA"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Office block"  
  },  
  "floorsAboveGround": {  
    "type": "Property",  
    "value": 7  
  },  
  "floorsBelowGround": {  
    "type": "Property",  
    "value": 0  
  },  
  "location": {  
    "type": "Geoproperty",  
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
  "mapUrl": {  
    "type": "Property",  
    "value": "http://www.example.com"  
  },  
  "modifiedAt": {  
    "type": "Property",  
    "value": "2016-08-08T10:18:16Z"  
  },  
  "occupier": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Person:9830f692-7677-11e6-838b-4f9fb3dc5a4f"  
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
  "owner": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld::cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "urn:ngsi-ld::1be9cd61-ef59-421f-a326-4b6c84411ad4"  
    ]  
  },  
  "source": {  
    "type": "Property",  
    "value": "http://www.example.com"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
