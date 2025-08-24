def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))

# if __name__ == "__main__": It allows you to separate code that should run only when the file is executed directly vs code that should be reusable when imported.    
# Scenerio with this 
# If you run python leap.py → works fine.
# But if you import leap inside another program → it will immediately ask for input, which is not what you want.
# Scenerio without this 
# Run directly → works normally.
# Import it:→ Now it just gives you the function, without running the input code.