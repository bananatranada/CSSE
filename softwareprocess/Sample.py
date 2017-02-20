import math
class Sample(object):

# outward facing methods
    def __init__(self, n=None):
        functionName = "Sample.__init__: "
        if(n == None):
            raise ValueError(functionName + "invalid n")
        if(not(isinstance(n, int))):
            raise ValueError(functionName + "invalid n")
        if((n < 2) or (n >= 30)):
            raise ValueError(functionName + "invalid n")
        self.n = n

    def getN(self):
        return self.n

    
    def p(self, t=None, tails=1):
        functionName = "Sample.p: "
        if(t == None):
            raise ValueError(functionName + "missing t")
        if(not(isinstance(t, float))):
            raise ValueError(functionName + "invalid t")
        if(t < 0.0):
            raise ValueError(functionName + "invalid t")
        
        if(not(isinstance(tails, int))):
            raise ValueError(functionName + "invalid tails")
        if((tails != 1) & (tails != 2)):
            raise ValueError(functionName + "invalid tails")
        
        constant = self.calculateConstant(self.n)
        integration = self.integrate(0, t, self.n, self.f) # where are high and low bounds?
        if(tails == 1):
            result = constant * integration + 0.5
        else:
            result = constant * integration * 2
            
        if(result > 1.0):
            raise ValueError(functionName + "result > 1.0")
        
        return result
        
# internal methods
    def gamma(self, x):
        if(x == 1):
            return 1
        if(x == 0.5):
            return math.sqrt(math.pi)
        return (x - 1) * self.gamma(x - 1)
    
    def calculateConstant(self, n):
        n = float(n)
        numerator = self.gamma((n + 1.0) / 2.0)
        denominator = self.gamma(n / 2.0) * math.sqrt(n * math.pi)
        result = numerator / denominator
        return result
    
    def f(self, u, n):
        n = float(n)
        base = (1 + (u ** 2) / n)
        exponent = -(n + 1.0) / 2
        result = base ** exponent
        return result
    
    def integrate(self, lowBound, highBound, n, f):
        # if (n % 2 != 0):
        #     raise ValueError("n must be even")

        epsilon = 0.001
        simpsonOld = 0.0
        simpsonNew = epsilon
        s = 4.0
        while (abs((simpsonNew - simpsonOld) / simpsonNew) > epsilon):
            print(simpsonNew)
            simpsonOld = simpsonNew
            w = (highBound - lowBound) * 1.0 / s
            simpsonNew = f(lowBound, n) + f(highBound, n)
            # i = 1
            # while (i < highBound):
            #     print(i)
            #     if i % 2 == 0:
            #         simpsonNew = simpsonNew + 2 * f(i * s, n) #wrong
            #     else:
            #         simpsonNew = simpsonNew + 4 * f(i * s, n)
            #     i += 1
            #     print('new i')
            print(range(1, highBound))
            for i in range(1, highBound):
                print(i)
                if i % 2 == 0:
                    simpsonNew = simpsonNew + 2 * f(i * s, n) #wrong
                else:
                    simpsonNew = simpsonNew + 4 * f(i * s, n)
            # simpsonNew *= (w / 3.0)
            print(abs((simpsonNew - simpsonOld) / simpsonNew))
            s *= 2

        return simpsonNew
        
        
    
        
            
        
