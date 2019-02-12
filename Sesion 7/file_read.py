# example of reading a file

name = 'mynotes.txt'

# open the file
myfile = open(name,'r')

print('File opened: {}'.format(myfile.name))

contents = myfile.read()

print('The file contents are: {}:'.format(contents))