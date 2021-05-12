# dict ຍ່ອຍ ແມ່ນການເຮັດໃຫ້ຂໍ້ມູນໃນສະມາຊິກຂອງ dict ມີ dict ຊ້ອນອີກ
# ເໝາະສຳລັບການເກັບຂໍ້ມູນທີ່ຊ້ອນກັນຫຼາຍໆຊຸດ
# ເຊັ່ນເກັບຂໍ້ມູນທຸລະກິດ, ບໍລິສັດ, ທີ່ຢູ່ ເປັນຕົ້ນ

# ສ້າງ dict ເພື່ອໃຊ້ເກັບຂໍ້ມູນບໍລິສັດ
company = {                             # ກຳນົດ dict ຫຼັກເປັນ ບໍລິສັດ
    "Administration" : {                # ກຳນົດ key ຫຼັກເປັນພະແນກຕ່າງໆ ໃນບໍລິສັດ
        "Head" : "ສົມດີ ທອງຄຸນ",           # ກຳນົດ key ຍ່ອຍຕາມຄວາມຕ້ອງການ ເຊັ່ນ ຫົວໜ້າ, ເບີໂທ, ອິເມວ, ພະນັກງານ ເປັນຕົ້ນ
        "Room" : [301,302,303],         # ໃນກໍລິນີ້ມີຫຼາຍຄ່າໃຫ້ໃສ່ໃນ []
        "Tel" : "021 666777",
        "Email" : "admin@company.com",
        "TotalEmployee" : 5
    },
    "IT" : {
        "Head" : "ວັນນາ ພຸດທະເສນ",         
        "Room" : [201,202],
        "Tel" : "021 666888",
        "Email" : "it@company.com",
        "TotalEmployee" : 3
    },
    "Accounting" :{
        "Head" : "ສົມພອນ ວັນນະພາ",         
        "Room" : [203,204],
        "Tel" : "021 666888",
        "Email" : "acc@company.com",
        "TotalEmployee" : 4
    },
    "HR" : {
        "Head" : "ກາສອນ ເດດສັກດີ",         
        "Room" : [103,104],
        "Tel" : "021 666888",
        "Email" : "hr@company.com",
        "TotalEmployee" : 4
    }
}

# ສະແດງຂໍ້ມູນທັງໝົດ
print(company)

# ສະແດງສະເພາະຂໍ້ມູນທີ່ຕ້ອງການ
print(company["Accounting"])

# ສະແດງຂໍ້ມູນທີ່ຍ່ອຍລົງໄປອິກ
print(company["Accounting"]["Head"])