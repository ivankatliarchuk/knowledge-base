---
title: system data design
summary: Design Data of the System
authors:
- Ivan K
tags: ["architecture", "design", "system", "data"]
date: 2021-03-8
some_url:
published: true
---

!!! note "data design"
    The document contains information related to data design.

## Question to ask

- What Data Groups exist in the system.. how large are they
- When will the data be accessed
- What access patterns will the data have
- How will the data grow over time
- Will all data in the time series have equal access
- What opearation will be run against the data
- Are different perspectives on data needed
- What are the batch processing needs
- Does the system have any real-time needs
