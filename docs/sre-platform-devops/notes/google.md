---
title: google notes
summary: google notes
authors: ["ivan k"]
tags: ["sre", "notes", "google"]
date: 20-Oct-2022
published: true
source:
- https://cloud.google.com/blog/products/devops-sre/sre-at-google-our-complete-list-of-cre-life-lessons
- https://sre.google/sre-book/dealing-with-interrupts/
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

** Issues needs triage **

> Common alerts that aren't diagnosed by either the dev team or SREs. Such alerts are frequently triaged as transient, but still distract your teammates from fixing real problems. Either investigate such alerts fully, or fix the alerting rules.

> An issue that probably should have paged, but didn't. In these cases, you should probably fix the monitoring so that such events do trigger a page. Often you encounter the issue while you're trying to fix something else, or it's related to a metric you're tracking but for which you haven't got an alert.

> An issue that is not pageable but requires attention, such as low-impact data corruption or slowness in some non-user-facing dimension of the system. Tracking reactive operational work is also appropriate here.

>  An issue that is not pageable and does not require attention. These alerts should be removed, because they create extra noise that distracts engineers from issues that do merit attention.

** Prioritization **

> SRE teams sometimes fall into ops mode because they focus on how to quickly address emergencies instead of how to reduce the number of emergencies. After you've learned enough about the service to ask hard questions about its design and deployment, spend some time prioritizing various service outages according to their impact on the team's stress levels.

