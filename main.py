age = int(input('how old are you man?: '))
grade = int(input('В каком классе вы учитесь?: '))

if age >= 10 and grade >= 800:
    print('condfirm')
else:
    print('Доступ запрещен.')
import time
start_time= time.time()
def fun():
    a=27
    b=42
    c=a+b
end_time= time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken) 
