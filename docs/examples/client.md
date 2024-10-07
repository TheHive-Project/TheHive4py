# Client

## Authentication

TheHive API provides two ways to authenticate the client:

- apikey auth
- username and password auth

### Auth with apikey

```python
--8<-- "examples/client/auth_with_apikey.py"
```

### Auth with username and password

```python
--8<-- "examples/client/auth_with_username_and_password.py"
```

## Organisation

The client will use the default organisation of the user. However in case the user belongs to multiple organisation the client also provides options to specify which organisation to use.


### Specify the organisation during init

In this example we will instaniate a client with the `admin` organisation explicitly:

```python
--8<-- "examples/client/org_via_constructor.py"
```

### Switch organisations during runtime

In this example we will instantiate a client without explicitly specifying an organisation and switch to another organisation using the [session_organisation][thehive4py.client.TheHiveApi.session_organisation] property:

```python
--8<-- "examples/client/org_during_runtime.py"
```

!!! warning
    The [session_organisation][thehive4py.client.TheHiveApi.session_organisation] property is not thread-safe and it's almost always better to instantiate more clients if one wants to work with multiple organisations in parallel.


## SSL Verification

By default the client verifies if the connection is going through SSL.
In case one needs to pass a custom certificate bundle or directory it's possible via the `verify` argument like:

```python
--8<-- "examples/client/ssl.py"
```

!!! note
    It's also possible to disable SSL verification completely by setting `verify` to `False`. 
    However this is greatly discouraged as it's a security bad practice.


## Retries

The client comes with a sensible retry mechanism by default that will try to cover the most common use cases.
However it's also possible to configure a tailored retry mechanism via the `max_retries` argument.

The below example will configure a custom retry mechanism with 5 total attempts, a backoff factor of 0.3 seconds on GET methods and 500 status codes: 

```python
--8<-- "examples/client/retries.py"
```

To learn more about the `urllib3.Retry` object please consult the official documentation [here](https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html#urllib3.util.Retry).


