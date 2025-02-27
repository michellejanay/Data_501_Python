from etl import extract, transform_remove, transform_add_average, load_to_csv
import pytest


def test_extract():
    test_file = 'student_test_scores_extended.xlsx'
    with pytest.raises(Exception):
        extract(test_file)
    

def test_transform_remove():
    test_list = [
        {
            'Name': 'Test', 
            'Math Score': '89', 
            'English Score': '87', 
            'Science Score': '94', 
            'Art Score': '90', 
            'History Score': '100', 
            'Number of Siblings': '3', 
            'Lunch Type': 'Veggie'}
    ]
    result_list = [
        {
            'Name': 'Test', 
            'Math Score': '89', 
            'English Score': '87', 
            'Science Score': '94', 
            'Art Score': '90', 
            'History Score': '100'
            }
    ]
    
    assert result_list == transform_remove(test_list)

def test_transform_add_average():
    test_list = [
        {
            'Name': 'Test', 
            'Math Score': '89', 
            'English Score': '87', 
            'Science Score': '94', 
            'Art Score': '90', 
            'History Score': '100'
            }
    ]
    result_list = [
        {
            'Name': 'Test', 
            'Math Score': '89', 
            'English Score': '87', 
            'Science Score': '94', 
            'Art Score': '90', 
            'History Score': '100', 
            'Average Score': 92
            }
    ]
    assert result_list == transform_add_average(test_list)

def test_load_to_csv():
    test_list = []
    with pytest.raises(Exception):
        load_to_csv(test_list)
