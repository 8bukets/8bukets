import test from "node:test";
import assert from "node:assert/strict";
import { getPendingReviews, moderateReview } from "../src/controllers/reviewController.js";

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

test("getPendingReviews rejects non-admin users", async () => {
  const req = { user: { role: "user" } };
  const res = createMockResponse();

  await getPendingReviews(req, res);

  assert.equal(res.statusCode, 403);
  assert.equal(res.body.error, "Admin access required");
});

test("moderateReview rejects non-admin users", async () => {
  const req = {
    user: { role: "user" },
    body: { status: "approved" },
    params: { id: 1 },
  };
  const res = createMockResponse();

  await moderateReview(req, res);

  assert.equal(res.statusCode, 403);
  assert.equal(res.body.error, "Admin access required");
});
