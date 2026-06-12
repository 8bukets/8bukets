import { processContent, persistKnowledge } from '../antigravity/services/knowledge_observer';

const intelephenseDocs = `
# Intelephense Documentation

## Getting Started

### About
Intelephense is a high performance, cross platform, cross editor PHP language server adhering to the Language Server Protocol (LSP).
When paired with an LSP capable editor it provides an essential set of code tools, making for a productive and rich PHP coding experience.
The Intelephense server is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to premium features can be obtained by purchasing a licence key.

## Installation

### Visual Studio Code
Visual Studio Code users should install the Intelephense extension from within the extensions view or download it from the VSCode marketplace.
The built-in VSCode PHP Language Features extension can cause excessive completion suggestions that are out of context and is best disabled. Go to the Extensions UI and search for PHP Language Features to disable it. Alternatively, you can disable parts of it via it's configuration settings. Other third party extensions that provide similar functionality to Intelephense may also need to be disabled for best results.
Optionally purchase and enter your licence key by opening the command palette (Ctrl+Shift+P) and searching for Enter licence key.

### Other Editors
Intelephense requires a Node.js runtime environment. It is recommended that you use a current LTS version of Node.js. To install Intelephense server you can use npm: npm i intelephense -g.
To start the intelephense server: intelephense {transport} where transport is one of --node-ipc, --stdio, --socket={number}, --pipe={string}.

## Configuration
Intelephense attempts to provide reasonable defaults for all settings. Important settings include:
- intelephense.files.associations: File globs that identify PHP files.
- intelephense.files.maxSize: Maximum file size in bytes to index (default 1MB).
- intelephense.environment.phpVersion: PHP version to use for analysis.
- intelephense.stubs: List of stubs to include.
Supports intelephense.config.json in workspace folder if client doesn't support workspace/configuration.

## Type System
Type information can be provided via coded type declarations or PHPDoc type annotations. PHPDoc is given precedence.
- Type Narrowing: Performs type narrowing of variables during control flow analysis (is_string, instanceof, etc.).
- Type Evolving: Change in a variable's type after an assignment expression.
- Supported Types: mixed, never, int, float, bool, string, void, null, true, false, unset, Literal Types, Object Types (shapes), array (generic, shapes), callable (signatures), iterable, Union, Intersection, DNF, Generics (@template), Conditional Return Type, Array Key/Value Types, Index Access Type.

## PHPDoc Annotations
Supports standard and non-standard annotations: @template, @template-extends, @template-implements, @template-use, @param-closure-this, @param-out, @assert, @assert-if-true, @assert-if-false, @mixin, @disregard, @type-alias, @import-type.

## Features
- FREE: Workspace Symbols, Document Symbols, Go to Definition, Hover, Highlight, Code Completion, Signature Help, Find All References, Formatting, Diagnostics, Inline Values, Embedded Languages.
- PREMIUM: Rename, Code Folding, Find All Implementations, Go to Type Definition, Go to Declaration, Smart Select, Type Hierarchy, Code Lens (References, Implementations, Overrides, Parent, Usages), Inlay Hints (Parameter Name, Parameter Type, Return Type), Document Links, Code Actions (Import Symbol, Add PHPDoc, Implement All Abstract Methods).

## Appendix
- Compatibility With Frameworks: Workarounds for runtime symbols and magic methods (type narrowing, helper files).
- PHPDoc vs PHPStorm Metadata: Recommends PHPDoc types for better compatibility. Supports @template and array shapes as alternatives to PHPStorm's metadata/attributes.
`;

async function main() {
  'use cache'
  console.log('🚀 Starting Intelephense documentation ingestion...');
  const insights = processContent(intelephenseDocs, 'User-Provided Documentation: Intelephense', 'Intelephense Documentation');

  // Customizing insights for better representation
  insights.description = 'Comprehensive Intelephense documentation including installation, configuration, type system, and features.';

  // Manually add some feature highlights as "posts"
  insights.recentPosts = [
    { title: 'Intelligence: Type System & Narrowing', link: 'https://intelephense.com/#type-system' },
    { title: 'Intelligence: Control Flow Analysis', link: 'https://intelephense.com/#control-flow' },
    { title: 'Feature: Workspace Symbols (LSP)', link: 'https://intelephense.com/#workspace-symbols' },
    { title: 'Premium: Rename & Refactoring', link: 'https://intelephense.com/#premium' }
  ];

  await persistKnowledge(insights);
  console.log('✨ Ingestion complete.');
}

main().catch(console.error);
