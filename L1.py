def start(kata):
    F={"4"}
    state=set(["0"])
    newstate=set([])
    for i in kata:
        for z in state:
            match z:
                case "0":
                    if i=="1":
                        newstate.add("1")
                case "1":
                    if i=="0":
                        newstate.add("2")
                case "2":
                    if i=="1":
                        newstate.add("3")
                case "3":
                    newstate.add("4")
                case "4":
                    newstate.add("3")
        state=newstate
        newstate=set([])
    for z in state:
        if z in F:
            print("diterima")
            return
    print("tidak diterima")

