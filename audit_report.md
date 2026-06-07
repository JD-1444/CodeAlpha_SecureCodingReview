# Secure Coding Review Report

## Project Overview

This project reviews a Python Login System for security vulnerabilities and provides secure coding recommendations.

## Vulnerabilities Identified

### 1. SQL Injection
Severity: High

Description:
User input was directly concatenated into SQL queries.

Impact:
Attackers can bypass authentication.

Remediation:
Use parameterized queries.

---

### 2. Plain Text Password Storage
Severity: Critical

Description:
Passwords are stored and compared in plain text.

Impact:
Data breach may expose passwords.

Remediation:
Hash passwords using SHA-256 or bcrypt.

---

### 3. Lack of Input Validation
Severity: Medium

Description:
Username length and format were not checked.

Impact:
Unexpected application behavior.

Remediation:
Validate all user inputs.

---

## Security Recommendations

- Use parameterized queries.
- Hash passwords before storage.
- Validate user inputs.
- Avoid exposing sensitive errors.
- Keep dependencies updated.

## Conclusion

The reviewed application contained multiple security vulnerabilities that could lead to unauthorized access. Implementing secure coding practices significantly improves application security.