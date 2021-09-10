#addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).
addition_str = "2+5+10+20"
spt = addition_str.split("+")
list1 = list(spt)
total = 0
list1 = [int(i) for i in list1]
print(str(list1))
for ele in range(0, len(list1)):
    total = total + list1[ele]
sum_val = int(total)
print(sum_val)