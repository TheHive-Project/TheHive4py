# Alert

## A simple alert

A new alert requires at least these fields to be defined:

-   `type`: The type of the alert.
-   `source`: The source of the alert.
-   `sourceRef`: A unique reference for the alert.
-   `title`: A descriptive title for the alert.
-   `description`: Additional information describing the alert.

Here's an example that demonstrates how to create the most simplistic alert possible using the [alert.create][thehive4py.endpoints.alert.AlertEndpoint.create] method:

```python
--8<-- "examples/alert/simple.py"
```

## An advanced alert

The previous example was as simple as it gets and only specified the required alert fields inline in the create method call.
With a more advanced example this can become complicated and hard to read. 
Fortunately we can use `thehive4py`'s type hints to the rescue and specify more complex input alerts outside of the method call. 

Here's how:
```python
--8<-- "examples/alert/advanced.py"
```

In the above snippet `input_alert` is created before the create call and later passed to the `alert` argument.
Finally after the creation of the alert we saved the response in the `output_alert` to be able to use it later.

!!! note
    While the above alert is a bit more advanced it's still far from the most complex example possible. 
    In case you want to see the what the Alert API offers please check out the [official alert docs](https://docs.strangebee.com/thehive/api-docs/#tag/Alert).


## Alert observables

In TheHive an observable is a piece of data or evidence (e.g., an IP address, domain, etc.) associated with a security incident, used to provide context and aid in the investigation and response process.

Let's take a look at different ways of populating alerts with observables, let them be textual or file based observables.

### Add observables during alert creation

We can add observables already during alert creation. This is a great way to combine alert and observable creation in an atomic way:

Let's create an alert with an `ip` and a `domain` observable:

```python
--8<-- "examples/alert/observable_during_alerting.py"
```

### Add observables to an existing alert

While it's probably the most convenient way to combine alert and observable creation in a single call, sometimes we don't have all the observables at hand during alert creation time or we have such a large number of observables that we cannot send them all in one single request.

Fortunately TheHive API supports alert observable creation on already existing alerts. Let's repeat the previous example, but this time add the two observables to an existing alert using the [alert.create_observable][thehive4py.endpoints.alert.AlertEndpoint.create_observable] method:


```python
--8<-- "examples/alert/observable_after_alerting.py"
```

### Add file based observables

In the previous examples we've seen how to handle observables without attachments. However sometimes we also want to add attachments to an observable not only textual data. Fortunately that is supported by TheHive. So in the next example let's create a temporary directory with a dummy file and some dummy content that will represent our file based observable and add it to an alert:


```python
--8<-- "examples/alert/observable_from_file.py"
```

As we can see from the above example a file based observable must specify the `attachment` property with a key that links it to the attachment specified in the `attachment_map` dictionary.

This way TheHive will know which attachment to pair with which observable behind the scenes.

In our example `attachment_key` is used to specify the relationship between the observable and the actual file. In this case its value is a uuid, however it can be any arbitrary value, though it's important that it should uniquely identify the attachment and the observable we would like to pair in TheHive.

## Update single and bulk 

Creating alerts is fun but sometimes an existing alert also needs to be updated. As expected `thehive4py` offers multiple ways to accomplish this task either on a single alert or multiple ones.

### Update single

A single alert can be updated using the [alert.update][thehive4py.endpoints.alert.AlertEndpoint.update] method. The method requires the `alert_id` of the alert to be updated and the `fields` to update.

```python
--8<-- "examples/alert/update_single.py"
```

In the above example we've updated the `title` and the `tags` fields.

Be mindful though, `thehive4py` is a lightweight wrapper around TheHive API and offers no object relationship mapping functionalities, meaning that the `original_alert` won't reflect the changes of the update.

In order to work with the updated alert we had to fetch the latest version using the [alert.get][thehive4py.endpoints.alert.AlertEndpoint.get] method and store it in the `updated_alert` variable.

Now the content of `updated_alert` should reflect the changes we made with our update request.

!!! tip
    To see the full list of supported update fields please consult the [official docs](https://docs.strangebee.com/thehive/api-docs/#tag/Alert/operation/Update%20Alert).

### Update bulk

It is also possible to update many alerts at the same time, however there's a constraint: the content of the `fields` property will be applied to all the specified alerts uniformly. With all that said one can use [alert.bulk_update][thehive4py.endpoints.alert.AlertEndpoint.bulk_update] method for bulk updates. 
The method accepts the same `fields` dictionary as before but with an additional `ids` field on it, which should contain the list of ids of the alerts to be bulk updated.

```python
--8<-- "examples/alert/update_bulk.py"
```

In the example we prepare two alerts for the bulk update, and collect their ids in the `original_alert_ids` list.
Then we update the fields `title` and `tags` on both alerts using the bulk update method.

## Get and find

There are multiple ways to retrieve already existing alerts, we can fetch them one by one or many at once!

### Get a single alert

To get a single alert one can use the [alert.get][thehive4py.endpoints.alert.AlertEndpoint.get] method with the alert's id as follows:

```python
--8<-- "examples/alert/fetch_with_get.py"
```

### Find multiple alerts

To fetch multiple alerts based on arbitrary conditions one can use the [alert.find][thehive4py.endpoints.alert.AlertEndpoint.find] method which is an abstraction on top of TheHive's Query API.

In the next example we will create two alerts with different tags. The first alert will get the `antivirus` tag while the second one will get the `phishing` tag.

Then we will construct query filters in different ways to look for alerts with these tags on them:

```python
--8<-- "examples/alert/fetch_with_find.py"
```

The above example demonstrates two ways to construct query filters.

One is to provide a raw dict based filter which is the plain format of [TheHive's Query API](https://docs.strangebee.com/thehive/api-docs/#tag/Query-and-Export). This is demonstrated in the `raw_filters` variable.

However this can be cumbersome to remember, that's why `thehive4py` provides filter builders to conveniently build filter expressions on the client side. This alternative approach is demonstrated in the `class_filters` variable.

These filter expressions can be chained together with different operators, just like we did with the `|` (`or`) operator in the example.

Currently, the filter classes support the following operators:

- `&`: Used for the Query API's `_and` construct.
- `|`: Used for the Query API's `_or` construct.
- `~`: Used for the Query API's `_not` construct.

The full list of the filter builders can be found in the [query.filters][thehive4py.query.filters] module.

## Promote and merge into a case

In TheHive alerts usually represent signals of compromise while cases provide a higher level entity to group these signals into one object.
Therefore we can promote an alert into a case or merge new alerts into an existing case for a more organised investigation.

### Promote to case

To create a case from an alert we can use [alert.promote_to_case][thehive4py.endpoints.alert.AlertEndpoint.promote_to_case] method.

```python
--8<-- "examples/alert/case_promote.py"
```

!!! tip
    For additional control the method accepts a `fields` argument which can be used to modify properties on the case.
    To see all available options please consult the [official docs](https://docs.strangebee.com/thehive/api-docs/#tag/Alert/operation/Create%20Case%20from%20Alert).

### Merge into case

Oftentimes new alerts correspond to an already existing case. Fortunately we have the option to merge such alerts into a parent case using the [alert.merge_into_case][thehive4py.endpoints.alert.AlertEndpoint.merge_into_case] method.

```python
--8<-- "examples/alert/case_merge.py"
```

In the above example we prepared a `parent_case` to which we merge the `new_alert` using its id and finally save the updated case in the `updated_parent_case` variable.

!!! tip
    It can happen that multiple new alerts belong to the same parent case. In such situation we can use the [alert.bulk_merge_into_case][thehive4py.endpoints.alert.AlertEndpoint.bulk_merge_into_case] method for a more convenient merge process.


## Delete single and bulk

`thehive4py` provides two different ways to delete alerts:

- delete a single alert
- delete alerts in bulk

### Delete single 

To delete a single alert the [alert.delete][thehive4py.endpoints.alert.AlertEndpoint.delete] method can be used as follows:

```python
--8<-- "examples/alert/delete_single.py"
```


### Delete in bulk

To delete multiple alerts via a single request one can use the [alert.bulk_delete][thehive4py.endpoints.alert.AlertEndpoint.bulk_delete] method as follows:

```python
--8<-- "examples/alert/delete_bulk.py"
```

In the above example we created two alerts and saved their ids in the `alert_ids_to_delete` variable just to pass it to the bulk deletion method.
