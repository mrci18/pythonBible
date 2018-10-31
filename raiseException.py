def add_2(num):
    if len(num) > 2:
        raise Exception("Numbers being multiplied must be less than 2")
    if len(num) < 2:
        raise Exception("Numbers being multiplied must be more than 1")
    else:
        return sum(num)
if __name__ == "__main__":
    for x in [1, 2], [3,4,5], [34]:
        try:
            print(add_2(x))
        except Exception as err:
            message = "{} - error, {} - type error, {} - error name".format(err, type(err), type(err).__name__)
            print(message)