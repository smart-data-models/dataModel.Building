<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Edificio  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Building/blob/master/Building/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Informazioni su un determinato edificio**  
versione: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: Categoria dell'edificio. Enum:'appartamenti, forno, fienile, ponte, bungalow, bunker, cattedrale, cabina, tettoia, cappella, chiesa, civico, commerciale, serra, costruzione, stalla, staccata, digestore, dormitorio, fattoria, fattoria_ausiliaria, garage, garbage_shed, tribuna, serra, hangar, ospedale, hotel, casa, casa galleggiante, capanna, industriale, asilo, chiosco, moschea, ufficio, parcheggio, padiglione, pubblico, residenziale, vendita al dettaglio, maneggio, tetto, rovine, scuola, servizio, capannone, santuario, scuderia, stadio, roulotte_statica, stalla, sinagoga, tempio, terrazza, stazione ferroviaria, torre_di_trasformazione, trasporto, università, magazzino, torre_d'acqua".  - `collapseRisk[number]`: Probabilità di crollo totale dell'edificio.  . Model: [https://schema.org/Number](https://schema.org/Number)- `containedInPlace[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `floorsAboveGround[integer]`: Piani sopra il livello del suolo  . Model: [https://schema.org/Number](https://schema.org/Number)- `floorsBelowGround[integer]`: Piani sotto il livello del suolo  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `occupier[array]`: Persona o ente che utilizza l'edificio  . Model: [https://schema.org/URL](https://schema.org/URL)- `openingHours[array]`: Orari di apertura di questo edificio.  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `peopleCapacity[number]`: Persone ammesse presenti nell'edificio  . Model: [https://schema.org/Number](https://schema.org/Number)- `peopleOccupancy[number]`: Persone presenti nell'edificio  . Model: [https://schema.org/Number](https://schema.org/Number)- `refMap[*]`: Riferimento alla mappa contenente l'edificio  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: NGSI Tipo di entità  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `address`  - `category`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Questa entità contiene una descrizione armonizzata di un edificio. Questa entità è associata ai segmenti verticali delle case intelligenti, delle città intelligenti, dell'industria e delle relative applicazioni IoT. Questo modello di dati è stato parzialmente sviluppato in collaborazione con gli operatori di telefonia mobile e con il [GSMA] (https://www.gsma.com/iot/iot-big-data/); rispetto al modello di dati GSMA sono state introdotte le seguenti modifiche il riferimento a `BuildingType` è stato rimosso, poiché l'attributo `BuildingType` rispetto a `category` non introduce informazioni significative. L'attributo `categoria` è obbligatorio. L'attributo `openingHours` è stato introdotto secondo il modello di dati di schema.org per consentire un'analisi fine degli orari di apertura degli edifici. Il GSMA lo sosteneva come testo libero nell'attributo `notes` (anch'esso rimosso). `refSubscriptionService` non è supportato, poiché il modello `SubscriptionService` non è attualmente supportato.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Building/blob/master/Building/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Building/Building/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Esempio di costruzione di valori-chiave NGSI-v2  
Ecco un esempio di edificio in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Esempio di costruzione di NGSI-v2 normalizzato  
Ecco un esempio di Edificio in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Esempio di costruzione di valori-chiave NGSI-LD  
Ecco un esempio di edificio in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Building:building-a85e3da145c1",  
    "type": "Building",  
    "address": {  
        "addressLocality": "London",  
        "postalCode": "EC4N 8AF",  
        "streetAddress": "25 Walbrook",  
        "type": "PostalAddress"  
    },  
    "category": "office",  
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
    "createdAt": "2016-08-08T10:18:16Z",  
    "dataProvider": "OperatorA",  
    "description": "Office block",  
    "floorsAboveGround": 7,  
    "floorsBelowGround": 0,  
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
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Building/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Esempio di edificio NGSI-LD normalizzato  
Ecco un esempio di Edificio in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Building/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
