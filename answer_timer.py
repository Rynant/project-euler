from timeit import Timer
from sys import argv

def time_solution(module_name, repeat=3, count=3):
    import_cmd = 'import {0}'.format(module_name)
    answer_cmd = '{0}.{1}()'.format(module_name, 'answer')
    
    print('Answer: ', end='')
    exec('{0}; print({1})'.format(import_cmd, answer_cmd))
    
    time = Timer(answer_cmd, import_cmd).repeat(repeat, count)
    print('Avg of {0} loop(s), best of {1}: {2:.6f} s'.format(
            count,
            repeat,
            min(time)/count))


if len(argv) == 2:
    time_solution(argv[1])
elif len(argv) == 3:
    time_solution(argv[1], int(argv[2]))
elif len(argv) == 4:
    time_solution(argv[1], int(argv[2]), int(argv[3]))
else:
    help_msg = '''Supply module name. The module's answer must be supplied by
an 'answer()' function (no args). Optionally, supply the number 
of times to run the command and the number of repeats.

Defaults: repeat=3, count=3,

EXAMPLES
# Loop answer 3 times and repeat test 3 times (default).
> answer_timer pe001

# Loop answer 100 times and repeat test 7 times
> answer_timer pe001 7 100

# Loop answer 10 times (default) and repeat test 5 times
> answer_timer pe001 5
'''
    print(help_msg)



