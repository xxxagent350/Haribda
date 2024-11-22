def Str_in_List2(Str):
    List = []
    Str_ = ''
    for i in Str:
        if i == ','and i != '[' and i != ']':
            try:
                List += [int(Str_)]
            except:
                List += [Str_]
            Str_ = ''
        elif i == ']':
            try:
                List += [int(Str_)]
            except:
                List += [Str_]
            Str_ = ''
        elif i != '[':
            Str_ += i

    return List
def Str_in_List(Str):
    if Str != '':
        List = []
        Str_ = ''
        for i in Str:
            if i == '-' :
                try:
                    List += [int(Str_)]
                except:

                    if Str_[0] == '[' and Str_[-1] == ']':
                        List += [Str_in_List2(Str_)]
                    else:
                        List += [Str_]
                Str_ = ''
            else:
                Str_ += i
        return List
    else:
        return []


def List_in_Str(List):
    Str = ''
    buf_List_in_Str_1 = len(List)
    for i in range(buf_List_in_Str_1):
        Str += str(List[i])
        Str += "-"
    return Str