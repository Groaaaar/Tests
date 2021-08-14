def solver(base):
    output=[0,0]
    output[0] = base*2
    if((base-1)%3)==0:
        output[1]=(base-1)/3
    return output

class inv_conj_gen():
    def __init__(self):
        self.level=0
        self.tries={1:[]}

    def add_level(self):
        temp_list = list(self.tries.keys())
        for i in temp_list:
            item = solver(i)
            if item[0] not in self.tries.keys():
                self.tries[int(item[0])]=list(self.tries[i])
                self.tries[int(item[0])].append(i)

            if (item[1] not in self.tries.keys()) and (item[1] != 0):
                self.tries[int(item[1])] = list(self.tries[i])
                self.tries[int(item[1])].append(i)
        self.level+=1
    def add_n_levels(self,n):
        while n>0:
            n=n-1
            self.add_level()
    def print_complexity(self):
        out = list(self.tries.values())
        out=list(map(len,out))
        return out

    def max_consecutive(self):
        for i in range(1,len(self.tries)+2):
            if i not in self.tries.keys():
                return i-1



tester = inv_conj_gen()
out = []
dico_size = 0
for i in range(64):
    dico_size = len(tester.tries)
    tester.add_level()
    print ("niveau {}: {}. Taille du dico: {}. Ajouts dans dico : {} ou {}%".
           format(i,tester.max_consecutive(),len(tester.tries),len(tester.tries)-dico_size,
                  100*(len(tester.tries)-dico_size)/len(tester.tries)))
