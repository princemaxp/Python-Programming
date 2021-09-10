#week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
spt = week_temps_f.split(",")
print(spt)
total = 0
spt = [float(i) for i in spt]
for ele in range(0, len(spt)):
    total = total + spt[ele]
total_temp = float(total)
print(total_temp)
num = 0
for i in spt:
    num += 1
temp_count = num
print(temp_count)
avg_temp = float(total_temp/temp_count)
print(avg_temp)