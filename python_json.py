## Python JSON
# JSON is a syntax for storing and exchanging data
# JSON is text, written with JavaScript object notation

## Python has a built-in package 'json' to work with JSON data
import json

## Parsing JSON - convert from JSON to Python
# use the json.loads() method, resulting in a Python dictionary
ex_json = '{"name":"Michael", "age":26, "city":"Philadelphia"}'
parsed_json = json.loads(ex_json)
print(parsed_json["name"]) # prints 'Michael'

## Converting to JSON
# use the json.dumps() method, resulting in a JSON string
# when you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
# https://www.w3schools.com/python/python_json.asp
ex_pyth_obj = {
    "name": "Timothy",
    "age": 35,
    "married": True,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model":"BMW", "mpg":27.5},
        {"model":"Ford", "mpg":21.5}
    ]
}
print(json.dumps(ex_pyth_obj))

## Formatting
# json.jumps() has parameters to format the results
# 1. 'indent' parameter
# 2. 'separators' parameter
# ex. below uses ". " to separate objects, and " = " to separate keys from values
# 3. 'sort_keys' parameter
print(json.dumps(ex_pyth_obj, indent=4, separators=(". ", " = "), sort_keys=True))