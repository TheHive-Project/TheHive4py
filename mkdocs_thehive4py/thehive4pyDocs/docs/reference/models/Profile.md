# Profile


### Input Profile

**Parameters**


| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```name```           | ```str```                        | Profile's name                                 | required            |
| ```permissions```    | ```List[str]```                  | List of profile's permissions                  | Not required        |


### Output Profile

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```_id```      | ```str```                        | Profile's id                    | required            |
| ```_type```    | ```str```                        | Profile's type                       |  required        |             
| ```_createdAt```         | ```int```                        | Profile's creation date                             | required            |
| ```_createdBy```      | ```str```                        | Profile's creator                            | required            |
| ```name```    | ```str```                        | Profile's name                     | required        |             
| ```editable```    | ```bool```                        | ```True``` to make the profile editable                       |  required        |             
| ```isAdmin```    | ```bool```                        | ```True``` to make the profile as an admin                    | required        |             
| ```_updatedAt```    | ```int```                        | Profile's updated date                        | Not required        |             
| ```_updatedBy```    | ```str```                        | The user that updated the profile                       | Not required        |             
| ```permissions```    | ```List[str]```                        | Profile's permissions                        | Not required        |             


### Input Update Profile

**Parameters**


| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```name```           | ```str```                        | Profile's name  to update                               | required            |
| ```permissions```    | ```List[str]```                  | List of profile's permissions to update                  | Not required        |