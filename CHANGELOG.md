# Change Log

## [1.4.2](https://github.com/TheHive-Project/TheHive4py/tree/1.4.2) (2017-12-27)

[1.4.2](https://github.com/TheHive-Project/TheHive4py/compare/1.4.1...1.4.2)

**Implemented enhancements:**

- Raise custom exceptions from api methods instead of calling sys.exit [\#55](https://github.com/TheHive-Project/TheHive4py/issues/55)

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
