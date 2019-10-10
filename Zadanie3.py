from datetime import datetime

print('rózne formatowania z tamtej stronki : ')
print('{:+d}'.format(42))

print('{:06.2f}'.format(3.141592653589793))

print('{:%Y-%m-%d %H:%M}'.format(datetime(2019, 10, 10, 12, 20)))

print('{:{align}{width}}'.format('test', align='^', width='20'))

print('{:{width}.{prec}f}'.format(2.7182, width=15, prec=3))
