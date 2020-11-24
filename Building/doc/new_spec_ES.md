Entidad: Edificio  
=================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Información sobre un edificio determinado**  

## Lista de propiedades  

`address`: La dirección postal.  `alternateName`: Un nombre alternativo para este artículo  `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  `category`:   `containedInPlace`:   `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `description`: Una descripción de este artículo  `floorsAboveGround`: Pisos sobre el nivel del suelo  `floorsBelowGround`: Pisos bajo el nivel del suelo  `id`:   `location`:   `name`: El nombre de este artículo.  `occupier`:   `openingHours`: Horario de apertura de este edificio.  `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  `refMap`: Relación. Referencia al mapa que contiene el edificio  `seeAlso`:   `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  `type`: NGSI Tipo de entidad    
Esta entidad contiene una descripción armonizada de un edificio. Esta entidad está asociada con los segmentos verticales de casas inteligentes, ciudades inteligentes, industria y aplicaciones de IO relacionadas. Este modelo de datos ha sido parcialmente desarrollado en cooperación con los operadores móviles y el [GSMA](https://www.gsma.com/iot/iot-big-data/), comparado con el modelo de datos del GSMA después de que se introduzcan cambios se elimina la referencia a "BuildingType", ya que el atributo "BuildingType" comparado con el de "categoría" no introduce información significativa. Se requiere el atributo "categórico". Se introduce "openHours" siguiendo el modelo de datos de schema.org para permitir un horario de apertura de los edificios. El GSMA apoyó esto como texto libre en el atributo "notas" (también eliminado). "RefSubscriptionService" no está soportado, ya que el modelo "SubscriptionService" no está soportado actualmente.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
Building:    
  description: 'Information on a given Building'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    category:    
      description: ""    
      items:    
        enum:    
          - apartments    
          - farm    
          - hotel    
          - house    
          - detached    
          - residential    
          - dormitory    
          - terrace    
          - houseboat    
          - bungalow    
          - static_caravan    
          - commercial    
          - office    
          - industrial    
          - retail    
          - warehouse    
          - kiosk    
          - bakehouse    
          - cathedral    
          - chapel    
          - church    
          - kindergarten    
          - mosque    
          - temple    
          - synagogue    
          - shrine    
          - civic    
          - hospital    
          - school    
          - stadium    
          - train_station    
          - transportation    
          - university    
          - grandstand    
          - public    
          - barn    
          - bridge    
          - bunker    
          - cabin    
          - carport    
          - conservatory    
          - construction    
          - cowshed    
          - digester    
          - farm_auxiliary    
          - garage    
          - garages    
          - garbage_shed    
          - greenhouse    
          - hangar    
          - hut    
          - pavilion    
          - parking    
          - riding_hall    
          - roof    
          - shed    
          - stable    
          - sty    
          - transformer_tower    
          - service    
          - ruins    
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
    floorsBelowGround:    
      description: 'Floors below the ground level'    
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
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *building_-_properties_-_location_-_oneof    
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    occupier:    
      description: ""    
      items:    
        oneOf:    
          - format: uri    
            type: string    
          - anyOf: *anyof    
      type: Property    
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
      type: Property    
    refMap:    
      description: 'Relationship. Reference to the map containing the building'    
      format: uri    
      type: string    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
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
Aquí hay un ejemplo de un edificio en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores clave" y devuelve los datos de contexto de una entidad individual.  
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
Aquí hay un ejemplo de un edificio en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
