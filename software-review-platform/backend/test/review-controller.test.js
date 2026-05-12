import test from "node:test";
import assert from "node:assert/strict";
import { createReview, rateReview } from "../src/controllers/reviewController.js";
import db from "../src/db/index.js";

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

test("createReview rejects short content", async () => {
  const req = {
    body: {
      software_id: 1,
      title: "Valid title",
      content: "too short",
      score: 5,
    },
    user: { id: 1, role: "user" },
  };
  const res = createMockResponse();

  await createReview(req, res);

  assert.equal(res.statusCode, 400);
  assert.equal(res.body.error, "Review must be at least 20 characters long");
});

test("createReview rejects out-of-range score", async () => {
  const req = {
    body: {
      software_id: 1,
      title: "Valid title",
      content: "This review has enough content to pass the length check.",
      score: 6,
    },
    user: { id: 1, role: "user" },
  };
  const res = createMockResponse();

  await createReview(req, res);

  assert.equal(res.statusCode, 400);
  assert.equal(res.body.error, "Score must be between 1 and 5");
});

test("createReview returns 404 when software does not exist", async () => {
  const req = {
    body: {
      software_id: 999,
      title: "Valid title",
      content: "This review has enough content to pass the length check.",
      score: 5,
    },
    user: { id: 1, role: "user" },
  };
  const res = createMockResponse();
  const originalQuery = db.query;

  db.query = async () => ({ rows: [] });

  try {
    await createReview(req, res);

    assert.equal(res.statusCode, 404);
    assert.equal(res.body.error, "Software not found");
  } finally {
    db.query = originalQuery;
  }
});

test("rateReview rejects out-of-range score", async () => {
  const req = {
    body: { score: 0 },
    params: { id: 1 },
    user: { id: 1, role: "user" },
  };
  const res = createMockResponse();

  await rateReview(req, res);

  assert.equal(res.statusCode, 400);
  assert.equal(res.body.error, "Score must be between 1 and 5");
});
