# Task


### Input Task

**Parameters**

| Name                    | Type                             | Description                                    | Default             |
|----------------------   |-----------------------           |------------------------------------------------|---------------------|
| ```title```             | ```str```                        | Task's title. Default: None                    | required            |
| ```group```             | ```str```                        | Task's group.                                  | Not required        |
| ```description```       | ```str```                        | Task's description. Default: None              | Not required        |
| ```status```            | ```str```                        | Task's status: ```Waiting```, ```InProgress```, ```Cancel```, ```Completed```. Default: ```Waiting```                                                                                        | Not required        |
| ```flag```             | ```bool```                       | Task's flag, ```True``` to mark the task as important. Default: ```False```                                                                                                   | Not required        |
| ```startDate```         | ```int```                        | Task's start date Default: None                | Not required        |
| ```endDate```           | ```int```                        | Task's end date Default: None                  | Not required        |
| ```order```             | ```int```                        | Task's start date Default: None                | Not required        |
| ```dueDate```           | ```int```                        | Task's due date Default: None                  | Not required        |
| ```assignee```          | ```str```                        | Task's assignee                                | Not required        |


### Output Task

**Parameters**

| Name                    | Type                             | Description                                    | Default             |
|----------------------   |-----------------------           |------------------------------------------------|---------------------|
| ```_id```             | ```str```                        | Task's title. Default: None                    | required            |
| ```_type```             | ```str```                        | Task's group.                                  |  required        |
| ```_createdBy```       | ```str```                        | Task's creator             |  required        |
| ```_createdAt```            | ```int```                        | Task's creation date                                                                                        | Not required        |
| ```group```             | ```str```                       | Task's group                                                                             |  required        |
| ```status```         | ```str```                        | Task's status: ```Waiting```, ```InProgress```, ```Cancel```, ```Completed```. Default: ```Waiting```                |  required        |
| ```flag```           | ```bool```                        | Task's flag, ```True``` to mark the task as important. Default: ```False```                   |  required        |
| ```order```             | ```int```                        | Task's order                |  required        |
| ```extraData```           | ```dict```                        | Task's extra data               |  required        |
| ```_updateBy```          | ```str```                        | The user that updated the task                                | Not required        |
| ```_updateAt```          | ```int```                        | Task's update date                             | Not required        |
| ```description```          | ```str```                        | Task's description                                | Not required        |
| ```startDate```          | ```int```                        | Task's start date                                | Not  required        |
| ```endDate```          | ```int```                        | Task's end date                                | Not required        |
| ```assignee```          | ```str```                        | Task's assignee                                | Not required        |
| ```dueDate```          | ```int```                        | Task's due date                                |  Not required        |


### Input Update Task

**Parameters**

| Name                    | Type                             | Description                                    | Default             |
|----------------------   |-----------------------           |------------------------------------------------|---------------------|
| ```title```             | ```str```                        | Task's title                    | required            |
| ```group```             | ```str```                        | Task's group                                  | Not required        |
| ```description```       | ```str```                        | Task's description              | Not required        |
| ```status```            | ```str```                        | Task's status: ```Waiting```, ```InProgress```, ```Cancel```, ```Completed```. Default: ```Waiting```                                                                                        | Not required        |
| ```flag```             | ```bool```                       | Task's flag, ```True``` to mark the task as important. Default: ```False```                                                                                                   | Not required        |
| ```startDate```         | ```int```                        | Task's start date                 | Not required        |
| ```endDate```           | ```int```                        | Task's end date                   | Not required        |
| ```order```             | ```int```                        | Task's start date                 | Not required        |
| ```dueDate```           | ```int```                        | Task's due date                  | Not required        |
| ```assignee```          | ```str```                        | Task's assignee                                | Not required        |