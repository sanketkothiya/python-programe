# 1)
# s = input()
# words = [word for word in s.split(" ")]
# print (" ".join(sorted(list(set(words)))))


# 2)

# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)


# 3)


# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print (",".join(values))


# 4)


# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print( f" letter is  ",d["LETTERS"])
# print( "DIGITS", d["DIGITS"])


# 5)

# s = input("enter the sentence we provide which is upper case and whuch is lower case character list")
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print ("UPPER CASE", d["UPPER CASE"])
# print ("LOWER CASE", d["LOWER CASE"])

# 6)


# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print (n1+n2+n3+n4)

# 7)

s=input("enter the number")
x=[y for y in s.split(",") if int(y)%2!=0]
print(",".join(x))

# values = raw_input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print ",".join(numbers)