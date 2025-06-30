

import seaborn as sns

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt



# Load the Titanic dataset

titanic_data = sns.load_dataset('titanic')



# Preview the first few rows

titanic_data.head()


print("Shape of the dataset:", titanic_data.shape)

print("\nColumns in the dataset:\n", titanic_data.columns)



# Check for missing values

print("\nMissing values in each column:\n", titanic_data.isnull().sum())



# Data types and summary statistics

print("\nData types:\n", titanic_data.dtypes)

print("\nSummary Statistics:\n", titanic_data.describe(include='all'))

print("\nMissing values in each column:\n", titanic_data.isnull().sum())

print("\nPercentage of missing values in each column:\n", (titanic_data.isnull().sum()/len(titanic_data))*100)



# Create the heatmap

plt.figure(figsize=(10, 6))

sns.heatmap(titanic_data.isnull(), cbar=False, cmap='viridis', yticklabels=False)

plt.title('Missing Values Heatmap')

plt.show()


from sklearn.experimental import enable_iterative_imputer

from sklearn.impute import IterativeImputer

from sklearn.ensemble import RandomForestRegressor



# Create a copy to avoid modifying the original DataFrame

titanic_data_filled = titanic_data.copy()



# Separate numerical and categorical columns

numerical_cols = titanic_data_filled.select_dtypes(include=['number']).columns

categorical_cols = titanic_data_filled.select_dtypes(exclude=['number']).columns



# Use IterativeImputer for numerical features

imputer_num = IterativeImputer(estimator=RandomForestRegressor(), random_state=0)

titanic_data_filled[numerical_cols] = imputer_num.fit_transform(titanic_data_filled[numerical_cols])



# Fill categorical features with the mode (most frequent value)

for col in categorical_cols:

    titanic_data_filled[col] = titanic_data_filled[col].fillna(titanic_data_filled[col].mode()[0])



# Verify if there are any missing values left

print("\nMissing values after imputation:\n", titanic_data_filled.isnull().sum())

print("\nSurvival Count:\n", titanic_data_filled['survived'].value_counts())

sns.countplot(x='survived', data=titanic_data_filled)

plt.title('Survival Count')

plt.show()



# Analyze 'pclass'

print("\nPclass Distribution:\n", titanic_data_filled['pclass'].value_counts())

sns.countplot(x='pclass', data=titanic_data_filled)

plt.title('Passenger Class Distribution')

plt.show()



# Analyze 'age'

print("\nAge Statistics:\n", titanic_data_filled['age'].describe())

sns.histplot(x='age', data=titanic_data_filled, kde=True)

plt.title('Age Distribution')

plt.show()



# Analyze 'sex'

print("\nSex Distribution:\n", titanic_data_filled['sex'].value_counts())

sns.countplot(x='sex', data=titanic_data_filled)

plt.title('Sex Distribution')

plt.show()

print("\nSurvival by Gender:\n", titanic_data_filled.groupby('sex')['survived'].value_counts())

sns.countplot(x='sex', hue='survived', data=titanic_data_filled)

plt.title('Survival by Gender')

plt.show()



# Analyze survival based on passenger class

print("\nSurvival by Passenger Class:\n", titanic_data_filled.groupby('pclass')['survived'].value_counts())

sns.countplot(x='pclass', hue='survived', data=titanic_data_filled)

plt.title('Survival by Passenger Class')

plt.show()



# Analyze survival based on age groups (create age bins)

titanic_data_filled['age_group'] = pd.cut(titanic_data_filled['age'], bins=[0, 18, 65, 100], labels=['Child', 'Adult', 'Senior'])

print("\nSurvival by Age Group:\n", titanic_data_filled.groupby('age_group')['survived'].value_counts())

sns.countplot(x='age_group', hue='survived', data=titanic_data_filled)

plt.title('Survival by Age Group')

plt.show()



# Further exploration: Analyze survival based on combinations of factors

# Example: Survival based on gender and class

print("\nSurvival by Gender and Class:\n", titanic_data_filled.groupby(['sex', 'pclass'])['survived'].value_counts())

sns.catplot(x='sex', hue='survived', col='pclass', kind='count', data=titanic_data_filled)

plt.show()# Survival Based on Embarkation Point

plt.figure(figsize=(10, 5))

sns.countplot(x='embarked', hue='survived', data=titanic_data, palette='Spectral')

plt.title('Survival Based on Embarkation Point')

plt.xlabel('Embarkation Point')

plt.ylabel('Count')

plt.legend(title='Survived', labels=['No', 'Yes'])

plt.show()



# Survival Based on Fare

plt.figure(figsize=(10, 6))

sns.histplot(titanic_data, x='fare', hue='survived', bins=20, kde=True, palette='viridis')

plt.title('Fare Distribution by Survival')

plt.xlabel('Fare')

plt.ylabel('Count')

plt.show()



# Family Size Analysis

titanic_data['family_size'] = titanic_data['sibsp'] + titanic_data['parch']



plt.figure(figsize=(10, 6))

sns.countplot(x='family_size', hue='survived', data=titanic_data, palette='cubehelix')

plt.title('Survival Based on Family Size')

plt.xlabel('Family Size')

plt.ylabel('Count')

plt.legend(title='Survived', labels=['No', 'Yes'])

plt.show()

bins = [0, 12, 18, 40, 60, 80]

labels = ['Child', 'Teenager', 'Adult', 'Middle-aged', 'Senior']

titanic_data['age_group'] = pd.cut(titanic_data['age'], bins=bins, labels=labels)



# Visualize Survival by Age Group

plt.figure(figsize=(10, 6))

sns.countplot(x='age_group', hue='survived', data=titanic_data, palette='magma')

plt.title('Survival Based on Age Group')

plt.xlabel('Age Group')

plt.ylabel('Count')

plt.legend(title='Survived', labels=['No', 'Yes'])

plt.show()



# Correlation heatmap

plt.figure(figsize=(12, 8))

# Select only numeric features for correlation calculation

numeric_features = titanic_data.select_dtypes(include=np.number)

sns.heatmap(numeric_features.corr(), annot=True, cmap='coolwarm', fmt=".2f")

plt.title('Feature Correlation Heatmap')

plt.show()

