def salom_ber(ism):
	"""Foydalanuvchi ismini qabul qilib,
	unga salom beruvchi funksiya"""
	print(f"Assalomu alaykum, hurmatli {ism.upper()}!")
# salom_ber("husan")
# salom_ber("olim")


def toliq_ism(ism, familiya):
	"""Foydalanuvchi ism va familyasini jamlab chiqaruchi funksiya"""
	print(f"foydalanuvchining ismi: {ism.upper()}\n"
		f"foydalanuvchining familiyasi: {familiya.upper()}")



# i = 'husan'
# f = 'aliev'
# toliq_ism(i, f)
# toliq_ism("olim","hakimov")
# toliq_ism(f, i)

def yosh_hisobla(ism, tugilgan_yil):
	"""foydalanuvchining yoshini hisoblaydigan dastur"""
	print(f"{ism.upper()} {2024-tugilgan_yil}")

yosh_hisobla('olim',1990)
# yosh_hisobla(1990,'olim') # Error

yosh_hisobla(tugilgan_yil=1990, ism='olim')
yosh_hisobla(tugilgan_yil=2005, ism='diyor')

