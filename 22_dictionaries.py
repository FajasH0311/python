## this add the key values for examble name, email, pass these are the key values to be stored in a email creation
customer = {
    "name": "EVE",
    "age": 30,
    "is_verified": True
}
## you can add dictionaries
customer["birthdate"] = "Jan 1 2000"

print(customer.get("birthdate"))

## you can add a default value by giving customer.get("name", "#default u need to give")
