def player(prev_play, opponent_history=[]):
    # Append the previous play to opponent's history for tracking
    if prev_play:
        opponent_history.append(prev_play)

    # Create counters for each type of strategy we will implement
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # First move: if no history, start with a default response
    if not opponent_history:
        return "R"

    # Strategy 1: Most frequent move of the opponent
    if len(opponent_history) > 1:
        last_ten = opponent_history[-10:]  # last 10 moves of the opponent
        most_frequent_move = max(set(last_ten), key=last_ten.count)
        return ideal_response[most_frequent_move]

    # Strategy 2: Mirror opponent's previous play for unpredictability
    if len(opponent_history) > 3:
        play_order = {"RR": 0, "RP": 0, "RS": 0,
                      "PR": 0, "PP": 0, "PS": 0,
                      "SR": 0, "SP": 0, "SS": 0}
        last_two = "".join(opponent_history[-2:])
        if len(last_two) == 2:
            play_order[last_two] += 1

        prediction = max(play_order, key=play_order.get)[-1:]
        return ideal_response[prediction]

    # If above strategies are inconclusive, choose randomly
    return ideal_response[opponent_history[-1]]
