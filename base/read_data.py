import yaml
def read_data(testcasenum,filename):
    with open("../data/"+filename,"r",encoding="utf-8") as f:
        data=yaml.load(f, Loader=yaml.FullLoader)
        data2=data[testcasenum]
        list_data=list()
        for ele in data2.values():
            list_data.append(ele["search"])
        return list_data