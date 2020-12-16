Entidad: Edificio  
=================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Building/blob/master/Building/LICENSE.md)  
Descripción global: **Información sobre un edificio determinado**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `category`: Categoría del edificio. Enum:"Apartamentos, panadería, granero, puente, bungalow, búnker, catedral, cabaña, cochera, capilla, iglesia, local, comercial, conservatorio, construcción, establo, chalet, digestor, dormitorio, granja, granja auxiliar, garaje, garajes, cobertizo de basura, tribuna, invernadero, hangar, hospital, hotel, casa, casa flotante, cabaña, industrial, jardín de infantes, quiosco, mezquita, oficina, aparcamiento, pabellón, público, residencial, minorista, picadero, techo, ruinas, escuela, servicio, cobertizo, santuario, establo, estadio, caravana estática, pocilga, sinagoga, templo, terraza, estación de tren, torre de transformación, transporte, universidad, almacén, torre de agua'.  - `containedInPlace`:   - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `floorsAboveGround`: Pisos sobre el nivel del suelo  - `floorsBelowGround`: Pisos bajo el nivel del suelo  - `id`: Identificador único de la entidad  - `location`:   - `name`: El nombre de este artículo.  - `occupier`: La persona o entidad que utiliza el edificio  - `openingHours`: Horario de apertura de este edificio.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `refMap`: Referencia al mapa que contiene el edificio  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: NGSI Tipo de entidad    
Propiedades requeridas  
- `address`  - `category`  - `id`  - `type`    
Esta entidad contiene una descripción armonizada de un edificio. Esta entidad está asociada con los segmentos verticales de casas inteligentes, ciudades inteligentes, industria y aplicaciones de IO relacionadas. Este modelo de datos ha sido parcialmente desarrollado en cooperación con los operadores móviles y el [GSMA](https://www.gsma.com/iot/iot-big-data/), comparado con el modelo de datos del GSMA después de que se introduzcan cambios se elimina la referencia a "BuildingType", ya que el atributo "BuildingType" comparado con el de "categoría" no introduce información significativa. Se requiere el atributo "categórico". Se introduce "openHours" siguiendo el modelo de datos de schema.org para permitir un horario de apertura de los edificios. El GSMA apoyó esto como texto libre en el atributo "notas" (también eliminado). "RefSubscriptionService" no está soportado, ya que el modelo "SubscriptionService" no está soportado actualmente.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Building:    
  description: 'Information on a given Building'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
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
    containedInPlace:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: &building_-_properties_-_location_-_oneof    
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
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *building_-_properties_-_location_-_oneof    
      title: 'GeoJSON Geometry'    
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
            - format: uri    
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
## Ejemplo de cargas útiles  
#### Construyendo valores clave de NGSI V2 Ejemplo  
Aquí hay un ejemplo de un edificio en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### Construcción NGSI V2 normalizada Ejemplo  
Aquí hay un ejemplo de un edificio en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Construyendo valores clave NGSI-LD Ejemplo  
Aquí hay un ejemplo de un edificio en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressLocality": "London",  
             "postalCode": "EC4N 8AF",  
             "streetAddress": "25 Walbrook",  
             "type": "PostalAddress"},  
 "category": ["office"],  
 "containedInPlace": {"coordinates": [[[100, 0],  
                                       [101, 0],  
                                       [101, 1],  
                                       [100, 1],  
                                       [100, 0]]],  
                      "type": "Polygon"},  
 "createdAt": "2016-08-08T10:18:16Z",  
 "dataProvider": "OperatorA",  
 "description": "Office block",  
 "floorsAboveGround": 7,  
 "floorsBelowGround": 0,  
 "id": "urn:ngsi-ld:Building:building-a85e3da145c1",  
 "location": {"coordinates": [[[100, 0],  
                               [101, 0],  
                               [101, 1],  
                               [100, 1],  
                               [100, 0]]],  
              "type": "Polygon"},  
 "mapUrl": "http://www.example.com",  
 "modifiedAt": "2016-08-08T10:18:16Z",  
 "occupier": ["urn:ngsi-ld:Person:9830f692-7677-11e6-838b-4f9fb3dc5a4f"],  
 "openingHours": ["Mo-Fr 10:00-19:00", "Sa 10:00-22:00", "Su 10:00-21:00"],  
 "owner": ["urn:ngsi-ld::cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
           "urn:ngsi-ld::1be9cd61-ef59-421f-a326-4b6c84411ad4"],  
 "source": "http://www.example.com",  
 "type": "Building"}  
```  
#### Construcción NGSI-LD normalizada Ejemplo  
Aquí hay un ejemplo de un edificio en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
