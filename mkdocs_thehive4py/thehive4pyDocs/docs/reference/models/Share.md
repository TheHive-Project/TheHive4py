# Share


### Input Share

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```organisation```   | ```str```                        | Organisation to share with                     | required            |
| ```share```          | ```bool```                       | ```True```to share. Default: ```False```       | Not required        |             
| ```profile```        | ```str```                        |                                                | Not required        |
| ```taskRule```       | ```str```                        |                                                | Not required        |
| ```observableRule``` | ```str```                        |                                                | Not required        |


### Output Share

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```_id```      | ```str```                        | Share's id                    | required            |
| ```_type```    | ```str```                        | Share's type                       |  required        |             
| ```_createdAt```         | ```int```                        | Share's creation date                             | required            |
| ```_createdBy```      | ```str```                        | Share's creator                            | required            |
| ```caseId```      | ```str```                        | Share's ID                            | required            |
| ```profileName```          | ```str```                       | The profile's name to share with       |  required        |             
| ```organisationName```   | ```str```                        | Organisation to share with                     | required            |
| ```owner```        | ```bool```                        |                                                | required        |
| ```taskRule```       | ```str```                        |Task rule                                                | required        |
| ```observableRule``` | ```str```                        |Observable rule                                                |  required        |
| ```_updatedAt```    | ```int```                        | Share's updated date                        | Not required        |             
| ```_updatedBy```    | ```str```                        | The user that updated the share                       | Not required        |  