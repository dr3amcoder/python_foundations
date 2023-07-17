# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==

def is_valid(password):  #defining function with one argument - password
    if len(password) <= 7:  #if statement to check length of password
        return False #return False if password length is less than or equal 7
    
    special_char = ["!", "@", "$", "%", "&"] # list created to contain specified special chars

    for char in special_char: #for loop; iterate through special_char list
        if char in password: #if statement to check if char in password
            return True #return result as bool - True
    else: #else statement, part of for loop to check if char in special_char, if not
        return False #return this result as bool value - False