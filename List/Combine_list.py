'''
ການລວມຂໍ້ມູນໃນ List ມີ 2 ວິທີຄື:
1. ສາມາດເຮັດໄດ້ງ່າຍໆ ໂດຍການໃຊ້ເຄື່ອງໝາຍ + ຫຼື ເອີ້ນວ່າ concatenate
2. ໃຊ້ .extend
'''

# List ດັ້ງເດີມ
phone = ["Samsung","Apple","Huawei","Nokia","Oppo","Realme","Vivo","Xiaomi"]
name = ["John", "Chiele", "Mike", "Kole", "Doley"]

# ເອົາ List ທີ່ຕ້ອງການມາລວມກັນ ໂດຍຈະຕ້ອງກຳນົດໂຕແປເພື່ອຮອງຮັບ
allgroub = phone + name
print("ລວມດ້ວຍການ + : \n",allgroub)      # ສະແດງສະມາຊິກທັງໝົດຫຼັງຈາກລວມກັນແລ້ວ

# ລວມດ້ວຍການໃຊ້ .extend
phone.extend(name)                      # ໂຕແປ phone ລວມເອົາສະມາຊິກຂອງ ໂຕແປ name ມາໄວ້ໃນໂຕຂອງມັນ
print("ລວມດ້ວຍ extend : \n", phone)      # ສະແດງສະມາຊິກໃນ phone ຫຼັງຈາກລວມກັນກັບ name ແລ້ວ

  