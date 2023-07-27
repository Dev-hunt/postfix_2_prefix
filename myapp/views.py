from django.shortcuts import render
from django.http import HttpResponse

# class postfix :
#     stack = list()
#     postfix = ''

#     def __init__(self, postfix) -> None:
#         if postfix[0].isdigit() :
#             self.postfix = postfix.split(',')
#         else :
#             self.postfix = postfix.split(',')[::-1]

#     def calculator(self) -> int:
#         for char in self.postfix :
#             if char.isdigit():
#                 self.stack.append(int(char))
#             else :
#                 a = self.stack.pop()
#                 b = self.stack.pop()
#                 match char :
#                     case '+' :
#                         self.stack.append(b + a)
#                     case '-' :
#                         self.stack.append(b - a)
#                     case '*' :
#                         self.stack.append(b * a)
#                     case '/' :
#                         self.stack.append(b / a)
#                     case '^' :
#                         self.stack.append(b ** a)
#         return self.stack.pop()
#     def postfix_to_prefix(self):
#         for char in self.postfix:
#             if char.isdigit():
#                 self.stack.append(int(char))
#         else:
#             operand1 = self.stack.pop()
#             operand2 = self.stack.pop()
#             self.stack.append(char + operand2 + operand1)
#         return self.stack.pop()
def calculator(expression):
        stack=[]
        for char in expression :
            if char.isdigit():
                stack.append(int(char))
            else :
                a = stack.pop()
                b = stack.pop()
                match char :
                    case '+' :
                        stack.append(b + a)
                    case '-' :
                        stack.append(b - a)
                    case '*' :
                        stack.append(b * a)
                    case '/' :
                        stack.append(b / a)
                    case '^' :
                        stack.append(b ** a)
        return stack.pop()   

def postfix_to_prefix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for char in expression:
        if char not in operators:
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(char + operand2 + operand1)
    return stack.pop()

def evaluate(request):
    total=''
    prefix=''
    try:
        if request.method == 'POST':
            express=request.POST.get('Expres')
            # result = postfix(express).postfix_to_prefix()
            # result=postfix_to_prefix(express)
            total=calculator(express)
            prefix=postfix_to_prefix(express)
            
    except:
        total="Invalid Expression"
        prefix="Invalid Expression"

    context={
        'Total':total,
        'Prefix':prefix
    }
    print(total)
    print(prefix)
    return render(request,'myapp_template/index.html',context)
# Create your views here.
