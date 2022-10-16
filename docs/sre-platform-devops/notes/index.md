---
title: sre notes
summary: sre notes
authors: ["ivan k"]
tags: ["sre", "notes", "google", "courses"]
date: 16-Oct-2022
published: true
---

# SRE Notes

> If you’re building a system from scratch, make sure that SLIs and SLOs are part of your system requirements. If you already have a production system but don’t have them clearly defined, then that’s your highest priority work. Do profit analysis and business objectives to define you SLI.

## DevOps Vs SRE

**DevOps (is a filosofy)**

- Reduce organization silos. Breaking down barriers across teams
- Accept failure as normal.
- Implement Gradual Change
- Leverage Tooling & Automation
- Measure everything

**SRE (a way to do things)**
- Share ownership in production with developers
- Blameless postmortems, to make sure exact same failure happens only once
- Reduce cost of failure e.g. work with engineering teams
- Understand the toil and automate the job away
- Measure toil and reliability
- Sustain system reliability
    - reactive , incident response and well training
    - proactive engineering; removing bottleneck, isolating failure domain, automating processes

**SRE Concepts**

- The concept of SRE starts with the idea that metrics should be closely tied to business objectives.

**SRE Reliability Principles**

- Communicate clearly how services intended to behave e.g. 3 tiers?? Exposing SLOs and trading off reliability against features
- Reliability is the most important feature
- Users decides on reliability not a monitoring solution
- Well engineering platform and ever increasing reliability BCP e.g. software 99.9%, Ops 99.99%, business 99.999%

## SLI

- Availability (how many requests are succeeding)
- Latency (i.e., how long a request takes)
- Error rates
- Throughput, correctness, data freshness

## Site Reliability Engineering: Measuring and Managing Reliability (Google Cloud)

[Coursera: sre](https://www.coursera.org/learn/site-reliability-engineering-slos/home/week/1)

- The Happiness Test states that "Services need target SLOs that capture the performance and availability levels that, if barely met, would keep the typical customer happy."
- SLAs are external promises to customers and must come with consequences.
- SLOs are internal promises (as opposed to being explicitly shared with customers), and they are directly tied to customer expectations.

> If you're targeting four nines, you can only have four minutes of complete down time in that same window. This isn't enough time to loop in a human, so your system has to be able to detect and self-heal complete outages to meet this target sustainably. If you want humans involved in an incident response, you will have to architect your system so that change propagates in waves, and no more than a certain fraction of the system is exposed to a change at once. So this way, the humans still have time to react.

> One that enables Google to quickly determine when product changes have impacted its customers, and one that allows customers to reason about the expected availability of those products.

### SLO process overview

1. List out critical user journeys and order them by business impact.
1. Determine which metrics to use as service-level indicators (SLIs) to most accurately track the user experience.
1. Determine SLO target goals and the SLO measurement period.
1. Create SLI, SLO, and error budget consoles.
1. Create SLO alerts.
