browser = "firefox"
match browser:
    case "chrome":
        print("Execute the code of chrome browser")
    case "firefox":
        print("Execute the code of firefox browser")
    case _:
        print("Do not execute")