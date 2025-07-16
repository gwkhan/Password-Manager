#password manager 


import csv
try:
	with open("pass.csv","r") as file:
		re = csv.reader(file)
		read = list(re)
		print(f'last saved pass : {read[-1]}')
except FileNotFoundError:
	with open("pass.csv","w",newline='')as file:
		write = csv.writer(file)
		write.writerow(["website","user","pass"])
while True:
	print("🔐 Password Manager Menu")
	print("1. Add New Password")
	print("2. View All Saved Passwords")
	print("3. Search Password by Website")
	print("4. Delete a Password Entry")
	print("5. Exit")
	choice = input("Enter your choice (1-5): ")
	if choice =="1":
		a = input("enter in format (website,user,pass)\nenter: ").capitalize()
		with open("pass.csv","a",newline = '') as file:
			wr = csv.writer(file)
			wr.writerow(a.split(","))
	elif choice =="2":
		with open("pass.csv","r")as file:
			r = csv.reader(file)
			for row in r:
				print(row)
	elif choice =="3":
		ask = input("enter website: ").capitalize()
		found = False
		with open("pass.csv", "r")as file:
			read = csv.reader(file)
			for r in read:
				if ask in r:
					print(r)
					found = True
		if not found:
			print("website not exist")
	elif choice =="4":
		dlt = input("which entry do you wanna delete?: ")
		with open("pass.csv","r")as file:
			read = list(csv.reader(file))
		with open("pass.csv","w",newline="")as file:
			write = csv.writer(file)
			for row in read:
				if dlt.lower() not in ",".join(row).lower():
					write.writerow(row)
	elif choice =="5":
		print("thx")
		break
	else:
		print("enter from 1-5")