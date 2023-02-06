


#Programı 1 kere çalıştırıp durdurduktan sonra CreatFile() fonskyionunu 28. satırdaki Yorum satırına alınız.
#Dosya Oluşturuyoruz
def creat_file():
        student_information_file= open("Studentİnformation.txt", "x")
            
#Öğrenci Bilgilerini Alıp Değişkenlere Atadık
def student_information():
    student_name = input("Student Name: ")
    student_surname = input("Student Surname: ")
    student_age = input("Student Age: ")
    student_Email = input("Student E-Mail: ")

# Girilen Bilgileri Dosyaya Kaydet

    student_information_file = open("Studentİnformation.txt", "a")
    student_information_file.write("------------------------------------------\n")
    student_information_file.write("Student Name: " + student_name + "\n")
    student_information_file.write("Student Surname: " + student_surname + "\n")
    student_information_file.write("Student Age: " + student_age + "\n")
    student_information_file.write("Student E-Mail: " + student_Email + "\n")
    student_information_file.write("------------------------------------------\n")
    student_information_file.close()

def transactions():
    creat_file()
    while True:
        selection = int(input("Menu\n1)Add New Student\n2)Show All Student İnformations\n3)Exit\n Your Selection: "))
    
        if selection == 1:
            student_information()
        elif selection == 2:
            student_information_file = open("Studentİnformation.txt","r",encoding="utf-8")
            read = student_information_file.read()
            print(read)
            student_information_file.close()
        elif selection == 3:
            break
        else:
            print("Wrong enter elements.Try Again")
        continue

transactions()