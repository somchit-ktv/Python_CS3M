'''
ການລົບສະມາຊິກອອກຈາກ set ສາມາດເຮັດໄດ້ 4 ແບບຄື:
1. remove ລົບສະມາຊິກທີ່ລະບຸອອກ ແຕ່ສະມາຊິກນັ້ນຈະຕ້ອງຢູ່ໃນ set ຖ້າບໍ່ມີຈະຂື້ນ Error
2. discard ລົບສະມາຊິກທີ່ລະບຸອອກ ສະມາຊິກບໍ່ຕ້ອງຢູ່ໃນ set ກໍ່ບໍ່ຂື້ນ Error
3. clear ລົບສະມາຊິກທັງໝົດໃນ set ອອກ ເຫຼືອແຕ່ set ເປົາ
4. del ລົບ set ແລະ ຄືນພື້ນທີ່ໜ່ວຍຄວາມຈຳ

'''

# set ຕັ້ງຕົ້ນ
phone = {"Samsung","Apple","Huawei","Nokia","Oppo","Realme","Vivo","Xiaomi"}
print("set ກ່ອນການລົບ :\n", phone)

# ລົບດ້ວຍຄຳສັ່ງ remove ຄືຈະຕ້ອງລະບຸວ່າສະມາຊິກໂຕໃດໃນ set ທີ່ຕ້ອງການລົບອອກ
phone.remove("Nokia")   # ໃຊ້ຄຳສັ່ງ .remove ພ້ອມລະບຸສະມາຊິກທີ່ຕ້ອງການລົບໃນ ()
phone.remove("Iphone")  # ຜົນລັບກໍ່ຈະໄດ້ KeyError: 'Iphone'
print("set ຫຼັງການລົບດ້ວຍ remove :\n",phone)

# ລົບດ້ວຍຄຳສັ່ງ remove ຄືຈະຕ້ອງລະບຸວ່າສະມາຊິກໂຕໃດໃນ set ທີ່ຕ້ອງການລົບອອກ
# ໃຊ້ຄຳສັ່ງ .discard ພ້ອມລະບຸສະມາຊິກທີ່ຕ້ອງການລົບໃນ () ເຖິງສະມາຊິກທີ່ລະບຸຈະບໍ່ຢູ່ໃນ set ກໍ່ຕາມ
phone.discard("Iphone")   
print("set ຫຼັງການລົບດ້ວຍ discard :\n",phone)

# ລົບດ້ວຍຄຳສັ່ງ clear ຄືຈະລົບສະມາຊິກທັງໝົດໃນ set ອອກ ເຫຼືອແຕ່ set ເປົາ
phone.clear()   # ໃຊ້ຄຳສັ່ງ .clear ໂດຍບໍ່ຕ້ອງລະບຸສະມາຊິກໃນ () 
print("set ຫຼັງການລົບດ້ວຍ clear :\n",phone)

# ລົບດ້ວຍຄຳສັ່ງ del ຄືຈະລົບ set ອອກ
del phone 
print("set ຫຼັງການລົບດ້ວຍ del :\n",phone)

