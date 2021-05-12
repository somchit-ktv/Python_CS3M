name = ("John", "Chiele", "Mike", "Kole", "Doley")
# ນັບຈຳນວນສະມາຊິກໃນ tuple ໃຊ້ len
print(len(name))

# ສຳລັບ len ເຮົາຍັງສາມາດໃຊ້ງານຮ່ວມກັນກັບ loop ເພື່ອສະແດງສະມາຊິກຂອງ tuple ໃນແຕ່ລະຕຳແໜ່ງ

# ກຳນົດໃຫ້ i ເປັນໂຕນັບຕຳແໜ່ງຕັ້ງແຕ່ 0 ຈົນຄົບຄວາມຍາວຂອງ name
for i in range(len(name)):            
    print("ສະມາຊິກຕຳແໜ່ງທີ່: ", i, "ແມ່ນ", name[i])       # ສະແດງຕຳແໜ່ງ index ພ້ອມສະມາຊິກໃນ tuple