def count(list):


    even=0
    odd = 0

    for i in list:
       if i%2==0:
           even+=1
       else:
           odd+=1

    return odd,even


list=[1,2,4,5,6,8,10]

even,odd=count(list)
print(f"even =-{even },odd =-{ odd}")
