# 프로그래머스 '다단계 칫솔 판매'
# https://programmers.co.kr/learn/courses/30/lessons/77486

class Node:
    def __init__(self, name, referral):
        self.name = name
        self.referral = referral
        self.money = 0

    def __repr__(self) -> str:
        return "(" + self.name + ", " + self.referral + ", " + str(self.money) + ")"


def solution(enroll, referral, seller, amount):
    node_dict = dict()

    for i in range(len(enroll)):
        name = enroll[i]
        referral_name = referral[i]
        node_dict[name] = Node(name, referral_name)
        
    for i in range(len(seller)):
        name = seller[i]
        money = amount[i] * 100
        
        while True:
            give_money = money // 10
            my_money = money - give_money

            node = node_dict[name]
            node.money += my_money
            
            name = node.referral
            money = give_money

            if name == '-' or money == 0:
                break
    
    answer = []

    for name in enroll:
        answer.append(node_dict[name].money)

    return answer