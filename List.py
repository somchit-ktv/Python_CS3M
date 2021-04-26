# primitive variable
a = 1
a1 = 2
a2 = 3
# .
# .
# .

# non-primitive variable : list
number = [] #list empty
number = [1,2,3,4,5]
name = ["John", "Chiele", "Mike", "Kole", "Doley"]
etc = [1,"Max",3.25,True,-20]

# constructure ແມ່ນການສ້າງຮູບແບບຂອງຂໍ້ມູນ
name = list(["John", "Chiele", "Mike", "Kole", "Doley"])

# ການເຂົ້າເຖິງຂໍ້ມູນແມ່ນຈະເຂົ້າໄປຕາມຕຳແໜ່ງ index ຂອງ list ແຕ່ລະຕຳແໜ່ງທີ່ເຮົາຕ້ອງການ
# print(number[4]+number[1])

# ການເຂົ້າເຖິງຂໍ້ມູນແບບກຳນົດຊ່ວງແມ່ນຈະໃຊ້ :
# print(name[2:4])

# ການແກ້ໄຂຂໍ້ມູນ
# ຊື່ໂຕແປ [index] = ຂໍ້ມູນທີ່ແກ້ໄຂ
# print("ກ່ອນແກ້ໄຂ : ", name)
# name[2] = "Luvs"
# print("ຫຼັງແກ້ໄຂ : ", name)

# loop ຈະເຮັດວຽກຈົນກວ່າຈະກວດສອບສະມາຊິກທຸກໂຕຄົບ
# for i in name:
#     print(i)

# ກວດສອບຂໍ້ມູນ ວ່າສີ່ງທີ່ເຮົາຕ້ອງການກວດສອບນັ້ນເປັນສະມາຊິກໃນ list ຫຼື ບໍ່ ໂດຍໃຊ້ if...in
# if 5 in number:
#     print("Yes")
# else:
#     print("No")

# ນັບຈຳນວນສະມາຊິກໃນ list ໃຊ້ len
print(len(name))




