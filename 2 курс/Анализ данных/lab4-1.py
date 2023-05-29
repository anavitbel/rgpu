xi = (1, 2, 3, 4, 5, 6)
ni = (2, 3, 6, 8, 22, 9)
mx = []
wx = []
n = sum(ni)

mx.append(ni[0])
mx.append(ni[0] + ni[1])
mx.append(ni[0] + ni[1] + ni[2])
mx.append(ni[0] + ni[1] + ni[2] + ni[3])
mx.append(ni[0] + ni[1] + ni[2] + ni[3] + ni[4])
mx.append(sum(ni))
wx.append(mx[0] / n)
wx.append(mx[1] / n)
wx.append(mx[2] / n)
wx.append(mx[3] / n)
wx.append(mx[4] / n)
wx.append(mx[5] / n)


print(f"Вариационные ряды и их графическое изображение. Задание 2\n")
print(f"Тарифный разряд xi      {xi[0]}      {xi[1]}     {xi[2]}      {xi[3]}      {xi[4]}      {xi[5]}       n   {n}")
print(f"Количество рабочих ni   {ni[0]}      {ni[1]}     {ni[2]}      {ni[3]}      {ni[4]}     {ni[5]}")
print(f"mx                      {mx[0]}      {mx[1]}     {mx[2]}     {mx[3]}     {mx[4]}     {mx[5]}")
print(f"wx                      {wx[0]}   {wx[1]}   {wx[2]}   {wx[3]}   {wx[4]}   {wx[5]}")
