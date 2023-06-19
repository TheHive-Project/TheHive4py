# Organisation


### Input Organisation

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```name```           | ```str```                        | Organisation's name                            | required            |
| ```description```    | ```str```                        | Organisation's description                     | Not required        |             
| ```taskRule```       | ```str```                        | Task rule                                      | Not required        |
| ```observableRule``` | ```str```                        | Observable rule                                | Not required        |
| ```locked```         | ```bool```                       |  ```True```to mark it as locked                | Not required        |


### Output Organisation

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```_id```           | ```str```                        | Organisation's id                            | required            |
| ```_type```           | ```str```                        | Organisation's type                            | required            |
| ```_createdBy```           | ```str```                        | Organisation's creator                            | required            |
| ```_createdAt```           | ```str```                        | Organisation's creation date                         | required            |
| ```name```           | ```str```                        | Organisation's name                            | required            |
| ```description```    | ```str```                        | Organisation's description                     |  required        |             
| ```taskRule```       | ```str```                        | Task rule                                      |  required        |
| ```observableRule``` | ```str```                        | Observable rule                                |  required        |
| ```locked```         | ```bool```                       |  ```True```to mark it as locked                |  required        |
| ```extraData```           | ```dict```                        | Organisation's extradata                     | required            |
| ```_updatedBy```       | ```str```                        | The user that updated the organisation                                      | Not required        |
| ```_updatedAt``` | ```int```                        | Update date                                |  Not required        |
| ```links```         | ```List[InputOrganisationLink]```                       |  Organisation's links                |  Not required        |
| ```avatar```           | ```str```                        | Organisation's avatar                     | Not required            |


### Input Update Organisation

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```name```           | ```str```                        | Organisation's name                            | required            |
| ```description```    | ```str```                        | Organisation's description                     |  required        |             
| ```taskRule```       | ```str```                        | Task rule                                      |  required        |
| ```observableRule``` | ```str```                        | Observable rule                                |  required        |
| ```locked```         | ```bool```                       |  ```True```to mark it as locked                |  required        |
| ```avatar```           | ```str```                        | Organisation's avatar                     | required            |


### Input Organisation Link

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```linkType```           | ```str```                        | Organisation's link type                            | required            |
| ```otherLinkType```    | ```str```                        | Other organisations link type                      |  required        |             

### Input Bulk Organisation Link

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```toOrganisation```    | ```str```                        |                      |  required        |   
| ```linkType```           | ```str```                        | Organisation's link type                            | required            |
| ```otherLinkType```    | ```str```                        | Other organisations link type                      |  required        |   


### Output Sharing Profile

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```name```           | ```str```                        | Profile's name                            | required            |
| ```description```    | ```str```                        | Profile's description                     |  required        |             
| ```autoShare```       | ```bool```                        | Auto share profile                                      |  required        |
| ```editable``` | ```bool```                        | Editable profile                                |  required        |
| ```permissionProfile```         | ```str```                       |  Profile's permission                |  required        |
| ```taskRule```           | ```str```                        | Task rule                 | required            |
| ```observableRule```           | ```str```                        | Observable rule                     | required            |