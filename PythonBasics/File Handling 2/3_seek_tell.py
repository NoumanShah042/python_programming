"""

tell()  -  return current position of file pointer
seek() -   reset the position of file pointer

***************************************************************

tell()
It returns an integer giving the file pointer current position in the file represented as a number
of bytes. File Pointer/File Handler is like a cursor, which defines from where the data has to be read
or written in the file. Sometimes it becomes important for us to know the position of the File Pointer.
With the help of tell(), this task can be performed easily

Syntax:  tell()
Parameters Required: No parameters are required.
Return Value:  tell() function returns the current position of the file pointer within the file.

*****************************************************************

seek():
When we open a file, the system points to the beginning of the file. Any read or write will happen from
the start. To change the file object’s position, use seek(offset, whence) function. The position will compute
by adding offset to a reference point, and the whence argument selects the reference point. It is useful
when operating over an open file. If we want to read the file but skip the first 5 bytes, open the file,
use function seek(5) to move to where you want to start reading, and then continue reading the file.

Description:
Syntax:  file_pointer .seek(offset, whence).
Offset:  In seek() function, offset is required. Offset is the position of the read/write pointer within the file.
Whence: This is optional. It defines the point of reference. The default is 0, which means absolute file positioning.

Value   Meaning
0   Absolute file positioning. The position is relative to the start of the file. The first argument cannot be negative.
1   Seek relative to the current position.The first argument can be negative to move backward or positive to move forward
2   Seek relative to the file’s end. The first argument must be negative.


"""

f = open("C:\\Users\\Syed Numan Rehman\\Desktop\\test.txt")
f.seek(0)

print(f.tell())
print(f.readline(), end="")
print(f.tell())              # the file pointer updated after read operation

print(f.readline(), end="")
print(f.tell())
f.close()

