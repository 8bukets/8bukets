# Knowledge Observation Insights (Unified)

**Latest Source:** https://intelephense.com/docs
**Latest Analysis:** 2026-05-30T03:07:44.001Z

## About
Intelephense is a high performance, cross platform, cross editor PHP language server adhering to the Language Server Protocol (LSP).
When paired with an LSP capable editor it provides an essential set of code tools, making for a productive and rich PHP coding experience.
The Intelephense server is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to premium features can be obtained by purchasing a licence key.

## Visual Studio Code
Visual Studio Code users should install the Intelephense extension from within the extensions view or download it from the VSCode marketplace.
The built-in VSCode PHP Language Features extension can cause excessive completion suggestions that are out of context and is best disabled. Go to the Extensions UI and search for PHP Language Features to disable it. Alternatively, you can disable parts of it via it's configuration settings. Other third party extensions that provide similar functionality to Intelephense may also need to be disabled for best results.
Optionally purchase and enter your licence key by opening the command palette (Ctrl+Shift+P) and searching for Enter licence key.
A screen capture showing how to enter your intelephense licence key into VSCode.
Entering a licence key via the VS Code command palette

Visual Studio Code users should install the Intelephense extension from within the extensions view or download from the [marketplace](https://marketplace.visualstudio.com/items?itemName=bmewburn.vscode-intelephense-client).
1. Disable the built-in VSCode PHP Language Features.
* Go to `Extensions`.
* Search for `@builtin php`
* Disable `PHP Language Features`. Leave `PHP Language Basics` enabled for syntax highlighting.
Note that other (3rd party) PHP extensions which provide similar functionality should also be disabled for best results.
2. Add glob patterns for non standard php file extensions to the `files.associations` setting.
3. Optionally purchase and enter your [licence key](https://intelephense.com) by opening the command pallete
-- `ctrl + shift + p` -- and searching for `Enter licence key`.
Further configuration options are available in the `intelephense` section of settings.

## Configuration
Intelephense attempts to provide reasonable defaults for all settings. Some of the more important settings to consider when getting started include:
- **intelephense.files.associations** - File globs that identify PHP files. Defaults to standard PHP file extensions e.g. *.php.
- **intelephense.files.maxSize** - Maximum file size in bytes to index and provide analysis for. Defaults to 1000000 (1MB).
- **intelephense.environment.phpVersion** - PHP version to use for analysis. Defaults to the most recent stable PHP version.
- **intelephense.stubs** - List of stubs to include. Defaults to core symbols and extensions that are bundled with PHP. If you are getting undefined symbols for built-in or PECL extensions, you may need to modify this list.
In VSCode, the settings UI can be used to modify the configuration values. For other LSP clients, please see the client documentation on how to modify these values. Intelephense supports the LSP workspace/didChangeConfiguration and workspace/configuration methods as a way of supplying configuration values to the server.
If neither of the methods above are supported by the client, then configuration values can be supplied via an intelephense.config.json file placed in the workspace folder. The JSON schema for this file is the same as the one used for the VSCode client. The top level intelephense property is not required in this file.
For Intelephense to work effectively it must have access to the definitions of the symbols used in your code. Opening a project folder (LSP InitializeParams rootUri or workspaceFolders) rather than individual files enables these symbols to be discovered by Intelephense via indexing the PHP files in the folder. Large workspaces require more system resources. Consider opening a smaller workspace or exclude unnecessary files via the intelephense.files.exclude setting to reduce resource usage.
If you need to include files from outside of the workspace folder, then add the paths to these files to the intelephense.environment.includePaths setting.
When configuring a multi-root workspace, Intelephense will presume that the folders in the workspace are separate projects and will not provide cross folder symbols unless you link the dependency between the projects via the intelephense.environment.includePaths setting.
Depending on the framework or library you use, you may find you need additional configuration to provide method declarations or override existing ones. Please see the Frameworks and Libraries section in the appendix for more information on this.

## Supported Types
In the list of supported types below, some can only be used in PHPDoc as documented types. Please see the PHP type system documentation if you are unfamiliar with the standard PHP types. PHPDoc only, or internal types, are flagged with an asterisk.
Additional types used in other static analysis engines that are not listed here are not fully supported. Intelephense attempts to fallback to an appropriate alternative in this situation.

## Top Type
`mixed`
The super-type of all types. Any other type can be assigned to a type constraint of mixed. If intelephense cannot determine a more specific type for a symbol or expression then this is the type it is given. Because of this, Intelephense also allows mixed to be assigned to any other type constraint as well, effectively turning off type checking for that instance. To switch off this behaviour you can set both `intelephense.diagnostics.relaxedTypeCheck` and `intelephense.diagnostics.noMixedTypeCheck` to `false`.

## Bottom Type
`never`
The sub-type of all types. This type can be assigned to any other type constraint. It is used to represent an impossibility in the code and can be used as the return type of a function that exits or always throws an exception.

## Scalar Types
Any of these types can be assigned to the other unless the `declare(strict_types=1)` directive is used in the file or `intelephense.diagnostics.strictTypes` is `true`.
- `int`
- `float`
- `bool`
- `string`

## Unit Types
- `void`
- `null`
- `true`
- `false`
- `unset*` Intelephense uses this PHP keyword to represent the type of an undefined variable.

## Literal Types
- `'myString'*` String literals are encapsulated in quotes.
- `9*` An integer literal.

## Object Types
- `object`
- `\MyNs\MyClass` Classes, interfaces, traits, and enums can be fully qualified or not. If not fully qualified then the standard PHP name resolution rules apply to determine the fully qualified name.
- `static`
- `self`
- `$this*`

## Array Types
- `array`
- `array<TKey, TValue>*` Generic form for an array where the type arguments represent the array key and value types respectively. If only a single type argument is provided then it will be normalised to `array`.
- `TValue[]*` Represents a numeric indexed array where the element type is `TValue`.

## Callable Types
- `callable` Base callable type that represents a callable string, callable array or a class that implements `__invoke`.
- `callable(TParamA $a, TParamB $b): TReturn*` Callable type signatures can be defined to improve language intelligence. Parameter names are optional. The callable type should be wrapped in parentheses if it forms part of a union. `Closure` can be used instead of `callable` for a more specific type.

## Alias Types
- `iterable` Alias for `Traversable|array`.
- `?A` Nullable type that is shorthand for `null|A`. Cannot be used as part of a union or intersection type.

## Union Types
`A|B|C`
A type which may have multiple atomic type representations. For example, a type constraint of `A|B` can be assigned type `A` or `B`.

## Intersection Types
`A&B&C`
A composite type which consists of multiple atomic types. For example, a type of `A&B` can be assigned to type `A` and to type `B`.

## DNF Types
`A|B|(C&D&E)`
When combining union and intersection types, only a single level of nesting is permitted. The union must be the top level.

## Generic Types
`MyType*`
A generic type can be declared using one or many `@template` PHPDoc annotations above the target class, interface, or trait. Type arguments can then be supplied in the same order as the `@template` declarations. The following built-in types are templated:
- `iterable<TKey, TValue>`
- `Traversable<TKey, TValue>`
- `array<TKey, TValue>`
- `Iterator<TKey, TValue>`
- `IteratorAggregate<TKey, TValue>`
- `ArrayAccess<TKey, TValue>`
- `WeakReference<TObject>`
- `WeakMap<TKey, TValue>`
- `Fiber<TStart, TResume, TReturn, TSuspend>`
- `DatePeriod<TDate, TEnd>`
- `ReflectionAttribute<TObject>`
- `ReflectionClass<TObject>`
- `Generator<TKey, TYield, TSend, TReturn>`
- `ArrayObject<TKey, TValue>`
- `SplDoublyLinkedList<TValue>`
- `SplQueue<TValue>`
- `SplStack<TValue>`
- `SplHeap<TValue>`
- `SplMinHeap<TValue>`
- `SplMaxHeap<TValue>`
- `SplPriorityQueue<TPriority, TValue>`
- `SplFixedArray<TValue>`
- `SplObjectStorage<TObject, TValue>`

## Conditional Return Type
`(TSubject is TCompare ? TTrue : TFalse)*`
Sometimes the return type of a function may depend on the type of a parameter. A conditional type can be used without templates too by using the parameter name. For example, `($myParam is string ? string : null)`. Conditional types must be wrapped in parentheses. Conditional types may also be nested.

## Array Key Type
`key-of<TArray>*`
This type will resolve to a union of the keys of an array shape.

## Array Value Type
`value-of<TArray>*`
This type will resolve to a union of the values of an array shape.

## Miscellaneous Types
- `resource*`
- `class-string<T>*` A string where the value is the name of class `T`.

## PHPDoc Annotations
Intelephense supports standard PHPDoc annotations as well as non-standard annotations which have been popularised by other static analysis tools such as Psalm and PHPStan. The below list describes the non-standard annotations that Intelephense supports. For further information on standard PHPDoc annotations, please see the PHP_FIG and phpDocumentor references.
Some libraries or projects that have adopted static analysis tools such as Psalm or PHPStan may prefix some annotations with the tool name to avoid conflicts with other tools.
To make Intelephense prefer these prefixed annotations over the un-prefixed ones, you can set the `intelephense.compatibility.preferPsalmPhpstanPrefixedAnnotations` setting to `true`. Intelephense does not aim to support all types and features of these tools but will attempt to fallback to appropriate alternatives where possible.

## @template
`/** @template TemplateName of OptionalTypeConstraint = OptionalDefaultType */`
This annotation is used to declare a type argument of a generic type, function or method. The order that the template types appear is the same order in which the type arguments must be supplied in a generic type expression. The template type can be optionally constrained to a specific type and given an optional default type to be used when no type argument is supplied.

## @template-extends
`/** @template-extends ParentType */`
This annotation is used to declare the type arguments supplied to a generic parent type. It can be used on classes and interfaces when extending a parent class or interface. The alias `@extends` is also supported.

## @template-implements
`/** @template-implements InterfaceType */`
This annotation is used to declare the type arguments supplied to a generic interface. It can be used on classes and enums when implementing an interface. The alias `@implements` is also supported.

## @template-use
`/** @template-use TraitType */`
This annotation is used to declare the type arguments supplied to a generic trait. It can be used on classes, traits and enums when using a trait. The alias `@use` is also supported.

## @param-closure-this
`/** @param-closure-this Type $parameter */`
This annotation is used to declare the type of the `$this` variable inside a closure that is passed as a parameter to a function or method. An example of a standard PHP method that benefits internally from this annotation is `Closure::bind()`.

## @param-out
`/** @param-out Type &$parameter */`
This annotation is used to declare the out type of a by-reference parameter. Intelephense will not modify the type of a by-reference parameter unless this annotation is used.

## @assert
`/** @assert Type $parameter */`
This annotation is used to declare a function or method that asserts that an argument is of the specified type. Intelephense will narrow the type of the passed variable to the asserted type after the function or method call. It is presumed that the function or method has no false path and that it will throw an exception or exit if the assertion fails.

## @assert-if-true @assert-if-false
`/** @assert-if-true Type $parameter */`
Similar to above but for functions or methods that have a boolean return type. This asserts that the passed variable is of the specified type on the true or false code path respectively at the call location.

## @mixin
`/** @mixin ClassName */`
This annotation is used to declare that the members of the specified class are mixed in to the current class via `__call`, `__callStatic`, `__get` or `__set` magic methods. Only available with a licence in Intelephense Premium.

## @disregard
`/** @disregard PXXXX */`
This annotation is used to suppress a specific diagnostic at the statement following the annotation. For example, `@disregard P1010` would suppress the diagnostic with code `P1010`. This can be useful when you have a specific case where you want to allow something that Intelephense would normally report as an issue.

## @type-alias
`/** @type-alias TypeName = Type */`
This annotation is used to declare a type alias. A type alias allows you to create a new name for an existing type, which can be useful for improving code readability or for creating more meaningful type names. It functions the same as `@phpstan-type` and `@psalm-type` annotations which are also recognised. Intelephense type aliases follow normal PHP namespace rules.

## @import-type
`/** @import-type TypeName as OptionalAlias */`
This annotation is used to import a type alias that has been declared in another file. It functions similarly to `@phpstan-import-type` and `@psalm-import-type` and both these annotations may also be used. However, type aliases are not bound to classes in Intelephense and as such the `from ClassName` specifier is unnecessary but still supported. Type aliases in Intelephense follow normal PHP namespace rules.

## Features
Intelephense provides a variety of features to enhance the development experience when working with PHP code. Many of these features are provided for free while others require a Premium licence to access. All images and videos in this section are taken from the VS Code client. The features are available to all LSP clients that support the relevant LSP methods. Keybindings listed for each feature are the defaults for the VS Code client.

## Free Features
The following features are available to all users of Intelephense. A licence is not necessary.

## Workspace Symbols
- **Availability:** FREE
- **LSP:** `workspace/symbol`
- **Keybinding:** `Ctrl+T`
This feature allows you to search for symbols in your workspace and navigate to their definitions. It is particularly useful for finding and navigating to symbols that are not directly referenced in the current file. When the query contains alphanumeric characters only, the search is performed on the unqualified name of the symbol. You can narrow your search to a specific symbol by using a query containing characters found in the Fully Qualified Structural Element Name (FQSEN) of the symbol. For example, a query of `m\pt:u(` would find the method with FQSEN `App\Models\Post::user()`.
Unfortunately, VS Code has a current issue where it will discard results if the query contains a backslash. This means that you cannot search on the namespace part of a type.

## Document Symbols
- **Availability:** FREE
- **LSP:** `textDocument/documentSymbol`
- **Keybinding:** `Ctrl+Shift+O`
This feature lists all symbols in the current document, providing an overview of the structure of the file. A client can use this information to provide a document outline view, breadcrumb navigation, and a symbol search specific to the current file.

## Go to Definition
- **Availability:** FREE
- **LSP:** `textDocument/definition`
- **Keybinding:** `F12` | right-click context menu
This feature allows you to navigate to the definition of a symbol when invoked on a reference to that symbol in the current file. Multiple definitions may sometimes be found for a symbol. For example, invoking the feature on the type name in a new expression may find both the constructor method and the class declaration as definitions. It is up to the client to decide how to present multiple definitions to the user. For example a peek definitions window may open or the user may simply be navigated to the first definition in the list.

## Hover
- **Availability:** FREE
- **LSP:** `textDocument/hover`
- **Keybinding:** `Ctrl+K Ctrl+I` | mouse-over
This feature provides information about a symbol when hovering over a reference to that symbol in the current file. The information provided can include the type of the symbol, it's signature if it is a function or method, and any associated documentation.

## Highlight
- **Availability:** FREE
- **LSP:** `textDocument/documentHighlight`
- **Keybinding:** Displayed automatically at the cursor position
This feature highlights all references to the symbol at the cursor position in the current file. This can be useful for quickly identifying all usages of a symbol in the current file. Read and write contexts will be identified if applicable and the client can choose to highlight them differently if desired.

## Code Completion
- **Availability:** FREE
- **LSP:** `textDocument/completion`
- **Keybinding:** `Ctrl+Space`
- **Trigger characters:** `$ > : \ / ' " * . <`
This feature provides a list of context appropriate completion suggestions for a symbol at the cursor position in the current file. The completions can include variables, functions, methods, classes, and other symbols. Where appropriate, additional edits are provided to automatically import a symbol.

## Signature Help
- **Availability:** FREE
- **LSP:** `textDocument/signatureHelp`
- **Keybinding:** `Ctrl+Shift+Space`
- **Trigger characters:** `( , :`
This feature provides information about the signature of a function or method when the cursor is within the argument list of a function or method call. The information provided can include the types of the parameters, the return type, and any associated documentation.

## Find All References
- **Availability:** FREE
- **LSP:** `textDocument/references`
- **Keybinding:** `Shift+F12` | right-click context menu
This feature provides a list of all references to a symbol in the current file or workspace. The references can include variables, functions, methods, classes, and other symbols. When there is a hierarchy of types, references to a type member will be determined relative to the initial base members.

## Formatting
- **Availability:** FREE
- **LSP:** `textDocument/formatting`
- **Keybinding:** `Ctrl+Shift+I` (format document)
- **LSP:** `textDocument/rangeFormatting`
- **Keybinding:** `Ctrl+K Ctrl+F` (format selection)
This feature provides formatting of a whole document or a selected range within a document. The Intelephense formatter is opinionated and aims to comply with PHP-FIG coding standards. Limited configuration options are available to allow some customisation of brace style.

## Diagnostics
- **Availability:** FREE
- **LSP:** `textDocument/publishDiagnostics`
- **Keybinding:** Published automatically `onType` or `onSave` | `F8` (next) | `Shift+F8` (previous)
This feature provides diagnostics for the currently opened files. Diagnostics include syntax errors, type errors, language constraints and other issues detected by Intelephense. Intelephense aims to provide rapid diagnostics that are aligned with the PHP engine where possible.
Performance and minimising false positives are prioritised over exhaustiveness. It should not be used as a substitute for testing your code. The diagnostics emitted can be configured in the settings to be more or less thorough or ignored altogether depending on your preferences and the codebase you are working with.
If you need fine grain control over which diagnostics are shown, try the `intelephense.diagnostics.exclude` setting. This setting allows you to map a file glob to an array of diagnostic codes to exclude from diagnostics. A full list of diagnostic codes can be found in the vscode-intelephense repository.
By default, Intelephense performs type checking on declared types only and in a relaxed mode in order to reduce false positives. In a hierarchy of types, a sub-type satisfies a super-type constraint. Intelephense also permits the reverse. That is, a super-type or wider type can be assigned to a sub-type or narrower type constraint. This default behaviour has been chosen due to inherent limitations in static analysis, the lack of syntax in PHP or PHPDoc to enable a developer to inline cast an expression or variable, and due to the variable quality of type information in some codebases.
To make type checks more thorough, there are several settings available.
- `intelephense.diagnostics.relaxedTypeCheck` controls whether to emit diagnostics when a super-type (excluding mixed) is assigned to a sub-type constraint.
- `intelephense.diagnostics.noMixedTypeCheck` controls whether to emit diagnostics when mixed is assigned to narrower type constraints.
- `intelephense.diagnostics.strictTypes` is a global equivalent to adding `declare(strict_types=1);` to the top of each file.
- `intelephense.diagnostics.typeCheckDocumentedTypes` controls whether documented types are included in type checking.

## Inline Values
- **Availability:** FREE
- **LSP:** `textDocument/inlineValues`
- **Keybinding:** Displayed automatically during a debug session
This feature provides ranges and text for variables in a file that may be relevant for a debugger to display inline values for during a debugging session. To see this feature in action in VS Code, install the official Xdebug extension.

## Embedded Languages
Intelephense presumes that text outside of PHP tags is HTML. Basic language intelligence is provided for HTML and embedded CSS and JavaScript within HTML.

## Premium Features
The following features require a licence to access. A licence can be purchased at the checkout page.

## Rename
- **Availability:** PREMIUM
- **LSP:** `textDocument/rename`
- **Keybinding:** `F2` | right-click context menu
This feature allows you to rename a symbol and all references to that symbol in the current file or workspace. This differs from a simple text find and replace in that it is aware of the syntax and semantics of the code, and will only rename the specific symbol.
Intelephense will prefer to limit renames to the current file if possible. For example, renaming a class reference in a file where the class has been imported with a use declaration will result in the references in that file only being renamed and the use declaration being updated with an alias. In such cases, to rename a symbol across the whole workspace, invoke the rename feature on the class declaration itself or the Fully Qualified Name (FQN) in the use declaration instead.
Renaming a namespace in a file updates imports and FQN references for the file symbols in that namespace through the workspace. If using PSR-4 style folder structures then renaming the namespace of a class is also the equivalent of a move class to file operation. Intelephense will return file rename instructions to the client in such cases.

## Code Folding
- **Availability:** PREMIUM
- **LSP:** `textDocument/foldingRange`
- **Keybinding:** `Ctrl+Shift+[` (fold) | `Ctrl+Shift+]` (unfold) | left-click editor gutter | right-click context menu
This feature allows you to fold and unfold regions of code in the current file. Intelephense provides folding ranges for symbol definition bodies, control structures, comments, imports, and custom regions identified by `#region` and `#endregion` comments. The folding provider is syntax tree driven and is more reliable than indent based folding providers such as the default provider in VS Code.

## Find All Implementations
- **Availability:** PREMIUM
- **LSP:** `textDocument/implementation`
- **Keybinding:** `Ctrl+F12` | right-click context menu
This feature provides a list of all implementations of a method or interface when invoked on a reference. This functions similar to go to definition but differs in that it will find the classes that implement the interface or methods that implement an abstract method declaration.

## Go to Type Definition
- **Availability:** PREMIUM
- **LSP:** `textDocument/typeDefinition`
- **Keybinding:** Right-click context menu
This feature allows you to navigate to the type definition of a variable. Similar to go to definition but differs in that it will navigate to the type definition rather than the variable declaration itself.

## Go to Declaration
- **Availability:** PREMIUM
- **LSP:** `textDocument/declaration`
- **Keybinding:** Right-click context menu
This feature allows you to navigate to the initial declaration of a symbol. Similar to go to definition, and depending on the context may function the same, it differs in that it will navigate to the initial declaration of a symbol in a hierarchy of types. For example, invoking this feature on a sub-type method reference will navigate to the initial declaration of the method in a super-type rather than the sub-type method declaration itself.

## Smart Select
- **Availability:** PREMIUM
- **LSP:** `textDocument/selectionRange`
- **Keybinding:** `Shift+Alt+→` (expand) | `Shift+Alt+←` (shrink)
This feature allows you to expand and shrink the current selection in the current file based on the syntax tree of the code. For example, if the cursor is on a variable name, the first expansion would select the variable name, the second expansion would select the whole variable declaration, the third expansion would select the whole statement, the fourth expansion would select the whole block, and so on. Being syntax tree driven, it is more precise than regex or indent based selection providers such as the default provider in VS Code.

## Type Hierarchy
- **Availability:** PREMIUM
- **LSP:** `textDocument/typeHierarchy`
- **Keybinding:** Right-click context menu
This feature provides a type hierarchy for a class, interface, trait or enum when invoked on a reference to the type. It is useful for understanding the inheritance structure of a type and for quick navigation to types in the hierarchy.

## Code Lens
- **Availability:** PREMIUM
- **LSP:** `textDocument/codeLens`
- **Keybinding:** Rendered inline above declarations | activated by left-clicking
This feature provides additional information and navigation for symbol declarations in the current file. Several lenses are provided by Intelephense. They are disabled by default to reduce visual clutter, see the `intelephense.codeLens` settings to enable them.
- **References**: shows the number of references to a symbol in the workspace and provides a link to view those references.
- **Implementations**: shows the number of implementations of an interface or abstract method and provides a link to view those implementations.
- **Overrides**: shows the number of overrides of a method in a type hierarchy and provides a link to view those overrides.
- **Parent**: shows whether a method overrides a parent method and provides a link to view the parent method.
- **Usages**: shows the number of types that use a trait and provides a link to view those usages.

## Inlay Hints
- **Availability:** PREMIUM
- **LSP:** `textDocument/inlayHint`
- **Keybinding:** Displayed inline automatically
This feature provides additional type and parameter information in the form of hints that are displayed inline with the code in the current file. Intelephense provides several types of inlay hints. They are enabled by default. See the `intelephense.inlayHints` settings to configure them.
- **Parameter Name**: shows the name of a parameter for a function or method argument.
- **Parameter Type**: shows the inferred type of a parameter in a closure that is an argument to another function or method when it has not been explicitly declared.
- **Return Type**: shows the inferred return type of a function or method when it has not been explicitly declared.

## Document Links
- **Availability:** PREMIUM
- **LSP:** `textDocument/documentLink`
- **Keybinding:** `Ctrl+Click` | mouse-over
This feature provides clickable links to related files and resources from the current file. Intelephense will show links to files referenced in `require` and `include` statements, and to local files referenced in `@see` annotations.
If your `require` statements are relative or you reference `$_SERVER['DOCUMENT_ROOT']`, you may need to configure the `intelephense.environment.documentRoot` setting to the correct path for the links to work. Intelephense will fallback to the workspace folder path if this setting has no value.

## Code Actions
- **Availability:** PREMIUM
- **LSP:** `textDocument/codeAction`
- **Keybinding:** `Ctrl+.` | left-click lightbulb
This feature provides a list of context appropriate actions that can be performed at the cursor position in the current file. VS Code will show a lightbulb icon on the current line when code actions are available. Intelephense provides several code actions.
- **Import Symbol**: Import (`use`) a type, function or constant to resolve an undefined symbol error.
- **Add PHPDoc**: Generate PHPDoc for functions, classes, and methods.
- **Implement All Abstract Methods**: Generate method stubs for all abstract methods that have not been implemented in a class.

## Intelephense
Intelephense is a high performance, cross platform PHP language server adhering to the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/).
When paired with an LSP capable editor it provides an essential set of code intelligence features that give a PHP developer a productive and rich editing experience.
This is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to all current and future features can be obtained by purchasing a licence key at https://intelephense.com.

## Requirements
[Node.js 12+](https://nodejs.org)

## Server Installation
```
npm i intelephense -g
```

## Language Server Protocol (LSP) Client
Intelephense needs an LSP compliant client to communicate with and integrate features into the editor. A list of editors and clients that support the LSP can be found at https://microsoft.github.io/language-server-protocol/implementors/tools/.
Please follow the setup guide of the relevant tool. The Information below may help in configuring the client.

## Framework Support
Intelephense aims to support all frameworks but does not implement framework specific solutions. Some frameworks are coded in a way that make it difficult to analyse. This may be because of lack of type declarations/annotations; heavy use of `__get`, `__set`, `__call`, `__callStatic` magic methods; or dynamic generation of class aliases at runtime.
Packages can be found online that aim to workaround these issues by providing stubs of symbols to help static analysers like Intelephense understand the code.
* Laravel - [barryvdh/laravel-ide-helper](https://github.com/barryvdh/laravel-ide-helper)


## Gemini CLI Remote Subagents

Gemini CLI supports connecting to remote subagents using the Agent-to-Agent (A2A) protocol. This allows Gemini CLI to interact with other agents, expanding its capabilities by delegating tasks to remote services.

Gemini CLI can connect to any compliant A2A agent. You can find samples of A2A agents in the following repositories:

* ADK Samples (Python)
* ADK Python Contributing Samples

## Proxy support
Gemini CLI routes traffic to remote agents through an HTTP/HTTPS proxy if one is configured. It uses the `general.proxy` setting in your `settings.json` file or standard environment variables (`HTTP_PROXY`, `HTTPS_PROXY`).

```json
{
  "general": {
    "proxy": "http://my-proxy:8080"
  }
}
```

## Defining remote subagents
Remote subagents are defined as Markdown files (`.md`) with YAML frontmatter. You can place them in:

* Project-level: `.gemini/agents/*.md` (Shared with your team)
* User-level: `~/.gemini/agents/*.md` (Personal agents)

### Configuration schema

| Field | Type | Required | Description |
|---|---|---|---|
| `kind` | string | Yes | Must be `remote`. |
| `name` | string | Yes | A unique name for the agent. Must be a valid slug (lowercase letters, numbers, hyphens, and underscores only). |
| `agent_card_url` | string | Yes* | The URL to the agent’s A2A card endpoint. Required if `agent_card_json` is not provided. |
| `agent_card_json` | string | Yes* | The inline JSON string of the agent’s A2A card. Required if `agent_card_url` is not provided. |
| `auth` | object | No | Authentication configuration. See Authentication. |

### Single-subagent example

```yaml
---
kind: remote
name: my-remote-agent
agent_card_url: https://example.com/agent-card
---
```

### Multi-subagent example
The loader explicitly supports multiple remote subagents defined in a single Markdown file.

```yaml
---
- kind: remote
  name: remote-1
  agent_card_url: https://example.com/1
- kind: remote
  name: remote-2
  agent_card_url: https://example.com/2
---
```

> **Note**
> Mixed local and remote agents, or multiple local agents, are not supported in a single file; the list format is currently remote-only.

### Inline Agent Card JSON
View formatting options for JSON strings

## Authentication
Many remote agents require authentication. Gemini CLI supports several authentication methods aligned with the A2A security specification. Add an `auth` block to your agent’s frontmatter to configure credentials.

### Supported auth types
Gemini CLI supports the following authentication types:

| Type | Description |
|---|---|
| `apiKey` | Send a static API key as an HTTP header. |
| `http` | HTTP authentication (Bearer token, Basic credentials, or any IANA-registered scheme). |
| `google-credentials` | Google Application Default Credentials (ADC). Automatically selects access or identity tokens. |
| `oauth` | OAuth 2.0 Authorization Code flow with PKCE. Opens a browser for interactive sign-in. |

### Dynamic values
For `apiKey` and `http` auth types, secret values (key, token, username, password, value) support dynamic resolution:

| Format | Description | Example |
|---|---|---|
| `$ENV_VAR` | Read from an environment variable. | `$MY_API_KEY` |
| `!command` | Execute a shell command and use the trimmed output. | `!gcloud auth print-token` |
| `literal` | Use the string as-is. | `sk-abc123` |
| `$$` / `!!` | Escape prefix. `$$FOO` becomes the literal `$FOO`. | `$$NOT_AN_ENV_VAR` |

> Security tip: Prefer `$ENV_VAR` or `!command` over embedding secrets directly in agent files, especially for project-level agents checked into version control.

### API key (`apiKey`)
Sends an API key as an HTTP header on every request.

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `apiKey`. |
| `key` | string | Yes | The API key value. Supports dynamic values. |
| `name` | string | No | Header name to send the key in. Default: `X-API-Key`. |

```yaml
---
kind: remote
name: my-agent
agent_card_url: https://example.com/agent-card
auth:
  type: apiKey
  key: $MY_API_KEY
---
```

### HTTP authentication (`http`)
Supports Bearer tokens, Basic auth, and arbitrary IANA-registered HTTP authentication schemes.

#### Bearer token
Use the following fields to configure a Bearer token:

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `http`. |
| `scheme` | string | Yes | Must be `Bearer`. |
| `token` | string | Yes | The bearer token. Supports dynamic values. |

```yaml
auth:
  type: http
  scheme: Bearer
  token: $MY_BEARER_TOKEN
```

#### Basic authentication
Use the following fields to configure Basic authentication:

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `http`. |
| `scheme` | string | Yes | Must be `Basic`. |
| `username` | string | Yes | The username. Supports dynamic values. |
| `password` | string | Yes | The password. Supports dynamic values. |

```yaml
auth:
  type: http
  scheme: Basic
  username: $MY_USERNAME
  password: $MY_PASSWORD
```

#### Raw scheme
For any other IANA-registered scheme (for example, Digest, HOBA), provide the raw authorization value.

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `http`. |
| `scheme` | string | Yes | The scheme name (for example, Digest). |
| `value` | string | Yes | Raw value sent as `Authorization: <scheme> <value>`. Supports dynamic values. |

```yaml
auth:
  type: http
  scheme: Digest
  value: $MY_DIGEST_VALUE
```

### Google Application Default Credentials (`google-credentials`)
Uses Google Application Default Credentials (ADC) to authenticate with Google Cloud services and Cloud Run endpoints. This is the recommended auth method for agents hosted on Google Cloud infrastructure.

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `google-credentials`. |
| `scopes` | string[] | No | OAuth scopes. Defaults to `https://www.googleapis.com/auth/cloud-platform`. |

```yaml
---
kind: remote
name: my-gcp-agent
agent_card_url: https://my-agent-xyz.run.app/.well-known/agent.json
auth:
  type: google-credentials
---
```

#### How token selection works
The provider automatically selects the correct token type based on the agent’s host:

| Host pattern | Token type | Use case |
|---|---|---|
| `*.googleapis.com` | Access token | Google APIs (Agent Engine, Vertex AI, etc.) |
| `*.run.app` | Identity token | Cloud Run services |

Access tokens authorize API calls to Google services. They are scoped (default: `cloud-platform`) and fetched via `GoogleAuth.getClient()`.
Identity tokens prove the caller’s identity to a service that validates the token’s audience. The audience is set to the target host. These are fetched via `GoogleAuth.getIdTokenClient()`.
Both token types are cached and automatically refreshed before expiry.

#### Setup
`google-credentials` relies on ADC, which means your environment must have credentials configured. Common setups:

* Local development: Run `gcloud auth application-default login` to authenticate with your Google account.
* CI / Cloud environments: Use a service account. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file, or use workload identity on GKE / Cloud Run.

#### Allowed hosts
For security, `google-credentials` only sends tokens to known Google-owned hosts:

* `*.googleapis.com`
* `*.run.app`

Requests to any other host will be rejected with an error. If your agent is hosted on a different domain, use one of the other auth types (`apiKey`, `http`, or `oauth`).

#### Examples
The following examples demonstrate how to configure Google Application Default Credentials.

Cloud Run agent:

```yaml
---
kind: remote
name: cloud-run-agent
agent_card_url: https://my-agent-xyz.run.app/.well-known/agent.json
auth:
  type: google-credentials
---
```

Google API with custom scopes:

```yaml
---
kind: remote
name: vertex-agent
agent_card_url: https://us-central1-aiplatform.googleapis.com/.well-known/agent.json
auth:
  type: google-credentials
  scopes:
    - https://www.googleapis.com/auth/cloud-platform
    - https://www.googleapis.com/auth/compute
---
```

### OAuth 2.0 (`oauth`)
Performs an interactive OAuth 2.0 Authorization Code flow with PKCE. On first use, Gemini CLI opens your browser for sign-in and persists the resulting tokens for subsequent requests.

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `oauth`. |
| `client_id` | string | Yes* | OAuth client ID. Required for interactive auth. |
| `client_secret` | string | No* | OAuth client secret. Required by most authorization servers (confidential clients). Can be omitted for public clients that don’t require a secret. |
| `scopes` | string[] | No | Requested scopes. Can also be discovered from the agent card. |
| `authorization_url` | string | No | Authorization endpoint. Discovered from the agent card if omitted. |
| `token_url` | string | No | Token endpoint. Discovered from the agent card if omitted. |

```yaml
---
kind: remote
name: oauth-agent
agent_card_url: https://example.com/.well-known/agent.json
auth:
  type: oauth
  client_id: my-client-id.apps.example.com
---
```

If the agent card advertises an `oauth2` security scheme with `authorizationCode` flow, the `authorization_url`, `token_url`, and `scopes` are automatically discovered. You only need to provide `client_id` (and `client_secret` if required).

Tokens are persisted to disk and refreshed automatically when they expire.

### Auth validation
When Gemini CLI loads a remote agent, it validates your auth configuration against the agent card’s declared `securitySchemes`. If the agent requires authentication that you haven’t configured, you’ll see an error describing what’s needed.

`google-credentials` is treated as compatible with `http` Bearer security schemes, since it produces Bearer tokens.

### Auth retry behavior
All auth providers automatically retry on 401 and 403 responses by re-fetching credentials (up to 2 retries). This handles cases like expired tokens or rotated credentials. For `apiKey` with `!command` values, the command is re-executed on retry to fetch a fresh key.

### Agent card fetching and auth
When connecting to a remote agent, Gemini CLI first fetches the agent card without authentication. If the card endpoint returns a 401 or 403, it retries the fetch with the configured auth headers. This lets agents have publicly accessible cards while protecting their task endpoints, or to protect both behind auth.

## Managing Subagents
Users can manage subagents using the following commands within Gemini CLI:

* `/agents list`: Displays all available local and remote subagents.
* `/agents reload`: Reloads the agent registry. Use this after adding or modifying agent definition files.
* `/agents enable <agent_name>`: Enables a specific subagent.
* `/agents disable <agent_name>`: Disables a specific subagent.

> **Tip**
> You can use the `@cli_help` agent within Gemini CLI for assistance with configuring subagents.

### Disabling remote agents
Remote subagents are enabled by default. To disable them, set `enableAgents` to `false` in your `settings.json`:

```json
{
  "experimental": {
    "enableAgents": false
  }
}
```
## Gemini CLI Subagents

# Subagents

Subagents are specialized agents that operate within your main Gemini CLI session. They are designed to handle specific, complex tasks—like deep codebase analysis, documentation lookup, or domain-specific reasoning—without cluttering the main agent’s context or toolset.

## What are subagents?
Subagents are “specialists” that the main Gemini agent can hire for a specific job.

*   **Focused context:** Each subagent has its own system prompt and persona.
*   **Specialized tools:** Subagents can have a restricted or specialized set of tools.
*   **Independent context window:** Interactions with a subagent happen in a separate context loop, which saves tokens in your main conversation history.

Subagents are exposed to the main agent as a tool of the same name. When the main agent calls the tool, it delegates the task to the subagent. Once the subagent completes its task, it reports back to the main agent with its findings.

## How to use subagents
You can use subagents through automatic delegation or by explicitly forcing them in your prompt.

### Automatic delegation
Gemini CLI’s main agent is instructed to use specialized subagents when a task matches their expertise. For example, if you ask “How does the auth system work?”, the main agent may decide to call the `codebase_investigator` subagent to perform the research.

### Forcing a subagent (@ syntax)
You can explicitly direct a task to a specific subagent by using the `@` symbol followed by the subagent’s name at the beginning of your prompt. This is useful when you want to bypass the main agent’s decision-making and go straight to a specialist.

Example:

**Terminal window**
`@codebase_investigator Map out the relationship between the AgentRegistry and the LocalAgentExecutor.`

When you use the `@` syntax, the CLI injects a system note that nudges the primary model to use that specific subagent tool immediately.

## Built-in subagents
Gemini CLI comes with the following built-in subagents:

### Codebase Investigator
*   **Name:** `codebase_investigator`
*   **Purpose:** Analyze the codebase, reverse engineer, and understand complex dependencies.
*   **When to use:** “How does the authentication system work?”, “Map out the dependencies of the AgentRegistry class.”
*   **Configuration:** Enabled by default. You can override its settings in `settings.json` under `agents.overrides`. Example (forcing a specific model and increasing turns):

```json
{
  "agents": {
    "overrides": {
      "codebase_investigator": {
        "modelConfig": { "model": "gemini-3-flash-preview" },
        "runConfig": { "maxTurns": 50 }
      }
    }
  }
}
```

### CLI Help Agent
*   **Name:** `cli_help`
*   **Purpose:** Get expert knowledge about Gemini CLI itself, its commands, configuration, and documentation.
*   **When to use:** “How do I configure a proxy?”, “What does the /rewind command do?”
*   **Configuration:** Enabled by default.

### Generalist Agent
*   **Name:** `generalist`
*   **Purpose:** A general, all-purpose subagent that uses the inherited tool access and configurations from the main agent. Useful for executing broad, resource-heavy subtasks in an isolated conversation, optimizing your main agent’s context by returning only the final result of that given task.
*   **When to use:** Use this agent when a task requires many steps, handles large volumes of information, or requires the same full capabilities as the main agent. It is ideal for:
    *   **Multi-file modifications:** Applying refactors or fixing errors across several files at once.
    *   **High-volume execution:** Running commands or tests that produce extensive terminal output.
    *   **Action-oriented research:** Investigations where the agent needs to both search code and run commands or make edits to find a solution. By delegating these tasks, you prevent your main conversation from becoming cluttered or slow. You can invoke it explicitly using `@generalist`.
*   **Configuration:** Enabled by default.

### Browser Agent (experimental)
*   **Name:** `browser_agent`
*   **Purpose:** Automate web browser tasks — navigating websites, filling forms, clicking buttons, and extracting information from web pages — using the accessibility tree.
*   **When to use:** “Go to example.com and fill out the contact form,” “Extract the pricing table from this page,” “Click the login button and enter my credentials.”

> **Note**
> This is a preview feature currently under active development.

#### Prerequisites
The browser agent requires:

*   **Chrome version 144 or later** (any recent stable release works).
*   The underlying `chrome-devtools-mcp` server is bundled with Gemini CLI and launched automatically — no separate installation is needed.

#### Enabling the browser agent
The browser agent is disabled by default. Enable it in your `settings.json`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    }
  }
}
```

#### Session modes
The `sessionMode` setting controls how Chrome is launched and managed. Set it under `agents.browser`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    },
    "browser": {
      "sessionMode": "persistent"
    }
  }
}
```

The available modes are:

| Mode | Description |
| :--- | :--- |
| `persistent` | **(Default)** Launches Chrome with a persistent profile stored at `~/.gemini/cli-browser-profile/`. Cookies, history, and settings are preserved between sessions. |
| `isolated` | Launches Chrome with a temporary profile that is deleted after each session. Use this for clean-state automation. |
| `existing` | Attaches to an already-running Chrome instance. You must enable remote debugging first by navigating to `chrome://inspect/#remote-debugging` in Chrome. No new browser process is launched. |

#### First-run consent
The first time the browser agent is invoked, Gemini CLI displays a consent dialog. You must accept before the browser session starts. This dialog only appears once.

#### Configuration reference
All browser-specific settings go under `agents.browser` in your `settings.json`. For full details, see the `agents.browser` configuration reference.

| Setting | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `sessionMode` | `string` | `"persistent"` | How Chrome is managed: `"persistent"`, `"isolated"`, or `"existing"`. |
| `headless` | `boolean` | `false` | Run Chrome in headless mode (no visible window). |
| `profilePath` | `string` | — | Custom path to a browser profile directory. |
| `visualModel` | `string` | — | Model override for the visual agent. |
| `allowedDomains` | `string[]` | — | Restrict navigation to specific domains (for example, `["github.com"]`). |
| `disableUserInput` | `boolean` | `true` | Disable user input on the browser window during automation (non-headless only). |
| `maxActionsPerTask` | `number` | `100` | Maximum tool calls per task. The agent is terminated when the limit is reached. |
| `confirmSensitiveActions` | `boolean` | `false` | Require manual confirmation for `upload_file` and `evaluate_script`. |
| `blockFileUploads` | `boolean` | `false` | Hard-block all file upload requests from the agent. |

#### Automation overlay and input blocking
In non-headless mode, the browser agent injects a visual overlay into the browser window to indicate that automation is in progress. By default, user input (keyboard and mouse) is also blocked to prevent accidental interference. You can disable this by setting `disableUserInput` to `false`.

#### Security
The browser agent enforces several layers of security:

*   **Domain restrictions:** When `allowedDomains` is set, the agent can only navigate to the listed domains (and their subdomains when using `*.` prefix). Attempting to visit a disallowed domain throws a fatal error that immediately terminates the agent. The agent also attempts to detect and block the use of allowed domains as proxies (e.g., via query parameters or fragments) to access restricted content.
*   **Blocked URL patterns:** The underlying MCP server blocks dangerous URL schemes including `file://`, `javascript:`, `data:text/html`, `chrome://extensions`, and `chrome://settings/passwords`.
*   **Sensitive action confirmation:** Form filling (`fill`, `fill_form`) always requires user confirmation through the policy engine, regardless of approval mode. When `confirmSensitiveActions` is `true`, `upload_file` and `evaluate_script` also require confirmation.
*   **File upload blocking:** Set `blockFileUploads` to `true` to hard-block all file upload requests, preventing the agent from uploading any files.
*   **Action rate limiting:** The `maxActionsPerTask` setting (default: 100) limits the total number of tool calls per task to prevent runaway execution.

#### Visual agent
By default, the browser agent interacts with pages through the accessibility tree using element `uid` values. For tasks that require visual identification (for example, “click the yellow button” or “find the red error message”), you can enable the visual agent by setting a `visualModel`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    },
    "browser": {
      "visualModel": "gemini-2.5-computer-use-preview-10-2025"
    }
  }
}
```

When enabled, the agent gains access to the `analyze_screenshot` tool, which captures a screenshot and sends it to the vision model for analysis. The model returns coordinates and element descriptions that the browser agent uses with the `click_at` tool for precise, coordinate-based interactions.

> **Note**
> The visual agent requires API key or Vertex AI authentication. It is not available when using “Sign in with Google”.

#### Sandbox support
The browser agent adjusts its behavior automatically when running inside a sandbox.

**macOS seatbelt (sandbox-exec)**
When the CLI runs under the macOS seatbelt sandbox, `persistent` and `isolated` session modes are forced to `isolated` with headless enabled. This avoids permission errors caused by seatbelt file-system restrictions on persistent browser profiles. If `sessionMode` is set to `existing`, no override is applied.

**Container sandboxes (Docker / Podman)**
Chrome is not available inside the container, so the browser agent is disabled unless `sessionMode` is set to `"existing"`. When enabled with existing mode, the agent automatically connects to Chrome on the host via the resolved IP of `host.docker.internal:9222` instead of using local pipe discovery. Port `9222` is currently hardcoded and cannot be customized.

To use the browser agent in a Docker sandbox:

1.  Start Chrome on the host with remote debugging enabled:

    **Terminal window**
    ```bash
    # Option A: Launch Chrome from the command line
    google-chrome --remote-debugging-port=9222

    # Option B: Enable in Chrome settings
    # Navigate to chrome://inspect/#remote-debugging and enable
    ```
2.  Configure `sessionMode` and allowed domains in your project’s `.gemini/settings.json`:

    ```json
    {
      "agents": {
        "overrides": {
          "browser_agent": { "enabled": true }
        },
        "browser": {
          "sessionMode": "existing",
          "allowedDomains": ["example.com"]
        }
      }
    }
    ```
3.  Launch the CLI with port forwarding:

    **Terminal window**
    ```bash
    GEMINI_SANDBOX=docker SANDBOX_PORTS=9222 gemini
    ```

## Creating custom subagents
You can create your own subagents to automate specific workflows or enforce specific personas.

### Agent definition files
Custom agents are defined as Markdown files (`.md`) with YAML frontmatter. You can place them in:

*   **Project-level:** `.gemini/agents/*.md` (Shared with your team)
*   **User-level:** `~/.gemini/agents/*.md` (Personal agents)

### File format
The file MUST start with YAML frontmatter enclosed in triple-dashes `---`. The body of the markdown file becomes the agent’s System Prompt.

Example: `.gemini/agents/security-auditor.md`

```yaml
---
name: security-auditor
description: Specialized in finding security vulnerabilities in code.
kind: local
tools:
  - read_file
  - grep_search
model: gemini-3-flash-preview
temperature: 0.2
max_turns: 10
---
```

You are a ruthless Security Auditor. Your job is to analyze code for potential
vulnerabilities.

Focus on:

1.  SQL Injection
2.  XSS (Cross-Site Scripting)
3.  Hardcoded credentials
4.  Unsafe file operations

When you find a vulnerability, explain it clearly and suggest a fix. Do not fix
it yourself; just report it.

### Configuration schema

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | `string` | **Yes** | Unique identifier (slug) used as the tool name for the agent. Only lowercase letters, numbers, hyphens, and underscores. |
| `description` | `string` | **Yes** | Short description of what the agent does. This is visible to the main agent to help it decide when to call this subagent. |
| `kind` | `string` | No | `local` (default) or `remote`. |
| `tools` | `array` | No | List of tool names this agent can use. Supports wildcards: `*` (all tools), `mcp_*` (all MCP tools), `mcp_server_*` (all tools from a server). If omitted, it inherits all tools from the parent session. |
| `mcpServers` | `object` | No | Configuration for inline Model Context Protocol (MCP) servers isolated to this specific agent. |
| `model` | `string` | No | Specific model to use (for example, `gemini-3-preview`). Defaults to `inherit` (uses the main session model). |
| `temperature` | `number` | No | Model temperature (0.0 - 2.0). Defaults to `1`. |
| `max_turns` | `number` | No | Maximum number of conversation turns allowed for this agent before it must return. Defaults to `30`. |
| `timeout_mins` | `number` | No | Maximum execution time in minutes. Defaults to `10`. |

### Tool wildcards
When defining tools for a subagent, you can use wildcards to quickly grant access to groups of tools:

*   `*`: Grant access to all available built-in and discovered tools.
*   `mcp_*`: Grant access to all tools from all connected MCP servers.
*   `mcp_my-server_*`: Grant access to all tools from a specific MCP server named `my-server`.

### Isolation and recursion protection
Each subagent runs in its own isolated context loop. This means:

*   **Independent history:** The subagent’s conversation history does not bloat the main agent’s context.
*   **Isolated tools:** The subagent only has access to the tools you explicitly grant it.
*   **Recursion protection:** To prevent infinite loops and excessive token usage, subagents cannot call other subagents. If a subagent is granted the `*` tool wildcard, it will still be unable to see or invoke other agents.

## Subagent tool isolation
Subagent tool isolation moves Gemini CLI away from a single global tool registry. By providing isolated execution environments, you can ensure that subagents only interact with the parts of the system they are designed for. This prevents unintended side effects, improves reliability by avoiding state contamination, and enables fine-grained permission control.

With this feature, you can:

*   **Specify tool access:** Define exactly which tools an agent can access using a `tools` list in the agent definition.
*   **Define inline MCP servers:** Configure Model Context Protocol (MCP) servers (which provide a standardized way to connect AI models to external tools and data sources) directly in the subagent’s markdown frontmatter, isolating them to that specific agent.
*   **Maintain state isolation:** Ensure that subagents only interact with their own set of tools and servers, preventing side effects and state contamination.
*   **Apply subagent-specific policies:** Enforce granular rules in your Policy Engine TOML configuration based on the executing subagent’s name.

### Configuring isolated tools and servers
You can configure tool isolation for a subagent by updating its markdown frontmatter. This lets you explicitly state which tools the subagent can use, rather than relying on the global registry.

Add an `mcpServers` object to define inline MCP servers that are unique to the agent.

Example:

```yaml
---
name: my-isolated-agent
tools:
  - grep_search
  - read_file
mcpServers:
  my-custom-server:
    command: 'node'
    args: ['path/to/server.js']
---
```

### Subagent-specific policies
You can enforce fine-grained control over subagents using the Policy Engine’s TOML configuration. This allows you to grant or restrict permissions specifically for an agent, without affecting the rest of your CLI session.

To restrict a policy rule to a specific subagent, add the `subagent` property to the `[[rules]]` block in your `policy.toml` file.

Example:

```toml
[[rules]]
name = "Allow pr-creator to push code"
subagent = "pr-creator"
description = "Permit pr-creator to push branches automatically."
action = "allow"
toolName = "run_shell_command"
commandPrefix = "git push"
```

In this configuration, the policy rule only triggers if the executing subagent’s name matches `pr-creator`. Rules without the `subagent` property apply universally to all agents.

## Managing subagents
You can manage subagents interactively using the `/agents` command or persistently via `settings.json`.

### Interactive management (/agents)
If you are in an interactive CLI session, you can use the `/agents` command to manage subagents without editing configuration files manually. This is the recommended way to quickly enable, disable, or re-configure agents on the fly.

For a full list of sub-commands and usage, see the `/agents` command reference.

### Persistent configuration (settings.json)
While the `/agents` command and agent definition files provide a starting point, you can use `settings.json` for global, persistent overrides. This is useful for enforcing specific models or execution limits across all sessions.

`agents.overrides`
Use this to enable or disable specific agents or override their run configurations.

```json
{
  "agents": {
    "overrides": {
      "security-auditor": {
        "enabled": false,
        "runConfig": {
          "maxTurns": 20,
          "maxTimeMinutes": 10
        }
      }
    }
  }
}
```

`modelConfigs.overrides`
You can target specific subagents with custom model settings (like system instruction prefixes or specific safety settings) using the `overrideScope` field.

```json
{
  "modelConfigs": {
    "overrides": [
      {
        "match": { "overrideScope": "security-auditor" },
        "modelConfig": {
          "generateContentConfig": {
            "temperature": 0.1
          }
        }
      }
    ]
  }
}
```

### Safety policies (TOML)
You can restrict access to specific subagents using the CLI’s Policy Engine. Subagents are treated as virtual tool names for policy matching purposes.

To govern access to a subagent, create a `.toml` file in your policy directory (e.g., `~/.gemini/policies/`):

```toml
[[rule]]
toolName = "codebase_investigator"
decision = "deny"
deny_message = "Deep codebase analysis is restricted for this session."
```

For more information on setting up fine-grained safety guardrails, see the Policy Engine reference.

## Optimizing your subagent
The main agent’s system prompt encourages it to use an expert subagent when one is available. It decides whether an agent is a relevant expert based on the agent’s description. You can improve the reliability with which an agent is used by updating the description to more clearly indicate:

*   Its area of expertise.
*   When it should be used.
*   Some example scenarios.

For example, the following subagent description should be called fairly consistently for Git operations.

> Git expert agent which should be used for all local and remote git operations. For example:
> *   Making commits
> *   Searching for regressions with bisect
> *   Interacting with source control and issues providers such as GitHub.

If you need to further tune your subagent, you can do so by selecting the model to optimize for with `/model` and then asking the model why it does not think that your subagent was called with a specific prompt and the given description.

## Remote subagents (Agent2Agent)
Gemini CLI can also delegate tasks to remote subagents using the Agent-to-Agent (A2A) protocol.

See the Remote Subagents documentation for detailed configuration, authentication, and usage instructions.

## Extension subagents
Extensions can bundle and distribute subagents. See the Extensions documentation for details on how to package agents within an extension.

## Disabling subagents
Subagents are enabled by default. To disable them, set `enableAgents` to `false` in your `settings.json`:

```json
{
  "experimental": { "enableAgents": false }
}
```

# What is an AI agent?

**Source:** https://cloud.google.com/discover/what-are-ai-agents
**Analysis:** 2026-06-07T14:24:44.481607

## Key features of an AI agent
As explained above, while the key features of an AI agent are reasoning and acting (as described in ReAct Framework ) more features have evolved over time. Reasoning: This core cognitive process involves using logic and available information to draw conclusions, make inferences, and solve problems. AI agents with strong reasoning capabilities can analyze data, identify patterns, and make informed decisions based on evidence and context. Acting : The ability to take action or perform tasks based on decisions, plans, or external input is crucial for AI agents to interact with their environment and achieve goals. This can include physical actions in the case of embodied AI, or digital actions like sending messages, updating data, or triggering other processes. Observing : Gathering information about the environment or situation through perception or sensing is essential for AI agents to understand their context and make informed decisions. This can involve various forms of perception, such as computer vision, natural language processing, or sensor data analysis. Planning : Developing a strategic plan to achieve goals is a key aspect of intelligent behavior. AI agents with planning capabilities can identify the necessary steps, evaluate potential actions, and choose the best course of action based on available information and desired outcomes. This often involves anticipating future states and considering potential obstacles. Collaborating : Working effectively with others, whether humans or other AI agents, to achieve a common goal is increasingly important in complex and dynamic environments. Collaboration requires communication, coordination, and the ability to understand and respect the perspectives of others. Self-refining : The capacity for self-improvement and adaptation is a hallmark of advanced AI systems. AI agents with self-refining capabilities can learn from experience, adjust their behavior based on feedback, and continuously enhance their performance and capabilities over time. This can involve machine learning techniques, optimization algorithms, or other forms of self-modification.

## What is the difference between AI agents, AI assistants, and bots?
AI assistants are AI agents designed as applications or products to collaborate directly with users and perform tasks by understanding and responding to natural human language and inputs. They can reason and take action on the users' behalf with their supervision. AI assistants are often embedded in the product being used. A key characteristic is the interaction between the assistant and user through the different steps of the task. The assistant responds to requests or prompts from the user, and can recommend actions but decision-making is done by the user.

AI agent AI assistant Bot ﻿ Purpose Autonomously and proactively perform tasks Assisting users with tasks Automating simple tasks or conversations Capabilities Can perform complex, multi-step actions; learns and adapts; can make decisions independently Responds to requests or prompts; provides information and completes simple tasks; can recommend actions but the user makes decisions Follows pre-defined rules; limited learning; basic interactions Interaction Proactive; goal-oriented Reactive; responds to user requests Reactive; responds to triggers or commands AI agent AI assistant Bot ﻿ Purpose Autonomously and proactively perform tasks Assisting users with tasks Automating simple tasks or conversations Capabilities Can perform complex, multi-step actions; learns and adapts; can make decisions independently Responds to requests or prompts; provides information and completes simple tasks; can recommend actions but the user makes decisions Follows pre-defined rules; limited learning; basic interactions Interaction Proactive; goal-oriented Reactive; responds to user requests Reactive; responds to triggers or commands

## Key differences
Autonomy : AI agents have the highest degree of autonomy, able to operate and make decisions independently to achieve a goal. AI assistants are less autonomous, requiring user input and direction. Bots are the least autonomous, typically following pre-programmed rules. Complexity : AI agents are designed to handle complex tasks and workflows, while AI assistants and bots are better suited for simpler tasks and interactions. Learning : AI agents often employ machine learning to adapt and improve their performance over time. AI assistants may have some learning capabilities, while bots typically have limited or no learning.

## How do AI agents work?
Every agent defines its role, personality, and communication style, including specific instructions and descriptions of available tools. Persona : A well defined persona allows an agent to maintain a consistent character and behave in a manner appropriate to its assigned role, evolving as the agent gains experience and interacts with its environment. Memory : The agent is equipped in general with short term, long term, consensus, and episodic memory. Short term memory for immediate interactions, long-term memory for historical data and conversations, episodic memory for past interactions, and consensus memory for shared information among agents. The agent can maintain context, learn from experiences, and improve performance by recalling past interactions and adapting to new situations. Tools : Tools are functions or external resources that an agent can utilize to interact with its environment and enhance its capabilities. They allow agents to perform complex tasks by accessing information, manipulating data, or controlling external systems, and can be categorized based on their user interface, including physical, graphical, and program-based interfaces. Tool learning involves teaching agents how to effectively use these tools by understanding their functionalities and the context in which they should be applied. Model : Large language models (LLMs) serve as the foundation for building AI agents, providing them with the ability to understand, reason, and act. LLMs act as the "brain" of an agent, enabling them to process and generate language, while other components facilitate reason and action.

## What are the types of agents in AI?
AI agents can be categorized in various ways based on their capabilities, roles, and environments. Here are some key categories of agents: There are different definitions of agent types and agent categories.

## Based on interaction
One way to categorize agents is by how they interact with users. Some agents engage in direct conversation, while others operate in the background, performing tasks without direct user input: Interactive partners (also known as, surface agents): Assisting us with tasks like customer service, healthcare, education, and scientific discovery, providing personalized and intelligent support. Conversational agents include Q&A, chit chat, and world knowledge interactions with humans. They are generally user query triggered and fulfill user queries or transactions. Autonomous background processes (also known as, background agents): Working behind the scenes to automate routine tasks, analyze data for insights, optimize processes for efficiency, and proactively identify and address potential issues. They include workflow agents. They have limited or no human interaction and are generally driven by events and fulfill queued tasks or chains of tasks.

## Based on number of agents
Single agent : Operate independently to achieve a specific goal. They utilize external tools and resources to accomplish tasks, enhancing their functional capabilities in diverse environments. They are best suited for well defined tasks that do not require collaboration with other AI agents. Can only handle one foundation model for its processing. Multi-agent : Multiple AI agents that collaborate or compete to achieve a common objective or individual goals. These systems leverage the diverse capabilities and roles of individual agents to tackle complex tasks. Multi-agent systems can simulate human behaviors, such as interpersonal communication, in interactive scenarios. Each agent can have different foundation models that best fit their needs.

## Benefits of using AI agents
AI agents can enhance the capabilities of language models by providing autonomy, task automation, and the ability to interact with the real world through tools and embodiment.

## Challenges with using AI agents
While AI agents offer many benefits, there are also some challenges associated with their use: Tasks requiring deep empathy / emotional intelligence or requiring complex human interaction and social dynamics – AI agents can struggle with nuanced human emotions. Tasks like therapy, social work, or conflict resolution require a level of emotional understanding and empathy that AI currently lacks. They may falter in complex social situations that require understanding unspoken cues. Situations with high ethical stakes – AI agents can make decisions based on data, but they lack the moral compass and judgment needed for ethically complex situations. This includes areas like law enforcement, healthcare (diagnosis and treatment), and judicial decision-making. Domains with unpredictable physical environments – AI agents can struggle in highly dynamic and unpredictable physical environments where real-time adaptation and complex motor skills are essential. This includes tasks like surgery, certain types of construction work, and disaster response. Resource-intensive applications – Developing and deploying sophisticated AI agents can be computationally expensive and require significant resources, potentially making them unsuitable for smaller projects or organizations with limited budgets.

## Deploy AI agents for scale and efficiency with Cloud Run
AI agents, with their inherent need for flexible compute power to handle reasoning, planning, and tool use, can be an excellent fit for Cloud Run . This fully managed serverless platform allows you to deploy your agent's code—often packaged within a container—as a scalable, reliable service or job. This approach abstracts away infrastructure management, letting developers concentrate on refining the agent's logic. Cloud Run offers several features that directly support the architecture and demands of sophisticated AI agents: Scalability and cost-efficiency: Cloud Run automatically scales the number of container instances up to meet peak demand and, crucially, can scale down to zero when the agent is idle. This means you only pay for the exact compute resources consumed during the agent's active execution, making it cost-effective for goal-oriented, intermittent workloads. Agent orchestration and serving: The core agent logic—which manages the model calls, tool selection, and reasoning process—runs as a Cloud Run service. This service provides a stable HTTPS endpoint, making the agent easily accessible via an API for user-facing applications or for communication with other agents Agent-to-Agent, or A2A: Frameworks like the Agent Development Kit (ADK) are designed to integrate seamlessly with Cloud Run for easy deployment. By leveraging Cloud Run's secure, auto-scaling, and flexible environment, organizations can operationalize complex single- or multi-agent systems efficiently.

## Use cases for AI agents
Organizations have been deploying agents to address a variety use cases , which we group into six key broader categories:

## Customer agents
Customer agents deliver personalized customer experiences by understanding customer needs, answering questions, resolving customer issues, or recommending the right products and services. They work seamlessly across multiple channels including the web, mobile, or point of sale, and can be integrated into product experiences with voice or video.

## Employee agents
Employee agents boost productivity by streamlining processes, managing repetitive tasks, answering employee questions, as well as editing and translating critical content and communications.

## Creative agents
Creative agents supercharge the design and creative process by generating content, images, and ideas, assisting with design, writing, personalization, and campaigns.

## Data agents
Data agents are built for complex data analysis. They have the potential to find and act on meaningful insights from data, all while ensuring the factual integrity of their results.

## Code agents
Code agents accelerate software development with AI-enabled code generation and coding assistance, and to ramp up on new languages and code bases. Many organizations are seeing significant gains in productivity, leading to faster deployment and cleaner, clearer code.

## Security agents
Security agents strengthen security posture by mitigating attacks or increasing the speed of investigations. They can oversee security across various surfaces and stages of the security life cycle: prevention, detection, and response.

## Google Cloud and AI agents
Google Cloud provides a portfolio of products and solutions in the AI agent space. These include integrated AI assistants, pre-built AI agents, AI applications, and a platform of agent and developer tools to build custom AI agents.

## Why Google
Choosing Google Cloud Trust and security Modern Infrastructure Cloud Multicloud Global infrastructure Locations Customers and case studies Analyst reports Whitepapers Blog

## Products and pricing
Google Cloud pricing Google Workspace pricing See all products

## Solutions
Infrastructure modernization Databases Application modernization Smart analytics Artificial Intelligence Security Productivity & work transformation Industry solutions DevOps solutions Small business solutions See all solutions

## Resources
Google Cloud Affiliate Program Google Cloud documentation Google Cloud quickstarts Google Cloud Marketplace Learn about cloud computing Support Code samples Cloud Architecture Center Training Certifications Google for Developers Google Cloud for Startups System status Release Notes

## Engage
Contact sales Find a Partner Become a Partner Events Podcasts Developer Center Press Corner Google Cloud on YouTube Google Cloud Tech on YouTube Follow on X Join User Research We're hiring. Join Google Cloud! Community forums
