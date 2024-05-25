def toliq_ism_yasa(ism, familiya):
	"""To'liq ism qaytaruvchi funksiya"""
	toliq_ism = f'{ism.title()} {familiya.title()}'
	return toliq_ism

# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('vali', 'aliev')

# print(talaba1)
# print(talaba2)

def toliq_ism_yasa2(ism, familiya, otasining_ismi=''):
	"""To'liq ism qaytaruvchi funksiya"""
	if otasining_ismi:
		return f'{ism.upper()} {familiya.upper()} {otasining_ismi.upper()}'
	else:
		return f'{ism.upper()} {familiya.upper()}'

# talaba1 = toliq_ism_yasa2('olim', 'hakimov', 'alijonovich')
# talaba2 = toliq_ism_yasa2('vali', 'aliev')

# print(talaba1)
# print(talaba2)

def auto(model, komp, rang, yil, narx):
	auto = {
		'model': model,
		'komp': komp,
		'rang': rang,
		'yil': yil,
		'narx': f'{narx}$',
	}
	return auto

# print(auto('BMW', 'BMW M3', 'Qora', 2020, 239842))
# auto_dict1 = auto('BMW', 'BMW M3', 'Qora', 2020, 239842)
# for a_k, a_v in auto_dict1.items():
# 	# print(a_k, ":", a_v)
# 	print(f'{a_k}: {a_v}')
