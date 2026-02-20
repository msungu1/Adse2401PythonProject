# python script to demonstarte random forest algorithim to predict customer churn a fictional store(maji mazuri traders)

#import the required modules
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

#1.create a random dataset (150 customer)

np.random.seed(42)

data = pd.DataFrame(
    {
        'Age':np.random.randint(18,70, 150),
        'Monthly_spend':np.random.randint(1500,45000, 150),
        'Visits_Per_Month':np.random.randint(4,30,150),
        'Mmeber_Years':np.random.randint(0,15,150),
        'Used_Discount':np.random.randint(0,2,150),  # 0 ->No, 1 -> Yes

    }
)

#create churn label
data["Churn"] = (
(data["Monthly_spend"]<10000) &
(data["Visits_Per_Month"]<9)
).astype(int)

#2.prpare data
x = data.drop('Churn',axis=1)
y = data['Churn']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=3, random_state=42)

#train the random forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

#4.predictions
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)*100
print(f"random forest accuracy: {accuracy: 2f}")

cm =confusion_matrix(y_test, y_pred, labels=[0,1])

fig_cm = px.imshow(
    cm,text_auto=True,labels=dict(x="Predcted",y="Actual",color="Count"),
    x=["No Churn","Churn"],
    y=["No Churn","Churn"],
    title="Confusion Matrix - customer churn",
)
fig_cm.show()

#7,churn distribution visualization
fig_churn = px.pi(
    data,
    names="Churn",
    title="overall customer churn distribution ",
    labels={"churn":"Churn status"},
)

fig_churn.update_traces(
    textinfo='percent + label',
)

fig_churn.show()