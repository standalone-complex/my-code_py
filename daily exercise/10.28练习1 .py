while True:
    try:
        m = {}
        string = input()
        
        for i in string:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        for key in sorted(m.keys()):
            print(str(key) + " " + str(m[key]))
        #print("")
    except:
        break