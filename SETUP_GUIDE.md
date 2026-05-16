# Setup Guide

This guide walks through publishing this folder as the first portfolio repository.

## Repository Name

Use:

`cybersecurity-portfolio`

## Repository Description

Use:

`Cybersecurity portfolio focused on GRC, cyber risk, CTI, vulnerability prioritization, and security strategy.`

## Recommended Visibility

Public.

The portfolio uses fictional and sanitized scenarios, so it is appropriate for a public GitHub repository.

## Create The Repository In GitHub

1. Go to GitHub.
2. Select the plus icon near the top right.
3. Select `New repository`.
4. Repository name: `cybersecurity-portfolio`.
5. Description: use the description above.
6. Visibility: `Public`.
7. Do not add a README, license, or `.gitignore` on GitHub because this folder already includes them.
8. Create the repository.

## Upload The Files

If Git is not installed:

1. Open the new empty repository on GitHub.
2. Select `uploading an existing file`.
3. Upload the contents of this `cybersecurity-portfolio` folder.
4. Commit directly to `main`.

If Git is installed later, use this flow:

```powershell
cd "$env:USERPROFILE\OneDrive\Desktop\GitHub\cybersecurity-portfolio"
git init
git branch -M main
git add .
git commit -m "Create cybersecurity portfolio"
git remote add origin https://github.com/shayaan-mohsin/cybersecurity-portfolio.git
git push -u origin main
```

## Create The GitHub Project

Create a project named:

`Cybersecurity Portfolio Roadmap`

Use the field and view setup in:

`project-management/github-project-setup.md`

Use the starter issue list in:

`project-management/backlog.csv`

## First Manual Issues To Create

Start with these five:

1. Create GitHub Project fields and views
2. Define fictional organization for NIST CSF assessment
3. Build initial risk register
4. Research CISA KEV catalog source
5. Select public breach or threat scenario for CTI brief

## First Sprint Goal

Complete Sprint 0:

- repository published
- GitHub Project created
- starter backlog created
- first five issues added
- README reviewed for public-facing wording
