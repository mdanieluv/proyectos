monto=int(input("Ingrese monto:"))
miguel=monto*0.27
luis=miguel*0.85
daniel=monto*0.25
eduardo=0.23*(miguel+daniel)
david=monto-(miguel+luis+daniel+eduardo)
print("Miguel: ",miguel)
print("Luis: ",luis)
print("Daniel: ",daniel)
print("Eduardo: ",eduardo)
print("David: ",david)