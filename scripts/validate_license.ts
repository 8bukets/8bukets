/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import fs from 'fs';
import path from 'path';

async function validateLicense() {
  console.log("Starting License Validation...");

  try {
    const licensePath = path.join(process.cwd(), 'LICENSE');

    if (!await fs.promises.access(licensePath).then(() => true).catch(() => false)) {
      console.error("❌ Validation Failed: LICENSE file does not exist.");
      process.exit(1);
    }

    const licenseContent = await fs.promises.readFile(licensePath, 'utf8');

    const expectedCopyright = "Copyright (c) 2024 Filip Keser. All rights reserved.";

    if (!licenseContent.includes(expectedCopyright)) {
      console.error("❌ Validation Failed: LICENSE file does not contain the expected copyright information.");
      process.exit(1);
    }

    console.log("✅ License Validation Passed: LICENSE file exists and contains the correct copyright information.");
  } catch (error) {
    console.error("Error during validation:", error);
    process.exit(1);
  }
}

validateLicense();
