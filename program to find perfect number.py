#w.a.p.t find the given number is perfect number or not

n=6
diviser_summ=0
for i in range(1,n//2+1):
    if n%i==0:
        diviser_summ+=i
if diviser_summ==n:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')

'''
iteration
1.controller will take 1 and check whether 6%1 will give 0 or not.6%1 will give 0
  so condition satisfies and diviser_summ will be added with 1 and store the added
  value in diviser_summ
2.it will take 2 and check whether 6%2 will give 0 or not.6%2 will give 0 so condition
  satisfies and diviser_summ will be added with 2 and store the added value in
  diviser_summ
3.it will take 3 and check whether 6%3 will give 0 or not.6%3 will give 0 so condition
  satisfies and diviser_summ will be added with 3 and store the added value in
  diviser_summ
4.after iteration controller will check if 6 is equal to diviser_summ or not.If it
  is true it will print perfect number,else it will print not perfect number

'''



  
