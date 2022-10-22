---
title: google notes
summary: google notes
authors: ["ivan k"]
tags: ["sre", "notes", "google", "platform"]
date: 20-Oct-2022
published: true
source:
- https://cloud.google.com/blog/products/devops-sre/sre-at-google-our-complete-list-of-cre-life-lessons
- https://sre.google/sre-book/dealing-with-interrupts/
- https://sre.google/sre-book/evolving-sre-engagement-model/
- https://sre.google/sre-book/introduction/
---

# Google Notes

> “Rollback early, rollback often.” Try to move your service towards this philosophy, and you’ll reduce the Mean Time To Recover of your service.

> “Canary your rollouts.” No matter how good your testing and QA, you'll find that your binary releases occasionally have problems with live traffic. An effective canarying strategy and good monitoring can reduce the Mean Time To Detect these problems, and dramatically reduce the number of affected users.

> Ideally, your team has a stack that is multihomed and provisioned in such a way that you have at least one instance you can divert from live traffic and temporarily loan to a learning exercise. Alternatively, you might have a smaller, but still fully featured, staging or QA instance of your stack that can be borrowed for a short time. If possible, subject the stack to synthetic load that approximates real user/client traffic, in addition to resource consumption, if possible.

> The opportunities for learning from a real production system under synthetic load are abundant. Senior SREs will have experienced all sorts of troubles: misconfigurations, memory leaks, performance regressions, crashing queries, storage bottlenecks, and so forth. In this realistic but relatively risk-free environment, proctors can manipulate the job set in ways that alter the behavior of the stack, forcing new SREs to find differences, determine contributing factors, and ultimately repair systems to restore appropriate behavior.

> As an alternative to the overhead of asking a senior SRE to carefully plan a specific type of breakage that the new SRE(s) must repair, you can also work in the opposite direction with an exercise that may also increase participation from the entire team: work from a known good configuration and slowly impair the stack at selected bottlenecks, observing upstream and downstream efforts through your monitoring.

> How you apply these practices is up to you, but the charge is clear: as SRE, you have to scale your humans faster than you scale your machines.

** Cognitive Flow **

> People enjoy performing tasks they know how to do. In fact, executing such tasks is one of the clearest paths to cognitive flow. Some SREs are on-call when they reach a state of cognitive flow. It can be very fulfilling to chase down the causes of problems, work with others, and improve the overall health of the system in such a tangible way

> On the other hand, when a person is concentrating full-time on interrupts, interrupts stop being interrupts. At a very visceral level, making incremental improvements to the system, whacking tickets, and fixing problems and outages becomes a clear set of goals, boundaries, and clear feedback: you close X bugs, or you stop getting paged. All that’s left is distractions. When you’re doing interrupts, your projects are a distraction. Even though interrupts may be a satisfying use of time in the short term, in a mixed project/on-call environment, people are ultimately happier with a balance between these two types of work. The ideal balance varies from engineer to engineer. It’s important to be aware that some engineers may not actually know what balance best motivates them (or might think they know, but you may disagree).

> **Polarizing time** means that when a person comes into work each day, they should know if they’re doing just project work or just interrupts. Polarizing their time in this way means they get to concentrate for longer periods of time on the task at hand. They don’t get stressed out because they’re being roped into tasks that drag them away from the work they’re supposed to be doing.

** Notes **

> For any given class of interrupt, if the volume of interrupts is too high for one person, add another person. This concept most obviously applies to tickets, but can potentially apply to pages, too—the on-call can start bumping things to their secondary, or downgrading pages to tickets.

> A person should never be expected to be on-call and also make progress on projects (or anything else with a high context switching cost).

> Your team should conduct a regular scrub for tickets and pages, in which you examine classes of interrupts to see if you can identify a root cause. If you think the root cause is fixable in a reasonable amount of time, then silence the interrupts until the root cause is expected to be fixed.

> Remember:  Your team sets the level of service provided by your service.  It’s OK to push back some of the effort onto your customer

> Remember that your job is to make the service work, not to shield the development team from alerts.

> To give acceptable on-call support for a component, you should at least know the consequences when it breaks and the urgency needed to fix problems.

> After scoping the dynamics and pain points of the team, lay the groundwork for improvement through best practices like postmortems and by identifying sources of toil and how to best address them.

> If you find yourself on a team without SLOs, first read Service Level Objectives, then get the tech leads and management in a room and start arbitrating.

> The preceding detailed discussions often lead to actions that SRE needs to take—fix this, monitor that, develop a subsystem to do the other. Track these improvements just as they would be tracked in any other meeting: assign action items to people and track their progress.

> Work done by SREs must be highly visible and sufficiently reviewed by the development team to ensure effective knowledge sharing. SREs should essentially work as a part of the development team, rather than an external unit.

** Issues needs triage **

> Common alerts that aren't diagnosed by either the dev team or SREs. Such alerts are frequently triaged as transient, but still distract your teammates from fixing real problems. Either investigate such alerts fully, or fix the alerting rules.

> An issue that probably should have paged, but didn't. In these cases, you should probably fix the monitoring so that such events do trigger a page. Often you encounter the issue while you're trying to fix something else, or it's related to a metric you're tracking but for which you haven't got an alert.

> An issue that is not pageable but requires attention, such as low-impact data corruption or slowness in some non-user-facing dimension of the system. Tracking reactive operational work is also appropriate here. These alerts should be removed, because they create extra noise that distracts engineers from issues that do merit attention.

** Prioritization **

> SRE teams sometimes fall into ops mode because they focus on how to quickly address emergencies instead of how to reduce the number of emergencies. After you've learned enough about the service to ask hard questions about its design and deployment, spend some time prioritizing various service outages according to their impact on the team's stress levels.

### The SRE Engagement Model

SRE seeks production responsibility for important services for which it can make concrete contributions to reliability. SRE is concerned with several aspects of a service, which are collectively referred to as _production_. These aspects include the following:

- System architecture and interservice dependencies
- Instrumentation, metrics, and monitoring
- Emergency response
- Capacity planning
- Change management
- Performance: availability, latency, and efficiency

When SREs engage with a service, we aim to improve it along all of these axes, which makes managing production for the service easier.

### Onboarding

> We've discussed in most of the rest of this book what happens when SRE is already in charge of a service. Few services begin their lifecycle enjoying SRE support, so there needs to be a process for evaluating a service, making sure that it merits SRE support, negotiating how to improve any deficits that bar SRE support, and actually instituting SRE support. We call this process onboarding. If you are in an environment where you are surrounded by a lot of existing services in varying states of perfection, your SRE team will probably be running through a prioritized queue of onboardings for quite a while until the team has finished taking on the highest-value targets.

> Onboarding involves a progressive transfer of responsibilities and ownership of various production aspects of the service, including parts of operations, the change management process, access rights, and so forth.

How to prioritize onboarding

- Prioritization queue of onboardings `Make take a while`
  + With growing use of the service and the growth of the revenue coming from the service
- Wait for a bug or SLO violation. `the earlier the bug is found, the cheaper it is to fix`
  + However, the main limitations of the PRR Model stem from the fact that the service is launched and serving at scale, and the SRE engagement starts very late in the development lifecycle.
- Onboard service on a platform. `probably the bets way`

Perhaps the `best way`, is to short-circuit the process by which specially created systems with lots of individual variations end up "arriving" at SRE's door. Provide product development with a platform of SRE-validated infrastructure, upon which they can build their systems. This platform will have the double benefit of being both reliable and scalable.

***Challenges***

Not all services receive close SRE engagement. A couple of factors are at play here:

- Many services don't need high reliability and availability, so support can be provided by other means.
  * The service has been engineered to be reliable and low maintenance, and can therefore remain with the development team.
- By design, the number of development teams that request SRE support exceeds the available bandwidth of SRE teams (see Introduction).

### Production Readiness Review Model

> The most typical initial step of SRE engagement is the Production Readiness Review (PRR), a process that identifies the reliability needs of a service based on its specific details. A PRR is considered a prerequisite for an SRE team to accept responsibility for managing the production aspects of a service.

The objectives of the Production Readiness Review are as follows:

- Verify that a service meets accepted standards of production setup and operational readiness, and that service owners are prepared to work with SRE and take advantage of SRE expertise.
- Improve the reliability of the service in production, and minimize the number and severity of incidents that might be expected. A PRR targets all aspects of production that SRE cares about.

#### Engagement

- Establishing an SLO/SLA for the service
- Planning for potentially disruptive design changes required to improve reliability
- Planning and training schedules

#### Analysis

Usually, the SRE team establishes and maintains a PRR checklist explicitly for the Analysis phase. The checklist is specific to the service and is generally based on domain expertise

A few examples of checklist items include:

- Do updates to the service impact an unreasonably large percentage of the system at once?
- Does the service connect to the appropriate serving instance of its dependencies? For example, end-user requests to a service should not depend on a system that is designed for a batch-processing use case.
- Does the service request a sufficiently high network quality-of-service when talking to a critical remote service?
- Does the service report errors to central logging systems for analysis? Does it report all exceptional conditions that result in degraded responses or failures to the end users?
- Are all user-visible request failures well instrumented and monitored, with suitable alerting configured?


## SRE & Platform Frameworks

To effectively respond to scalability conditions, it became necessary to develop a model that allowed for the following principles:

**Codified best practices**

The ability to commit what works well in production to code, so services can simply use this code and become "production ready" by design.

**Reusable solutions**

Common and easily shareable implementations of techniques used to mitigate scalability and reliability issues.

**A common production platform with a common control surface**

Uniform sets of interfaces to production facilities, uniform sets of operational controls, and uniform monitoring, logging, and configuration for all services. Services built using these frameworks share implementations that are designed to work with the SRE-supported platform, and are maintained by both SRE and development teams.

**Easier automation and smarter systems**

A common control surface that enables automation and smart systems at a level not possible before. For example, SREs can readily receive a single view of relevant information for an outage, rather than hand collecting and analyzing mostly raw data from disparate sources (logs, monitoring data, and so on).

---

The service frameworks implement infrastructure code in a standardized fashion and address various production concerns. Each concern is encapsulated in one or more framework modules, each of which provides a cohesive solution for a problem domain or infrastructure dependency.

- Instrumentation and metrics
- Request logging
- Control systems involving traffic and load management

A framework essentially is a prescriptive implementation for using a set of software components and a canonical way of combining these components. The framework can also expose features that control various components in a cohesive manner. For example, a framework might provide the following:

- Business logic organized as well-defined semantic components that can be referenced using standard terms
- Standard dimensions for monitoring instrumentation
- A standard format for request debugging logs
- A standard configuration format for managing load shedding
- Capacity of a single server and determination of "overload" that can both use a semantically consistent measure for feedback to various control systems

### Platform Management Benefits

The structural approach, founded on service frameworks and a common production platform and control surface, provided a host of new benefits.

- Frameworks provide multiple upfront gains in consistency and efficiency.
- They free developers from having to glue together and configure individual components in an ad hoc service-specific manner,
- They drive a single reusable solution for production concerns across services, which means that framework users end up with the same common implementation and minimal configuration differences.
- Significantly lower operational overhead
- Universal support by design
- Faster, lower overhead engagements
- Built-in service features as part of the framework implementation
- Faster service onboarding (usually accomplished by a single SRE during one quarter)
- Less cognitive burden for the SRE teams managing services built using frameworks

