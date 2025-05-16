[//]: # (Style hack to limit ToC depth as it is not supported via in-file configuration)
[//]: # (More details: https://github.com/squidfunk/mkdocs-material/discussions/2532)
<style>
  .md-sidebar--secondary .md-nav__list .md-nav__list {
    display: none
  }
</style>

## 2.0.0b10 (2025-05-13)
### Removed
* [#401](https://github.com/TheHive-Project/TheHive4py/issues/401) - Remove support for python 3.8 by [@Kamforka](https://github.com/Kamforka) in [#407](https://github.com/TheHive-Project/TheHive4py/pull/407)
### Fixed
* [#410](https://github.com/TheHive-Project/TheHive4py/issues/410) - Review and fix alert docs by [@Kamforka](https://github.com/Kamforka) in [#412](https://github.com/TheHive-Project/TheHive4py/pull/412)
* [#417](https://github.com/TheHive-Project/TheHive4py/issues/417) - consider empty dicts in json requests by [@Kamforka](https://github.com/Kamforka) in [#418](https://github.com/TheHive-Project/TheHive4py/pull/418)
### Other
* [#411](https://github.com/TheHive-Project/TheHive4py/issues/411) - Fix changelog linkification script by [@Kamforka](https://github.com/Kamforka) in [#413](https://github.com/TheHive-Project/TheHive4py/pull/413)
* [#408](https://github.com/TheHive-Project/TheHive4py/issues/408) - Use TheHive 5.4.8 in integration tests by [@Kamforka](https://github.com/Kamforka) in [#409](https://github.com/TheHive-Project/TheHive4py/pull/409)
* [#414](https://github.com/TheHive-Project/TheHive4py/issues/414) - Use TheHive v5.4.9 in integration tests by [@Kamforka](https://github.com/Kamforka) in [#415](https://github.com/TheHive-Project/TheHive4py/pull/415)
* [#419](https://github.com/TheHive-Project/TheHive4py/issues/419) - Use TheHive v5.5.1 in integration tests by [@Kamforka](https://github.com/Kamforka) in [#421](https://github.com/TheHive-Project/TheHive4py/pull/421)


**Full Changelog**: [2.0.0b9...2.0.0b10](https://github.com/TheHive-Project/TheHive4py/compare/2.0.0b9...2.0.0b10)

## 2.0.0b9 (2025-02-25)
### Added
* [#390](https://github.com/TheHive-Project/TheHive4py/issues/390) - Extend CaseEndpoint with apply_case_template method by [@Kamforka](https://github.com/Kamforka) in [#391](https://github.com/TheHive-Project/TheHive4py/pull/391)
* [#354](https://github.com/TheHive-Project/TheHive4py/issues/354) - Add case endpoint docstrings by [@Kamforka](https://github.com/Kamforka) in [#399](https://github.com/TheHive-Project/TheHive4py/pull/399)
* [#355](https://github.com/TheHive-Project/TheHive4py/issues/355) - Add changelog to docs by [@Kamforka](https://github.com/Kamforka) in [#400](https://github.com/TheHive-Project/TheHive4py/pull/400)
### Removed
* [#398](https://github.com/TheHive-Project/TheHive4py/issues/398) - Remove `update_share` method from case endpoint by [@Kamforka](https://github.com/Kamforka) in [#402](https://github.com/TheHive-Project/TheHive4py/pull/402)
### Fixed
* [#388](https://github.com/TheHive-Project/TheHive4py/issues/388) - Enhance session's error parse method by [@Kamforka](https://github.com/Kamforka) in [#393](https://github.com/TheHive-Project/TheHive4py/pull/393)
* [#389](https://github.com/TheHive-Project/TheHive4py/issues/389) - Fix types.cortex.OutputAnalyzerJob by [@Kamforka](https://github.com/Kamforka) in [#392](https://github.com/TheHive-Project/TheHive4py/pull/392)
* [#395](https://github.com/TheHive-Project/TheHive4py/issues/395) - Fix InputAnalyzerJob type and add regression test by [@JuanTecedor](https://github.com/JuanTecedor) in [#397](https://github.com/TheHive-Project/TheHive4py/pull/397)
### Other
* [#386](https://github.com/TheHive-Project/TheHive4py/issues/386) - Use TheHive 5.4.7 in integration tests by [@Kamforka](https://github.com/Kamforka) in [#387](https://github.com/TheHive-Project/TheHive4py/pull/387)
* [#354](https://github.com/TheHive-Project/TheHive4py/issues/354) - Add case endpoint docs by [@Kamforka](https://github.com/Kamforka) in [#394](https://github.com/TheHive-Project/TheHive4py/pull/394)


**Full Changelog**: [2.0.0b8...2.0.0b9](https://github.com/TheHive-Project/TheHive4py/compare/2.0.0b8...2.0.0b9)

## 2.0.0b8 (2025-01-15)

### Added
*  [#376](https://github.com/TheHive-Project/TheHive4py/issues/376) - Add `Has` query filter and fix deprecations, add warning for `Contains` filter by [@JuanTecedor](https://github.com/JuanTecedor) in [#377](https://github.com/TheHive-Project/TheHive4py/pull/377)
*  [#374](https://github.com/TheHive-Project/TheHive4py/issues/374) - Add new endpoint to be able to manage case templates by [@Anko59](https://github.com/Anko59) in [#375](https://github.com/TheHive-Project/TheHive4py/pull/375)

### Changed
*  [#370](https://github.com/TheHive-Project/TheHive4py/issues/370) - Enhance cortex endpoint with additional methods and types by [@Anko59](https://github.com/Anko59) in [#371](https://github.com/TheHive-Project/TheHive4py/pull/371)
*  [#376](https://github.com/TheHive-Project/TheHive4py/issues/376) - Fix outdated query filters to address corresponding TheHive warnings by [@JuanTecedor](https://github.com/JuanTecedor) in [#377](https://github.com/TheHive-Project/TheHive4py/pull/377)
*  [#380](https://github.com/TheHive-Project/TheHive4py/issues/380) - Update case and alert endpoint types by [@Kamforka](https://github.com/Kamforka) in [#383](https://github.com/TheHive-Project/TheHive4py/pull/383)

### Deprecated
*  [#361](https://github.com/TheHive-Project/TheHive4py/issues/361) - Add deprecation warning for python 3.8 by [@Kamforka](https://github.com/Kamforka) in [#384](https://github.com/TheHive-Project/TheHive4py/pull/384)
*  [#376](https://github.com/TheHive-Project/TheHive4py/issues/376) - Deprecate `Contains` query filter in favour of `Has` by [@JuanTecedor](https://github.com/JuanTecedor) in [#377](https://github.com/TheHive-Project/TheHive4py/pull/377)

### Other
*  [#362](https://github.com/TheHive-Project/TheHive4py/issues/362) - Add release.yml to better control auto generated release notes by [@Kamforka](https://github.com/Kamforka) in [#379](https://github.com/TheHive-Project/TheHive4py/pull/379)
*  [#372](https://github.com/TheHive-Project/TheHive4py/issues/372) - Use TheHive 5.4.5 in integration tests by [@Kamforka](https://github.com/Kamforka) in [#373](https://github.com/TheHive-Project/TheHive4py/pull/373)
*  [#381](https://github.com/TheHive-Project/TheHive4py/issues/381) - Use TheHive 5.4.6 in integration tests by [@Kamforka](https://github.com/Kamforka) in [#382](https://github.com/TheHive-Project/TheHive4py/pull/382)

### New Contributors
* [@Anko59](https://github.com/Anko59) made their first contribution in [#371](https://github.com/TheHive-Project/TheHive4py/pull/371)
* [@JuanTecedor](https://github.com/JuanTecedor) made their first contribution in [#377](https://github.com/TheHive-Project/TheHive4py/pull/377)

**Full Changelog**: [2.0.0b7...2.0.0b8](https://github.com/TheHive-Project/TheHive4py/compare/2.0.0b7...2.0.0b8)

## 2.0.0b7 (2024-11-24)

### Breaking changes
* `TheHiveApi` client's `verify` argument was improperly set to the default value of `None`, which only raised a warning when the client was connecting to a TheHive instance with an `https://` base url. From now on `verify` will default to `True` that might lead to an SSL verification error, so to fix that one can:
  
    - pass the path to the cert bundle to be used by the client, e.g.: `verify=/path/to/cert/bundle.crt`
    - export the `REQUESTS_CA_BUNDLE` with the cert bundle path, e.g.: `REQUESTS_CA_BUNDLE=/path/to/cert/bundle.crt`
    - disable SSL verification like before - not recommended - e.g.: `verify=None`
 
### Deprecated
* [TheHiveApi.case.update](https://github.com/TheHive-Project/TheHive4py/blob/b3162f695368aefe200740acebd157dfba503e23/thehive4py/endpoints/case.py#L43) method's `case` argument is going to be retired in favor of the `fields` argument to conform with other endpoints update methods.

### Added
*  [#339](https://github.com/TheHive-Project/TheHive4py/issues/339) - add codecov action by [@Kamforka](https://github.com/Kamforka) in [#342](https://github.com/TheHive-Project/TheHive4py/pull/342)
*  [#339](https://github.com/TheHive-Project/TheHive4py/issues/339) - add workflow trigger on merge to main by [@Kamforka](https://github.com/Kamforka) in [#343](https://github.com/TheHive-Project/TheHive4py/pull/343)
*  [#347](https://github.com/TheHive-Project/TheHive4py/issues/347) - Add support for Python 3.13 by [@Kamforka](https://github.com/Kamforka) in [#349](https://github.com/TheHive-Project/TheHive4py/pull/349)
*  [#345](https://github.com/TheHive-Project/TheHive4py/issues/345) - Add initial mkdocs page by [@Kamforka](https://github.com/Kamforka) in [#346](https://github.com/TheHive-Project/TheHive4py/pull/346)
*  [#301](https://github.com/TheHive-Project/TheHive4py/issues/301) - Add client, alert and api reference docs by [@Kamforka](https://github.com/Kamforka) in [#350](https://github.com/TheHive-Project/TheHive4py/pull/350)
*  [#340](https://github.com/TheHive-Project/TheHive4py/issues/340) - Add retry mechanism by [@Kamforka](https://github.com/Kamforka) in [#344](https://github.com/TheHive-Project/TheHive4py/pull/344)
 
### Changed 
* Patch important note sections in README by [@Kamforka](https://github.com/Kamforka) in [#337](https://github.com/TheHive-Project/TheHive4py/pull/337)
* Bump actions/download-artifact from 3 to 4.1.7 in /.github/workflows by [@dependabot](https://github.com/dependabot) in [#338](https://github.com/TheHive-Project/TheHive4py/pull/338)
*  [#301](https://github.com/TheHive-Project/TheHive4py/issues/301) - Adjust thehive4py title's font size by [@Kamforka](https://github.com/Kamforka) in [#357](https://github.com/TheHive-Project/TheHive4py/pull/357)
*  [#359](https://github.com/TheHive-Project/TheHive4py/issues/359) - Upgrade test integrator to use v5.4.2 by [@Kamforka](https://github.com/Kamforka) in [#360](https://github.com/TheHive-Project/TheHive4py/pull/360)

### New Contributors
* [@dependabot](https://github.com/dependabot) made their first contribution in [#338](https://github.com/TheHive-Project/TheHive4py/pull/338)

**Full Changelog**: [2.0.0b6...2.0.0b7](https://github.com/TheHive-Project/TheHive4py/compare/2.0.0b6...2.0.0b7)

## 2.0.0b6 (2024-08-28)

### What's Changed
* Review task type hints by [@Kamforka](https://github.com/Kamforka) in [#318](https://github.com/TheHive-Project/TheHive4py/pull/318)
* Extend alert endpoint with attachment methods by [@Kamforka](https://github.com/Kamforka) in [#321](https://github.com/TheHive-Project/TheHive4py/pull/321)
* Rework test container by [@Kamforka](https://github.com/Kamforka) in [#326](https://github.com/TheHive-Project/TheHive4py/pull/326)
* Align pyproject.toml to Git Repo License of MIT by [@jamesmckibbenathrb](https://github.com/jamesmckibbenathrb) in [#330](https://github.com/TheHive-Project/TheHive4py/pull/330)
* Update TheHive icon link in README.md by [@Kamforka](https://github.com/Kamforka) in [#331](https://github.com/TheHive-Project/TheHive4py/pull/331)
* Add a generic query endpoint and align case update fields with other update methods by [@Kamforka](https://github.com/Kamforka) in [#334](https://github.com/TheHive-Project/TheHive4py/pull/334)

### New Contributors
* [@jamesmckibbenathrb](https://github.com/jamesmckibbenathrb) made their first contribution in [#330](https://github.com/TheHive-Project/TheHive4py/pull/330)

**Full Changelog**: [2.0.0b5...2.0.0b6](https://github.com/TheHive-Project/TheHive4py/compare/2.0.0b5...2.0.0b6)


## 2.0.0b5 (2023-10-13)

### What's Changed
Merged Pull Requests
* Delete unused setup.py by [@Kamforka](https://github.com/Kamforka) in [#298](https://github.com/TheHive-Project/TheHive4py/pull/298)
* Actualize main with develop by [@Kamforka](https://github.com/Kamforka) in [#297](https://github.com/TheHive-Project/TheHive4py/pull/297)
* Enhance readme by [@Kamforka](https://github.com/Kamforka) in [#299](https://github.com/TheHive-Project/TheHive4py/pull/299)
* Add deployment workflow by [@Kamforka](https://github.com/Kamforka) in [#300](https://github.com/TheHive-Project/TheHive4py/pull/300)
* Update important note and add query examples by [@Kamforka](https://github.com/Kamforka) in [#305](https://github.com/TheHive-Project/TheHive4py/pull/305)
* Change to MIT license by [@Kamforka](https://github.com/Kamforka) in [#306](https://github.com/TheHive-Project/TheHive4py/pull/306)
* Get rid of setup.cfg by [@Kamforka](https://github.com/Kamforka) in [#309](https://github.com/TheHive-Project/TheHive4py/pull/309)
* Fix and update filters by [@Kamforka](https://github.com/Kamforka) in [#310](https://github.com/TheHive-Project/TheHive4py/pull/310)
* Bump thehive4py-integrator to v5.2.5 by [@Kamforka](https://github.com/Kamforka) in [#312](https://github.com/TheHive-Project/TheHive4py/pull/312)


**Full Changelog**: [2.0.0b4...2.0.0b5](https://github.com/TheHive-Project/TheHive4py/compare/2.0.0b4...2.0.0b5)

## 2.0.0b4 (2023-01-20)

### What's Changed
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/2.0.0b3...2.0.0b4)

**Closed issues:**

- Add case and alert TTPs operations [\#268](https://github.com/TheHive-Project/TheHive4py/issues/268)
- How to perform a bulk-insert of observables [\#263](https://github.com/TheHive-Project/TheHive4py/issues/263)

**Merged pull requests:**

- add py.typed to the project to please mypy and make the library PEP-561 compliant [\#272](https://github.com/TheHive-Project/TheHive4py/pull/272) ([Kamforka](https://github.com/Kamforka))
- 268 add case and alert ttps operations [\#271](https://github.com/TheHive-Project/TheHive4py/pull/271) ([Kamforka](https://github.com/Kamforka))
- Test observable attachment download [\#270](https://github.com/TheHive-Project/TheHive4py/pull/270) ([Kamforka](https://github.com/Kamforka))
- Add parameters to method alert.promote\_to\_case\(\) [\#269](https://github.com/TheHive-Project/TheHive4py/pull/269) ([vdebergue](https://github.com/vdebergue))
- Update README.md [\#267](https://github.com/TheHive-Project/TheHive4py/pull/267) ([ater49](https://github.com/ater49))
- Download an attachment from an observable [\#266](https://github.com/TheHive-Project/TheHive4py/pull/266) ([mike1796](https://github.com/mike1796))
- Create local ci commands for devs [\#265](https://github.com/TheHive-Project/TheHive4py/pull/265) ([Kamforka](https://github.com/Kamforka))
- Add observableType endpoints [\#264](https://github.com/TheHive-Project/TheHive4py/pull/264) ([Black-Pearl25](https://github.com/Black-Pearl25))
- Migrate to pyproject.toml [\#262](https://github.com/TheHive-Project/TheHive4py/pull/262) ([Kamforka](https://github.com/Kamforka))
- Add basic ci workflow [\#261](https://github.com/TheHive-Project/TheHive4py/pull/261) ([Kamforka](https://github.com/Kamforka))


## 2.0.0b3 (2022-10-24)

### What's Changed
[Full Changelog](https://github.com/TheHive-Project/TheHive4py/compare/2.0.0b2...2.0.0b3)

**Closed issues:**

- Use between with 2 dates [\#257](https://github.com/TheHive-Project/TheHive4py/issues/257)
- JSONDecodeError not caught correctly when using AWS Lambda [\#255](https://github.com/TheHive-Project/TheHive4py/issues/255)
- thehive4py==1.8.1 Code Erroe [\#254](https://github.com/TheHive-Project/TheHive4py/issues/254)

**Merged pull requests:**

- Set InputAlert's date property as optional [\#260](https://github.com/TheHive-Project/TheHive4py/pull/260) ([Kamforka](https://github.com/Kamforka))
- Use json.loads instead of relying on requests' json method [\#259](https://github.com/TheHive-Project/TheHive4py/pull/259) ([Kamforka](https://github.com/Kamforka))
- Persist error response data in TheHiveError [\#258](https://github.com/TheHive-Project/TheHive4py/pull/258) ([Kamforka](https://github.com/Kamforka))

## 2.0.0b2 (2022-08-20)

### What's Changed
*  [#250](https://github.com/TheHive-Project/TheHive4py/issues/250) - Implement list comment methods for alerts and cases by [@Kamforka](https://github.com/Kamforka) in [#251](https://github.com/TheHive-Project/TheHive4py/pull/251)
* [fr] ability to manage multi valued customfields by [@Kamforka](https://github.com/Kamforka) in [#253](https://github.com/TheHive-Project/TheHive4py/pull/253)


**Full Changelog**: [2.0.0b1..2.0.0b2](https://github.com/TheHive-Project/TheHive4py/compare/2.0.0b1..2.0.0b2)


## 2.0.0b1 (2022-08-05)

### What's Changed
*  [#250](https://github.com/TheHive-Project/TheHive4py/issues/250) - Implement list comment methods for alerts and cases by [@Kamforka](https://github.com/Kamforka) in [#251](https://github.com/TheHive-Project/TheHive4py/pull/251)


**Full Changelog**: [2.0.0b0...2.0.0b1](https://github.com/TheHive-Project/TheHive4py/compare/2.0.0b0...2.0.0b1)

## 2.0.0b0 (2022-08-05)

### What's Changed
* Update for 5.0.1 by [@vdebergue](https://github.com/vdebergue) in [#241](https://github.com/TheHive-Project/TheHive4py/pull/241)
* added case.set_share by [@migueldo](https://github.com/migueldo) in [#242](https://github.com/TheHive-Project/TheHive4py/pull/242)

### New Contributors
* [@vdebergue](https://github.com/vdebergue) made their first contribution in [#241](https://github.com/TheHive-Project/TheHive4py/pull/241)
* [@migueldo](https://github.com/migueldo) made their first contribution in [#242](https://github.com/TheHive-Project/TheHive4py/pull/242)

**Full Changelog**: [2.0.0b0](https://github.com/TheHive-Project/TheHive4py/commits/2.0.0b0)