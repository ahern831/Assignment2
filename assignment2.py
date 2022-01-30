import socket
import sys

class Assignment2:
    
    # Task 1
    def __init__ (self, year):
        self.year = year 

    # Task 2
    def tellAge(self, currentYear):
        self.currentYear = currentYear
        print ("Your age is ", currentYear - self.year)
    
    # Task 3
    def listAnniversaries(self):
        a = []
        p = 10
        m = self.year + 10
        while m <= self.currentYear:
            a.append(p)
            p = p + 10
            m = m + 10
        return a
        
    # Task 4
    def modifyYear(self, n):
        
        year1 = str(self.year)[:2]
        year2 = str(self.year)[-2:]
            
        result1 = ""
        result2 = ""
        
        for i in range(n):
            result1 += year1
            
        result2 = self.year * n
        result2 = str(result2)[:2]
        result2 = int(result2) + 1
            
        result = str(result1) + str(result2)
        return result
        
    # Task 5
    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False
    
        if string[0].islower() == False:
            return False
    
        # Initialize the count to 0
        _num_count = 0  
        for i in string:
            if i.isdigit():
                _num_count += 1  
    
            # If the count of numbers is greater than 1 
            #return False
            if _num_count > 1:
                return False
                
        return True
    
    def connectTcp(self, host, port):
        self.host = host
        self.port = port
        A = False
        try:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
        except socket.error as Err:
            print('Socket creation failed.')
            
        try:
            host_ip = socket.gethostbyname(self.host)
        except socket.gaierror:
            return A
            
        soc.connect((host_ip, self.port))
        A = True
        return A
        
        
#Task 1
a = Assignment2 (1990) 

#Task 2
a.tellAge(2022)
print("\n")

#Task 3
ret = a.listAnniversaries()
print(ret)
print("\n")

#Task 4
ret1 = a.modifyYear(3)
print(ret1)
print("\n")

#Task 5
ret2 = a.checkGoodString("f1obar0more")
print(ret2)
ret2 = a.checkGoodString("foobar0more")
print(ret2)
print("\n")

#Task 6
retval = a.connectTcp('www.google.com', 80)
print(retval)
if retval:
    print("Connection established correctly")
else:
    print("Some error")

