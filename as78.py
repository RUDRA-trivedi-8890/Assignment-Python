class Solution:
    def decodar(self,num):
        d={}
        for i in range(65,91,1):
            d[i-64] = chr(i)
        #print(d)
        self.x=num
        while(num>0):
            r=num%10
            num//=10
            if(r==0):
                r=10
            s=""
            #print(r)
            print(d[r])
            s=d[r]
            r="".join(s)
        while(self.x>0):
            r=self.x%100
           #print(r)
            self.x//=100
            m=""
            print(d[r])
            m=d[r]
            k="".join(m)
        print("decodes msgs are",r,"and",k)
s=Solution()
s.decodar(11106)