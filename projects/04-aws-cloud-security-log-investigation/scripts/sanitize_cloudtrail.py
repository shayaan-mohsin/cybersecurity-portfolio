"""Legacy redaction disabled: it could leak identifiers and corrupt CIDR semantics.
Use only the provided synthetic fixture for this local draft. Real-event publication
requires a separately reviewed allowlist projection and rendered privacy inspection.
No generic regex sanitizer can establish that an export is safe to publish.
"""
raise SystemExit('Raw-log sanitization is unavailable in this draft. Use synthetic data; no output written.')
