a = '-'.join(['STRING1', 'STRING2', 'STRING3'])
print(a)

print(a.split('-'))

print()

# sorted(<list>) function doesnt't change the original list (generates a copy)
# <list>.sort() method does change the original list


sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand... The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''

def get_longest_word(str_arg: str):
    longest_word = ''
    # replace() return a copy, and doesn't modify the original string
    str_arg = str_arg.replace('.', ' ').replace(',', ' ')
    for word in str_arg.split():
        longest_word = word if len(word) > len(longest_word) else longest_word
    return longest_word

print(get_longest_word(sample_story))