# import module
# module.price(3)
# module.price_morning(3)
# module.price_student(3)

import module as mv #nickname
mv.price(3)
mv.price_morning(3)
mv.price_student(3)

from module import * #all
price(3)
price_morning(3)
price_student(3)

from module import price_morning as morning
morning(5)

