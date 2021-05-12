# ການເພີ່ມສະມາຊິກເຂົ້າໄປໃນ set ເຮັດໄດ້ໂດຍການໃຊ້ຄຳສັ່ງ .add()

name = {"John", "Chiele", "Mike", "Kole", "Doley"}
name.add("Jame")    # ເພີ່ມສະມາຊິກ Jame ເຂົ້າໄປໃນ set

print(name)         # ສະແດງສະມາຊິກ name ຫຼັງການເພີ່ມ 

# ການເພີ່ມສະມາຊິກດ້ວຍ add ແມ່ນບໍ່ສາມາດເພີ່ມແບບຫຼາຍໂຕໄດ້
# name.add("Wick", "Kanh")   
# ຜົນລັບກໍ່ຈະບອກວ່າ TypeError: set.add() takes exactly one argument (2 given) 

"""
ໃນກໍລະນີຕ້ອງການເພີ່ມຫຼາຍສະມາຊິກເຂົ້າໄປໃນ set 
ແມ່ນຕ້ອງໄດ່ສ້າງ list ເພື່ອມາເກັບຄ່າສະມາຊິກໃໝ່ທີ່ຈະເພີ່ມ
ຫຼັງຈາກນັ້ນໃຊ້ຄຳສັ່ງ update ໄປທີ່ set
"""
list_set = ["Wick", "Kanh"]
name.update(list_set)

# ຫຼື ສາມາດເຮັດແບບເພີ່ມເຂົ້າໄປໂດຍກົງໂດຍບໍ່ສ້າງໂຕແປ list ກໍ່ໄດ້
name.update(["Wick", "Kanh"])

print("Updated set = ", name)