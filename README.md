<div align="center">
  <p>
   <a href="https://github.com/TheHive-Project/TheHive4py" target="_blank"><img src="https://strangebee.com/wp-content/uploads/2024/07/Icon4Nav_TheHive.png" alt="TheHive Logo"></a>
  </p>
  <h1>thehive4py</h1>
  <p>
   <em>the de facto Python API client of <a href="https://strangebee.com/thehive/">TheHive</a></em>
  </p>
  <p align="center">
      <a href="https://github.com/TheHive-Project/TheHive4py/releases" target="_blank">
          <img src="https://img.shields.io/github/v/release/Thehive-project/thehive4py?logo=github&logoColor=FFC72C&labelColor=0049D4" alt="release">
      </a>
      <a href="https://github.com/TheHive-Project/TheHive4py/actions/workflows/main-cicd.yml" target="_blank">
          <img src="https://img.shields.io/github/actions/workflow/status/TheHive-Project/TheHive4py/main-cicd.yml?logo=github&logoColor=FFC72C&labelColor=0049D4" alt="build">
      </a>
      <a href="https://app.codecov.io/github/TheHive-Project/TheHive4py" target="_blank">
          <img src="https://img.shields.io/codecov/c/gh/TheHive-Project/TheHive4py?logo=codecov&logoColor=FFC72C&labelColor=0049D4" alt="codecov">
      </a>
      <a href="https://pypi.org/project/thehive4py" target="_blank">
          <img src="https://img.shields.io/pypi/dm/thehive4py?logo=python&logoColor=FFC72C&labelColor=0049D4" alt="pypi">
      </a>
      <a href="./LICENSE" target="_blank">
          <img src="https://img.shields.io/github/license/TheHive-Project/TheHive4py?logo=unlicense&logoColor=FFC72C&labelColor=0049D4" alt="license">
      </a>
      <a href="https://discord.com/invite/XhxG3vzM44" target="_blank">
          <img src="https://img.shields.io/discord/779945042039144498?logo=discord&logoColor=FFC72C&labelColor=0049D4" alt="discord">
      </a>
  </p>
</div>

---
**Documentation**: <a href="https://thehive-project.github.io/TheHive4py" target="_blank">https://thehive-project.github.io/TheHive4py</a>

**Source Code**: <a href="https://github.com/TheHive-Project/TheHive4py" target="_blank">https://github.com/TheHive-Project/TheHive4py</a>

---

# Introduction

> [!IMPORTANT]
> thehive4py v1.x is not maintained anymore as TheHive v3 and v4 are end of life. thehive4py v2.x is a complete rewrite and is not compatible with thehive4py v1.x.

**What's New:** This is a rebooted version of `thehive4py` designed specifically for TheHive 5. Stay tuned, as we have more exciting updates in store!

Welcome to `thehive4py`, the Python library designed to simplify interactions with TheHive 5.x. Whether you're a cybersecurity enthusiast or a developer looking to integrate TheHive into your Python projects, this library has got you covered.

Feel free to explore the library's capabilities and contribute to its development. We appreciate your support in making TheHive integration in Python more accessible and efficient.

# Quickstart

## Requirements
`thehive4py` works with all currently supported python versions. One can check the official version support and end of life status [here](https://devguide.python.org/versions/).

## Installation
The `thehive4py` can be installed with pip like:

```
pip install thehive4py
```

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
        apikey="h1v3b33",
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


> [!NOTE]
> Attempting to create another alert with the same values for `type`, `source`, and `sourceRef` will not be accepted by the backend as the combination of the three fields should be unique per alert.

## Add alert observables

To make your alerts more informative and actionable, you can add observables to them. Observables are specific pieces of data related to an alert. In this example, we'll enhance the previous alert with two observables: an IP address `93.184.216.34` and a domain `example.com`.

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

If you need to add or modify fields in an existing alert, you can easily update it using client's `alert.update` method. In this example, we'll add a tag `my-tag` and change the alert's title:

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

It's essential to understand that the `my_alert` object in your Python code will not automatically reflect these changes. `thehive4py` doesn't provide object relationship mapping features. To get the latest version of the alert after making modifications, you need to fetch it again:

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
pip install -e .[dev]
```
    
This command installs the package in editable mode (`-e`) and includes additional development dependencies.
 
Now, you have the `thehive4py` package installed in your development environment, ready for contributions.

## Contributing

To contribute to `thehive4py`, follow these steps:

1.  **Create an issue:** Start by creating an issue that describes the problem you want to solve or the feature you want to add. This allows for discussion and coordination with other contributors.
    
2.  **Create a branch:** Once you have an issue, create a branch for your work. Use the following naming convention: `<issue-no>-title-of-branch`. For example, if you're working on issue #1 and updating the readme, name the branch `1-update-readme`.
    
    

## Run CI checks before pushing changes

The project is utilizing the [nox] library to define and run automated dev scripts.

To ensure the integrity of your changes and maintain code quality you can use the provided sessions from the local `noxfile.py`.
For example you can run CI checks before pushing your changes to the repository. Use one of the following methods:

**Method 1: Manual check**

Run the CI checks manually by using the following command:

    nox

This will trigger all CI checks except tests as the `noxfile.py` is configured to do so by default.


To run individual checks one can list all the available sessions with:

    nox --list

**Method 2: Automatic checks with pre-commit hooks [experimental]**

> [!NOTE]
> The pre-commit hooks are not thoroughly tested at the moment and probably broken

For a more streamlined workflow, you can install pre-commit hooks provided by the repository. These hooks will automatically execute checks before each commit. To install them, run:

```
pre-commit install
```

With pre-commit hooks in place, your changes will be automatically validated for compliance with coding standards and other quality checks each time you commit. This helps catch issues early and ensures a smooth contribution process.

## Testing

> [!NOTE]
> Since TheHive 5.3 the licensing constraints has been partially lifted therefore a public integrator image is available for running tests both locally and in github.

`thehive4py` primarily relies on integration tests, which are designed to execute against a live TheHive 5.x instance. These tests ensure that the library functions correctly in an environment closely resembling real-world usage.

### Test requirements

Since the test suite relies on the existence of a live TheHive docker container a local docker engine installation is a must.
If you are unfamiliar with docker please check out the [official documentation][get-docker].

### Test setup

The test suite relies on the official [thehive-image] to create a container locally with the predefined name `thehive4py-integration-tester` which will act as a unique id.  
The container will expose TheHive on a random port to make sure it causes no conflicts for any other containers which expose ports.  
The suite can identify this random port by querying the container info based on the predefined name.
Once TheHive is responsive the suite will initialize the instance with a setup required by the tests (e.g.: test users, organisations, etc.).  
Please note that due to this initial setup the very first test run will idle for some time to make sure everything is up and running. Any other subsequent runs' statup time should be significantly faster.  

### Testing locally
To execute the whole test suite locally one can use the `test` session provided by the local `noxfile.py` utility script like:

    nox --session=test

or

    nox -s test

for short.

Note however that the above will command execute the entire test suite which can take several minutes to complete.
In case one wants to execute only a portion of the test suite then the easiest workaround is to pass additional arguments to the session e.g.:

    nox -s test -- tests/test_observable_endpoint.py -v

The nox command will parse additional arguments after the `--` option terminator argument and they will be passed to the underlying `pytest` command.


[get-docker]: https://docs.docker.com/get-docker/
[query-api-docs]: https://docs.strangebee.com/thehive/api-docs/#operation/Query%20API
[thehive-image]: https://hub.docker.com/r/strangebee/thehive
[nox]: https://nox.thea.codes/en/stable/
