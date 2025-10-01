def get_star_rating(average):
    """Returns a star rating based on average points."""
    if average >= 35:
        return "★★★★★"
    elif average >= 30:
        return "★★★★☆"
    elif average >= 25:
        return "★★★☆☆"
    elif average >= 20:
        return "★★☆☆☆"
    else:
        return "★☆☆☆☆"

def athlete_performance_tracker():
    """Main function to track athlete performance in a sports season."""
    print("=== Athlete Performance Tracker ===\n")
    
    sport = input("Enter sport: ")
    season = input("Enter season: ")
    
    try:
        num_games = int(input("Enter number of games in season: "))
        num_players = int(input("Enter number of players to track: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return
    
    players = []

    print("\n=== Enter Player Data ===\n")
    
    for i in range(1, num_players + 1):
        print(f"Player {i}/{num_players}")
        name = input("Name: ")
        stats = []

        for game in range(1, num_games + 1):
            while True:
                try:
                    points = float(input(f"Game {game} points: "))
                    stats.append(points)
                    break
                except ValueError:
                    print("Invalid input. Enter a number.")
        
        player_data = {
            "name": name,
            "stats": stats,
            "average": sum(stats) / len(stats),
            "best_game": max(stats),
            "worst_game": min(stats),
            "best_game_index": stats.index(max(stats)) + 1,
            "worst_game_index": stats.index(min(stats)) + 1
        }
        players.append(player_data)
        print()

    print("=== Season Performance Report ===")
    print(f"Sport: {sport} | Season: {season} | Games: {num_games} | Players: {num_players}\n")

    top_player = max(players, key=lambda x: x["average"])

    for player in players:
        print(f"--- {player['name']} ---")
        print(f"Best Game: {int(player['best_game'])} points (Game {player['best_game_index']})")
        print(f"Worst Game: {int(player['worst_game'])} points (Game {player['worst_game_index']})")
        print(f"Season Average: {player['average']:.1f} points/game")
        print(f"Season Rating: {get_star_rating(player['average'])}\n")

    print("=== Summary ===")
    print(f"Top Performer: {top_player['name']} ({top_player['average']:.1f} avg)")

athlete_performance_tracker()
