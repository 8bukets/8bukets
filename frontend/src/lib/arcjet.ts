import arcjet, { shield, fixedWindow, detectBot } from "@arcjet/next";

export default arcjet({
  key: process.env.ARCJET_KEY!,
  rules: [
    shield({
      mode: "LIVE",
    }),
    detectBot({
      mode: "LIVE",
      allow: ["CATEGORY:SEARCH_ENGINE"], // allow search engines
    }),
    fixedWindow({
      mode: "LIVE",
      window: "60s",
      max: 10,
    }),
  ],
});
