name = ["John", "Chiele", "Mike", "Kole", "Doley"]
# ນັບຈຳນວນສະມາຊິກໃນ list ໃຊ້ len
print(len(name))

# ສຳລັບ len ເຮົາຍັງສາມາດໃຊ້ງານຮ່ວມກັນກັບ loop ເພື່ອສະແດງສະມາຊິກຂອງ list ໃນແຕ່ລະຕຳແໜ່ງ
for i in range(len(name)):            # ກຳນົດໃຫ້ i ເປັນໂຕນັບຕຳແໜ່ງຕັ້ງແຕ່ 0 ຈົນຄົບຄວາມຍາວຂອງ name
    print("ສະມາຊິກຕຳແໜ່ງທີ່: ", i, "ແມ່ນ", name[i])       # ສະແດງຕຳແໜ່ງ index ພ້ອມສະມາຊິກໃນ list
