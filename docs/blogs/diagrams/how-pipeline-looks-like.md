

classDiagram
    class PlatformEngineer
    class Developer
    class GitLabSaaS
    class RunnerManagement
    class VagueDocumentation
    class BreakingChanges
    class TimeWasting

    PlatformEngineer "empowers" -- Developer
    PlatformEngineer "struggles with" -- GitLabSaaS
    GitLabSaaS "hinders" -- PlatformEngineer
    RunnerManagement "is difficult in" -- GitLabSaaS
    VagueDocumentation "contributes to" -- TimeWasting
    BreakingChanges "contributes to" -- TimeWasting
    TimeWasting "impacts" -- PlatformEngineer

make this diagram more human centric

flowchart TD
    A[Tech Companies] --> B{Considerations for In-house Observability}
    B --> C[Infrastructure Costs]
    B --> D[Platform Team Costs]
    B --> E[Vendor Margins]
    C --> F[Cloud Providers vs Vendor Solutions]
    D --> G[Hire Dedicated Team]
    E --> H[Analyze Vendor Markup]

    subgraph Coinbase Case
        I[Datadog Cost: $65M]
        I --> J[Consider In-house for Cost Reduction]
        J --> K[Optimize Infrastructure]
        J --> L[Hire Dedicated Team]
        K & L --> M[Potential Cost Reduction]
        M --> N[Vendor's Compelling Offer]
        N -->
        