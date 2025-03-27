
investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

bitcoin_amount = 1.2
bitcoin_to_usd = 40000
def calculate_bitcoin_to_usd(bitcoin_amount, bitcoin_to_usd):
   bitcoinToUSD  = bitcoin_amount * bitcoin_to_usd
  return investment_in_usd

bitcoin_value_usd = calculate_bitcoin_to_usd(bitcoin_amount, bitcoin_to_usd)
if bitcoin_value_usd <= 30000:
  print("Investment below $30,000! SELL!")
else:
  print("Investment above $30,000")