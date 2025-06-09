import matplotlib.pyplot as plt

def calculate_payout(prize_pot, num_players):
    return prize_pot / num_players

def visualize_game(prize_pot, initial_players):
    players = initial_players
    payouts = []

    while players > 0:
        payout_per_person = calculate_payout(prize_pot, players)
        payouts.append(payout_per_person)
        players -= 1

    plt.plot(range(initial_players, 0, -1), payouts, marker='o')
    plt.title('Squid Game Payout Visualization')
    plt.xlabel('Number of Players')
    plt.ylabel('Payout per Person')

    # Reverse the x-axis
    plt.gca().invert_xaxis()

    # Set y-axis to logarithmic scale
    plt.yscale('log')

    plt.show()

# Example: visualize the game with an initial prize pot of $1,000,000 and 456 players
visualize_game(4.56e6, 456)
