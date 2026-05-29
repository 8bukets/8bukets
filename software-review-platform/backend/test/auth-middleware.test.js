import test from "node:test";
import assert from "node:assert/strict";
import jwt from "jsonwebtoken";
import authMiddleware from "../src/middleware/auth.js";

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

test("auth middleware rejects requests without token", () => {
  const req = { headers: {} };
  const res = createMockResponse();
  let nextCalled = false;

  process.env.JWT_SECRET = "test-secret";

  authMiddleware(req, res, () => {
    nextCalled = true;
  });

  assert.equal(nextCalled, false);
  assert.equal(res.statusCode, 401);
  assert.equal(res.body.error, "No token");
});

test("auth middleware attaches decoded user for valid bearer token", () => {
  const token = jwt.sign({ id: 1, email: "user@example.com", role: "user" }, "test-secret");
  const req = { headers: { authorization: `Bearer ${token}` } };
  const res = createMockResponse();
  let nextCalled = false;

  process.env.JWT_SECRET = "test-secret";

  authMiddleware(req, res, () => {
    nextCalled = true;
  });

  assert.equal(nextCalled, true);
  assert.equal(req.user.email, "user@example.com");
  assert.equal(req.user.role, "user");
});
