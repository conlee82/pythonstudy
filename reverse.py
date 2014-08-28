
def reverse(test):
    for index in range(len(test)-1,-1,-1):
        yield test[index]

for char in reverse('this is test string'):
    print(char)
    
    
"""      
def reverse(data):
    data[-1:-18]
    
data = "this is test string"
print(data[:])
"""