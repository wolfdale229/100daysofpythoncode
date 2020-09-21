from collections import deque

def search(name):
    search_queue = deque()
    graph = {name:''}
    search_queue += graph[name]
    searched = []
    
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def person_is_seller(name):
    return name[-1] == 'u'

search('you')
