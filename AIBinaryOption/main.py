from agent import Agent
from environment import Environment

price_quote = []

with open('bcdata.sgs.10813.csv', encoding='UTF-8') as file:
	lines = file.readlines()
	for line in lines[1:]:
		parts = line.strip().split(';')
		value_str = parts[1].replace('"', '').replace(',', '.')
		value = float(value_str)
		price_quote.append(value)
