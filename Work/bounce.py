# bounce.py
#
# Exercise 1.5


def bounce(ht,bounce_back):
    for i in range(10):
        ht = round(ht*bounce_back,4)
        print(f'{i+1} {ht}')
        print('{0:} {1:}'.format(i+1,ht))

if __name__ == '__main__':
    bounce(100,3/5)
