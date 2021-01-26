#променлива за броя на кучетата
#променлива за броя на останалите животни
#пресмятане разходите за храна на кучетата (бр. кучета * 2.50)
#пресмятане разходите за храна на другите животни (бр. животни * 4.0)
#пресмятане общите разходи

dogs = int(input())
other_animals = int(input())
sum_dogs = dogs * 2.50
sum_other_animals = other_animals * 4.0
all = sum_dogs + sum_other_animals
print(f"{all:.2f} lv.")