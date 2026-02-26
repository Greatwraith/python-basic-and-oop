# MRO (Method Resolution Order) in Multiple Inheritance
# is the order Python uses to decide which method to call

# is the order Python uses to look for a method
# starting from the child class, then moving through parent classes
# from left to right when multiple parents exist


# In multiple inheritance, Python uses MRO (left to right) to decide which method is called
class A:
    def class_a_method(self):
        return 'im the class A Method'
        
    def say_hello(self):
        return 'Hello,Da jia hao. im class A!'
        
        
class B:
    def class_b_method(self):
        return 'im the class B Method'
        
    def say_hello(self):
        return 'Hello,Da jia hao. im class B!'
        


class C(B, A):
    # Method Resolution Order (MRO):
    # for C(B, A)Python looks for methods in this order: C → B → A
    # for C(A, B)Python looks for methods in this order: C → A → B
    
    # B is checked first, then A (Method Resolution Order)
    # same way goes if C(A, B)
    pass


classA = A()
classB = B()
CallClass = C()

# help(CallClass) shows the class structure, parents, and MRO
# ⬇️ active it ⬇️
# help(CallClass)


# ....
print(CallClass.class_a_method())
print(CallClass.class_b_method())
print(CallClass.say_hello())
        
    