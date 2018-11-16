from reverse_string import reverse_string
# print(reverse_string)

def test_null_input():
   '''None input returns None result''' 
   assert reverse_string(None) == None
   
def test_empty_string():
   '''empty input returns empty string'''
   assert reverse_string('') == ''

def test_one_char():
   '''One character input returns the same character'''
   assert reverse_string('a') == 'a'

def test_two_chars():
   '''Two characters input returns the reverse'''
   assert reverse_string('ab') == 'ba'
   
def test_more_than_2_chars():
   '''Greater than 2 characters input returns the reverse of the string'''
   assert reverse_string('abc') == 'cba'

# def test_answer():
#     '''this is testing adding 2'''
#     # assert actual_result expected_result
#     assert func(3) == 5
    
# def test_answer2():
#     '''this is testing adding 2'''
#     # assert actual_result expected_result
#     assert func(4) == 6