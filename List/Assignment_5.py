# ຫາຄ່າເລກຍົກກຳລັງ
number=[1,2,3,4,5,6,7]          # ກຳນົດສະມາຊິກຂອງ list

print(number)
# ແບບປົກກະຕິ
for i in range(len(number)):    # ກຳນົດໃຫ້ i ເປັນໂຕນັບຕຳແໜ່ງຕັ້ງແຕ່ 0 ຈົນຄົບຄວາມຍາວຂອງ number
    number[i]=number[i]**2      # ເອົາຄ່າຂອງ number ໃນຕຳແໜ່ງ i ມາຄູນໃຫ້ຕົວມັນເອງ
print(number)                   

# ແບບສັ້ນ
number=[i*i for i in number]
print(number)