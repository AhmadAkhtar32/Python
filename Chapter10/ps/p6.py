class Demo:
    def __init__(harry, value):  # 'self' replaced with 'harry'
        harry.value = value

    def show(harry):
        print(f"Value is {harry.value}")

obj = Demo(10)
obj.show()
