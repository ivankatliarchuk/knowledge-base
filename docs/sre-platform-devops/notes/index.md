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

> The application cannot surpass the SLA of its runtime (eg. EC2, Lambda, Google Compute Engine, etc).

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

While the Service Level Agreement (SLA) is the commitment toward the end users, the Service Level Objective (SLO) is more of a guide for the team behind a service and serves as a guardrail for their deployment using Error Budgets.

> But how do you know how much headroom you have left before you violate your SLOs, and what can you do about it? Well, we use something known as an error budget to figure this out. An error budget is basically the inverse of availability, and it tells us how unreliable your service is allowed to be. If your SLO says that 99.9 percent of requests should be successful in a given quarter, your error budget allows 0.1 percent of requests to fail. This unavailability can be generated as a result of bad pushes by the product teams, planned maintenance, hardware failures, et cetera. Let's look at error budgets in terms of time. 0.1 percent unavailability times 28 days in the four-week window, times 24 hours in a day, times 60 minutes in an hour is equal to 40.32 minutes of downtime per month. This is just about enough time for your monitoring systems to surface an issue, and for a human to investigate and fix it. And that only allows for one incident per month. As you can see, that's not a lot of time at all. When you come up with your SLOs, you and your product teams, and ideally your leadership are also agreeing not to spend all of this error budget. You want to find a happy medium where you can still have development velocity and user happiness without burning through your error budget. Think of the budget as a household budget. It's there to be spent on things you want, such as rolling out new software versions, which might break, releasing new features, plan downtime, inevitable failure in hardware, networks, power, et cetera. You shouldn't overspend it, but that's not to say you can't spend it at all. If you look at your error budget for your SLOs over standard time period like 28 days, you may see that you've used 90 percent of your error budget. In this case, 36.28 minutes of unavailability a month. No need to panic. In general, you shouldn't care whether you've used 10 percent, 25 percent, or 70 percent of your error budget in the past 28 days. But you should care if you've used 110 percent. If you don't have the budget, you need to take action to make your service more reliable, and protect users from additional unavailability. There are many benefits to using error budgets. Because you and your product teams have to maintain their budget, it is a common incentive for your developers and your reliability engineers. It's shared between the two teams and helps strike a balance between innovation and reliability. It allows your Dev team to manage the risks themselves, and self-regulate by figuring out what to spend the error budget on such as more changes, faster pushes, or riskier features. And unrealistic reliability goals become unattractive because they dampen the velocity of innovation without providing benefit.

**Characteristics**

- The inverse of an SLO. Error budgets are the amount of time your system can be down. So if your service has an availability SLO of 99.9% in 28 days, then you have an error bud
- A quantitative metric for service unreliability

**Benefits**

- Common incentives for Dev and SREs. Error budgets are a great common incentive for your development and SRE teams to help strike a balance between reliability and development velocity.  They also allow teams to self-regulate and manage the risks they take with new features.
- Dev teams can self-manage risk
- Unrealistic goals become unattractive
- Error budgets help to balance development velocity and reliability.

**Align Incentives**

- Devs can take risks and push more quickly
- SRE team can work more proactively

**Advanced Techniques**

- Dynamic release cadence. `Based on remaining error budget`
- "Rainy Day" fund. `Covers unexpected events
- Error budget-based alerts. `Exhaustion rate drives alerting`
- "Silver bullets". `For critical new features`

**Improve Reliability**

- Reducing detection time (TTD time to detect)
- Reducing repair time (time to resolution )
  * Develop a playbook
  * Parse and collate server debug logs
- Reducing impact % users/functionality (canary releases)
- Reducing frequency (time to failure TTF)

> By canarying changes and incrementing the percentage of effected regions, you release change into production gradually. This allows you to detect and respond to failures before your entire service has been impacted.

> SLO violations can be bugs in the product, in the code, or even in the SLO itself, but it is always a bug somewhere. Postmortems can highlight what those bugs are, and create action items to get them fixed.

## Choosing a Good SLI

- It is close approximation of the user experience. We want to measure the user experience as directly as possible. We assume that when that experience is poor enough, we are not meeting our users' expectations of service reliability and they are therefore unhappy with our service.
- It shows long-term trends clearly. A smoothed-out signal over a long time horizon is more valuable for an SLI, because these metrics tend to have lower variance and higher signal-to-noise ratio.
- System metrics, correlations in between things like thread pool fulness, or request queue length and outages.
- Has predictable relationships with user happiness.
- Shows service is working as users expecting it to.
- SLI expressed as `Good Events/Valid Events`
- Aggregated over a long time horizon.

### SLI Framework

- SLIs fail between 0 and 100%
- Consistency makes building common tooling easier

### Request/Response SLI

- Availability
  * The proportion of minutes a virtual machine was booted and accessible
- Latency
  * The proportion of valid requests served faster then a threshold
  * The proportion of work-queue tasks that are completed faster than a threshold
- Quality
  * The proportion of valid requests served without degrading quality

### Why do you think the lower metric is better for use as an SLI than the upper one?

- makes the relationship with user happiness unpredictable
- makes it hard to measure the user experience accurately
- makes it hard to set a meaningful static SLO target
- metric deterioration correlates with outage
- it can set as a thresholds

## Ways of measuring SLI

- Requests Logs
- Application metrics
- Frond-end infra metrics
- Synthetic clients
- Client-side instrumentation
