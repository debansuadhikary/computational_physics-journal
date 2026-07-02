# PyPI = Python Programming Index is a library of all the packages that are open source and we may use in order to ease our misery (URL = pypi.org)
# One among them is "cowsay" which we can understand in the following code 

import cowsay
import sys

# if len(sys.argv) == 2:
#     cowsay.trex("hello," + sys.argv[1])

# here we are importing our own module form a different code 
from sayings import hello
if len(sys.argv) == 2:
    hello(sys.argv[1])

