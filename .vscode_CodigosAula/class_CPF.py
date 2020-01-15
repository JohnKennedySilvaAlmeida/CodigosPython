class cpf: #obs! import
    
    @staticmethod
    def validar(cpf):
        res = True  
        
        if len(cpf) != 11:
            print('Error'.center(100))
            res = False
               
        elif cpf in [s * 11 for s in [str(n) for n in range(10)]]:
            res = False     

        return res

        '''calc = [i for i in range(1, 10)]
        d1= (sum([int(a)*b for a,b in zip(cpf[:-2], calc)]) % 11) % 10
        d2= (sum([int(a)*b for a,b in zip(reversed(cpf[:-2]), calc)]) % 11) % 10
        return str(d1) == cpf[-2] and str(d2) == cpf[-1]

        # cpf = valor '''