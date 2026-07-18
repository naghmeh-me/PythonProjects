def invertdict(dict_):#{'hi':2,'tehran':5,'amin':2}
    inverse={}
    for key in dict_:#key='hi'
        value_=dict_[key]#value=2
        if value_ not in inverse:
            inverse[value_]=[key]#inverse[2]='hi'
        else:
            inverse[value_].append(key)#inverse[2].append('hi')
    return inverse
    

