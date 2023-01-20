# import ipdb to load the library into this file.

# Use ipdb.set_trace() to pause the execution of the code and inspect variables.
def tracing_the_function():
    inside_the_function = "We're inside the function"
    print(inside_the_function)
    print("We're about to stop because of ipdb!")
    
    # use ipdb here!
    
    this_variable_hasnt_been_interpreted_yet = \
        "The program froze before it could read me!"
    print(this_variable_hasnt_been_interpreted_yet)

tracing_the_function()


# Define a function plus_two that takes in a num and adds 2 to the param. Use ipdb to inspect the result before returning

evil_monster = "Bowser"
# Define a function princess_peachs_castle that prints {evil_monster} is trying to kidnap Princess Peach!" to show the scope of the variable

def practicing_function_scope():
  im_trapped_in_the_function = "You can't access me outside this function!"
  
# Attempt to print the variable inside of the practicing_function_scope function

# Add global to the inner variable and print again


