# Вам даны две строки и . Определите, существует ли непустая строка, которая встречается как подстрока и в A , и в B
# Input Format
# В первой строке записано целое число
# T- количество тестов. Далее следуют сами тесты. Каждый тест описывается двумя строками, в первой из которых записана строка A, 
# а во второй строка B
# Output Format
# Для каждого теста выведите ответ: строку YES, либо строку NO.
    
# import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    if len(set(s1) & set(s2)) > 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)ы

        fptr.write(result + '\n')

    fptr.close()
