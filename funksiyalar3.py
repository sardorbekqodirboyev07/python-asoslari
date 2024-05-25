def toliq_ism_yasa(ism, familiya):
	"""toliq ism qaytaruvchi funksiya"""
	toliq_ism=f"{ism.title()} {familiya.title()}"
	return toliq_ism

# toliq_ism_yasa('olim','hakimov')

# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')
# talaba3 = toliq_ism_yasa('jamshid','jumanazarov')
# talaba4 = toliq_ism_yasa('bunyod','zayniddinov')
# print(f"darsga kelgan talabalar: {talaba3} va {talaba2}")
# print(f"darsga kelmagan talabalar: {talaba1} va {talaba4}")


def toliq_ism_yasa2(ism,familiya, otasining_ismi=" "):
	if otasining_ismi:
		toliq_ism=f"{ism.title()} {otasining_ismi.upper()} {familiya.title()}"
	else:
		toliq_ism= f" {ism} {familiya}"	
	return toliq_ism.title()

# talaba1 = toliq_ism_yasa2('bunyod','zayniddinov', 'alievich')
# talaba2 = toliq_ism_yasa2('olim','zolimov')
# print(f"darsga kelgan talabalar: {talaba1} va {talaba2}")

def avto_info(kompaniya,model,rang,karobka,yil,narhi=None):
	auto_dict = {
		'kompaniya': kompaniya,
		'model': model,
		'rang': rang,
		'karobka': karobka,
		'yil': yil,
		'narhi': narhi,
	}

	return auto_dict

a = avto_info('GM', 'Cobalt', 'oq', 'avtomat', 2021, 1800000)
print(a)