age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))

if age >= 20 and grade >= 5:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
import time
start_time= time.time()
def fun():
    a=2
    b=3
    c=a+b
end_time= time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken) # 0.0345
