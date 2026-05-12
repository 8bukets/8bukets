import test from "node:test";
import assert from "node:assert/strict";
import db from "../src/db/index.js";

process.env.NO_LISTEN = "1";

const { healthHandler } = await import("../src/server.js");

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

test("GET /api/health returns ok when database healthcheck passes", async () => {
  const originalHealthcheck = db.healthcheck;
  const res = createMockResponse();

  db.healthcheck = async () => true;

  try {
    await healthHandler({}, res);

    assert.equal(res.statusCode, 200);
    assert.equal(res.body.ok, true);
    assert.equal(res.body.database, "ok");
  } finally {
    db.healthcheck = originalHealthcheck;
  }
});

test("GET /api/health returns 503 when database healthcheck fails", async () => {
  const originalHealthcheck = db.healthcheck;
  const res = createMockResponse();

  db.healthcheck = async () => {
    throw new Error("database unavailable");
  };

  try {
    await healthHandler({}, res);

    assert.equal(res.statusCode, 503);
    assert.equal(res.body.ok, false);
    assert.equal(res.body.database, "error");
  } finally {
    db.healthcheck = originalHealthcheck;
  }
});
