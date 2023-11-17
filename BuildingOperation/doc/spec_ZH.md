<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：建筑运行    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.Building/blob/master/BuildingOperation/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**关于特定楼宇运行的信息**    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `alternateName[string]`: 该项目的替代名称  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateFinished[date-time]`: 操作的实际结束日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `dateStarted[date-time]`: 行动的实际开始日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 项目描述  - `endDate[date-time]`: 计划结束行动的日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `id[*]`: 实体的唯一标识符  - `name[string]`: 该项目的名称  - `operationSequence[array]`: 如果有，操作顺序标识  . Model: [https://schema.org/Text](https://schema.org/Text)- `operationType[string]`: 建筑施工类型  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `refBuilding[*]`: 执行操作的楼宇编号  . Model: [https://schema.org/URL](https://schema.org/URL)- `refOperator[*]`: 参照在建筑物上进行操作的操作员  . Model: [https://schema.org/URL](https://schema.org/URL)- `refRelatedBuildingOperation[array]`: 依次参考其他建筑工程  - `refRelatedDeviceOperation[array]`: 与当前操作相关的设备。设备类型实体的引用列表  . Model: [https://schema.org/URL](https://schema.org/URL)- `result[string]`: 建造操作的结果。枚举：'确定，中止  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `startDate[date-time]`: 计划开始行动的日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `status[string]`: 操作状态。枚举：'已取消、已完成、正在进行、已计划、已安排'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: 必须是 BuildingOperation  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `endDate`  - `id`  - `refBuilding`  - `startDate`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
该实体包含对应用于引用楼宇的通用操作（与智能楼宇相关）的统一描述。楼宇操作包含楼宇或适用于楼宇的操作所报告或与之相关的动态数据。该实体与智能家居、智能城市、工业和相关物联网应用的垂直细分市场有关。本数据模型部分是与移动运营商和[GSMA](https://www.gsma.com/iot/iot-big-data/)合作开发的，与 GSMA 数据模型相比，引入了以下变化 - `refRelatedDeviceOperation` 取代了 `refRelatedOperation` 。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
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
## 有效载荷示例    
#### BuildingOperation NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 BuildingOperation 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### BuildingOperation NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 BuildingOperation 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### BuildingOperation NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 BuildingOperation 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### BuildingOperation NGSI-LD normalized 示例    
下面是一个规范化 JSON-LD 格式的 BuildingOperation 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
