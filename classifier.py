import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#df = pd.read_csv("/content/mlops1/data/Iris.csv")

# azureml-core of version 1.0.72 or higher is required
# azureml-dataprep[pandas] of version 1.1.34 or higher is required

from azureml.core import Workspace, Dataset

subscription_id = '8a2e81e7-89f6-4b3e-bba1-390c3f74abe7'
resource_group = 'joeachakji-rg'
workspace_name = 'joes-workspace'

workspace = Workspace(subscription_id, resource_group, workspace_name)

dataset = Dataset.get_by_name(workspace, name='Iris')
df = dataset.to_pandas_dataframe() # dont forget to edit this line

features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
taget = 'Species'

X_train, X_test, y_train, y_test = train_test_split(df[features],df[taget] , test_size=0.1, shuffle=True)
#step-1: initialise the model class
clf = DecisionTreeClassifier(criterion="entropy") #Information gain as criteria
#step-2: train the model on training set
clf.fit(X_train,y_train)
#step-3 evaluate the data on testing set
y_pred = clf.predict(X_test)

print(f"Accuacy of the model is {accuracy_score(y_test,y_pred)*100}") #--> this test accuracy