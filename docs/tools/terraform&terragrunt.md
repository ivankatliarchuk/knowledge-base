---
title: terraform
summary: infrastructure tooling
authors: ["ivan k"]
tags: ["tools", "terraform", "terragrunt", "ioc"]
date: 2021-03-08
published: true
---

!!! note "terraform"
    Terraform is an open-source infrastructure as code software tool created by HashiCorp. Users define and provision data center infrastructure using a declarative configuration language known as HashiCorp Configuration Language, or optionally JSON.

## General tools

- [Terrahelp](https://github.com/opencredo/terrahelp){:target="_blank"}
- [Terracogniate: read from cloud and generate Terraform code](https://github.com/cycloidio/terracognita){:target="_blank"}
- [Terraform Landscape: improve Terraform's plan output to be easier to read and understand][terr-landscape]{:target="_blank"}
- [Terraspace: provides an organized structure, conventions over configurations, keeps your code DRY](https://terraspace.cloud/){:target="_blank"}

## Misconfiguration

- [Checkov: Static Code IoC Analytics toole][checkov]{:target="_blank"}
- [Geodesic: is the fastest way to get up and running with a rock solid, production grade cloud platform](https://github.com/cloudposse/geodesic)

## Testing

- [Terrascan: detect compliance and security violations across Infrastructure as Code][terrascan]{:target="_blank"}
- [Terraform compliance: a lightweight, security focused, BDD test framework against terraform][terr-compliance]{:target="_blank"}
- [TFSec: security scanner for your Terraform code][tfsec]{:target="_blank"}

## Terraform Modules

- [GCP: modules](https://github.com/GoogleCloudPlatform/terraform-google-examples)
- [AWS: cost estimation](https://github.com/antonbabenko/terraform-cost-estimation)
- [AWS: account baseline](https://github.com/nozaq/terraform-aws-secure-baseline)
- [Secret Hub](https://secrethub.io/blog/secret-management-for-terraform/)
- [AWS: waf](https://github.com/ik-terraform/terraform-waf-owasp)
- [AWS: waf](https://github.com/ik-terraform/aws-waf-security-automation)
- [AWS: waf owasp](https://github.com/traveloka/terraform-aws-waf-owasp-top-10-rules)

<!-- resources -->
[terrascan]: https://github.com/accurics/terrascan
[terr-compliance]: https://github.com/eerkunt/terraform-compliance
[terr-landscape]: https://github.com/coinbase/terraform-landscape
[tfsec]: https://github.com/liamg/tfsec
[checkov]: https://github.com/bridgecrewio/checkov
