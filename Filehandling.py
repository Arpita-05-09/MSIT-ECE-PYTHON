class FileRead:
    def main():
        a=open("sample.txt","r")
        print(a.read())
    def main_2():
        b=open("text.txt","w")
        b.write("Google")
        print("File Created Successfully")
        b.close()
FileRead.main()
FileRead.main_2()