def judge_circle(moves):
    if moves.lower().count('u') == moves.lower().count('d') and moves.lower().count('l') == moves.lower().count('r'):
        return True
    else:
        return False
print(judge_circle(input()))