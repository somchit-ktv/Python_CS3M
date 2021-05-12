"""
join ແມ່ນການເອົາຂໍ້ມູນຕັ້ງແຕ່ 2 set ມາລວມກັນ, ຄືກັນກັບການ join ໃນ SQL ເຊີ່ງສາມາດເຮັດໄດ້ຫຼາຍຮູບແບບ ຄື:
1. union
2. intersection
3. difference

"""

# 1. union ມີການເຮັດວຽກຄ້າຍຄືຄຳສັ່ງ update ຄືຈະທຳການລວມສະມາຊິກທັງໝົດຂອງ 2 set ເຂົ້າກັນໃຫ້ເປັນ set ດຽວ

setUnion1 = {"John", "Chiele", "Mike", "Kole", "Doley"}
setUnion2 = {"Jame", "Soney", "Wincer", "Bicole", "Dante"}

# ສ້າງ set ໃໝ່ຂື້ນມາເພື່ອໃຊ້ເກັບສະມາຊິກທີ່ທຳການ union ກັນແລ້ວຂອງ 2 set
setJoin = setUnion1.union(setUnion2)
print("ແບບໃຊ້ union => ", setJoin)


# 2. intersection ຈະທຳການລວມເອົາສະມາຊິກທີ່ຄືກັນຂອງ 2 set
setInter1 = {"mango", "watermalon", "kiwi", "apple", "strawberry"}
setInter2 = {"apple", "strawberry", "orange", "cherry", "banana"}

# ກຳນົດໂຕແປໃໝ່ເພື່ອເກັບເອົາຄ່າສະມາຊິກທີ່ຄືກັນຂອງ setInter1 ຕໍ່ກັບ setInter2
setJoin2 = setInter1.intersection(setInter2)
print("ແບບໃຊ້ intersection => ", setJoin2)

# ຫຼື ຖ້າບໍ່ຢາກສ້າງໂຕແປໃໝ່ກໍ່ສາມາດໃຊ້ intersection_update ກໍ່ໄດ້
setInter1.intersection_update(setInter2)
print("ແບບໃຊ້ intersection_update => ", setInter1)


# 3. difference ຈະທຳການລວມເອົາສະມາຊິກທີ່ແຕກຕ່າງກັນຂອງ 2 set 
setDiff1 = {"mango", "watermalon", "kiwi", "apple", "strawberry"}
setDiff2 = {"apple", "strawberry", "orange", "cherry", "banana"}

# ກຳນົດໂຕແປໃໝ່ເພື່ອເກັບເອົາຄ່າສະມາຊິກທີ່ແຕກຕ່າງກັນຂອງ setDiff1 ຕໍ່ກັບ setDiff2
setJoin3 = setDiff1.difference(setDiff2)
print("ແບບໃຊ້ difference => ", setJoin3)

# ຫຼື ຖ້າບໍ່ຢາກສ້າງໂຕແປໃໝ່ກໍ່ສາມາດໃຊ້ difference_update ກໍ່ໄດ້
setDiff1.difference_update(setDiff2)
print("ແບບໃຊ້ difference_update => ", setDiff1)
