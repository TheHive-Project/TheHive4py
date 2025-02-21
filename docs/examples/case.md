# Case

## A minimalistic case

The most minimalistic case requires at least the below fields to be defined:

-   `title`: The title of the case.
-   `description`: The description of the case.

Here's an example that demonstrates how to create the most minimalistic case possible using the [case.create][thehive4py.endpoints.case.CaseEndpoint.create] method:

```python
--8<-- "examples/case/minimalistic.py"
```
## An advanced case

The previous example demonstrated how to create the simplest case ever.

In the next example let's create a more advanced case by using the combination of the [InputCase][thehive4py.types.case.InputCase] type hint and the [case.create][thehive4py.endpoints.case.CaseEndpoint.create] method.

```python
--8<-- "examples/case/advanced.py"
```

In the above snippet `input_case` is created before the create call and later passed to the `case` argument.

Finally after the creation of the case we saved the response in the `output_case` to be able to use it later.

!!! note
    While the above case is a bit more advanced it's still far from the most complex example that is possible. 
    Should you be interested of what the Case API offers please check out the [official docs](https://docs.strangebee.com/thehive/api-docs/#tag/Case).

## Get and find

There are multiple ways to retrieve already existing cases:

### Get a single case

To get a single case one can use the [case.get][thehive4py.endpoints.case.CaseEndpoint.get] method with the case's id as follows:

```python
--8<-- "examples/case/fetch_with_get.py"
```

### Find multiple cases

To fetch multiple cases based on arbitrary conditions one can use the [case.find][thehive4py.endpoints.case.CaseEndpoint.find] method which is an abstraction on top of TheHive's Query API.

In the next example we will create two cases with different tags. The first case will get the `antivirus` tag while the second one will get the `phishing` tag.

Then we will construct a query filter that will look for cases with these tags on them:

```python
--8<-- "examples/case/fetch_with_find.py"
```

The above example demonstrates how to construct query filters.

These filter expressions can be chained together with different operators, just like we did with the `|` (`or`) operator in the example.

Currently, the filter classes support the following operators:

- `&`: Used for the Query API's `_and` construct.
- `|`: Used for the Query API's `_or` construct.
- `~`: Used for the Query API's `_not` construct.

The full list of the filter builders can be found in the [query.filters][thehive4py.query.filters] module.

## Update single and bulk

Sometimes an existing case needs to be updated. TheHive offers multiple ways to accomplish this task either with a single case or multiple ones.

### Update single

A single case can be updated using [case.update][thehive4py.endpoints.case.CaseEndpoint.update] method. The method requires the `case_id` of the case to be updated and the `fields` to update.

```python
--8<-- "examples/case/update_single.py"
```

In the above example we've updated the `title` and the `tags` fields.

Be mindful though, `thehive4py` is a lightweight wrapper around TheHive API and offers no object relationship mapping functionalities, meaning that the original `original_case` won't reflect the changes of the update.

To work with the updated case we fetched the latest version using the [case.get][thehive4py.endpoints.case.CaseEndpoint.get] method and stored it in the `updated_case` variable.

Now the content of `updated_case` should reflect the changes we made with our update request.

!!! tip
    To see the full list of supported update fields please consult the [official docs](https://docs.strangebee.com/thehive/api-docs/#tag/Case/operation/Update%20case).

### Update bulk

To update the **same fields** with the **same values** on multiple cases at the same time, one can use [case.bulk_update][thehive4py.endpoints.case.CaseEndpoint.bulk_update] method. 
The method accepts the same `fields` dictionary with an additional `ids` field on it, which should contain the list of ids of the cases to be bulk updated.

```python
--8<-- "examples/case/update_bulk.py"
```

In the example we prepare two cases for the bulk update, and collect their ids in the `original_case_ids` list.
Then we update the fields `title` and `tags` on both cases using the bulk update method.


## Merge cases

Many times during case triaging it occurs that individual cases turn out to be closely related. For this use case TheHive provides an option to merge individual cases using the [case.merge][thehive4py.endpoints.case.CaseEndpoint.merge] method.

In the following example we will create two cases and will merge them into one new case:

```python
--8<-- "examples/case/merge.py"
```

As you can see the merged cases will end up in one single case which is represented by the `merge_case` variable in our example.

!!! important
    In case you wonder what will happen to the original cases, during the merge they will be deleted and their legacy will live on in the final merge case.

!!! note
    In the example we merged two cases, but it's worth to mention that the merge endpoint lets us merge as many cases as we need into one final case.

## Delete 

It's possible to delete a case using the [case.delete][thehive4py.endpoints.case.CaseEndpoint.delete] method.
Here's a simple example to demonstrate: 

```python
--8<-- "examples/case/delete.py"
```

!!! note
    In contrast to the alert endpoint the case endpoint doesn't support bulk deletion of cases, so should you need to delete multiple cases the easiest options is to collect the case ids and iterate over them using the single delete endpoint.

## Case observables

TheHive API provides multiple ways to add observables to cases, let them be textual or file based observables.

### Add observables to an existing case

Unlike the Alert API, the Case API doesn't support adding observables to cases during their creation, this means that we can only add case observables retroactively.

In the next example we're gonna create a case to add two observables to it using the [case.create_observable][thehive4py.endpoints.case.CaseEndpoint.create_observable] method:

```python
--8<-- "examples/case/obervable_simple.py"
```

### Add file based observables

In the previous example we've seen how to handle simple observables without attachments. Next we will create a temporary directory with a dummy file and some dummy content that will represent our file based observable and add it to a case:


```python
--8<-- "examples/case/observable_file.py"
```

As we can see from the above example a file based observable needs an actual file and its filepath, in our example these are represented by `observable_filepath` and `observable_file`

Finally the `observable` metadata needs to be defined with its `dataType` as `file` and then the `data` field should be omitted. Finally the `observable_path` argument must be defined with the value of the actual `observable_filepath`.

This way TheHive will pair the observable metadata with the file as its attachment behind the scenes.

## Case tasks

For more advanced case handling we can specify tasks which will serve as steps during the evaluation of the case.

Fortunately TheHive API provides different options to add tasks to cases and we will check them out in the next sections.

### Add tasks during case creation

We can specify tasks already during case creation. This is a great way to combine case and task creation in an atomic way.

Let's do an example to create a case with a `Triage` and `Respond` tasks:

```python
--8<-- "examples/case/tasks_during_creation.py"
```

This snippet will create a case with the required tasks in one go.

### Add tasks to an existing case

In the previous section we could see that it's possible to specify tasks during case creation, however sometimes we want to add tasks after a case has been created.

For this purpose we can use the [case.create_task][thehive4py.endpoints.case.CaseEndpoint.create_task] method.

Now let's do an example by adding tasks retroactively to a case:

```python
--8<-- "examples/case/tasks_after_creation.py"
```

In the above example we created an empty case as `case_to_enrich`, and then defined a list of two tasks in the `case_tasks` variable.

Finally using a for loop and the `case.create_task` method we added them to our dummy case one by one.

## Case pages

In order to give more context to a case we can add pages to it, which could serve as additional notes or documentation during investigation.

Like usual TheHive API provides different possibilities to add such pages to cases that we will see in the next sections.

### Add pages during case creation

We can add pages already during case creation. This is a great way to combine case and page creation in a single go.

Let's create a case with two pages, one to take notes and another one to summarize the case:

```python
--8<-- "examples/case/pages_during_creation.py"
```

As you can see we had to specify the `title`, `category` and `content` fields which are all mandatory for the page objects.

On the other hand each of these fields are freetext fields so we have the freedom to specify any value for them.


### Add pages to an existing case

In the previous section we could see that it's possible to add pages during case creation, however sometimes we want to add pages after a case has been created.

For this purpose we can use the [case.create_page][thehive4py.endpoints.case.CaseEndpoint.create_page] method.

Now let's do an example by adding pages retroactively to a case:

```python
--8<-- "examples/case/pages_after_creation.py"
```

In the above example we created an empty case as `case_to_enrich`, and then defined a list of pages in the `page_tasks` variable.

Finally using a for loop and the `case.create_page` method we added them to our dummy case one by one.

## Case procedures

TheHive considers the [MITRE ATT&CK](https://attack.mitre.org/) framework as a first class citizen and fully supports its tactics, techniques and procedures (TTPs for short), therefore it's possible to enrich cases with procedures from their catalog.

TheHive simply refers to the MITRE ATT&CK TTPs as procedures, and next we will see how can these procedures be applied to cases.

### Add procedures to an existing case

In this example we will create an empty case and using the [case.create_task][thehive4py.endpoints.case.CaseEndpoint.create_task] method we will enrich it with the technique of [[T1566] Phishing](https://attack.mitre.org/techniques/T1566/) and the subtechnique of [[T1566.001] Phishing - Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/):


```python
--8<-- "examples/case/procedures_after_creation.py"
```

The procedure entity requires `occurDate` and `patternId` as they are mandatory fields while `tactic` and `description` are optional.

To simplify the example we also used the [helpers.now_to_ts][thehive4py.helpers.now_to_ts] function to generate a dummy timestamp for the procedures.

