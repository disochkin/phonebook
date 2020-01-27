import textwrap

output_file = "output.txt"

def adv_print(*args, **kwargs):
    start = kwargs.get('start', '')
    max_line = kwargs.get('max_line', 5)
    in_file = kwargs.get('in_file', False)

    if in_file:
        with open(output_file, 'w') as f_obj:
            if start:
                if in_file:
                    print(start, sep='', file=f_obj)
                for item in args:
                    print('\n'.join(textwrap.wrap(item, max_line)), file=f_obj)

    else:
        if start:
            if in_file:
                print(start, sep='')
            for item in args:
                print('\n'.join(textwrap.wrap(item, max_line)))


adv_print("zzzzzzzzzzzzzzzzzzzzz","zzzzxxxxxxxxxxxxxxxxxxxxxxxxx")
adv_print("zzzzzzzzzzzzzzzzzzzzz","zzzzxxxxxxxxxxxxxxxxxxxxxxxxx", max_line=8, start='start_line!')
adv_print("zzzzzzzzzzzzzzzzzzzzz","zzzzxxxxxxxxxxxxxxxxxxxxxxxxx", max_line=8, start='start_line!', in_file=True)

#print("zzz","zzzz")