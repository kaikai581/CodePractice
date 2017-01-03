# This script is an almost faithful line by line translation
# of Wouter Verkerke's ROOT script taken from here:
# https://root.cern.ch/phpBB3/download/file.php?id=7257&sid=1cc8e740355c8095e47538959787881c
# See https://root.cern.ch/phpBB3/viewtopic.php?f=15&t=9087&sid=26efa500aad18fdcefbff7294df39ad3

from ROOT import *
from ROOT.RooFit import *

# make each toy data different
RooRandom.randomGenerator().SetSeed()

w = RooWorkspace('w',1)
w.factory('SUM::genmodel(1000*Gaussian::g(x[-10,10],mg[0],3),1000*Uniform::u(x))')
w.var('x').setBins(10)


# The 'observed' data
argset_x = RooArgSet(w.var('x'))
obsData = w.pdf('genmodel').generate(argset_x,AllBinned(),NumEvents(2000))

# Make HistFuncs for sigma and background to serve as templates
dh_bkg = w.pdf('u').generateBinned(argset_x,1000)
dh_sig = w.pdf('g').generateBinned(argset_x,1000)

Asig = RooRealVar('Asig','Asig',1,0.01,10)
Abkg = RooRealVar('Abkg','Abkg',1,0.01,10)

# ***** Case 0 - 'Rigid templates' *****

# Construct histogram shapes for signal and background
p_h_sig = RooHistFunc('p_h_sig','p_h_sig',argset_x,dh_sig)
p_h_bkg = RooHistFunc('p_h_bkg','p_h_bkg',argset_x,dh_bkg)

# Construct the sum of these
model0 = RooRealSumPdf('model0','model0',RooArgList(p_h_sig,p_h_bkg),RooArgList(Asig,Abkg),kTRUE)

# ***** Case 1 - 'Beeston Barlow' *****

# Construct parameterized histogram shapes for signal and background
p_ph_sig = RooParamHistFunc('p_ph_sig','p_ph_sig',dh_sig)
p_ph_bkg = RooParamHistFunc('p_ph_bkg','p_ph_bkg',dh_bkg)

# Construct the sum of these
model_tmp = RooRealSumPdf('sp_ph','sp_ph',RooArgList(p_ph_sig,p_ph_bkg),RooArgList(Asig,Abkg),kTRUE)

# Construct the subsidiary poisson measurements constraining the histogram parameters
hc_sig = RooHistConstraint('hc_sig','hc_sig',RooArgSet(p_ph_sig))
hc_bkg = RooHistConstraint('hc_bkg','hc_bkg',RooArgSet(p_ph_bkg))

# Construct the joint model
model1 = RooProdPdf('model1','model1',RooArgSet(hc_sig,hc_bkg),Conditional(RooArgSet(model_tmp),argset_x))

# ***** Case 2 - 'Beeston Barlow' light *****

# Construct the background histogram shape, using the same parameters as the signal histogram
p_ph_bkg2 = RooParamHistFunc('p_ph_bkg','p_ph_bkg',dh_bkg,p_ph_sig,1)

# Construct the sum of signal and background2
model2_tmp = RooRealSumPdf('sp_ph','sp_ph',RooArgList(p_ph_sig,p_ph_bkg2),RooArgList(Asig,Abkg),kTRUE)

# Construct the subsidiary poisson measurements constraining the sum of the histograms
hc_sigbkg = RooHistConstraint('hc_sigbkg','hc_sigbkg',RooArgSet(p_ph_sig,p_ph_bkg2))

# Construct the joint model
model2 = RooProdPdf('model2','model2',RooArgSet(hc_sigbkg),Conditional(RooArgSet(model2_tmp),argset_x))

# fit models to data
model0.fitTo(obsData)
asig_val0 = Asig.getVal()
asig_err0 = Asig.getError()
model1.fitTo(obsData)
asig_val1 = Asig.getVal()
asig_err1 = Asig.getError()
model2.fitTo(obsData)
asig_val2 = Asig.getVal()
asig_err2 = Asig.getError()
print 'Asig [normal ] =',asig_val0,'+/-',asig_err0
print 'Asig [BB     ] =',asig_val1,'+/-',asig_err1
print 'Asig [BBlight] =',asig_val2,'+/-',asig_err2

# make plot
xframe = w.var('x').frame(Title('gaussian on top of uniform'))
obsData.plotOn(xframe)
model0.plotOn(xframe,LineColor(kYellow))
model1.plotOn(xframe,LineColor(kMagenta))
model2.plotOn(xframe,LineColor(kBlue))
xframe.Draw()

#~ w.Print()
raw_input('press enter to continue')
