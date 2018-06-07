import cx_Freeze

executables = [cx_Freeze.Executable("memory.py")]

cx_Freeze.setup(
    name = "Memory Lane",
    options = {"build.exe":{"packages":["pygame"],"include_files":["data/snd/a.ogg","data/snd/card.ogg","data/snd/gameOver.ogg","data/snd/helpMusic.ogg","data/snd/inGame.ogg","data/snd/intro.ogg","data/snd/intro.wav","data/snd/noPair.ogg","data/snd/pair.ogg","data/snd/win.ogg","data/fnt/KLEPTOMA.TTF","data/fnt/scribble.TTF","data/fnt/ShakeThatBooty.ttf","data/img/1red.png","data/img/2red.png","data/img/3red.png","data/img/4red.png","data/img/5red.png","data/img/6red.png","data/img/back.png","data/img/button.png","data/img/button2.png","data/img/card.png","data/img/cards2.png","data/img/cards2b.png","data/img/cards3.png","data/img/cards4.png","data/img/change2.png","data/img/circle.png","data/img/circle2.png","data/img/circle3.png","data/img/circle4.png","data/img/circle5.png","data/img/circle6.png","data/img/city.jpg","data/img/city.png","data/img/cityglow.png","data/img/continue.png","data/img/desert.png","data/img/desertglow.png","data/img/Help_Blue.png","data/img/Help_Turquoise.png","data/img/img1.png","data/img/img2.png","data/img/img3.png","data/img/img4.png","data/img/img5.png","data/img/img6.png","data/img/img7.png","data/img/img8.png","data/img/img9.png","data/img/img10.png","data/img/img11.png","data/img/img12.png","data/img/instruction2.png","data/img/instructions.png","data/img/jungle.jpg","data/img/jungle.png","data/img/jungleglow.png","data/img/logo.png","data/img/rank1.png","data/img/rank2.png","data/img/rank3.png","data/img/ranke4.png","data/img/words.png"]}},
    description = "Memory Game",
    icon = "icon.ico",
    executables = executables
    )
