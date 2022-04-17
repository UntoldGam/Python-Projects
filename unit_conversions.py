def convert(number, type):
    if type == "mm to cm":
        converted = float(number) * 10
        return print('Number converted: '+str(converted))
    elif type == "cm to mm":
        converted = float(number) / 10
        return print('Number converted: '+str(converted))
