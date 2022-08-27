
import numpy as np


def inverse_fx(f,x):
    """
    Given a function f as a dictionary, it computes f^-1(x).

    Args:
        f: a function encoded in a dictionary
        x: a value encoded as a dictionary key

    Returns:
        List of all the values f^-1(x)
    """
    return list(np.array(list(f.keys()))[np.where(np.in1d(np.array(list(f.values())),x))[0]])

def get_cardinalities_Falpha(F,alpha,cards_domain,cards_codomain):
    """
    It computes the cardinality of domain and codomain, of a function f out of a dictionary of functions F.

    Args:
        f: a dictionary of functions
        alpha: a key to a function
        cards_domain: dictionary of set cardinalities
        cards_codomain: dictionary of set cardinalities

    Returns:
        cards_domain: the cardinality of the domain of F_alpha
        cards_codomain: the cardinality of the codomain of F_alpha
    """
    domain = inverse_fx(F,alpha)
    card_domain = 1
    for d in domain:
        card_domain = card_domain * cards_domain(d)
    card_codomain = cards_codomain(alpha)
    return card_domain,card_codomain

def is_list_contained_in_list(subset,superset):
    """
    Returns whether the list subset is set-contained in the list superset.

    Args:
        subset: list
        superset: list

    Returns:
        True if subset is contained in superset
    """ 
    return np.all(np.in1d(np.array(subset),np.array(superset)))

def is_list_contents_unique(ulist):
    """
    Returns whether the list contains duplicates.

    Args:
        ulist: list

    Returns:
        True if the list does not contain duplicates
    """ 
    return len(set(ulist)) == len(ulist)

def is_surjective(frange,fcodomain):
    """
    Check the surjectivity conditions by evaluating whether codomain and range are equal

    Args:
        frange: list
        fcodomain: list

    Returns:
        True if codomain and range are set equal 
    """ 
    return set(fcodomain)==set(frange)

def flat_tensor_product(x,y):
    tensor = np.einsum('ij,kl->ikjl',x,y)
    return tensor.reshape((tensor.shape[0]*tensor.shape[1],tensor.shape[2]*tensor.shape[3]))

def tensorize_list(tensor,l):
        #Given a list of matrices iteratively compute the tensor product and flatten
        if tensor is None:
            if len(l)>1:
                tensor = flat_tensor_product(l[0],l[1])
                return tensorize_list(tensor,l[2:])
            else:
                return l[0]
        else:
            if len(l)>0:
                tensor = flat_tensor_product(tensor,l[0])
                return tensorize_list(tensor,l[1:])
            else:
                return tensor

def invert_matrix_max_entropy(A):        
    invA = np.transpose(A)
    invA = invA / np.sum(invA,axis=0)
    return invA
    
def invert_matrix_pinv(A):
    invA = np.linalg.pinv(A)
    return invA