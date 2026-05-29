CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'user' CHECK (role IN ('user', 'admin', 'reviewer')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS software (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    description TEXT,
    category TEXT,
    website_url TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    software_id INT NOT NULL REFERENCES software(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    sentiment_score NUMERIC(5,2) DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ratings (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    review_id INT NOT NULL REFERENCES reviews(id) ON DELETE CASCADE,
    score INT NOT NULL CHECK (score >= 1 AND score <= 5),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, review_id)
);

CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    review_id INT NOT NULL REFERENCES reviews(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS moderation (
    id SERIAL PRIMARY KEY,
    review_id INT NOT NULL REFERENCES reviews(id) ON DELETE CASCADE,
    status TEXT NOT NULL DEFAULT 'pending',
    reason TEXT,
    reviewed_by INT REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO software (name, slug, description, category, website_url)
VALUES
    ('Ahrefs', 'ahrefs', 'SEO intelligence platform for backlink analysis, keyword research, and competitive content discovery.', 'seo-marketing', 'https://ahrefs.com'),
    ('SEMrush', 'semrush', 'Search marketing suite for SEO, competitive research, content planning, and paid traffic analysis.', 'seo-marketing', 'https://www.semrush.com'),
    ('Google Analytics 4', 'google-analytics-4', 'Web and product analytics platform for understanding traffic, engagement, and conversion behavior.', 'analytics', 'https://analytics.google.com'),
    ('HubSpot', 'hubspot', 'CRM and growth platform for marketing, sales, service, and customer lifecycle workflows.', 'crm-marketing', 'https://www.hubspot.com'),
    ('WordPress', 'wordpress', 'Content management system and website platform used for blogs, business sites, and publishing workflows.', 'cms-website', 'https://wordpress.org'),
    ('Webflow', 'webflow', 'Visual website platform that combines design, CMS capabilities, and modern publishing workflows.', 'cms-website', 'https://webflow.com'),
    ('Notion', 'notion', 'Collaborative workspace for docs, projects, internal knowledge, and lightweight team workflows.', 'productivity-knowledge', 'https://www.notion.so'),
    ('ChatGPT', 'chatgpt', 'AI assistant used for drafting, research, idea generation, and workflow acceleration across many roles.', 'ai-productivity', 'https://chatgpt.com'),
    ('Vercel', 'vercel', 'Frontend deployment platform optimized for modern web applications, previews, and edge delivery.', 'hosting-deployment', 'https://vercel.com'),
    ('Shopify', 'shopify', 'Ecommerce platform for storefront creation, product management, payments, and online retail operations.', 'ecommerce', 'https://www.shopify.com')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO users (email, password_hash, role)
VALUES
    ('demo-user@software-review-platform.local', '$2b$10$wJwVY6Q9B2rjM0dM7b6mTO56V2KfQ5jM2xA0Q9B4FZ8hP7N1lRz4K', 'user'),
    ('demo-admin@software-review-platform.local', '$2b$10$wJwVY6Q9B2rjM0dM7b6mTO56V2KfQ5jM2xA0Q9B4FZ8hP7N1lRz4K', 'admin')
ON CONFLICT (email) DO NOTHING;

INSERT INTO reviews (user_id, software_id, title, content, status, sentiment_score)
SELECT
    u.id,
    s.id,
    seed.title,
    seed.content,
    seed.status,
    seed.sentiment_score
FROM (
    VALUES
        ('demo-user@software-review-platform.local', 'ahrefs', 'Strong SEO research depth for content teams', 'Ahrefs was most useful when we needed fast keyword discovery, backlink visibility, and competitor content direction in one workflow. The data depth felt strong, but pricing can be difficult for smaller teams.', 'approved', 0.85),
        ('demo-user@software-review-platform.local', 'semrush', 'Broad marketing coverage but takes time to learn', 'SEMrush felt valuable because it combines SEO, competitive research, and content planning in one place. The tradeoff is interface complexity, especially for teams that only need a smaller part of the platform.', 'approved', 0.55),
        ('demo-user@software-review-platform.local', 'wordpress', 'Flexible, proven, but depends on careful setup', 'WordPress is still one of the most adaptable publishing platforms if you want control over content and extensions. It works well, but plugin quality and maintenance discipline make a big difference over time.', 'approved', 0.45),
        ('demo-user@software-review-platform.local', 'chatgpt', 'Useful daily assistant when prompts are clear', 'ChatGPT became useful once we treated it as a workflow assistant for drafting, idea generation, and structured research. It saves time, but output quality still depends heavily on prompt clarity and review.', 'approved', 0.80),
        ('demo-user@software-review-platform.local', 'vercel', 'Great deployment experience for modern frontend teams', 'Vercel made preview deployments and frontend release workflows noticeably smoother. It is strongest when the team already works in a modern React or Next.js setup.', 'pending', 0.70)
) AS seed(user_email, software_slug, title, content, status, sentiment_score)
JOIN users u ON u.email = seed.user_email
JOIN software s ON s.slug = seed.software_slug
WHERE NOT EXISTS (
    SELECT 1
    FROM reviews r
    WHERE r.user_id = u.id
      AND r.software_id = s.id
      AND r.title = seed.title
);

INSERT INTO ratings (user_id, review_id, score)
SELECT
    u.id,
    r.id,
    seed.score
FROM (
    VALUES
        ('demo-user@software-review-platform.local', 'Strong SEO research depth for content teams', 5),
        ('demo-user@software-review-platform.local', 'Broad marketing coverage but takes time to learn', 4),
        ('demo-user@software-review-platform.local', 'Flexible, proven, but depends on careful setup', 4),
        ('demo-user@software-review-platform.local', 'Useful daily assistant when prompts are clear', 5),
        ('demo-user@software-review-platform.local', 'Great deployment experience for modern frontend teams', 4)
) AS seed(user_email, review_title, score)
JOIN users u ON u.email = seed.user_email
JOIN reviews r ON r.title = seed.review_title
WHERE NOT EXISTS (
    SELECT 1
    FROM ratings rt
    WHERE rt.user_id = u.id
      AND rt.review_id = r.id
);

INSERT INTO comments (user_id, review_id, content)
SELECT
    u.id,
    r.id,
    seed.content
FROM (
    VALUES
        ('demo-admin@software-review-platform.local', 'Strong SEO research depth for content teams', 'Helpful review. It gives enough context on both research depth and pricing tradeoffs.'),
        ('demo-admin@software-review-platform.local', 'Flexible, proven, but depends on careful setup', 'The point about plugin quality is important and worth keeping visible for buyers.')
) AS seed(user_email, review_title, content)
JOIN users u ON u.email = seed.user_email
JOIN reviews r ON r.title = seed.review_title
WHERE NOT EXISTS (
    SELECT 1
    FROM comments c
    WHERE c.user_id = u.id
      AND c.review_id = r.id
      AND c.content = seed.content
);

INSERT INTO moderation (review_id, status, reason, reviewed_by)
SELECT
    r.id,
    seed.status,
    seed.reason,
    admin.id
FROM (
    VALUES
        ('Strong SEO research depth for content teams', 'approved', 'Approved as useful seeded launch review'),
        ('Broad marketing coverage but takes time to learn', 'approved', 'Approved as useful seeded launch review'),
        ('Flexible, proven, but depends on careful setup', 'approved', 'Approved as useful seeded launch review'),
        ('Useful daily assistant when prompts are clear', 'approved', 'Approved as useful seeded launch review'),
        ('Great deployment experience for modern frontend teams', 'pending', 'Waiting for admin moderation')
) AS seed(review_title, status, reason)
JOIN reviews r ON r.title = seed.review_title
JOIN users admin ON admin.email = 'demo-admin@software-review-platform.local'
WHERE NOT EXISTS (
    SELECT 1
    FROM moderation m
    WHERE m.review_id = r.id
      AND m.status = seed.status
);
