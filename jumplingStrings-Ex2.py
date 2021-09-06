# Write python code to jumble 2 strings without using any built-ins.
#    Take chars from alternate indexes and shift.
#    Before running you must ensure both strings are of same length.
#    Handle exceptions.
def jumbleStr(x, y):
    output = ''
    try:
        if len(x) == len(y):
            for i in range(len(x)):
                output = output + x[i]
                output = output + y[i]
            print(output)
        else:
            raise
    except Exception as err:
        print('length of strings are not same', err)
        output = 'lengths are not same'
    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jumbleStr('hellooo', 'world')
