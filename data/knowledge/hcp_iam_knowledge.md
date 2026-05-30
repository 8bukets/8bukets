# IAM Role Assignments for Terraform / HCP Context

This document captures the IAM role assignments necessary for operating Terraform/HCP within this project's context.

## User Details
- **Email ID:** 8bukets@gmail.com
- **Auth method:** GitHub
- **User ID:** 626eb9aa-6f12-40a0-af3c-0b8fc325049e
- **Type:** User

## Role Assignments

| Role  | Description | Scope |
|---|---|---|
| **Admin** | Has full access to all resources including the right to edit IAM, invite users, edit roles. | `default-project` (Project) |
| **Owner** | Has all of the admin’s permissions, and also the ability to delete the organization and promote/demote other owners. | `8bukets-org` (Organization) - Inherited |