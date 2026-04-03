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
