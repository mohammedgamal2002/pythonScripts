

list = [1, 3, 5]
summationX = 0
summationXSqr = 0
mean = 0
mean_xSqr = 0
variance = 0

for i in list:
    summationX = summationX + i
    summationXSqr = summationXSqr + pow(i, 2)

mean = summationX / len(list)
mean_xSqr = summationXSqr / len(list)
variance = mean_xSqr - pow(mean, 2)
print("Mean = ", mean)

print(f"Variance = {variance:.2f}".format(variance))

print(f"({mean:.2f}) +- {variance:.2f}".format(mean, variance))
