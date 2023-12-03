# Task : Name of Functions
# Elements : Elements of Data elements
def filterX(Task,Elements):
    Result=[]
    for no in Elements:
        if(Task(no)==True):
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result=[]
    for no in Elements:
        Ret=(Task(no))
        Result.append(Ret)
    return Result

def reduceX(Task,Elements):
    Sum=0
    for no in Elements:
        Sum=Task(Sum,no)
    return Sum