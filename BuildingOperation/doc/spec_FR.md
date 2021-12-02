Entité : BuildingOperation  
==========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Building/blob/master/BuildingOperation/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Information sur une opération de construction donnée**  

## Liste des propriétés  

- `alternateName`: Un nom alternatif pour cet élément  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateFinished`: La date de fin réelle de l'opération.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateStarted`: La date de début effective de l'opération.  - `description`: Une description de cet article  - `endDate`: La date de fin prévue pour l'opération.  - `id`: Identifiant unique de l'entité  - `name`: Le nom de cet élément.  - `operationSequence`: Id de la séquence de l'opération si disponible  - `operationType`: Type d'opération sur le bâtiment  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refBuilding`: Référence du bâtiment où l'opération est effectuée.  - `refOperator`: Référence à l'opérateur qui effectue l'opération sur le bâtiment.  - `refRelatedBuildingOperation`: Référence à d'autres opérations de construction lorsqu'elles se succèdent  - `refRelatedDeviceOperation`: Dispositifs liés à l'opération en cours. Une liste de références à une entité de type Device.  - `result`: Résultat de l'opération de construction. Enum : "ok, avorté  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `startDate`: La date de début prévue pour l'opération.  - `status`: Statut de l'opération. Enum : 'cancelled, finished, ongoing, planned, scheduled' (annulé, terminé, en cours, planifié, prévu)  - `type`: Il doit s'agir de BuildingOperation    
Propriétés requises  
- `endDate`  - `id`  - `refBuilding`  - `startDate`  - `type`    
Cette entité contient une description harmonisée d'une opération générique (liée aux bâtiments intelligents) appliquée au bâtiment référencé. L'opération de bâtiment contient des données dynamiques signalées par, ou associées à un bâtiment ou à des opérations applicables au bâtiment. Cette entité est associée aux segments verticaux des maisons intelligentes, des villes intelligentes, de l'industrie et des applications IoT connexes. Ce modèle de données a été partiellement développé en coopération avec les opérateurs mobiles et la [GSMA] (https://www.gsma.com/iot/iot-big-data/). Par rapport au modèle de données de la GSMA, les changements suivants sont introduits : `refRelatedDeviceOperation` remplace `refRelatedOperation`.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
      description: 'Unique identifier of the entity'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    operationSequence:    
      description: 'Id of the sequence of the operation when available'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    operationType:    
      description: 'Type of the operation on the building'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *buildingoperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
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
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    refRelatedBuildingOperation:    
      description: 'Reference to other building operations when in sequence'    
      items:    
        anyOf: *buildingoperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Relationship    
    refRelatedDeviceOperation:    
      description: 'Devices related to the current operation. A list of references to an entity of type Device.'    
      items:    
        anyOf: *buildingoperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    result:    
      description: 'Result of the building operation. Enum:''ok, aborted'''    
      enum:    
        - ok    
        - aborted    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
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
      description: 'Status of the operation. Enum:''cancelled, finished, ongoing, planned, scheduled'' '    
      enum:    
        - cancelled    
        - finished    
        - ongoing    
        - planned    
        - scheduled    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
## Exemples de charges utiles  
#### BuildingOperation Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'une BuildingOperation au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### BuildingOperation NGSI-v2 normalisé Exemple  
Voici un exemple de BuildingOperation au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### BuildingOperation Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'une BuildingOperation au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### BuildingOperation NGSI-LD normalisé Exemple  
Voici un exemple de BuildingOperation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude