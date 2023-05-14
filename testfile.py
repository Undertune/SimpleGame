import pandas as pd
import matplotlib.pyplot as plt

data = {'tasks': [300, 500, 700]}
df = pd.DataFrame(data, index=['tasks_pending', 'tasks_ongoing', 'tasks_completed'])

df.plot.pie(y='tasks', figsize=(5, 5), autopct='%1.1f%%', startangle=90)
plt.show()