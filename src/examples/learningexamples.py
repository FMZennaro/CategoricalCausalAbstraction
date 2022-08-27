
import numpy as np

from pgmpy.models import BayesianNetwork as BN
from pgmpy.factors.discrete import TabularCPD as cpd


def M0_simpletest(mech=None):
    if mech is None: mech = np.array([[0.2,0.1,],[0.3,0.6],[0.5,0.3]], dtype=np.float32)
    
    M0 = BN([('a','b')])

    cpdA = cpd(variable='a',
              variable_card=2,
              values=[[0.5],[0.5]],
              evidence=None,
              evidence_card=None)
    cpdB = cpd(variable='b',
              variable_card=3,
              values=mech,
              evidence=['a'],
              evidence_card=[2])

    M0.add_cpds(cpdA,cpdB)
    M0.check_model()    
    return M0

def M1_simpletest(mech=None):
    if mech is None: mech = np.array([[0.7,0.4],[0.3,0.6]], dtype=np.float32)
    
    M1 = BN([('x','y')])

    cpdX = cpd(variable='x',
              variable_card=2,
              values=[[0.5],[0.5]],
              evidence=None,
              evidence_card=None)
    cpdY = cpd(variable='y',
              variable_card=2,
              values=mech,
              evidence=['x'],
              evidence_card=[2])


    M1.add_cpds(cpdX,cpdY)
    M1.check_model()   
    return M1

def A_simpletest(mech_low=None,mech_high=None,alphas=None):
    M0 = M0_simpletest(mech_low)
    M1 = M1_simpletest(mech_high)
    R = ['a','b']
    a = {'a': 'x',
         'b': 'y'}
    if alphas is None:
        alphas = {"x": np.array([[1,0],[0,1]]),
                 "y": np.array([[1,0,1],[0,1,0]])}
    return M0,M1,R,a,alphas


def M0_multidiagramtest(mech_T=None,mech_C=None):
    if mech_T is None: mech_T = np.array([[.6,.55,.1,.1],[.3,.25,.4,.4],[.1,.2,.5,.5]], dtype=np.float32)
    if mech_C is None: mech_C = np.array([[.7,.7,.4],[.3,.3,.6]], dtype=np.float32)
    
    M0 = BN([('S','T'),('T','C')])

    cpdS = cpd(variable='S',
              variable_card=4,
              values=[[.25],[.25],[.25],[.25]],
              evidence=None,
              evidence_card=None)
    cpdT = cpd(variable='T',
              variable_card=3,
              values=mech_T,
              evidence=['S'],
              evidence_card=[4])
    cpdC = cpd(variable='C',
              variable_card=2,
              values=mech_C,
              evidence=['T'],
              evidence_card=[3])

    M0.add_cpds(cpdS,cpdT,cpdC)
    M0.check_model()
    return M0

def M1_multidiagramtest(mech_T=None,mech_C=None):
    if mech_T is None: mech_T = np.array([[.9,.8,.5],[.1,.2,.5]], dtype=np.float32)
    if mech_C is None: mech_C = np.array([[.7,.4],[.3,.6]], dtype=np.float32)
        
    M1 = BN([('S_','T_'),('T_','C_')])

    cpdS = cpd(variable='S_',
              variable_card=3,
              values=[[.25],[.5],[.25]],
              evidence=None,
              evidence_card=None)
    cpdT = cpd(variable='T_',
              variable_card=2,
              values=mech_T,
              evidence=['S_'],
              evidence_card=[3])
    cpdC = cpd(variable='C_',
              variable_card=2,
              values=mech_C,
              evidence=['T_'],
              evidence_card=[2])

    M1.add_cpds(cpdS,cpdT,cpdC)
    M1.check_model()
    
    return M1

def A_multidiagramtest(mech_T_low=None,mech_C_low=None,mech_T_high=None,mech_C_high=None,alphas=None):
    M0 = M0_multidiagramtest(mech_T_low,mech_C_low)
    M1 = M1_multidiagramtest(mech_T_high,mech_C_high)
    R = ['S','T','C']
    a = {'S': 'S_',
         'T': 'T_',
         'C': 'C_'}
    if alphas is None:
        alphas = {"S_": np.array([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,1,1]]),
                 "T_": np.array([[1,1,0],
                        [0,0,1]]),
                 "C_": np.array([[1,0],
                        [0,1]])}
    return M0,M1,R,a,alphas