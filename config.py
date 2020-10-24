import os
file = '~/.gitconfig'
os.mknod(file, 0777)
f = open(file, 'w')
f.write('[credential]\n	helper = store')
f.close()


file = '~/.git-credentials'
os.mknod(file, 0777)
f = open(file, 'w')
f.write('https:username:password@github.com')
f.close()
