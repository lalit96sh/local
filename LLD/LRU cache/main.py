from LRUCache import LRUCache

cache = LRUCache()

print("\tSET: S,\n\tGET: G\n\tPRINT: P")
while True:
    v = input("Press : ")
    if v=="s":
        key = input("key : ")
        value = input("value : ")
        cache.set(key=key,value=value)
    elif v=="g":
        key = input("key : ")
        ans = cache.get(key)
        print("ans : {}".format(ans))
    elif v=="p":
        cache.print_cache()
    else:
        break
    