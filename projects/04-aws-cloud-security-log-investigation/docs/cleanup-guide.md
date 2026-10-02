# Proposed cleanup plan

[Project overview](../README.md) · [Build plan](aws-build-and-hardening-guide.md)

Cleanup has not been executed because this template has not been deployed.

For a future lab, inventory resources by stack and confirm each belongs to the authorized exercise. Preserve required evidence according to its retention policy before deletion. Versioned S3 buckets can retain noncurrent versions and delete markers; stack deletion may fail until owned contents are handled deliberately.

Review and remove only lab-owned resources, including any optional detector created by the exercise. Do not disable a pre-existing organizational detector or trail. Inspect stack deletion events and confirm no billable lab resources remain. Record exceptions and the final verification.
