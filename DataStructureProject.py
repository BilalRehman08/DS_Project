#!/usr/bin/env python
# coding: utf-8

# In[41]:


import random 
class SkipNode: 
    def __init__(self, item, layer): 
        self.item = item 
        self.next = [None]*(layer+1) 

class SkipList: 
    def __init__(self, maximum_layers, div): 
        self.maximum_layers = maximum_layers 
        self.div = div 
        self.head = self.Create(self.maximum_layers, -1) 
        self.lyrs = 0
   
    def Create(self, lyr, item): 
        n = SkipNode(item, lyr) 
        return n 

    def Random_Layer(self): 
        lyr = 0
        while random.random()<self.div and  lyr<self.maximum_layers:
            lyr += 1
        return lyr
    
    def Input(self,item):
        self.update = [None]*(self.maximum_layers+1) 
        current = self.head 
        for i in range(self.lyrs, -1, -1): 
            while current.next[i] and current.next[i].item < item: 
                current = current.next[i] 
            self.update[i] = current 
        self.current = current.next[0] 
    
    def Insertion(self, item): 
        a=self.Input(item)
        if self.current == None or self.current.item != item: 
            layer = self.Random_Layer() 
            if layer > self.lyrs: 
                for i in range(self.lyrs+1, layer+1): 
                    self.update[i] = self.head 
                self.lyrs = layer 
            n = self.Create(layer, item) 
            for i in range(layer+1): 
                n.next[i] = self.update[i].next[i] 
                self.update[i].next[i] = n 
             
    def Deletion(self, item): 
        a=self.Input(item)
        if self.current != None and self.current.item == item: 
            for i in range(self.lyrs+1): 
                if self.update[i].next[i] != self.current: 
                    break
                self.update[i].next[i] = self.current.next[i] 
            while(self.lyrs>0 and self.head.next[self.lyrs] == None): 
                self.lyrs -= 1 
          
    def Searching(self, item): 
        print("\n******Searched Element******")
        current = self.head 
        for i in range(self.lyrs, -1, -1): 
            while(current.next[i] and current.next[i].item < item): 
                current = current.next[i] 
        current = current.next[0] 
        if current and current.item == item: 
            print("Searched :", item)
        else:
            print("Element not found")
  
    def Print(self): 
        print("\n******Layers******") 
        head = self.head 
        for lyr in range(self.lyrs+1): 
            print("Layers ",lyr,":", end=" ") 
            SkipNode = head.next[lyr] 
            while(SkipNode != None): 
                print(SkipNode.item, end=" ") 
                SkipNode = SkipNode.next[lyr] 
            print("")
            
obj = SkipList(3, 0.5) 
print("---------> Before Delete")
obj.Insertion(9) 
obj.Insertion(2) 
obj.Insertion(4) 
obj.Insertion(1) 
obj.Insertion(10)
obj.Insertion(8)
obj.Insertion(3) 
obj.Insertion(4) 
obj.Insertion(15) 
obj.Insertion(0) 
obj.Insertion(7)
obj.Insertion(19)
obj.Print()  
print("")
print("---------> After Delete")
obj.Deletion(4) 
obj.Deletion(9)
obj.Deletion(3)
obj.Deletion(0)
obj.Print() 
obj.Searching(2)
obj.Searching(0)


# In[ ]:




