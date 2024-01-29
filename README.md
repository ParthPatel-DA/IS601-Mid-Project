# Project Name: Midterm Project (Dosa Restaurant)

IS601 - Web Systems Development - Mid Project

## Project Goal:

1. Reads the JSON orders from a file whose name is passed as the first positional argument.

2. Creates a new JSON file named customers.json that contains an object with phone numbers as keys and customers names as values. The phone number and customer name should both be strings and the phone number should be of the form xxx-xxx-xxxx

```json
{
    "609-555-0124": "Karl",
    "732-555-1234": "Mike",
    ...
}
```

3. Create a new JSON file named items.json that contains an object with item names (string) as keys and an object with price (key=price, number) and number of times it has been ordered (key=orders, number) as a value:

```json
{
    "Butter Masala Dosa": {
        "price": 12.95,
        "orders": 52
    },
    "Butter Mysore Masala Dosa": {
        "price": 11.95,
        "orders": 12
    },
    ...
}
```

## Steps to run the project:

...

## Change Logs:

| S.No | Date       | Change Description           |
| ---- | ---------- | ---------------------------- |
| 1    | 01-28-2024 | Added example data JSON file |
| 2    | 01-28-2024 | Added README.md file         |

## References:

#### Project Requirement:

https://web.njit.edu/~rt494/python_web_api/midterm-project.html

#### JSON File:

https://raw.githubusercontent.com/rxt1077/IS601/master/midterm_project/example_orders.json
