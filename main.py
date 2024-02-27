age = int(input('how old are you?: '))
grade = int(input('В каком классе вы учитесь?: '))

if age >= 10 and grade >= 60:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
import time
start_time= time.time()
def fun():
    a=10
    b=3000
    c=a+b
end_time= time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken) # 0.01
