d = 17
monthes = ['January','February','March','April','May','June','July','August','September','October','November','December']
m = 2
mn = monthes[m-1]
y = 2009
yd = 4
s = '/'
print('1: {1:0>2d}{3}{0:0>2d}{3}{2}'.format(d,m,y,s))
print('2: {0:0>2d}{3}{1:0>2d}{3}{2}'.format(d,m,y,s))
print('3: {2}{3}{1:0>2d}{3}{0:0>2d}'.format(d,m,y,s))
print('4: {1} {0}, {2}'.format(d,mn,y))
print('5: {1}{3}{0}{3}{2}'.format(d,m,y,s))
print('6: {0}{3}{1}{3}{2}'.format(d,m,y,s))
print('7: {2}{3}{1}{3}{0}'.format(d,m,y,s))
print('8: {1: >2d}{3}{0: >2d}{3}{2}'.format(d,m,y,s))
print('9: {0: >2d}{3}{1: >2d}{3}{2}'.format(d,m,y,s))
print('A: {2}{3}{1: >2d}{3}{0: >2d}'.format(d,m,y,s))
print('B: {1:0>2d}{0:0>2d}{2}'.format(d,m,y))
print('C: {0:0>2d}{1:0>2d}{2}'.format(d,m,y))
print('D: {2}{1:0>2d}{0:0>2d}'.format(d,m,y))
print('E: {1:3s}{0:0>2d}{2}'.format(d,mn,y))
print('F: {0:0>2d}{1:3s}{2}'.format(d,mn,y))
print('G: {2}{1:3s}{0:0>2d}'.format(d,mn,y))
print('J: {0} {1}, {2}'.format(d,mn,y))
print('K: {2}, {1:3s} {0}'.format(d,mn,y))
print('L: {1:3s} {0:0>2d}, {2}'.format(d,mn,y))
print('M: {0:0>2d}, {1:3s} {2}'.format(d,mn,y))
print('N: {2}, {1:3s} {0:0>2d}'.format(d,mn,y))
print('L: {1:3s} {0:0>2d}, {2}'.format(d,mn,y))
print('P: {0:0>2d}, {1:3s} {2}'.format(d,mn,y))
print('Q: {2}, {1:3s} {0:0>2d}'.format(d,mn,y))


