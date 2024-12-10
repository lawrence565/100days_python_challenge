student = ["Angela", "James", "Tim"]
score = [72, 85, 78]

student_dict = {
    "student": student,
    "score": score
}

# for (key, value) in student_dict.items():
#     print(key, value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

for (key, value) in student_data_frame.items():
    print(key) # Print the column name
    print(value) # Print all the value of the column

for (index, row) in student_data_frame.iterrows():
    print(index) # Print the id of the row
    print(row) # Print the whole value of the row, including the column