#Case

###CaseStatusValue

Possible values for the status of a case : ```New```, ```InProgress```, ```Indeterminate```, ```FalsePositive```, ```TruePositive```, ```Other```, ```Duplicated```.


### Input Case

**Parameters**

| Name                    | Type                             | Description                                    | Default             |
|-------------------------|-----------------------           |------------------------------------------------|---------------------|
| ```title```             | ```str```                        | Case's title. Default: None                    | required            |
| ```description```       | ```str```                        | Case's description. Default: None              | required            |
| ```severity```          | ```int```                        | Case's severity: ```1```, ```2```, ```3```, ```4``` for ```LOW```, ```MEDIUM```, ```HIGH```, ```CRTICAL```. Default: ```2```                                                                   | Not required        |  
| ```tags```              | ```List[str]```                  | List of case tags. Default: ```[]```           | Not required        |
| ```flags```             | ```bool```                       | Case's flag, ```True``` to mark the case as important. Default: ```False```                                                                                                   | Not required        |
| ```tlp```               | ```int```                        | Case's TLP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2```                                                                      | Not required        |
| ```pap```               | ```int```                        | Case's PAP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2```                                                                      | Not required        |
| ```status```            | ```CaseStatusValue```            | Case's status                                  | Not required        |
| ```summary```           | ```str```                        | Case's summary                                 | Not required        |
| ```assignee```          | ```str```                        | Case's assignee                                | Not required        |
| ```customFields```      | ```List[InputCustomFieldValue]```| A set of CustomField instances, or the result of a ```CustomFieldHelper.build()``` method. Default: ```{}```                                                                                 | Not required        |
| ```caseTemplate```      | ```str```                        | Case template's name. If specified then the case is created using the given template. Default: ```None```                                                                                 | Not required        |
| ```tasks```             | ```List[InputTask]```            | Set of tasks, defined as InputTask instances   | Not required        |
| ```sharingParameters``` | ```List[InoputShare]```          | Defined as InputShare instances                | Not required        |
| ```taskRule```          | ```str```                        |                                                | Not required        | 
| ```observablesRule```   | ```str```                        |                                                | Not required        | 


### Output Case

**Parameters**

| Name | Type | Description | Default |
|------|------|-------------|---------|
|```_id ```      |```str ```      |``` ```             |```required ```         |
|```_type ```      |```str ```      |``` ```             |```required ```         |
|```_createdBy ```      |```str ```      |```The profile that created the case ```             |```required ```         |
|```_createdAt ```      |```int```      |```The creation date of the case ```             |```required ```         |
|```number```      |```int```      |```The case's number ```             |```required ```         |
|```title ```      |```str```      |```The case's title ```             |```required ```         |
|```description ```      |```str```      |```The case's description ```             |```required ```         |
|```severity ```      |```int```      |```Case's severity: ```1```, ```2```, ```3```, ```4``` for ```LOW```, ```MEDIUM```, ```HIGH```, ```CRTICAL```. Default: ```2```             |```required ```         |
|```startDate```      |```int```      |```The case's start date ```             |```required ```         |
|```flag ```      |```bool```      |```Case's flag, ```True``` to mark the case as important. Default: ```False``` ```             |```required ```         |
|```tlp ```      |```int ```      |```Case's TLP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2```             |```required ```         |
|```pap ```      |```int ```      |```Case's PAP: ```0```, ```1```, ```2```, ```3``` for ```WHITE```, ```GREEN```, ```AMBER```, ```RED```. Default: ```2``` ```             |```required ```         |
|```status```      |```CaseStatusValue```      |```The case's status ```             |```required ```         |
|```stage ```      |```str ```      |``` ```             |```required ```         |
|```extraData```      |```dict```      |``` ```             |```required ```         |
|```newData```      |```int```      |``` ```             |```required ```         |
|```timeToDetect```      |```int```      |``` ```             |```required ```         |
|```_updatedBy```      |```str```      |```The profile that updated the case ```             |```Not required```         |
|```_updatedAt```      |```int ```      |```The date the case was updated ```             |```Not required```         |
|```endDate```      |```int ```      |```The case's end date ```             |```Not required ```         |
|```tags```      |```List[str] ```      |``` ```             |```Not required ```         |
|```summary ```      |```str```      |```Case's summary ```             |```Not required ```         |
|```impactStatus```      |```ImpactStatusValue```      |``` ```             |```Not required ```         |
|```assignee```      |```str ```      |```The profile(s) assigned to the case ```             |```Not required ```         |
|```customFields ```      |```List[OutputCustomFieldValue] ```      |``` ```             |```Not required ```         |
|```userPermissions```      |```List[str] ```      |``` ```             |```Not required ```         |
|```inProgressDate```      |```int```      |``` ```             |```Not required ```         |
|```closeDate```      |```int ```      |``` ```             |```Not required ```         |
|```alertDate```      |```int ```      |``` ```             |```Not required ```         |
|```alertNewDate```      |```int ```      |``` ```             |```Not required ```         |
|```alertInProgressDate```      |```int ```      |``` ```             |```Not required ```         |
|```alertImportedDate```      |```int ```      |``` ```             |```Not required ```         |
|```timeToTriage```      |```int ```      |``` ```             |```Not required ```         |
|```timeToQualify```      |```int ```      |``` ```             |```Not required ```         |
|```timeToAcknowledge ```      |```int ```      |``` ```             |```Not required ```         |
|```timeToResolve```      |```int ```      |``` ```             |```Not required ```         |
|```handlingDuration```      |```int ```      |``` ```             |```Not required ```         |