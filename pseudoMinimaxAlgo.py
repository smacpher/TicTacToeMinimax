import logging

choice = None

def minimax(state, is_turn, depth):

    # base case
    if is_end_game_state(state): # game is either 1) a tie 2) ai won 3) other player won

        return get_score(state, is_turn)

    else:   

        scores = []
        moves = []

        possible_moves = get_possible_moves(move)

        for child_state in possible_moves: # generate the moves

            scores.append(minimax(child_state), not is_turn)
            moves.append(move(child_state)) # generate a move from the child_state

        if is_turn: # AI (max) player's turn

            max_score_index = scores.find(max(scores))

            choice = moves[max_score_index]

            return scores[max_score_index] # AI's turn: return the highest score
        else: # Opponents (min) player's turn

            min_score_index = scores.find(min(scores))

            choice = moves[min_score_index] 

            return scores[min_score_index] # Opponent's turn: return the lowest score



