# import module_7 as m7
# m7.hello_function()

#aliasing and importing a function from a module
# from module_7 import hello_function as hf

# hf()

#recursive function
def say_hi(num):
    if num == 0:
        return
    print("Hi")
    say_hi(num-1)
    
say_hi(5)

n = 5
while n != 0:
    print("Hi")
    n -= 1 