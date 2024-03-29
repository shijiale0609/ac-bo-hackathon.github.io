---
number: 15
title: Adaptive Batch Sizes for Bayesian Optimization of Reaction Yield
topic: general
team_leads:
  - Rubén Laplaza (Laboratory for Computational Molecular Design, EPFL, Switzerland), @rlaplaza
  - Jan Weinreich (Laboratory for Computational Molecular Design, EPFL, Switzerland), @janweinreich

contributors:
  - Ksenia Briling (Laboratory for Computational Molecular Design, EPFL, Switzerland), @briling
  - Yannick Calvino Alonso (Laboratory for Computational Molecular Design, EPFL, Switzerland), @YAY-C
  - Alexandre Alain Schöpfer (Laboratory for Computational Molecular Design, EPFL, Switzerland), @aa-schoepfer
  - Leon Schlosser (University of Münster, Germany), @le-schlo
  - Florian Boser (University of Münster, Germany), @FlorianBoser
 
# github: https://github.com/janweinreich/best_batchers
# youtube_video: https://www.youtube.com/watch?v=utnWbJsObF0

---

**Challenge:** 

Our goal is to design a Bayesian Optimization (BO) framework to optimize chemical reactions towards maximal reaction yield.
We assume that each possible experiment (independent of which one) takes a fixed time (i.e. 1 hour) if performed individually, but experiments can be combined in batches. The model is retrained after each batch. Model retraining also takes a fixed amount of time (e.g. 0.5 h). 

On many occasions in chemistry, batch sizes are fixed related to infrastructure specifications, for instance, the number of wells in a robot-driven HTE platform. Thus, as the time cost of running one experiment of as many as wells is the same, batching is preferred. Overall, running in large batches minimizes retraining time, but running sequentially maximizes the information before each decision is taken as the model is always trained with all the previously obtained data points.

However, in this project we will assume that batches are not perfectly parallel (i.e., the batch size is allowed to change at each iteration). Say an experiment, independent of batch size, takes at least 1 h to complete. We start with a single experiment, taking 1 hour, but add 3 additional experiments with additional time overhead. Preparing the first experiment takes most of the time. The three additional experiments will take less time, say only t<sub>add</sub> = 0.5 h each. Thus, the total time for the batch is t = 1 h (base time) + 3*0.5 h = 2.5 h.  We will consider t<sub>add</sub> to be known and use it to study its relationship with batch size.

Considering the “discounted” time of the additional experiments in a batch, and the reduced retraining time when training on multiple samples at once, how do we determine the optimal batch size at each iteration towards maximizing reaction yield in the shortest time?

**Datasets Suggested:**
- Direct arylation dataset. Shields, B. J.; Stevens, J.; Li, J.; Parasram, M.; Damani, F.; Alvarado, J. I. M.; Janey, J. M.; Adams, R. P.; Doyle, A. G. [Bayesian Reaction Optimization as a Tool for Chemical Synthesis](https://doi.org/10.1038/s41586-021-03213-y). Nature, 2021, 590, 89–96.

Other dataset suggestions (not restricted to reaction yield) are welcomed.
