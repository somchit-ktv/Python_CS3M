# ການຄັດລອກ list ແມ່ນການ copy ເອົາສະມາຊິກທັງໝົດຂອງ list ໜື່ງ ມາໄວ້ອີກ list ໜື່ງ

# list ຕັ້ງຕົ້ນ
phone = ["Samsung","Apple","Huawei","Nokia","Oppo","Realme","Vivo","Xiaomi"]

x = []              # x ເປັນໂຕແປທີ່ຈະໃຊ້ໃນການຄັດລອກຂໍ້ມູນສະມາຊິກທັງໝົດຂອງ phone ມາໃສ່
print("ກ່ອນຄັດລອກ : \n", x)

x = phone.copy()    # ໃຊ້ .copy ເພື່ອຄັດລອກ
print("ຫຼັງຄັດລອກ : \n", x)