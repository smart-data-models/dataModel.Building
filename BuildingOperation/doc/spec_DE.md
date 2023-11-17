<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: BuildingOperation    
==========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Building/blob/master/BuildingOperation/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Informationen über ein bestimmtes Bauvorhaben**    
Version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateFinished[date-time]`: Das tatsächliche Enddatum des Vorgangs  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `dateStarted[date-time]`: Der tatsächliche Starttermin für den Vorgang  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Eine Beschreibung dieses Artikels  - `endDate[date-time]`: Das geplante Enddatum der Operation  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `id[*]`: Eindeutiger Bezeichner der Entität  - `name[string]`: Der Name dieses Artikels  - `operationSequence[array]`: Id der Sequenz des Vorgangs, sofern verfügbar  . Model: [https://schema.org/Text](https://schema.org/Text)- `operationType[string]`: Art der Maßnahme am Gebäude  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refBuilding[*]`: Referenz des Gebäudes, in dem der Vorgang durchgeführt wird  . Model: [https://schema.org/URL](https://schema.org/URL)- `refOperator[*]`: Verweis auf den Bediener, der die Arbeiten am Gebäude durchführt  . Model: [https://schema.org/URL](https://schema.org/URL)- `refRelatedBuildingOperation[array]`: Verweis auf andere Baumaßnahmen, wenn diese aufeinander folgen  - `refRelatedDeviceOperation[array]`: Geräte, die sich auf den aktuellen Vorgang beziehen. Eine Liste von Verweisen auf eine Entität des Typs Gerät  . Model: [https://schema.org/URL](https://schema.org/URL)- `result[string]`: Ergebnis des Bauvorgangs. Enum:'ok, abgebrochen'  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `startDate[date-time]`: Geplanter Starttermin für das Vorhaben  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `status[string]`: Status des Vorgangs. Enum:'abgebrochen, beendet, laufend, geplant, vorgesehen'  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Es muss BuildingOperation sein  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `endDate`  - `id`  - `refBuilding`  - `startDate`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Diese Einheit enthält eine harmonisierte Beschreibung eines generischen Vorgangs (in Bezug auf intelligente Gebäude), der auf das referenzierte Gebäude angewendet wird. Der Gebäudevorgang enthält dynamische Daten, die von einem Gebäude oder von auf das Gebäude anwendbaren Vorgängen gemeldet werden oder damit verbunden sind. Diese Einheit ist mit den vertikalen Segmenten intelligente Häuser, intelligente Städte, Industrie und damit verbundene IoT-Anwendungen verbunden. Dieses Datenmodell wurde teilweise in Zusammenarbeit mit Mobilfunkbetreibern und der [GSMA] (https://www.gsma.com/iot/iot-big-data/) entwickelt. Im Vergleich zum GSMA-Datenmodell wurden die folgenden Änderungen eingeführt: "refRelatedDeviceOperation" ersetzt "refRelatedOperation".    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
BuildingOperation:      
  description: Information on a given Building Operation      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateFinished:      
      description: The actual end date for the operation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateStarted:      
      description: The actual start date for the operation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    endDate:      
      description: The planned end date for the operation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    operationSequence:      
      description: Id of the sequence of the operation when available      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    operationType:      
      description: Type of the operation on the building      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    refBuilding:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Building reference where the operation is performed      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
    refOperator:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Reference to the Operator doing the operation on the building      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
    refRelatedBuildingOperation:      
      description: Reference to other building operations when in sequence      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Relationship      
    refRelatedDeviceOperation:      
      description: Devices related to the current operation. A list of references to an entity of type Device      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
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
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    startDate:      
      description: The planned start date for the operation      
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
      description: It has to be BuildingOperation      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## Beispiel-Nutzlasten    
#### BuildingOperation NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für eine BuildingOperation im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
  "operationSequence": [  
    "fan_power%3D0",  
    "set_temperature%3D24"  
  ],  
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
#### BuildingOperation NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für eine BuildingOperation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "type": "BuildingOperation",  
  "status": {  
    "type": "Text",  
    "value": "finished"  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "2016-08-08T10:18:16Z"  
  },  
  "operationSequence": {  
    "type": "StructuredValue",  
    "value": [  
      "fan_power%3D0",  
      "set_temperature%3D24"  
    ]  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2016-08-20T10:18:16Z"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Air conditioning levels reduced due to out of hours"  
  },  
  "refRelatedDeviceOperation": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
    "value": [  
      "b4fb8bff-1a8f-455f-8cc0-ca43c069f865",  
      "55c24793-3437-4157-9bda-667c9e1531fc"  
    ]  
  },  
  "source": {  
    "type": "Text",  
    "value": "http://www.example.com"  
  },  
  "refBuilding": {  
    "type": "Text",  
    "value": "building-a85e3da145c1"  
  },  
  "result": {  
    "type": "Text",  
    "value": "ok"  
  },  
  "operationType": {  
    "type": "Text",  
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
    "type": "Text",  
    "value": "OperatorA"  
  }  
}  
```  
</details>    
#### BuildingOperation NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für eine BuildingOperation im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:BuildingOperation:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "type": "BuildingOperation",  
  "createdAt": "2016-08-08T10:18:16Z",  
  "dataProvider": "OperatorA",  
  "dateFinished": "2016-08-20T10:18:16Z",  
  "dateStarted": "2016-08-08T10:18:16Z",  
  "description": "Air conditioning levels reduced due to out of hours",  
  "endDate": "2016-08-20T10:18:16Z",  
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
  "startDate": "2016-08-08T10:18:16Z",  
  "status": "finished",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Building/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### BuildingOperation NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für eine BuildingOperation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Building/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
