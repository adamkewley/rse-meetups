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
> - Anaconda is popular in research. Many research projects/papers require
>   anaconda in order to (e.g.) install relevant dependencies. Anaconda also
>   includes Jupyter Notebook, which is useful because many research papers
>   in the wild provide their python code via Jupyter Notebooks.
>
> - Visual Studio Code is requested so that all meetup participants have
>   roughly the same setup.


## Slides

1. ⚠️ TODO: Work in progress ⚠️


## Table of Contents

1. ⚠️ TODO: Work in progress ⚠️


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


## Presentation: Version Control (basics)

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

## Challenge 2: A Bigger Problem

## Challenge 3: Run/Fix an Actual Research Codebase


## Notes (from session development)

### Sourcing an Example Codebase for a "Run/Fix a Real Research Codebase" Section

The idea is to try and find a small, but real, peer-reviewed research paper that
includes code and to then go through actually running it. The utility of it is
that we can use the tools/approaches covered with toy examples above to try
and grind on some of these codebases, hopefully enabling us to understand
exactly what the researchers did, any bugs, etc.

- Tried to find via Dryad. E.g. https://datadryad.org/search?f%5Bdryad_dataset_file_ext_sm%5D%5B%5D=zip&q=Computational+Biomechanics
- But most papers in Dryad don't include code
- If I search "python" some papers do include code, but many are about pythons (the snake)
- Here are a subset of potentially-relevant datasets:

  - https://datadryad.org/stash/dataset/doi:10.7272/Q6Q81B8F doesn't have an OpenEye version or examples
  - https://datadryad.org/stash/dataset/doi:10.5061/dryad.372sq ok but requires Jupyter
  - https://github.com/tompollard/tableone/ bit too polished
  - Dryad seems to mostly be for data - it sucks for code

Lets try journals, e.g. https://journals.plos.org/ploscompbiol/:

  - I went through all of the September submissions: https://journals.plos.org/ploscompbiol/issue

  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010712 close to home, but would actually be very hard to get running
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011399 - C++ :(
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011387
    - https://gitlab.gwdg.de/nsharma/self_loops_egt
    - Jupyter
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011217
    - https://github.com/levinmay/adaptiveBehavior
    - Jupyter
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011301
    - https://github.com/bartwesterman/Kanev_et_al_2023
    - but shadow-requires bash and java (+ML bs)
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010835
    - https://github.com/shalit-lab/ICVS
    - Matlab
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010697
    - https://github.com/Ermentrout/ploswaves
    - A repo of gzips?
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011458
    - Julia
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011454
    - MATLAB
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011446
    - MATLAB
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011428
    - https://github.com/hzau-liulab/NABind
    - Python, but uses an enormous amount of dependencies
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011424
    - https://github.com/luciagrami/EarlyEradication
    - Bits of python, but has many dependencies
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011457
    - OSF + matlab
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011452
    - OSF repo of zip files, which just contain ply etc. - no code
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011427
    - https://zenodo.org/record/7988965
    - Close to what I need, but uses conda and installs a bunch of stuff
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011067
    - https://github.com/mobeets/value-rnn-beliefs
    - Close, but requires 48 h runtime
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011444
    - https://github.com/aicb-ZhangLabs/iHerd
    - Sounds promising, but requires setting up a gigantic conda environment

  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011449
    - https://github.com/eliebouassi/classification-lymphocyte-behavior
    - Promising, but no data available (human dataset)

  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011459
    - https://github.com/rentzi/sparseRegularizers
    - Actually seems good, but will require participants to have Jupyter

  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010867
    - https://github.com/Data2Dynamics/d2d
    - Massive MATLAB codebase
  
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011492
    - MATLAB/R
  
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011464
    - https://gitlab.lcsb.uni.lu/ICS-lcsb/energy-metabolism-model-astrocyte
    - Possible candidate, but it's a bit too messy
  
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010704
    - https://github.com/Collective-Logic-Lab/landau
    - Depends on Wolfram
  
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011406
    - https://github.com/mackelab/sbi-for-connectomics
    - Although not easy to run in the meetups, good example for documenting the
      research in an open-science-y way

  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011494
    - https://github.com/RuodanL/fixation_probability
    - Jupyter, but seems ok otherwise

  - https://github.com/ygidtu/Trackplot
    - Bigger: might be a good way to introduce hacking on a larger codebase  

hits:

- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011383 --> https://github.com/John-king-zhou/COVID
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010526 --> https://github.com/crossley/sensory_uncertainty_fffb
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011067
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011442 --> https://github.com/ZhangGroup-MITChemistry/OpenABC
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011460 --> https://github.com/enordquist/bkpred
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011474 --> https://serena-aneli.github.io/recombulator-x/
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011472 --> https://github.com/ncbi/TranNet


## Content Topics

General concepts that need to be discussed/delivered/shown/experimented with etc:

- IDEs vs text editors
- REPL
- Command line
- Basic git usage
- Github/documentation (it's obvious, but worth pointing out)
- LLMs (ChatGPT/GH Copilot)

## Delivery Ideas

- Provide a "messy" codebase that participants have to try and unravel using some
  of the tools shown
- Have us work on a toy problem (e.g. sort an array or something basic) and then
  show how the tools complement the workflow
- Present a harder problem (e.g. download data from this API and compute+plot the
  average number of downloads etc.) and then show how all of these tools, when
  combined with a little bit of AI, can get something working very quickly

## Prerequisites

- Try to bring a laptop
- Try to have Visual Studio Code already installed
- Try to have git already installed
- (maybe the AI/LLM stuff can be shown by the presenter, so that participants
   don't all have to get OpenAI/GitHub accounts)
