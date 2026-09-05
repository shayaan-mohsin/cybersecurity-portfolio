# Resume And Interview Notes

## Resume Positioning

Use this as project experience, not employment experience.

Strong phrasing:

- Built a cost-conscious AWS cloud security lab using CloudTrail, S3, IAM, VPC security groups, IAM Access Analyzer, and optional GuardDuty.
- Secured lab resources with S3 Block Public Access, encryption, versioning, no default inbound security group access, root MFA guidance, and least-privilege review.
- Investigated CloudTrail management events to identify root activity, failed console login, IAM policy changes, access key creation, S3 public-access changes, security group exposure, and logging-change attempts.
- Automated CloudTrail analysis with Python to parse JSON/CSV exports, flag high-risk events, generate frequency summaries, and produce markdown investigation reports.
- Documented remediation actions, evidence-handling boundaries, and public-safe reporting practices for cloud security portfolio work.

Avoid phrasing that overclaims:

- "Managed production AWS security."
- "Performed an enterprise cloud audit."
- "Led incident response for a real organization."
- "Detected a real attacker."

## Interview Story

Use this project to tell a clear story:

1. I wanted hands-on cloud log investigation experience.
2. I built a small AWS lab instead of relying only on theory.
3. I secured the baseline environment first.
4. I generated safe events that resemble common cloud security questions.
5. I reviewed CloudTrail evidence and focused on identity, logging, network exposure, and S3 access.
6. I wrote Python automation to make the review repeatable.
7. I documented what happened, why it mattered, and how to remediate it.

## Concepts To Be Ready To Explain

### CloudTrail

CloudTrail records AWS account activity. It helps answer who did what, where, and when.

### Management Events

Management events are control-plane actions, such as creating resources, changing IAM policies, or modifying logging.

### GuardDuty

GuardDuty is AWS managed threat detection. It analyzes AWS data sources and produces findings that analysts can triage.

### S3 Block Public Access

S3 Block Public Access helps prevent public access from being granted through bucket policies or ACLs.

### IAM Access Analyzer

IAM Access Analyzer helps identify resources that may be accessible from outside the account or organization.

### Security Group Exposure

A security group rule allowing administrative ports from `0.0.0.0/0` can expose systems to the internet. Even in a lab, it is useful to detect and remediate that pattern quickly.

## How To Answer "Was This Real Experience?"

Recommended answer:

> Yes, this was a hands-on AWS lab project. I built and secured a small cloud environment, generated management events, reviewed CloudTrail evidence, and automated parts of the investigation with Python. It was not production employment experience, but it gave me practical experience reading logs, identifying risky cloud changes, and documenting remediation.

That wording is confident and honest. It shows real work without pretending it was a job.
