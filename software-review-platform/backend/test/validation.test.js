import test from "node:test";
import assert from "node:assert/strict";
import {
  isIntegerInRange,
  isValidEmail,
  isValidPassword,
  normalizedString,
} from "../src/utils/validation.js";

test("isValidEmail accepts normal email addresses", () => {
  assert.equal(isValidEmail("user@example.com"), true);
  assert.equal(isValidEmail(" user@example.com "), true);
});

test("isValidEmail rejects malformed values", () => {
  assert.equal(isValidEmail("not-an-email"), false);
  assert.equal(isValidEmail("user@localhost"), false);
  assert.equal(isValidEmail(""), false);
});

test("normalizedString trims strings and normalizes non-strings", () => {
  assert.equal(normalizedString("  hello  "), "hello");
  assert.equal(normalizedString(null), "");
});

test("isValidPassword enforces a minimum length", () => {
  assert.equal(isValidPassword("12345678"), true);
  assert.equal(isValidPassword("short"), false);
});

test("isIntegerInRange checks numeric boundaries", () => {
  assert.equal(isIntegerInRange(5, 1, 5), true);
  assert.equal(isIntegerInRange("3", 1, 5), true);
  assert.equal(isIntegerInRange(0, 1, 5), false);
  assert.equal(isIntegerInRange(6, 1, 5), false);
  assert.equal(isIntegerInRange("3.5", 1, 5), false);
});
