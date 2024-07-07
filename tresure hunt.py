print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input('You \'re at a crossroad. Where do you want to go "left" or "right"?.').lower()
if choice1 == "left":
    choice2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" or swim to wait for a boat. Type swim to "swim" across.').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One "red", one "yellow" and one "blue". Which colour do you choose?').lower()
        if choice3 == "red":
            print('''



                                             (  .      )
                                         )           (              )
                                               .  '   .   '  .  '  .
                                      (    , )       (.   )  (   ',    )
                                       .' ) ( . )    ,  ( ,     )   ( .
                                    ). , ( .   (  ) ( , ')  .' (  ,    )
                                   (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
                               jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


                              it is a room on full of fire game over!!''')
        elif choice3 == "yellow":
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************


  you got the treasure you win!!''')
        elif choice3 == "blue":
            print('''

                                                 (    )
                                                ((((()))
                                                |o\ /o)|
                                                ( (  _')
                                                 (._.  /\__
                                                ,\___,/ '  ')
                                  '.,_,,       (  .- .   .    )
                                   \   \\     ( '        )(    )
                                    \   \\    \.  _.__ ____( .  |
                                     \  /\\   .(   .'  /\  '.  )
                                      \(  \\.-' ( /    \/    \)
                                       '  ()) _'.-|/\/\/\/\/\|
                                           '\\ .( |\/\/\/\/\/|
                                             '((  \    /\    /
                                             ((((  '.__\/__.')
                                              ((,) /   ((()   )
                                               "..-,  (()("   /
                                          pils  _//.   ((() ."
                                        _____ //,/" ___ ((( ', ___
                                                         ((  )
                                                          / /
                                                        _/,/'
                                                      /,/,"

                              you are eaten by beast game over!!!''')
        else:
            print("you choose a door that does not exist. game over!!")

    else:
        print('''

                                 .-._   _ _ _ _ _ _ _ _
                      .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
                      '.___ '    .   .--_'-' '-' '-' _'-' '._
                       V: V 'vv-'   '_   '.       .'  _..' '.'.
                         '=.____.=_.--'   :_.__.__:_   '.   : :
                                 (((____.-'        '-.  /   : :
                       snd                         (((-'\ .' /
                                                 _____..'  .'
                                                '-._____.-'

             you are attacked by trout. Game over!!''')
else:
    print('''
                _____       _____
              /        \    /        \
             |    ⛰️    |  |    💨    |
             |          |  |          |
              \  ___  /    \  ___  /
                \     /        \    /
                  \ /            \ /
          
    you fell into a devils kitchen. Game over!!''')
