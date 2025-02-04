# -*- coding: utf-8 -*-
"""Data_Visualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mp_0z9q-G9Q-S9IhSWGlb7jWdpDQ-SXP
"""

import pandas as pd
from google.colab import files
import matplotlib.pyplot as plt

uploaded = files.upload()
filename = list(uploaded.keys())[0]

df = pd.read_csv(filename)

# Count the occurrences of each job title
job_counts = df['review_jobTitle'].value_counts()
top_job_counts = job_counts.head(10)
x=top_job_counts.index
y=top_job_counts.values
plt.barh(x,y)
for index, value in enumerate(y):
  plt.text(value,index,str(value))
plt.title('Top 10 Job Roles')
plt.xlabel('Employee Count')
plt.figure(figsize=(6,13))
plt.show()

# Count the occurrences of each work location
location_counts = df['review_workLocation'].value_counts()
top_location_counts = location_counts.head(10)
x=top_location_counts.index
y=top_location_counts.values
plt.barh(x,y)
for index, value in enumerate(y):
  plt.text(value,index,str(value))
plt.title('Top 10 Work Locations')
plt.xlabel('Employee Count')
plt.show()

rating_counts = df['review_ratingValue'].value_counts().sort_index(ascending=False)
rating_counts.plot(kind='bar', title='Overall Rating Count', xlabel='Rating', ylabel='Rating Count')
# Display the plot
plt.show()

rating_counts = df['rating_promotions'].value_counts().sort_index(ascending=False)
org_rating_counts = rating_counts.head(5)
org_rating_counts.plot(kind='bar', title='Promotion Rating Count', xlabel='Rating', ylabel='Rating Count')
# Display the plot
plt.show()

rating_counts = df['rating_skilldev'].value_counts().sort_index(ascending=False)
org_rating_counts = rating_counts.head(5)
org_rating_counts.plot(kind='bar', title='Skill Development Rating Count', xlabel='Rating', ylabel='Rating Count')
# Display the plot
plt.show()

rating_counts = df['rating_culture'].value_counts().sort_index(ascending=False)
org_rating_counts = rating_counts.head(5)
org_rating_counts.plot(kind='bar', title='Work Culture Rating Count', xlabel='Rating', ylabel='Rating Count')
# Display the plot
plt.show()

rating_counts = df['rating_worklifebal'].value_counts().sort_index(ascending=False)
org_rating_counts = rating_counts.head(5)
org_rating_counts.plot(kind='bar', title='Worklife Balance Rating Count', xlabel='Rating', ylabel='Rating Count')
# Display the plot
plt.show()

rating_counts = df['rating_jobsecurity'].value_counts().sort_index(ascending=False)
org_rating_counts = rating_counts.head(5)
org_rating_counts.plot(kind='bar', title='Job Security Rating Count', xlabel='Rating', ylabel='Rating Count')
# Display the plot
plt.show()

rating_counts = df['rating_salarybenifits'].value_counts().sort_index(ascending=False)
org_rating_counts = rating_counts.head(5)
org_rating_counts.plot(kind='bar', title='Salary Benefits Rating Count', xlabel='Rating', ylabel='Rating Count')
# Display the plot
plt.show()

rating_counts = df['rating_worksatis'].value_counts().sort_index(ascending=False)
org_rating_counts = rating_counts.head(5)
org_rating_counts.plot(kind='bar', title='Work Satisfaction Rating Count', xlabel='Rating', ylabel='Rating Count')
# Display the plot
plt.show()