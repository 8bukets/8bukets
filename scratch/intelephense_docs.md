# Intelephense Documentation

## Getting Started

### About
Intelephense is a high performance, cross platform, cross editor PHP language server adhering to the Language Server Protocol (LSP).

When paired with an LSP capable editor it provides an essential set of code tools, making for a productive and rich PHP coding experience.

The Intelephense server is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to premium features can be obtained by purchasing a licence key.

### Installation

#### Visual Studio Code
Visual Studio Code users should install the Intelephense extension from within the extensions view or download it from the VSCode marketplace.

The built-in VSCode PHP Language Features extension can cause excessive completion suggestions that are out of context and is best disabled. Go to the Extensions UI and search for `PHP Language Features` to disable it. Alternatively, you can disable parts of it via its configuration settings. Other third party extensions that provide similar functionality to Intelephense may also need to be disabled for best results.

Optionally purchase and enter your licence key by opening the command palette (`Ctrl+Shift+P`) and searching for `Enter licence key`.

#### Other Editors
Intelephense requires a Node.js runtime environment. It is recommended that you use a current LTS version of Node.js. To install Intelephense server you can use npm.

```bash
npm i intelephense -g
```

Intelephense needs an LSP compliant client to communicate with and integrate features into the editor. Please follow the setup guide of the relevant tool. The information below may help in configuring the client.

To start the intelephense server:

```bash
intelephense {transport}
```

Where `{transport}` is one of:
* `--node-ipc`
* `--stdio`
* `--socket={number}`
* `--pipe={string}`

If your LSP client exposes `initializationOptions`, then the following values are accepted:

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

When `initializationOptions` properties are not provided by the client, the following defaults are used:

| OS | Property | Path | Fallback |
| :--- | :--- | :--- | :--- |
| *nix | `storagePath` | `$XDG_CONFIG_HOME/intelephense/workspace/` | `$HOME/.config/intelephense/workspace/` |
| *nix | `globalStoragePath` | `$XDG_CONFIG_HOME/intelephense/global/` | `$HOME/.config/intelephense/global/` |
| *nix | `licenceKey` | `{globalStoragePath}/licence.txt` | `{globalStoragePath}/license.txt` |
| Windows | `storagePath` | `%AppData%/intelephense/workspace/` | `%UserProfile%/intelephense/workspace/` |
| Windows | `globalStoragePath` | `%AppData%/intelephense/global/` | `%UserProfile%/intelephense/global/` |
| Windows | `licenceKey` | `{globalStoragePath}/licence.txt` | `{globalStoragePath}/license.txt` |

If your LSP client does not expose `initializationOptions` then a licence key can be provided by placing (only) the key in a text file at the default `licenceKey` path listed above.

### Configuration
Please see the VSCode client `package.json` configuration property for a full list of configuration options and associated JSON schema. Note that the configuration keys are given in dot notation. As an example, the equivalent JSON object for `intelephense.files.exclude` would be `{"intelephense": {"files": {"exclude": []}}}`.

Intelephense attempts to provide reasonable defaults for all settings. Some of the more important settings to consider when getting started include:

* `intelephense.files.associations` - File globs that identify PHP files. Defaults to standard PHP file extensions e.g. `*.php`.
* `intelephense.files.maxSize` - Maximum file size in bytes to index and provide analysis for. Defaults to `1000000` (1MB).
* `intelephense.environment.phpVersion` - PHP version to use for analysis. Defaults to the most recent stable PHP version.
* `intelephense.stubs` - List of stubs to include. Defaults to core symbols and extensions that are bundled with PHP. If you are getting undefined symbols for built-in or PECL extensions, you may need to modify this list.

In VSCode, the settings UI can be used to modify the configuration values. For other LSP clients, please see the client documentation on how to modify these values. Intelephense supports the LSP `workspace/didChangeConfiguration` and `workspace/configuration` methods as a way of supplying configuration values to the server.

If neither of the methods above are supported by the client, then configuration values can be supplied via an `intelephense.config.json` file placed in the workspace folder. The JSON schema for this file is the same as the one used for the VSCode client. The top level `intelephense` property is not required in this file.

For Intelephense to work effectively it must have access to the definitions of the symbols used in your code. Opening a project folder (LSP `InitializeParams` `rootUri` or `workspaceFolders`) rather than individual files enables these symbols to be discovered by Intelephense via indexing the PHP files in the folder. Large workspaces require more system resources. Consider opening a smaller workspace or exclude unnecessary files via the `intelephense.files.exclude` setting to reduce resource usage.

If you need to include files from outside of the workspace folder, then add the paths to these files to the `intelephense.environment.includePaths` setting.

When configuring a multi-root workspace, Intelephense will presume that the folders in the workspace are separate projects and will not provide cross folder symbols unless you link the dependency between the projects via the `intelephense.environment.includePaths` setting.

Depending on the framework or library you use, you may find you need additional configuration to provide method declarations or override existing ones. Please see the Frameworks and Libraries section in the appendix for more information on this.

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

Intelephense will also compute inferred types when a declared or documented type is not found or during control flow analysis. When a type is inferred it may be reduced to its minimal representation. For example, `MyClass|object` would become `object` because `MyClass` is a sub-type of `object`.

Intelephense provides limited support for PHPStorm metadata as a way of overriding or supplementing type information. It is recommended to use PHPDoc type annotations instead of PHPStorm metadata where possible as they are more widely supported across different tools. Support for PHPStorm metadata may be removed in future releases. Please see the PHPDoc Instead of PHPStorm Metadata/Attributes section in the appendix for more information.

### Type Narrowing
Intelephense performs type narrowing of variables during control flow analysis. Type narrowing expressions include built-in type assertions such as `is_string`, custom type assertions annotated with `@assert`, `instanceof`, and equality expressions. The example below demonstrates type narrowing.

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

Intelephense will type evolve array types when mutated only if they are declared with an empty array initialiser. Otherwise they are considered to retain their initial declared, annotated or inferred type. The example below demonstrates type evolving.

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
In the list of supported types below, some can only be used in PHPDoc as documented types. Please see the PHP type system documentation if you are unfamiliar with the standard PHP types. PHPDoc only, or internal types, are flagged with an asterisk.

Additional types used in other static analysis engines that are not listed here are not fully supported. Intelephense attempts to fallback to an appropriate alternative in this situation.

#### Top Type
`mixed`

The super-type of all types. Any other type can be assigned to a type constraint of `mixed`. If Intelephense cannot determine a more specific type for a symbol or expression then this is the type it is given. Because of this, Intelephense also allows `mixed` to be assigned to any other type constraint as well, effectively turning off type checking for that instance. To switch off this behaviour you can set both `intelephense.diagnostics.relaxedTypeCheck` and `intelephense.diagnostics.noMixedTypeCheck` to `false`.

#### Bottom Type
`never`

The sub-type of all types. This type can be assigned to any other type constraint. It is used to represent an impossibility in the code and can be used as the return type of a function that exits or always throws an exception.

#### Scalar Types
Any of these types can be assigned to the other unless the `declare(strict_types=1)` directive is used in the file or `intelephense.diagnostics.strictTypes` is `true`.

* `int`
* `float`
* `bool`
* `string`

#### Unit Types
* `void`
* `null`
* `true`
* `false`
* `unset`* Intelephense uses this PHP keyword to represent the type of an undefined variable.

#### Literal Types
* `'myString'`* String literals are encapsulated in quotes.
* `9`* An integer literal.

#### Object Types
* `object`
* `\MyNs\MyClass` Classes, interfaces, traits, and enums can be fully qualified or not. If not fully qualified then the standard PHP name resolution rules apply to determine the fully qualified name.
* `object{name: string, optional?: string}`* Object shapes can be used to provide further information on dynamic object properties. This improves completion suggestions and type inference when accessing these properties. Optional properties can be declared by adding a `?` at the end of the name.
* `static`
* `self`
* `$this`*

#### Array Types
* `array`
* `array<TKey, TValue>`* Generic form for an array where the type arguments represent the array key and value types respectively. If only a single type argument is provided then it will be normalised to `array<string|int, TValue>`.
* `TValue[]`* Represents a numeric indexed array where the element type is `TValue`.
* `array{description: string, 'length (cm)': float, optional?: string, ...<int, string>}`* Array shapes can be used to provide further information on array element keys and value types. This improves completion suggestions and type inference when accessing these elements. Keys with non alphanumeric characters need to be in quotes. Optional keys can be declared by adding a `?` at the end of the key. Unspecified extra elements can be declared by adding an element of form `...<TKey, TValue>`. Keys are optional and default to numerically indexed. For example a two element tuple would be `array{Type0, Type1}`. A mix of keyed and unkeyed elements is not supported.

#### Callable Types
* `callable` Base callable type that represents a callable string, callable array or a class that implements `__invoke`.
* `callable(TParamA $a, TParamB $b): TReturn`* Callable type signatures can be defined to improve language intelligence. Parameter names are optional. The callable type should be wrapped in parentheses if it forms part of a union. `Closure` can be used instead of `callable` for a more specific type.

#### Alias Types
* `iterable` Alias for `Traversable|array`.
* `?A` Nullable type that is shorthand for `null|A`. Cannot be used as part of a union or intersection type.

#### Union Types
`A|B|C`

A type which may have multiple atomic type representations. For example, a type constraint of `A|B` can be assigned type `A` or `B`.

#### Intersection Types
`A&B&C`

A composite type which consists of multiple atomic types. For example, a type of `A&B` can be assigned to type `A` and to type `B`.

#### DNF Types
`A|B|(C&D&E)`

When combining union and intersection types, only a single level of nesting is permitted. The union must be the top level.

#### Generic Types
`MyType<TypeArg1, TypeArg2>`*

A generic type can be declared using one or many `@template` PHPDoc annotations above the target class, interface, or trait. Type arguments can then be supplied in the same order as the `@template` declarations. The following built-in types are templated:

* `iterable<TKey, TValue>`
* `Traversable<TKey, TValue>`
* `array<TKey, TValue>`
* `Iterator<TKey, TValue>`
* `IteratorAggregate<TKey, TValue>`
* `ArrayAccess<TKey, TValue>`
* `WeakReference<TObject>`
* `WeakMap<TKey, TValue>`
* `Fiber<TStart, TResume, TReturn, TSuspend>`
* `DatePeriod<TDate, TEnd>`
* `ReflectionAttribute<TObject>`
* `ReflectionClass<TObject>`
* `Generator<TKey, TYield, TSend, TReturn>`
* `ArrayObject<TKey, TValue>`
* `SplDoublyLinkedList<TValue>`
* `SplQueue<TValue>`
* `SplStack<TValue>`
* `SplHeap<TValue>`
* `SplMinHeap<TValue>`
* `SplMaxHeap<TValue>`
* `SplPriorityQueue<TPriority, TValue>`
* `SplFixedArray<TValue>`
* `SplObjectStorage<TObject, TValue>`

#### Conditional Return Type
`(TSubject is TCompare ? TTrue : TFalse)`*

Sometimes the return type of a function may depend on the type of a parameter. A conditional type can be used without templates too by using the parameter name. For example, `($myParam is string ? string : null)`. Conditional types must be wrapped in parentheses. Conditional types may also be nested.

#### Array Key Type
`key-of<TArray>`*

This type will resolve to a union of the keys of an array shape.

#### Array Value Type
`value-of<TArray>`*

This type will resolve to a union of the values of an array shape.

#### Index Access Type
`TArray[TKey]`*

This type will resolve to the type of the value at index `TKey` in `TArray`. It is particularly useful in conjunction with `key-of<TArray>` and shape types for mapping the return type when accessing container items with arbitrary strings. For example:

```php
<?php

class MyContainerItem {}

class MyContainer
{
    /**
     * @template TMap of array{item: MyContainerItem, other: object}
     * @template TKey of key-of<TMap>
     * @param TKey $name
     * @return TMap[TKey]
     */
    function get($name): mixed {}
}

$container = new MyContainer();
$item = $container->get('item'); //$item is MyContainerItem
```

#### Miscellaneous Types
* `resource`*
* `class-string<T>`* A string where the value is the name of class `T`.

## PHPDoc Annotations
Intelephense supports standard PHPDoc annotations as well as non-standard annotations which have been popularised by other static analysis tools such as Psalm and PHPStan. The below list describes the non-standard annotations that Intelephense supports.

To make Intelephense prefer tool-prefixed annotations over un-prefixed ones, you can set the `intelephense.compatibility.preferPsalmPhpstanPrefixedAnnotations` setting to `true`.

### @template
`/** @template TemplateName of OptionalTypeConstraint = OptionalDefaultType */`
Used to declare a type argument of a generic type, function or method.

### @template-extends
`/** @template-extends ParentType<TypeArg1, TypeArg2> */`
Used to declare the type arguments supplied to a generic parent type. The alias `@extends` is also supported.

### @template-implements
`/** @template-implements InterfaceType<TypeArg1, TypeArg2> */`
Used to declare the type arguments supplied to a generic interface. The alias `@implements` is also supported.

### @template-use
`/** @template-use TraitType<TypeArg1, TypeArg2> */`
Used to declare the type arguments supplied to a generic trait. The alias `@use` is also supported.

### @param-closure-this
`/** @param-closure-this Type $parameter */`
Declares the type of the `$this` variable inside a closure passed as a parameter.

### @param-out
`/** @param-out Type &$parameter */`
Declares the out type of a by-reference parameter.

### @assert
`/** @assert Type $parameter */`
Declares that a function asserts an argument is of a specified type.

### @assert-if-true @assert-if-false
`/** @assert-if-true Type $parameter */`
Asserts type narrowing on the true or false code paths.

### @mixin
`/** @mixin ClassName */`
Declares that members of a class are mixed in via magic methods. (Premium feature).

### @disregard
`/** @disregard PXXXX */`
Suppresses a specific diagnostic at the following statement.

### @type-alias
`/** @type-alias TypeName = Type */`
Declares a type alias.

### @import-type
`/** @import-type TypeName as OptionalAlias */`
Imports a type alias from another file.

## Features

### Free Features

#### Workspace Symbols
* **Availability**: FREE
* **LSP**: `workspace/symbol`
* **Keybinding**: `Ctrl+T`
Search for symbols in your workspace and navigate to their definitions. Supports Fully Qualified Structural Element Name (FQSEN) queries.

#### Document Symbols
* **Availability**: FREE
* **LSP**: `textDocument/documentSymbol`
* **Keybinding**: `Ctrl+Shift+O`
Lists all symbols in the current document for outline views and breadcrumb navigation.

#### Go to Definition
* **Availability**: FREE
* **LSP**: `textDocument/definition`
* **Keybinding**: `F12`
Navigate to the definition of a symbol.

#### Hover
* **Availability**: FREE
* **LSP**: `textDocument/hover`
* **Keybinding**: `Ctrl+K Ctrl+I`
Shows type information, signature, and documentation on mouse-over.

#### Highlight
* **Availability**: FREE
* **LSP**: `textDocument/documentHighlight`
Highlights all references to the symbol at the cursor position in the current file.

#### Code Completion
* **Availability**: FREE
* **LSP**: `textDocument/completion`
* **Keybinding**: `Ctrl+Space`
Context-aware suggestions for symbols as you type.

#### Signature Help
* **Availability**: FREE
* **LSP**: `textDocument/signatureHelp`
* **Keybinding**: `Ctrl+Shift+Space`
Displays parameter information during function or method calls.

#### Find All References
* **Availability**: FREE
* **LSP**: `textDocument/references`
* **Keybinding**: `Shift+F12`
Lists every usage of a symbol across the workspace.

#### Formatting
* **Availability**: FREE
* **LSP**: `textDocument/formatting`
Opinionated formatter complying with PHP-FIG coding standards.

#### Diagnostics
* **Availability**: FREE
* **LSP**: `textDocument/publishDiagnostics`
Surfaces syntax errors, type errors, and other issues as you type or on save.

#### Inline Values
* **Availability**: FREE
* **LSP**: `textDocument/inlineValues`
Displays variable states inline during a debug session (requires Xdebug).

#### Embedded Languages
Provides language intelligence for HTML, CSS, and JavaScript within PHP files.

### Premium Features

#### Rename
* **Availability**: PREMIUM
* **LSP**: `textDocument/rename`
* **Keybinding**: `F2`
Refactors a symbol and all its references across the workspace.

#### Code Folding
* **Availability**: PREMIUM
* **LSP**: `textDocument/foldingRange`
* **Keybinding**: `Ctrl+Shift+[`
Collapses and expands regions based on the syntax tree.

#### Find All Implementations
* **Availability**: PREMIUM
* **LSP**: `textDocument/implementation`
* **Keybinding**: `Ctrl+F12`
Lists concrete classes implementing an interface or abstract method.

#### Go to Type Definition
* **Availability**: PREMIUM
* **LSP**: `textDocument/typeDefinition`
Navigates to the type of a variable.

#### Go to Declaration
* **Availability**: PREMIUM
* **LSP**: `textDocument/declaration`
Navigates to the initial declaration in a type hierarchy.

#### Smart Select
* **Availability**: PREMIUM
* **LSP**: `textDocument/selectionRange`
* **Keybinding**: `Shift+Alt+→`
Expands or shrinks the selection based on the syntax tree.

#### Type Hierarchy
* **Availability**: PREMIUM
* **LSP**: `textDocument/typeHierarchy`
Shows the inheritance structure of a type.

#### Code Lens
* **Availability**: PREMIUM
* **LSP**: `textDocument/codeLens`
Displays reference counts and navigation links above declarations.

#### Inlay Hints
* **Availability**: PREMIUM
* **LSP**: `textDocument/inlayHint`
Shows inferred parameter names and return types inline.

#### Document Links
* **Availability**: PREMIUM
* **LSP**: `textDocument/documentLink`
* **Keybinding**: `Ctrl+Click`
Makes `require`/`include` paths and `@see` annotations clickable.

#### Code Actions
* **Availability**: PREMIUM
* **LSP**: `textDocument/codeAction`
* **Keybinding**: `Ctrl+.`
Provides quick-fix and refactoring options (e.g., Import Symbol, Add PHPDoc).

## Appendix

### Compatibility With Frameworks and Libraries
Intelephense aims to support all PHP frameworks and libraries. If symbols are missing due to runtime bootstrapping or magic methods, use these workarounds:

#### Solutions that form part of the executable code
```php
<?php
// Use instanceof to narrow type
$view = view();
if ($view instanceof CustomView) {
  $view->customViewMethod();
}

// Or use @var annotation
/** @var CustomView $view */
$view = view();
$view->customViewMethod();
```

#### Solutions that do not form part of the project executable code
Create a helper file (e.g., `intelephense_helper.php`) in your workspace with alternate symbol declarations:
```php
<?php
function view(): CustomView {}
interface View { function customViewMethod(); }
```

### PHPDoc Instead of PHPStorm Metadata/Attributes
It is recommended to use PHPDoc types for better compatibility.

#### Return type based on input
```php
/**
 * @template T of string|object
 * @param T $input
 * @return T
 */
function paintColourDoc(string|object $input): string|object {}
```

#### Map-based return types
```php
/**
 * @template T of array{red: RedService, blue: BlueObject, green: GreenCollection}
 * @template K of key-of<T>
 * @param K $value
 * @return T[K]
 */
function getColourDoc(string $value): mixed {}
```

#### Array shapes
```php
/**
 * @return array{red: RedService, blue: BlueObject, green: GreenCollection}
 */
function getColoursDoc(): array {}
```

#### Expected values
```php
/**
 * @param 'red'|'blue'|'green' $colour
 */
function setColourDoc(string $colour): void {}
```
