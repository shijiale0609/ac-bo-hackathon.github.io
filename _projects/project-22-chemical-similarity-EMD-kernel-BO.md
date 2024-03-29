---
number: 22 # leave as-is, maintainers will adjust
title: Chemical Similarity-Informed Earth Mover’s Distance Kernel Bayesian Optimization for Predicting the Properties of Molecules and Molecular Mixtures
topic: real-world

team_leads:
  - Jiale Shi (<a href=https://github.com/shijiale0609> shijiale0609 </a>) (Massachusetts Institute of Technology)
  - [Dandan Tang](https://github.com/DandanTang0) (University of Virginia)
  - [Qianxiang Ai](https://github.com/qai222) (Massachusetts Institute of Technology)
  - [Christoph Griehl](https://github.com/dionyce) (Max Planck Institute for Dynamics of Complex Technical Systems)
    
#contributors:

# github: AC-BO-Hackathon/<your-repo-name>
github: AC-BO-Hackathon/project-chemical-similarity-EMD-kernel-BO
youtube_video: I179UR8P054

---
The default distance function used in the kernel functions of Gaussian Processes is the Euclidean distance. The configuration of these kernels significantly influences the model's performance. In this work, we will develop a series of chemical similarity-informed custom kernels for Bayesian Optimization to predict the properties of molecules. Additionally, we will compare how different chemical similarity functions can affect the performance of Bayesian Optimization. Beyond pure components, we will employ the earth mover's distance to define the pairwise distance of mixtures from the pairwise distance of individual components, thereby extending this method to predict the properties of chemical mixtures.

Reference:

1. Moss, Henry B., and Ryan-Rhys Griffiths. "Gaussian process molecule property prediction with flowmo." arXiv preprint arXiv:2010.01118 (2020).
2. Hargreaves, Cameron J., et al. "The earth mover’s distance as a metric for the space of inorganic compositions." Chemistry of Materials 32.24 (2020): 10610-10620.
