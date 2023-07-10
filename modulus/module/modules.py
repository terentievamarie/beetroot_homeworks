def make_readable(seconds):
    if seconds<0 or seconds>359999:
        return "Please,enter another number of seconds"
    
    hours = seconds//3600
    minuts=(seconds%3600)//60
    seconds1=seconds-hours*3600-minuts*60
    return f'{hours:02d}:{minuts:02d}:{seconds1:02d}'