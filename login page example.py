def outer_fun(fun):
    def warpper_fun():
        print("before")
        val = fun()
        print("after")
        return val

    return warpper_fun


@outer_fun
def message():
    print("this is the main function")


message()


def login(fun):
    def login_details(name, islogin):
        if islogin == False:
            print("please login first to continue further.")
            return
        # print("team uvw")
        return fun(name)

    return login_details


@login
def home_page(name):
    print(f"welcome to the home page {name}")


home_page("srinu", False)
# my_homepage = login(home_page)
# my_homepage("srinu", True)


@login
def about(name):
    print(f"this is our about page {name}")


about("pavan", True)


def help_page():
    print("this is your help page")


help_page()

