import time
print("--------------------------------------------------")
#Selamat datang kepada pengguna
print("Selamat datang ke Laman Kuiz Pendidikan Islam Tingkatan 1 !")
time.sleep(1)
print("--------------------------------------------------")

#Chances
chances=1
print("Anda perlu pilih", chances,"jawapan betul.\nAnda akan dapat 1 skor jika jawapan betul.\n")
time.sleep(2)

#score
score=0

#soalan 1
print("==================================================")
question_1=print("1) IBADAH TERBAHAGI KEPADA....?\n(A) 2 \n(B) 3 \n(C) 4 \n(D) 1 \n\n")
answer_1= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_1, "\n\n")

time.sleep(2)

#soalan 2
print("==================================================")
question_2 = print("2)BERAPAKAH JENIS HUKUM YANG ADA DALAM ISLAM?\n(A) 4\n(B) 6\n(C) 5\n(D) 2\n\n")  
answer_2 = "c"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_2):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n ")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_2, "\n\n")

time.sleep(2)

#soalan 3
print("==================================================")
question_3 = print("3)APAKAH JENIS HUKUM MENDAPAT PAHALA JIKA DILAKUKAN DAN TIDAK BERDOSA JIKA DI TINGGALKAN? \n(A) haram \n(B) wajib\n(C) makruh\n(D) sunat\n\n")
answer_3 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_3, "\n\n")

time.sleep(2)

#soalan 4
print("==================================================")
question_4 =print("4)APAKAH HUKUM MANDI WAKTU PAGI??\n(A) Harus\n(B) Sunat\n(C) Wajib\n(D) Haram\n\n")
answer_4= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS",answer_4, "\n\n")

time.sleep(1)

#soalan 5
print("==================================================")
question_5 =print("5)  MEMBACA AYAT QURSI SEBELUM TIDUR HUKUMNYA ADALAH....\n(A) Wajib\n(B) Sunat\n(C) Harus\n(D) Makruh\n\n")
answer_5= "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_5, "\n\n")

time.sleep(2)

#soalan 6
print ("=================================================")
question_6 =print ("6) APAKAH HUKUM BERSEDEKAH?....\n (A) WajiB \n (B) Sunat \n (C) Harus \n (D)Haram \n\n")
answer_6="b"

for i in range (chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_6):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_6, "\n\n")

time.sleep (2)


#print the score
print("==================================================")
while score >=2:
    print("Tahniah! Skor anda ialah", score,)
    break

while score <2:
    print ("Moga berjaya di lain masa! Skor anda ialah",score)
    break

#Goobye message
print("Terima kasih kerana menyertai kuiz ini jumpa lagiii!")
  