def exam(first, second):
    addition = first + second
    multiplication = first * second
    print(addition, multiplication)
    # return


exam(5, 2)

exam_2 = lambda first_2, second_2: first_2 + second_2
# exam_3 = lambda first_2, second_2: first_2 * second_2

print(exam_2(5, 6))
# print(exam_3(5, 6))
