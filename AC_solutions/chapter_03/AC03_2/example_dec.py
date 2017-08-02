def call_alert(method_name):
    def _decorator(cls):
        method = getattr(cls, method_name)

        def new_method(*args, **kwargs):
            print('Calling the method!')
            return method(*args, **kwargs)

        setattr(cls, method_name, new_method)
        return cls

    return _decorator


# Here we apply it to a test class:

@call_alert('walk')
class Test:
    def walk(self):
        return 'I am walking'


if __name__ == "__main__":
    t = Test()
    print(t.walk())
