student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Loop through dictionary
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_df = pandas.DataFrame(student_dict)
# print(student_df)

# Loop through data frame
# for (key, value) in student_df.items():
#     print(value)

# Loop through rows of data frame
for (index, row) in student_df.iterrows():
    print(row.student)
