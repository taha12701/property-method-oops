class marks:

  def __init__(self,math,phy,chem):
    self.math=math
    self.phy=phy
    self.chem=chem
    self.per=str((self.math + self.phy + self.chem )/3) + "%"

  # def change(self):
  #   self.per=str((self.math + self.phy + self.chem )/3) + "%"

  @property
  def change(self):
    return str((self.math + self.phy + self.chem )/3) + "%"

m1=marks(98,89,90)
print(m1.per)
m1.phy=96
# m1.change()
# print(m1.per)
# print(m1.change)
