# ຕົວຢ່າງ 2: ຊອກຫາຄ່າຫຼາຍສຸດ, ໜ້ອຍສຸດ ແລະ ຜົນລວມຂອງຕົວເລກທີ່ປ້ອນເຂົ້າ

number=[]                               # ສ້າງ list ເປົ່າຂື້ນມາໄວ້ເກັບຂໍ້ມູນ
while True:                             # ທຳການວົນຮອບເມື່ອເງື່ອນໄຂຖືກຕ້ອງ
    x=int(input("ປ້ອນຕົວເລກຂອງທ່ານ :"))    # ຮັບຂໍ້ມູນຈາກແປ້ນພິມໂດຍຂໍ້ມູນຈະແປງເປັນ integer
    if x<0:                             # ຖ້າຫາກປ້ອນຄ່າທີ່ຕ່ຳກວ່າ 0
        break                           # ຢຸດການທຳງານຂອງ loop
    number.append(x)                    # ໃຫ້ທຳການຮັບຕົວເລກທີ່ປ້ອນເຂົ້າມາເພື່ອໃສ່ຕຳແໜ່ງສຸດທ້າຍຂອງ list 

print(number)                           # ສະແດງຕົວເລກທີ່ປ້ອນເຂົ້າມາ
print("ຄ່າທີ່ຫຼາຍທີ່ສຸດ",max(number))          # ສະແດງຕົວເລກທີ່ຫຼາຍທີ່ສຸດໂດຍໃຊ້ ຟັງຊັນ max
print("ຄ່າທີ່ໜ້ອຍທີ່ສຸດ",min(number))         # ສະແດງຕົວເລກທີ່ໜ້ອຍທີ່ສຸດໂດຍໃຊ້ ຟັງຊັນ min
print("ຜົນລວມ",sum(number))              # ສະແດງຜົນລວມຂອງຕົວເລກທີ່ປ້ອນເຂົ້າມາໂດຍໃຊ້ ຟັງຊັນ sum