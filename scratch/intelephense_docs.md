# Intelephense Documentation

## Getting Started

### About
Intelephense is a high performance, cross platform, cross editor PHP language server adhering to the Language Server Protocol (LSP).

When paired with an LSP capable editor it provides an essential set of code tools, making for a productive and rich PHP coding experience.

The Intelephense server is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to premium features can be obtained by purchasing a licence key.

### Installation
#### Visual Studio Code
Visual Studio Code users should install the Intelephense extension from within the extensions view or download it from the VSCode marketplace.

The built-in VSCode PHP Language Features extension can cause excessive completion suggestions that are out of context and is best disabled. Go to the Extensions UI and search for PHP Language Features to disable it. Alternatively, you can disable parts of it via its configuration settings. Other third party extensions that provide similar functionality to Intelephense may also need to be disabled for best results.

Optionally purchase and enter your licence key by opening the command palette (Ctrl+Shift+P) and searching for Enter licence key.

#### Other Editors
Intelephense requires a Node.js runtime environment. It is recommended that you use a current LTS version of Node.js. To install Intelephense server you can use npm.

```bash
npm i intelephense -g
```

Intelephense needs an LSP compliant client to communicate with and integrate features into the editor. A list of editors and clients that support the LSP can be found online. Please follow the setup guide of the relevant tool. The information below may help in configuring the client.

To start the intelephense server:
```bash
intelephense {transport}
```
Where {transport} is one of:
* --node-ipc
* --stdio
* --socket={number}
* --pipe={string}

If your LSP client exposes initializationOptions, then the following values are accepted:
```typescript
interface InitialisationOptions {
    // Optional absolute path to storage directory for workspace specific data.
    storagePath?: string;

    // Optional absolute path to a global storage directory for global data.
    globalStoragePath?: string;

    //Optional licence key or absolute path to a text file containing the licence key.
    licenceKey?: string;

    //Optional flag to clear server state.
    //State can also be cleared by deleting {storagePath}/intelephense
    clearCache?: boolean;
}
```

When initializationOptions properties are not provided by the client, the following defaults are used:

| OS | Property | Path | Fallback |
|---|---|---|---|
| *nix | storagePath | $XDG_CONFIG_HOME/intelephense/workspace/ | $HOME/.config/intelephense/workspace/ |
| *nix | globalStoragePath | $XDG_CONFIG_HOME/intelephense/global/ | $HOME/.config/intelephense/global/ |
| *nix | licenceKey | {globalStoragePath}/licence.txt | {globalStoragePath}/license.txt |
| Windows | storagePath | %AppData%/intelephense/workspace/ | %UserProfile%/intelephense/workspace/ |
| Windows | globalStoragePath | %AppData%/intelephense/global/ | %UserProfile%/intelephense/global/ |
| Windows | licenceKey | {globalStoragePath}/licence.txt | {globalStoragePath}/license.txt |

### Configuration
Please see the VSCode client package.json configuration property for a full list of configuration options and associated JSON schema. Note that the configuration keys are given in dot notation. As an example, the equivalent JSON object for intelephense.files.exclude would be {"intelephense": {"files": {"exclude": []}}}.

Intelephense attempts to provide reasonable defaults for all settings. Some of the more important settings to consider when getting started include:
* intelephense.files.associations - File globs that identify PHP files. Defaults to standard PHP file extensions e.g. *.php.
* intelephense.files.maxSize - Maximum file size in bytes to index and provide analysis for. Defaults to 1000000 (1MB).
* intelephense.environment.phpVersion - PHP version to use for analysis. Defaults to the most recent stable PHP version.
* intelephense.stubs - List of stubs to include. Defaults to core symbols and extensions that are bundled with PHP. If you are getting undefined symbols for built-in or PECL extensions, you may need to modify this list.

In VSCode, the settings UI can be used to modify the configuration values. For other LSP clients, please see the client documentation on how to modify these values. Intelephense supports the LSP workspace/didChangeConfiguration and workspace/configuration methods as a way of supplying configuration values to the server.

If neither of the methods above are supported by the client, then configuration values can be supplied via an intelephense.config.json file placed in the workspace folder. The JSON schema for this file is the same as the one used for the VSCode client. The top level intelephense property is not required in this file.

For Intelephense to work effectively it must have access to the definitions of the symbols used in your code. Opening a project folder (LSP InitializeParams rootUri or workspaceFolders) rather than individual files enables these symbols to be discovered by Intelephense via indexing the PHP files in the folder. Large workspaces require more system resources. Consider opening a smaller workspace or exclude unnecessary files via the intelephense.files.exclude setting to reduce resource usage.

If you need to include files from outside of the workspace folder, then add the paths to these files to the intelephense.environment.includePaths setting.

When configuring a multi-root workspace, Intelephense will presume that the folders in the workspace are separate projects and will not provide cross folder symbols unless you link the dependency between the projects via the intelephense.environment.includePaths setting.

## Type System

Providing type information in your PHP code will result in a better experience when using Intelephense. Type information can be provided via coded type declarations or PHPDoc type annotations. Where both have been provided, PHPDoc type annotations are given precedence as they can provide more detailed type information.

```php
<?php

/**
 * @param string $s  <- A phpdoc parameter type annotation for $s
 * @return string[] <- A phpdoc return type annotation specifying the array element type
 **/
function foo(string $s): array {} // <- type declarations for $s (string) and function return (array)
```

Intelephense will also compute inferred types when a declared or documented type is not found or during control flow analysis. When a type is inferred it may be reduced to its minimal representation. For example, MyClass|object would become object because MyClass is a sub-type of object.

Intelephense provides limited support for PHPStorm metadata as a way of overriding or supplementing type information. It is recommended to use PHPDoc type annotations instead of PHPStorm metadata where possible as they are more widely supported across different tools. Support for PHPStorm metadata may be removed in future releases.

### Type Narrowing
Intelephense performs type narrowing of variables during control flow analysis. Type narrowing expressions include built-in type assertions such as is_string, custom type assertions annotated with @assert, instanceof, and equality expressions.

```php
<?php

class Foo {}

function example(string|array|Foo|null $input): void
{
    if (!$input) {
        // $input is narrowed to string|array|null in this block
        // empty strings, empty arrays and null are all falsey
    } else {
        // $input is narrowed to string|array|Foo in this block

        if ($input instanceof Foo) {
            // $input is narrowed to Foo in this block
        } else if (is_string($input)) {
            // $input is narrowed to string in this block
        } else {
            // $input is narrowed to array in this block
        }
    }
}
```

### Type Evolving
Type evolving is the change in a variable's type after an assignment expression. Simple variables and parameters always change to the type of the assigned expression regardless of initial assignments, type declarations or annotations.

Properties with no type declaration or annotation will also change to the type of the assigned expression. Otherwise they will only widen or narrow according to the bounds of the initial type they have been declared or annotated with.

Intelephense will type evolve array types when mutated only if they are declared with an empty array initialiser. Otherwise they are considered to retain their initial declared, annotated or inferred type.

```php
<?php

function example(int $a): void
{
    $a = "string"; // $a is now type string

    $b = []; // $b is type array and flagged as evolving

    $b[] = "string"; // $b is now type string[]

    $b[] = 9; //$b is now (string|int)[]

    $c = [1, 2]; // $c is type int[] and NOT flagged as evolving

    $c[] = "string"; // $c is still type int[]
}
```

### Supported Types

#### Top Type
mixed
The super-type of all types. Any other type can be assigned to a type constraint of mixed. If intelephense cannot determine a more specific type for a symbol or expression then this is the type it is given. Because of this, Intelephense also allows mixed to be assigned to any other type constraint as well, effectively turning off type checking for that instance.

#### Bottom Type
never
The sub-type of all types. This type can be assigned to any other type constraint. It is used to represent an impossibility in the code and can be used as the return type of a function that exits or always throws an exception.

#### Scalar Types
int, float, bool, string.

#### Unit Types
void, null, true, false, unset* (represents an undefined variable).

#### Literal Types
'myString'*, 9* (integer literal).

#### Object Types
object, \MyNs\MyClass, object{name: string, optional?: string}*, static, self, $this*.

#### Array Types
array, array<TKey, TValue>*, TValue[]*, array{description: string, 'length (cm)': float, optional?: string, ...<int, string>}*.

#### Callable Types
callable, callable(TParamA $a, TParamB $b): TReturn*, Closure*.

#### Alias Types
iterable (Alias for Traversable|array), ?A (Nullable type shorthand for null|A).

#### Union Types
A|B|C - A type which may have multiple atomic type representations.

#### Intersection Types
A&B&C - A composite type which consists of multiple atomic types.

#### DNF Types
A|B|(C&D&E) - When combining union and intersection types, only a single level of nesting is permitted. The union must be the top level.

#### Generic Types
Supports @template PHPDoc annotations. The following built-in types are templated:
iterable, Traversable, array, Iterator, IteratorAggregate, ArrayAccess, WeakReference, WeakMap, Fiber, DatePeriod, ReflectionAttribute, ReflectionClass, Generator, ArrayObject, SplDoublyLinkedList, SplQueue, SplStack, SplHeap, SplMinHeap, SplMaxHeap, SplPriorityQueue, SplFixedArray, SplObjectStorage.

#### Conditional Return Type
(TSubject is TCompare ? TTrue : TFalse)* - Sometimes the return type of a function may depend on the type of a parameter.

#### Array Key Type
key-of<TArray>* - Resolves to a union of the keys of an array shape.

#### Array Value Type
value-of<TArray>* - Resolves to a union of the values of an array shape.

#### Index Access Type
TArray[TKey]* - Resolves to the type of the value at index TKey in TArray.

#### Miscellaneous Types
resource*, class-string<T>*.

## PHPDoc Annotations
Intelephense supports standard PHPDoc annotations as well as non-standard ones from tools like Psalm and PHPStan.

* **@template**: Used to declare a type argument of a generic type, function or method.
* **@template-extends**: Used to declare the type arguments supplied to a generic parent type. Alias @extends is also supported.
* **@template-implements**: Used to declare the type arguments supplied to a generic interface. Alias @implements is also supported.
* **@template-use**: Used to declare the type arguments supplied to a generic trait. Alias @use is also supported.
* **@param-closure-this**: Declares the type of the $this variable inside a closure passed as a parameter.
* **@param-out**: Declares the out type of a by-reference parameter.
* **@assert**: Declares a function that asserts an argument is of a specified type.
* **@assert-if-true / @assert-if-false**: Similar to @assert but for boolean return paths.
* **@mixin**: (Premium) Declares that members of a specified class are mixed in.
* **@disregard**: Suppresses a specific diagnostic at the following statement.
* **@type-alias**: Declares a type alias for improving readability.
* **@import-type**: Imports a type alias declared in another file.

## Features

### Free Features
The following features are available to all users.

#### Workspace Symbols
Search for symbols in your workspace (Ctrl+T). Use FQSEN query syntax for specific symbols.

#### Document Symbols
Lists all symbols in the current document (Ctrl+Shift+O).

#### Go to Definition
Navigate to the definition of a symbol (F12).

#### Hover
Show type information and documentation for a symbol when hovering.

#### Highlight
Highlight all references to the symbol at the cursor position in the current file.

#### Code Completion
Context appropriate completion suggestions ($ > : \ / ' " * . <).

#### Signature Help
Information about function/method signatures during a call (Ctrl+Shift+Space).

#### Find All References
List all references to a symbol in the current file or workspace (Shift+F12).

#### Formatting
Format a whole document or selected range. Complies with PHP-FIG coding standards.

#### Diagnostics
Syntax errors, type errors, and language constraints.

#### Inline Values
Variable ranges and text for debuggers to display inline values.

#### Embedded Languages
Language intelligence for HTML, CSS, and JavaScript within PHP files.

### Premium Features
Requires a licence.

#### Rename
Refactor a symbol and all its semantic references (F2).

#### Code Folding
Fold and unfold regions of code based on the syntax tree.

#### Find All Implementations
List all implementations of a method or interface (Ctrl+F12).

#### Go to Type Definition
Navigate to the type definition of a variable rather than its declaration.

#### Go to Declaration
Navigate to the initial declaration of a symbol in a type hierarchy.

#### Smart Select
Expand and shrink selections based on the syntax tree (Shift+Alt+→/←).

#### Type Hierarchy
Understand the inheritance structure of a class, interface, trait, or enum.

#### Code Lens
Reference counts and navigation links above declarations (Implementations, Overrides, Parent, Usages).

#### Inlay Hints
Inferred parameter names and return types inline with the code.

#### Document Links
Clickable links for require/include statements and @see annotations.

#### Code Actions
Quick-fix and refactoring options (Ctrl+.), such as Import Symbol, Add PHPDoc, and Implement All Abstract Methods.

## Appendix

### Frameworks and Libraries
Intelephense aims to support all PHP frameworks but does not implement specific solutions. Workarounds include type narrowing in code using `instanceof`, PHPDoc `@var` annotations, or using helper files for symbol overrides.

### PHPDoc Instead of PHPStorm Metadata/Attributes
It is recommended to use PHPDoc types for greater compatibility. Examples include using `@template` for return type mapping and array shapes (e.g., `array{red: RedService}`) for structured array documentation.

---
All the best - https://markposition.wordpress.com
