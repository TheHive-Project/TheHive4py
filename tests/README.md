# What you need to know

TBD
You'll need a development licence to execute the tests through pytest. You can request one licence to the Strangebee team by contacting them.

## How initialize my development environment?

1. Open a command line windows move to the `tests` folder. Check that you have the `docker-compose.yml` file

2. Run the following command:

```bash
docker compose -p thehive4py-integration-tests up -d
```

This will initialize the development environment for the first time, especially databases.

3. Wait until TheHive become available at `http://localhost:9000` (if default port wasn't changed) and connect with the default credentials

4. Once you are connected, go on the settings to activate your development licence

5. Create two new organisations named respectively "test-org" and "share-org" (description is free)

6. Add the user `admin@thehive.local` as `org-admin` for both organisations

## How can I run the tests?

Simply run the following command as soon as your development environment is initialized

```bash
pytest -x
```
