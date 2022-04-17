# WHAT IS THIS PROGRAM? WHAT DOES IT DO?

# VARIABLES 

# MAIN CODE

def execute(project):
    if project == "UC":
        def run():
            
            number = float(input('What number do you want converted?  '))
            un = 'What do you want to convert {} to? Use the format: start_unit to end_unit e.g. mm to cm '
            unit = input(un.format(number))
            import unit_conversions

            unit_conversions.convert(number, unit)
            

        run()