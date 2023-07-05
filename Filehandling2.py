"""class FileRead:
    def main():
        a=open("sample.txt","r")
        print(a.read())
    def main_2():
        d=str(input("Enter a file name"))
        b=open(d,"w")
        c=str(input("Enter the content"))
        b.write(c)
        print("File Created Successfully")
        b.close()
FileRead.main()
FileRead.main_2()"""
import os 
class FileHandling:
    def main():
        x=str(input("Enter a file name"))
        y=str(input("Enter a text in the file"))
        b=open(x,"w")
        b.write(y)
        b.close()
        print(x,"\nFile created successfully")
        print("\n\t\t----Reading File Contents----")
        z=open(x,"r")
        print("\n")
        print(z.read())
    def FileDelete():
        xyz=str(input("Enter the file name to delete:"))
        os.remove(xyz)
FileHandling.main()
FileHandling.FileDelete()


