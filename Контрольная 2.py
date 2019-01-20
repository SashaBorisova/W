try:
    u1=int(input())
    u2=int(input())
    t=int(input())
    def decorator(original_function):
        def wrapper(u1,u2,t):
            a=original_function(u1,u2,t)
            s=u1*t+(a*t*t)/2
            print(s)
        return wrapper
    def original_function(u1,u2,t):
        a=(u2-u1)/t
        print(a)
        return a
    original_function=decorator(original_function)
    d=original_function(u1,u2,t)
except (ValueError, ZeroDivisionError):
    print(("РќРµР»СЊР·СЏ РІРІРѕРґРёС‚СЊ СЃС‚СЂРѕРєРё РёР»Рё РґРµР»РёС‚СЊ РЅР° РЅРѕР»СЊ"))
