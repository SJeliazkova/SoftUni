# брой маси = брой покривки = брой карета - цяло число от конзолата
# дължина на правоъгълните маси в метри
# ширина на правоъгълните маси в метри
# изчисляване площта на покривките = брой *( дължина +2 * 0.3 ) * ( ширина + 2 * 0.3)
# изчисляване площта на каретат = брой * дължина/2 * ширина/2
# цена покривки = площ покривка * 7 долара
# цена карета = площ каре * 9 долара
# крайна цена в долари = цена покривки + цена карета - до 2 знак
# крайна цена в левове = крайна цена в долари * курс (1.85) - до 2 знак

number_of_tables = int(input())
lenght = float(input())
width = float(input())

area_of_tablecloth = number_of_tables * (lenght + 2 * 0.3) * (width + 2 * 0.3)
area_of_quads = number_of_tables * ( lenght / 2 ) * ( lenght / 2)
price_of_tablecloth = area_of_tablecloth * 7
price_of_quads = area_of_quads * 9

total_price_usd = price_of_quads + price_of_tablecloth
total_price_bgn = total_price_usd * 1.85

print(f"{total_price_usd:.2f} USD")
print(f"{total_price_bgn:.2f} BGN")
