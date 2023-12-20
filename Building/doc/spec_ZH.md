<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：建筑  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Building/blob/master/Building/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**关于特定建筑物的**信息  
版本： 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 标识公共街道上特定房产的编号    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: 建筑物类别。枚举：'公寓、烤房、谷仓、桥梁、平房、碉堡、大教堂、小屋、车棚、教堂、教堂、公民、商业、温室、建筑、牛棚、独立式、沼气池、宿舍、农场、农场辅助设施、车库、车库、垃圾棚、看台、温室、飞机库、医院、旅馆、房屋、船屋、小屋、工业、幼儿园、小卖部、清真寺、办公室、停车场、亭子、公共建筑、住宅、零售、骑马厅、屋顶、废墟、学校、服务设施、棚屋、神龛、马厩、体育场、静态房车、风格、犹太教堂、寺庙、露台、火车站、变压器塔、运输工具、大学、仓库、水塔'。  - `collapseRisk[number]`: 建筑物完全倒塌的概率  . Model: [https://schema.org/Number](https://schema.org/Number)- `containedInPlace[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `floorsAboveGround[number]`: 地面以上楼层  . Model: [https://schema.org/Number](https://schema.org/Number)- `floorsBelowGround[number]`: 地面以下楼层  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `occupier[array]`: 使用建筑物的个人或实体  . Model: [https://schema.org/URL](https://schema.org/URL)- `openingHours[array]`: 该建筑的开放时间  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `peopleCapacity[number]`: 大楼内允许的人员  . Model: [https://schema.org/Number](https://schema.org/Number)- `peopleOccupancy[number]`: 楼内人员  . Model: [https://schema.org/Number](https://schema.org/Number)- `refMap[*]`: 包含建筑物的地图参考  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 实体类型  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `address`  - `category`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
该实体包含对建筑物的统一描述。该实体与智能家居、智能城市、工业和相关物联网应用的垂直细分市场相关联。本数据模型部分是与移动运营商和[GSMA](https://www.gsma.com/iot/iot-big-data/)合作开发的，与 GSMA 数据模型相比，引入了以下变化 删除了 "BuildingType"，因为与 "category "属性相比，"BuildingType "没有引入重要信息。类别 "属性是必需的。根据 schema.org 数据模型引入了 `openingHours` 属性，以便对建筑物的开放时间进行细化。GSMA 支持在 `notes` 属性中将其作为自由文本（也已删除）。由于目前不支持 `SubscriptionService` 模型，因此不支持 `refSubscriptionService` 属性。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Building:    
  description: Information on a given Building    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
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
      description: Probability of total collapse of the building    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    containedInPlace:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
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
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    floorsAboveGround:    
      description: Floors above the ground level    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    floorsBelowGround:    
      description: Floors below the ground level    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    mapUrl:    
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
      description: Reference to the map containing the building    
      x-ngsi:    
        type: Relationship    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    occupier:    
      description: Person or entity using the building    
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
    openingHours:    
      description: Opening hours of this building    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHours    
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
    peopleCapacity:    
      description: Allowed people present at the building    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    peopleOccupancy:    
      description: People present at the building    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    type:    
      description: NGSI Entity type    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Building/blob/master/Building/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Building/Building/schema.json    
  x-model-tags: ""    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 建立 NGSI-v2 密钥值示例  
下面是一个以 JSON-LD 格式作为键值的 Building 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### 建立 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 "建筑 "示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "building-a85e3da145c1",  
  "type": "Building",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "office"  
    ]  
  },  
  "floorsBelowGround": {  
    "type": "Boolean",  
    "value": false  
  },  
  "description": {  
    "type": "Text",  
    "value": "Office block"  
  },  
  "floorsAboveGround": {  
    "type": "Number",  
    "value": 7  
  },  
  "occupier": {  
    "type": "StructuredValue",  
    "value": [  
      "9830f692-7677-11e6-838b-4f9fb3dc5a4f"  
    ]  
  },  
  "mapUrl": {  
    "type": "Text",  
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
    "type": "StructuredValue",  
    "value": {  
      "addressLocality": "London",  
      "postalCode": "EC4N 8AF",  
      "streetAddress": "25 Walbrook"  
    }  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "1be9cd61-ef59-421f-a326-4b6c84411ad4"  
    ]  
  },  
  "openingHours": {  
    "type": "StructuredValue",  
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
#### 建立 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为 key-values 的 Building 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Building/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### 建筑 NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的 "建筑 "示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
      "streetAddress": "25 Walbrook"  
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
    "type": "GeoProperty",  
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
