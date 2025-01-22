import pandas as pd

# 2877. Create a DataFrame from List

student_data = [[1,15],[2,11],[3,11],[4,20]]

"""
Write a solution to create a DataFrame from a 2D list called student_data.
This 2D list contains the IDs and ages of some students
"""

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

test = createDataframe(student_data)  # Fixed capitalization of function name
print(test)
