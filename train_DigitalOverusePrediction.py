import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model    import LogisticRegression
from sklearn.metrics         import accuracy_score,classification_report,confusion_matrix,ConfusionMatrixDisplay

data=pd.read_csv("ml_ready_ROLE OF DOPAMINE IN THE BEHAVIOURAL PATTERNS OF ADULTS.csv")
data.head()


#Define features(X) and target variable(y)
Digital_Overuse_Index_col=['Daily_screen_time','Prod_screen_time','Notif_check_freq','Video_preference']
y=data["Digital_Overuse_Index_class"]
X=data[Digital_Overuse_Index_col]

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
for col in Digital_Overuse_Index_col:
    plt.figure(figsize=(6,4))
    sns.histplot(data[col],bins=data[col].nunique(),kde=False)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Number of participants")
    plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="Digital_Overuse_Index_class",data=data)
plt.title(f"Distribution of Digital Overuse Index Class")
plt.xlabel("Digital Overuse Index Class")
plt.ylabel("Number of participants")
plt.show()

#Correlation Heatmap
plt.figure(figsize=(12,8))
corr=data[Digital_Overuse_Index_col].corr()
sns.heatmap(corr,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Heatmap of Digital Overuse Index Features and Target")
plt.show()

#Coefficient-based Feature Importance Analysis
coef=pd.Series(model.coef_[0],index=X.columns)
coef=coef.sort_values(ascending=True)

plt.figure(figsize=(8,6))
coef.plot(kind='barh')
plt.title('Logistic Regression Coefficients')
plt.xlabel('Coefficient Value')
plt.ylabel('Digital Overuse Index Variables')
plt.show()

#Confusion Matrix
y_predi=model.predict(X_test)
cm=confusion_matrix(y_test,y_predi)
disp=ConfusionMatrixDisplay(cm)
disp.plot(cmap='Greens')
plt.title('Confusion Matrix')
plt.show()