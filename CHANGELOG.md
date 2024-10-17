# Change Log

## [1.8.2](https://github.com/TheHive-Project/TheHive4py/tree/1.8.2) (2024-10-17)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.8.1...1.8.2)

**Deprecation:**

Add an overall warning about the deprecation and retirement of thehive4py 1.x library

## [1.8.1](https://github.com/TheHive-Project/TheHive4py/tree/1.8.1) (2021-01-13)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.8.0...1.8.1)

**Fixed bugs:**

- \[BUG\] Unable to create Alert [\#207](https://github.com/TheHive-Project/TheHive4py/issues/207)

**Closed issues:**

- \[Feature Request\] Add alert artifact methods, for TheHive 4 only [\#208](https://github.com/TheHive-Project/TheHive4py/issues/208)

## [1.8.0](https://github.com/TheHive-Project/TheHive4py/tree/1.8.0) (2020-11-27)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.7.2...1.8.0)

**Fixed bugs:**

- \[Bug\] With TheHive 4.0.1 thehive4py api.get\_case\_observables\(\) fails [\#198](https://github.com/TheHive-Project/TheHive4py/issues/198)
- Error updating alert artifact [\#195](https://github.com/TheHive-Project/TheHive4py/issues/195)
- typo error on api.py line 658 [\#173](https://github.com/TheHive-Project/TheHive4py/issues/173)
- Documentation mismatch on function return [\#165](https://github.com/TheHive-Project/TheHive4py/issues/165)
- Fix exception handling for merge\_alert\_into\_case [\#203](https://github.com/TheHive-Project/TheHive4py/pull/203) ([haam3r](https://github.com/haam3r))
- Issue \#173: corrected typo 'custom\_field.madatory' to 'custom\_field.mandatory' [\#188](https://github.com/TheHive-Project/TheHive4py/pull/188) ([fwalloe](https://github.com/fwalloe))

**Closed issues:**

- Query ContainsString not working [\#193](https://github.com/TheHive-Project/TheHive4py/issues/193)
- \[Bug\] Cannot create Case Observable on TheHive4 despite manageObservable Permission [\#179](https://github.com/TheHive-Project/TheHive4py/issues/179)
- Querying for Cases that Contain Substring in Custom Field [\#128](https://github.com/TheHive-Project/TheHive4py/issues/128)
- FR: Download file from task log [\#112](https://github.com/TheHive-Project/TheHive4py/issues/112)
- Add attachment download support [\#204](https://github.com/TheHive-Project/TheHive4py/issues/204)
- Add method to merge an alert into a case [\#197](https://github.com/TheHive-Project/TheHive4py/issues/197)
- Add support to ignoreSimilarity attribute [\#194](https://github.com/TheHive-Project/TheHive4py/issues/194)
- Missing function delete\_case\_task [\#190](https://github.com/TheHive-Project/TheHive4py/issues/190)
- \[Bug\] Get\_Case\_Template broken in TheHive 4 [\#183](https://github.com/TheHive-Project/TheHive4py/issues/183)
- Add support to alert.externalLink attribute [\#169](https://github.com/TheHive-Project/TheHive4py/issues/169)
- Create enumerations for enumerated data [\#161](https://github.com/TheHive-Project/TheHive4py/issues/161)
- Add find\_task\_logs function [\#160](https://github.com/TheHive-Project/TheHive4py/issues/160)
- Add PAP field to alert [\#159](https://github.com/TheHive-Project/TheHive4py/issues/159)
- Add find\_observables method [\#157](https://github.com/TheHive-Project/TheHive4py/issues/157)
- Allow passing in file-like objects to alert artifacts [\#136](https://github.com/TheHive-Project/TheHive4py/issues/136)
- Allow file observable creation from memory [\#35](https://github.com/TheHive-Project/TheHive4py/issues/35)

**Merged pull requests:**

- Fixed typo in explanation part of some functions in query.py [\#199](https://github.com/TheHive-Project/TheHive4py/pull/199) ([fwalloe](https://github.com/fwalloe))
- Get case observable function [\#206](https://github.com/TheHive-Project/TheHive4py/pull/206) ([jeffrey-e](https://github.com/jeffrey-e))
- Add method to delete alert [\#202](https://github.com/TheHive-Project/TheHive4py/pull/202) ([haam3r](https://github.com/haam3r))
- Make get\_task\_logs\(\) use 'api/case/task/log/\_search/'  [\#200](https://github.com/TheHive-Project/TheHive4py/pull/200) ([jnahorny](https://github.com/jnahorny))
- Use dict key lookup instead of hasattr [\#196](https://github.com/TheHive-Project/TheHive4py/pull/196) ([Kamforka](https://github.com/Kamforka))
- Implement case task deletion via patch request [\#191](https://github.com/TheHive-Project/TheHive4py/pull/191) ([gelim](https://github.com/gelim))
- Add delete\_case\_observable method to api [\#189](https://github.com/TheHive-Project/TheHive4py/pull/189) ([p-tekh](https://github.com/p-tekh))
- Added MISP export functionality [\#187](https://github.com/TheHive-Project/TheHive4py/pull/187) ([emalderson](https://github.com/emalderson))
- Adding externalLink to Alert model [\#181](https://github.com/TheHive-Project/TheHive4py/pull/181) ([milesflo](https://github.com/milesflo))
- Get alert with similarities [\#172](https://github.com/TheHive-Project/TheHive4py/pull/172) ([dainok](https://github.com/dainok))
- Add find\_observables [\#171](https://github.com/TheHive-Project/TheHive4py/pull/171) ([dainok](https://github.com/dainok))
- Fix documentation mismatch on api.find\_first TheHive-Project/TheHive4py\#165 [\#166](https://github.com/TheHive-Project/TheHive4py/pull/166) ([haam3r](https://github.com/haam3r))
- Merge alert to case [\#164](https://github.com/TheHive-Project/TheHive4py/pull/164) ([haam3r](https://github.com/haam3r))
- Pass in file-like objects for case observables [\#135](https://github.com/TheHive-Project/TheHive4py/pull/135) ([jaredjennings](https://github.com/jaredjennings))

## [1.7.2](https://github.com/TheHive-Project/TheHive4py/tree/1.7.2) (2020-06-24)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.7.1...1.7.2)

**Fixed bugs:**

- Fix the constructor of TheHiveApi class [\#170](https://github.com/TheHive-Project/TheHive4py/issues/170)
- NameError: name 'requests' is not defined [\#163](https://github.com/TheHive-Project/TheHive4py/issues/163)

**Merged pull requests:**

- Importing requests module [\#168](https://github.com/TheHive-Project/TheHive4py/pull/168) ([gaglimax](https://github.com/gaglimax))

## [1.7.1](https://github.com/TheHive-Project/TheHive4py/tree/1.7.1) (2020-06-04)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.7.0...1.7.1)

**Fixed bugs:**

- Not able to create Case Observable [\#162](https://github.com/TheHive-Project/TheHive4py/issues/162)

**Merged pull requests:**

- Add id for case template [\#140](https://github.com/TheHive-Project/TheHive4py/pull/140) ([golaso](https://github.com/golaso))

## [1.7.0](https://github.com/TheHive-Project/TheHive4py/tree/1.7.0) (2020-05-29)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.6.0...1.7.0)

**Implemented enhancements:**

- Add custom field support for new types [\#152](https://github.com/TheHive-Project/TheHive4py/issues/152)
- Return type is not correctly filled [\#150](https://github.com/TheHive-Project/TheHive4py/issues/150)
- Models Case and CaseTemplate don't have PAP attribute [\#127](https://github.com/TheHive-Project/TheHive4py/issues/127)
- Improve jsonify function to allow excluding attributes [\#125](https://github.com/TheHive-Project/TheHive4py/issues/125)

**Fixed bugs:**

- Add support to datetime for "date" CustomFields [\#138](https://github.com/TheHive-Project/TheHive4py/issues/138)
- Update alert using 'fields' is not working [\#130](https://github.com/TheHive-Project/TheHive4py/issues/130)
- Models should have the attribute 'id' [\#120](https://github.com/TheHive-Project/TheHive4py/issues/120)
- promote\_alert\_to\_case\(\) doesn't apply caseTemplate [\#114](https://github.com/TheHive-Project/TheHive4py/issues/114)
- PAP flag missing when creating a case from a retrieved Case object [\#111](https://github.com/TheHive-Project/TheHive4py/issues/111)
- Specify an optional case template parameter to promote\_alert\_to\_case [\#115](https://github.com/TheHive-Project/TheHive4py/pull/115) ([agix](https://github.com/agix))

**Closed issues:**

- FR: Allow specifying a custom `date` value for Alerts [\#151](https://github.com/TheHive-Project/TheHive4py/issues/151)
- FR: Get "task name" in an "case\_task\_log" event [\#148](https://github.com/TheHive-Project/TheHive4py/issues/148)
- Create case with the hive 4 rc1 [\#144](https://github.com/TheHive-Project/TheHive4py/issues/144)
- Is TheHive4py still alive? [\#141](https://github.com/TheHive-Project/TheHive4py/issues/141)
- support for case template deletion/creation [\#124](https://github.com/TheHive-Project/TheHive4py/issues/124)
- Example python create case with observables [\#113](https://github.com/TheHive-Project/TheHive4py/issues/113)
- Unable to create new case from existing case data [\#110](https://github.com/TheHive-Project/TheHive4py/issues/110)
- Alert create error: \('Connection aborted.', error\(104, 'Connection reset by peer'\) [\#109](https://github.com/TheHive-Project/TheHive4py/issues/109)
- Requesting analyzer report from cortex with thehive4py [\#107](https://github.com/TheHive-Project/TheHive4py/issues/107)
- Update\_Case not updating Case Severity [\#100](https://github.com/TheHive-Project/TheHive4py/issues/100)
- Add support to multi tenancy [\#154](https://github.com/TheHive-Project/TheHive4py/issues/154)
- Add support to like and wildcard operators [\#149](https://github.com/TheHive-Project/TheHive4py/issues/149)
- Add ioc and sighted attributes to case and alert artifacts [\#126](https://github.com/TheHive-Project/TheHive4py/issues/126)
- Create update\_case\_observable [\#121](https://github.com/TheHive-Project/TheHive4py/issues/121)

**Merged pull requests:**

- Add support for case delete, creating custom fields and create case templates [\#146](https://github.com/TheHive-Project/TheHive4py/pull/146) ([aurelienhess](https://github.com/aurelienhess))
- Support for json datetime [\#139](https://github.com/TheHive-Project/TheHive4py/pull/139) ([ehooo](https://github.com/ehooo))
- Added IDs in all models [\#123](https://github.com/TheHive-Project/TheHive4py/pull/123) ([mgabriel-silva](https://github.com/mgabriel-silva))
- Added update\_case\_observable [\#122](https://github.com/TheHive-Project/TheHive4py/pull/122) ([mgabriel-silva](https://github.com/mgabriel-silva))
- Added support for custom owner on Case creation [\#118](https://github.com/TheHive-Project/TheHive4py/pull/118) ([victorvillar](https://github.com/victorvillar))

## [1.6.0](https://github.com/TheHive-Project/TheHive4py/tree/1.6.0) (2018-12-17)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.5.3...1.6.0)

**Merged pull requests:**

- Implement some more functions [\#96](https://github.com/TheHive-Project/TheHive4py/pull/96) ([jojoob](https://github.com/jojoob))
- Create new sample bulk-alert-merge-to-case.py [\#95](https://github.com/TheHive-Project/TheHive4py/pull/95) ([david-burkett](https://github.com/david-burkett))
- Update observable [\#94](https://github.com/TheHive-Project/TheHive4py/pull/94) ([joseluratm](https://github.com/joseluratm))

## [1.5.3](https://github.com/TheHive-Project/TheHive4py/tree/1.5.3) (2018-11-16)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.5.2...1.5.3)

**Fixed bugs:**

- Unable to close case as TruePositive WithImpact [\#93](https://github.com/TheHive-Project/TheHive4py/issues/93)

## [1.5.2](https://github.com/TheHive-Project/TheHive4py/tree/1.5.2) (2018-11-12)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.5.1...1.5.2)

**Fixed bugs:**

- Support task-groups for tasks \(e.g. creation of Cases\) [\#91](https://github.com/TheHive-Project/TheHive4py/issues/91)

**Closed issues:**

- Unknown attribute alert.customFields when creating alert in version 1.5.1 [\#88](https://github.com/TheHive-Project/TheHive4py/issues/88)

**Merged pull requests:**

- support for task group names [\#92](https://github.com/TheHive-Project/TheHive4py/pull/92) ([crackytsi](https://github.com/crackytsi))

## [1.5.1](https://github.com/TheHive-Project/TheHive4py/tree/1.5.1) (2018-10-10)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.5.0...1.5.1)

**Implemented enhancements:**

- Add customFields to Alert [\#87](https://github.com/TheHive-Project/TheHive4py/pull/87) ([zpriddy](https://github.com/zpriddy))

## [1.5.0](https://github.com/TheHive-Project/TheHive4py/tree/1.5.0) (2018-09-25)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.4.4...1.5.0)

**Closed issues:**

- Update observable [\#7](https://github.com/TheHive-Project/TheHive4py/issues/7)
- Update task [\#6](https://github.com/TheHive-Project/TheHive4py/issues/6)
- Add a simple template search method [\#83](https://github.com/TheHive-Project/TheHive4py/issues/83)
- Max recursion depth exceeded error [\#82](https://github.com/TheHive-Project/TheHive4py/issues/82)

**Merged pull requests:**

- Feature/promote alert to case [\#86](https://github.com/TheHive-Project/TheHive4py/pull/86) ([uplateandonline](https://github.com/uplateandonline))
- Feature/search templates [\#84](https://github.com/TheHive-Project/TheHive4py/pull/84) ([uplateandonline](https://github.com/uplateandonline))
- Prevent max recursion depth exceeded error [\#80](https://github.com/TheHive-Project/TheHive4py/pull/80) ([Psynbiotik](https://github.com/Psynbiotik))
- added search support for tasks [\#79](https://github.com/TheHive-Project/TheHive4py/pull/79) ([neok0](https://github.com/neok0))

## [1.4.4](https://github.com/TheHive-Project/TheHive4py/tree/1.4.4) (2018-07-02)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.4.3...1.4.4)

**Fixed bugs:**

- Missing parameter \_field in Between function [\#71](https://github.com/TheHive-Project/TheHive4py/pull/71) ([tagashy](https://github.com/tagashy))

**Closed issues:**

- xsrf-token in theHive4py [\#76](https://github.com/TheHive-Project/TheHive4py/issues/76)
- Retrieve analyzer report after analysis \[question\] [\#75](https://github.com/TheHive-Project/TheHive4py/issues/75)
- Keep analyzer reports when merging a case [\#73](https://github.com/TheHive-Project/TheHive4py/issues/73)
- find\_cases query on custom field \(for template cases\) [\#72](https://github.com/TheHive-Project/TheHive4py/issues/72)
- Unify the naming of statuses and filters [\#70](https://github.com/TheHive-Project/TheHive4py/issues/70)
- How can I automate case creation using email? [\#68](https://github.com/TheHive-Project/TheHive4py/issues/68)
- Searching For Cases [\#78](https://github.com/TheHive-Project/TheHive4py/issues/78)

**Merged pull requests:**

- Add support for alert markAsRead/Unread [\#74](https://github.com/TheHive-Project/TheHive4py/pull/74) ([itsnotapt](https://github.com/itsnotapt))
- Add Support for update\_case\_tasks method [\#63](https://github.com/TheHive-Project/TheHive4py/pull/63) ([billmurrin](https://github.com/billmurrin))

## [1.4.3](https://github.com/TheHive-Project/TheHive4py/tree/1.4.3) (2018-02-07)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.4.2...1.4.3)

**Implemented enhancements:**

- add update\_alert to allow updating an alert [\#61](https://github.com/TheHive-Project/TheHive4py/pull/61) ([Rolinh](https://github.com/Rolinh))

**Fixed bugs:**

- How to close a case via API [\#67](https://github.com/TheHive-Project/TheHive4py/issues/67)
- CustomFields are not updated in update\_case [\#66](https://github.com/TheHive-Project/TheHive4py/issues/66)
- Correction in update\_case usage [\#57](https://github.com/TheHive-Project/TheHive4py/issues/57)

**Closed issues:**

- is there any method for create automatic alert when there's incoming email  [\#65](https://github.com/TheHive-Project/TheHive4py/issues/65)
- Query for creating alert  [\#56](https://github.com/TheHive-Project/TheHive4py/issues/56)

**Merged pull requests:**

- fix spelling of exception [\#58](https://github.com/TheHive-Project/TheHive4py/pull/58) ([billmurrin](https://github.com/billmurrin))
- created get\_linked\_cases method in api [\#60](https://github.com/TheHive-Project/TheHive4py/pull/60) ([billmurrin](https://github.com/billmurrin))

## [1.4.2](https://github.com/TheHive-Project/TheHive4py/tree/1.4.2) (2017-12-27)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.4.1...1.4.2)

**Implemented enhancements:**

- Raise custom exceptions from api methods instead of calling sys.exit [\#55](https://github.com/TheHive-Project/TheHive4py/issues/55)

**Closed issues:**

- Support several small functions in TheHive4py [\#47](https://github.com/TheHive-Project/TheHive4py/issues/47)

**Merged pull requests:**

- Add Sighted Support to the Observable Model [\#54](https://github.com/TheHive-Project/TheHive4py/pull/54) ([billmurrin](https://github.com/billmurrin))

## [1.4.1](https://github.com/TheHive-Project/TheHive4py/tree/1.4.1) (2017-12-19)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.4.0...1.4.1)

**Merged pull requests:**

- fix get\_case\_observables method [\#53](https://github.com/TheHive-Project/TheHive4py/pull/53) ([billmurrin](https://github.com/billmurrin))

## [1.4.0](https://github.com/TheHive-Project/TheHive4py/tree/1.4.0) (2017-12-05)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.3.1...1.4.0)

**Implemented enhancements:**

- Provide just the template name when creating a case from a template [\#45](https://github.com/TheHive-Project/TheHive4py/issues/45)
- Add support of custom fields to the case model [\#39](https://github.com/TheHive-Project/TheHive4py/issues/39)
- Case helper [\#37](https://github.com/TheHive-Project/TheHive4py/pull/37) ([npratley](https://github.com/npratley))

**Fixed bugs:**

- Error updating case [\#51](https://github.com/TheHive-Project/TheHive4py/issues/51)

**Closed issues:**

- Add a query builder capabilities [\#49](https://github.com/TheHive-Project/TheHive4py/issues/49)
- Run Cortex analyzer through api [\#40](https://github.com/TheHive-Project/TheHive4py/issues/40)
- Update case [\#5](https://github.com/TheHive-Project/TheHive4py/issues/5)

**Merged pull requests:**

- Added missing attributes to the Case class. [\#50](https://github.com/TheHive-Project/TheHive4py/pull/50) ([npratley](https://github.com/npratley))
- Added the functionality to run a Cortex analyzer on an observable [\#44](https://github.com/TheHive-Project/TheHive4py/pull/44) ([alexgoedeke](https://github.com/alexgoedeke))
- Added get\_task\_logs method [\#42](https://github.com/TheHive-Project/TheHive4py/pull/42) ([billmurrin](https://github.com/billmurrin))
- Added a method to update a case. [\#41](https://github.com/TheHive-Project/TheHive4py/pull/41) ([npratley](https://github.com/npratley))

## [1.3.1](https://github.com/TheHive-Project/TheHive4py/tree/1.3.1) (2017-09-17)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.3.0...1.3.1)

**Fixed bugs:**

- Basic auth doesn't work with version 1.3.0 [\#38](https://github.com/TheHive-Project/TheHive4py/issues/38)

## [1.3.0](https://github.com/TheHive-Project/TheHive4py/tree/1.3.0) (2017-09-15)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.2.3...1.3.0)

**Implemented enhancements:**

- Allow specifying range to return \> 10 cases, observables, etc., [\#30](https://github.com/TheHive-Project/TheHive4py/issues/30)
- fix two cases of bad indentation in exception handling code [\#26](https://github.com/TheHive-Project/TheHive4py/pull/26) ([Rolinh](https://github.com/Rolinh))
- fix default severity level of an alert [\#25](https://github.com/TheHive-Project/TheHive4py/pull/25) ([Rolinh](https://github.com/Rolinh))

**Fixed bugs:**

- certificate verify option not included in create\_case\_task [\#27](https://github.com/TheHive-Project/TheHive4py/issues/27)

**Closed issues:**

- Add an API method to create users [\#33](https://github.com/TheHive-Project/TheHive4py/issues/33)
- Feature Request - Task Log Template/Boilerplate Text [\#32](https://github.com/TheHive-Project/TheHive4py/issues/32)
- Case model is missing the required `status` attribute [\#29](https://github.com/TheHive-Project/TheHive4py/issues/29)
- Add support to authentication by API key [\#36](https://github.com/TheHive-Project/TheHive4py/issues/36)
- Add a find\_alerts method to search for alerts [\#31](https://github.com/TheHive-Project/TheHive4py/issues/31)

**Merged pull requests:**

- Added verify parameter to calls [\#28](https://github.com/TheHive-Project/TheHive4py/pull/28) ([billmurrin](https://github.com/billmurrin))

## [1.2.3](https://github.com/TheHive-Project/TheHive4py/tree/1.2.3) (2017-07-20)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.2.2...1.2.3)

**Implemented enhancements:**

- Adding option for an Internal CA  [\#24](https://github.com/TheHive-Project/TheHive4py/issues/24)

**Merged pull requests:**

- Find first [\#23](https://github.com/TheHive-Project/TheHive4py/pull/23) ([3c7](https://github.com/3c7))

## [1.2.2](https://github.com/TheHive-Project/TheHive4py/tree/1.2.2) (2017-07-06)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.2.1...1.2.2)

**Fixed bugs:**

- Remove print calls from TheHiveApi.find\_cases method [\#22](https://github.com/TheHive-Project/TheHive4py/issues/22)

## [1.2.1](https://github.com/TheHive-Project/TheHive4py/tree/1.2.1) (2017-06-29)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.2.0...1.2.1)

**Fixed bugs:**

- Fix the issue related to wrong base64 decoding when creating alerts [\#20](https://github.com/TheHive-Project/TheHive4py/issues/20)
- python-magic dependency not in setup.py [\#19](https://github.com/TheHive-Project/TheHive4py/issues/19)
- "future" dependency not documented in requirements.txt [\#18](https://github.com/TheHive-Project/TheHive4py/issues/18)

**Merged pull requests:**

- Install python-magic package on setup [\#16](https://github.com/TheHive-Project/TheHive4py/pull/16) ([ilyaglow](https://github.com/ilyaglow))

## [1.2.0](https://github.com/TheHive-Project/TheHive4py/tree/1.2.0) (2017-05-12)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.1.1...1.2.0)

**Closed issues:**

- Add the ability to create a TheHive alert [\#13](https://github.com/TheHive-Project/TheHive4py/issues/13)

**Merged pull requests:**

- Added ability to find tasks by caseId [\#11](https://github.com/TheHive-Project/TheHive4py/pull/11) ([AverageS](https://github.com/AverageS))

## [1.1.1](https://github.com/TheHive-Project/TheHive4py/tree/1.1.1) (2017-05-11)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.1.0...1.1.1)

**Fixed bugs:**

- Use basic auth when calling TheHive apis [\#14](https://github.com/TheHive-Project/TheHive4py/issues/14)

## [1.1.0](https://github.com/TheHive-Project/TheHive4py/tree/1.1.0) (2017-03-23)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.0.1...1.1.0)

**Implemented enhancements:**

- Search for cases [\#4](https://github.com/TheHive-Project/TheHive4py/issues/4)
- Add observables to a case [\#3](https://github.com/TheHive-Project/TheHive4py/issues/3)

## [1.0.1](https://github.com/TheHive-Project/TheHive4py/tree/1.0.1) (2017-03-08)
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/1.0.0...1.0.1)

**Fixed bugs:**

- Issue creating a cases without metrics and without case template [\#8](https://github.com/TheHive-Project/TheHive4py/issues/8)

## [1.0.0](https://github.com/TheHive-Project/TheHive4py/tree/1.0.0) (2017-03-08)
**Closed issues:**

- 2nd typo in setup.py [\#2](https://github.com/TheHive-Project/TheHive4py/issues/2)
- Typo in setup.py [\#1](https://github.com/TheHive-Project/TheHive4py/issues/1)



\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*