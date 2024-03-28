def solution(numbers):
    answer = ""
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_text = ""
    for num in numbers:
        num_text += num
        if num_text in num_list:
            answer += str(num_list.index(num_text))
            num_text = ""
    return int(answer)

# def solution(numbers):
#     for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
#         numbers = numbers.replace(eng, str(num))
#     return int(numbers)

a = "onetwothreefourfivesixseveneightnine"
# b = 5
# c = 4
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)

