def update_container (id, state):
    x = "UPDATE Containers set condition_con = "+str(state)
    return x


def update_user_score (id, score):
    x = "UPDATE Users set pts_usr = pts_usr + "+str(score)
    return x
