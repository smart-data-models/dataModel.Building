<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティBuildingOperation  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Building/blob/master/BuildingOperation/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**指定されたビルディング操作に関する情報**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `alternateName[string]`: この項目の別称  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateFinished[string]`: 操作の実際の終了日。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateStarted[string]`: 実際の運用開始日。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: このアイテムの説明  - `endDate[string]`: 運用終了予定日。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `id[*]`: エンティティの一意な識別子  - `name[string]`: このアイテムの名称です。  - `operationSequence[array]`: 可能な場合は、操作のシーケンスの ID  . Model: [https://schema.org/Text](https://schema.org/Text)- `operationType[string]`: 建物に対する操作の種類  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `refBuilding[*]`: 操作が行われる建物の参照。  . Model: [https://schema.org/URL](https://schema.org/URL)- `refOperator[*]`: 建物に対して操作を行うオペレーターを指す。  . Model: [https://schema.org/URL](https://schema.org/URL)- `refRelatedBuildingOperation[array]`: 他のビルディングオペレーションを順次参照する場合  - `refRelatedDeviceOperation[array]`: 現在の操作に関連するデバイス。Device 型のエンティティへの参照のリスト。  . Model: [https://schema.org/URL](https://schema.org/URL)- `result[string]`: 建築操作の結果。Enum:'ok, aborted'  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `startDate[string]`: 運用開始予定日。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `status[string]`: 操作のステータス。Enum:'cancelled, finished, ongoing, planned, scheduled'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: BuildingOperationである必要があります。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `endDate`  - `id`  - `refBuilding`  - `startDate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
このエンティティは、参照される建物に適用される（スマートビルに関連する）一般的な操作の調和された記述を含んでいる。建物操作は、建物によって報告された、または建物に関連する動的データ、または建物に適用される操作を含む。このエンティティは、スマートホーム、スマートシティ、産業、および関連するIoTアプリケーションの垂直セグメントに関連するものである。このデータモデルは、モバイル通信事業者と[GSMA](https://www.gsma.com/iot/iot-big-data/)の協力により一部開発されました。GSMAデータモデルと比較して、以下の変更が導入されています - `refRelatedDeviceOperation` は `refRelatedOperation` を置き換えます。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### BuildingOperation NGSI-v2 key-value 例  
ここでは、BuildingOperationをJSON-LD形式でkey-valuesにした例を示す。これは、`options=keyValues` を使用した場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### BuildingOperation NGSI-v2 正規化例  
以下は、BuildingOperationをJSON-LD形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### BuildingOperation NGSI-LD key-value 例  
BuildingOperationをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### BuildingOperation NGSI-LD 正規化例  
以下は、BuildingOperationをJSON-LD形式で正規化した例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
