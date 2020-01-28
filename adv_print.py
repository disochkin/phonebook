import textwrap

output_file = "output.txt"

def adv_print(*args, **kwargs):
    start = kwargs.get('start', '')
    max_line = kwargs.get('max_line', 5)
    in_file = kwargs.get('in_file', False)

    if in_file:
        with open(output_file, 'w') as f_obj:
            if start:
                print(start, file=f_obj)
            for item in args:
                print('\n'.join(textwrap.wrap(item, max_line)), file=f_obj)

    else:
        if start:
            print(start)
        for item in args:
                print('\n'.join(textwrap.wrap(item, max_line)))


adv_print("zzzzzzzzzzzzzzzzzzzzz","zzzzxxxxxxxxxxxxxxxxxxxxxxxxx", max_line=10)


