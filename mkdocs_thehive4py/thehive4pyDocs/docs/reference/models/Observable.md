# Observable


### Input Observable

**Parameters**


| Name                 | Type                    | Description                                    | Default             |
|----------------------|-----------------------  |------------------------------------------------|---------------------|
| ```dataType```         | ```str```             | Observable's data type                         | required            |
| ```data```             | ```str```             | Observable's data                              | required            |
| ```message```          | ```str```             | Observable's description                       | Not required        |
| ```StartDate```        | ```int```             | Observable's start date                        | Not required        |
| ```tlp```              | ```int```             | Observable's TLP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2```                                                          | Not required        |
| ```pap```              | ```int```             | Observable's PAP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2```                                                          | Not required        |
| ```tags```             | ```List[str]```       | List of observable tags                        | Not required        |
| ```ioc```              | ```bool```            | Observable's ioc flag, ```True``` to mark an observable as IOC. Default: ```False```                                                                                       | Not required        |
| ```sighted```          | ```bool```            | Observable's sighted flag, ```True``` to mark the observable as sighted. Default: ```False```                                                                                       | Not required        |
| ```sightedAt```        | ```int```             | The date of the observable's sighting          | Not required        |
| ```ignoreSimilarity``` | ```bool```            | Observable's similarity ignore flag. ```True``` to ignore the observable during similarity computing                                                                                         | Not required        |  
| ```isZip```            | ```bool```            | ```True``` to mark the observable a zip        | Not required        |
| ```zipPassword```      | ```bool```            | ```True``` to mark the password-protected zip  | Not required        |
| ```attachment```       | ```str```             | The observable's attachment                    | Not required        |


### Output Observable

**Parameters**

| Name                | Type                   | Description                                   | Default             |
|---------------------|------------------------|-----------------------------------------------|---------------------|
| ```_id```         | ```str```             | Observable's id                        | required            |
| ```_type```             | ```str```             | Observable's type                              | required            |
| ```_createdBy```          | ```str```             | The user that created the observable                       | required        |
| ```_createdAt```        | ```int```             | Observable's creation date                        | required        |
| ```datatype```             | ```str```       | Observable's datatype                        | required        |
| ```startDate```             | ```int```       | Observable's start date                       | required        |
| ```tlp```              | ```int```             | Observable's TLP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2```                                                          |  required        |
| ```pap```              | ```int```             | Observable's PAP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2```                                                          |  required        |
| ```ioc```              | ```bool```            | Observable's ioc flag, ```True``` to mark an observable as IOC. Default: ```False```                                                                                       |  required        |
| ```sighted```          | ```bool```            | Observable's sighted flag, ```True``` to mark the observable as sighted. Default: ```False```                                                                                       |  required        |
| ```reports```        | ```dict```             | Observable's reports          |  required        |
| ```extraData``` | ```dict```            | Observable's extraData                                                                                        |  required        |  
| ```ignoreSimilarity```            | ```bool```            | Ignore similar observables        | required        |
| ```_updatedBy```      | ```str```            | The user that updated the observable  | Not required        |
| ```_updatedAt```       | ```int```             | Observablel's update date                    | Not required        |
| ```data```       | ```str```             | The observable's data                    | Not required        |
| ```attachment```       | ```OutputAttachment```             | The observable's attachment                    | Not required        |
| ```tags```       | ```List[str]```             | The observable's tags                  | Not required        |
| ```sightedAt```       | ```int```             | The observable's sighted flag,  ```True``` to mark an observable as IOC. Default: ```False```                    | Not required        |
| ```message```       | ```str```             | The observable's message                  | Not required        |


### Input Update Observable

**Parameters**

| Name                | Type                   | Description                                   | Default             |
|---------------------|------------------------|-----------------------------------------------|---------------------|
| ```datatype```             | ```str```       | Observable's datatype                        | required        |
| ```message```       | ```str```             | The observable's message                  | required        |
| ```tlp```              | ```int```             | Observable's TLP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2```                                                          |  required        |
| ```pap```              | ```int```             | Observable's PAP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2```                                                          |  required        |
| ```tags```             | ```List[str]```       | List of observable tags                        |  required        |
| ```ioc```              | ```bool```            | Observable's ioc flag, ```True``` to mark an observable as IOC. Default: ```False```                                                                                       |  required        |
| ```sighted```          | ```bool```            | Observable's sighted flag, ```True``` to mark the observable as sighted. Default: ```False```                                                                                       |  required        |
| ```sightedAt```       | ```int```             | The observable's sighted flag,  ```True``` to mark an observable as IOC. Default: ```False```                    | required        |
| ```ignoreSimilarity```            | ```bool```            | Ignore similar observables        | required        |




