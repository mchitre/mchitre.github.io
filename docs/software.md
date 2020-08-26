---
title: Public Software
layout: page
hero_height: is-fullwidth
hero_image: assets/images/head2.jpg
---

When I write software to meet my needs, I often find that those needs may be shared by others. So I try to make the software more generally applicable, and offer it to others who might have use for it. The process of generalizing helps me write better software. And usage by others improves the quality and features through user feedback & bug reports.

Here is a list of publicly available software tools & systems that I develop, maintain or largely contribute to:

### UnetStack -- an extensible underwater network stack

* [UnetStack](https://unetstack.net) -- project page, UnetStack download, documentation
* [Unet handbook](https://unetstack.net/handbook/) -- an online book providing step-by-step guidance to working with UnetStack
* [unetpy](https://pypi.org/project/unetpy/) -- Python interface to UnetStack
* [UnetSockets.jl](https://github.com/org-arl/UnetSockets.jl) -- Julia interface to UnetStack
* [unet-contrib](https://contrib.unetstack.net/) -- UnetStack community repository

### fjåge -- a general-purpose agent framework for Java/Groovy

The fjåge framework forms the core of not only UnetStack, but also several other robotics projects that I contribute to. It provides an *agent-based operating system* that makes development of modular and extensible software systems easy.

* [fjåge](https://github.com/org-arl/fjage) -- agent framework repository, documentation
* [fjåge-sentuator](https://github.com/org-arl/fjage-sentuator) -- sensor/actuator interface for agent-based systems
* [fjågepy](https://pypi.org/project/fjagepy/) -- Python interface to fjåge
* [Fjage.jl](https://github.com/org-arl/Fjage.jl) -- Julia interface to fjåge

### Python packages & tools

* [arlpy](https://pypi.org/project/arlpy/) -- Python tools for:
  * Signal processing (`arlpy.signal`)
  * Communication systems (`arlpy.comms`)
  * Beamforming & array processing (`arlpy.bf`)
  * Stable distributions (`arlpy.stable`)
  * Geographical coordinates (`arlpy.geo`)
  * Underwater acoustics (`arlpy.uwa`)
  * Underwater acoustic propagation modeling (`arlpy.uwapm`) -- Python interface to [Bellhop](https://oalib-acoustics.org)
  * Plotting utilities (`arlpy.plot`)
  * Miscellaneous common utilities (`arlpy.utils`)
* [unetpy](https://pypi.org/project/unetpy/) -- Python interface to UnetStack
* [fjågepy](https://pypi.org/project/fjagepy/) -- Python interface to fjåge

### Julia packages & tools

* [SignalAnalysis.jl](https://github.com/org-arl/SignalAnalysis.jl) -- Signal analysis toolbox
* [UnderwaterAcoustics.jl](https://github.com/org-arl/UnderwaterAcoustics.jl) -- underwater acoustic propagation modeling tools, including an interface to [Bellhop](https://oalib-acoustics.org)<br><font size="-1">(Julia versions are aimed at being compatible with automatic differentiation and probabilistic programming)</font>
* [InteractiveViz.jl](https://github.com/org-arl/InteractiveViz.jl) -- interactive visualization tools
* [jajub](https://github.com/org-arl/jajub) -- Java-Julia bridge, for Java applications with Julia components
* [UnetSockets.jl](https://github.com/org-arl/UnetSockets.jl) -- Julia interface to UnetStack
* [Fjage.jl](https://github.com/org-arl/Fjage.jl) -- Julia interface to fjåge

### Miscellaneous

* [jhwbus](https://github.com/org-arl/jhwbus) -- Java hardware bus (I2C) access
* [Jupyter IEEE paper template](https://github.com/org-arl/jupyter-ieee-paper) -- Jupyter notebook to generate fully formatted IEEE papers
