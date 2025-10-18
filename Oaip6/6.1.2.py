#2 пример создания пустого списка с последующим заполнением его в цикле случайными числами:
import random
c = []
i = 0
while i < 10:
    c.append(random.randint(0, 100))
    i += 1
print(c)