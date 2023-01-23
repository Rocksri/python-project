name = "Guvi python"

# Using string slicing
result = name[5:]
print(result)

# Using string split() method
result = name.split(" ")[-1]
print(result)

# Using regular expression
import re

result = re.search("[a-zA-Z]+$", name).group()
print(result)
