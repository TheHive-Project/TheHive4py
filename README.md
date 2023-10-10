![TheHive Logo](https://thehive-project.org/img/logo.png)

[![Discord](https://img.shields.io/discord/779945042039144498)](https://chat.thehive-project.org)
[![License](https://img.shields.io/github/license/TheHive-Project/TheHive4py)](./LICENSE)
[![Pypi Page](https://img.shields.io/pypi/dm/thehive4py)](https://pypi.org/project/thehive4py)
[![CICD Action Badge](https://github.com/TheHive-Project/TheHive4py/actions/workflows/main-cicd.yml/badge.svg)](https://github.com/TheHive-Project/TheHive4py/actions/workflows/main-cicd.yml)

# thehive4py

> **IMPORTANT:** thehive4py v1.x is not maintained anymore as TheHive v3 and v4 are end of life. thehive4py v2.x is a complete rewrite and is not compatible with thehive4py v1.x. The library is still in beta phase.

**What's New:** This is a rebooted version of `thehive4py` designed specifically for TheHive 5. Stay tuned, as we have more exciting updates in store!

Welcome to `thehive4py`, the Python library designed to simplify interactions with TheHive 5.x. Whether you're a cybersecurity enthusiast or a developer looking to integrate TheHive into your Python projects, this library has got you covered.

Feel free to explore the library's capabilities and contribute to its development. We appreciate your support in making TheHive integration in Python more accessible and efficient.

# Quickstart

## Requirements
`thehive4py` works with all currently supported python versions, at the time of writing `py>=3.8`. One can check the official version support and end of life status [here](https://devguide.python.org/versions/).

## Installation
The `thehive4py` can be installed with pip like:

```
pip install "thehive4py>=2.0.0b"
```

**Important Note**: Since `thehive4py` 2.x is still in beta it is necessary to specify the beta version number during pip install, otherwise the latest version of 1.x would be installed.

## Create a client

You can create a `thehive4py` client instance in two different ways, depending on your authentication method:

**Method 1: Username/password authentication**
    
If you're using a username and password for authentication, you can create a client like this:
    
```python
from thehive4py import TheHiveApi

hive = TheHiveApi(
        url="https://thehive.example.com",
        username="analyst@example.com",
        password="supersecret",
    )
``` 
    
**Method 2: Apikey authentication**
    
Alternatively, if you prefer using an API key for authentication, use this method:
    
```python    
from thehive4py import TheHiveApi

hive = TheHiveApi(
        url="https://thehive.example.com",
        apikey="c0ff33nc0d3",
    )
```

Choose the authentication method that best suits your needs and security requirements.


## Create an alert

To create a new alert, you can use the client's `alert.create` method with the following minimally required fields:

-   `type`: The type of the alert.
-   `source`: The source of the alert.
-   `sourceRef`: A unique reference for the alert.
-   `title`: A descriptive title for the alert.
-   `description`: Additional information describing the alert.

Here's an example that demonstrates how to create a new alert with these required fields:

```python
my_alert = hive.alert.create(
    alert={
        "type": "my-alert",
        "source": "my-source",
        "sourceRef": "my-reference",
        "title": "My test alert",
        "description": "Just a description",
    }
)
```
The above snippet will create a new alert with the minimally required fields and will store the output alert response in the `my_alert` variable.


**Important Note**: Attempting to create another alert with the same values for `type`, `source`, and `sourceRef` will not be accepted by the backend as the combination of the three fields should be unique per alert.

## Add alert observables

To make your alerts more informative and actionable, you can add observables to them. Observables are specific pieces of data related to an alert. In this example, we'll enhance the previous alert with two observables: an IP address (`93.184.216.34`) and a domain (`example.com`).

**Method 1: Adding observables individually**

You can add observables to an existing alert using the `alert.create_observable` method as shown below:

```python
hive.alert.create_observable(
    alert_id=my_alert["_id"],
    observable={"dataType": "ip", "data": "93.184.216.34"},
)
hive.alert.create_observable(
    alert_id=my_alert["_id"],
    observable={"dataType": "domain", "data": "example.com"},
)
```

This method is useful when you want to add observables to an alert after its initial creation.

**Method 2: Adding observables during alert creation**

Alternatively, if you already know the observables when creating the alert, you can use the `observables` field within the alert creation method for a more concise approach:


Alternatively in case the observables are known during alert time we can use the `alert.create` method's `observables` field as a shortcut:

```python
my_alert = hive.alert.create(
    alert={
        "type": "my-alert",
        "source": "my-source",
        "sourceRef": "my-reference",
        "title": "My test alert",
        "description": "Just a description",
        "observables": [
            {"dataType": "ip", "data": "93.184.216.34"},
            {"dataType": "domain", "data": "example.com"},
        ],
    }
)
```

This method not only saves you from making additional network requests but also reduces the chance of errors, making your code more efficient and reliable.

By incorporating observables into your alerts, you provide valuable context and information for further analysis and incident response.

## Update an alert

If you need to add or modify fields in an existing alert, you can easily update it using client's `alert.update` method. In this example, we'll add a tag (`my-tag`) and change the alert's title:

```python
hive.alert.update(
    alert_id=my_alert["_id"],
    fields={
        "title": "My updated alert",
        "tags": ["my-tag"],
    },
)
```

The code above updates the alert's title and adds a new tag to the alert in TheHive.

**Important Note**: It's essential to understand that the `my_alert` object in your Python code will not automatically reflect these changes. `thehive4py` doesn't provide object relationship mapping features. To get the latest version of the alert after making modifications, you need to fetch it again:

```python
my_alert = hive.alert.get(alert_id=my_alert["_id"])
```

After this request, `my_alert["title"]` will be `"My Updated Alert"`, and `my_alert["tags"]` will include `"my-tag"`. This ensures that you have the most up-to-date information in your Python code.

## Create a case

You have two options to create a case in `thehive4py`: either promote an existing alert to a case or create a new, empty case.

**Method 1: Promote an existing alert to a case**

You can convert an existing alert into a case and associate it with that alert using the `alert.promote_to_case` method:

```python
my_case = hive.alert.promote_to_case(alert_id=my_alert["_id"])
```

This method will create a case based on the existing alert and automatically assign the alert to the case. Any observables from the alert will also be copied as case observables.

**Method 2: Create an empty case**

Alternatively, you can create a new, empty case using the `case.create` method:

```python
my_case = hive.case.create(
    case={"title": "My First Case", "description": "Just a description"}
)
```

This method creates a fresh case with no alerts or observables attached.

To merge an existing alert into a new case at a later time, use the `alert.merge_into_case` method:

```python
hive.alert.merge_into_case(alert_id=my_alert["_id"], case_id=my_case["_id"])
```

By choosing the method that suits your workflow, you can efficiently manage cases and alerts within TheHive using `thehive4py`.

## Query Case Observables

To retrieve observables from a case, you can use the `case.find_observables` method provided by `thehive4py`. This method supports various filtering and querying options, allowing you to retrieve specific observables or all observables associated with a case.

### Retrieve All Observables of a Case

To retrieve all the observables of a case, use the following code:

```python
case_observables = hive.case.find_observables(case_id=my_case["_id"])
```

### Retrieve Specific Observables of a Case
If you want to retrieve specific observables based on criteria, you can leverage TheHive's powerful query capabilities. You can refer to the official [Query API][query-api-docs] documentation for more details.

Here's an example of how to retrieve IP observables from a case:

```python
ip_observable = hive.case.find_observables(
    case_id=my_case["_id"], filters=Eq("dataType", "ip") & Like("data", "93.184.216.34")
)
```


In this example, we use the `Eq`, `Like` and the `&` operators filters to specify the criteria for the query. You can also achieve the same result using a dict-based approach for filtering:

```python
ip_observable = hive.case.find_observables(
    case_id=my_case["_id"],
    filters={
        "_and": [
            {"_field": "dataType", "_value": "ip"},
            {"_like": {"_field": "data", "_value": "93.184.216.34"}},
        ]
    }
)
```

The dict-based approach is possible, but we recommend using the built-in filter classes for building query expressions due to their ease of use.

Currently, the filter classes support the following operators:

- `&`: Used for the Query API's `_and` construct.
- `|`: Used for the Query API's `_or` construct.
- `~`: Used for the Query API's `_not` construct.

These operators provide a convenient and intuitive way to construct complex queries.

# Development

## Setting up a virtual environment (optional)

A virtual environment is highly recommended for clean and isolated Python development. It allows you to manage project-specific dependencies and avoid conflicts with other projects. In case you don't know what is/how to use a virtual environment let's find out more [here](https://docs.python.org/3/library/venv.html#module-venv).

## Install the package for development 

If you are a first time contributor to github projects please make yourself comfortable with the page [contributing to projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

Navigate to the cloned repository's directory and install the package with development extras using pip:
    
```
pip install -e '.[dev]'
```
    
This command installs the package in editable mode (`-e`) and includes additional development dependencies.
 
Now, you have the `thehive4py` package installed in your development environment, ready for contributions.

## Contributing

To contribute to `thehive4py`, follow these steps:

1.  **Create an issue:** Start by creating an issue that describes the problem you want to solve or the feature you want to add. This allows for discussion and coordination with other contributors.
    
2.  **Create a branch:** Once you have an issue, create a branch for your work. Use the following naming convention: `<issue-no>-title-of-branch`. For example, if you're working on issue #1 and updating the readme, name the branch `1-update-readme`.
    
3.  **Commit prefix:** When making commits, prefix them with `#<issue-no> - commit message`. This practice helps in easy navigation and tracking of commits back to the corresponding issue. For instance, use `#1 - update readme` as the commit message.
    

## Run CI checks before pushing changes

To ensure the integrity of your changes and maintain code quality, you can run CI checks before pushing your changes to the repository. Use one of the following methods:

**Method 1: Manual check**

Run the CI checks manually by executing the following command:

```
python scripts/ci.py 
```

This command will trigger the CI checks and provide feedback on any issues that need attention.

**Method 2: Automatic checks with pre-commit hooks [experimental]**

**Important Note**: The pre-commit hooks are not thoroughly tested at the moment and probably broken

For a more streamlined workflow, you can install pre-commit hooks provided by the repository. These hooks will automatically execute checks before each commit. To install them, run:

```
pre-commit install
```

With pre-commit hooks in place, your changes will be automatically validated for compliance with coding standards and other quality checks each time you commit. This helps catch issues early and ensures a smooth contribution process.

## Testing

`thehive4py` primarily relies on integration tests, which are designed to execute against a live TheHive 5.x instance. These tests ensure that the library functions correctly in an environment closely resembling real-world usage.

However, due to licensing constraints with TheHive 5.x, the integration tests are currently not available for public or local use.

To ensure code quality and prevent broken code from being merged, a private image is available for the integration-test workflow. This means that any issues should be detected and addressed during the PR phase.

The project is actively working on a solution to enable developers to run integration tests locally, providing a more accessible and comprehensive testing experience.

While local testing is in development, relying on the automated PR checks ensures the reliability and quality of the `thehive4py` library.

[query-api-docs]: https://docs.strangebee.com/thehive/api-docs/#operation/Query%20API