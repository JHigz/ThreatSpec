# @component MyApp:Web:Guest (#guest)
# @component MyApp:Web:Main (#main)
# @connects #guest to #main with HTTP

def main():
    print("Hello World")

# @component MyApp:Web:login (#login)
# @connects #guest to #login with HTTP/GET-Request

def login():
    print('This is the login page')
