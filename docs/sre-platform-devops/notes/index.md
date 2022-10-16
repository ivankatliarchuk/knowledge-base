---
title: sre notes
summary: sre notes
authors: ["ivan k"]
tags: ["sre", "notes", "google", "courses", "sre:notes"]
date: 16-Oct-2022
published: true
---

# SRE Notes

> If you’re building a system from scratch, make sure that SLIs and SLOs are part of your system requirements. If you already have a production system but don’t have them clearly defined, then that’s your highest priority work. Do profit analysis and business objectives to define you SLI.

## DevOps Vs SRE

**DevOps (is a philosophy)**

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

> 100% reliability is almost always the wrong target. It becomes much, much more expensive to make systems even more reliable, so there’s some point where the marginal cost of reliability exceeds the marginal value of reliability.

### SLO

**Process Overview**

1. List out critical user journeys and order them by business impact.
1. Determine which metrics to use as service-level indicators (SLIs) to most accurately track the user experience.
1. Determine SLO target goals and the SLO measurement period.
1. Create SLI, SLO, and error budget consoles.
1. Create SLO alerts.

**Characteristics**

- Just high enough to keep customers happy
- Ambitious but achievable

### Error Budgets

> But how do you know how much headroom you have left before you violate your SLOs, and what can you do about it? Well, we use something known as an error budget to figure this out. An error budget is basically the inverse of availability, and it tells us how unreliable your service is allowed to be. If your SLO says that 99.9 percent of requests should be successful in a given quarter, your error budget allows 0.1 percent of requests to fail. This unavailability can be generated as a result of bad pushes by the product teams, planned maintenance, hardware failures, et cetera. Let's look at error budgets in terms of time. 0.1 percent unavailability times 28 days in the four-week window, times 24 hours in a day, times 60 minutes in an hour is equal to 40.32 minutes of downtime per month. This is just about enough time for your monitoring systems to surface an issue, and for a human to investigate and fix it. And that only allows for one incident per month. As you can see, that's not a lot of time at all. When you come up with your SLOs, you and your product teams, and ideally your leadership are also agreeing not to spend all of this error budget. You want to find a happy medium where you can still have development velocity and user happiness without burning through your error budget. Think of the budget as a household budget. It's there to be spent on things you want, such as rolling out new software versions, which might break, releasing new features, plan downtime, inevitable failure in hardware, networks, power, et cetera. You shouldn't overspend it, but that's not to say you can't spend it at all. If you look at your error budget for your SLOs over standard time period like 28 days, you may see that you've used 90 percent of your error budget. In this case, 36.28 minutes of unavailability a month. No need to panic. In general, you shouldn't care whether you've used 10 percent, 25 percent, or 70 percent of your error budget in the past 28 days. But you should care if you've used 110 percent. If you don't have the budget, you need to take action to make your service more reliable, and protect users from additional unavailability. There are many benefits to using error budgets. Because you and your product teams have to maintain their budget, it is a common incentive for your developers and your reliability engineers. It's shared between the two teams and helps strike a balance between innovation and reliability. It allows your Dev team to manage the risks themselves, and self-regulate by figuring out what to spend the error budget on such as more changes, faster pushes, or riskier features. And unrealistic reliability goals become unattractive because they dampen the velocity of innovation without providing benefit.

**Benefits**

- Common incentives for Dev and SREs
