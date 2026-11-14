#FUNCTION WRITING GUIDE 
# Our goal is alwys writing functions that are easy to read and understand, for you and others. 
# PEP8 -STYLE GUIDE:
#Example:

def calculate_discount(price: float, rate: float) -> float: 
    """
    Calculate the final price after applying a discount
    Args: 
        price(float): Original product price.
        rate(float): Discount rate as numbers(e.g 20 for 20%)
    Returns:
        fianl_price(float): Final price after applying discount. 
    """
    final_price = price - (price * rate/100)
    return final_price
print(calculate_discount(80, 20))



# 1. Use snake_case for function names - write function names in lowercase and separate words with underscores. 
# 2. Use clear descriptive function names - describe exactly what the function does; start with a verb; use full words, avoid abbreviations 
# 3. Parameter names should describe their values - use full, meaningful words, avoid abbreviations and single letters
# 4. Always describe functions using Docstring """""" - helps teammates understand your code; helps you remember your logic in future. Docstring """""" is a short text on the first line inside a function that explains what the function does. We don't use comment # because python ignores comments, they are only notes for use (it is lost). Rather, we use docstring """""" because python stores it inside the function and can be reused by tools, editors. Docstring can be used by functions, tools, IDEs etc. 
# 5. Replace Prints with Return to send data back to the program 
# 6. Don't change parameter values directly, create local variables for any processing. 

# OTHERS: 
# 1. Return one-line expression directly - put simple calculations directly inside the return statement instead of storing them in extra variables.  (e.g. return price - price(price * rate/100))
# 2. Use data type hints - always add type hints to parameters and return to make the function easier to understand. This is important because in real projects, most bugs come from wrong data types. e.g. price: float - float here is only a hint, it does not convert. for return use ->
# 3. Explain Args and Return in Docstring - always describe what goes in and what comes out of the function in the docstring. 