
#  Causal Abstraction
A series of notebooks containing tutorials, reproduction of work in the literature, and open notes on the problem of abstraction of structural causal models (starting from a categorical framework).


## Contents

1. **Categorical Abstraction**: A tutorial notebook in which we explore the idea of abstraction between causal models following the framework presented in [Rischel2020] and illustrating the main ideas by replicating (theoretically and experimentally) the examples in Sections 4.11-4.13 of [Rischel2020].

2. **Abstraction Mapping**: A notebook in which we take a closer look to the definition of abstraction between causal models that was presented in [Rischel2020] and reviewed in the previous notebook. Along with the theoretical discussion we also implement classes to encode SCMs and abstractions.

3. **Transformations and Abstractions**: Another tutorial notebook where we consider in this case the concept of transformation and exact transformations from [Rubenstein2017] and we perform a first example-driven comparison between abstractions and transformations.

4. **Automating Abstraction Error**: In this notebook we automate the estimation of abstraction error using the framework introduced in [Rischel2020] and explored in the notebook *Categorical Abstraction*. We implement a function that estimate abstraction error as a function of a chosen evaluation set and metric.

5. **Compositional Abstraction Error** : An important property when working with approximate abstraction is the compositionality of errors. This property depends on the correct choice of a distance metric. In this notebook we review the examples and counterexamples presented in [Rischel2021].

6. **Reviewing forms of consistency**: Assessment of the quality of an abstraction in the framework of [Rischel2020] is based on the evaluation of interventional consistency. In this notebook we review different types of consistency (observational, interventional, and counterfactual) in the context of abstraction.

P1. **Motivating example**: code and simulation in support for the paper [Zennaro2022a]

X1. **GA Abstraction Learning.ipynb**: preliminary attempt at solving an abstraction learning problem using a genetic algorithm.




## Disclaimers

**Notebooks are best visualized on [nbviewer](https://nbviewer.jupyter.org/)**: equations, in particular, may not be rendered on github.

**This is a work in progress**: notebooks are executable, but TODO sections are sprinkled across the notebooks.

**Feedbacks are welcome**: mistakes are in all likelihood due to misunderstandings of the notebook author and suggestions/corrections are very welcome! :)

**References** the notebook refers to ideas from *causality* and *category theory*. Useful references for causality are [Pearl2009,Peters2017], while for category theory are [Spivak2014,Fong2018].


### Bibliography

[Rubenstein2017] Paul K Rubenstein, Sebastian Weichwald, Stephan Bongers, Joris M Mooij, Dominik Janzing, Moritz Grosse-Wentrup, and Bernhard Scholkopf. "Causal consistency of structural equation models." Uncertainty in Artificial Intelligence (UAI). 2017.

[Rischel2020] Rischel, Eigil Fjeldgren. "The Category Theory of Causal Models." (2020).

[Rischel2021] Rischel, Eigil F., and Sebastian Weichwald. "Compositional abstraction error and a category of causal models." Uncertainty in Artificial Intelligence. PMLR, 2021.

[Pearl2009] Pearl, Judea. Causality. Cambridge university press, 2009.

[Peters2017] Peters, Jonas, Dominik Janzing, and Bernhard Schölkopf. Elements of causal inference: foundations and learning algorithms. The MIT Press, 2017.

[Spivak2014] Spivak, David I. Category theory for the sciences. MIT Press, 2014.

[Fong2018] Fong, Brendan, and David I. Spivak. "Seven sketches in compositionality: An invitation to applied category theory." arXiv preprint arXiv:1803.05316 (2018).

[Otsuka2022] Otsuka, Jun, and Hayato Saigo. "On the Equivalence of Causal Models: A Category-Theoretic Approach." arXiv preprint arXiv:2201.06981 (2022).

[Beckers2019] Beckers, Sander, and Joseph Y. Halpern. "Abstracting causal models." Proceedings of the AAAI conference on artificial intelligence. Vol. 33. No. 01. 2019.

[Beckers2020] Beckers, Sander, Frederick Eberhardt, and Joseph Y. Halpern. "Approximate causal abstractions." Uncertainty in Artificial Intelligence. PMLR, 2020.

[Chalupka2015] Chalupka, Krzysztof, Pietro Perona, and Frederick Eberhardt. "Visual causal feature learning." Proceedings of the Thirty-First Conference on Uncertainty in Artificial Intelligence. 2015.

[Chalupka2017] Chalupka, Krzysztof, Frederick Eberhardt, and Pietro Perona. "Causal feature learning: an overview." Behaviormetrika 44.1 (2017): 137-164.

[Hoel2013] Hoel, Erik P., Larissa Albantakis, and Giulio Tononi. "Quantifying causal emergence shows that macro can beat micro." Proceedings of the National Academy of Sciences 110.49 (2013): 19790-19795.

[Hoel2017] Hoel, Erik P. "When the map is better than the territory." Entropy 19.5 (2017): 188.

[Zennaro2022a] Zennaro, Fabio Massimo, Paolo Turrini, and Theo Damoulas. "Towards Computing an Optimal Abstraction for Structural Causal Models." UAI 2022 Workshop on Causal Representation Learning.

[Zennaro2022b] Zennaro, Fabio Massimo. "Abstraction between Structural Causal Models: A Review of Definitions and Properties." UAI 2022 Workshop on Causal Representation Learning.