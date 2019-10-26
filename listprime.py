import time

print("list the range in which you want to find prime number \n")
minrange = int(input("min range = "))
maxrange = int(input("\nmax range = "))
count = 0
lis = []
start_time = time.time()
for i in range(minrange,maxrange):
    if i % 2 !=0 and i % 3 !=0 and i % 5 !=0 and i % 7 !=0:
        lis.append(str(i))

end_time = time.time()
print(lis)
end_time2 = time.time()
e_t = end_time - start_time
l_t = end_time2 - start_time
print(e_t, "\n", l_t, "\n", l_t - e_t)
