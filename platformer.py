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
        level=1
        master.destroy()
    def callhard():
        global level
        level=2
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
        return ['GRFYN',
                'CLGUBA',
                'PBBY',
                'TERRAJNL',
                'QVABFNHE',
                'ZNPVAGBFU',
                'FHASYBJRE',
                'ERBCRA',
                'HANOYR',
                'FUHQQRE',
                'UBHEYL',
                'LN',
                'HCFPNYR',
                'NZCHGRR',
                'FGHSSL',
                'TENZC',
                'FYBO',
                'YBFRE',
                'TENFF']


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

hangmn_game()
mainloop()