Ask=input('Choose interface mode:\n1.WordleBot\n2.Game with support\nElse to stop\n')
while Ask.isdigit():
    if Ask==1:
        import WordleBot
    else:
        import Gamewithsupport
    Ask=input('Choose interface mode:\n1.WordleBot\n2.Game with support\nElse to stop\n')
       