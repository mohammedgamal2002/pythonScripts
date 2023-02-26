perfect_powers = [1]
power = 2
num = 2
limit = 100
while(power <= 10 and 2**power <= limit):
    print("\nPower : {s}\n".format(s = power))
    num = 2
    while((num**power <= limit)):
        perfect_power = num**power
        print("\t{0}^{1} = {2}".format(num, power, perfect_power))
        perfect_powers.append(perfect_power)
        num = num + 1
    power = power + 1
print("\n\nperfect powers (no-duplicates):\n")
print(sorted(dict.fromkeys(perfect_powers)))

result = sorted(dict.fromkeys(perfect_powers))

def PrintConsecutivePairs(my_list):
    x = my_list[0]
    for i in range(1,len(my_list)):
        if my_list[i] - x == 1:
            print("Pair : ({num1}, {num2})".format(num1 = x, num2 = my_list[i]))
        x = my_list[i]

PrintConsecutivePairs(result)