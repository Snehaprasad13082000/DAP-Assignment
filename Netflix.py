import pandas as pd
from matplotlib import pyplot as plt

dataset=pd.read_csv("Korea.csv")
dataf=pd.DataFrame(dataset)
korea=dataf.head(15)
korea.plot(x="nation",y="visitor",kind="bar",title="Visitors to south korea")
plt.show()
