import math
import sys
from os import rename

import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


name = input("Your name? ")
print(greet(name))
# print(greet("World"))
# print(greet("Torsten"))

# r = requests.get("http://httpbin.org/get")
# print(r.status_code)
