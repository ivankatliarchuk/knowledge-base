---
title: Application Readiness checklist
created: 2021-07-29
tags: ["application readiness", "infrastructure", "readiness", 'forensic', 'platform', 'containers security']
source:
- https://cloudsecurityalliance.org/blog/2017/12/11/aws-cloud-proactive-security-forensic-readiness-part-1/
- https://cloudsecurityalliance.org/blog/2018/03/13/aws-cloud-proactive-security-part-2/
author: cloudsecurityalliance
---

# AWS Cloud: Proactive Security and Forensic Readiness

## Part 1

> ## Excerpt
> In a recent study by Dashlane regarding password strength, AWS was listed as an organization that supports weak password rules.

---
By Neha Thethi, Information Security Analyst, BH Consulting

**Part 1 – Identity and Access Management in AWS**

This is the first in a [five-part blog series](http://bhconsulting.ie/aws-cloud-proactive-security-forensic-readiness-five-part-best-practice/) that provides a checklist for proactive security and forensic readiness in the AWS cloud environment. This post relates to identity and access management in AWS.

In a [recent study by Dashlane](https://blog.dashlane.com/dashlane-password-power-rankings-2017/#takeaways) regarding password strength, AWS was listed as an organization that supports weak password rules. However, AWS has numerous features that enable granular control for access to an account’s resources by means of the Identity and Access Management (IAM) service. IAM provides control over who can use AWS resources (authentication) and how they can use those resources (authorization).

The following list focuses on limiting access to, and use of, root account and user credentials; defining roles and responsibilities of system users; limiting automated access to AWS resources; and protecting access to data stored in storage buckets – including important data stored by services such as CloudTrail.

The checklist provides best practice for the following:

1.  [How are you protecting the access to and the use of **AWS root account credentials**?](https://cloudsecurityalliance.org/blog/2017/12/11/aws-cloud-proactive-security-forensic-readiness-part-1/#1bookmark)
2.  [How are you defining **roles** and **responsibilities** of **system users** to control human access to the AWS Management Console and API?](https://cloudsecurityalliance.org/blog/2017/12/11/aws-cloud-proactive-security-forensic-readiness-part-1/#2bookmark)
3.  [How are you protecting the access to and the use of **user account credentials**?](https://cloudsecurityalliance.org/blog/2017/12/11/aws-cloud-proactive-security-forensic-readiness-part-1/#3bookmark)
4.  [How are you limiting **automated access** to AWS resources?](https://cloudsecurityalliance.org/blog/2017/12/11/aws-cloud-proactive-security-forensic-readiness-part-1/#4bookmark)
5.  [How are you protecting your **CloudTrail logs** stored in S3 and your **Billing S3 bucket**?](https://cloudsecurityalliance.org/blog/2017/12/11/aws-cloud-proactive-security-forensic-readiness-part-1/#5bookmark)

### **Best-practice checklist**

**1) How are you protecting the access to and the use of AWS root account credentials?**

-   Lock away your AWS account (root) login credentials
-   Use multi-factor authentication (MFA) on root account
-   Make minimal use of root account (or no use of root account at all if possible). Use IAM user instead to manage the account
-   Do not use AWS root account to create API keys.

**2) How are you defining roles and responsibilities of system users to control human access to the AWS Management Console and API?**

-   Create individual IAM users
-   Configure a strong password policy for your users
-   Enable MFA for privileged users
-   Segregate defined roles and responsibilities of system users by creating user groups. Use groups to assign permissions to IAM users
-   Clearly define and grant only the minimum privileges to users, groups, and roles that are needed to accomplish business requirements.
-   Use AWS defined policies to assign permissions whenever possible
-   Define and enforce user life-cycle policies
-   Use roles to delegate access to users, applications, or services that don’t normally have access to your AWS resources
-   Use roles for applications that run on Amazon EC2 instances
-   Use access levels (list, read, write and permissions management) to review IAM permissions
-   Use policy conditions for extra security
-   Regularly monitor user activity in your AWS account(s).

**3) How are you protecting the access to and the use of user account credentials?**

-   Rotate credentials regularly
-   Remove/deactivate unnecessary credentials
-   Protect EC2 key pairs. Password protect the _.pem_ and _.ppk_ file on user machines
-   Delete keys on your instances when someone leaves your organization or no longer requires access
-   Regularly run least privilege checks using IAM user Access Advisor and IAM user Last Used Access Keys
-   Delegate access by using roles instead of by sharing credentials
-   Use IAM roles for cross-account access and identity federation
-   Use temporary security instead of long-term access keys.

**4) How are you limiting automated access to AWS resources**?

-   Use IAM roles for EC2 and an AWS SDK or CLI
-   Store static credentials securely that are used for automated access
-   Use instance profiles or Amazon STS for dynamic authentication
-   For increased security, implement alternative authentication mechanisms (e.g. LDAP or Active Directory)
-   Protect API access using Multi-factor authentication (MFA).

**5) How are you protecting your CloudTrail logs stored in S3 and your Billing S3 bucket?**

-   Limit access to users and roles on a “need-to-know” basis for data stored in S3
-   Use bucket access permissions and object access permissions for fine-grained control over S3 resources
-   Use bucket policies to grant other AWS accounts or IAM

# Part 2

> ## Excerpt
> Protecting any computing infrastructure requires a layered approach. The layers are typically divided into physical, network, system, application, and data.

---
By Neha Thethi, Information Security Analyst, BH Consulting

### **Part 2: Infrastructure-level protection in AWS**

This is the second in a [five-part blog series](http://bhconsulting.ie/aws-cloud-proactive-security-forensic-readiness-five-part-best-practice/) that provides a checklist for proactive security and forensic readiness in the AWS cloud environment. This post relates to protecting your virtual infrastructure within AWS.

Protecting any computing infrastructure requires a layered or defense-in-depth approach. The layers are typically divided into physical, network (perimeter and internal), system (or host), application, and data. In an Infrastructure as a Service (IaaS) environment, AWS is responsible for security ‘of’ the cloud including the physical perimeter, hardware, compute, storage and networking, while customers are responsible for security ‘in’ the cloud, or on layers above the hypervisor. This includes the operating system, perimeter and internal network, application and data.

Infrastructure protection requires defining trust boundaries (e.g., network boundaries and packet filtering), system security configuration and maintenance (e.g., hardening and patching), operating system authentication and authorizations (e.g., users, keys, and access levels), and other appropriate policy enforcement points (e.g., web application firewalls and/or API gateways).

The key AWS service that supports service-level protection is AWS Identity and Access Management (IAM) while Virtual Private Cloud (VPC) is the fundamental service that contributes to securing infrastructure hosted on AWS. VPC is the virtual equivalent of a traditional network operating in a data center, albeit with the scalability benefits of the AWS infrastructure. In addition, there are several other services or features provided by AWS that can be leveraged for infrastructure protection.

The following list mainly focuses on network and host-level boundary protection, protecting integrity of the operating system on EC2 instances and Amazon Machine Images (AMIs) and security of containers on AWS.

The checklist provides best practice for the following:

1.  [How are you enforcing **network** and **host-level boundary protection**?](https://cloudsecurityalliance.org/blog/2018/03/13/aws-cloud-proactive-security-part-2/#1bookmark)
2.  [How are you protecting against **distributed denial of service (DDoS) attacks** at network and application level?](https://cloudsecurityalliance.org/blog/2018/03/13/aws-cloud-proactive-security-part-2/#2bookmark)
3.  [How are you managing the **threat of malware**?](https://cloudsecurityalliance.org/blog/2018/03/13/aws-cloud-proactive-security-part-2/#3bookmark)
4.  [How are you identifying **vulnerabilities** or **misconfigurations** in the operating system of your **Amazon EC2 instances**?](https://cloudsecurityalliance.org/blog/2018/03/13/aws-cloud-proactive-security-part-2/#4bookmark)
5.  [How are you protecting the **integrity** of the **operating system** on your **Amazon EC2 instances**?](https://cloudsecurityalliance.org/blog/2018/03/13/aws-cloud-proactive-security-part-2/#5bookmark)
6.  [How are you ensuring **security** of **containers** on AWS?](https://cloudsecurityalliance.org/blog/2018/03/13/aws-cloud-proactive-security-part-2/#6bookmark)
7.  [How are you ensuring only **trusted Amazon Machine Images (AMIs)** are launched?](https://cloudsecurityalliance.org/blog/2018/03/13/aws-cloud-proactive-security-part-2/#7bookmark)
8.  [How are you creating **secure custom** (private or public) **AMIs**?](https://cloudsecurityalliance.org/blog/2018/03/13/aws-cloud-proactive-security-part-2/#8bookmark)

IMPORTANT NOTE: Identity and access management is an integral part of securing an infrastructure, however, you’ll notice that the following checklist does not focus on the AWS IAM service. I have covered this in a separate checklist on IAM best practices [here](https://blog.cloudsecurityalliance.org/2017/12/11/aws-cloud-proactive-security-forensic-readiness-part-1/).

### _**Best-practice checklist**_

**1\. How are you enforcing network and host-level boundary protection?**

-   Establish appropriate network design for your workload to ensure only desired network paths and routing are allowed
-   For large-scale deployments, design network security in layers – external, DMZ, and internal
-   When designing NACL rules, consider that it’s a stateless firewall, so ensure to define both outbound and inbound rules
-   Create secure VPCs using network segmentation and security zoning
-   Carefully plan routing and server placement in public and private subnets.
-   Place instances (EC2 and RDS) within VPC subnets and restrict access using security groups and NACLs
-   Use non-overlapping IP addresses with other VPCs or data centre in use
-   Control network traffic by using security groups (stateful firewall, outside OS layer), NACLs (stateless firewall, at subnet level), bastion host, host based firewalls, etc.
-   Use Virtual Gateway (VGW) where Amazon VPC-based resources require remote network connectivity
-   Use IPSec or AWS Direct Connect for trusted connections to other sites
-   Use VPC Flow Logs for information about the IP traffic going to and from network interfaces in your VPC
-   Protect data in transit to ensure the confidentiality and integrity of data, as well as the identities of the communicating parties.

**2\. How are you protecting against distributed denial of service (DDoS) attacks at network and application level?**

-   Use firewalls including Security groups, network access control lists, and host based firewalls
-   Use rate limiting to protect scarce resources from overconsumption
-   Use Elastic Load Balancing and Auto Scaling to configure web servers to scale out when under attack (based on load), and shrink back when the attack stops
-   Use AWS Shield, a managed Distributed Denial of Service (DDoS) protection service, that safeguards web applications running on AWS
-   Use Amazon CloudFront to absorb DoS/DDoS flooding attacks
-   Use AWS WAF with AWS CloudFront to help protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources
-   Use Amazon CloudWatch to detect DDoS attacks against your application
-   Use VPC Flow Logs to gain visibility into traffic targeting your application.

**3\. How are you managing the threat of malware?**

-   Give users the minimum privileges they need to carry out their tasks
-   Patch external-facing and internal systems to the latest security level.
-   Use a reputable and up-to-date antivirus and antispam solution on your system.
-   Install host based IDS with file integrity checking and rootkit detection
-   Use IDS/IPS systems for statistical/behavioural or signature-based algorithms to detect and contain network attacks and Trojans.
-   Launch instances from trusted AMIs only
-   Only install and run trusted software from a trusted software provider (note: MD5 or SHA-1 should not be trusted if software is downloaded from random source on the internet)
-   Avoid SMTP open relay, which can be used to spread spam, and which might also represent a breach of the AWS Acceptable Use Policy.

**4\. How are you identifying vulnerabilities or misconfigurationsin the operating system of your Amazon EC2 instances?**

-   Define approach for securing your system, consider the level of access needed and take a least-privilege approach
-   Open only the ports needed for communication, harden OS and disable permissive configurations
-   Remove or disable unnecessary user accounts.
-   Remove or disable all unnecessary functionality.
-   Change vendor-supplied defaults prior to deploying new applications.
-   Automate deployments and remove operator access to reduce attack surface area using tools such as EC2 Systems Manager Run Command
-   Ensure operating system and application configurations, such as firewall settings and anti-malware definitions, are correct and up-to-date; Use EC2 Systems Manager State Manager to define and maintain consistent operating system configurations
-   Ensure an inventory of instances and installed software is maintained; Use EC2 Systems Manager Inventory to collect and query configuration about your instances and installed software
-   Perform routine vulnerability assessments when updates or deployments are pushed; Use Amazon Inspector to identify vulnerabilities or deviations from best practices in your guest operating systems and applications
-   Leverage automated patching tools such as EC2 Systems Manager Patch Manager to help you deploy operating system and software patches automatically across large groups of instances
-   Use AWS CloudTrail, AWS Config, and AWS Config Rules as they provide audit and change tracking features for auditing AWS resource changes.
-   Use template definition and management tools, including AWS CloudFormation to create standard, preconfigured environments.

**5\. How are you protecting the integrity of the operating system on your Amazon EC2 instances?**

-   Use file integrity controls for Amazon EC2 instances
-   Use host-based intrusion detection controls for Amazon EC2 instances
-   Use a custom Amazon Machine Image (AMI) or configuration management tools (such as Puppet or Chef) that provide secure settings by default.

**6\. How are you ensuring security of containers on AWS?**

-   Run containers on top of virtual machines
-   Run small images, remove unnecessary binaries
-   Use many small instances to reduce attack surface
-   Segregate containers based on criteria such as role or customer and risk
-   Set containers to run as non-root user
-   Set filesystems to be read-only
-   Limit container networking; Use AWS ECS to manage containers and define communication between containers
-   Leverage Linux kernel security features using tools like SELinux, Seccomp, AppArmor
-   Perform vulnerability scans of container images
-   Allow only approved images during build
-   Use tools such as Docker Bench to automate security checks
-   Avoid embedding secrets into images or environment variables, Use S3-based secrets storage instead.

**7\. How are you ensuring only trusted Amazon Machine Images (AMIs) are launched?**

-   Treat shared AMIs as any foreign code that you might consider deploying in your own data centre and perform the appropriate due diligence
-   Look for description of shared AMI, and the AMI ID, in the Amazon EC2 forum
-   Check aliased owner in the account field to find public AMIs from Amazon.

**8\. How are you creating secure custom (private or public) AMIs?**

-   Disable root API access keys and secret key
-   Configure Public Key authentication for remote login
-   Restrict access to instances from limited IP ranges using Security Groups
-   Use bastion hosts to enforce control and visibility
-   Protect the .pem file on user machines
-   Delete keys from the authorized\_keys file on your instances when someone leaves your organization or no longer requires access
-   Rotate credentials (DB, Access Keys)
-   Regularly run least privilege checks using IAM user Access Advisor and IAM user Last Used Access Keys
-   Ensure that software installed does not use default internal accounts and passwords.
-   Change vendor-supplied defaults before creating new AMIs
-   Disable services and protocols that authenticate users in clear text over the network, or otherwise insecurely.
-   Disable non-essential network services on startup. Only administrative services (SSH/RDP) and the services required for essential applications should be started.
-   Ensure all software is up to date with relevant security patches
-   For in instantiated AMIs, update security controls by running custom bootstrapping Bash or Microsoft Windows PowerShell scripts; or use bootstrapping applications such as Puppet, Chef, Capistrano, Cloud-Init and Cfn-Init
-   Follow a formalised patch management procedure for AMIs
-   Ensure that the published AMI does not violate the Amazon Web Services Acceptable Use Policy. Examples of violations include open SMTP relays or proxy servers. For more information, see the Amazon Web Services Acceptable Use Policy [http://aws.amazon.com/aup/](https://aws.amazon.com/aup/)

Security at the infrastructure level, or any level for that matter, certainly requires more than just a checklist. For a comprehensive insight into infrastructure security within AWS, we suggest reading the following AWS whitepapers – [AWS Security Pillar](https://d0.awsstatic.com/whitepapers/architecture/AWS-Security-Pillar.pdf) and [AWS Security Best Practises](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.pdf).

<!-- REsources -->
For more details, refer to the following AWS resources:

-   [AWS Best Practices for DDoS Resiliency](https://d1.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf)
-   [AWS re:Invent 2016: Securing Container-Based Applications (CON402)](https://www.youtube.com/watch?v=Fv4dXU5zNiM)
-   [AWS Securing EC2 Instances](https://aws.amazon.com/answers/security/aws-securing-ec2-instances/)
-   [Security in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html)
-   [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
-   [Logging IAM Events with AWS CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html)
-   [Security Checklist – General](https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Checklist.c509298947ea947e69d08dc098913cfdb042f2c8.pdf)
-   [AWS Security Best Practices](https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.d47f115d8afb49efeed8fd20dd756890ad0cc81d.pdf)
-   [Protect your S3 bucket in a right way](https://mackeepersecurity.com/post/protect-your-s3-bucket-in-a-right-way)

