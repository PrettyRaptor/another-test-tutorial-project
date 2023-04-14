import collections

a = 'aaaaabbbbccc'
my_counter = collections.Counter(set(a))
print(my_counter)

print(my_counter.most_common())