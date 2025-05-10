x = 'global' 
#función externa
def outer_function():
    x = 'enclosing'
    #función interna
    def inner_function():
        x ='local'
        print(x)

    inner_function()
    print(x)
outer_function()
print(x)