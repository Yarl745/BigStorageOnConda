from collections import deque
# ----------------------------------------------------------------------------------------------------------------------
graph = {}
graph['you'] = ['bob', 'claire', 'alice']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tom', 'jonny']
graph['anuj'] = []; graph['peggy'] = []; graph['tom'] = []; graph['jonny'] = []
#
search_deque = deque()
search_deque += graph['you']
#
reapet_test = {}
# ----------------------------------------------------------------------------------------------------------------------
def person_is_seller(name):
    return name[-1] == 'z'
#
while search_deque:
    print(search_deque)
    friend = search_deque.popleft()
    if reapet_test.get(friend):
        print('repeat!!!')
        continue
    elif person_is_seller(friend):
        print('the orange seller was founded!')
        break
    else:
        search_deque += graph[friend]
        reapet_test[friend] = True
else:
    print('the orange seller is not exist in your friends-web')


# ----------------------------------------------------------------------------------------------------------------------

