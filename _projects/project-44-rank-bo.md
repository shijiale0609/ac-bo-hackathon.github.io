---
number: 44 # leave as-is, maintainers will adjust
title: RBBO - rank-based Bayesian optimization
topic: general
team_leads:
  - Gary Tom (University of Toronto) @gkwt

# Comment these lines by prepending the pound symbol (#) to each line to hide these elements
contributors:
  - Samantha Corapi (University of Toronto) @samanthacorapi
  - Stanley Lo (University of Toronto) @stanlo229

github: gkwt/rank-bo
youtube_video: c84Sd2IwMAQ

---

Applying the use of ranking models for Bayesian optimization discovery of materials based libraries. Ranking models use a form of metric learning that aims to sort inputs rather than directly predicting a regressive label. This changes the structure of the loss (comparing pairs and lists of inputs) and allows the surrogate to focus on the relative value of the properties, which is often what we are most interested in if we are maximizing some property in the BO campaign.

Here we will compare the performance of a typical regression model, and a ranking model in a BO campaign for screening virtual libraries of chemical compounds. We will also compare their performances when applied to "rougher" feature spaces.

References:
- Graff, David E., Eugene I. Shakhnovich, and Connor W. Coley. "Accelerating high-throughput virtual screening through molecular pool-based active learning." Chemical science 12.22 (2021): 7866-7881.
- Aldeghi, Matteo, et al. "Roughness of molecular property landscapes and its impact on modellability." Journal of Chemical Information and Modeling 62.19 (2022): 4660-4671.
