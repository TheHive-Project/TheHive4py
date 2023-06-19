# Procedure

### Input Procedure

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```occurDate```      | ```int```                        | Procedure occurence date                       | required            |
| ```tactic```         | ```str```                        | Procedure's tactic                             | required            |
| ```patternId```      | ```str```                        | Procedure's pattern                            | required            |
| ```description```    | ```str```                        | Procedure's description                        | Not required        |             


### Output Procedure

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```_id```      | ```str```                        | Procedure's id                    | required            |
| ```_createdAt```         | ```int```                        | Procedure's creation date                             | required            |
| ```_createdBy```      | ```str```                        | Procedure's creator                            | required            |
| ```occurDate```    | ```int```                        | Procedure's occur date                        |  required        |             
| ```tactic```    | ```str```                        | Procedure's tactic                       | required        |             
| ```tacticLabel```    | ```str```                        | Procedure's tactiv labled                        |  required        |             
| ```extraData```    | ```dict```                        | Procedure's extra data                       | required        |             
| ```_updatedAt```    | ```int```                        | Procedure's updated date                        | Not required        |             
| ```_updatedBy```    | ```str```                        | The user that updated the procedure                       | Not required        |             
| ```description```    | ```str```                        | Procedure's description                        | Not required        |             
| ```patternId```    | ```str```                        | Procedure's pattern ID                       | Not required        |             
| ```patternName```    | ```str```                        | Procedure's pattern name                        | Not required        |             


### Input Update Procedure

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```description```         | ```str```                        | Procedure's description to update                             | required            |
| ```occurDate```      | ```int```                        | Procedure occurence date                       | required            |