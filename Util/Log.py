import builtins 

def info(n,str):
    builtins.step += abs(n)
    print(f'\033[92m{builtins.step:<3}\033[0m \033[94m||\033[0m {str}')

def error(str):
    print(f'\033[91m{str}\033[0m')