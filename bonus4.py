feet_inches = input("Enter your height in feet and inches: ")


def parse(feetinches):
    diff = feetinches.split(" ")
    feet = float(diff[0])
    inches = float(diff[1])	

    return feet, inches

def convert(feet, inches):
    meters = (feet * 0.3048) + (inches * 0.0254)
    return meters


f,i = parse(feet_inches)
print(f,i)
print(convert(f,i))


