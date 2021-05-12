class ItemStore:
  def __init__(self):
    self.items = SwordItem()
    self.stocked = True

  # "buy" an item, checked by driver, sets stocked to false
  def buy_item(self):
    self.stocked = False

  # reset shop 
  def restock(self):
    self.stocked = True
    self.items.increment_value()


class SwordItem:
  def __init__(self):
    self.value = 180

  def increment_value(self):
    self.value += (1/2 * self.value)