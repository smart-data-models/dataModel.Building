Entité : BuildingType  
=====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Building/blob/master/BuildingType/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité contient une description harmonisée d'un type de bâtiment générique. Cette entité est associée aux segments verticaux de la maison intelligente, des villes intelligentes, de l'industrie et des applications IoT connexes. Le type de bâtiment comprend une structure hiérarchique qui permet de regrouper les types de bâtiment de manière flexible.**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `buildingTypeChildren`: Référence aux types de bâtiments enfants, c'est-à-dire immédiatement inférieurs à cette entité dans la hiérarchie.  - `buildingTypeParent`: Renvoie à toute entité de type de bâtiment de niveau supérieur sur laquelle ce type est basé.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `root`: Un indicateur logique qu'il s'agit de la racine d'une hiérarchie BuildingType. True indique qu'il s'agit de la racine, false indique qu'il ne s'agit pas de la racine.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Identifiant de l'entité NGSI. Il doit s'agir de BuildingType    
Propriétés requises  
- `id`  - `type`    
Ce modèle de données est issu du projet original GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Il y a quelques adaptations mineures pour répondre aux exigences des modèles de données intelligents.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BuildingType:    
  description: 'This entity contains a harmonised description of a generic building type. This entity is associated with the vertical segments of smart home, smart cities, industry and related IoT applications. The building type includes a hierarchical structure that allows building types to be grouped in a flexible way.'    
  properties:    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    buildingTypeChildren:    
      description: 'Reference to child building types i.e. immediately below this entity in the hierarchy.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    buildingTypeParent:    
      'anyOf ':    
        - 'description ': 'Property. Identifier format of any NGSI entity '    
          'maxLength ': 256    
          'minLength ': 1    
          'pattern ': ^[\w\-\.\{\}\$\+\*\[\]`|~^@!:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'References any higher level Building Type entities that this type is based on.'    
      x-ngsi:    
        type: Relationship    
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
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &buildingtype_-_properties_-_owner_-_items_-_anyof    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *buildingtype_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    root:    
      description: 'A logical indicator that this is the root of a BuildingType hierarchy.True indicates it is the root, false indicates that it is not the root.'    
      type: boolean    
      x-ngsi:    
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
    type:    
      description: 'NGSI Entity identifier. It has to be BuildingType'    
      enum:    
        - BuildingType    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Building/blob/master/BuildingType/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Building/BuildingType/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.2    
```  
</details>    
## Exemples de charges utiles  
#### BuildingType Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'un BuildingType au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:BuildingType:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "type": "BuildingType",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "name": "House",  
  "description": "Standard building type definition for a domestic house",  
  "root": false,  
  "buildingTypeParent": "urn:ngsi-ld:BuildingType:4146335f-839f-4ff9-a575-6b4e6232b734",  
  "buildingTypeChildren": [  
    "urn:ngsi-ld:BuildingType:e4291e84-58f8-11e8-84c3-77e4f1f8c4f1",  
    "urn:ngsi-ld:BuildingType:a71c7a08-58f9-11e8-a41e-4bcb7249360e",  
    "urn:ngsi-ld:BuildingType:afac9bbc-58f9-11e8-b587-1f0d57b81bb4"  
  ]  
}  
```  
#### BuildingType NGSI-v2 normalisé Exemple  
Voici un exemple d'un BuildingType au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:BuildingType:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "type": "BuildingType",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "name": {  
    "type": "Text",  
    "value": "House"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Standard building type definition for a domestic house"  
  },  
  "root": {  
    "type": "Boolean",  
    "value": false  
  },  
  "buildingTypeParent": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingType:4146335f-839f-4ff9-a575-6b4e6232b734"  
  },  
  "buildingTypeChildren": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:BuildingType:e4291e84-58f8-11e8-84c3-77e4f1f8c4f1",  
      "urn:ngsi-ld:BuildingType:a71c7a08-58f9-11e8-a41e-4bcb7249360e",  
      "urn:ngsi-ld:BuildingType:afac9bbc-58f9-11e8-b587-1f0d57b81bb4"  
    ]  
  }  
}  
```  
#### BuildingType Valeurs clés NGSI-LD Exemple  
Voici un exemple d'un BuildingType au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Building/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:BuildingType:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "type": "BuildingType",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "name": "House",  
  "description": "Standard building type definition for a domestic house",  
  "root": false,  
  "buildingTypeParent": "urn:ngsi-ld:BuildingType:4146335f-839f-4ff9-a575-6b4e6232b734",  
  "buildingTypeChildren": [  
    "urn:ngsi-ld:BuildingType:e4291e84-58f8-11e8-84c3-77e4f1f8c4f1",  
    "urn:ngsi-ld:BuildingType:a71c7a08-58f9-11e8-a41e-4bcb7249360e",  
    "urn:ngsi-ld:BuildingType:afac9bbc-58f9-11e8-b587-1f0d57b81bb4"  
  ]  
}  
```  
#### Type de bâtiment NGSI-LD normalisé Exemple  
Voici un exemple d'un BuildingType au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Building/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:BuildingType:57b912ab-eb47-4cd5-bc9d-73abece1f1b3",  
  "type": "BuildingType",  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "name": {  
    "type": "Property",  
    "value": "House"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Standard building type definition for a domestic house"  
  },  
  "root": {  
    "type": "Property",  
    "value": false  
  },  
  "buildingTypeParent": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingType:4146335f-839f-4ff9-a575-6b4e6232b734"  
  },  
  "buildingTypeChildren": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:BuildingType:e4291e84-58f8-11e8-84c3-77e4f1f8c4f1",  
      "urn:ngsi-ld:BuildingType:a71c7a08-58f9-11e8-a41e-4bcb7249360e",  
      "urn:ngsi-ld:BuildingType:afac9bbc-58f9-11e8-b587-1f0d57b81bb4"  
    ]  
  }  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
