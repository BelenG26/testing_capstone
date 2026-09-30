"""
Generate quoted for lawn mowing service.
small lawn = $10
medium lawn = $15
large lawn = $20

Add on $5 for same-day service

"""

def lawn_quote(size, same_day):
    if size == "small":
        price = 10
    elif size == "medium":
        price = 15
    elif size == "large":
        price = 20
    else:
        return # cant calculate- return none
    if same_day:
        price += 5

    return price