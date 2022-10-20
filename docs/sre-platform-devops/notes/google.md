---
title: google notes
summary: google notes
authors: ["ivan k"]
tags: ["sre", "notes", "google"]
date: 20-Oct-2022
published: true
source:
- https://cloud.google.com/blog/products/devops-sre/sre-at-google-our-complete-list-of-cre-life-lessons
---

# Google Notes

> “Rollback early, rollback often.” Try to move your service towards this philosophy, and you’ll reduce the Mean Time To Recover of your service.

> “Canary your rollouts.” No matter how good your testing and QA, you'll find that your binary releases occasionally have problems with live traffic. An effective canarying strategy and good monitoring can reduce the Mean Time To Detect these problems, and dramatically reduce the number of affected users.

> Ideally, your team has a stack that is multihomed and provisioned in such a way that you have at least one instance you can divert from live traffic and temporarily loan to a learning exercise. Alternatively, you might have a smaller, but still fully featured, staging or QA instance of your stack that can be borrowed for a short time. If possible, subject the stack to synthetic load that approximates real user/client traffic, in addition to resource consumption, if possible.

> The opportunities for learning from a real production system under synthetic load are abundant. Senior SREs will have experienced all sorts of troubles: misconfigurations, memory leaks, performance regressions, crashing queries, storage bottlenecks, and so forth. In this realistic but relatively risk-free environment, proctors can manipulate the job set in ways that alter the behavior of the stack, forcing new SREs to find differences, determine contributing factors, and ultimately repair systems to restore appropriate behavior.

> As an alternative to the overhead of asking a senior SRE to carefully plan a specific type of breakage that the new SRE(s) must repair, you can also work in the opposite direction with an exercise that may also increase participation from the entire team: work from a known good configuration and slowly impair the stack at selected bottlenecks, observing upstream and downstream efforts through your monitoring.

> How you apply these practices is up to you, but the charge is clear: as SRE, you have to scale your humans faster than you scale your machines.
