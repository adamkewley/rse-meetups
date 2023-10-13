# 1. Introduction and Tooling

> Why dedicating time to studying software engineering is useful for
> research, and where tooling can help.


## Prerequisites

If you want to participate in the interactive potions of this session, then you
will need:

- A laptop (Windows/Mac/Linux)
- Python (https://www.python.org/downloads/).
  - Make sure to add it to the system PATH when installing it, so that you can
    write `python` on the command line
- git (https://git-scm.com/downloads)
  - Make sure to add it to the system PATH when installing it (default), so
    that you can write `git` on the command line
  - You can usually use all defaults in the installer (i.e. `next` `next`
    `next`)
- Visual Studio Code (https://code.visualstudio.com/download)

> ❓ Why these:
>
> - Python is a popular ([link](https://survey.stackoverflow.co/2023/#section-most-popular-technologies-programming-scripting-and-markup-languages))
>   programming language that's easy to learn+read.
>
> - Git is the most popular version control system on the planet, and is
>   extensively used in research (e.g. it has been a long time since
>   I have encountered a non-git repository)
>
> - Visual Studio Code is requested so that all meetup participants have
>   roughly the same setup.


## Slides

Download them [here](PresentationSlides.odp)


## Presentation/Discussion: Introduction

- General schedule
- Vibe for the sessions (short bursts of lecture-type content, ideally
  interspersed with interactive segments)
- Who each participant is, why they think they need software
- Discuss unifying themes, goals, etc. that pervade each participant's
  research goals - even if they're in different research groups/fields
- Discuss which parts of those themes are common, and how research software
  engineering techniques (tools, testing, design patterns, general approach)
  might be able to help with those research goals


## Presentation: Tooling

- Why is tooling necessary? Why not just use notepad? Etc.
- Where can it be useful
- First topics: IDEs and git


## Interactive/Live: A Toy Problem for Tooling

Topics:

- Basic tooling overview
- Environment setup
- Downloading code
- Spotting ahead-of-time bugs (e.g. typos, unused vars)
- Spotting runtime bugs (debugging, REPL)

In this section, we will go through an obviously fake, small, codebase that
needs to be fixed/untangled in order to work. This is normal when working on
research codebases, and good tooling can make it much easier to see what's
going on.

The fake codebase contains examples of:

- How to get the code (e.g. via `git`)
- Bad documentation
- Bad `import`s
- Unusual package usage
- Typos
- Bad code practices that usually lead to bugs (e.g. unused variables)
- Bad maths/logic

Concretely, we'll cover:

- Setting up Visual Studio Code
- Cloneing the example
- Figure out how to get it running
- Use tooling to spot obvious coding mistakes
- Use pylint to enhance the tooling to spot other mistakes
- Run the example
- Use a debugger to understand what's going on
- Use REPL to investigate inputs vs. outputs etc.


## Version Control (basics)

- Show how all of the fixes/changes we made during the interactive session
  were automatically tracked by `git`
- Show how we can commit those changes, creating a "history" that can be
  browsed
- This isn't just useful for developers: it's useful when (e.g.) researchers
  adapt existing research code for new purposes. Knowing exactly how you got
  from A to B can be very useful (e.g. when comparing results, bugs, etc.)

The next meetup (collaboration/sharing) covers how version control is a
central part of open source and open science approaches.


## Presentation: AI and LLMs

- What they're useful for (learning, writing line-of-business scripts, etc.)
- Demo: a basic session with ChatGPT:
  - Ask it to write a script that does this or that
  - Ask it to describe each step
  - Ask it to describe some code (ideally, from the interactive session)
- Point out what it isn't so great at:
  - Creating new insights, or explaining a solution/underlying cause for
    something by combining various higher-level abstractions
  - Related: writing larger codebases with nuanced behavior, high-level design
    considerations, etc.
- Demo: GitHub Copilot


## (Bonus) Interactive: Reproduce Open Science

The idea is to try and find a small, but real, peer-reviewed research paper that
includes code and to then go through actually running it. The utility of doing
this is that we can use the tools/approaches covered with toy examples above to
see whether we can grind on real codebases; hopefully, enabling us to understand
exactly what the researchers did, any bugs, etc.

### How the Example Was Sourced

- Tried to find via Dryad. E.g. https://datadryad.org/search?f%5Bdryad_dataset_file_ext_sm%5D%5B%5D=zip&q=Computational+Biomechanics
- But most datasets on Dryad don't include code
- If I search "python" some papers do include code, but many are about pythons (the snake)
- Here are a subset of potentially-relevant datasets:

  - https://datadryad.org/stash/dataset/doi:10.7272/Q6Q81B8F doesn't have an OpenEye version or examples
  - https://datadryad.org/stash/dataset/doi:10.5061/dryad.372sq ok but requires Jupyter
  - https://github.com/tompollard/tableone/ bit too polished

- Then I tried journals. Specifically, PLOS Computational Biology: https://journals.plos.org/ploscompbiol/ .
- I went through all of September 2023's submissions: https://journals.plos.org/ploscompbiol/issue

Here are the articles/repos that were rejected:

| Article | Code | Notes |
| - | - | - |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010712) | | Close to what researchers tend to write, but will be hard to get running during a meetup |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011399) | | C++ |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011387) | [link](https://gitlab.gwdg.de/nsharma/self_loops_egt) | Jupyter |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011217) | [link](https://github.com/levinmay/adaptiveBehavior) | Jupyter |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011301) | [link](https://github.com/bartwesterman/Kanev_et_al_2023) | Shadow-requires Java and ML libraries |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010835) | [link](https://github.com/shalit-lab/ICVS) | Matlab |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010697) | [link](https://github.com/Ermentrout/ploswaves) | A repo of gzip files? |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011458) | | Julia |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011454) | | Matlab |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011446) | | Matlab |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011428) | [link](https://github.com/hzau-liulab/NABind) | Python, but an enormous amount of dependencies |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011424) | [link](https://github.com/luciagrami/EarlyEradication) | Bits of python, but many dependencies |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011457) | | Matlab |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011452) | | OSF repo of zipped data files - no code |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011427) | [link](https://zenodo.org/record/7988965) | Close to what I need, but requires conda and installs many dependencies |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011067) | [link](https://github.com/mobeets/value-rnn-beliefs) | Close, but requires a GPU and takes 48 hours to run |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011444) | [link](https://github.com/aicb-ZhangLabs/iHerd) | Close, but uses conda to install a gigantic conda environment |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011449) | [link](https://github.com/eliebouassi/classification-lymphocyte-behavior) | Promising, but no example data available because it requires a human dataset (no public ones are available?) |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011459) | [link](https://github.com/rentzi/sparseRegularizers) | Jupyter |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010867) | [link](https://github.com/Data2Dynamics/d2d) | Matlab (and massive) |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011492) | | Matlab/R |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011464) | [link](https://gitlab.lcsb.uni.lu/ICS-lcsb/energy-metabolism-model-astrocyte) | Might work, but it's quite messy |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010704) | [link](https://github.com/Collective-Logic-Lab/landau) | Requires a Wolfram account |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011406) | [link](https://github.com/mackelab/sbi-for-connectomics) | Although not easy to run in the meetups (conda, dependencies), it's good example for documenting the research in an open-science-y way |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011494) | [link](https://github.com/RuodanL/fixation_probability) | Jupyter |
|  | [link](https://github.com/ygidtu/Trackplot) | Might be a good way to introduce hacking on a larger research codebase |

Here are possible hits:

| Article | Code | Notes |
| - | - | - |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011383) | [link](https://github.com/John-king-zhou/COVID) | |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010526) | [link](https://github.com/crossley/sensory_uncertainty_fffb) | |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011067) | | |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011442) | [link](https://github.com/ZhangGroup-MITChemistry/OpenABC) | |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011460) | [link](https://github.com/enordquist/bkpred) | |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011474) | [link](https://serena-aneli.github.io/recombulator-x/) | |
| [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011472) | [link](https://github.com/ncbi/TranNet) | |
