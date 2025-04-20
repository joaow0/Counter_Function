from time import sleep

def line():
    print('-=' * 20)

def counter(txt1, txt2, txt3, start, end, step):
    line()
    print(txt1)

    # Count from 1 to 10
    for i in range(1, 11, 1):
        print(i, end=' ', flush=True)
        sleep(0.3)
    print('END!')
    
    line()
    print(txt2)

    # Count from 10 to 0, step -2
    for y in range(10, -1, -2):
        print(y, end=' ', flush=True)
        sleep(0.3)
    print('END!')

    line()
    print(txt3)

    # Custom count
    start = int(input('Start: '))
    end = int(input('End: '))
    step = int(input('Step: '))

    if step == 0:
        step = 1
    if start > end and step > 0:
        step *= -1

    print(f'Counting from {start} to {end} by {abs(step)}')
    
    # Adjust end value based on step direction
    if step > 0:
        end += 1
    else:
        end -= 1

    for u in range(start, end, step):
        print(u, end=' ', flush=True)
        sleep(0.3)
    print('END!')