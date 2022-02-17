
# CategoricalCausalAbstraction
A series of notebooks containing tutorials, reproduction of work in papers [1,2,3], and open notes on the problem of abstraction of structural causal models in a categorical framework.

### Contents

1. **Categorical Abstraction**: A tutorial notebook in which we explore the idea of abstraction between causal models following the framework presented in [1] and illustrating the main ideas by replicating (theoretically and experimentally) the examples in Sections 4.11-4.13 of [1].

2. **Abstraction Mapping**: A notebook in which we take a closer look to the definition of abstraction between causal models that was presented in [1] and reviewed in the previous notebook. Along with the theoretical discussion we also implement classes to encode SCMs and abstractions.

3. **Transformations and Abstractions**: Another tutorial notebook where we consider in this case the concept of transformation and exact transformations from [2] and we perform a first example-driven comparison between abstractions and transformations.

4. **Automating Abstraction Error**: In this notebook we automate the estimation of abstraction error using the framework introduced in [1] and explored in the notebook *Categorical Abstraction*. We implement a function that estimate abstraction error as a function of a chosen evaluation set and metric.

### Disclaimers

**Notebooks are best visualized on [nbviewer](https://nbviewer.jupyter.org/)**: equations, in particular, may not be rendered on github.

**This is a work in progress**: notebooks are executable, but TODO sections are sprinkled across the notebooks.

**Feedbacks are welcome**: mistakes are in all likelihood due to misunderstandings of the notebook author and suggestions/corrections are very welcome! :)

**References** the notebook refers to ideas from *causality* and *category theory*. Useful references for causality are [4,5], while for category theory are [6,7].

### Bibliography

[1] Rischel, Eigil Fjeldgren. "The Category Theory of Causal Models." (2020).

[2] Rubenstein, Paul K., et al. "Causal consistency of structural equation models." arXiv preprint arXiv:1707.00819 (2017).

[3] Rischel, Eigil F., and Sebastian Weichwald. "Compositional Abstraction Error and a Category of Causal Models." arXiv preprint arXiv:2103.15758 (2021).

[4] Pearl, Judea. Causality. Cambridge university press, 2009.

[5] Peters, Jonas, Dominik Janzing, and Bernhard Schölkopf. Elements of causal inference: foundations and learning algorithms. The MIT Press, 2017.

[6] Spivak, David I. Category theory for the sciences. MIT Press, 2014.

[7] Fong, Brendan, and David I. Spivak. "Seven sketches in compositionality: An invitation to applied category theory." arXiv preprint arXiv:1803.05316 (2018).
