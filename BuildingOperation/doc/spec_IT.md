Entità: BuildingOperation  
=========================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Building/blob/master/BuildingOperation/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Informazioni su una data operazione di costruzione**  

## Elenco delle proprietà  

- `alternateName`: Un nome alternativo per questa voce  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateFinished`: La data di fine effettiva dell'operazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateStarted`: La data effettiva di inizio dell'operazione.  - `description`: Una descrizione di questo articolo  - `endDate`: La data di fine prevista per l'operazione.  - `id`: Identificatore unico dell'entità  - `name`: Il nome di questo articolo.  - `operationSequence`: Id della sequenza dell'operazione, se disponibile  - `operationType`: Tipo di operazione sull'edificio  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `refBuilding`: Riferimento dell'edificio in cui viene eseguita l'operazione.  - `refOperator`: Riferimento all'Operatore che fa l'operazione sull'edificio.  - `refRelatedBuildingOperation`: Riferimento ad altre operazioni di costruzione quando in sequenza  - `refRelatedDeviceOperation`: Dispositivi relativi all'operazione corrente. Un elenco di riferimenti a un'entità di tipo Dispositivo.  - `result`: Risultato dell'operazione di costruzione. Enum:'ok, abortito'.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `startDate`: La data di inizio prevista per l'operazione.  - `status`: Stato dell'operazione. Enum:'cancellato, finito, in corso, pianificato, programmato'.  - `type`: Deve essere BuildingOperation    
Proprietà richieste  
- `endDate`  - `id`  - `refBuilding`  - `startDate`  - `type`    
Questa entità contiene una descrizione armonizzata di un'operazione generica (relativa agli edifici intelligenti) applicata all'edificio di riferimento. L'operazione dell'edificio contiene dati dinamici riportati da, o associati con un edificio o operazioni applicabili all'edificio. Questa entità è associata ai segmenti verticali di case intelligenti, città intelligenti, industria e applicazioni IoT correlate. Questo modello di dati è stato parzialmente sviluppato in collaborazione con gli operatori mobili e il [GSMA](https://www.gsma.com/iot/iot-big-data/), rispetto al modello di dati GSMA vengono introdotte le seguenti modifiche - `refRelatedDeviceOperation` sostituisce `refRelatedOperation`.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BuildingOperation:    
  description: 'Information on a given Building Operation'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
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
    dateFinished:    
      description: 'The actual end date for the operation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateStarted:    
      description: 'The actual start date for the operation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    endDate:    
      description: 'The planned end date for the operation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    id:    
      anyOf: &buildingoperation_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operationSequence:    
      description: 'Id of the sequence of the operation when available'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    operationType:    
      description: 'Type of the operation on the building'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *buildingoperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refBuilding:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Building reference where the operation is performed.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    refOperator:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the Operator doing the operation on the building.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    refRelatedBuildingOperation:    
      description: 'Reference to other building operations when in sequence'    
      items:    
        anyOf: *buildingoperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Relationship    
    refRelatedDeviceOperation:    
      description: 'Devices related to the current operation. A list of references to an entity of type Device.'    
      items:    
        anyOf: *buildingoperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    result:    
      description: 'Result of the building operation. Enum:''ok, aborted'''    
      enum:    
        - ok    
        - aborted    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    startDate:    
      description: 'The planned start date for the operation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    status:    
      description: 'Status of the operation. Enum:''cancelled, finished, ongoing, planned, scheduled'' '    
      enum:    
        - cancelled    
        - finished    
        - ongoing    
        - planned    
        - scheduled    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'It has to be BuildingOperation'    
      enum:    
        - BuildingOperation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - type    
    - id    
    - refBuilding    
    - startDate    
    - endDate    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Building/blob/master/BuildingOperation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Building/BuildingOperation/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### Esempio di valori chiave NGSI-v2 di BuildingOperation  
Ecco un esempio di una BuildingOperation in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "type": "BuildingOperation",  
  "dateCreated": "2016-08-08T10:18:16Z",  
  "dateModified": "2016-08-08T10:18:16Z",  
  "source": "http://www.example.com",  
  "dataProvider": "OperatorA",  
  "refBuilding": "building-a85e3da145c1",  
  "operationType": "airConditioning",  
  "description": "Air conditioning levels reduced due to out of hours",  
  "result": "ok",  
  "startDate": "2016-08-08T10:18:16Z",  
  "endDate": "2016-08-20T10:18:16Z",  
  "dateStarted": "2016-08-08T10:18:16Z",  
  "dateFinished": "2016-08-20T10:18:16Z",  
  "status": "finished",  
  "operationSequence": ["fan_power%3D0", "set_temperature%3D24"],  
  "refRelatedBuildingOperation": [  
    "b4fb8bff-1a8f-455f-8cc0-ca43c069f865",  
    "55c24793-3437-4157-9bda-667c9e1531fc"  
  ],  
  "refRelatedDeviceOperation": [  
    "36744245-6716-4a28-84c7-0e3d7520f143",  
    "33b2b713-9223-40a5-87a0-3f80a1264a6c"  
  ]  
}  
```  
#### BuildingOperation NGSI-v2 normalizzato Esempio  
Ecco un esempio di una BuildingOperation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "type": "BuildingOperation",  
  "status": {  
    "value": "finished"  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "2016-08-08T10:18:16Z"  
  },  
  "operationSequence": {  
    "value": ["fan_power%3D0", "set_temperature%3D24"]  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2016-08-20T10:18:16Z"  
  },  
  "description": {  
    "value": "Air conditioning levels reduced due to out of hours"  
  },  
  "refRelatedDeviceOperation": {  
    "type": "Relationship",  
    "value": [  
      "36744245-6716-4a28-84c7-0e3d7520f143",  
      "33b2b713-9223-40a5-87a0-3f80a1264a6c"  
    ]  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2016-08-08T10:18:16Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2016-08-08T10:18:16Z"  
  },  
  "refRelatedBuildingOperation": {  
    "type": "Relationship",  
    "value": [  
      "b4fb8bff-1a8f-455f-8cc0-ca43c069f865",  
      "55c24793-3437-4157-9bda-667c9e1531fc"  
    ]  
  },  
  "source": {  
    "value": "http://www.example.com"  
  },  
  "refBuilding": {  
    "type": "Relationship",  
    "value": "building-a85e3da145c1"  
  },  
  "result": {  
    "value": "ok"  
  },  
  "operationType": {  
    "value": "airConditioning"  
  },  
  "dateStarted": {  
    "type": "DateTime",  
    "value": "2016-08-08T10:18:16Z"  
  },  
  "dateFinished": {  
    "type": "DateTime",  
    "value": "2016-08-20T10:18:16Z"  
  },  
  "dataProvider": {  
    "value": "OperatorA"  
  }  
}  
```  
#### CostruireOperazione NGSI-LD valori-chiave Esempio  
Ecco un esempio di una BuildingOperation in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:BuildingOperation:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "type": "BuildingOperation",  
  "modifiedAt": "2016-08-08T10:18:16Z",  
  "createdAt": "2016-08-08T10:18:16Z",  
  "status": {  
    "type": "Property",  
    "value": "finished"  
  },  
  "startDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-08T10:18:16Z"  
    }  
  },  
  "operationSequence": {  
    "type": "Property",  
    "value": [  
      "fan_power%3D0",  
      "set_temperature%3D24"  
    ]  
  },  
  "endDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-20T10:18:16Z"  
    }  
  },  
  "description": {  
    "type": "Property",  
    "value": "Air conditioning levels reduced due to out of hours"  
  },  
  "refRelatedDeviceOperation": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:DeviceOperation:36744245-6716-4a28-84c7-0e3d7520f143",  
      "urn:ngsi-ld:DeviceOperation:33b2b713-9223-40a5-87a0-3f80a1264a6c"  
    ]  
  },  
  "refRelatedBuildingOperation": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:BuildingOperation:b4fb8bff-1a8f-455f-8cc0-ca43c069f865",  
      "urn:ngsi-ld:BuildingOperation:55c24793-3437-4157-9bda-667c9e1531fc"  
    ]  
  },  
  "source": {  
    "type": "Property",  
    "value": "http://www.example.com"  
  },  
  "refBuilding": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Building:building-a85e3da145c1"  
  },  
  "result": {  
    "type": "Property",  
    "value": "ok"  
  },  
  "operationType": {  
    "type": "Property",  
    "value": "airConditioning"  
  },  
  "dateStarted": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-08T10:18:16Z"  
    }  
  },  
  "dateFinished": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-20T10:18:16Z"  
    }  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "OperatorA"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### BuildingOperation NGSI-LD normalizzato Esempio  
Ecco un esempio di una BuildingOperation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "createdAt": "2016-08-08T10:18:16Z",  
  "dataProvider": "OperatorA",  
  "dateFinished": {  
    "@type": "DateTime",  
    "@value": "2016-08-20T10:18:16Z"  
  },  
  "dateStarted": {  
    "@type": "DateTime",  
    "@value": "2016-08-08T10:18:16Z"  
  },  
  "description": "Air conditioning levels reduced due to out of hours",  
  "endDate": {  
    "@type": "DateTime",  
    "@value": "2016-08-20T10:18:16Z"  
  },  
  "id": "urn:ngsi-ld:BuildingOperation:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "modifiedAt": "2016-08-08T10:18:16Z",  
  "operationSequence": [  
    "fan_power%3D0",  
    "set_temperature%3D24"  
  ],  
  "operationType": "airConditioning",  
  "refBuilding": "urn:ngsi-ld:Building:building-a85e3da145c1",  
  "refRelatedBuildingOperation": [  
    "urn:ngsi-ld:BuildingOperation:b4fb8bff-1a8f-455f-8cc0-ca43c069f865",  
    "urn:ngsi-ld:BuildingOperation:55c24793-3437-4157-9bda-667c9e1531fc"  
  ],  
  "refRelatedDeviceOperation": [  
    "urn:ngsi-ld:DeviceOperation:36744245-6716-4a28-84c7-0e3d7520f143",  
    "urn:ngsi-ld:DeviceOperation:33b2b713-9223-40a5-87a0-3f80a1264a6c"  
  ],  
  "result": "ok",  
  "source": "http://www.example.com",  
  "startDate": {  
    "@type": "DateTime",  
    "@value": "2016-08-08T10:18:16Z"  
  },  
  "status": "finished",  
  "type": "BuildingOperation"  
}  
```  
