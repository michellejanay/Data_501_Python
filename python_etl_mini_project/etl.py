import csv
students_csv_file = 'student_test_scores_extended(in).csv'
students_excel = 'student_test_scores_extended.xlsx'


def extract(csv_file):
    # checking file type ends with csv
    if not csv_file.lower().endswith('.csv'):
        raise Exception('please use a csv file')
    # an empty list to store extracted data
    extracted_students = []
    try:
        # opening the file
        with open(csv_file, 'r') as file:
            # reading the file
            students_test_scores = csv.DictReader(file)
            # saving data from file to new list
            for student in students_test_scores:
                extracted_students.append(student)
    except Exception as e: 
        raise Exception(f'an error occured while processing your file: {e}')
    # returning the new list of dictionaries
    return extracted_students

def transform_remove(student_list):
    # removing unnecessary columns
    for student in student_list:
        # none is a fail-safe default value if the key does not exist in the dictionary
        student.pop('Number of Siblings', None)
        student.pop('Lunch Type', None)
        student.pop('Test Preparation', None)
        student.pop('Study Time (hours)', None)
        student.pop('Favorite Subject', None)
        student.pop('Main Teacher', None)
    return student_list

def transform_add_average(student_list):
    transformed_students = []
    # looping through students
    for student in student_list:
        # setting the average
        average = 0
        # looping through dictionary to find the keys with 'Score' in the name
        for key,value in student.items():
            if 'Score' in key:
                # adding the scores to the average variable
                average += int(value)
        # calculating average
        student_average = average / 5
        # saving average score into a new key for each student
        student['Average Score'] = student_average
        # saving the transformation to a new list
        transformed_students.append(student)
        # reseting the average value
        average = 0
    return transformed_students

def load_to_csv(student_list):
    if len(student_list) == 0:
        raise Exception('your data is empty, please use a csv file')
    try:
        # finding the column names from the dictionary keys
        column_names = list(student_list[0].keys())
        # giving the new file a name
        file_name = 'students_with_average.csv'
        # opening the file to write to it
        with open(file_name, 'w', newline='') as csv_file:
            # declaring the CSV writer
            writer = csv.DictWriter(csv_file, fieldnames=column_names)
            # writing column names
            writer.writeheader()
            # writing data
            writer.writerows(student_list)
            # result message
            print('successfully written files')
    except Exception as e:
        raise Exception(f'an error occured while processing your data: {e}')

# one function to rule them all
def etl(orginal_file):
    extracted = extract(orginal_file)
    first_transform = transform_remove(extracted)
    second_transform = transform_add_average(first_transform)
    loaded = load_to_csv(second_transform)
    print('new csv successfully created')
    return loaded

# etl(students_csv_file)