Entité : BuildingOperation  
==========================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Information sur une opération de construction donnée**  

## Liste des biens  

`alternateName`: Un autre nom pour cet article  `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  `dateFinished`: La date de fin effective de l'opération.  `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  `dateStarted`: La date réelle de début de l'opération.  `description`: Une description de cet article  `endDate`: La date de fin prévue pour l'opération.  `id`:   `name`: Le nom de cet article.  `operationSequence`:   `operationType`:   `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  `refBuilding`:   `refOperator`:   `refRelatedBuildingOperation`: Relation.  `result`: Résultat de l'opération de construction  `seeAlso`:   `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  `startDate`: La date de début prévue pour l'opération.  `status`:   `type`: Il doit s'agir de BuildingOperation    
Cette entité contient une description harmonisée d'une opération générique (relative aux bâtiments intelligents) appliquée au bâtiment référencé. L'opération de bâtiment contient des données dynamiques déclarées par, ou associées à, un bâtiment ou des opérations applicables au bâtiment. Cette entité est associée aux segments verticaux des maisons intelligentes, des villes intelligentes, de l'industrie et des applications IdO connexes. Ce modèle de données a été partiellement développé en coopération avec les opérateurs de téléphonie mobile et le [GSMA] (https://www.gsma.com/iot/iot-big-data/). Par rapport au modèle de données GSMA, les changements suivants sont introduits - "refRelatedDeviceOperation" remplace "refRelatedOperation".  
## Modèle de données description des biens  
Classement par ordre alphabétique  
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
Voici un exemple de BuildingOperation en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple d'une opération de bâtiment au format JSON normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple d'une opération de construction en format JSON-LD comme valeurs clés. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple d'une opération de bâtiment au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
