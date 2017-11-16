from array import *
from ROOT import *

c1 = TCanvas()
c1.Divide(1, 2)

fland = TF1("fland","TMath::Landau(x,[0],[1],0)",-5,10);
fland.SetParameters(0,1);
c1.cd(1)
fland.Draw()

ndata = 100
npoints = int(ndata/5.)
vland = []
hland = TH1F('hland', 'hland', npoints, -5, 10)
randgen = TRandom3(0)
for i in range(0, ndata):
  val = randgen.Landau()
  vland.append(val)
  hland.Fill(val)
c1.cd(2)
hland.Scale(1./npoints)
#~ hland.Draw('hist')

# TKDE
aland = array('d', vland)
kdeland = TKDE(npoints, aland, -5, 10, 'kUnbinned')
kfland = kdeland.GetFunction(npoints, -5, 10)
#~ kfland.Draw('same')
kfland.Draw()
print fland.GetMaximumX(), kfland.GetMaximumX()

raw_input('press enter to continue')
