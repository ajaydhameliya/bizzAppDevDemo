
import pandas as pd

ajay = pd.read_csv(r'C:\Users\hp\PycharmProjects\pythonProject\CSV\p3.csv')
ajay1 = pd.DataFrame(ajay, columns=['Barth Date', 'Age'])
print(ajay1)

