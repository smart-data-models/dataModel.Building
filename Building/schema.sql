/* (Beta) Export of data model Building of the subject dataModel.Building for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Building_type AS ENUM ('Building');
CREATE TABLE Building (address json, alternateName text, areaServed text, category json, collapseRisk text, containedInPlace json, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, floorsAboveGround integer, floorsBelowGround integer, id text, location json, name text, occupier json, openingHours json, owner json, peopleCapacity text, peopleOccupancy text, refMap text, seeAlso json, source text, type Building_type);