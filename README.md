# Example 1

- Basic form submission
  - avoid POST/Redirect/GET
  - template fragment as response
- `example_1_1` directory contains django without htmx
- `exmaple_1_2` directory contains django with htmx

# Example 2

- Input validation
  - avoid waiting for form submission to get feedback for errors
- `example_2_1` directory contains django without htmx
- `exmaple_2_2` directory contains django with htmx

# Example 3

- Dropdown menu
  - avoid using APIs
- `example_3_1` directory contains django without htmx
  - uses javascript for fetching the dropdown contents from an API
- `exmaple_3_2` directory contains django with htmx

# Running the examples

## Prerequisite

- Python
- pip

## Packages

In the root directory of this repo, install required packages

```
$ python -m pip install --upgrade pip
$ python -m pip install -r requirements.txt
```

## Run the server

In any of the examples directory, execute the commands below

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Alternatively, you can also add default data

```
$ python manage.py seed 
```
