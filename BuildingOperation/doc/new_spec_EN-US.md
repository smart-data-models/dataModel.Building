Entity: BuildingOperation  
=========================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **Information on a given Building Operation**  

## List of properties  

- `alternateName`: An alternative name for this item  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateFinished`: The actual end date for the operation.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateStarted`: The actual start date for the operation.  - `description`: A description of this item  - `endDate`: The planned end date for the operation.  - `id`:   - `name`: The name of this item.  - `operationSequence`:   - `operationType`:   - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refBuilding`:   - `refOperator`:   - `refRelatedBuildingOperation`: Relationship.   - `result`: Result of the building operation  - `seeAlso`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `startDate`: The planned start date for the operation.  - `status`:   - `type`: It has to be BuildingOperation    
This entity contains a harmonised description of a generic operation (related to smart buildings) applied to the referenced building. The building operation contains dynamic data reported by, or associated with a building or operations applicable to the building. This entity is associated with the vertical segments of smart homes, smart cities, industry and related IoT applications. This data model has been partially developed in cooperation with mobile operators and the [GSMA](https://www.gsma.com/iot/iot-big-data/), compared to GSMA data model the following changes are introduced - `refRelatedDeviceOperation` replaces `refRelatedOperation`  
## Data Model description of properties  
Sorted alphabetically  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BuildingOperation:    
  description: 'Information on a given Building Operation'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateFinished:    
      description: 'The actual end date for the operation.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateStarted:    
      description: 'The actual start date for the operation.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    description:    
      description: 'A description of this item'    
      type: Property    
    endDate:    
      description: 'The planned end date for the operation.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    operationSequence:    
      description: ""    
      items:    
        type: string    
      type: Property    
    operationType:    
      description: ""    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *buildingoperation_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    refBuilding:    
      anyOf: *buildingoperation_-_properties_-_owner_-_items_-_anyof    
    refOperator:    
      anyOf: *buildingoperation_-_properties_-_owner_-_items_-_anyof    
    refRelatedBuildingOperation:    
      description: 'Relationship. '    
      items:    
        anyOf: *buildingoperation_-_properties_-_owner_-_items_-_anyof    
      refRelatedDeviceOperation:    
        description: 'Relationship. '    
        items:    
          anyOf: *buildingoperation_-_properties_-_owner_-_items_-_anyof    
        type: array    
      type: array    
    result:    
      description: 'Result of the building operation'    
      enum:    
        - ok    
        - aborted    
      type: Property    
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
    startDate:    
      description: 'The planned start date for the operation.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    status:    
      description: ""    
      enum:    
        - planned    
        - ongoing    
        - finished    
        - scheduled    
        - cancelled    
      type: Property    
    type:    
      description: 'It has to be BuildingOperation'    
      enum:    
        - BuildingOperation    
      type: Property    
  required:    
    - type    
    - id    
    - refBuilding    
    - startDate    
    - endDate    
  type: object    
```  
</details>    
#### BuildingOperation NGSI V2 key-values Example    
Here is an example of a BuildingOperation in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### BuildingOperation NGSI V2 normalized Example    
Here is an example of a BuildingOperation in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### BuildingOperation NGSI-LD key-values Example    
Here is an example of a BuildingOperation in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "createdAt": "2016-08-08T10:18:16Z",  
 "dataProvider": "OperatorA",  
 "dateFinished": {"@type": "DateTime", "@value": "2016-08-20T10:18:16Z"},  
 "dateStarted": {"@type": "DateTime", "@value": "2016-08-08T10:18:16Z"},  
 "description": "Air conditioning levels reduced due to out of hours",  
 "endDate": {"@type": "DateTime", "@value": "2016-08-20T10:18:16Z"},  
 "id": "urn:ngsi-ld:BuildingOperation:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
 "modifiedAt": "2016-08-08T10:18:16Z",  
 "operationSequence": ["fan_power%3D0", "set_temperature%3D24"],  
 "operationType": "airConditioning",  
 "refBuilding": "urn:ngsi-ld:Building:building-a85e3da145c1",  
 "refRelatedBuildingOperation": ["urn:ngsi-ld:BuildingOperation:b4fb8bff-1a8f-455f-8cc0-ca43c069f865",  
                                 "urn:ngsi-ld:BuildingOperation:55c24793-3437-4157-9bda-667c9e1531fc"],  
 "refRelatedDeviceOperation": ["urn:ngsi-ld:DeviceOperation:36744245-6716-4a28-84c7-0e3d7520f143",  
                               "urn:ngsi-ld:DeviceOperation:33b2b713-9223-40a5-87a0-3f80a1264a6c"],  
 "result": "ok",  
 "source": "http://www.example.com",  
 "startDate": {"@type": "DateTime", "@value": "2016-08-08T10:18:16Z"},  
 "status": "finished",  
 "type": "BuildingOperation"}  
```  
#### BuildingOperation NGSI-LD normalized Example    
Here is an example of a BuildingOperation in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
