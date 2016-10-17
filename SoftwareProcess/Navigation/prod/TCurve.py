"""
Created on September 2016
@author: Chandrashekar Chary Vadla
"""
import math
class TCurve(object):

# outward facing methods
    def __init__(self, n=None):
        functionName = "TCurve.__init__: "
        if(n == None):
            raise ValueError(functionName + "invalid n")
        if(not(isinstance(n, int))):
            raise ValueError(functionName + "invalid n")
        if((n < 2) or (n >= 30)):
            raise ValueError(functionName + "invalid n")
        self.n = n

    
    def p(self, t=None, tails=1):
        functionName = "TCurve.p: "
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
        
        constant = self. calculateConstant(self.n)
        integration = self.integrate(t, self.n, self.f)
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
    
    def integrate(self, t, n, f):
        #Given values are
        epsilon = 0.001
        simpsonOld = 0.0
        simpsonNew = epsilon
        s = 4      # 4 slices// 
        while (abs((simpsonNew - simpsonOld)/ simpsonNew) > epsilon):
            simpsonOld = simpsonNew
            #Here Lowbound is 0 and Highbound is t So,(t-0)/s means w=t/s 
            w=t/s
            f1=self.f(0,self.n)+self.f(t,self.n) #Adding lowbound and highbound//First and Last terms
            f2=0.0
            f3=0.0
            i=1.0
            #Total Terms are s+1,2 terms already added above so remaining are s-1
            s1=s-1
            while(i<=s1):
                f2+=4.0*self.f(i*w,self.n) 
                #Calculating 4*coefficients// f2 gives sum of all 4 Coefficients
                i=i+1
                if(i<=s1):
                    f3+=2.0*self.f(i*w,self.n) 
                    #Calculating 2*Coefficients// f3 gives sum of all 2 Coefficients
                    i=i+1
            simpsonNew = (f2+f3+f1)*(w/3)    
            s = s * 2
        return simpsonNew

