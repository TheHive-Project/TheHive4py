# ObservableType


### Input Observable type

**Parameters**

| Name                 | Type                    | Description                                    | Default             |
|----------------------|-----------------------  |------------------------------------------------|---------------------|
| ```name```           | ```str```               | ObservableType's name                          | required            |
| ```isAttachment```   | ```bool```              | ```True``` to mark it as an attachment         | Not required        |


### Output Observable type

**Parameters**

| Name                 | Type                    | Description                                    | Default             |
|----------------------|-----------------------  |------------------------------------------------|---------------------|
| ```_id```           | ```str```               | ObservableType's id                          | required            |
| ```_type```           | ```str```               | ObservableType's type                          | required            |
| ```_createdBy```           | ```str```               | ObservableType's creator                         | required            |
| ```_createdAt```           | ```int```               | ObservableType's creation date                          | required            |
| ```name```           | ```str```               | ObservableType's name                          | required            |
| ```isAttachment```   | ```bool```              | ```True``` to mark it as an attachment         | required        |
| ```_updatedBy```           | ```str```               | The user that updated the observable type                         | Not required            |
| ```_updatedAt```           | ```int```               | ObservableType's update date                         | Not required            |