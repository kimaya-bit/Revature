from test import fib , next_collatz_element
def test_fib1():
    assert fib(0)==0
    assert fib(1)==1
def test_fib2(): 
    assert fib(2)==2
def test_fib3():
    assert fib(3)==3
def test_collatz_1():
    assert next_collatz_element(1)==4
def test_collatz_2():
    assert next_collatz_element(5)==5        
    
    

