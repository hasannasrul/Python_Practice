# #-----------    list is  mutabale sequence
# x = [1,2,3,4,7,9,10]
# for i in x:
#     print("x is {}".format(i))

# #-----------    tuple is immutable also range()
# y = (1,23,3,4,5,6,7)
# for i in y:
#     print("y is {}".format(i))

# #----------- dictionary is key value pair and is also mutable
z = {'one': 1,'two':3, 'three':3}
for k,v in z.items():
    print("key:{} value:{}".format(k,v))

# QUESTION 1
x = [1,2,3,4,7,9,10]

if type(x) == "list":
    print("yep")
else:
    print("nope")

#solution 1

if isinstance(x,list):
    print("yep")
else:
    print("nope")