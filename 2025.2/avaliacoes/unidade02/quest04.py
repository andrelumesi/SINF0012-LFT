from abc import abstractmethod
from abc import ABCMeta

'''
Definicao de excmd
'''
class Excmd(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExcmdCircunflexo(Excmd):
    def __init__(self, excmdesq, excmddir):
        self.excmdesq = excmdesq
        self.excmddir = excmddir
    def accept(self, visitor):
        return visitor.visitCompoundFunProgram(self)
    

class ExcmdShift(Excmd):
    def __init__(self, excmdesq, excmddir):
        self.excmdesq = excmdesq
        self.excmddir = excmddir
    def accept(self, visitor):
        return visitor.visitCompoundFunProgram(self)
    



class ExcmdHash(Excmd):
    def __init__(self, excmdesq, excmddir):
        self.excmdesq = excmdesq
        self.excmddir = excmddir
    def accept(self, visitor):
        return visitor.visitCompoundFunProgram(self)
    


class ExcmdNotNum(Excmd):
    def __init__(self, num):
        self.num = num
    def accept(self, visitor):
        return visitor.visitCompoundFunProgram(self)
    

class ExcmdId(Excmd):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitCompoundFunProgram(self)
    

class Excmdcall(Excmd):
    def __init__(self, id, excmd):
        self.id = id
        self.excmd = excmd
    def accept(self, visitor):
        return visitor.visitCompoundFunProgram(self)