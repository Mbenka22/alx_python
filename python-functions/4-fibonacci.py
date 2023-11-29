def fibonacci_sequence(n):
    fibonacci_list=[]
    if n<=0:
        return fibonacci_list
if n>=1:
    fibonacci_list.append(0)
if n >=2:
    fibonacci_list.append(1) 
for i in range(2,n):
    next_number=fibonacci_list[i-1]+fibonacci_list[i-2]
    fibonnacci_list.append(next_number)
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))
    