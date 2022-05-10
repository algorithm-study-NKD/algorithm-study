def solution(numbers, target):
    answer = 0
    tree = [0]
    
    for n in numbers:
        node = []
        for t in tree:
            node.append(t+n)
            node.append(t-n)
        tree = node

    answer = tree.count(target)
    
    return answer