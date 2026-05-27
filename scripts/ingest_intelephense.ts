import { processContent, persistKnowledge } from '../antigravity/services/knowledge_observer';

const intelephenseDocs = `
Intelephense is a high performance, cross platform, cross editor PHP language server adhering to the Language Server Protocol (LSP).
When paired with an LSP capable editor it provides an essential set of code tools, making for a productive and rich PHP coding experience.
The Intelephense server is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to premium features can be obtained by purchasing a licence key.
Installation
Visual Studio Code
Intelephense requires a Node.js runtime environment. npm i intelephense -g
To start the intelephense server: intelephense {transport} --node-ipc --stdio --socket={number} --pipe={string}
Type System
Providing type information in your PHP code will result in a better experience when using Intelephense. Type information can be provided via coded type declarations or PHPDoc type annotations.
Type Narrowing
Intelephense performs type narrowing of variables during control flow analysis. Type narrowing expressions include built-in type assertions such as is_string, custom type assertions annotated with @assert, instanceof, and equality expressions.
Type Evolving
Type evolving is the change in a variable's type after an assignment expression.
Supported Types: mixed, never, int, float, bool, string, void, null, true, false, unset, Literal Types, Object Types, Array Types, Callable Types, Alias Types, Union Types, Intersection Types, DNF Types, Generic Types, Conditional Return Type, Array Key Type, Array Value Type, Index Access Type.
PHPDoc Annotations: @template, @template-extends, @template-implements, @template-use, @param-closure-this, @param-out, @assert, @assert-if-true, @assert-if-false, @mixin, @disregard, @type-alias, @import-type.
Features: Workspace Symbols, Document Symbols, Go to Definition, Hover, Highlight, Code Completion, Signature Help, Find All References, Formatting, Diagnostics, Inline Values, Embedded Languages.
Premium Features: Rename, Code Folding, Find All Implementations, Go to Type Definition, Go to Declaration, Smart Select, Type Hierarchy, Code Lens, Inlay Hints, Document Links, Code Actions.
`;

async function main() {
  console.log('🚀 Starting Intelephense documentation ingestion...');
  const insights = processContent(intelephenseDocs, 'User-Provided Documentation: Intelephense');

  // Customizing insights for better representation
  insights.title = 'Intelephense - PHP Language Server';
  insights.description = 'High performance PHP language server adhering to LSP with premium features.';

  // Manually add some feature highlights as "posts"
  insights.recentPosts = [
    { title: 'Intelligence: Type System & Narrowing', link: 'https://intelephense.com/#type-system' },
    { title: 'Intelligence: Control Flow Analysis', link: 'https://intelephense.com/#control-flow' },
    { title: 'Feature: Workspace Symbols (LSP)', link: 'https://intelephense.com/#workspace-symbols' },
    { title: 'Premium: Rename & Refactoring', link: 'https://intelephense.com/#premium' }
  ];

  persistKnowledge(insights);
  console.log('✨ Ingestion complete.');
}

main().catch(console.error);
