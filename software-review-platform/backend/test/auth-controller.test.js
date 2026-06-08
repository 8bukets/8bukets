import test from "node:test";
import assert from "node:assert/strict";
import { login, register } from "../src/controllers/authController.js";

function createMockResponse() {
  return {
    statusCode: 200,
    body: null,
    status(code) {
      this.statusCode = code;
      return this;
    },
    json(payload) {
      this.body = payload;
      return this;
    },
  };
}

test("register rejects malformed email", async () => {
  const req = { body: { email: "bad-email", password: "12345678" } };
  const res = createMockResponse();

  await register(req, res);

  assert.equal(res.statusCode, 400);
  assert.equal(res.body.error, "Enter a valid email address");
});

test("register rejects short password", async () => {
  const req = { body: { email: "user@example.com", password: "short" } };
  const res = createMockResponse();

  await register(req, res);

  assert.equal(res.statusCode, 400);
  assert.equal(res.body.error, "Password must be at least 8 characters long");
});

test("login rejects malformed email before touching persistence", async () => {
  const req = { body: { email: "not-an-email", password: "12345678" } };
  const res = createMockResponse();
  const originalSecret = process.env.JWT_SECRET;

  process.env.JWT_SECRET = "test-secret";

  try {
    await login(req, res);

    assert.equal(res.statusCode, 400);
    assert.equal(res.body.error, "Enter a valid email address");
  } finally {
    process.env.JWT_SECRET = originalSecret;
  }
});

test("login fails clearly when JWT secret is missing", async () => {
  const req = { body: { email: "user@example.com", password: "12345678" } };
  const res = createMockResponse();
  const originalSecret = process.env.JWT_SECRET;

  delete process.env.JWT_SECRET;

  try {
    await login(req, res);

    assert.equal(res.statusCode, 500);
    assert.equal(res.body.error, "JWT secret is not configured");
  } finally {
    process.env.JWT_SECRET = originalSecret;
  }
});
