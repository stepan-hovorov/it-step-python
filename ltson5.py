many = 10000
my_bascket = {}
ware_1 = input()
my_bascket[ware_1.split(' ')[0]] = int((ware_1.split(' '))[1])
ware_2 = input()
my_bascket[ware_2.split(' ')[0]] = int((ware_2.split(' '))[1])
ware_3 = input()
my_bascket[ware_3.split(' ')[0]] = int((ware_3.split(' '))[1])
ware_4 = input()
my_bascket[ware_4.split(' ')[0]] = int((ware_4.split(' '))[1])
ware_5 = input()
my_bascket[ware_5.split(' ')[0]] = int((ware_4.split(' '))[1])
total_cost = sum(my_bascket.values())
print('We bought these :')
print('ware -', my_bascket.popitem())
print('ware -', my_bascket.popitem())
print('ware -', my_bascket.popitem())
print('ware -', my_bascket.popitem())
print('ware -', my_bascket.popitem())
print("Total cost-", total_cost)

if many >= total_cost:
    print(total_cost-many)
elif many <= total_cost:
    print('грошей не вистачає')