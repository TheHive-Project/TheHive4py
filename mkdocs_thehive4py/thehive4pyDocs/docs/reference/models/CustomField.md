# Custom Field


### Input Custom Field

**Parameters**


| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```name```           | ```str```                        | Name of the custom field                       | required            |
| ```group```          | ```str```                        | Group of the custom field                      | required            |              
| ```description```    | ```str```                        | Description of the custom field                | required            |
| ```type```           | ```str```                        | type of the field, possible values are ```string```, ```boolean```, ```number```, ```date```, ```integer```, ```float```                                                                     | required            |
| ```displayName```    | ```str```                        | Display name of the custom field               | Not required        |
| ```mandatory```      | ```bool```                       | True if the field is mandatory                 | Not required        |
| ```option```         | ```list```                       | list of possible values for the field          | Not required        |


### OutputCustom Field

**Parameters**


| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```_id```           | ```str```                        | Custom field's ID                       | required            |
| ```_type```          | ```str```                        | Custom field's type                      | required            |              
| ```_createdBy```    | ```str```                        | Custom field creator                | required            |
| ```_createdAt```           | ```int```                        | Custom field's creation date | required            |
| ```name```         | ```str```                       | Custom field's name          |  required        |
| ```displayName```    | ```str```                        | Display name of the custom field               |  required        |
| ```group```    | ```str```                        | Custom field's group              | required        |
| ```description```    | ```str```                        | Custom field's description               |  required        |
| ```type```    | ```str```                        | Custom field's type              |  required        |
| ```mandatory```      | ```bool```                       | True if the field is mandatory                 |  Default value = false       |
| ```_updatedBy```      | ```str```                       | The user that updated the custom field                 |  Not required        |
| ```_updatedAt```      | ```int```                       | The date the custom field was updated                 |  Not required        |
| ```options```      | ```list```                       | Custom field's options                 |  Not required        |

### Input Custom Field Value

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```name```           | ```str```                        | Name of the custom field                       | required            |
| ```value```          | ```Any```                        | Value of the custom field                      | Not required        |
| ```order```         | ```int```                        | Order of the custom field                      | Not required        |


### Output Custom Field Value

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```_id```           | ```str```                        |Custom field's ID                       | required            |
| ```name```           | ```str```                        | Custom field's name                      |  required        |
| ```description```    | ```str```                        | Custom field's description                      |  required        |
| ```type```           | ```str```                        | Custom field's type                      | required        |
| ```value```          | ```Any```                        | Custom field's value                      |  required        |
| ```order```          | ```int```                        | Custom field's order                      |  required        |


### Input Update Custom Field 

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```displayName```           | ```str```                        |Custom field's display name                       | required            |
| ```group```           | ```str```                        | Custom field's group                      |  required        |
| ```description```    | ```str```                        | Custom field's description                      |  required        |
| ```type```           | ```str```                        | Custom field's type                      | required        |
| ```options```          | ```list```                        | Custom field's options                      |  required        |
| ```mandatory```          | ```bool```                        | True if the field is mandatory                      |  Default value = False        |