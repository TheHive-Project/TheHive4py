#Alert 

### Input Alert

**Parameters**

| Name                 | Type                             | Description                                    | Default             |
|----------------------|-----------------------           |------------------------------------------------|---------------------|
| ```type```           | ```str```                        | Alert's type. Default: None                    | required            |
| ```source```         | ```str```                        | Alert's source. Default: None                  | required            |              
| ```sourceRef```      | ```str```                        | Alert's source reference. Used to specify the unique identifier of the alert. Default: None                                                                                              | required            |
| ```title```          | ```str```                        | Alert's title. Default: None                   | required            |
| ```description```    | ```str```                        | Alert's description. Default: None             | required            |
| ```date```           | ```int```                        | Alert's occur date. Default: ```Now()```       | Not required        |
| ```externalLink```   | ```str```                        | Alert's external link. Used to easily navigate to the source of the alert. Default: None                                                                                                       | Not required        |
| ```severity```       | ```int```                        | Alert's severity: ```1```, ```2```, ```3```, ```4``` for ```LOW```, ```MEDIUM```, ```HIGH```, ```CRTICAL```. Default: ```2```                                                                | Not required        |  
| ```tags```           | ```List[str]```                  | List of alert tags. Default: ```[]```          | Not required        |
| ```flags```          | ```bool```                       | Alert's flag, ```True``` to mark the alert as important. Default: ```False```                                                                                                | Not required        |
| ```tlp```            | ```int```                        | Alert's TLP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2```                                                                   | Not required        |
| ```pap```            | ```int```                        | Alert's PAP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2```                                                                   | Not required        |
| ```customFields```   | ```List[InputCustomFieldValue]```| A set of CustomField instances, or the result of a ```CustomFieldHelper.build()``` method. Default: ```{}```                                                                                  | Not required        |
| ```summary```        | ```str```                        | Alert's summary                                | Not required        |
| ```status```         | ```str```                        | Alert's status                                 | Not required        |
| ```caseTemplate```   | ```str```                        | Alert template's name. Default: ```None```     | Not required        |
| ```observables```    | ```List[InputObservables]```     |                                                | Not required        | 

### Output Alert 

**Parameters**

| Name | Type | Description | Default |
|------|------|-------------|---------|
|```_id ```      |```str ```      |```The alert's id ```             |```required ```         |
|```_type ```      |```str ```      |``` ```             |```required ```         |
|```_createdBy ```      |```str ```      |```the profile that created the alert ```             |```required ```         |
|```_createdAt ```      |```int ```      |```The creation date of the alert ```             |```required ```         |
|```type ```      |```str ```      |``` ```             |```required ```         |
|```source ```      |```str ```      |``` ```             |```required ```         |
|```sourceRef ```      |```str ```      |``` ```             |```required ```         |
|```title ```      |```str ```      |``` ```             |```required ```         |
|```description ```      |```str ```      |``` ```             |```required ```         |
|```severity ```      |```int ```      |``` ```             |```required ```         |
|```date ```      |```int ```      |``` ```             |```required ```         |
|```tlp ```      |```int ```      |``` ```             |```required ```         |
|```pap ```      |```int ```      |``` ```             |```required ```         |
|```follow ```      |```bool ```      |``` ```             |```required ```         |
|```observableCount ```      |```int ```      |``` ```             |```required ```         |
|```status ```      |```str ```      |``` ```             |```required ```         |
|```stage ```      |```str ```      |``` ```             |```required ```         |
|```extraData ```      |```dict ```      |``` ```             |```required ```         |
|```newData ```      |```int ```      |``` ```             |```required ```         |
|```timeToDetect ```      |```int ```      |``` ```             |```required ```         |
|```_updatedBy ```      |```str ```      |``` ```             |```Not required ```         |
|```_updatedAt ```      |```int ```      |``` ```             |```Not required ```         |
|```externalLink ```      |```str ```      |``` ```             |```Not required ```         |
|```tags ```      |```List[str] ```      |``` ```             |```Not required ```         |
|```customFields ```      |```List[OutputCustomFieldValue] ```      |``` ```             |```Not required ```         |
|```caseTemplate ```      |```str ```      |``` ```             |```Not required ```         |
|```caseId ```      |```str ```      |``` ```             |```Not required ```         |
|```summary ```      |```str ```      |``` ```             |```Not required ```         |
|```inProgressDate ```      |```int ```      |``` ```             |```Not required ```         |
|```closeDate ```      |```int ```      |``` ```             |```Not required ```         |
|```importDate ```      |```int ```      |``` ```             |```Not required ```         |
|```timeToTriage ```      |```int ```      |``` ```             |```Not required ```         |
|```timeToQualify ```      |```int ```      |``` ```             |```Not required ```         |
|```timeToAcknowledge ```      |```int ```      |``` ```             |```Not required ```         |


### InputUpdateAlert

**Parameters**

| Name | Type | Description | Default |
|------|------|-------------|---------|
|```type ```      |```str ```      |``` ```             |```required ```         |
|```source ```      |```str ```      |``` ```             |```required ```         |
|```sourceRef ```      |```str ```      |``` ```             |```required ```         |
|```externalLink ```      |```str ```      |``` ```             |```required ```         |
|```title```      |```str ```      |``` ```             |```required ```         |
|```description ```      |```str ```      |``` ```             |```required ```         |
|```severity```      |```int ```      |``` ```             |```required ```         |
|```date```      |```int ```      |``` ```             |```required ```         |
|```lastSyncDate ```      |```int ```      |``` ```             |```required ```         |
|```tags```      |```List[str] ```      |``` ```             |```required ```         |
|```tlp ```      |```int ```      |``` ```             |```required ```         |
|```pap ```      |```int ```      |``` ```             |```required ```         |
|```follow ```      |```bool ```      |``` ```             |```required ```         |
|```customFields```      |```List[InputCustomFieldValue] ```      |``` ```             |```required ```         |
|```status ```      |```str ```      |``` ```             |```required ```         |
|```summary```      |```str ```      |``` ```             |```required ```         |
|```ids ```      |```List[str] ```      |```For Bulk update only ```             |```required ```         |


### InputPromoteAlert

**Parameters**

| Name | Type | Description | Default |
|------|------|-------------|---------|
|```title ```      |```str ```      |``` ```             |```required ```         |
|```description ```      |```str ```      |``` ```             |```required ```         |
|```severity```      |```int```      |``` ```             |```required ```         |
|```startDate ```      |```int```      |``` ```             |```required ```         |
|```endDate```      |```int```      |``` ```             |```required ```         |
|```tags ```      |```List[str]```      |``` ```             |```required ```         |
|```flag```      |```bool```      |``` ```             |```required ```         |
|```tlp```      |```int```      |``` ```             |```required ```         |
|```pap ```      |```int```      |``` ```             |```required ```         |
|```status```      |```str```      |``` ```             |```required ```         |
|```summary```      |```str```      |``` ```             |```required ```         |
|```assignee```      |```str```      |``` ```             |```required ```         |
|```customFields```      |```List[InputCustomFieldValue]```      |``` ```             |```required ```         |
|```caseTemplate```      |```str```      |``` ```             |```required ```         |
|```tasks```      |```List[InputTask]```      |``` ```             |```required ```         |
|```sharingParameters```      |```List[InputShare]```      |``` ```             |```required ```         |
|```taskRule```      |```str ```      |``` ```             |```required ```         |
|```observableRule```      |```str ```      |``` ```             |```required ```         |