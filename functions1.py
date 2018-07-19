# def make_double(a):
#     dbl=a*2
#     return dbl
# b= make_double((5))
# print(b)
# def make_half(a):
#     half=a/2
#     return half
# b= make_half(100)
# print(b)
# def make_plural(word):
#     return word+'s'
# print(make_plural('hat'))
# def get_power(base, exp):
#     '''
#     Raise base to the power of the exp
#     :param base:int
#     :param exp:int
#     :return: int
#     '''
#     return base** exp
# # print(get_power((8,2)))
# # def find_max(num1,num2,num3):
# #     return max(num1,num2,num3)
# # print(find_max(34,89,100))
# def find_sum(num1,num2,num3,num4,num5):
#     return sum((num3,num1,num2,num4,num5))
# print (find_sum(1,2,3,4,5))
# def find_mult(a,b,c,d,e):
#     return (a*b*c*d*e)
# print(find_mult(8,2,3,-1,7))
# def print_str(a):
#     return a[::-1]
# print (print_str('abcde1234'))
# def num_rage(a):
#     a=(1,8)
#     return a
#     user_input= input('Pick a number')
#     if user_input==a:
#         print('Number is in range')

# #     print(factorial(6))
# #     print("I'm in the module!!!")
#
# def factorial(n):
#     if n<2:
#         return 1
#     return n*factorial(n-1)
# factorial
# def factorial(num):
#     answer=1
#     for n in range(num):
#         answer=answer*n
#         return answer
# print (factorial(4))
# 7
# def count_upper_lower(word):
#     count_uppers=0
#     count_lowers=0
#     for w in word:
#         if w==w.lower():
#             count_lowers+=1
#         else:
#             count_uppers+=1
#     return (count_uppers, count_lowers)
# # t= count_upper_lower('ValentinaBarragan')
# # print(t)
# # print('The upper count is", t[0], ", the lower count is ",
# def make_unique(nums):
#     return tuple(set(nums))
# # print(make_unique((1,2,3,4,4,5,6,6,7)))
# print ('im in a module')

def find_weight(user_input_weight, user_input_planet='earth'):
    Mercury = .38
    Venus = .91
    Earth= 1.00
    Mars= 0.38
    Jupiter= 2.34
    Saturn=1.06
    Uranus= .92
    Neptune= 1.19
    Pluto=.06
    if user_input_planet=='earth':
        return user_input_weight*Earth
    if user_input_planet== 'Mercury':
        return user_input_weight*Mercury
    if user_input_planet== 'Venus':
        return user_input_weight* Venus
    if user_input_planet== 'Neptune':
        return user_input_weight* Neptune
    if user_input_planet== 'Pluto':
        return user_input_weight* Pluto
    if user_input_planet== 'Uranus':
        return user_input_weight* Uranus
    if user_input_planet== 'Saturn':
        return user_input_weight*Saturn


if __name__=='__main__':
    print(find_weight(100))









