/* (Beta) Export of data model BuildingOperation of the subject dataModel.Building for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE BuildingOperation_result_type AS ENUM ('ok', 'aborted');
CREATE TYPE BuildingOperation_status_type AS ENUM ('cancelled', 'finished', 'ongoing', 'planned', 'scheduled');
CREATE TYPE BuildingOperation_type AS ENUM ('BuildingOperation');
CREATE TABLE BuildingOperation (
  "alternateName" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateFinished" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "dateStarted" TIMESTAMP,
  "description" TEXT,
  "endDate" TIMESTAMP,
  "id" TEXT PRIMARY KEY,
  "name" TEXT,
  "operationSequence" JSON,
  "operationType" TEXT,
  "owner" JSON,
  "refBuilding" JSON,
  "refOperator" JSON,
  "refRelatedBuildingOperation" JSON,
  "refRelatedDeviceOperation" JSON,
  "result" BuildingOperation_result_type,
  "seeAlso" JSON,
  "source" TEXT,
  "startDate" TIMESTAMP,
  "status" BuildingOperation_status_type,
  "type" BuildingOperation_type
);