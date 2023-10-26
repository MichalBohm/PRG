print("Jsi v místnosti. Můžeš jít dál všemi 4-mi směry. Proč? Protože chceš poklad. To dá rozum ne?")
print("1) Jdi na sever")
print("2) Jdi na jih")
print("3) Jdi na východ")
print("4) Jdi na západ")
mistnost3=""
smer=input("Zadej volbu:")
while mistnost3!="b":
    if smer=="sever":
        print("Šel jsi na sever a vešel jsi do místnosti se třemi dveřmi")
        print("a) Jdi do prvních dveří")
        print("b) Jdi do druhých dveří")
        print("c) Jdi do třetích dveří")
        print("d) Jít zpět")
        mistnost1=input("Zadej volbu:")

        if mistnost1 == "a":
            print("V téhle místnosti se poklad nenachází, co sis myslel? Asi až moc velký optimista")
        elif mistnost1=="b":
            print("Narazil jsi na strážce, který tě nepustil dál, i kdyby tam měl stát celý svůj život")
        elif mistnost1=="c":
            print("Vešel jsi do prázdné místnosti a cítíš se zle")
        elif mistnost1=="d":
            print("Šel si zpět zklamaný se svou vlastní neschopností \n")
            print("1) Jdi na sever")
            print("2) Jdi na jih")
            print("3) Jdi na západ")
            print("4) Jdi na východ") 
            smer=input("Zadej volbu:")
        else:
            print("Chyba vstupu")

    if smer=="jih":
        print("Šel jsi na jih a vešel jsi do místnosti se třemi dveřmi")
        print("a) Jdi do prvních dveří")
        print("b) Jdi do druhých dveří")
        print("c) Jdi do třetích dveří")
        print("d) Jít zpět")
        mistnost2=input("zadej volbu:")

        if mistnost2=="a":
            print("V téhle místnosti je úplné prázdno, sedíš tam chvíli a přemýšlíš o svých životních rozhodnutích. 'Možná jsem měl zůstat doma :('")
        elif mistnost2=="b":
            print("Vešel jsi do místnosti rozhledl se a jediné co jsi zahlédl byla malba na stěně, vypadala podobně jako známý obrázek trollface.")
        elif mistnost2=="c":
            print("Narazil jsi na starce, který ti pověděl, že v této místnosti se poklad nenachází. Ty mu věříš? Proč.")
        elif mistnost2=="d":
            print("Šel si zpět zklamaný se svou vlastní neschopností \n")
            print("1) Jdi na sever")
            print("2) Jdi na jih")
            print("3) Jdi na západ")
            print("4) Jdi na východ") 
            smer=input("Zadej volbu:")
        else:
            print("Chyba vstupu")

    if smer=="východ":
        print("Šel jsi na západ a vešel jsi do místnosti se třemi dveřmi")
        print("a) Jdi do prvních dveří")
        print("b) Jdi do druhých dveří")
        print("c) Jdi do třetích dveří")
        print("d) Jít zpět")
        mistnost3=input("zadej volbu:")

        if mistnost3=="a":
            print("Vešel jsi do dveři, ale za dveřmi se nenacházi ani místnost")
        elif mistnost3=="b":
            print("Našel jsi poklad, stálo ti to za to? Myslíš si, že se ti zlepšil život po nalazení tohodle pokladu?")
        elif mistnost3=="c":
            print("Tady poklad není")
        elif mistnost3=="d":
            print("Šel si zpět celkem štastný z nějákeho důvodu? \n")
            print("1) Jdi na sever")
            print("2) Jdi na jih")
            print("3) Jdi na západ")
            print("4) Jdi na východ") 
            smer=input("Zadej volbu:")
        else:
            print("Chyba vstupu")

    if smer=="západ":
        print("Šel jsi na východ a vešel jsi do místnosti se třemi dveřmi")
        print("a) Jdi do prvních dveří")
        print("b) Jdi do druhých dveří")
        print("c) Jdi do třetích dveří")
        print("d) Jít zpět")
        mistnost4=input("zadej volbu:")

        if mistnost4=="a":
            print("Tahle cesta nevede k pokladu, možná někde v Japonsku bude.")
        elif mistnost4=="b":
            print("Vešel jsi do prázdne místnosti, kde byla taková špatná energie. Možná tam někde je domácí úkol.")
        elif mistnost4=="c":
            print("V místnosti se nachází obr, který tě nepustí dál. Sice si se ho neptal na jeho názor, ale bojíš se ho.")
        elif mistnost4=="d":
            print("Šel si zpět celkem celkem naštvanej, kdo by to řekl? :D \n")
            print("1) Jdi na sever")
            print("2) Jdi na jih")
            print("3) Jdi na západ")
            print("4) Jdi na východ") 
            smer=input("Zadej volbu:")
        else:
            print("Chyba vstupu")

print("Vyhrál si... Co přesně? Jak to mám vědět. Ale vrátil si se domů za svojí rodinou změněný touhle výpravou, nikdy nebudeš stejný.")
print("""    ⠀         ⣰⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣦⣀⡀⠀⢀⣴⣇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
    ⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
    ⠀⠀⠀⣴⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⣾⣿⣿⣿⣿⣿⣶⣿⣯⣭⣬⣉⣽⣿⣿⣄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
    ⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
    ⢸⣿⣿⣿⣿⠟⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⣿⣿⣿⣿⡿⠛⠉⠉⠉⠉⠁
    ⠘⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀""")