# Write a function that takes **kwargs as an input and finds out the final values.
#   - Use decorators to execute the code (Optional)
#   - Handle all Exceptions
def opt(**x):
    dictval = [v for k, v in x.items()]
    action = dictval.pop()
    if action == 'sum':
        res = sum(dictval)
        print(res)
        return res
    elif action == 'avg':
        try:
            output = sum(dictval) / len(dictval)
            print(dictval, output, action)
        except ZeroDivisionError as e:
            output=e
        return output
    elif action == 'max':
        maxout = max(dictval)
        print(maxout)
        return maxout
    elif action == 'min':
        minout = min(dictval)
        print(min(dictval), dictval)
        return minout


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    opt(x=100, y=200, z=150, a=300, b=180, e=90, f=25, g=80, h=120, action="avg")
    opt(x=100, y=200, z=150, a=300, b=180, e=90, f=25, g=80, h=120, action="sum")
    opt(x=100, y=200, z=150, a=300, b=180, e=90, f=25, g=80, h=120, action="min")
    opt(x=100, y=200, z=150, a=300, b=180, e=90, f=25, g=80, h=120, action="max")
