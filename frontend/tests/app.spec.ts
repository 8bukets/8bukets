import { test, expect } from '@playwright/test';

test('has title and landing content', async ({ page }) => {
  await page.goto('/');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/Googleov Full-Stack Ekosustav/i);

  // Expect the main heading to be visible
  await expect(page.getByRole('heading', { name: /Googleov Full-Stack Ekosustav/i })).toBeVisible();
});

test('navigation links work', async ({ page }) => {
  await page.goto('/');

  // Click the Sign In link
  await page.getByRole('link', { name: /Sign In/i }).click();
  await expect(page).toHaveURL(/.*login/);
  await expect(page.getByRole('heading', { name: /Sign in to your account/i })).toBeVisible();

  // Go back and click Create Account
  await page.goto('/');
  await page.getByRole('link', { name: /Create Account/i }).click();
  await expect(page).toHaveURL(/.*register/);
  await expect(page.getByRole('heading', { name: /Create your account/i })).toBeVisible();
});
