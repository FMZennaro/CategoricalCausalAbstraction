
import numpy as np

from pgmpy.models import BayesianNetwork as BN
from pgmpy.factors.discrete import TabularCPD as cpd

def generate_values(c,d):
    val = np.random.rand(c,d)
    return val / np.sum(val,axis=0)

def Mt0_0():
    M = BN([('A','C'), ('E','B'), ('E','C'), ('B','C'), ('C','D'), ('C','F')])

    cpdA = cpd(variable='A',
              variable_card=3,
              values=generate_values(3,1),
              evidence=None,
              evidence_card=None)

    cpdE = cpd(variable='E',
              variable_card=2,
              values=generate_values(2,1),
              evidence=None,
              evidence_card=None)

    cpdB = cpd(variable='B',
              variable_card=4,
              values=generate_values(4,2),
              evidence=['E'],
              evidence_card=[2])

    cpdC = cpd(variable='C',
              variable_card=6,
              values=generate_values(6,24),
              evidence=['A','B','E'],
              evidence_card=[3,4,2])

    cpdD = cpd(variable='D',
              variable_card=3,
              values=generate_values(3,6),
              evidence=['C'],
              evidence_card=[6])

    cpdF = cpd(variable='F',
              variable_card=2,
              values=generate_values(2,6),
              evidence=['C'],
              evidence_card=[6])

    M.add_cpds(cpdA,cpdB,cpdC,cpdD,cpdE,cpdF)
    if M.check_model(): return M
    
def Mt0_1():
    M = BN([('X','Y'), ('Y','Z'), ('Y','W'), ('X','Z')])

    cpdX = cpd(variable='X',
              variable_card=3,
              values=generate_values(3,1),
              evidence=None,
              evidence_card=None)

    cpdY = cpd(variable='Y',
              variable_card=4,
              values=generate_values(4,3),
              evidence=['X'],
              evidence_card=[3])

    cpdZ = cpd(variable='Z',
              variable_card=2,
              values=generate_values(2,12),
              evidence=['Y','X'],
              evidence_card=[4,3])

    cpdW = cpd(variable='W',
              variable_card=2,
              values=generate_values(2,4),
              evidence=['Y'],
              evidence_card=[4])

    M.add_cpds(cpdX,cpdY,cpdZ,cpdW)
    if M.check_model(): return M

def get_A_Mt0_1_Mt0_1():
    R = ['A','B', 'C', 'D', 'F']
    a = {'A': 'X',
         'B': 'X',
         'C': 'Y',
         'D': 'Z',
         'F': 'W'}
    alphas = {'X': generate_values(3,12),
             'Y': generate_values(4,6),
             'Z': generate_values(2,3),
             'W': generate_values(2,2)}
    return Mt0_0(),Mt0_1(),R,a,alphas

def Mt1_0():
    M = BN([('A','C'), ('A','D'), ('B','D'), ('B','E'), ('B','F'), ('F','I'), ('D','H'), ('G','E'), ('G','F')])

    cpdA = cpd(variable='A',
              variable_card=3,
              values=generate_values(3,1),
              evidence=None,
              evidence_card=None)

    cpdB = cpd(variable='B',
              variable_card=4,
              values=generate_values(4,1),
              evidence=None,
              evidence_card=None)

    cpdC = cpd(variable='C',
              variable_card=7,
              values=generate_values(7,3),
              evidence=['A'],
              evidence_card=[3])

    cpdD = cpd(variable='D',
              variable_card=4,
              values=generate_values(4,12),
              evidence=['A','B'],
              evidence_card=[3,4])

    cpdE = cpd(variable='E',
              variable_card=3,
              values=generate_values(3,8),
              evidence=['B','G'],
              evidence_card=[4,2])

    cpdF = cpd(variable='F',
              variable_card=3,
              values=generate_values(3,8),
              evidence=['B','G'],
              evidence_card=[4,2])

    cpdG = cpd(variable='G',
              variable_card=2,
              values=generate_values(2,1),
              evidence=None,
              evidence_card=None)

    cpdH = cpd(variable='H',
              variable_card=6,
              values=generate_values(6,4),
              evidence=['D'],
              evidence_card=[4])

    cpdI = cpd(variable='I',
              variable_card=5,
              values=generate_values(5,3),
              evidence=['F'],
              evidence_card=[3])

    M.add_cpds(cpdA,cpdB,cpdC,cpdD,cpdE,cpdF,cpdG,cpdH,cpdI)
    if M.check_model(): return M
    
def Mt1_1():
    M = BN([('X','Z'), ('Y','W'), ('Y','V')])
    M.add_node('U')

    cpdX = cpd(variable='X',
              variable_card=3,
              values=generate_values(3,1),
              evidence=None,
              evidence_card=None)

    cpdY = cpd(variable='Y',
              variable_card=3,
              values=generate_values(3,1),
              evidence=None,
              evidence_card=None)

    cpdZ = cpd(variable='Z',
              variable_card=24,
              values=generate_values(24,3),
              evidence=['X'],
              evidence_card=[3])

    cpdW = cpd(variable='W',
              variable_card=2,
              values=generate_values(2,3),
              evidence=['Y'],
              evidence_card=[3])

    cpdV = cpd(variable='V',
              variable_card=8,
              values=generate_values(8,3),
              evidence=['Y'],
              evidence_card=[3])

    cpdU = cpd(variable='U',
              variable_card=2,
              values=generate_values(2,1),
              evidence=None,
              evidence_card=None)

    M.add_cpds(cpdX,cpdY,cpdZ,cpdW,cpdV,cpdU)
    if M.check_model(): return M
    
def get_A_Mt1_1_Mt1_1():
    R = ['A','B', 'D', 'E', 'F', 'G', 'H', 'I']
    a = {'A': 'X',
         'B': 'Y',
         'D': 'Z',
         'E': 'W',
         'F': 'V',
         'G': 'U',
         'H': 'Z',
         'I': 'V'}
    alphas = {'X': generate_values(3,3),
             'Y': generate_values(3,4),
             'Z': generate_values(24,24),
             'W': generate_values(2,3),
             'V': generate_values(8,15),
             'U': generate_values(2,2),
             }
    return Mt1_0(),Mt1_1(),R,a,alphas