class DataImporter:
	def __init__(self, price_quote=[]):
		self.price_quote = price_quote

	def pull_data_from(self, file_path):
		with open(file_path, encoding='UTF-8') as file:
			lines = file.readlines()
			for line in lines[1:]:
				parts = line.strip().split(';')
				value_str = parts[1].replace('"', '').replace(',', '.')
				self.price_quote.append(float(value_str))
				return self.price_quote
