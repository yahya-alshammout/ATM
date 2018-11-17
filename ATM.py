
class ATM:
	def __init__(self, balance, bank_name):
		self.balance = balance
		self.bank_name = bank_name
		self.withdrawals_list = []
	def withdraw(self, request):
		print("welcome to ", self.bank_name)
		print("balance = ", self.balance)
		if request <= self.balance:
			if request > 0 :
				self.withdrawals_list.append(request)
				self.balance -= request
				notes = [100, 50, 10, 5]
				for note in notes:
					while request >= note:
						request -= note
						print("give ", str(note))
						if request < note and request != 0:
							print("give ", str(request))
			else:
				print("please try again")
		else:
			print("not enough money")
		return self.balance
	def show_withdrawals(self):
		for withdrawal in self.withdrawals_list:
			print(withdrawal)


atm1 = ATM(500, "Jordan Bank")
atm1.withdraw(700)
atm1.withdraw(300)
atm1.show_withdrawals()

atm2 = ATM(1000, "Islamic Bank")
atm2.withdraw(500)
atm2.withdraw(253)
atm2.show_withdrawals()
