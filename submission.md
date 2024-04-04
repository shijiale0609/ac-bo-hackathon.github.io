---
title: Submit a Project
menu_title: Submission
menu_icon: cloud-arrow-up
---

Project proposals are submitted by hackathon participants, where the submitter intends to lead that project and form a team (or work on it solo) during the hackathon. Some people might already have a team in mind while others might add team members after submitting the proposal. Likewise, there will be people who want to join an existing team instead of proposing their own project. The [slack channel](_/../agenda.md) is the primary communication channel for brainstorming project ideas and forming teams.

See below for the project topics and instructions on how to submit a project proposal.

## Topics

While a list of topics is provided, we are open to new ideas. If you have a project in mind that doesn't fit into one of the topics below, you are welcome and encouraged to submit a project proposal for it.

### Topic 1: Applying Algorithms to Benchmark Tasks (`benchmark-task`)

We provide a set of prepackaged benchmark tasks and instructions, and your job will be to choose a package or algorithm and apply it to task(s) of your choice. The tasks will cover a broad range of both optimization complexity and application domains. Submissions that demonstrate algorithm performance on the hackathon-supplied benchmarks falls under the `benchmark-task` topic. Projects focused on comparing algorithm performance on existing benchmarks that aren't part of the hackathon set, but not necessarily on creating an entirely new benchmark, can go into either the `benchmark-task` or `general` topic.

The benchmark functions listed below have been prepared in advance of the hackathon. Each of these is hosted on the [Acceleration Consortium's Hugging Face organization](https://huggingface.co/AccelerationConsortium) and can be programmatically accessed via the "Use with API" instructions at the bottom of each benchmark function's webpage.

| Name | Description |
| ---- | ---- |
| [Branin function](https://huggingface.co/spaces/AccelerationConsortium/branin) | A 2D analytic function used for optimization benchmarking |
| [Hybrid Space Toy](https://huggingface.co/spaces/AccelerationConsortium/Hybrid_Space_Toy) | A simple function with continuous and categorical parameters |
| [Process Optimization Toy](https://huggingface.co/spaces/AccelerationConsortium/Process_Toy) | A simple continuous function with many irrelevant parameters |
| [Hartmann-4](https://huggingface.co/spaces/AccelerationConsortium/TransferLearning4D) | The Hartmann function in 4 dimensions posed as a transfer learning task |
| [Direct Arylation](https://huggingface.co/spaces/AccelerationConsortium/Direct_Arylation) | Optimize yield as a function of reaction conditions |
| [Cross Coupling Reactions of Aryl Halides](https://huggingface.co/spaces/AccelerationConsortium/ArylHalides) | Optimize yield based on combinations of a base, ligand, additive, and aryl halide. |
| [Advanced Optimization](https://huggingface.co/spaces/AccelerationConsortium/crabnet-hyperparameter) | A high-dimensional, multi-objective, multi-fidelity function. |

### Topic 2: Developing New Benchmarks (`benchmark-dev`)

Ideally, these tasks will be representative of real-world problems in chemistry and materials science. While remotely accessible automated experiments would be the gold standard, the more pragmatic benchmark tasks typically include surrogate modeling. The new benchmark tasks should lean towards real-world conditions in terms of optimization problem type (objectives, fidelities, constraints) and/or relevance towards chemistry and materials applications (e.g., molecules, materials, reactions, etc.). Ideally, these benchmark tasks will be hosted on Hugging Face spaces, similar to the tasks from `benchmark-task`. See the Hugging Face spaces section of the [resources page](_/../resources.md).

### Topic 3: Creating Instructional Tutorials (`tutorial`)

We have a set of topics in Bayesian optimization attached with the planned [AC data science microcourse](https://ac-microcourses.readthedocs.io/en/latest/courses/data-science/overview.html), and your job will be to create a tutorial that introduces the topic conceptually and provides a hands-on example. Topics other than the ones listed are also fair game. These are meant to be "gentle introduction" tutorials which assume beginner Python knowledge and beginner Bayesian optimization knowledge (see [resources](_/../resources.md) for more details on what is meant by "beginner").

### Topic 4: Real-world Chemistry and Materials Tasks (`real-world`)

The hackathon is open to proposals for real-world optimization tasks in chemistry and materials science. This will involve providing beginner-friendly background knowledge on the impact of the application, existing solutions, and the science behind it. This is particularly well-suited for those who would prefer to contribute in a non-coding context, as it allows domain experts to formulate high-impact research tasks from an optimization perspective. It will also involve providing rigorous details around the optimization problem, including search space (tunable parameters + constraints), objectives, experimental equipment, reagants, and standard operating procedures. These should be well-defined problems that *can* and *should* be tackled with Bayesian optimization, but have not yet been tackled successfully or adequately. If you do not have a background in Bayesian optimization, it is highly recommended that you watch the recording of the Accelerate '23 [Gentle Introduction to Bayesian Optimization](https://youtu.be/IVaWl2tL06c) training workshop in preparation for projects in this category.

### Topic 5: General (`general`)

This category is for projects that don't fit into the special topics listed above, but generally fall within the topic of Bayesian optimization for the physical sciences. Projects in this context are welcome! If you're unsure about a project, feel free to reach out to [sterling.baird@utoronto.ca](mailto:sterling.baird@utoronto.ca).

## Project initialization

As a teamleader, to initialize your project[<sup>(?)</sup>][faq]{:title="Can I participate in multiple projects?"}, please follow these steps:

1. Use [this link to create a new file](https://github.com/AC-BO-Hackathon/ac-bo-hackathon.github.io/new/main/_projects) in a fork of the hackathon repository named `project-<your-team-name>.md`. For example, if your team name is "Bayes Bandits", the file should be named `project-bayes-bandits.md`. The team name can be whatever you'd like (e.g., project name, GitHub username, institution).

![project submission](../assets/project-submission.png)

1. Copy the template from below into the file and fill in the title, topic, team leads, and contributors sections. Topic can be one of `benchmark-task`, `benchmark-dev`, `tutorial`, `real-world`, and `general`, per the topics listed above.
2. Submit a pull request to the hackathon repository with the title "Add project \<your-team-name\>" and if applicable, tag your team members in the pull request description using the <code>@</code> symbol followed by their GitHub username. For example, <code>@sgbaird</code>. This can be updated later if needed.
3. Once the pull request is merged, your project will appear on [the projects page](_/../projects.md)

```yaml
---
number: 1 # leave as-is, maintainers will adjust
title: Project 1 title
topic: <topic-name>
team_leads:
  - Project lead 1 (Institution 1) @gh-username1
  - Project lead 2 (Institution 2) @gh-username2

# Comment these lines by prepending the pound symbol (#) to each line to hide these elements
contributors:
  - Contributor 1 (Institution 1) @gh-username3
  - Contributor 2 (Institution 2) @gh-username4

# github: AC-BO-Hackathon/<your-repo-name>
# youtube_video: <your-video-id>

---

Project 1 description

References:

```

Here is an example of a filled-in project file called `project-bayes-bandits.md` for the "Bayes Bandits" team for a submission to the `general` topic. Please replace any colons (`:`) with hyphens (`-`) in the title, if applicable, and ensure that the filename ends with the Markdown (`.md`) extension. Also, ensure that you include the first line with `---` (required for the webpage to build correctly). The references section is optional. Please include links in Markdown format where appropriate.

```yaml
---
number: 1 # leave as-is, maintainers will adjust
title: Investigation of Bandit Optimization for Composite Materials Design
topic: general
team_leads:
  - Jane Doe (University of Invention) @jdoe
  - John Smith (Institute of Discovery) @john-smith

contributors:
  - Larry Lab (University of Invention) @labamation
  - David Data (University of Science) @data4everyone
  - Rachel Research (Institute of Discovery) @researchlife

# github: AC-BO-Hackathon/<your-repo-name>
# youtube_video: <your-video-id>

---

This project will investigate the application of bandit optimization to the design of composite materials. We will focus on the optimization of the mechanical properties of the composite materials, such as strength, stiffness, and toughness as a function of the fiber types and matrix materials. We will compare the performance of bandit optimization with the performance of Bayesian optimization using featurization tactics for this highly discrete space.

References:

1. Aleksandrs Slivkins (2019), ["Introduction to Multi-Armed Bandits"](http://dx.doi.org/10.1561/2200000068), Foundations and Trends in Machine Learning: Vol. 12: No. 1-2, pp 1-286.

2. Dimmery, D., Bakshy, E., & Sekhon, J. (2019). [Shrinkage Estimators in Online Experiments](https://doi.org/10.48550/ARXIV.1904.12918). arXiv.
```

The project templates are anticipated for release during mid-March. Once these are ready you, team leaders can follow the instructions below:

1. Accept the GitHub Classroom invitation to a topic above (see also [resources](_/../resources.md))
2. Create a new team in the GitHub Classroom interface
3. Have your team members click on the same GitHub Classroom invitation link that you used and join the team you created.
4. Open a new pull request to modify your project file. Replace `<your-repo-name>` with the GitHub repository name that was created by GitHub Classroom for you using the corresponding project template link. For example, if your team name is "Bayes Bandits" and the template is called "benchmarking", the repository will be named `benchmarking-bayes-bandits`, and the `github` field should be `AC-BO-Hackathon/project-X-bayes-bandits`. You are also welcome to use your own repository hosted somewhere else on GitHub (e.g., `sgbaird/honegumi`) You will also need to uncomment the line by removing the `#`. For example:

```markdown
# github: AC-BO-Hackathon/<your-repo-name>
```
would be replaced with:
  
```markdown
github: AC-BO-Hackathon/benchmarking-bayes-bandits
```

If the submission instructions from above are daunting, you are welcome to submit your project proposal by email to [sterling.baird@utoronto.ca](mailto:sterling.baird@utoronto.ca). Please include "AC BO Hackathon Project Proposal" in the subject line. We will create the project file and corresponding pull request for you.

## Project showcase and judging

The closing session on {{ site.event_close_date }} is for sharing with peers and judges and getting feedback while everyone is still around on the Gather Town event space. This will also conclude the synchronous portion of the hackathon. Participants will prepare a poster image, a link to a video, or an embedded website to be showcased in Poster Room A from the Gather Town space (see [agenda](_/../agenda.md)). One of these objects will be placed into an interactive "poster" object for your project by an organizer. The item (image or link) should be supplied to the organizers 15 min prior to the showcase by posting in the slack channel or DM'ing Sterling Baird. See the [FAQ][faq]{:title="How do I prepare for the project showcase?"} for more info.

## End of hackathon

To ensure a dynamic and engaging submission process, we ask that all hackathon teams submit their final projects through social media (e.g., Twitter, LinkedIn, YouTube) and then link to this in their project file. By sharing your work with a broader audience, you’ll help to promote groundbreaking research in materials science and chemistry while inspiring others to contribute to the field. This step is also a requirement for teams wishing to contribute to the scholarly article.[<sup>(?)</sup>][faq]{:title="What is required for me to participate in the scholarly article?"}

Here are the guidelines for submitting your project:

1. Create a concise video presentation (2 minutes or less) summarizing your team’s project, highlighting its applications in materials science and chemistry, and showcasing your project outputs.

2. Upload your video to YouTube (unlisted is fine) and post about it on social media (e.g., LinkedIn, X)

3. Submit a pull request to update your project file with the YouTube video ID (e.g., `IVaWl2tL06c` for `https://youtu.be/IVaWl2tL06c`) and a sentence with a link to the social media post. For example, for the YouTube video, you would replace the following two lines:

```markdown
github: AC-BO-Hackathon/bayes-bandits
# youtube_video: <your-video-id>
```
with:
```
github: AC-BO-Hackathon/bayes-bandits
youtube_video: IVaWl2tL06c
```

For the social media post, you would add a sentence like `Check out our social media post on [LinkedIn](<your link here>)!` before the References section. For example:

```markdown
This project will investigate the application of bandit optimization to the design of composite materials. We will focus on the optimization of the mechanical properties of the composite materials, such as strength, stiffness, and toughness as a function of the fiber types and matrix materials. We will compare the performance of bandit optimization with the performance of Bayesian optimization using featurization tactics for this highly discrete space.

References:
1. Aleksandrs Slivkins (2019), "Introduction to Multi-Armed Bandits", Foundations and Trends in Machine Learning: Vol. 12: No. 1-2, pp 1-286. http://dx.doi.org/10.1561/2200000068
2. Dimmery, D., Bakshy, E., & Sekhon, J. (2019). Shrinkage Estimators in Online Experiments. arXiv. https://doi.org/10.48550/ARXIV.1904.12918
```

would change to (replace `<your_link_here>` with your actual link, without the angle brackets):

```markdown
This project will investigate the application of bandit optimization to the design of composite materials. We will focus on the optimization of the mechanical properties of the composite materials, such as strength, stiffness, and toughness as a function of the fiber types and matrix materials. We will compare the performance of bandit optimization with the performance of Bayesian optimization using featurization tactics for this highly discrete space.

Check out our social media post on [LinkedIn](<your link here>)!

References:
1. Aleksandrs Slivkins (2019), "Introduction to Multi-Armed Bandits", Foundations and Trends in Machine Learning: Vol. 12: No. 1-2, pp 1-286. http://dx.doi.org/10.1561/2200000068
2. Dimmery, D., Bakshy, E., & Sekhon, J. (2019). Shrinkage Estimators in Online Experiments. arXiv. https://doi.org/10.48550/ARXIV.1904.12918
```

This pull request will be considered your final submission. Again, if you find this process daunting, you are welcome to instead send your link by email to [sterling.baird@utoronto.ca](mailto:sterling.baird@utoronto.ca). Please include "AC BO Hackathon Final Submission" in the subject line. We will update the project file and create corresponding pull request for you. If you don't want to post it to YouTube, you can also post the video directly to LinkedIn or Twitter. In this case, please remove the `youtube_video: ...` line and mention that the social media post contains the video.

[faq]: {{ site.baseurl }}{% link faq.md %}
