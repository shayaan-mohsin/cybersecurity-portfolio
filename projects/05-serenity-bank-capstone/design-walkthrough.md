# Walkthrough: one customer request, separate administrative access

[Project overview](README.md) · [Validation table](decisions-and-validation.md)

This is a proposed design explanation for the academic scenario. No requests or tests below were executed.

## Customer path

1. A customer authenticates through a customer identity service. This is distinct from the cloud administrator’s identity system.
2. The application validates the session and checks authorization for the specific account record and requested operation.
3. An application workload uses its own narrowly scoped identity to access the required data.
4. The service records a suitable audit event without placing secrets or unnecessary customer data in logs.

A test would create two fictional customers and verify that one cannot read or change the other’s record, including when identifiers in a request are altered. A successful sign-in alone would not pass that test.

## Workforce and privileged paths

Employees use a workforce identity service and role-appropriate business applications. An administrator uses a separate privileged role for an authorized change. Temporary, scoped privileges and a recorded approval would reduce standing access, but their effectiveness would need testing.

An AWS IAM role authorizes AWS API access; it is not, by itself, the bank’s customer identity system. Azure workforce administration and a customer-facing sign-in service likewise require an explicit service and tenant design.

## Workload and key paths

Application services need identities independent of human accounts. The design should specify credential lifetime, permissions, rotation or replacement, and logs.

AWS Key Management Service and Azure Key Vault are different services with different access models. A hybrid design must specify which keys protect which data, who can use or administer them, and how dependencies behave during recovery. Merely naming both services does not establish a working integration.

## Recovery path

A backup’s existence is not proof of a recoverable service. A test would restore data and required configurations in isolation, check integrity, restore key and identity dependencies, run a controlled business transaction, and obtain service-owner acceptance.

The capstone has no measured recovery time or recovery-point result. Those objectives would first need to be agreed with business owners and then tested.
