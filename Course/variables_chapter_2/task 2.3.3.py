#task 2.3.3
number_of_briks = int(input("Please enter 3 numbers: "))
hundreds = number_of_briks // 100
singles = number_of_briks % 10
tens = (number_of_briks // 10) % 10
print(hundreds, tens, singles)

sum_of_all_briks = hundreds + singles + tens
print(sum_of_all_briks)

devide_between_pigs = sum_of_all_briks // 3
print (devide_between_pigs)

modulo_briks_per_pig = sum_of_all_briks % 3
print(modulo_briks_per_pig)

is_it_true = bool(modulo_briks_per_pig ==0)
print(is_it_true)