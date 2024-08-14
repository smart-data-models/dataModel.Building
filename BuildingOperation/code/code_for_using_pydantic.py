from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class Result(Enum):
    ok = 'ok'
    aborted = 'aborted'


class Status(Enum):
    cancelled = 'cancelled'
    finished = 'finished'
    ongoing = 'ongoing'
    planned = 'planned'
    scheduled = 'scheduled'


class Type(Enum):
    BuildingOperation = 'BuildingOperation'


class BuildingOperation(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateFinished: Optional[AwareDatetime] = Field(
        None, description='The actual end date for the operation'
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateStarted: Optional[AwareDatetime] = Field(
        None, description='The actual start date for the operation'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    endDate: Optional[AwareDatetime] = Field(
        None, description='The planned end date for the operation'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    name: Optional[str] = Field(None, description='The name of this item')
    operationSequence: Optional[List[str]] = Field(
        None, description='Id of the sequence of the operation when available'
    )
    operationType: Optional[str] = Field(
        None, description='Type of the operation on the building'
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    refBuilding: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Building reference where the operation is performed')
    refOperator: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to the Operator doing the operation on the building',
    )
    refRelatedBuildingOperation: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None, description='Reference to other building operations when in sequence'
    )
    refRelatedDeviceOperation: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='Devices related to the current operation. A list of references to an entity of type Device',
    )
    result: Optional[Result] = Field(
        None, description="Result of the building operation. Enum:'ok, aborted'"
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startDate: Optional[AwareDatetime] = Field(
        None, description='The planned start date for the operation'
    )
    status: Optional[Status] = Field(
        None,
        description="Status of the operation. Enum:'cancelled, finished, ongoing, planned, scheduled' ",
    )
    type: Optional[Type] = Field(None, description='It has to be BuildingOperation')
