
import numpy as np
import networkx as nx
import itertools
import src.utils as ut

    
def check_path_between_sets(G,sources,targets):
    """
    It computes whether there is a path between a set of source nodes and a set of target nodes.

    Args:
        G: a networkx graph
        sources: a set of source nodes in G
        targets: a set of target nodes in G

    Returns:
        True if there is a path in G between source and target
    """
    augmentedG = G.copy()

    augmented_s = 'augmented_s_'+str(np.random.randint(10**6))
    augmented_t = 'augmented_t_'+str(np.random.randint(10**6))
    augmentedG.add_node(augmented_s)
    augmentedG.add_node(augmented_t)

    [augmentedG.add_edge(augmented_s,s) for s in sources]
    [augmentedG.add_edge(t,augmented_t) for t in targets]

    return nx.has_path(augmentedG,augmented_s,augmented_t)

def powerset(iterable):
    """
    It computes the power set of a set.

    Args:
        iterable: an iterable

    Returns:
        The power set of iterable
    """
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))
    
def get_pairs_in_M1_with_directed_path_in_M1(M1):
    J = []
    sources = list(M1.nodes())
    targets = list(M1.nodes())
    for s in sources:
        for t in list(set(targets)-{s}):
            if nx.has_path(M1,s,t):
                J.append((s,t))
    return J
    
def get_all_pairs_in_M1(M1):
    J = list(itertools.permutations(M1.nodes(),2))
    return J
    
def get_pairs_in_M1_with_directed_path_in_M1_or_M0(M0,M1,a):
    J = []
    sources = list(M1.nodes())
    targets = list(M1.nodes())
    for s in sources:
        for t in list(set(targets)-{s}):
            if nx.has_path(M1,s,t):
                J.append((s,t))
            else:
                M0_sources = ut.inverse_fx(a,s)
                M0_targets = ut.inverse_fx(a,s)
                if check_path_between_sets(M0,M0_sources,M0_targets):
                    J.append((s,t))
    return J
    
def get_sets_in_M1_with_directed_path_in_M1_or_M0(M0,M1,a,verbose=False):
    J = []
    sets = list(powerset(M1.nodes()))
    sets.remove(())

    for i in sets:
        for j in sets:
            M1_sources = list(i)
            M1_targets = list(j)
            if not(any(x in M1_sources for x in M1_targets)):            
                if check_path_between_sets(M1,M1_sources,M1_targets):
                    if verbose: print('- Checking {0} -> {1}: True'.format(M1_sources,M1_targets))
                    J.append([M1_sources,M1_targets])
                else:
                    if verbose: print('- Checking {0} -> {1}: False'.format(M1_sources,M1_targets))
                    M0_sources = ut.inverse_fx(a,M1_sources)
                    M0_targets = ut.inverse_fx(a,M1_targets)
                    if check_path_between_sets(M0,M0_sources,M0_targets):
                        if verbose: print('---- Checking {0} -> {1}: True'.format(M0_sources,M0_targets))
                        J.append([M1_sources,M1_targets])
                    else:
                        if verbose: print('---- Checking {0} -> {1}: False'.format(M0_sources,M0_targets))
    if verbose: print('\n {0} legitimate pairs of sets out of {1} possbile pairs of sets'.format(len(J),len(sets)**2))  

    return J