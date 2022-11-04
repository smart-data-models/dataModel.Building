<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: EdificioTipo  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Building/blob/master/BuildingType/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di un tipo generico di edificio. Questa entità è associata ai segmenti verticali di casa intelligente, città intelligenti, industria e applicazioni IoT correlate. Il tipo di edificio comprende una struttura gerarchica che consente di raggruppare i tipi di edificio in modo flessibile **.  
versione: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `buildingTypeChildren[array]`: Riferimento ai tipi di edificio figli, cioè immediatamente sotto questa entità nella gerarchia.  - `buildingTypeParent[*]`: Riferisce qualsiasi entità di tipo edificio di livello superiore su cui si basa questo tipo.  - `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `root[boolean]`: Un indicatore logico che indica che questa è la radice di una gerarchia di BuildingType. True indica che è la radice, false indica che non è la radice.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Identificatore dell'entità NGSI. Deve essere BuildingType  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Questo modello di dati deriva dal progetto originale GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Sono stati apportati alcuni piccoli adattamenti per soddisfare i requisiti dei modelli di dati intelligenti.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BuildingType:    
  description: 'This entity contains a harmonised description of a generic building type. This entity is associated with the vertical segments of smart home, smart cities, industry and related IoT applications. The building type includes a hierarchical structure that allows building types to be grouped in a flexible way.'    
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
    buildingTypeChildren:    
      description: 'Reference to child building types i.e. immediately below this entity in the hierarchy.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    buildingTypeParent:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'References any higher level Building Type entities that this type is based on.'    
      x-ngsi:    
        type: Relationship    
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
    id:    
      anyOf: &buildingtype_-_properties_-_owner_-_items_-_anyof    
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
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *buildingtype_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    root:    
      description: 'A logical indicator that this is the root of a BuildingType hierarchy.True indicates it is the root, false indicates that it is not the root.'    
      type: boolean    
      x-ngsi:    
        type: Property    
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
      description: 'NGSI Entity identifier. It has to be BuildingType'    
      enum:    
        - BuildingType    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Building/blob/master/BuildingType/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Building/BuildingType/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### BuildingType Valori-chiave NGSI-v2 Esempio  
Ecco un esempio di BuildingType in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:BuildingType:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "type": "BuildingType",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "name": "House",  
  "description": "Standard building type definition for a domestic house",  
  "root": false,  
  "buildingTypeParent": "urn:ngsi-ld:BuildingType:4146335f-839f-4ff9-a575-6b4e6232b734",  
  "buildingTypeChildren": [  
    "urn:ngsi-ld:BuildingType:e4291e84-58f8-11e8-84c3-77e4f1f8c4f1",  
    "urn:ngsi-ld:BuildingType:a71c7a08-58f9-11e8-a41e-4bcb7249360e",  
    "urn:ngsi-ld:BuildingType:afac9bbc-58f9-11e8-b587-1f0d57b81bb4"  
  ]  
}  
```  
</details>  
#### BuildingType NGSI-v2 normalizzato Esempio  
Ecco un esempio di BuildingType in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:BuildingType:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "type": "BuildingType",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "name": {  
    "type": "Text",  
    "value": "House"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Standard building type definition for a domestic house"  
  },  
  "root": {  
    "type": "Boolean",  
    "value": false  
  },  
  "buildingTypeParent": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingType:4146335f-839f-4ff9-a575-6b4e6232b734"  
  },  
  "buildingTypeChildren": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:BuildingType:e4291e84-58f8-11e8-84c3-77e4f1f8c4f1",  
      "urn:ngsi-ld:BuildingType:a71c7a08-58f9-11e8-a41e-4bcb7249360e",  
      "urn:ngsi-ld:BuildingType:afac9bbc-58f9-11e8-b587-1f0d57b81bb4"  
    ]  
  }  
}  
```  
</details>  
#### BuildingType Valori chiave NGSI-LD Esempio  
Ecco un esempio di BuildingType in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:BuildingType:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
    "type": "BuildingType",  
    "buildingTypeChildren": [  
        "urn:ngsi-ld:BuildingType:e4291e84-58f8-11e8-84c3-77e4f1f8c4f1",  
        "urn:ngsi-ld:BuildingType:a71c7a08-58f9-11e8-a41e-4bcb7249360e",  
        "urn:ngsi-ld:BuildingType:afac9bbc-58f9-11e8-b587-1f0d57b81bb4"  
    ],  
    "buildingTypeParent": "urn:ngsi-ld:BuildingType:4146335f-839f-4ff9-a575-6b4e6232b734",  
    "dataProvider": "https://provider.example.com",  
    "description": "Standard building type definition for a domestic house",  
    "name": "House",  
    "root": false,  
    "source": "https://source.example.com",  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Building/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Building/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### BuildingType NGSI-LD normalizzato Esempio  
Ecco un esempio di BuildingType in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:BuildingType:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
    "type": "BuildingType",  
    "buildingTypeChildren": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:BuildingType:e4291e84-58f8-11e8-84c3-77e4f1f8c4f1",  
            "urn:ngsi-ld:BuildingType:a71c7a08-58f9-11e8-a41e-4bcb7249360e",  
            "urn:ngsi-ld:BuildingType:afac9bbc-58f9-11e8-b587-1f0d57b81bb4"  
        ]  
    },  
    "buildingTypeParent": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:BuildingType:4146335f-839f-4ff9-a575-6b4e6232b734"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://provider.example.com"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Standard building type definition for a domestic house"  
    },  
    "name": {  
        "type": "Property",  
        "value": "House"  
    },  
    "root": {  
        "type": "Property",  
        "value": false  
    },  
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Building/context.jsonld",  
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
