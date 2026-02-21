def sum(*nums):
    s = 0
    for i in nums:
        s += nums
    print (s)
print(sum(1,2,3,4))

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")