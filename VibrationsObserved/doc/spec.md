Entity: VibrationsObserved  
==========================  
[Open License](https://github.com/smart-data-models//dataModel.Building/blob/master/VibrationsObserved/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **The vibrations observed in a specific place.**  

## List of properties  

- `accelerationMeasured`: Magnitude of the vibrations observed (e.g. Earthquake) or other floor movements  - `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateObserved`: Date and time of the observation in ISO8601  - `description`: A description of this item  - `id`: Unique identifier of the entity  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI-LD Entity Type. It has to be VibrationsObserved    
Required properties  
- `accelerationMeasured`  - `dateObserved`  - `id`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
VibrationsObserved:    
  description: 'The vibrations observed in a specific place.'    
  properties:    
    accelerationMeasured:    
      description: 'Magnitude of the vibrations observed (e.g. Earthquake) or other floor movements'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: m/s2    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateObserved:    
      description: 'Date and time of the observation in ISO8601'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &vibrationsobserved_-_properties_-_owner_-_items_-_anyof    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *vibrationsobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It has to be VibrationsObserved'    
      enum:    
        - VibrationsObserved    
      type: Property    
  required:    
    - id    
    - dateObserved    
    - accelerationMeasured    
  type: object    
```  
</details>    
## Example payloads    
#### VibrationsObserved NGSI-v2 key-values Example    
Here is an example of a VibrationsObserved in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "VibrationsObserved-Sevilla-1",  
  "type": "VibrationsObserved",  
  "name": "Sevilla vibrations",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Sevilla"  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      37.3984759,  
      -5.9904124  
    ]  
  },  
  "dataProvider": "IMU-Station-123",  
  "dateObserved": "2021-03-08T09:45:00Z",  
  "accelerationMeasured": 1.3  
}  
```  
#### VibrationsObserved NGSI-v2 normalized Example    
Here is an example of a VibrationsObserved in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:VibrationsObserved:id:IPZH:79807295",  
"type": "VibrationsObserved",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2021-03-08T09:45:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-03-08T09:45:00Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "No source"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Sevilla vibrations"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Sevilla vibrations"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "Text",  
    "value": [  
      "urn:ngsi-ld:VibrationsObserved:items:ENTK:59457468",  
      "urn:ngsi-ld:VibrationsObserved:items:DDNB:10988523"  
    ]  
  },  
  "seeAlso": {  
    "type": "Text",  
    "value": [  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        37.3984759,  
        -5.9904124  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "C/Torre del Oro",  
      "addressLocality": "Seville",  
      "addressRegion": "Andalucia",  
      "addressCountry": "ES",  
      "postalCode": "41410",  
      "postOfficeBoxNumber": "",  
      "areaServed": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": ""  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2021-03-08T09:45:00Z"  
  },  
  "accelerationMeasured": {  
    "type": "Number",  
    "value": 1.3  
  }  
}  
```  
#### VibrationsObserved NGSI-LD key-values Example    
Here is an example of a VibrationsObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:VibrationsObserved-Sevilla-1",  
  "type": "VibrationsObserved",  
  "name": "Sevilla vibrations",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Sevilla"  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      37.3984759,  
      -5.9904124  
    ]  
  },  
  "dataProvider": "IMU-Station-123",  
  "dateObserved": "2021-03-08T09:45:00Z",  
  "accelerationMeasured": 1.3  
}  
```  
#### VibrationsObserved NGSI-LD normalized Example    
Here is an example of a VibrationsObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:VibrationsObserved:id:IPZH:79807295",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-08T09:45:00Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-08T09:45:00Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "No source"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Sevilla vibrations"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": "Sevilla vibrations"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": ""  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:VibrationsObserved:items:ENTK:59457468",  
      "urn:ngsi-ld:VibrationsObserved:items:DDNB:10988523"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        37.3984759,  
        -5.9904124  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "C/Torre del Oro",  
      "addressLocality": "Seville",  
      "addressRegion": "Andalucia",  
      "addressCountry": "ES",  
      "postalCode": "41410",  
      "postOfficeBoxNumber": "",  
      "areaServed": ""  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": ""  
  },  
  "type": "VibrationsObserved",  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-08T09:45:00Z"  
    }  
  },  
  "accelerationMeasured": {  
    "type": "Property",  
    "value": 1.3  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
