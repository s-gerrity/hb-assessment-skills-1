"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################

"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""

# Write your function here
def is_hometown(hometown):
    if hometown == 'Oakland':
        return True
    return False


"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""

# Write your function here
def full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
        return full_name

"""PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""

def hometown_greeting(first_name, last_name, hometown):
    full_name = f"{first_name} {last_name}"
    if hometown == 'Oakland':
        return print(f"Hi {full_name}, we're from the same place!")
    else:
        return print(f"Hi {full_name}, I'd like to visit {hometown}!")

"""PROMPT 4

Write a function that returns True if a fruit is a berry.

Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""

# Write your function here
list_of_berries = ['strawberry', 'raspberry', 'blackberry', 'currant']
def is_berry(fruit):
    for berry in list_of_berries:
        if fruit == berry:
            return print(True)
    return print(False) 

"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""

# Write your function here
berry_ship_price = 0
ship_price_not_berries = 5

list_of_berries = ['strawberry', 'raspberry', 'blackberry', 'currant']
def shipping_cost(item):
    for berry in list_of_berries:
         if item == berry:
            return print(berry_ship_price)
    return print(ship_price_not_berries)
    

"""PROMPT 6

Write a function that returns the total cost of something by applying
taxes and fees of various states.

States will be given as their two-letter abbreviations. For example,
California's abbreviation is 'CA'.

There are some states with special fees. All fees should be added to the new
subtotal *after* tax:
    - CA (California): add a 3% (0.03) tax for recycling
    - PA (Pennsylvania): add $2.00 safety fee
    - MA (Massachusettes):
        - add $1.00 for items with a base price of $100.00 or less
        - add $3.00 for items over $100.00

Arguments:
    - Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)

Return:
    - Total price after taxes and fees (float)
"""

# Write your function here
def total_cost(base_price, state, tax=0.05):
    recycling_fee_ca = .03
    safety_fee_pa = 2
    item_under_or_equal_100_ma = 1
    item_over_100_ma = 3
    if state == 'MA':
        if base_price <= 100:
            return print(((base_price * tax) + base_price) + item_under_or_equal_100_ma)
        elif base_price > 100:
            return print(((base_price * tax)+ base_price) + item_over_100_ma)
    elif state == 'PA':
        return print(((base_price * tax) + base_price) + safety_fee_pa)
    elif state == 'CA':
        return print((base_price * recycling_fee_ca) + (base_price * tax) + base_price)
    else:
        return print((base_price * tax) + base_price)

"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the  list and return
the list.

We haven't taught you how to do this! You'll need to do some research on your
own --- find a way to write a Python function that can take in an arbitrary
amount of arguments.

Arguments:
    - A list (list)
    - Additional args

Return:
    - A list with arguments added to the end (list)
"""

# Write your function here


"""PROMPT 8

Write a function that takes in a word and returns a tuple. You'll do this in an
interesting way though, so make sure you read these directions thoroughly.

The tuple will contain two items:
    - The given word
    - The given word, multiplied 3 times

To do this, your function will create an *inner* function. The *inner*
function will multiply the given word by 3 and return it.

Then, the outer function will call the *inner* function to create a tuple.

Examples:
    - 'hi' -> ('hi', 'hihihi')

Arguments:
    - A word (str)

Return:
    - (word, wordx3) (tuple)
"""

# Write your function here

