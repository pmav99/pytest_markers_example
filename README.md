Try the following:

- `pytest -v` which will skip both schism and delft tests
- `pytest -v --rundelft` which will skip schism tests
- `pytest -v --runschism` which will skip delft tests
- `pytest -v --rundelft --runschism` which will not skip any tests
