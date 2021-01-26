# променливи от конзолата за дължина и ширина на залата в м, страна на гардероба в м
# площ на залата = дължина * ширина в м
# площ на гардероба = страна на гардероба * страна на гардероба
# площ на скамейка = площ на залата / 10
# свободно пространство = площ на залата - площ гардероб - площ скамейка
# брой на танцьорите = свободно пространство / 0.704
# принт брой на танцьорите закръглен до цяло число надолу - math.floor

import math
l = float(input())
w = float(input())
a = float(input())

area_hall = l * w
area_wardrobe = a * a
area_bench = area_hall / 10
free_space = area_hall - area_bench - area_wardrobe
count_dancers = free_space / 0.704

print(math.floor(count_dancers))