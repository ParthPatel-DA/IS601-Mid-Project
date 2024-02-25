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

```shell
# Windows
py main.py example_orders.json

# Mac
python3 main.py example_orders.json
```

## Result:

Following files will be generated after running the project:

1. [customers.json](https://github.com/ParthPatel-DA/IS601-Mid-Project/blob/master/customers.json)
2. [items.json](https://github.com/ParthPatel-DA/IS601-Mid-Project/blob/master/items.json)

## Change Logs:

| S.No | Date       | Change Description                                                                                                                                               |
| ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | 01-28-2024 | [Added example data JSON file](https://github.com/ParthPatel-DA/IS601-Mid-Project/commit/27228a002bcc35c1126fd890f0cadf3bb8ef985d)                               |
| 2    | 01-28-2024 | [Added README.md file](https://github.com/ParthPatel-DA/IS601-Mid-Project/commit/c55932b76d55a08eb7733c288435d186ebbc2a4f)                                       |
| 3    | 02-25-2024 | [Added read json file function](https://github.com/ParthPatel-DA/IS601-Mid-Project/commit/9a4a6f1c03a021731cc50a603281b0b99cc0796f)                              |
| 4    | 02-25-2024 | [Added write json file function](https://github.com/ParthPatel-DA/IS601-Mid-Project/commit/efdcb8c2d39602f90a83d9c4c067ec702a847495)                             |
| 5    | 02-25-2024 | [Added generate customer data function](https://github.com/ParthPatel-DA/IS601-Mid-Project/commit/c7df9362ce05b72d07273be9e2e57df134bf0035)                      |
| 6    | 02-25-2024 | [Added generate order data function](https://github.com/ParthPatel-DA/IS601-Mid-Project/commit/6698cda6202eca506d6bbfef87166b00f36354f5)                         |
| 7    | 02-25-2024 | [Updated result data in sorted order](https://github.com/ParthPatel-DA/IS601-Mid-Project/commit/ca6490546dd0d892e36db266cb2cb4147282b062)                        |
| 8    | 02-25-2024 | [Added function to combine all operation in single function](https://github.com/ParthPatel-DA/IS601-Mid-Project/commit/bc648e9df81e8fbd5a5c469ae7d9d882bcd5e429) |
| 9    | 02-25-2024 | [Added both result file](https://github.com/ParthPatel-DA/IS601-Mid-Project/commit/bc6ffdde662c13b174fff91feab6113b674f945b)                                     |
| 10   | 02-25-2024 | [Updated README.md file](https://github.com/ParthPatel-DA/IS601-Mid-Project/commit/7be3789033c6b7f1b41a9365c9ee101e92d59ac9)                                     |

## References:

#### Project Requirement:

https://web.njit.edu/~rt494/python_web_api/midterm-project.html

#### JSON File:

https://raw.githubusercontent.com/rxt1077/IS601/master/midterm_project/example_orders.json
