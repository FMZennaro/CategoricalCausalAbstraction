import math
import numpy as np
import scipy.stats as stats

def _compute_maxent_input_distrib(M):
    return np.ones(M.shape[1])/M.shape[1]

def _compute_maxent_output_distrib(M):
    return np.ones(M.shape[0])/M.shape[0]


def EI(M,base=2):
    maxent_input_distrib = _compute_maxent_input_distrib(M)
    maxent_effects = np.dot(M,maxent_input_distrib)
    KLs = stats.entropy(M, np.expand_dims(maxent_effects,axis=1),base=base)
    EI = np.average(KLs)
    return KLs,EI

def determinism(M,base=2):
    maxent_output_distrib = _compute_maxent_output_distrib(M)
    KLs = stats.entropy(M, np.expand_dims(maxent_output_distrib,axis=1),base=base)
    determinism = np.average(KLs/np.log2(M.shape[1]))
    return KLs,determinism

def degeneracy(M,base=2):
    maxent_input_distrib = _compute_maxent_input_distrib(M)
    maxent_effects = np.dot(M,maxent_input_distrib)
    maxent_output_distrib = _compute_maxent_output_distrib(M)
    KLs = stats.entropy(maxent_effects, maxent_output_distrib,base=base)
    degeneracy = KLs/math.log(M.shape[1],base)
    return KLs,degeneracy

def effectiveness(M,base=2):
    _,det = determinism(M,base=base)
    _,deg = degeneracy(M,base=base)
    return det-deg

def EI_eff_size(M,base=2):
    eff = effectiveness(M,base=base)
    size = math.log(M.shape[1],base)
    return eff*size