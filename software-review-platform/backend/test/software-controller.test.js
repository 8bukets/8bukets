import test from "node:test";
import assert from "node:assert/strict";
import { getSoftware } from "../src/controllers/softwareController.js";
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

test("getSoftware applies q and category filters to the query", async () => {
  const originalQuery = db.query;
  let capturedSql = "";
  let capturedParams = [];

  db.query = async (sql, params) => {
    capturedSql = sql;
    capturedParams = params;
    return { rows: [] };
  };

  const req = { query: { q: "chat", category: "ai-productivity" } };
  const res = createMockResponse();

  try {
    await getSoftware(req, res);

    assert.equal(res.statusCode, 200);
    assert.match(capturedSql, /s\.name ILIKE/);
    assert.match(capturedSql, /s\.category = \$2/);
    assert.deepEqual(capturedParams, ["%chat%", "ai-productivity"]);
  } finally {
    db.query = originalQuery;
  }
});

test("getSoftware applies review-count sorting when requested", async () => {
  const originalQuery = db.query;
  let capturedSql = "";

  db.query = async (sql) => {
    capturedSql = sql;
    return { rows: [] };
  };

  const req = { query: { sort: "reviews" } };
  const res = createMockResponse();

  try {
    await getSoftware(req, res);

    assert.equal(res.statusCode, 200);
    assert.match(capturedSql, /ORDER BY review_count DESC, average_rating DESC, s\.name ASC/);
  } finally {
    db.query = originalQuery;
  }
});
