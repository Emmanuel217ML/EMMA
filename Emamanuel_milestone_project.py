number = -1
the_list = []
print("Enter a list of numbers, type 0 when finished")

last = 0
average = 0
while number != 0:
    number = int(input("Enter a number: "))
    if number != 0:
        the_list.append(number)


for numbers in the_list:
    last += numbers

average = last / len(the_list)

largest_num = the_list[0]

for numbers in the_list:
    last += numbers
    if numbers > largest_num:
        largest_num = numbers


print(f"The sum is: {last}")
print(f"The average is: {average}")
print(f"The largest number is: {largest_num}")