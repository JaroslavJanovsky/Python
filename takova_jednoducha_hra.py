def play_game():
    print(" ")
    print(" ")    
    print("			Vítám Tě v tomto krátkém příběhu.")
    print(" ")
    print("Stifler, největší pařmen a prcíř všech dob, si u Tebe v bytě uspořádal pařbu, když jsi byl pryč. ")
    print("Vrátíš se na byt, kde nevěřícně koukáš na ten bordel: obrazy, co visely na zdi, ")
    print("jsou teď podtácky na pivo, a místo nich teď visí trencle a tanga......")
    print("			......v kuchyni je nablito......")
    print("			......na stropě taky......")
    print("			.......v obýváku ne......")
    print("......ale je tam Stifler na gauči. Na otázku ,,Proč na sobě nic nemáš?'' odpoví ,,Je vedro. ''.")
    print("Na otázku ,,A proč máš nasazenej kondom, ty vole?!?'' odpoví ,,No zas takové vedro není.'' ")
    print(" ")
    print("Máš na výběr z těchto pěkných oslovení:")
    print(" ")
    print("a)Dobytek")
    print("b)Hovado")
    print("c)Kretén")
    print("d)žádné")
    print(" ")
    print(" ")
    print(" ")
    
    while True:
        # Ask the player to pick one insult
        insult = input("Tak co to bude?: ").lower()
        
        # Check if the insult is valid

        if insult == 'a':
            print(' ')
            print('Ty dobytku jeden ožralej!')
            print(' ')
        elif insult == 'b':
            print(' ')
            print('Hovado vypatlaný!')
            print(' ')
        elif insult == 'c':
            print(' ')
            print('že tě tvoje máma radši nepolkla, kreténe!')
            print(' ')
        elif insult == 'd':
            print(f' ')
            print('Jebat....')
            print('...')
            print('...')
            print('...')
            print('..., řekneš si pro sebe, a dáš Stiflerovi pěstí tak, že usne na gauči.')
            print(' ')
            print('Pak si jdeš lehnout do ložnice mezi hromadu těl na posteli,')
            print('přikryješ se Helenou, a taky usneš, páč nemáš sílu teď něco uklízet ani řešit.')
            print(' ')
            print('Inu, dobrého po málu.')
            print(' ')
            print(' ')
            print(' ')
            print(' ')
            break
        else:
            print('Retard je Stifler, ne Ty. Zadej buď a, b, c nebo d. Takže znova:')


def main():
    while True:
        play_game()
        play_again = input("			Chceš si ten krátký příběh zopakovat? (ok/leda hovno): ").lower()
        if play_again != 'ok':
            print(" ")
            print(" ")
            print("Ne? Tak už si jdi taky lehnout nebo dostaneš hudlana........ale ne od Helenky!")
            break

if __name__ == "__main__":
    main()
