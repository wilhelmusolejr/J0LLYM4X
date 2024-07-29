discount = 9

class Denoes:
  def __init__(self, deno, gcash_price, quantity, free, toPay, whatToBuy):
    self.deno = deno
    self.gcash_price = gcash_price
    self.quantity = quantity
    self.free = free
    self.toPay = toPay
    self.whatToBuy = whatToBuy
    self.total_quantity = quantity + free
    self.total = (quantity * gcash_price) + ((quantity + free) * toPay)
    self.gain = (whatToBuy * self.total_quantity) * float("." + str(100 - discount)) - self.total

# Number of available voucher
one = 1
twentyThree = 0
thirtySeven = 0
eightyFive = 0
oneTwentyNine = 0

# DATA
deno = {
  '10': Denoes(10, 3, one, 0, 10, 20),
  '30': Denoes(30, 25, twentyThree, 1, 19, 50),
  '50': Denoes(50, 45, thirtySeven, 0, 46, 100),
  '100': Denoes(100, 69, eightyFive, 0, 45, 150),
  '150': Denoes(150, 135, oneTwentyNine, 0, 134, 300)
}

gain = 0
gcashFund = 0
toPayTotal = 0
totalRg = 0
for attr, value in deno.items():
  gain += value.gain
  gcashFund += value.total
  totalRg += value.whatToBuy * value.total_quantity
  toPayTotal += (value.toPay * value.total_quantity)
  # print(attr, value.total, value.whatToBuy, value.gain)
print(discount, "% Discount for the buyer (FB)")
print("Gain per sim = ", gain, "pesos")
print("Fund needed = ", gcashFund, "pesos")
print("To pay needed = ", toPayTotal, "pesos")
print("Total RG to be generated = ", totalRg)
