def start(kata):
    F={"6"}
    state=set(["0"])
    newstate=set([])
    for i in kata:
        for z in state:
            match z:
                case "0":
                    newstate.add("1")
                case "1":
                    newstate.add("2")
                case "2":
                    newstate.add("3")
                case "3":
                    newstate.add("1")
                    newstate.add("4")
                case "4":
                    if i=="0":
                        newstate.add("5")
                case "5":
                    if i=="0":
                        newstate.add("6")
                case "6":
                    pass
        state=newstate
        newstate=set([])
    for z in state:
        if z in F:
            print("diterima")
            return
    print("tidak diterima")