def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value=', '.join(f'{k} {v}' for k,v in kwargs.items())
        print(f'name : {func.__name__}, with args : {args_value} and kwargs : {kwargs_value}')

        return func(*args,**kwargs)
    
    return wrapper

@debug
def hello():
    return "hello"
@debug
def greet(name,msg='welcome'):
    print(f'{name} , {msg}')

hello()
greet('kunal',msg='hello')
