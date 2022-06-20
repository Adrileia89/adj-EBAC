import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

data = pd.read_csv('gasolina.csv') 
sns.lineplot(x='dia', y='venda', data=data) 
plt.savefig('gasolina.png') 
plt.show()