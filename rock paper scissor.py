from random import choice
con = ["rock","paper","scissor"]

while True:
    cont = choice(con)
    ip = input(
        """
        Choose: rock
                paper
                scissor
            => for exit enter 'exit' : """
    ).lower()
    if ip == "exit" or ip == "'exit'":
        print("you're exited successfully")
        break
    else:
        # cont = list(map(lambda x: x.lower(),cont))
        if ip == cont:
            print(
                """Result => TIE""")
        elif ((ip == "rock" and cont == "scissor") or (ip == "paper" and cont == "rock") or
              (ip == "scissor" and cont == "paper")):
            print(f"Result => you win, computer showed {cont}")
        else:
            print(f"Result => you lose, computer showed {cont}")

