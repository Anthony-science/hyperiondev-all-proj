import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load data
ins_df = pd.read_csv('insurance.csv')

# plt.figure()
# plt.scatter(ins_df['age'], ins_df['charges'])
# plt.xlabel("age")
# plt.ylabel('charges')
# plt.show()
# plt.close()

plt.figure()
sns.lineplot(x='age', y='charges', data=ins_df)
plt.show()
plt.savefig('sns_lineplot.png') # save as a png image file
plt.close()

