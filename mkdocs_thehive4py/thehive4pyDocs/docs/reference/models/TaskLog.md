# TaskLog


### Input TaskLog

**Parameters**

| Name                    | Type                             | Description                                    | Default             |
|----------------------   |-----------------------           |------------------------------------------------|---------------------|
| ```message```           | ```str```                        | Log's description. Default: None               | required            |
| ```startDate```         | ```int```                        | Log's start date                               | Not required        |
| ```includeInTimeLine``` | ```int```                        |                                                | Not required        |


### Output TaskLog

**Parameters**

| Name                    | Type                             | Description                                    | Default             |
|----------------------   |-----------------------           |------------------------------------------------|---------------------|
| ```_id```      | ```str```                        | Task log's id                    | required            |
| ```_type```    | ```str```                        | Task log's type                       |  required        |             
| ```_createdAt```         | ```int```                        | Task log's creation date                             | required            |
| ```_createdBy```      | ```str```                        | Task log's creator                            | required            |
| ```message```           | ```str```                        | Log's description. Default: None               | required            |
| ```date```         | ```int```                        | Log's date                               |  required        |
| ```owner```         | ```str```                        | Log's owner                             |  required        |
| ```extraData``` | ```dict```                        |Log's extra data                                                |  required        |
| ```_updatedBy```           | ```str```                        | The user that updated the log               | Not required            |
| ```_updatedAt```         | ```int```                        | Log's update date                               |  Not required        |
| ```attachments```         | ```List[dict]```                        | Log's attachments                            | Not required        |
| ```includeInTimeline``` | ```int```                        |Include log in timeline                                               |  Not required        |


### Input Update TaskLog

**Parameters**

| Name                    | Type                             | Description                                    | Default             |
|----------------------   |-----------------------           |------------------------------------------------|---------------------|
| ```message```           | ```str```                        | Log's description.                | required            |
| ```includeInTimeLine``` | ```int```                        |   Include log in timeline                                             | Not required        |