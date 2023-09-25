def print_winners(top1, top2, top3):
    print(f"""          {top1}          
  {top2}  
                  {top3}  
   II      I      III   
""")


def main():
    players = {
        int(input()): 'Петя',
        int(input()): 'Вася',
        int(input()): 'Толя',
    }

    sorted_players = dict(sorted(players.items(), reverse=True))

    print_winners(*sorted_players.values())


if __name__ == '__main__':
    main()
