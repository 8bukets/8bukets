# Data Model

## Goal

Describe the core entities and relationships behind the MVP review platform.

## Core Entities

### User

Represents a registered person using the platform.

Typical fields:

- `id`
- `email`
- `password_hash`
- `role`
- `created_at`

Typical roles:

- `user`
- `admin`

## Software

Represents a software product that can receive reviews.

Typical fields:

- `id`
- `name`
- `slug`
- `description`
- `category`
- `created_at`

## Review

Represents a written opinion tied to a user and a software product.

Typical fields:

- `id`
- `user_id`
- `software_id`
- `title`
- `content`
- `status`
- `sentiment_score`
- `created_at`

Typical status values:

- `pending`
- `approved`
- `rejected`

## Rating

Represents a score tied to a review or review interaction model.

Typical fields:

- `id`
- `user_id`
- `review_id`
- `score`

## Comment

Represents a comment on a review.

Typical fields:

- `id`
- `user_id`
- `review_id`
- `content`
- `created_at`

## Moderation

Represents moderation decisions associated with reviews.

Typical fields:

- `id`
- `review_id`
- `status`
- `reason`
- `reviewed_by`
- `created_at`

## Relationships

### User to Review

- one user can create many reviews

### Software to Review

- one software entry can have many reviews

### Review to Comment

- one review can have many comments

### Review to Rating

- one review can have many ratings

### Review to Moderation

- one review can have one or more moderation records depending on implementation detail

## MVP Data Principles

- software should be structured
- reviews should be separate from editorial content
- moderation state should be explicit
- user roles should be simple in MVP

## Derived Values

The app will often display derived values such as:

- average rating
- review count
- moderation counts
- pending review count

These should be treated as computed outputs rather than separate core entities.

## Future Extensions

Likely future entities:

- vendor profile
- company ownership claim
- reviewer verification
- trust score
- notification record
- search index materialization

## Modeling Rule

Do not use legacy blog content as a substitute for structured software, review, or moderation records.
