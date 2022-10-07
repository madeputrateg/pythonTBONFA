def start(kata):
    F={"4"}
    state=set(["0"])
    newstate=set([])
    for i in kata:
        for z in state:
            match z:
                case "0":
                    newstate.add("1")
                case "1":
                    newstate.add("2")
                    if i=="0":
                        newstate.add("3")
                case "2":
                    newstate.add("0")
                case "3":
                    if i=="0":
                        newstate.add("4")
                case "4":
                    pass
        state=newstate
        newstate=set([])
    for z in state:
        if z in F:
            print("diterima")
            return
    print("tidak diterima")
