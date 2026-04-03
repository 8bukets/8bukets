import test from "node:test";
import assert from "node:assert/strict";
import jwt from "jsonwebtoken";
import { me } from "../src/controllers/authController.js";

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

test("me returns decoded user for valid bearer token", async () => {
  const originalSecret = process.env.JWT_SECRET;
  process.env.JWT_SECRET = "test-secret";

  const token = jwt.sign(
    { id: 7, email: "admin@example.com", role: "admin" },
    process.env.JWT_SECRET
  );
  const req = { headers: { authorization: `Bearer ${token}` } };
  const res = createMockResponse();

  try {
    await me(req, res);

    assert.equal(res.statusCode, 200);
    assert.equal(res.body.email, "admin@example.com");
    assert.equal(res.body.role, "admin");
  } finally {
    process.env.JWT_SECRET = originalSecret;
  }
});

test("me rejects missing token", async () => {
  const req = { headers: {} };
  const res = createMockResponse();

  await me(req, res);

  assert.equal(res.statusCode, 401);
  assert.equal(res.body.error, "No token");
});
