# Find out another global variable that is used inside functions.
# What is the difference between this global variable and known? Why?

# A. If a global variable refers to a mutable value, you can modify the value without declaring the variable.

# !!BE CAREFUL!!: Global variables can be useful, but if you have a lot of them, and you modify them frequently,
# they can make programs hard to debug.
# Read more about local and global variables: 
# https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python