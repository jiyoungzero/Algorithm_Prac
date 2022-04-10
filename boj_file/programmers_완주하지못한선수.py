def solution(participant, completion):
    answer = ''
    for par in participant:
        for com in completion:
            if par == com:
                participant.remove(par)
                completion.remove(par)
                if par in participant:
                    answer = par
                    return answer
    answer = participant[0]
    return answer
