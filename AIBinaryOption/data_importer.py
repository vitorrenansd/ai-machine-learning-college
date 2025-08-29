class DataImporter:

	def pull_data_from(file_path):
		price_quote = []

		with open(file_path, encoding='UTF-8') as file:
			lines = file.readlines()
			for line in lines[1:]:
				parts = line.strip().split(';')
				value_str = parts[1].replace('"', '').replace(',', '.')
				price_quote.append(float(value_str))
				return price_quote
