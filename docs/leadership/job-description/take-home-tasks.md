---
title: take home tasks
summary: home task
author: "ik"
tags: ["job", "task", "take home", "platform"]
date: 23-03-2023
---

# Tasks

## Task 2

Rewrite with following requirements:

- A system similar(not necessary exact clone) to one you had experience working with
- Document the requirement for a platform
- Briefly document technology choices and options considered

Below are some consideration you may with to make

- The purpose of the task is to check for understanding design decisions
- How Day2Ops was implemented and potential improvements in areas like; monitoring, observability, high availability, disaster recovery, maintainability


The Task:

- Create a system demonstration similar (but not necessarily an exact clone) to one you have experience working with.
- Provide a brief description of the system.
- An architecture diagram using a tool such as draw.io or similar.
- Outline the following requirements for the system in your document:
  + High availability and disaster recovery, including failover and backup/recovery procedures (if any).
  + Security and access control, including authentication and authorization for users and applications.
  + Automated deployment, including automatic provisioning of infrastructure (such as virtual machines, load balancers, etc.) as needed.
  + Scalability, including the ability to add and remove resources dynamically as needed.
   + Technology Choices and Options Considered:

Technology Choices and Options Considered:

Your document should also briefly touch upon the technology choices and options considered for each of the above requirements. You should be able to explain the reasons for choosing the technologies, and discuss any alternatives that were considered.

Evaluation Criteria

Your submission will be evaluated based on the following criteria:

- How well your requirements document satisfies the needs of Day2Ops.
- The clarity and completeness of your requirements document.
- The quality of your technology choices and options considered.
- The overall creativity and technical skill demonstrated in your submission.

Submission Instructions:

Please submit your requirements document as a PDF or Google Docs file, along with any supporting diagrams or other materials. You may also include a README file with any additional information you wish to provide.

Outline evaluation criteria for a take home task provided below

## Task 2

Cloud Platform Engineers are integral to almost every area of Engineering at CTM. We are
responsible for the provision and support of the infrastructure that monitors, runs and
stores the code or data that other engineering teams produce. We are the educators on
best cloud practice and work collaboratively to solve the problems that other engineering
teams face.

In this task you will be expected to produce a simple clustered web service setup in AWS
that when hit with a GET request to an endpoint returns a simple 'hello world' with the date
and time as a response. The purpose of this task is to check for basic programming
knowledge, a detailed understanding of infrastructure design decisions, and some
architectural considerations. You are welcome to use any tools or languages you wish.

Below are some considerations you may wish to make, time permitting;

- Infrastructure and pipelines as code is a strong ethos amongst the Cloud Platform team
- Tools that are transferable, or platform agnostic, are more desirable within reason
- Services or products we deploy should be monitored, highly available, scalable,
maintainable, and reproducible

Evaluation Criteria

Your submission will be evaluated based on the following criteria:

1. Functionality - Does the web service function as expected? Does it return the correct response when hit with a GET request to the endpoint? Is the code clean and well-structured?

2. Infrastructure Design - How well did the candidate design the infrastructure? Did they choose appropriate AWS services to set up the clustered web service? Did they consider the infrastructure requirements for a highly available, scalable, and maintainable service?

3. Documentation and Clarity - Are the detailed instructions provided clear and easy to follow? Are any assumptions or design decisions made by the candidate clearly explained? Did the candidate include any inline comments to justify or explain their code?

4. Transferability - Did the candidate choose tools and languages that are transferable or platform agnostic? Were the tools and technologies used appropriate for the task at hand?

5. Observability and Reproducibility - Did the candidate set up monitoring for the web service? Can the code be easily reproduced by someone else? Were any automated deployment pipelines used to provision the infrastructure?

Overall, the evaluation criteria should focus on assessing the candidate's programming knowledge, infrastructure design skills, and understanding of cloud best practices.

Submission Instructions:

Please provide the code and detailed instructions on how to reproduce your answer. We
encourage commenting inline to make justification or observations in your answer.


We have no plans to do any further work  in team namespaces area e.g. changing configs or anything else. For now It would be great if core services migrated to team namespaces, same time if you feel like is not yet a right time to migrate everything over,
