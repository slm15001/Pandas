# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "C:/Users/Sal/Desktop/git pull/UTAUS201807DATA2/homework-instructions/04-Numpy-Pandas/Instructions/PyCitySchools/Resources/schools_complete.csv"
student_data_to_load = "C:/Users/Sal/Desktop/git pull/UTAUS201807DATA2/homework-instructions/04-Numpy-Pandas/Instructions/PyCitySchools/Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head(5)

#school names unique
schools_unique = school_data['school_name'].unique()
#Total Schools Counted
total_school_count= school_data['school_name'].nunique()

#Total Students Counted
total_students_count = school_data_complete['Student ID'].nunique()


#Total Budget Calculate
total_budget = school_data['budget'].sum()

#Average Math score
avg_math_score = student_data['math_score'].mean()

#Average Reading score
avg_reading_score = student_data['reading_score'].mean()

#Math Passing score is 70 or greater
math_scores_flag_70 = student_data['math_score']>=70
student_data["math_scores_flag_70"]= math_scores_flag_70
total_mathscores = []
total_mathscores = len(math_scores_flag_70)
math_70_count= np.count_nonzero(math_scores_flag_70)
math_failing_Count = total_mathscores - math_70_count
math_pass_percent = math_70_count / total_mathscores

#Reading Passing score is 70 or greater
read_scores_flag_70 = student_data['reading_score']>=70
student_data["read_scores_flag_70"]= math_scores_flag_70
total_readscores = []
total_readscores = len(read_scores_flag_70)
read_70_count=np.count_nonzero(read_scores_flag_70)
read_failing_count = total_readscores - read_70_count
read_pass_percent = read_70_count / total_readscores

#Average of Passing Rate
avg_pass_rate = (read_pass_percent + math_pass_percent)/2

#Data Frame for District Summary
School_df = pd.DataFrame({
    "Total Schools": [total_school_count],
    "Total Students":[total_students_count],
    "Total Budget":[total_budget],
    "Average Math Score":[avg_math_score],
    "Average Reading Score":[avg_reading_score],
    "% Passing Math":[math_pass_percent],
    "% Passing Reading":[read_pass_percent],
    "% Overall Passing Rate":[avg_pass_rate]
     })
School_df

#total students by school
student_total = school_data_complete.groupby('school_name').count()['Student ID']


#school type
school_type = school_data.set_index('school_name')['type']


#total students by school
budget_by_school = school_data_complete.groupby('school_name').mean()['budget']
#

#budget by student
budget_by_student = budget_by_school/student_total

#avg math score
avg_math_score = school_data_complete.groupby('school_name').mean()['math_score']


avg_read_score = school_data_complete.groupby('school_name').mean()['reading_score']
#avg_read_score_df =pd.DataFrame(avg_read_score)

math_group = school_data_complete[school_data_complete['math_score']>=70].groupby('school_name').count()['Student ID']
math_pass = math_group/student_total
#math_pass_df = pd.DataFrame(math_pass)

read_group = school_data_complete[school_data_complete['reading_score']>=70].groupby('school_name').count()['Student ID']
read_pass = read_group/student_total
#read_pass_df = pd.DataFrame(read_pass)
#read_pass_df

avg_pass = (read_pass + math_pass)/2
#avg_pass_df = pd.DataFrame(avg_pass)
#avg_pass_df



#School Summary data frame
School_df["Total Students"] = School_df["Total Students"].map("{:,}".format)
School_df["Total Budget"] = School_df["Total Budget"].map("${:,.0f}".format)
School_df["Average Math Score"] = School_df["Average Math Score"].map("{:.2f}".format)
School_df["Average Reading Score"] = School_df["Average Reading Score"].map("{:.2f}".format)


School_df


df1 = pd.DataFrame(school_type).reset_index().rename(columns={'type':'Type'})
df2 = pd.DataFrame(student_total).reset_index().rename(columns={'Student ID':'Total Student'})
df3 = pd.DataFrame(budget_by_school).reset_index().rename(columns={'budget':'Total Budget'})
df4 = pd.DataFrame(budget_by_student).reset_index().rename(columns = {0:'Budget per Student'})
df5 = pd.DataFrame(avg_math_score).reset_index().rename(columns = {'math_score':'Avg Math Score'})
df6 = pd.DataFrame(avg_read_score).reset_index().rename(columns = {'reading_score':'Avg Reading Score'})
df7 = pd.DataFrame(math_pass).reset_index().rename(columns = {'Student ID':'% Passing Math'})
df8 = pd.DataFrame(read_pass).reset_index().rename(columns = {'Student ID':'% Passing Reading'})
df9 = pd.DataFrame(avg_pass).reset_index().rename(columns = {'Student ID':'Overall Pass Rate'})


#Create Data Frame for School Summary
df1 = df1.merge(df2, how = 'left', on ='school_name')
df1 = df1.merge(df3, how = 'left', on ='school_name')
df1 = df1.merge(df4, how = 'left', on ='school_name')
df1 = df1.merge(df5, how = 'left', on ='school_name')
df1 = df1.merge(df6, how = 'left', on ='school_name')
df1 = df1.merge(df7, how = 'left', on ='school_name')
df1 = df1.merge(df8, how = 'left', on ='school_name')
df1 = df1.merge(df9, how = 'left', on ='school_name')

#df1["Total Budget"] = df1["Total Budget"].map("${:,.0f}".format)
#df1["Budget per Student"] = df1["Budget per Student"].map("${:,.0f}".format)
#df1["Avg Math Score"] = df1["Avg Math Score"].map("{:,.2f}".format)
#df1["Avg Reading Score"] = df1["Avg Reading Score"].map("{:,.2f}".format)
#df1["% Passing Math"] = df1["% Passing Math"].map("{:,.2f}".format)
#df1["% Passing Reading"] = df1["% Passing Reading"].map("{:,.2f}".format)
#df1["Overall Pass Rate"] = df1["Overall Pass Rate"].map("{:,.2f}".format)

#Sort and display the top five schools in overall passing rate
df1_pass_school = df1.sort_values("Overall Pass Rate", ascending=False)
df1_new_index = df1_pass_school.reset_index(drop=True)

df1_new_index.head(5)


#avg math scores by grade
avg_math_score_grade_df = pd.DataFrame(school_data_complete.groupby(['school_name','grade']).mean()['math_score'])
avg_math_score_grade_df

#avg reading scores by grade
avg_read_score_grade_df = pd.DataFrame(school_data_complete.groupby(['school_name','grade']).mean()['reading_score'])
avg_read_score_grade_df


#Sort and display the bottom five schools in overall passing rate
df1_bottom_school = df1.sort_values("Overall Pass Rate", ascending=True)
df1_bottom_new_index = df1_bottom_school.reset_index(drop=True)
df1_bottom_new_index.head(5)

df1_modify=df1

#Create a table that breaks down school performances based on average Spending Ranges (Per Student). 
#Use 4 reasonable bins to group school spending. Include in the table each of the following:

#Score by spending :
# Sample bins. Feel free to create your own bins.
bins = [0, 590, 620 ,650, 680]
group_labels = ["<$590", "$590-620", "$620-650","$650-680"]


# Slice the data and place it into bins
df1_modify["Budget per Student_bin value"] = pd.cut(df1_modify["Budget per Student"], bins, labels=group_labels)


df_math_avg= pd.DataFrame(df1_modify.groupby('Budget per Student_bin value')['Avg Math Score'].mean()).reset_index().rename(columns={'Avg Math Score':'Math Avg'})
df_read_avg= pd.DataFrame(df1_modify.groupby('Budget per Student_bin value')['Avg Reading Score'].mean()).reset_index().rename(columns={'Avg Reading Score':'Read Avg'})
df_percent_math_pass= pd.DataFrame(df1_modify.groupby('Budget per Student_bin value')['% Passing Math'].mean()).reset_index().rename(columns={'% Passing Math':'Math Pass Rate'})
df_percent_read_pass= pd.DataFrame(df1_modify.groupby('Budget per Student_bin value')['% Passing Reading'].mean()).reset_index().rename(columns={'% Passing Reading':'Reading Pass Rate'})
df_percent_overall= pd.DataFrame(df1_modify.groupby('Budget per Student_bin value')['Overall Pass Rate'].mean()).reset_index().rename(columns={'Overall Pass Rate':'Overall Pass %'})

#Create Data Frame for School Summary
df_math_avg = df_math_avg.merge(df_read_avg, how = 'left', on ='Budget per Student_bin value')
df_math_avg = df_math_avg.merge(df_percent_math_pass, how = 'left', on ='Budget per Student_bin value')
df_math_avg = df_math_avg.merge(df_percent_read_pass, how = 'left', on ='Budget per Student_bin value')
df_math_avg = df_math_avg.merge(df_percent_overall, how = 'left', on ='Budget per Student_bin value')

print(df_math_avg)

#Score by School sice :
# Sample bins. Feel free to create your own bins.
school_bins = [0, 1250, 2500 , 3750, 5000]
school_group_labels = ["<1250", "(1250-2500)", "(2500-3750)","3750+"]


# Slice the data and place it into bins
df1_modify_size=df1
df1_modify_size

# Slice the data and place it into bins
df1_modify_size["Total Student"] = pd.cut(df1_modify_size["Total Student"], school_bins, labels=school_group_labels) 

#group by school size
df_math_avg_size= pd.DataFrame(df1_modify.groupby('Total Student')['Avg Math Score'].mean()).reset_index().rename(columns={'Avg Math Score':'Math Avg'})
df_read_avg_size= pd.DataFrame(df1_modify.groupby('Total Student')['Avg Reading Score'].mean()).reset_index().rename(columns={'Avg Reading Score':'Read Avg'})
df_pass_math_avg_size= pd.DataFrame(df1_modify.groupby('Total Student')['% Passing Math'].mean()).reset_index().rename(columns={'% Passing Math':'Math Pass Rate'})
df_pass_read_avg_size= pd.DataFrame(df1_modify.groupby('Total Student')['% Passing Reading'].mean()).reset_index().rename(columns={'% Passing Reading':'Read Pass Rate'})
df_pass_overall_avg_size= pd.DataFrame(df1_modify.groupby('Total Student')['Overall Pass Rate'].mean()).reset_index().rename(columns={'Overall Pass Rate':'Overall Pass Rate'})


#Create Data Frame for School Summary
df_math_avg_size = df_math_avg_size.merge(df_read_avg_size, how = 'left', on ='Total Student')
df_math_avg_size = df_math_avg_size.merge(df_pass_math_avg_size, how = 'left', on ='Total Student')
df_math_avg_size = df_math_avg_size.merge(df_pass_read_avg_size, how = 'left', on ='Total Student')
df_math_avg_size = df_math_avg_size.merge(df_pass_overall_avg_size, how = 'left', on ='Total Student')

print(df_math_avg_size)


#group by school type
df_group_type_math= pd.DataFrame(df1_modify_type.groupby('Type')['Avg Math Score'].mean()).reset_index().rename(columns={'Avg Math Score':'Math_Avg_Group'})
df_group_type_read= pd.DataFrame(df1_modify_type.groupby('Type')['Avg Reading Score'].mean()).reset_index().rename(columns={'Avg Reading Score':'Read_Avg_Group'})
df_group_type_mathpass= pd.DataFrame(df1_modify_type.groupby('Type')['% Passing Math'].mean()).reset_index().rename(columns={'% Passing Math':'Mathpass_Group'})
df_group_type_readpass= pd.DataFrame(df1_modify_type.groupby('Type')['% Passing Reading'].mean()).reset_index().rename(columns={'% Passing Reading':'Readpass_Group'})
df_group_type_overallpass= pd.DataFrame(df1_modify_type.groupby('Type')['Overall Pass Rate'].mean()).reset_index().rename(columns={'Overall Pass Rate':'Overall_Group'})

#Create Data Frame for School Summary
df_group_type_math = df_group_type_math.merge(df_group_type_read, how = 'left', on ='Type')
df_group_type_math = df_group_type_math.merge(df_group_type_mathpass, how = 'left', on ='Type')
df_group_type_math = df_group_type_math.merge(df_group_type_readpass, how = 'left', on ='Type')
df_group_type_math = df_group_type_math.merge(df_group_type_overallpass, how = 'left', on ='Type')

print(df_group_type_math)




