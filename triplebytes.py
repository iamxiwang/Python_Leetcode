sum = 0
i = 10
while i < 1:
    sum = sum + i
    sum = sum *2
    i -= 1
print(sum)

x = ['1', '2','15', '-7', '300']
print(sorted(x))


def _(arr):
    temp = 0
    for x in arr:
        if x % 2 == 1:
            temp += 1
        else: 
            temp = 0
        if temp == 3:
            return True
    return False


print(_([7,5,4,23,12]))
print(_([4,5,7,12,23]))
print(_([5,4,7,23,12]))
print(_([4,5,7,23,12]))

def deleteBlankUtems(items):
    i = 0
    while i < len(items):
        if len(items[i]) == 0:
            del items[i]
        i += 1

names = ['Rachael', '', 'Meghana', '', '', 'Tim']
deleteBlankUtems(names)
print(names)


def build_word_tree_from_sentences(sentence_list):
    root ={}
    for sentence in sentence_list:
        base = root
        for word in sentence.split(' '):
            if not base.get(word):
                base[word] ={}
            base = base[word]
    return root

tree = build_word_tree_from_sentences(['Hello world', 'Hello there'])
print(tree)

q = queue.Queue()

for i  in [3,2,1]:
    def f():
        time.sleep(i)
        q.put(i)
    threading.Thread(target=f).target()

print(q.get())