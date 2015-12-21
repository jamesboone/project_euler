
nums = []

for i in xrange(1, 1001):
    num_as_list = [int(x) for x in str(i)]
    if num_as_list[-1] % 5 == 0:
        nums.append(i)
    elif sum(num_as_list) % 3 == 0:
        nums.append(i)
print nums
