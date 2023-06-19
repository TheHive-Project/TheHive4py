# User


### Input User

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```login```          | ```str```                        | User's login                                   | required            |
| ```name```           | ```str```                        | User's name                                    | required            |
| ```profile```        | ```str```                        | User's profile                                 | required            |
| ```email```          | ```str```                        | User's email                                   | Not required        |             
| ```password```       | ```str```                        | User's password                                | Not required        |             
| ```organisation```   | ```str```                        | User's organisation                            | Not required        |             
| ```type```           | ```str```                        | User's type                                    | Not required        |             


### Output Organisation Profile

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```organisationId```   | ```str```                        | Organisation's ID                            | required        |             
| ```organisation```        | ```str```                        | Organisation                             | required            |
| ```profile```           | ```str```                    | Organisation's profile                                                | Not required            |


### Output User

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```_id```          | ```str```                        | User's id                                 | required            |
| ```_createdBy```           | ```str```                        | User's creator                                    | required            |
| ```_createdAt```        | ```int```                        | User's creation date                               | required            |
| ```login```          | ```str```                        | User's login                         | required        |             
| ```name```       | ```str```                        | User's name                                |  required        |             
| ```hasKey```   | ```bool```                        | ```True``` if the user has a key                            |  required        |             
| ```hasPassword```           | ```bool```                        | ```True``` if the user has a password                                  |  required        |
| ```hasMFA```           | ```bool```                        | ```True``` if the user has an MFA                                  |  required        |
| ```locked```           | ```bool```                        | ```True``` is the user is locked                                  |  required        |
| ```profile```           | ```str```                        | User's profile                                  |  required        |
| ```organisation```           | ```str```                        | User's organisation                                  |  required        |
| ```type```           | ```str```                        | User's type                                  |  required        |
| ```extraData```           | ```dict```                        | User's extra data                                  |  required        |    
| ```_updatedBy```           | ```str```                        | The user that updated the user                                  | Not required        |
| ```_updatedAt```           | ```int```                        | The user's update date                                 |  Not required        |
| ```email```           | ```str```                        | User's email                                  |  Not required        |
| ```permissions```           | ```List[str]```                        | User's permissions                                  |  Not required        |
| ```avatar```           | ```str```                        | User's avatar                                  |  Not required        |
| ```organisations```           | ```List[OutputOrganisationProfile]```                        | User's organisations                         |  Not required        |
| ```defaultOrganisation```           | ```str```                        | User's default organisation                                  | Not  required        |           


### Input Update User

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```name```           | ```str```                        | User's name                                    | required            |
| ```organisation```   | ```str```                        | User's organisation                            | Not required        |             
| ```profile```        | ```str```                        | User's profile                                 | required            |
| ```locked```           | ```bool```                        | ```True``` is the user is locked                                  |  Not required        |
| ```avatar```           | ```str```                        | User's avatar                                  |  Not required        |
| ```email```          | ```str```                        | User's email                                   | Not required        |             
| ```defaultOrganisation```           | ```str```                        | User's default organisation                                  | Not  required        |           
   

### Input User Organisation

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```organisation```   | ```str```                        | User's organisation                            | required        |             
| ```profile```        | ```str```                        | User's profile                                 | required            |
| ```default```           | ```bool```                    |                                                | Not required            |


### Output User Organisation

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```organisation```   | ```str```                        | User's organisation                            | required        |             
| ```profile```        | ```str```                        | User's profile                                 | required            |
| ```default```           | ```bool```                    |                                                | Not required            |