"""
subset ແມ່ນ set ຍ່ອຍ
superset ແມ່ນ set ຫຼັກ
ຕົວຢ່າງ: 
ປະເທດລາວ ແມ່ນ superset 
=> ແຕ່ລະແຂວງ ແມ່ນ subset ຂອງປະເທດລາວ
=> ແຕ່ລະເມືອງ ແມ່ນ subset ຂອງແຂວງ
=> ແຕ່ລະບ້ານ ແມ່ນ subset ຂອງເມືອງ

"""
# superset ເປັນນະຄອນຫຼວງວຽງຈັນ ມີສະມາຊິກເປັນແຕ່ລະເມືອງ
vientiane_cap = {"Chanthabuly", "Sikhottabong", "Xaysetha", "Sisattanak", "Naxaithong", "Xaythany", "Hadxayfong", "Sangthong", 	"Parkngum"}

# subset ສະມາຊິກແຕ່ລະເມືອງ
district = {"Xaysetha", "Sisattanak"}

# ກວດສອບວ່າ ສະມາຊິກ subset ທີ່ລະບຸມີຢູ່ໃນ superset ຫຼື ບໍ່ ຜົນລັບຈະໄດ້ເປັນຄ່າ boolean
print("Subset check => ",district.issubset(vientiane_cap))

# ກວດສອບວ່າ superset ມີສະມາຊິກ subset ທີ່ລະບຸ ຫຼື ບໍ່ ຜົນລັບຈະໄດ້ເປັນຄ່າ boolean
print("Superset check => ",vientiane_cap.issuperset(district))