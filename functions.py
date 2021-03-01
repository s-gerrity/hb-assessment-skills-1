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
    """Return `True` if a town name matches the name of my hometown"""

    #Compare if the hometown arguement is the same as my hometown
    if hometown == 'Oakland':
        #If it is the same, return `True`
        return True

    #If it is not the same, return `False`    
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
    """Take in a first and last name to return a full name."""

    #Use an f-string to combine first and last name arguments 
    # to make the full name
    full_name = f"{first_name} {last_name}"
        #Surface the full name
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
# Write your function here

def hometown_greeting(first_name, last_name, hometown):
    """Print a greeting according to if you have the same hometown and address them by name."""

    #Combine first and last name to make their full name
    full_name = f"{first_name} {last_name}"
    #Compare the users hometown to our hometown
    if hometown == 'Oakland':

        #Message for if hometowns are the same
        return print(f"Hi {full_name}, we're from the same place!")

        #Message if they are different hometowns
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

BERRIES = ['strawberry', 'raspberry', 'blackberry', 'currant']
#Official list of berries

def is_berry(fruit):
    """Determine if a fruit mentioned qualifies as a berry."""

    #Check each berry in official list of berries
    for berry in berries:
    
        #Compare fruit input to our official list of berries
        if fruit == berry:

            #If the fruit input is in our berry list, return `True`
            return print(True)

    #If the fruit is not a berry, return `False`        
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

#Berries ship for a different price than all items
BERRY_SHIP_PRICE = 0
#Everything else does not ship for free
SHIP_PRICE_NOT_BERRIES = 5

#Official list of items that qualify as a berry
BERRIES = ['strawberry', 'raspberry', 'blackberry', 'currant']


def shipping_cost(item):
    """Determine shipping cost according to item; all items have the same shipping EXCEPT berries"""

    #Check through each berry in the official list
    for berry in berries:
        #If the item is a berry, determine price
        if item == berry:
            #Surface berry specific ship price
            return print(berry_ship_price)
    #Surface price for any non-berry item       
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
    """Get total order cost based on item, state, and tax. 
    Some states have special fees. If tax is not specified, default to 5%"""

    #Special fees for CA, PA, & MA in US dollars $ or percentages %
    recycling_fee_ca = .03
    safety_fee_pa = 2
    item_under_or_equal_100_ma = 1
    item_over_100_ma = 3

    #Check if state is MA (Massachusettes) bc special fees apply for base price totals
    if state == 'MA':
        #Orders under $100 have a special fee
        if base_price <= 100:
            #Calculate total with tax, special fee, and base price
            return print(((base_price * tax) + base_price) + item_under_or_equal_100_ma)
        #Orders over $100 have a special fee
        elif base_price > 100:
            #Calculate total with tax, special fee, and base price
            return print(((base_price * tax)+ base_price) + item_over_100_ma)

    #Check if state is PA (Pennsylvania) bc special fees apply for safety fee on all PA orders        
    elif state == 'PA':
        #Calculate total with tax, special fee, and base price
        return print(((base_price * tax) + base_price) + safety_fee_pa)

    #Check if state is CA (California) bc special tax applies for recycling fee on all CA orders
    elif state == 'CA':
        #Calculate total with tax, special fee, and base price
        return print((base_price * recycling_fee_ca) + (base_price * tax) + base_price)

    #If state not MA, PA, CA proceed to calculate tax and base price
    else:
        #Surface total
        return print((base_price * tax) + base_price)

"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the list and return
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

def growing_to_do_list(todays_to_do_list, *argv):
    """For our to-do list that we start every morning, we add any amount 
    of new items midday. This list will add the new items."""

    #New additions to add to the main to-do list for today
    midday_to_do_list_adds = [*argv]
    #Review each item in the new to-do list
    for item in midday_to_do_list_adds:

        #Add the new items from the midday list to our final to-do list for today
        todays_to_do_list.append(item)

    #Surface the final to-do list for today    
    return print(todays_to_do_list)

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

def call_and_response(call):
    """For our protest this weekend, we have a call and response for the group."""

    #The response to the call should be repeated 3 times
    response = call * 3
    #Our official protest song is the call then the response (the call three times)
    protest_song = (call, response)
    #Shout our protest song!
    return print(protest_song)
