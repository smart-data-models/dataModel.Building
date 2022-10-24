<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: EdificioOperazione  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Building/blob/master/BuildingOperation/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Informazioni su una determinata operazione edilizia**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `alternateName[string]`: Un nome alternativo per questa voce  - `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateFinished[string]`: La data di fine effettiva dell'operazione.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateStarted[string]`: La data di inizio effettivo dell'operazione.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Descrizione dell'articolo  - `endDate[string]`: La data di fine prevista per l'operazione.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `id[*]`: Identificatore univoco dell'entità  - `name[string]`: Il nome di questo elemento.  - `operationSequence[array]`: Id della sequenza dell'operazione, se disponibile  . Model: [https://schema.org/Text](https://schema.org/Text)- `operationType[string]`: Tipo di intervento sull'edificio  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `refBuilding[*]`: Riferimento all'edificio in cui viene eseguita l'operazione.  . Model: [https://schema.org/URL](https://schema.org/URL)- `refOperator[*]`: Riferimento all'Operatore che esegue l'operazione sull'edificio.  . Model: [https://schema.org/URL](https://schema.org/URL)- `refRelatedBuildingOperation[array]`: Riferimento ad altre operazioni edilizie in sequenza  - `refRelatedDeviceOperation[array]`: Dispositivi relativi all'operazione corrente. Un elenco di riferimenti a un'entità di tipo Dispositivo.  . Model: [https://schema.org/URL](https://schema.org/URL)- `result[string]`: Risultato dell'operazione di costruzione. Enum:'ok, interrotta'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `startDate[string]`: La data di inizio prevista per l'operazione.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `status[string]`: Stato dell'operazione. Enum:'annullata, terminata, in corso, pianificata, programmata'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Deve essere BuildingOperation  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `endDate`  - `id`  - `refBuilding`  - `startDate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Questa entità contiene una descrizione armonizzata di un'operazione generica (relativa agli edifici intelligenti) applicata all'edificio di riferimento. L'operazione dell'edificio contiene dati dinamici segnalati da o associati a un edificio o a operazioni applicabili all'edificio. Questa entità è associata ai segmenti verticali delle case intelligenti, delle città intelligenti, dell'industria e delle relative applicazioni IoT. Questo modello di dati è stato parzialmente sviluppato in collaborazione con gli operatori di telefonia mobile e [GSMA] (https://www.gsma.com/iot/iot-big-data/); rispetto al modello di dati GSMA sono state introdotte le seguenti modifiche - `refRelatedDeviceOperation` sostituisce `refRelatedOperation`.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### BuildingOperation NGSI-v2 valori-chiave Esempio  
Ecco un esempio di BuildingOperation in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### EdificioOperazione NGSI-v2 normalizzato Esempio  
Ecco un esempio di BuildingOperation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### CostruireOperazione Valori chiave NGSI-LD Esempio  
Ecco un esempio di BuildingOperation in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:BuildingOperation:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
    "type": "BuildingOperation",  
    "createdAt": "2016-08-08T10:18:16Z",  
    "dataProvider": {  
        "type": "Property",  
        "value": "OperatorA"  
    },  
    "dateFinished": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-20T10:18:16Z"  
        }  
    },  
    "dateStarted": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-08T10:18:16Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Air conditioning levels reduced due to out of hours"  
    },  
    "endDate": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-20T10:18:16Z"  
        }  
    },  
    "modifiedAt": "2016-08-08T10:18:16Z",  
    "operationSequence": {  
        "type": "Property",  
        "value": [  
            "fan_power%3D0",  
            "set_temperature%3D24"  
        ]  
    },  
    "operationType": {  
        "type": "Property",  
        "value": "airConditioning"  
    },  
    "refBuilding": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Building:building-a85e3da145c1"  
    },  
    "refRelatedBuildingOperation": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:BuildingOperation:b4fb8bff-1a8f-455f-8cc0-ca43c069f865",  
            "urn:ngsi-ld:BuildingOperation:55c24793-3437-4157-9bda-667c9e1531fc"  
        ]  
    },  
    "refRelatedDeviceOperation": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:DeviceOperation:36744245-6716-4a28-84c7-0e3d7520f143",  
            "urn:ngsi-ld:DeviceOperation:33b2b713-9223-40a5-87a0-3f80a1264a6c"  
        ]  
    },  
    "result": {  
        "type": "Property",  
        "value": "ok"  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://www.example.com"  
    },  
    "startDate": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-08T10:18:16Z"  
        }  
    },  
    "status": {  
        "type": "Property",  
        "value": "finished"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Building/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### EdificioOperazione NGSI-LD normalizzato Esempio  
Ecco un esempio di BuildingOperation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:BuildingOperation:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
    "type": "BuildingOperation",  
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
