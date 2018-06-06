from Tkinter import *
import random
import os

clear = lambda: os.system('clear')
import time
import random
import codecs
from random import randint

def satellite_sim():
    canvas_width = 800
    canvas_height =800

    master = Tk()

    canvas = Canvas(master, width=canvas_width, height=canvas_height,bg = '#16316E')
    canvas.pack()

    ##Creates upper half of stars
    def create_stars():
        for c in range(0, 80):
            x = random.randint(1, 801)
            y = random.randint(1, 580)
            canvas.create_oval((x,y),(x-6,y-6), fill = "white", outline = "White")

        ##creates lower left half of stars
        for k in range(0, 10):
            x = random.randint(1, 190)
            y = random.randint(580, 801)
            canvas.create_oval((x,y),(x-6,y-6), fill = "white", outline = "White")

        canvas.create_oval((100, 100), (94, 94), fill="yellow", outline="yellow")
        canvas.create_oval((700, 100), (694, 94), fill="yellow", outline="yellow")

    def create_buttons():
        canvas.create_rectangle((630,670),(690,731),fill = '#00C5FF',outline='#16316E')
        ninety = Label(text = "Next", font=('Bodoni',45),bg="#2874A6", borderwidth=1)
        ninety.pack()
        ninety.place(x=690,y=671)


    ##Creates the Satelite
    def create_satelite(w,z):
        ##Left Solar panel
        ##For the 90 degree position, use w=0
        y= 88
        x=176+w
        ##Lines on Solar Panel
        canvas.create_rectangle((160+w,88),(240+w,152), fill="#4863A0", width = 3)
        for j in range(0,5):
            canvas.create_line((x,88),(x,152))
            x = x+16

        for i in range(0,4):
            canvas.create_line((160+w, y), (240+w, y))
            y = y + 16

        ##Body of Satelite
        canvas.create_rectangle((240+w, 96), (296+w, 144), fill="Gray", width=3)

        ##Right solar Panel
        y = 88
        x = 312+w
        canvas.create_rectangle((296+w, 88), (376+w, 152), fill="#4863A0", width=3)
        ##Lines on Solar Panel
        for b in range(0, 5):
            canvas.create_line((x, 88), (x, 152))
            x = x + 16

        for a in range(0, 4):
            canvas.create_line((296+w, y), (376+w, y))
            y = y + 16

        ##Lower Part (Satelite Dish)
        canvas.create_line((268+w,144),(268+w,182),width=3)
        canvas.create_line((218+w,200),(268+w,160), (318+w,200),width=3,smooth=True)
        canvas.create_line((268+w,182),(268+w,218-z), width=3)
        canvas.create_oval((264+w,214-z),(272+w,222-z), fill="Black")

    ##Makes the Satelite Dish
    def create_satelite_dish():
        canvas.create_line((199, 600), (400, 900), (601, 600), smooth=True, width=5, fill='gray')
        canvas.create_line((400, 750), (400, 682.66), width=5, fill='gray')
        canvas.create_oval((380, 662.66), (420, 702.66), width=5, fill='gray', outline="Gray")


    def callback(event):
        global counter
        print(event.x, event.y)
        if (event.x < 690 and event.x > 630) and (event.y < 730 and event.y > 670):
            counter += 1
            if counter >= 3:
                counter = 0
            if counter == 0:
                move_satilite(0,0)
            if counter == 1:
                print('Hello_1')
                move_satilite(132,0)
            if counter == 2:
                print('Hello_2')
                move_satilite(192,5)

        if ((event.x <101 and event.x > 93) and (event.y <101 and event.y >93)):
            draw()

        if ((event.x <701 and event.x > 693) and (event.y <101 and event.y >93)):
            flashcards_and_planner_2_in_1()

    def radio_wave(counter):
        if counter == 0:
            x = 268
            y = 218
            t = 225.5
            r = 288

            canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width = 3, fill='green')
            for k in range(0,15):
                y = y + 15
                r = r - 40
                t = t + 15
                canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width = 3, fill='green')
                y = y + 15
                r = r + 40
                t = t + 15
                canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width = 3, fill='green')

            x = 268
            y = 686
            r = 275.5
            t = 666

            canvas.create_line((x, y), (r, t), (x + 15, y), smooth=True, width = 3, fill='green')
            for k in range(0,4):
                x = x + 15
                r = r + 15
                t = t + 40
                canvas.create_line((x, y), (r, t), (x + 15, y), smooth=True, width = 3, fill='green')
                x = x + 15
                r = r + 15
                t = t - 40
                canvas.create_line((x, y), (r, t), (x + 15, y), smooth=True, width = 3, fill='green')

        if counter == 1:
            x = 400
            y = 218
            t = 225.5
            r = 420

            canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')
            for k in range(0, 15):
                y = y + 15
                r = r - 40
                t = t + 15
                canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')
                y = y + 15
                r = r + 40
                t = t + 15
                canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')

        if counter == 2:
            x = 460
            y = 213
            r = 440
            t = 220.5


            canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')
            for k in range(0, 17):
                y = y + 15
                r = r + 40
                t = t + 15
                canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')
                if k==17:
                    print("Hi")
                else:
                    y = y + 15
                    r = r - 40
                    t = t + 15
                    canvas.create_line((x, y), (r, t), (x, y + 15), smooth=True, width=3, fill='green')

            x = 460
            y = 738
            r = 467.5
            t = 715.5

            canvas.create_line((x, y), (r, t), (x - 15, y - 15), smooth=True, width=3, fill='green')
            for k in range(0, 2):
                x = x - 15
                y = y - 15
                r = r - 45
                t = t + 15
                canvas.create_line((x, y), (r, t), (x - 15, y - 15), smooth=True, width=3, fill='green')
                if k==1:
                    print("Hi")
                else:
                    x = x - 15
                    y = y - 15
                    r = r + 15
                    t = t - 45
                    canvas.create_line((x, y), (r, t), (x - 15, y - 15), smooth=True, width=3, fill='green')


    canvas.bind("<Button-1>", callback)
    global counter
    counter=0

    def move_satilite(w,z):
        canvas.create_rectangle((0, 0), (800, 800), fill='#16316E')
        create_stars()
        create_satelite(w,z)
        create_buttons()
        create_satelite_dish()
        radio_wave(counter)


    move_satilite(0,0)

def hangmn_game():
    master = Tk()
    w = Canvas(master, width=600, height=600,)
    w.pack()

    def calleasy():
        global level
        level=0
        master.destroy()
    def callmedium():
        global level
        level=0
        master.destroy()
    def callhard():
        global level
        level=0
        master.destroy()
    def callinstructions():
        print("The game is simple.\nGuess letters to try to guess the word the computer is thinking of.\nThere are 3 levels: easy, medium and hard.\n"
              "Choose whichever level fits you best!"
              )

    r = w.create_rectangle(0, 0, 600, 100)
    w.itemconfigure(r, fill='blue')
    r = w.create_rectangle(0, 100, 600, 200)
    w.itemconfigure(r, fill='green')
    r = w.create_rectangle(0, 200, 600, 300)
    w.itemconfigure(r, fill='red')
    r = w.create_rectangle(0, 300, 600, 400)
    w.itemconfigure(r, fill='yellow')
    r = w.create_rectangle(0, 400, 600, 500)
    w.itemconfigure(r, fill='orange')
    r = w.create_rectangle(0, 500, 600, 600)
    w.itemconfigure(r, fill='purple')


    label = Label(master, text='Hangman', font = ('Courier', 30, 'bold'))
    label.pack()
    label.place(x=230, y=100)

    easy = Button(master, text="Easy", font = ('Chelsea Market', 20, 'bold'), command=calleasy)
    easy.pack()
    easy.place(x=150, y=300)

    medium = Button(master, text="Medium", font = ('Chelsea Market', 20, 'bold'), command=callmedium)
    medium.pack()
    medium.place(x=245, y=300)

    hard = Button(master, text="Hard", font = ('Chelsea Market', 20, 'bold'), command=callhard)
    hard.pack()
    hard.place(x=370, y=300)

    instructions = Button(master, text="Instructions", font = ('Chelsea Market', 20, 'bold'), command=callinstructions)
    instructions.pack()
    instructions.place(x=230, y=500)



    # hangman structures
    def hang_holder():
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")
        print("               ===============")
        print("               H             H")
        print("               H             H")
        print("               H              ")
        print("               H              ")
        print("               H              ")
        print("               H              ")
        print("               H              ")
        print("               H              ")
        print("               H              ")
        print("               H              ")
        print("               H              ")
        print("               H              ")
        print("               H              ")
        print("               H              ")
        print("               H              ")
        print("       =================      ")
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")


    def hangman_head():
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")
        print("               ===============")
        print("               H             H")
        print("               H             H")
        print("               H            ___      ")
        print("               H           /   \     ")
        print("               H          { i i }    ")
        print("               H           \___/     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("       =================             ")
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")


    def hangman_body():
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")
        print("               ===============")
        print("               H             H")
        print("               H             H")
        print("               H            ___      ")
        print("               H           /   \     ")
        print("               H          { i i }    ")
        print("               H           \___/     ")
        print("               H            [ ]      ")
        print("               H            [ ]      ")
        print("               H            [ ]      ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("       =================             ")
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")


    def hangman_arm1():
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")
        print("               ===============")
        print("               H             H")
        print("               H             H")
        print("               H            ___      ")
        print("               H           /   \     ")
        print("               H      __  { i i }    ")
        print("               H      \ \  \___/     ")
        print("               H        \ \ [ ]      ")
        print("               H          \ [ ]      ")
        print("               H            [ ]      ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("               H                     ")
        print("       =================             ")
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")


    def hangman_arm2():
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")
        print("               ===============")
        print("               H             H")
        print("               H             H")
        print("               H            ___        ")
        print("               H           /   \       ")
        print("               H      __  { i i }  __  ")
        print("               H      \ \  \___/  / /  ")
        print("               H        \ \ [ ] / /    ")
        print("               H          \ [ ] /      ")
        print("               H            [ ]        ")
        print("               H                       ")
        print("               H                       ")
        print("               H                       ")
        print("               H                       ")
        print("               H                       ")
        print("               H                       ")
        print("       =================               ")
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")


    def hangman_leg1():
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")
        print("               ===============")
        print("               H             H")
        print("               H             H")
        print("               H            ___        ")
        print("               H           /   \       ")
        print("               H      __  { i i }  __  ")
        print("               H      \ \  \___/  / /  ")
        print("               H        \ \ [ ] / /    ")
        print("               H          \ [ ] /      ")
        print("               H            [ ]        ")
        print("               H           / |         ")
        print("               H          / /          ")
        print("               H       &&/_/           ")
        print("               H      (___/            ")
        print("               H                       ")
        print("               H                       ")
        print("       =================               ")
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")


    def hangman_leg2():
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")
        print("               ===============")
        print("               H             H")
        print("               H             H")
        print("               H            ___        ")
        print("               H           /   \       ")
        print("               H      __  { i i }  __  ")
        print("               H      \ \  \___/  / /  ")
        print("               H        \ \ [ ] / /    ")
        print("               H          \ [ ] /      ")
        print("               H            [ ]        ")
        print("               H           / | \       ")
        print("               H          / / \ \      ")
        print("               H       &&/_/   \_\&&   ")
        print("               H      (___/     \___)  ")
        print("               H                       ")
        print("               H                       ")
        print("       =================               ")
        print(
            "                                                                                                                                     ")
        print(
            "                                                                                                                                     ")


    def print_game_over():
        print('                                                                       ')
        print('                                                                       ')
        print('                                                                       ')
        print('                                                                       ')
        print('                                                                       ')
        print('                                                                       ')
        print('                                                                       ')
        print('     ...........      `......`      `````      ````` ```````````````` ')
        print('     NMMMMMMMMMM-     /MMMMMM+      MMMMs      NMMMy :MMMMMMMMMMMMMMM/')
        print('  :NNMM/````````    oMMMM``NMMMy    MMMMMMh -MMMMMMy :MMMM:`````````` ')
        print('/mNMM:-`          ymNMm--  --hMNmd  MMMMMMNmNMMMMMMy :MMMM:           ')
        print('+MMMM.   odddddd. hMMMm      hMMMN  MMMMMMMMMMMMMMMy :MMMMdddddhddd`  ')
        print('oMMMM.   :+yMMMM. hMMMNyyyyyyNMMMN  MMMMh+yMM++NMMMy :MMMMs++++++++`  ')
        print(':oyMMss-   +MMMM. hMMMNoooooomMMMN  MMMMo -oo  NMMMy :MMMM:           ')
        print('  -yyMMy+++yMMMM. hMMMd      hMMMN  MMMMo      NMMMy :MMMMs+++++++o++.')
        print('     hhhhhhhhhhh. ohhhs      ohhhy  hhhh/      hhhh+ -hhhhhhhhhhhhhhh-')
        print('                                                                      ')
        print('  -ddddhhhddhh    sdhdy      ohhdy  hhdddhdhhhhddhd+ -dhhddhddhhdhh`  ')
        print('/yhMMo+++++yMMyy. hMMMm      hMMMN  MMMMh++++++++++: :MMMMs+++++oMMyy-')
        print('oMMMM`     /MMMM. hMMMm      hMMMN  MMMMo            :MMMM-     -MMMM/')
        print('oMMMM`     /MMMM. hMMMm      hMMMN  MMMMh++++++++.   :MMMM-   .+sMMMM/')
        print('oMMMM`     /MMMM. shmMm//  :/dMNhy  MMMMmhhhhhhhh:   :MMMMo:::sMMhhhh-')
        print('oMMMM`     +MMMM.   +mmMM:-NMNms    MMMMo            :MMMMmmNMMMN--   ')
        print('+NNMM.`````+MMNN.     :NNMMNN+      MMMMs__________  :MMMM- sNMMMMM-` ')
        print('  -MMMMMMMMMMN          `MM-        MMMMMMMMMMMMMMMy :MMMM-   /MMMMMM/')
        print('   ```````````           ``         ```````````````   ````     `````` ')
        print('                                                                      ')
        print('                                                                      ')
        print('                                                                      ')
        print('                                                                       ')
        print('                                                                       ')
        print('                                                                       ')
        print(' The word was %s !' % chosen_word)


    def print_you_win():
        print('                                                                         ')
        print('                                                                         ')
        print('                                                                         ')
        print('                                                                         ')
        print('                                                                         ')
        print('                                                      ``..-`             ')
        print('                                           ```.`-.--:::-.`/:          ')
        print('                                ``--::+++-://:.`` `` `   `./`         ')
        print('                      `.-::/+/..+//:--``` `               .s:         ')
        print('           `..:://+++o+//:-.`````       ``.. .+ooo`       .:s         ')
        print('   .://++++o+/:--`````       `-://:.   /yooo``syss/       `.y.        ')
        print('   o:.` ```          .:/++  /yhhhhhhy- .ysss- +ssss        .+/        ')
        print('   o/`        -osyh: ohhh+ /yyyyssyssy: oyy+: -ysss.       .-o        ')
        print('   -/`         /yyyy.+yys. syyy+  +yyhy./ysso` syys+        `/.       ')
        print('   `y:.         :yhyyyyys  syso/  `syyy/`yyyy/ ohhys        `..       ')
        print('    +s.          .yhyyyy+  /ss++. `ssoo/ +yyyhyhhhh+        ``:`      ')
        print('    .y-           `syyyy.   /oooo++oooo.  /yhyhhyy+`         `/-      ')
        print('     o:.           `ssos-   `:so:-+yso-     .:///-  +oyy/    .:+      ')
        print('     :+.            oyyyo     `.:://- `:/+oo``hhhy  /hhhy     .o.     ')
        print('     `+-`           .:--. `--:/ /syys  syhhhs`+hhh. .hhyh-    .+:     ')
        print('      ::`     ``.-. -//++ .ysss :yyyy. /yhhhhs:hhh+  shhho    `./     ')
        print('      -s.     :+soo`-yyyy:`syys `yyyy+ .hhhhhhyyhhy` :hhys`    .s-    ')
        print('       /-.    `osys:.syysy.oyhy  +shyy` syhhsyyyhhh:  ./+:`    `/+    ')
        print('       -o.     .o/:-.+oosso+yyy  -+yyy: :yyy//yhhhho  +hhy+    `.o`   ')
        print('       `o.`     :+///+s//ssssyh`  syys+ `yyyy`/hhhyy` .oyo-     `/-   ')
        print('        /:.      :/syhy+ +yysyy`  /yyhh` +yyy- -/::-`  ___      `:o   ')
        print('        -+.      `shyyy+ .yyyyy`  .oo+/. ``            ``` .-::-.-/   ')
        print('        `+.`      .yyyyo  -/::-            ````..-//+oooo/.---``      ')
        print('         //`       ..`          `````.-:/+ooooo+/::-.`                ')
        print('         .+.`        `````.-://++oooo+/:-.`                           ')
        print('          o.```..-:::.:+oo+/:-.`                                      ')
        print('          :oooo+/:-.`                                                 ')
        print('                                                                      ')
        print('                                                                      ')
        print('                                                                      ')
        print('                                                                      ')


    # define word lists

    def easy_words():
        return ['TERRAJNL',
                'GRFYN',
                'PBZCHGRE',
                'VAGREARG',
                'FNGRYYVGR',
                'PBBBBBBY']


    def intermediate_words():
        return ['UBZBZBECUBHF',
                'QVNTENCU',
                'ZLFGVPNYYL',
                'VAGREHEONA',
                'PBZZHAVMR',
                'ZNTVFGRE',
                'ONPGREVNA',
                'UBEVMBAJNEQ',
                'ZLNEVNA',
                'FNYHGNGVBA',
                'CREFCRPGVIVGL',
                'HAFURNGUVAT',
                'FGRABTENCURE',
                'VAQVNAUBBQ',
                'CBFGSVKNY',
                'HAOERNQRQ',
                'UBYYBJARFF',
                'VASRPGBE',
                'NOHGGVAT',
                'INPPVARR',
                'OHGGBAUBYQRE',
                'VAQVTRABHFARFF',
                'FJNZL',
                'BEVTVANYYL',
                'OBBXYRG',
                'PURNCVAT',
                'NPGVINGBE',
                'ZBWB',
                'ERNPPBHAG',
                'RDHNGBEVNY',
                'CBYVB',
                'HAOYBFFBZVAT',
                'ZVAQRE',
                'GHAVAT',
                'TEBHG']


    def expert_words():
        return ['ORFGHQ',
                'TENVAVAT',
                'HAYBJYL',
                'ZLEGYROREEL',
                'UBUA',
                'PLCEVABVQRNA',
                'PHPXBBCVAG',
                'ARTNGVIVGL',
                'ORRFJNK',
                'ZVFVASYNZR',
                'ONTCVCRF',
                'NGZBFCURER',
                'HAERTNY',
                'HAVSVYNE',
                'AVTUGRQ',
                'FANCCVAT',
                'ABAPRYYHYNE',
                'CYRHEBOENAPUVNGR',
                'NATVBFCBEBHF',
                'FCRGPU',
                'CVZBYN',
                'BGVNAG',
                'HAFGEVIVAT',
                'ZRGUNQBAR',
                'ERPBAIREG',
                'CBQBQLAVN',
                'FHCENFRAFVOYR',
                'QBJAFGERRG',
                'NAGVFCYVGGVAT',
                'BOFGERCREBHFYL',
                'CBECBENGR',
                'BOFGEHPGBE',
                'ONGULYVGVP',
                'OVGGREOHFU',
                'HASNVEZVAQRQ',
                'CEBGENQR',
                'LNUTNA',
                'BFPVYYNGBEVNPRNR',
                'GVQQYRE',
                'CBYYRAVTREBHF',
                'FGNEPUYVXR',
                'HAGHPXRQ',
                'NJXJNEQYL',
                'GRTZVAN',
                'PRCUNYNGN',
                'UBHAQYVXR',
                'PEBJY',
                'FHOPYBIRE',
                'FHOBEOVPHYNE',
                'CERQRPRNFRE',
                'RZNAPVCNGVBAVFG',
                'CREIREGVOYL',
                'CNENZRAVN',
                'HAQRESBEGVSL',
                'HAQNZNTVAT',
                'CERPBAFGVGHRAG',
                'FDHNZBRCVGURYVNY',
                'WVGRAQEN',
                'QVPGNGBEFUVC',
                'NGNKVNTENCU',
                'FHCRECBFNOYR',
                'UBFCVGNOYL',
                'HAPBAQRAFVAT',
                'ZRGGYRQ',
                'IREEHPNGRQ',
                'CRBEVN',
                'QVIVFVOVYVGL',
                'ULCRECVRFVF',
                'CVPXFZNA',
                'PBAARPGVIR',
                'ULQEBGNPGVP',
                'ZRTNYBPRCUNYVN',
                'ERCREPBYNGVBA',
                'UNZNYQ',
                'BVGNIN',
                'NREBCUVYR',
                'JUVZOERY',
                'ERPHEIBGREANGR',
                'AREIVFZ',
                'CEROVQ',
                'ABEZNYVFG',
                'HACEBCURGVPNYYL',
                'GRGENQRPNCBQBHF',
                'SYHAXLVFGVP',
                'RKCRAFVIRYL',
                'BYVTBTNYNPGVN',
                'VAPBASBEZNOYR',
                'EBHAQYRG',
                'CBBYRE',
                'CNYNRBYBTVPNY',
                'ZVFFHNQR',
                'LNCC',
                'PNZCVZRGRE',
                'YBJAYL']


    def decode_word(word):
        return codecs.decode(word, "rot-13")


    def get_word_list(index):
        return [easy_words(), intermediate_words(), expert_words()][index]


    # draw hangman figure based on how many failed attempts the user made
    def draw_hangman(fails):
        hangman_functions = [hang_holder, hangman_head, hangman_body,
                             hangman_arm1, hangman_arm2, hangman_leg1,
                             hangman_leg2]
        hangman_functions[fails]()


    def print_positions(numberofletters):
        s = ''
        for i in range(0, numberofletters):
            s += ' ' + '___'
        print(s)


    def print_letters(numberofletters, letters):
        s = ''
        for i in range(0, numberofletters):
            s += '  ' + letters[i] + ' '
        print(s)


    def print_letters_and_positions(numberofletters, letters, attempts_remaining):
        print_letters(numberofletters, letters)
        print_positions(numberofletters)
        print('Attempts remaining: ' + str(attempts_remaining))


    # return user input within allowed range of values between 'lower' and 'upper' bounds with given prompt
    def select_from_range(prompt, lower, upper):
        while True:
            value = int(input(prompt))
            if lower <= value <= upper:
                break
        return value


    # execute one 'round' of the game
    def step(fails, chosen_word, letters, max_attempts):
        numberofletters = len(chosen_word)

        # if user input is a letter in the chosen word, add it to the already guessed letters,
        # otherwise, increment number of failed attempts.
        chosen_letter = input('Choose a letter: ').upper()[0]
        if chosen_letter in chosen_word:
            for i in range(0, numberofletters):
                if chosen_word[i] == chosen_letter:
                    letters[i] = chosen_letter
        else:
            fails += 1

        # show 'user interface'
        clear()
        draw_hangman(fails)
        print_letters_and_positions(numberofletters, letters, max_attempts - fails)

        # if there are still letters to guess, and there are attempts left, execute another round,
        # otherwise show outcome of game
        if fails < max_attempts:
            if ' ' in letters:
                step(fails, chosen_word, letters, max_attempts)
            else:
                print_you_win()
                satellite_sim()
        else:
            print_game_over()


    # Beginning of main program

    max_attempts = 6

    print("Welcome to Hangman!")
    time.sleep(1)

    mainloop()

    # determine game level
    #level = select_from_range('Play Easy (0), Intermediate (1), or Expert (2)? Pick a number from 0 to 2: ', 0, 2)

    words = get_word_list(level)

    print("I will think of a word and you will have " + str(max_attempts) + " guesses to find the word!")
    time.sleep(1)

    # pick word to play with
    #wordnumber = select_from_range('Pick a number between 1 and ' + str(len(words)) + ': ', 1, len(words))

    chosen_word = decode_word(words[(randint(0, len(words)))])

    print("Have Fun!!!")
    time.sleep(1)

    # initialize letters
    letters = []
    for i in range(0, len(chosen_word)):
        letters.append(' ')

    # show initial 'user interface'
    hang_holder()
    print_letters_and_positions(len(chosen_word), letters, max_attempts)

    # execute initial round
    step(0, chosen_word, letters, max_attempts)

def draw():
    master = Tk()
    import time
    global color
    color = 'blue'
    global shape
    shape = 'circle'

    def callback(event):

        if shape == 'rectangle':
            rectangle = x.create_rectangle((event.x) - float(size_slider.get()) * .5,
                                           (event.y) - float(size_slider.get()) * .5,
                                           (event.x) + float(size_slider.get()) * .5,
                                           (event.y) + float(size_slider.get()) * .5, outline=color)
            x.itemconfigure(rectangle, fill=(color))

        if shape == 'circle':
            circle = x.create_oval((event.x) - float(size_slider.get()) * .5, (event.y) - float(size_slider.get()) * .5,
                                   (event.x) + float(size_slider.get()) * .5, (event.y) + float(size_slider.get()) * .5,
                                   outline=color)
            x.itemconfigure(circle, fill=(color))

        if shape == 'triangle':
            triangle = x.create_polygon(event.x, event.y - float(size_slider.get()) * .625,
                                        event.x - float(size_slider.get()) * .75,
                                        event.y + float(size_slider.get()) * .625,
                                        event.x + float(size_slider.get()) * .75,
                                        event.y + float(size_slider.get()) * .625,
                                        )
            x.itemconfigure(triangle, fill=(color))

    w = Canvas(master, width=600, height=600, )
    w.pack()
    x = Canvas(master, width=462, height=402, )
    x.bind("<B1-Motion>", callback)
    x.bind("<Button-1>", callback)
    x.pack()
    x.place(x=122, y=72)

    def call_square():
        global shape
        print('The shape is a square!')
        shape = 'rectangle'

    def call_circle():
        global shape
        print('The shape is a circle!')
        shape = 'circle'

    def call_triangle():
        global shape
        print('The shape is a triangle!')
        shape = 'triangle'

    def call_pen():
        global color
        global shape
        print('The pen is enabled!')
        color = 'blue'
        shape = 'circle'

    def call_eraser():
        global color
        print('The eraser is enabled!')
        color = 'white'

    def call_clear():
        x.delete("all")
        print('Cleared!')

    def call_smile():
        print(':-)')
        print('This is the tkinter GUI that Ben Krueger and Aidan MacDonnel made. It is based off an old mac GUI.')

    def call_red():
        global color
        print('The color is red!')
        color = 'red'

    def call_orange():
        global color
        print('The color is orange!')
        color = 'orange'

    def call_yellow():
        global color
        print('The color is yellow!')
        color = 'yellow'

    def call_green():
        global color
        print('The color is green!')
        color = 'green'

    def call_blue():
        global color
        print('The color is blue!')
        color = 'blue'

    def call_purple():
        global color
        print('The color is purple!')
        color = 'purple'

    def call_done():
        print('quitting...')
        time.sleep(2)
        master.destroy()

    color_rectangle = w.create_rectangle(0, 350, 100, 590)
    w.itemconfigure(color_rectangle, fill='white')

    shape_rectangle = w.create_rectangle(120, 500, 590, 590)
    w.itemconfigure(shape_rectangle, fill='white')

    canvas_rectangle = w.create_rectangle(120, 70, 590, 480)
    w.itemconfigure(canvas_rectangle, fill='white')

    size_rectangle = w.create_rectangle(0, 70, 100, 330)
    w.itemconfigure(size_rectangle, fill='white')

    label = Label(master, text='SIZE', font=('Courier', 20, 'bold'))
    label.pack()
    label.place(x=20, y=80)

    size_slider = Scale(master, from_=0, to=100, length=200, tickinterval=20)
    size_slider.pack()
    size_slider.place(x=0, y=120)

    color_list = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']

    shape_list_top = [' Square ', '  Circle  ', 'Triangle']

    shape_list_bottom = [' Pen  ', 'Eraser', ' Clear', ':-)']

    call_back_lst_color = {'Red': call_red, 'Orange': call_orange, 'Yellow': call_yellow, 'Green': call_green,
                           'Blue': call_blue, 'Purple': call_purple}

    call_back_lst_shape_top = {' Square ': call_square, '  Circle  ': call_circle, 'Triangle': call_triangle}

    call_back_lst_shape_bottom = {' Pen  ': call_pen, 'Eraser': call_eraser, ' Clear': call_clear, ':-)': call_smile}

    def button_creator_color(color_list, callback):
        height = 315
        for i in color_list:
            height = height + 40
            color_button = Button(master, text=i, font=('Chelsea Market', 15, 'bold'), command=callback[i])
            color_button.pack()
            color_button.place(x=15, y=height)

    def button_creator_shapes(shape_list, length, height, callback):
        for i in shape_list:
            length = length + 100
            shape_button = Button(master, text=i, font=('Chelsea Market', 15, 'bold'), command=callback[i])
            shape_button.pack()
            shape_button.place(x=length, y=height)

    done = Button(master, text='QUIT', font=('Courier', 20, 'bold'), command=call_done)
    done.pack()
    done.place(x=530, y=10)

    button_creator_color(color_list, call_back_lst_color)
    button_creator_shapes(shape_list_top, 50, 510, call_back_lst_shape_top)
    button_creator_shapes(shape_list_bottom, 50, 550, call_back_lst_shape_bottom)

def flashcards_and_planner_2_in_1():
    master = Tk()

    title_screen = Canvas(master, width=800, height=800, bg='#6960EC')
    title_screen.pack()

    global x
    x = 0

    global next_button
    next_button = True

    math = False
    la = False
    science = False
    history = False
    language = False
    other = False

    def Finished_command():
        call_flashcards()
        flash_title()
        flash_sequence()

    b = 0

    def return_word(hello):
        global word_input
        global def_input
        global definition
        global Flash_num
        global b
        b = b + 1
        if len(term_list) == 0:
            flash_num_label_term = Label(master_flash_input, text='You have 1 flashcard', font=('Bodoni', 25, 'bold'),
                                         fg='black', bg='white')
            flash_num_label_term.pack()
            flash_num_label_term.place(x=300, y=500)
        else:
            flash_num_label_term = Label(master_flash_input,
                                         text='You have ' + (str(len(term_list) + 1)) + ' flashcards',
                                         font=('Bodoni', 25, 'bold'), fg='black', bg='white')
            flash_num_label_term.pack()
            flash_num_label_term.place(x=300, y=500)
        word_input = word.get()
        def_input = definition.get()
        word.delete(0, 'end')
        definition.delete(0, 'end')
        term_list.append(word_input)
        definition_list.append(def_input)
        print('hello')
        print(term_list)
        print(definition_list)
        Flash_num = word_count

    def OK_command():
        global word_count
        global term_list
        global definition_list
        global word_input
        global word
        global definition
        global def_input

        word_count = flash_num_slider.get()
        print(word_count)
        term_list = []
        definition_list = []

        for x in range(0, word_count):
            word_input = ''
            def_input = ''
            word = Entry(master_flash_input)
            word.pack()
            word.place(x=325, y=300)

            definition = Entry(master_flash_input)
            definition.pack()
            definition.place(x=325, y=400)
            definition.bind('<Return>', return_word)

            instruction_label_enter = Label(master_flash_input,
                                            text="Enter the term, then the definiton, then click enter.\n Once you have entered all your flashcards\n click finished.",
                                            font=('Bodoni', 25, 'bold'), fg='black', bg='white')
            instruction_label_enter.pack()
            instruction_label_enter.place(x=100, y=50)

            instruction_label_term = Label(master_flash_input, text="Term:", font=('Bodoni', 25, 'bold'), fg='black',
                                           bg='white')
            instruction_label_term.pack()
            instruction_label_term.place(x=250, y=295)

            instruction_label_definition = Label(master_flash_input, text="Defintion:", font=('Bodoni', 25, 'bold'),
                                                 fg='black', bg='white')
            instruction_label_definition.pack()
            instruction_label_definition.place(x=200, y=395)

            OK_button.destroy()
            flash_num_slider.destroy()
            instruction_label.destroy()

        Finished_button = Button(master_flash_input, text="Finished", font=('Bodoni', 25, 'bold'), fg='black',
                                 bg='White', command=Finished_command)
        Finished_button.pack()
        Finished_button.place(x=350, y=750)

    def create_flashcards():
        global master_flash_input
        global flashcard_input
        global flash_num_slider
        global OK_button
        global instruction_label
        master_flash_input = Tk()
        flashcard_input = Canvas(master_flash_input, width=800, height=800, bg='white')
        flashcard_input.pack()
        instruction_label = Label(master_flash_input, text="Enter the amount of flashcards\n you wish to make!",
                                  font=('Bodoni', 25, 'bold'), fg='black', bg='white')
        instruction_label.pack()
        instruction_label.place(x=250, y=50)
        flash_num_slider = 0
        flash_num_slider = Scale(master_flash_input, from_=0, to=50, length=360, tickinterval=10,
                                 font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
        flash_num_slider.pack()
        flash_num_slider.place(x=250, y=150)
        OK_button = Button(master_flash_input, text="OK", font=('Bodoni', 25, 'bold'), fg='black', bg='White',
                           command=OK_command)
        OK_button.pack()
        OK_button.place(x=400, y=750)

    def next_command():
        global x
        global next_button
        next_button = True
        x = x + 1
        if x >= len(term_list):
            print("Sorry, you ain't got no more flashcards.")
            x = x - 1
        else:
            Word.destroy()
            flash_title()
            flash_sequence()

    def flip_command():
        global next_button
        if next_button == True:
            next_button = False
            Word.destroy()
            flash_title()
            flash_sequence()
        else:
            next_button = True
            Word.destroy()
            flash_title()
            flash_sequence()

    def done_command():
        global hour
        global minute
        global schedule_canvas
        global master_4
        master_4 = Tk()

        hour = input('Enter the hour you want to start:')
        if (0 >= hour) or (hour > 12) or (type(hour) != int):
            print('Invalid input. Try again.')
            done_command()
        minute = input('Enter the minute you want to start as a two digit number:')
        if (0 > minute) or (minute > 59) or (type(minute) != int):
            print('Invalid input. Try again.')
            done_command()
        else:
            if minute < 10:
                print (str(hour) + ':0' + str(minute))
            else:
                print (str(hour) + ':' + str(minute))
        schedule_canvas = Canvas(master_4, width=800, height=800, bg='white')
        schedule_canvas.pack()
        create_schedule()
        create_planner(subjects_with_hw)
        clock_time(time_for_subjects)

    def flash_sequence():
        flash_buttons()

        if next_button == True:
            global Word
            Word = Label(flashcard_canvas, text=term_list[x], font=('Bodoni', 50, 'bold'), fg='black', bg='white')
            Word.pack()
            Word.place(x=210, y=400)
            flash_buttons()
        else:
            Word = Label(flashcard_canvas, text=definition_list[x], font=('Bodoni', 50, 'bold'), fg='black', bg='white')
            Word.pack()
            Word.place(x=210, y=400)
            flash_buttons()

    next_true = False

    def flash_buttons():
        global master_2
        next_button = Button(master_2, text="Next", font=('Bodoni', 25, 'bold'), fg='black', bg='White',
                             command=next_command)
        next_button.pack()
        next_button.place(x=710, y=750)
        flip_button = Button(master_2, text="Flip", font=('Bodoni', 25, 'bold'), fg='black', bg='White',
                             command=flip_command)
        flip_button.pack()
        flip_button.place(x=10, y=750)

    def call_flashcards():
        global master_2
        global flashcard_canvas
        master_2 = Tk()
        flashcard_canvas = Canvas(master_2, width=800, height=800, bg='white')
        flashcard_canvas.pack()

    def flash_title():
        Title_flash = Label(master_2, text='Flash Time', font=('Bodoni', 50, 'bold'), fg='blue', bg='white')
        Title_flash.pack()
        Title_flash.place(x=275, y=100)

    def planner_title():
        Title_planner = Label(master_3, text='How much time will\n you spend on each subject?',
                              font=('Bodoni', 35, 'bold'), fg='black', bg='white')
        Title_planner.pack()
        Title_planner.place(x=160, y=10)

    def done_button():
        done_button = Button(master_3, text="Done", font=('Bodoni', 25, 'bold'), fg='black', bg='White',
                             command=done_command)
        done_button.pack()
        done_button.place(x=362.5, y=750)

    def label_creator_subject(subject_list):
        height = 0
        global subject_label
        for i in subject_list:
            height = height + 110
            subject_label = Label(master_3, text=i, font=('Bodoni', 25, 'bold'), fg='black', bg='white')
            subject_label.pack()
            subject_label.place(x=15, y=height)

    def slider_creator_time():
        height = 0
        global slider_button_math
        global slider_button_Language_arts
        global slider_button_science
        global slider_button_history
        global slider_button_language
        global slider_button_other

        height = height + 110
        slider_button_math = Scale(master_3, from_=0, to=110, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'),
                                   orient=HORIZONTAL)
        slider_button_math.pack()
        slider_button_math.place(x=425, y=height)

        height = height + 110
        slider_button_Language_arts = Scale(master_3, from_=0, to=110, length=360, tickinterval=10,
                                            font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
        slider_button_Language_arts.pack()
        slider_button_Language_arts.place(x=425, y=height)

        height = height + 110
        slider_button_science = Scale(master_3, from_=0, to=110, length=360, tickinterval=10,
                                      font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
        slider_button_science.pack()
        slider_button_science.place(x=425, y=height)

        height = height + 110
        slider_button_history = Scale(master_3, from_=0, to=110, length=360, tickinterval=10,
                                      font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
        slider_button_history.pack()
        slider_button_history.place(x=425, y=height)

        height = height + 110
        slider_button_language = Scale(master_3, from_=0, to=110, length=360, tickinterval=10,
                                       font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
        slider_button_language.pack()
        slider_button_language.place(x=425, y=height)

        height = height + 110
        slider_button_other = Scale(master_3, from_=0, to=110, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'),
                                    orient=HORIZONTAL)
        slider_button_other.pack()
        slider_button_other.place(x=425, y=height)

    def create_schedule():
        global subjects_with_hw
        global time_for_subjects
        subjects_with_hw = []
        time_for_subjects = []
        if slider_button_math.get() > 0:
            print('You have ' + str(slider_button_math.get()) + ' minutes of Math.')
            subjects_with_hw.append('Math')
            time_for_subjects.append(slider_button_math.get())
        if slider_button_Language_arts.get() > 0:
            print('You have ' + str(slider_button_Language_arts.get()) + ' minutes of Language Arts.')
            subjects_with_hw.append('Language Arts')
            time_for_subjects.append(slider_button_Language_arts.get())
        if slider_button_science.get() > 0:
            print('You have ' + str(slider_button_science.get()) + ' minutes of Science.')
            subjects_with_hw.append('Science')
            time_for_subjects.append(slider_button_science.get())
        if slider_button_history.get() > 0:
            print('You have ' + str(slider_button_history.get()) + ' minutes of History.')
            subjects_with_hw.append('History')
            time_for_subjects.append(slider_button_history.get())
        if slider_button_language.get() > 0:
            print('You have ' + str(slider_button_language.get()) + ' minutes of Language.')
            subjects_with_hw.append('Language')
            time_for_subjects.append(slider_button_language.get())
        if slider_button_other.get() > 0:
            print('You have ' + str(slider_button_other.get()) + ' minutes of Somthing else.')
            subjects_with_hw.append('Other')
            time_for_subjects.append(slider_button_other.get())

        print(subjects_with_hw)
        print(time_for_subjects)

    def clock_time(time_for_subjects):
        global time
        global time_label
        global time_hour
        global time_minute
        global time_clock_label
        global time_clock_label_1
        global time_clock_label_2
        global hour1
        global minute1
        global hour2
        global minute2
        global minute_string
        global minute_string_two
        global height
        global minute_string_zero
        height = 110
        minute_string = ''
        minute_string_two = ''
        if minute < 10:
            minute_string_zero = str('0' + str(minute))
            time_clock_label = Label(master_4, text=('Start at: ' + str(hour) + ':' + str(minute_string_zero)),
                                     font=('Bodoni', 25, 'bold'), fg='black', bg='white')
            time_clock_label.pack()
            time_clock_label.place(x=550, y=110)
        else:
            time_clock_label = Label(master_4, text=('Start at: ' + str(hour) + ':' + str(minute)),
                                     font=('Bodoni', 25, 'bold'), fg='black', bg='white')
            time_clock_label.pack()
            time_clock_label.place(x=550, y=110)
        time_hour = time_for_subjects[0] / 60
        time_minute = time_for_subjects[0] % 60
        hour1 = hour + time_hour
        minute1 = minute + time_minute
        if minute1 >= 60:
            hour1 = hour1 + 1
            minute1 = minute1 - 60
        if minute1 < 10:
            minute_string = str('0' + str(minute1))
            time_clock_label = Label(master_4, text=('Start at: ' + str(hour1) + ':' + str(minute_string)),
                                     font=('Bodoni', 25, 'bold'), fg='black', bg='white')
            time_clock_label.pack()
            time_clock_label.place(x=550, y=220)
        else:
            print(str(hour1) + ':' + str(minute1) + ' minute1')
            time_clock_label = Label(master_4, text=('Start at: ' + str(hour1) + ':' + str(minute1)),
                                     font=('Bodoni', 25, 'bold'), fg='black', bg='white')
            time_clock_label.pack()
            time_clock_label.place(x=550, y=220)

        height = 330
        for j in range(1, len(time_for_subjects) - 1):

            hour2 = time_for_subjects[j] / 60
            minute2 = time_for_subjects[j] % 60
            print('Hour one is ' + str(hour1))
            print('Hour two is ' + str(hour2))
            hour2 = hour1 + hour2
            minute2 = minute2 + minute1
            if minute2 >= 60:
                hour2 = hour2 + 1
                minute2 = minute2 - 60
            if minute2 < 10:
                minute_string_two = ('0' + str(minute2))
                print(str(hour2) + ':' + minute_string_two + ' minute string 2')
                print(str(hour2) + ':' + str(minute2) + ' minute 2')
                time_clock_label = Label(master_4, text=('Start at: ' + str(hour2) + ':' + str(minute_string_two)),
                                         font=('Bodoni', 25, 'bold'), fg='black', bg='white')
                time_clock_label.pack()
                time_clock_label.place(x=550, y=height)
            else:
                print(str(hour2) + ':' + str(minute2) + ' minute 2')
                time_clock_label = Label(master_4, text=('Start at: ' + str(hour2) + ':' + str(minute2)),
                                         font=('Bodoni', 25, 'bold'), fg='black', bg='white')
                time_clock_label.pack()
                time_clock_label.place(x=550, y=height)
                hour1 = hour2
                minute1 = minute2
                height = height + 110

        height = 0
        for i in range(0, len(time_for_subjects)):
            height = height + 110
            time = time_for_subjects[i]
            time_label = Label(master_4, text=(str(time) + ' minutes'), font=('Bodoni', 25, 'bold'), fg='black',
                               bg='white')
            time_label.pack()
            time_label.place(x=350, y=height)

    def selection_screen():
        global subject_list
        global call_back_list
        subject_list = ['Math', 'Language Arts', 'Science', 'History', 'Language', 'Other']
        label_creator_subject(subject_list)
        slider_creator_time()
        planner_title()
        done_button()

    def create_planner(subjects_with_hw):
        planner_label = Label(master_4, text='Schedule', font=('Bodoni', 60, 'bold'), fg='black', bg='white')
        planner_label.pack()
        planner_label.place(x=255, y=10)
        height = 0
        for x in subjects_with_hw:
            height = height + 110
            schedule_label = Label(master_4, text=x, font=('Bodoni', 25, 'bold'), fg='black', bg='white')
            schedule_label.pack()
            schedule_label.place(x=15, y=height)

    def call_planner():
        global master_3
        global planner_canvas
        global math_time
        master_3 = Tk()
        planner_canvas = Canvas(master_3, width=800, height=800, bg='white')
        planner_canvas.pack()
        selection_screen()

    Title_main = Label(master, text='Homework Planner', font=('Bodoni', 60, 'bold'), fg='#5CB3FF', bg='#6960EC')
    Title_main.pack()
    Title_main.place(x=150, y=100)

    flashcard_button = Button(master, text="Flashcards", font=('Bodoni', 25, 'bold'), fg='black', bg='#6960EC',
                              command=create_flashcards)
    flashcard_button.pack()
    flashcard_button.place(x=320, y=300)

    planner_button = Button(master, text="Planner", font=('Bodoni', 25, 'bold'), fg='black', bg='#6960EC',
                            command=call_planner)
    planner_button.pack()
    planner_button.place(x=340, y=400)

    Coders_label = Label(master, text='By: \n Ben Krueger and \n Aidan MacDonell', font=('Bodoni', 35, 'bold'),
                         fg='#5CB3FF', bg='#6960EC')
    Coders_label.pack()
    Coders_label.place(x=250, y=500)


hangmn_game()
mainloop()