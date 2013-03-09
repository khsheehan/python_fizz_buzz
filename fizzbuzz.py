#!/usr/bin/python
print['fizz'*(x%3==0)+'buzz'*(x%5==0)+'%d'%x*(x%3*x%5!=0)for x in range(1,101)]