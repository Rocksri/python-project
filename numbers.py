x = "89e9jcd^o38829@3%3,/mkl$w1"

# Using list comprehension
result = "".join([i for i in x if i.isnumeric()])
print(result)

# Using regular expression
import re
result = re.sub("[^0-9]", "", x)
print(result)
