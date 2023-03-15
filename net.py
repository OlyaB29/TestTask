
def check_relation(net, first, second):
    prev_prev_level_friends = []
    prev_level_friends = [first]
    while len(prev_level_friends):
        next_level_friends = []
        for person in prev_level_friends:
            friends_of_person = seach_friends(net, person, prev_prev_level_friends+prev_level_friends+next_level_friends)
            if second in friends_of_person:
                return True
            next_level_friends += friends_of_person
        prev_prev_level_friends += prev_level_friends
        prev_level_friends = next_level_friends
    return False


def seach_friends(net, person, friends):
    net_of_person = list(filter(lambda el: person in el, net))
    friends_of_person = list(map(lambda el: el[el[0] == person], net_of_person))
    return list(filter(lambda el: el not in friends, friends_of_person))



if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )
    print(check_relation(net, "Лена", "Маша"))
# assert check_relation(net, "Петя", "Стёпа") is True
# assert check_relation(net, "Маша", "Петя") is True
# assert check_relation(net, "Ваня", "Дима") is False
# assert check_relation(net, "Лёша", "Настя") is False
# assert check_relation(net, "Стёпа", "Маша") is True
# assert check_relation(net, "Лена", "Маша") is False
# assert check_relation(net, "Вова", "Лена") is True
