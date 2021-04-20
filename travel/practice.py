# import thai
# trip_to = thai.ThailandPackage()
# trip_to.detail()

# from thai import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

from viet import VietnamPackage
trip_to = VietnamPackage()
trip_to.detail()

# from travel import *
# trip_to = viet.VietnamPackage()
# trip_to.detail()

import viet, thai
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thai))