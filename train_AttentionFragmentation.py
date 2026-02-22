import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model    import LogisticRegression
from sklearn.metrics         import accuracy_score,classification_report,confusion_matrix,ConfusionMatrixDisplay

data=pd.read_csv("ml_ready_attention_fragmentation_data.csv")
data.head()
Attention_Fragmentation_Score_col=['Daily_screen_time','Notif_check_freq','Video_preference','Perceived_prod_reduction','Screentime_regret']
#Define features(X) and target variable(y)
y=data["Attention_fragmentation_class"]
X=data[Attention_Fragmentation_Score_col]

# Train(80%) and test (20%) with stratify parameter to ensure proportion of
# classes is preserved
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=3,stratify=y)

#Applied Logistic Regression
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)

#Model prediction
y_predic=model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,y_predic))
print(classification_report(y_test,y_predic))

#Average of cross validation scores as a small dataset was used
scores=cross_val_score(model,X,y,cv=5)
print("Scores:",scores)
print("Average accuracy:",scores.mean())

#Feature Weightage
importance=pd.DataFrame({"Feature":X.columns,"Weight":model.coef_[0]}).sort_values(by="Weight",ascending=False)
importance

#Distribution Analysis
for col in data.columns:
  if col!="Attention_fragmentation_class" and col!="Id" :
    plt.figure(figsize=(6,4))
    sns.histplot(data[col],bins=data[col].nunique(),kde=False)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Number of participants")
    plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="Attention_fragmentation_class",data=data)
plt.title(f"Distribution of Attention Fragmentation Class")
plt.xlabel("Attention Fragmentation Class")
plt.ylabel("Number of participants")
plt.show()

#Correlation Heatmap
plt.figure(figsize=(12,8))
data_corr=data.drop(columns=['Id'], errors='ignore')
corr=data_corr.corr()
sns.heatmap(corr,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Heatmap of Survey Features and Target")
plt.show()

#Coefficient-based Feature Importance Analysis
coef=pd.Series(model.coef_[0],index=X.columns)
coef=coef.sort_values(ascending=True)

plt.figure(figsize=(8,6))
coef.plot(kind='barh')
plt.title('Logistic Regression Coefficients')
plt.xlabel('Coefficient Value')
plt.ylabel('Attention Fragmentation Variables')
plt.show()

#Confusion Matrix
y_predi=model.predict(X_test)
cm=confusion_matrix(y_test,y_predi)
disp=ConfusionMatrixDisplay(cm)
disp.plot(cmap='Greens')
plt.title('Confusion Matrix')
plt.show()