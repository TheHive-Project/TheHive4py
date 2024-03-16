# CustomEvent


### Input Custom Event

**Parameters**


| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```date```           | ```int```                        | Event's date                                   | required            |
| ```title```          | ```str```                        | Event's title                                  | required            |
| ```endDate```        | ```int```                        | Event's end date                               | required            |
| ```description```    | ```str```                        | event's description                            | Not required        |             


### Output Custom Event

**Parameters**

| Name                    | Type                             | Description                                    | Default             |
|----------------------   |-----------------------           |------------------------------------------------|---------------------|
| ```_id```      | ```str```                        | Event's id                    | required            |
| ```_type```    | ```str```                        | Event's type                       |  required        |             
| ```_createdAt```         | ```int```                        | Event's creation date                             | required            |
| ```_createdBy```      | ```str```                        | Event's creator                            | required            |
| ```date```      | ```int```                        | Event's date                            | required            |
| ```title```      | ```str```                        | Event's title                            | required            |
| ```_updatedBy```           | ```str```                        | The user that updated the event             | Not required            |
| ```_updatedAt```         | ```int```                        | Event's update date                               |  Not required        |
| ```endDate```        | ```int```                        | Event's end date                               | Not required            |
| ```description```    | ```str```                        | event's description                            | Not required        |     


### Input Update Custom Event

**Parameters**


| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```date```           | ```int```                        | Event's date                                   | required            |
| ```title```          | ```str```                        | Event's title                                  | required            |
| ```endDate```        | ```int```                        | Event's end date                               | required            |
| ```description```    | ```str```                        | event's description                            | Not required        |  


### Output Timeline Event

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```date```           | ```int```                        | Timeline's date                                   | required            |
| ```kind```          | ```str```                        | Timeline's kind                                  | required            |
| ```entity```        | ```str```                        | Timeline's entity                                | required            |
| ```entityId```    | ```str```                        | Timeline entity's ID                            | Not required        |  
| ```details```        | ```dict```                        | Timeline details                               | required            |
| ```endDate```    | ```int```                        | Timeline end date                            | Not required        |  


### Output Timeline 

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```events```           | ```List[OutputTimelineEvent]```                        | Timeline's events                                 | required            |