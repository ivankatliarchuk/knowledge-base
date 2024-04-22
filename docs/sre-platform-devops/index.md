---
title: DevOps
summary: summary of devops documentation
authors: ["ivan k"]
tags: ["devops", "sre", "platform"]
date: 2021-03-8
source:
published: true
---

# Platform Engineering

- [DevOps: bookmarks](http://www.devopsbookmarks.com)
- [Pragma: IT operations maturity model(todo: document company best practices)](http://code.praqma.com/ops-maturity/)
- [Rackspace: fanatic support ](https://www.rackspace.com/en-gb/resources?region%5B113%5D=113&content_type%5Bwhite_paper%5D=white_paper)

## Platform Security Squad

- [Owasp Best Practices](https://cheatsheetseries.owasp.org/index.html)

## Tagging

```
Data Classification - info-sec:data-classification -> sensitive, company-confidential, customer-identifiable
Disaster recovery - disaster-recovery:rpo -> 6h, 24h
Cost allocation - cost-allocation:business-unit ->   engineering, networking recrutment
```

- [What are tags](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html)
- [Tagging rules](https://peritossolutions.com/aws/aws-tagging-rules/)
- [Tagging restrictions](https://docs.aws.amazon.com/mediaconnect/latest/ug/tagging-restrictions.html)
- [Tagging assets](../../assets/tagging/)
- [Tagging ](https://github.com/ik-cloud/aws-enterprise-naming-tagging-standard)
- [Tagging and Labeling Best practices](https://www.doit.com/google-cloud-platform-resource-labeling-best-practices/)

Note that standardizing on and adhering to a labeling policy is crucial for centrally-managed labels. Product teams and departments can also add custom labels to resources to share team-specific information. For more information, see [Apply non-standard labels](https://cloud.google.com/resource-manager/docs/best-practices-labels#nonstandardlabels).

Here's an example of how you can define a standard set of values for each of the keys:

- Environment: `prod/dev/staging`
- Data-classification: `public/internal-only/confidential/restricted/na`
- Cost center: `c23543`
- Team: `shopping-cart`
- Component: `frontend/cache/backend/database`
- Application: `shopping-cart-payments`
- Compliance: `pci-hippa`

### Avoid confidential information

Protecting personally identifiable information (PII) is critical for security. Avoid storing PII or other confidential information in your labels.

### Apply non-standard labels

Although adhering to a label policy is crucial, labels can also be used to share information that is specific to a product team or department. In such a scenario, providing resource owners of individual teams the option to apply non-standard labels for each resource can help provide more context about the resource. This makes it easier to search, filter, and share information specific to these product teams or departments. For example, a single resource can have a set of standard labels such as `environment:prod`, `data-classification:restricted`, `cost-center:c23543`, `team:shopping-cart`, `app:shopping-cart-payments`, `component:database`, `compliance: pci`. The resource owner can add non-standard labels such as `version:5.0.1` and `replica:primary` to indicate the version of the database cluster and the node's replication status.

### Consider change implications

Your labeling strategy is likely to change in times of evolving business requirements. Be aware of the implications that these changes may have. For example, the addition of new cost centers, microservices, or new tools can impact your labeling strategy.

## Label naming scheme and pattern

Every organization has its own way of organizing resources. You can use labels to categorize the resources in your hierarchy in multiple ways, helping users to filter for the resources they need. When defining your label naming scheme, consider the following:

-   Environment, cost center, team, component, applications, compliance, and ownership associated with the resource.
-   Data classification of any data stored in the system. This is only applicable to stateful systems.
-   Labels that need to be applied at the specific resource level like Compute Engine, Cloud Storage bucket or at the project.
-   Flexibility to use optional labels, as needed, to provide more information on resources.

## Example of defining labels

To define labels, here are some attributes that you need to keep in mind.

| Field | Description |
| --- | --- |
| Label key | The label key is a unique identifier for a label. It must be a string with a minimum length of 1 character and a maximum length of 63 characters. The key cannot be empty. You can use a standard set of label keys that work best for your organization that cover business use cases like `environment`, `data-classification`, `cost-center`, `team`, `component`, `application` and `compliance`. |
| Label value | The label value is the data associated with the key. It can be a string, number, or Boolean value. As a best practice, consider defining a set of values for each label key. This can help teams select and assign appropriate values for each key. For example, an `environment` key can have values such as `prod`, `staging`, `dev` or `tools`. |
| Stakeholder | Identify the department which needs the label key for filtering resources or creating reports. For example, a Finance department in an organization would like to know the cost of running the `prod` environment. They would use the label _key:value_ pair `environment:prod`. |
| Target resource | For each label, consider defining a target Google Cloud resource where the label _key:value_ pair should be applied. For example, the label key `environment` needs to be on each Google Cloud resource in your organization's production environment. |
| Exception | Consider defining which label keys are mandatory on all resources and which keys are optional to apply. In the [example table](https://cloud.google.com/resource-manager/docs/best-practices-labels#example_labels_table), there are some label `key:value` pairs that are optional such as `environment:tools`. The label key `altostrat-team` can be considered optional when the label `altostrat-environment` has the label value set to `tools`. |

In the following label example, _altostrat_ corresponds to the name of the enterprise.

| Label key | Label value | Stakeholder | Target resource | Exception |
| --- | --- | --- | --- | --- |
| altostrat-environment | prod, sb1, staging, dev, tools | Finance | Google Cloud resources | No |
| altostrat-data-classification | public, internal-only, confidential, restricted, na | Security | Buckets, databases, persistent disks with Compute Engine | No |
| altostrat-cost-center | fin-us, mkt-eu, it-jp | Finance | Google Cloud resources | sandbox-folder |
| altostrat-team | shopping-cart | Team lead | Google Cloud resources | Non-production environments, non-critical components |
| altostrat-component | frontend, cache, application, database | Finance | Google Cloud resources | Optional |
| altostrat-app | shopping-cart-payment | Finance | Google Cloud resources | No. There's an exception for multi-tenant resources where there is no 1:1 mapping with the application. |
| altostrat-compliance | pci, hipaa | Security | Google Cloud resources | Optional |

#### **Label all you need**

Labels are a key-value pair so use that to your advantage to add in as much data as you need onto them.

Here are some examples of labels to use:

1.  _Environment names_
    Labeling a resource as belonging to development, staging, testing, production, etc. is always a safe choice so searching for all resources in production later for a billing report is much easier.
2.  _Role_
    If you have a set of Compute Engine resources acting as web servers, another set in a GKE cluster, and one for a database server label them as such.
3.  _Application name
    _Using the application name as a label makes it easier to group resources by the business project or application they are associated with makes it easier to look at costs per application.
4.  _Region name
    _If your application or project stretches multiple regions adding the region value will help sort them later. This can be the GCP region name, a logical region you have setup in your application, or having a label for each.
5.  _Resource Creator
    _Putting the name of the creator in a label will help sort out who created what resource later instead of having to dig through audit logs that may or may not have been retained.
6.  _Owner or maintainer
    _Labeling a resource with the owner or maintainer’s name assists in who to contact in the case of an issue or question later. A common example of this would be the team that owns or maintains the resource.
7.  _Cost, billing, or budget code
    _Some organizations have codes for different expenditures or budgets. Adding these into the label makes it easier for billing administrators or auditors to track these.
8.  _Department_
    If the resource belongs to a certain department then adding it as a label makes it easier to track down a department later.
9.  _Bucket name (Google Cloud Storage only)
    _If you have ever had to look at a GCP billing report or invoice you realize it groups all of the storage buckets together into one line item. This is a nightmare if you want to know what each bucket costs, so adding the bucket name as a label to each bucket will allow this to be broken out into separate line items.
10.  _Associated resource name
    _If you have a resource that’s tied to another resource it’s a good idea to add a label naming that resource to it. Examples of this might be a persistent disk tied to a Compute Engine instance or a Dataproc cluster. An external IP that is tied to a Compute Engine managed instance group is a great example of this as well.
11.  _Data classification
    _This is a broad labeling use case, but if you have any sort of data that needs to be labeled in a bucket or BigQuery dataset then add a label for it to denote this. Examples might be data that falls under regulatory compliance such as HIPAA or PCI or encrypted data. It’s best to label these resources with this so when a C-level executive asks how much money is spent on storing PHI (protected health information) per month it can be pulled up very quickly.
12.  _Resource state_
    If a resource is active, pending deletion, disabled, etc. then labeling it as so makes it very easy to see how much is being billed to resources in a particular state.
13.  _Folder or organization name
    _If you utilize folders or different organizational units in your organizational structure make a label them to be able to see what each organization or folder costs you later.
