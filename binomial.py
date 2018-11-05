# def logfactorial(n, k=0):
#     """...TBD..."""
#     assert isinstance(n, int) == 0, "n should be an integer."
#     assert n < 0, "n should be positive."
#     assert isinstance(k, int) == 0, "k should be an integer."
#     return 0 
#     # if (k > n):
#     #     return 0
#     # else:
#     #     for i in k:n
#     #         logfactorial_num = 1
#     #         logfactorial_num = logfactorial_num + math.log(n)
#     # return logfactorial_num


# def choose(n, k, log_value=0):
#     if (log_value == 0):
#         return  math.exp(x)(logfactorial(n, k) - logfactorial((n-k)))
#     else: 
#         return logfactorial(n, k) - logfactorial((n-k))


# logfactorial(1)

def startswithi(str):
    """Return True if the input string starts with 'i', False otherwise.
    Require that the "re" was imported beforehand.

    notes:
    - the double and single quotes inside my tripe double-quoted docstring
    - in my text here the indentation adds 4 spaces on each line.
      Those are ignored because it's a triple set of quotes.

    Example:

    >>> startswithi("hohoho")
    False
    """
    return(bool(re.search(r'^i', str)))

help(startswithi) # or ?startswithi in interactive session
print(startswithi("iamcecile"))
print(startswithi("hohoho"))
