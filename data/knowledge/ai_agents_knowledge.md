# ANTIGRAVITY AI AGENTS KNOWLEDGE BASE

*Last Updated: 2026-05-16T00:35:18.354Z*

## DOCUMENT: intelephense_docs.md
**Source:** local://intelephense_docs.md
**Ingested At:** 2026-05-16T00:35:18.134Z

### About
Intelephense is a high performance, cross platform, cross editor PHP language server adhering to the Language Server Protocol (LSP).

When paired with an LSP capable editor it provides an essential set of code tools, making for a productive and rich PHP coding experience.

The Intelephense server is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to premium features can be obtained by purchasing a licence key.

### Visual Studio Code
Visual Studio Code users should install the Intelephense extension from within the extensions view or download it from the VSCode marketplace.

The built-in VSCode PHP Language Features extension can cause excessive completion suggestions that are out of context and is best disabled. Go to the Extensions UI and search for PHP Language Features to disable it. Alternatively, you can disable parts of it via it's configuration settings. Other third party extensions that provide similar functionality to Intelephense may also need to be disabled for best results.

Optionally purchase and enter your licence key by opening the command palette (Ctrl+Shift+P) and searching for Enter licence key.

A screen capture showing how to enter your intelephense licence key into VSCode.
Entering a licence key via the VS Code command palette

### Other Editors
Intelephense requires a Node.js runtime environment. It is recommended that you use a current LTS version of Node.js. To install Intelephense server you can use npm.

npm i intelephense -g
Intelephense needs an LSP compliant client to communicate with and integrate features into the editor. A list of editors and clients that support the LSP can be found here. Please follow the setup guide of the relevant tool. The information below may help in configuring the client.

To start the intelephense server:

intelephense {transport}
Where {transport} is one of:

--node-ipc
--stdio
--socket={number}
--pipe={string}
If your LSP client exposes initializationOptions, then the following values are accepted:

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
When initializationOptions properties are not provided by the client, the following defaults are used:

OS	Property	Path	Fallback
*nix	storagePath	$XDG_CONFIG_HOME/intelephense/workspace/	$HOME/.config/intelephense/workspace/
*nix	globalStoragePath	$XDG_CONFIG_HOME/intelephense/global/	$HOME/.config/intelephense/global/
*nix	licenceKey	{globalStoragePath}/licence.txt	{globalStoragePath}/license.txt
Windows	storagePath	%AppData%/intelephense/workspace/	%UserProfile%/intelephense/workspace/
Windows	globalStoragePath	%AppData%/intelephense/global/	%UserProfile%/intelephense/global/
Windows	licenceKey	{globalStoragePath}/licence.txt	{globalStoragePath}/license.txt
If your LSP client does not expose initializationOptions then a licence key can be provided by placing (only) the key in a text file at the default licenceKey path listed above.

### Configuration
Please see the VSCode client package.json configuration property for a full list of configuration options and associated JSON schema. Note that the configuration keys are given in dot notation. As an example, the equivalent JSON object for intelephense.files.exclude would be {"intelephense": {"files": {"exclude": []}}}.

Intelephense attempts to provide reasonable defaults for all settings. Some of the more important settings to consider when getting started include:

intelephense.files.associations - File globs that identify PHP files. Defaults to standard PHP file extensions e.g. *.php.
intelephense.files.maxSize - Maximum file size in bytes to index and provide analysis for. Defaults to 1000000 (1MB).
intelephense.environment.phpVersion - PHP version to use for analysis. Defaults to the most recent stable PHP version.
intelephense.stubs - List of stubs to include. Defaults to core symbols and extensions that are bundled with PHP. If you are getting undefined symbols for built-in or PECL extensions, you may need to modify this list.
In VSCode, the settings UI can be used to modify the configuration values. For other LSP clients, please see the client documentation on how to modify these values. Intelephense supports the LSP workspace/didChangeConfiguration and workspace/configuration methods as a way of supplying configuration values to the server.

If neither of the methods above are supported by the client, then configuration values can be supplied via an intelephense.config.json file placed in the workspace folder. The JSON schema for this file is the same as the one used for the VSCode client. The top level intelephense property is not required in this file.

For Intelephense to work effectively it must have access to the definitions of the symbols used in your code. Opening a project folder (LSP InitializeParams rootUri or workspaceFolders) rather than individual files enables these symbols to be discovered by Intelephense via indexing the PHP files in the folder. Large workspaces require more system resources. Consider opening a smaller workspace or exclude unnecessary files via the intelephense.files.exclude setting to reduce resource usage.

If you need to include files from outside of the workspace folder, then add the paths to these files to the intelephense.environment.includePaths setting.

When configuring a multi-root workspace, Intelephense will presume that the folders in the workspace are separate projects and will not provide cross folder symbols unless you link the dependency between the projects via the intelephense.environment.includePaths setting.

Depending on the framework or library you use, you may find you need additional configuration to provide method declarations or override existing ones. Please see the Frameworks and Libraries section in the appendix for more information on this.

### Type System
Providing type information in your PHP code will result in a better experience when using Intelephense. Type information can be provided via coded type declarations or PHPDoc type annotations. Where both have been provided, PHPDoc type annotations are given precedence as they can provide more detailed type information.

<?php

/**
 * @param string $s  <- A phpdoc parameter type annotation for $s
 * @return string[] <- A phpdoc return type annotation specifying the array element type
 **/
function foo(string $s): array {} // <- type declarations for $s (string) and function return (array)
Intelephense will also compute inferred types when a declared or documented type is not found or during control flow analysis. When a type is inferred it may be reduced to it's minimal representation. For example, MyClass|object would become object because MyClass is a sub-type of object.

Intelephense provides limited support for PHPStorm metadata as a way of overriding or supplementing type information. It is recommended to use PHPDoc type annotations instead of PHPStorm metadata where possible as they are more widely supported across different tools. Support for PHPStorm metadata may be removed in future releases. Please see the PHPDoc Instead of PHPStorm Metadata/Attributes section in the appendix for more information.

### Type Narrowing
Intelephense performs type narrowing of variables during control flow analysis. Type narrowing expressions include built-in type assertions such as is_string, custom type assertions annotated with @assert, instanceof, and equality expressions. The example below demonstrates type narrowing.

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

### Type Evolving
Type evolving is the change in a variable's type after an assignment expression. Simple variables and parameters always change to the type of the assigned expression regardless of initial assignments, type declarations or annotations.

Properties with no type declaration or annotation will also change to the type of the assigned expression. Otherwise they will only widen or narrow according to the bounds of the initial type they have been declared or annotated with.

Intelephense will type evolve array types when mutated only if they are declared with an empty array initialiser. Otherwise they are considered to retain their initial declared, annotated or inferred type. The example below demonstrates type evolving.

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

### Supported Types
In the list of supported types below, some can only be used in PHPDoc as documented types. Please see the PHP type system documentation if you are unfamiliar with the standard PHP types. PHPDoc only, or internal types, are flagged with an asterisk.

Additional types used in other static analysis engines that are not listed here are not fully supported. Intelephense attempts to fallback to an appropriate alternative in this situation.

### Top Type
mixed

The super-type of all types. Any other type can be assigned to a type constraint of mixed. If intelephense cannot determine a more specific type for a symbol or expression then this is the type it is given. Because of this, Intelephense also allows mixed to be assigned to any other type constraint as well, effectively turning off type checking for that instance. To switch off this behaviour you can set both intelephense.diagnostics.relaxedTypeCheck and intelephense.diagnostics.noMixedTypeCheck to false.

### Bottom Type
never

The sub-type of all types. This type can be assigned to any other type constraint. It is used to represent an impossibility in the code and can be used as the return type of a function that exits or always throws an exception.

### Scalar Types
Any of these types can be assigned to the other unless the declare(strict_types=1) directive is used in the file or intelephense.diagnostics.strictTypes is true.

int
float
bool
string

### Unit Types
void
null
true
false
unset* Intelephense uses this PHP keyword to represent the type of an undefined variable.

### Literal Types
'myString'* String literals are encapsulated in quotes.
9* An integer literal.

### Object Types
object
\MyNs\MyClass Classes, interfaces, traits, and enums can be fully qualified or not. If not fully qualified then the standard PHP name resolution rules apply to determine the fully qualified name.
object{name: string, optional?: string}* Object shapes can be used to provide further information on dynamic object properties. This improves completion suggestions and type inference when accessing these properties. Optional properties can be declared by adding a ? at the end of the name.
static
self
$this*

### Array Types
array
array<TKey, TValue>* Generic form for an array where the type arguments represent the array key and value types respectively. If only a single type argument is provided then it will be normalised to array<string|int, TValue>.
TValue[]* Represents a numeric indexed array where the element type is TValue.
array{description: string, 'length (cm)': float, optional?: string, ...<int, string>}* Array shapes can be used to provide further information on array element keys and value types. This improves completion suggestions and type inference when accessing these elements. Keys with non alphanumeric characters need to be in quotes. Optional keys can be declared by adding a ? at the end of the key. Unspecified extra elements can be declared by adding an element of form ...<TKey, TValue>. Keys are optional and default to numerically indexed. For example a two element tuple would be array{Type0, Type1}. A mix of keyed and unkeyed elements is not supported.

### Callable Types
callable Base callable type that represents a callable string, callable array or a class that implements __invoke.
callable(TParamA $a, TParamB $b): TReturn* Callable type signatures can be defined to improve language intelligence. Parameter names are optional. The callable type should be wrapped in parentheses if it forms part of a union. Closure can be used instead of callable for a more specific type.

### Alias Types
iterable Alias for Traversable|array.
?A Nullable type that is shorthand for null|A. Cannot be used as part of a union or intersection type.

### Union Types
A|B|C

A type which may have multiple atomic type representations. For example, a type constraint of A|B can be assigned type A or B.

### Intersection Types
A&B&C

A composite type which consists of multiple atomic types. For example, a type of A&B can be assigned to type A and to type B.

DNF Types
A|B|(C&D&E)

When combining union and intersection types, only a single level of nesting is permitted. The union must be the top level.

### Generic Types
MyType<TypeArg1, TypeArg2>*

A generic type can be declared using one or many @template PHPDoc annotations above the target class, interface, or trait. Type arguments can then be supplied in the same order as the @template declarations. The following built-in types are templated:

iterable<TKey, TValue>
Traversable<TKey, TValue>
array<TKey, TValue>
Iterator<TKey, TValue>
IteratorAggregate<TKey, TValue>
ArrayAccess<TKey, TValue>
WeakReference<TObject>
WeakMap<TKey, TValue>
Fiber<TStart, TResume, TReturn, TSuspend>
DatePeriod<TDate, TEnd>
ReflectionAttribute<TObject>
ReflectionClass<TObject>
Generator<TKey, TYield, TSend, TReturn>
ArrayObject<TKey, TValue>
SplDoublyLinkedList<TValue>
SplQueue<TValue>
SplStack<TValue>
SplHeap<TValue>
SplMinHeap<TValue>
SplMaxHeap<TValue>
SplPriorityQueue<TPriority, TValue>
SplFixedArray<TValue>
SplObjectStorage<TObject, TValue>

### Conditional Return Type
(TSubject is TCompare ? TTrue : TFalse)*

Sometimes the return type of a function may depend on the type of a parameter. A conditional type can be used without templates too by using the parameter name. For example, ($myParam is string ? string : null). Conditional types must be wrapped in parentheses. Conditional types may also be nested.

### Array Key Type
key-of<TArray>*

This type will resolve to a union of the keys of an array shape.

### Array Value Type
value-of<TArray>*

This type will resolve to a union of the values of an array shape.

### Index Access Type
TArray[TKey]*

This type will resolve to the type of the value at index TKey in TArray. It is particularly useful in conjunction with key-of<TArray> and shape types for mapping the return type when accessing container items with arbitrary strings. For example:

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

### Miscellaneous Types
resource*
class-string<T>* A string where the value is the name of class T.
PHPDoc Annotations
Intelephense supports standard PHPDoc annotations as well as non-standard annotations which have been popularised by other static analysis tools such as Psalm and PHPStan. The below list describes the non-standard annotations that Intelephense supports. For further information on standard PHPDoc annotations, please see the PHP_FIG and phpDocumentor references.

Some libraries or projects that have adopted static analysis tools such as Psalm or PHPStan may prefix some annotations with the tool name to avoid conflicts with other tools.

To make Intelephense prefer these prefixed annotations over the un-prefixed ones, you can set the intelephense.compatibility.preferPsalmPhpstanPrefixedAnnotations setting to true. Intelephense does not aim to support all types and features of these tools but will attempt to fallback to appropriate alternatives where possible.

@template
/** @template TemplateName of OptionalTypeConstraint = OptionalDefaultType */
This annotation is used to declare a type argument of a generic type, function or method. The order that the template types appear is the same order in which the type arguments must be supplied in a generic type expression. The template type can be optionally constrained to a specific type and given an optional default type to be used when no type argument is supplied.

@template-extends
/** @template-extends ParentType<TypeArg1, TypeArg2> */
This annotation is used to declare the type arguments supplied to a generic parent type. It can be used on classes and interfaces when extending a parent class or interface. The alias @extends is also supported.

@template-implements
/** @template-implements InterfaceType<TypeArg1, TypeArg2> */
This annotation is used to declare the type arguments supplied to a generic interface. It can be used on classes and enums when implementing an interface. The alias @implements is also supported.

@template-use
/** @template-use TraitType<TypeArg1, TypeArg2> */
This annotation is used to declare the type arguments supplied to a generic trait. It can be used on classes, traits and enums when using a trait. The alias @use is also supported.

@param-closure-this
/** @param-closure-this Type $parameter */
This annotation is used to declare the type of the $this variable inside a closure that is passed as a parameter to a function or method. An example of a standard PHP method that benefits internally from this annotation is Closure::bind().

@param-out
/** @param-out Type &$parameter */
This annotation is used to declare the out type of a by-reference parameter. Intelephense will not modify the type of a by-reference parameter unless this annotation is used.

@assert
/** @assert Type $parameter */
This annotation is used to declare a function or method that asserts that an argument is of the specified type. Intelephense will narrow the type of the passed variable to the asserted type after the function or method call. It is presumed that the function or method has no false path and that it will throw an exception or exit if the assertion fails.

@assert-if-true @assert-if-false
/** @assert-if-true Type $parameter */
Similar to above but for functions or methods that have a boolean return type. This asserts that the passed variable is of the specified type on the true or false code path respectively at the call location.

@mixin
/** @mixin ClassName */
This annotation is used to declare that the members of the specified class are mixed in to the current class via __call, __callStatic, __get or __set magic methods. Only available with a licence in Intelephense Premium.

@disregard
/** @disregard PXXXX */
This annotation is used to suppress a specific diagnostic at the statement following the annotation. For example, @disregard P1010 would suppress the diagnostic with code P1010. This can be useful when you have a specific case where you want to allow something that Intelephense would normally report as an issue.

@type-alias
/** @type-alias TypeName = Type */
This annotation is used to declare a type alias. A type alias allows you to create a new name for an existing type, which can be useful for improving code readability or for creating more meaningful type names. It functions the same as @phpstan-type and @psalm-type annotations which are also recognised. Intelephense type aliases follow normal PHP namespace rules.

@import-type
/** @import-type TypeName as OptionalAlias */
This annotation is used to import a type alias that has been declared in another file. It functions similarly to @phpstan-import-type and @psalm-import-type and both these annotations may also be used. However, type aliases are not bound to classes in Intelephense and as such the from ClassName specifier is unnecessary but still supported. Type aliases in Intelephense follow normal PHP namespace rules.

### Features
Intelephense provides a variety of features to enhance the development experience when working with PHP code. Many of these features are provided for free while others require a Premium licence to access. All images and videos in this section are taken from the VS Code client. The features are available to all LSP clients that support the relevant LSP methods. Keybindings listed for each feature are the defaults for the VS Code client.

### Free Features
The following features are available to all users of Intelephense. A licence is not necessary.

### LSP
workspace/symbol

### Keybinding
Ctrl+T
This feature allows you to search for symbols in your workspace and navigate to their definitions. It is particularly useful for finding and navigating to symbols that are not directly referenced in the current file. When the query contains alphanumeric characters only, the search is performed on the unqualified name of the symbol. You can narrow your search to a specific symbol by using a query containing characters found in the Fully Qualified Structural Element Name (FQSEN) of the symbol. For example, a query of m\pt:u( would find the method with FQSEN App\Models\Post::user().

Unfortunately, VS Code has a current issue where it will discard results if the query contains a backslash. This means that you cannot search on the namespace part of a type.

Workspace Symbols panel in VS Code showing search results for a PHP symbol
Searching for workspace symbols using the FQSEN query syntax

### LSP
textDocument/documentSymbol

### Keybinding
Ctrl+Shift+O
This feature lists all symbols in the current document, providing an overview of the structure of the file. A client can use this information to provide a document outline view, breadcrumb navigation, and a symbol search specific to the current file.

Document Symbols outline panel showing PHP class and method structure
Document symbols provide an outline of the current file's structure
Go to Definition

### LSP
textDocument/definition

### Keybinding
F12 | right-click context menu
This feature allows you to navigate to the definition of a symbol when invoked on a reference to that symbol in the current file. Multiple definitions may sometimes be found for a symbol. For example, invoking the feature on the type name in a new expression may find both the constructor method and the class declaration as definitions. It is up to the client to decide how to present multiple definitions to the user. For example a peek definitions window may open or the user may simply be navigated to the first definition in the list.

Go to Definition navigates directly to a symbol's definition

### LSP
textDocument/hover

### Keybinding
Ctrl+K Ctrl+I | mouse-over
This feature provides information about a symbol when hovering over a reference to that symbol in the current file. The information provided can include the type of the symbol, it's signature if it is a function or method, and any associated documentation.

Hover tooltip showing PHP symbol type information and documentation
Hover shows type information and documentation for a symbol

### LSP
textDocument/documentHighlight

### Keybinding
Displayed automatically at the cursor position
This feature highlights all references to the symbol at the cursor position in the current file. This can be useful for quickly identifying all usages of a symbol in the current file. Read and write contexts will be identified if applicable and the client can choose to highlight them differently if desired.

Document Highlight marking all references to a PHP symbol in the editor
Document Highlight marks all references to the symbol under the cursor. Read and write contexts are coloured differently.

### LSP
textDocument/completion

### Keybinding
Ctrl+Space
Trigger characters
$ > : \ / ' " * . <
This feature provides a list of context appropriate completion suggestions for a symbol at the cursor position in the current file. The completions can include variables, functions, methods, classes, and other symbols. Where appropriate, additional edits are provided to automatically import a symbol.

Code Completion dropdown with context-aware PHP symbol suggestions
Code Completion provides context-aware suggestions as you type

### LSP
textDocument/signatureHelp

### Keybinding
Ctrl+Shift+Space
Trigger characters
( , :
This feature provides information about the signature of a function or method when the cursor is within the argument list of a function or method call. The information provided can include the types of the parameters, the return type, and any associated documentation.

Signature Help popup displaying PHP function parameter information
Signature Help displays parameter information for the current function call

### LSP
textDocument/references

### Keybinding
Shift+F12 | right-click context menu
This feature provides a list of all references to a symbol in the current file or workspace. The references can include variables, functions, methods, classes, and other symbols. When there is a hierarchy of types, references to a type member will be determined relative to the initial base members.

Find All References panel listing all usages of a PHP symbol
Find All References lists every usage of a symbol across the workspace

### LSP
textDocument/formatting

### Keybinding
Ctrl+Shift+I (format document)

### LSP
textDocument/rangeFormatting

### Keybinding
Ctrl+K Ctrl+F (format selection)
This feature provides formatting of a whole document or a selected range within a document. The Intelephense formatter is opinionated and aims to comply with PHP-FIG coding standards. Limited configuration options are available to allow some customisation of brace style.

Formatter applies PHP-FIG coding standards to the document

### LSP
textDocument/publishDiagnostics

### Keybinding
Published automatically onType or onSave | F8 (next) | Shift+F8 (previous)
This feature provides diagnostics for the currently opened files. Diagnostics include syntax errors, type errors, language constraints and other issues detected by Intelephense. Intelephense aims to provide rapid diagnostics that are aligned with the PHP engine where possible.

Performance and minimising false positives are prioritised over exhaustiveness. It should not be used as a substitute for testing your code. The diagnostics emitted can be configured in the settings to be more or less thorough or ignored altogether depending on your preferences and the codebase you are working with.

If you need fine grain control over which diagnostics are shown, try the intelephense.diagnostics.exclude setting. This setting allows you to map a file glob to an array of diagnostic codes to exclude from diagnostics. A full list of diagnostic codes can be found in the vscode-intelephense repository.

By default, Intelephense performs type checking on declared types only and in a relaxed mode in order to reduce false positives. In a hierarchy of types, a sub-type satisfies a super-type constraint. Intelephense also permits the reverse. That is, a super-type or wider type can be assigned to a sub-type or narrower type constraint. This default behaviour has been chosen due to inherent limitations in static analysis, the lack of syntax in PHP or PHPDoc to enable a developer to inline cast an expression or variable, and due to the variable quality of type information in some codebases.

To make type checks more thorough, there are several settings available.

intelephense.diagnostics.relaxedTypeCheck controls whether to emit diagnostics when a super-type (excluding mixed) is assigned to a sub-type constraint.
intelephense.diagnostics.noMixedTypeCheck controls whether to emit diagnostics when mixed is assigned to narrower type constraints.
intelephense.diagnostics.strictTypes is a global equivalent to adding declare(strict_types=1); to the top of each file.
intelephense.diagnostics.typeCheckDocumentedTypes controls whether documented types are included in type checking.
Diagnostics panel showing PHP type errors and warnings inline in the editor
Diagnostics surface type errors and other issues either as you type or on save depending on your settings.

### LSP
textDocument/inlineValues

### Keybinding
Displayed automatically during a debug session
This feature provides ranges and text for variables in a file that may be relevant for a debugger to display inline values for during a debugging session. To see this feature in action in VS Code, install the official Xdebug extension.

Inline Values showing variable states in the editor during a debug session
Inline Values display variable states during a debug session

### Embedded Languages
Intelephense presumes that text outside of PHP tags is HTML. Basic language intelligence is provided for HTML and embedded CSS and JavaScript within HTML.

Language intelligence for HTML and CSS embedded within a PHP file
Language intelligence for HTML, CSS, and JavaScript within PHP files

### Premium Features
The following features require a licence to access. A licence can be purchased at the checkout page.

### LSP
textDocument/rename

### Keybinding
F2 | right-click context menu
This feature allows you to rename a symbol and all references to that symbol in the current file or workspace. This differs from a simple text find and replace in that it is aware of the syntax and semantics of the code, and will only rename the specific symbol.

Intelephense will prefer to limit renames to the current file if possible. For example, renaming a class reference in a file where the class has been imported with a use declaration will result in the references in that file only being renamed and the use declaration being updated with an alias. In such cases, to rename a symbol across the whole workspace, invoke the rename feature on the class declaration itself or the Fully Qualified Name (FQN) in the use declaration instead.

Renaming a namespace in a file updates imports and FQN references for the file symbols in that namespace through the workspace. If using PSR-4 style folder structures then renaming the namespace of a class is also the equivalent of a move class to file operation. Intelephense will return file rename instructions to the client in such cases.

Rename refactors a symbol and all its references across the workspace

### LSP
textDocument/foldingRange

### Keybinding
Ctrl+Shift+[ (fold) | Ctrl+Shift+] (unfold) | left-click editor gutter | right-click context menu
This feature allows you to fold and unfold regions of code in the current file. Intelephense provides folding ranges for symbol definition bodies, control structures, comments, imports, and custom regions identified by #region and #endregion comments. The folding provider is syntax tree driven and is more reliable than indent based folding providers such as the default provider in VS Code.

Code Folding collapses and expands regions based on the syntax tree

### LSP
textDocument/implementation

### Keybinding
Ctrl+F12 | right-click context menu
This feature provides a list of all implementations of a method or interface when invoked on a reference. This functions similar to go to definition but differs in that it will find the classes that implement the interface or methods that implement an abstract method declaration.

Find All Implementations listing concrete classes implementing a PHP interface
Find All Implementations lists all concrete implementations of an interface or abstract method
Go to Type Definition

### LSP
textDocument/typeDefinition

### Keybinding
Right-click context menu
This feature allows you to navigate to the type definition of a variable. Similar to go to definition but differs in that it will navigate to the type definition rather than the variable declaration itself.

Go to Type Definition navigates to the type of a variable
Go to Declaration

### LSP
textDocument/declaration

### Keybinding
Right-click context menu
This feature allows you to navigate to the initial declaration of a symbol. Similar to go to definition, and depending on the context may function the same, it differs in that it will navigate to the initial declaration of a symbol in a hierarchy of types. For example, invoking this feature on a sub-type method reference will navigate to the initial declaration of the method in a super-type rather than the sub-type method declaration itself.

Go to Declaration navigates to the initial declaration in a type hierarchy

### LSP
textDocument/selectionRange

### Keybinding
Shift+Alt+→ (expand) | Shift+Alt+← (shrink)
This feature allows you to expand and shrink the current selection in the current file based on the syntax tree of the code. For example, if the cursor is on a variable name, the first expansion would select the variable name, the second expansion would select the whole variable declaration, the third expansion would select the whole statement, the fourth expansion would select the whole block, and so on. Being syntax tree driven, it is more precise than regex or indent based selection providers such as the default provider in VS Code.

Smart Select expands or shrinks the selection based on the syntax tree

### LSP
textDocument/typeHierarchy

### Keybinding
Right-click context menu
This feature provides a type hierarchy for a class, interface, trait or enum when invoked on a reference to the type. It is useful for understanding the inheritance structure of a type and for quick navigation to types in the hierarchy.

Type Hierarchy panel showing the inheritance structure of a PHP class
Type Hierarchy shows the inheritance structure of a type

### LSP
textDocument/codeLens

### Keybinding
Rendered inline above declarations | activated by left-clicking
This feature provides additional information and navigation for symbol declarations in the current file. Several lenses are provided by Intelephense. They are disabled by default to reduce visual clutter, see the intelephense.codeLens settings to enable them.

References: shows the number of references to a symbol in the workspace and provides a link to view those references.
Implementations: shows the number of implementations of an interface or abstract method and provides a link to view those implementations.
Overrides: shows the number of overrides of a method in a type hierarchy and provides a link to view those overrides.
Parent: shows whether a method overrides a parent method and provides a link to view the parent method.
Usages: shows the number of types that use a trait and provides a link to view those usages.
Code Lens displaying reference counts above PHP class and method declarations
Code Lens displays reference counts and navigation links above declarations

### LSP
textDocument/inlayHint

### Keybinding
Displayed inline automatically
This feature provides additional type and parameter information in the form of hints that are displayed inline with the code in the current file. Intelephense provides several types of inlay hints. They are enabled by default. See the intelephense.inlayHints settings to configure them.

Parameter Name: shows the name of a parameter for a function or method argument.
Parameter Type: shows the inferred type of a parameter in a closure that is an argument to another function or method when it has not been explicitly declared.
Return Type: shows the inferred return type of a function or method when it has not been explicitly declared.
Inlay Hints showing inferred parameter names and return types inline in PHP code
Inlay Hints show inferred parameter names and return types inline

### LSP
textDocument/documentLink

### Keybinding
Ctrl+Click | mouse-over
This feature provides clickable links to related files and resources from the current file. Intelephense will show links to files referenced in require and include statements, and to local files referenced in @see annotations.

If your require statements are relative or you reference $_SERVER['DOCUMENT_ROOT'], you may need to configure the intelephense.environment.documentRoot setting to the correct path for the links to work. Intelephense will fallback to the workspace folder path if this setting has no value.

Document Links showing clickable require and include paths in a PHP file
Document Links make require/include paths and @see annotations clickable

### LSP
textDocument/codeAction

### Keybinding
Ctrl+. | left-click lightbulb
This feature provides a list of context appropriate actions that can be performed at the cursor position in the current file. VS Code will show a lightbulb icon on the current line when code actions are available. Intelephense provides several code actions.

Import Symbol: Import (use) a type, function or constant to resolve an undefined symbol error.
Add PHPDoc: Generate PHPDoc for functions, classes, and methods.
Implement All Abstract Methods: Generate method stubs for all abstract methods that have not been implemented in a class.
Code Actions offer quick-fix and refactoring options at the cursor position

### Appendix
Compatibility With Frameworks and Libraries
Intelephense aims to support all PHP frameworks and libraries but does not implement specific solutions for these. Limited or unexpected language intelligence can sometimes be provided if the package:

Declares symbols at runtime via bootstrapping code or configuration.
Uses interfaces heavily but encourages calling methods only declared on implementations.
Uses __get,__call, or __callStatic magic heavily without corresponding @property or @method annotations.
Has insufficient or incorrect type declarations/annotations.
In such cases you may notice a lack of completion suggestions, trouble jumping to definitions or undefined symbol diagnostics may appear even though the code may work when executed.

For example, a common problem can be when a framework returns an interface from a function but the project has been bootstrapped to use a particular concrete type that has additional methods not declared on the interface.

<?php

interface View {}

class CustomView implements View
{
  public function customViewMethod() {}
}

function view(): View
{
  //some code that happens to return CustomView at runtime based on some bootstrapping code or config
}

view()->customViewMethod(); //undefined method 😭
There are several ways to workaround the problem above. These workarounds can fall into two categories. Either they become part of the project executable code itself, or they are declared in a non-executable helper file and are there only to override the default Intelephense behaviour.

Solutions that form part of the executable code
The advantage here is that problems in the code would become more apparent if the bootstrapping logic ever changed and returned a different class. The disadvantage is it is more code to write and perhaps difficult to retrofit to existing code.

<?php

//Assign the return value to a variable and narrow the type
$view = view();
if (! $view instanceof CustomView) {
  throw new Exception('Unexpected View instance');
}
$view->customViewMethod();

//Or with an annotation.
//This won't alter the execution of the code but still involves modifying the executable code.

/** @var CustomView $view */
$view = view();
$view->customViewMethod();

//A custom function could also be created and called instead to narrow the type
function customView(): CustomView
{
  $view = view();
  assert($view instanceof CustomView);
  return $view;
}

customView()->customViewMethod();
Solutions that do not form part of the project executable code
This involves creating a file with alternate symbol declarations and placing it in your workspace folder (not in vendor). Intelephense will prioritise user declared symbols over vendor declared symbols.

The advantage here is that it can be retrofitted easily to existing code, applies to all usages of the symbol and executable code remains untouched. The disadvantage is that it could suppress an actual error that Intelephense would otherwise detect.

<?php
// Create a file and add it to your workspace.
// eg intelephense_helper.php

// Declare a different signature for the view function.
// One that declares the concrete return type.
function view(): CustomView {}

// Or add the undefined method to the interface instead.
interface View
{
  function customViewMethod();
}
If classes, interfaces, traits, or enums have override definitions then Intelephense will treat them as partial types and merge them with the vendor declared types. Type overrides should either not use extends or implements clauses, or, alternatively keep them the same as the real type because implements and extends values are not merged.

There are also packages that provide or generate IDE helper files that may improve the experience when using various frameworks and libraries. For example:

laravel-ide-helper

PHPDoc Instead of PHPStorm Metadata/Attributes
PHPStorm provides a way to override or express types using metadata and custom attributes in order to provide better language intelligence for code that is difficult to analyse statically, and to address limitations in the PHP language.

The same can be achieved with PHPDoc types. For greater compatibility with Intelephense and other PHP static analysis tools such as Psalm and PHPStan it is recommended to use PHPDoc types instead of PHPStorm metadata and attributes.

Intelephense does not support PHPStorm attributes and provides only limited support for PHPStorm metadata. Support for PHPStorm metadata may be removed in future versions of Intelephense.

The following examples show how to express types using PHPDoc types instead of PHPStorm metadata and attributes.

<?php

class RedService {}
class BlueObject {}
class GreenCollection {}

// ----------------------------------------------------------------------------------------------
// Problem:
// A function accepts string|object and returns this type after performing some operation.
// We want to return a string if a string is passed or a specific object if an object is passed,
// not a string|object.

// Using PHPStorm metadata:
function paintColourMeta(string|object $input): string|object {}

PHPSTORM_METADATA\override(paintColourMeta(), PHPSTORM_METADATA\type(0));

// Using PHPDoc annotations:

/**
 * @template T of string|object
 * @param T $input
 * @return T
 */
function paintColourDoc(string|object $input): string|object {}
$result = paintColourDoc(new BlueObject); // $result is inferred as BlueObject

// ----------------------------------------------------------------------------------------------
// Problem:
// A function accepts a string and returns a different type based on the string passed in.
// We want to return a specific type based on the string argument, not a union of all possible return types.

// Using PHPStorm metadata:
function getColourMeta(string $value): mixed {}

PHPSTORM_META\override(getColourMeta(), PHPSTORM_META\map([
    'red' => RedService::class,
    'blue' => BlueObject::class,
    'green' => GreenCollection::class,
]));

// Using PHPDoc annotations:

/**
 * @template T of array{red: RedService, blue: BlueObject, green: GreenCollection}
 * @template K of key-of<T>
 * @param K $value
 * @return T[K]
 */
function getColourDoc(string $value): mixed {}
$obj = getColourDoc('red'); // $obj is inferred as RedService

// ----------------------------------------------------------------------------------------------
// Problem:
// A function returns an array with a specific set of string keys.
// We want to provide language intelligence based on the keys and value types of the returned array.

// Using PHPStorm attributes:

### [\JetBrains\PhpStorm\ArrayShape(['red' => RedService::class, 'blue' => BlueObject::class, 'green' => GreenCollection::class])]
function getColoursAttr(): array {}

// Using PHPDoc annotations:

/**
 * @return array{red: RedService, blue: BlueObject, green: GreenCollection}
 */
function getColoursDoc(): array {}
$green = getColoursDoc()['green']; // $green is inferred as GreenCollection

// ----------------------------------------------------------------------------------------------
// Problem:
// A function accepts a specific set of string literals as arguments.
// We want to provide language intelligence based on the allowed string literals

// Using PHPStorm attributes:

### [\JetBrains\PhpStorm\ExpectedValues(values: ['red', 'blue', 'green'])]
function setColourAttr(string $colour): void {}

// Using PHPDoc annotations:

/**
 * @param 'red'|'blue'|'green' $colour
 * @return void
 */
function setColourDoc(string $colour): void {}
setColourDoc(''); // Completion suggestions for 'red', 'blue', 'green'

---

## DOCUMENT: Intelephense: README
**Source:** https://raw.githubusercontent.com/bmewburn/intelephense-docs/master/README.md
**Ingested At:** 2026-05-16T00:35:18.214Z

### Intelephense
Intelephense is a high performance, cross platform PHP language server adhering to the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/).

When paired with an LSP capable editor it provides an essential set of code intelligence features that give a PHP developer a productive and rich editing experience.

This is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to all current and future features can be obtained by purchasing a licence key at https://intelephense.com.

### Installation


### Getting Started


### Features


### Support


### Licence


---

## DOCUMENT: Intelephense: installation
**Source:** https://raw.githubusercontent.com/bmewburn/intelephense-docs/master/installation.md
**Ingested At:** 2026-05-16T00:35:18.251Z

### Installation


### Visual Studio Code
Visual Studio Code users should install the Intelephense extension from within the extensions view or download from the [marketplace](https://marketplace.visualstudio.com/items?itemName=bmewburn.vscode-intelephense-client).

1. Disable the built-in VSCode PHP Language Features.

    * Go to `Extensions`.
    * Search for `@builtin php`
    * Disable `PHP Language Features`. Leave `PHP Language Basics` enabled for syntax highlighting.

    Note that other (3rd party) PHP extensions which provide similar functionality should also be disabled for best results.
2. Add glob patterns for non standard php file extensions to the `files.associations` setting.

    For example: `"files.associations": { "*.module": "php" }`.
3. Optionally purchase and enter your [licence key](https://intelephense.com) by opening the command pallete
-- `ctrl + shift + p` -- and searching for `Enter licence key`.

Further configuration options are available in the `intelephense` section of settings.

### Other Editors


### Requirements
[Node.js 12+](https://nodejs.org)

### Server Installation
```
npm i intelephense -g
```

### Language Server Protocol (LSP) Client
Intelephense needs an LSP compliant client to communicate with and integrate features into the editor. A list of editors and clients that support the LSP can be found at https://microsoft.github.io/language-server-protocol/implementors/tools/.

Please follow the setup guide of the relevant tool. The Information below may help in configuring the client.

### Run
```
intelephense {transport}
```
Where `{transport}` is one of:
* `--node-ipc`
* `--stdio`
* `--socket={number}`
* `--pipe={string}`

### Initialisation Options
```typescript
interface InitialisationOptions {
    //Optional absolute path to storage dir. Defaults to os.tmpdir().
    storagePath?: string;

    //Optional absolute path to a global storage dir. Defaults to os.homedir().
    globalStoragePath?: string;

    //Optional licence key or absolute path to a text file containing the licence key.
    //{os.homedir()}/intelephense/licence.txt will also be checked by
    //default if initializationOptions are not exposed by client.
    licenceKey?: string;

    //Optional flag to clear server state.
    //State can also be cleared by deleting {storagePath}/intelephense
    clearCache?: boolean;
}
```

### Capabilities
<details>
	<summary>Server capabilities JSON returned from `initialize` request.</summary>

```javascript
{
	textDocumentSync: TextDocumentSyncKind.Incremental,
	documentSymbolProvider: true,
	workspaceSymbolProvider: true,
	completionProvider: {
		triggerCharacters: [
			//php
			'$', '>', ':', '\\', '/',
			//phpdoc
			'*',
			// html/js
			'.', '<'
		],
		resolveProvider: true
	},
	signatureHelpProvider: {
		triggerCharacters: ['(', ',']
	},
	definitionProvider: true,
	referencesProvider: true,
	hoverProvider: true,
	documentFormattingProvider: true,	    //Dynamic registration if available.
    documentRangeFormattingProvider: true,  //Dynamic registration if available.
	documentHighlightProvider: true,
	workspace: {
		workspaceFolders: {
			supported: true,
			changeNotifications: true
		}
	},
	foldingRangeProvider: true,		//With licence key only.
	implementationProvider: true,	//With licence key only.
	declarationProvider: true,		//With licence key only.
	renameProvider: { 			    //With licence key only.
		prepareProvider: true
	},
	typeDefinitionProvider: true,	//With licence key only.
    selectionRangeProvider: true    //With licence key only.
}
```
</details>

### Configuration Options
<details>
	<summary>JSON schema for `workspace/configuration` request data</summary>

```json
{
    "intelephense.compatibility.correctForBaseClassStaticUnionTypes": {
        "type": "boolean",
        "default": true,
        "description": "Resolves `BaseClass|static` union types to `static` instead of `BaseClass`.",
        "scope": "window"
    },
    "intelephense.compatibility.correctForArrayAccessArrayAndTraversableArrayUnionTypes": {
        "type": "boolean",
        "default": true,
        "description": "Resolves `ArrayAccess` and `Traversable` implementations that are unioned with a typed array to generic syntax. eg `ArrayAccessOrTraversable|ElementType[]` => `ArrayAccessOrTraversable<mixed, ElementType>`.",
        "scope": "window"
    },
    "intelephense.files.maxSize": {
        "type": "number",
        "default": 1000000,
        "description": "Maximum file size in bytes.",
        "scope": "window"
    },
    "intelephense.files.associations": {
        "type": "array",
        "default": [
            "*.php",
            "*.phtml"
        ],
        "description": "Configure glob patterns to make files available for language server features. Inherits from files.associations.",
        "scope": "window"
    },
    "intelephense.files.exclude": {
        "type": "array",
        "items": {
            "type": "string"
        },
        "default": [
            "**/.git/**",
            "**/.svn/**",
            "**/.hg/**",
            "**/CVS/**",
            "**/.DS_Store/**",
            "**/node_modules/**",
            "**/bower_components/**",
            "**/vendor/**/{Tests,tests}/**",
            "**/.history/**",
            "**/vendor/**/vendor/**"
        ],
        "description": "Configure glob patterns to exclude certain files and folders from all language server features. Inherits from files.exclude.",
        "scope": "resource"
    },
    "intelephense.stubs": {
        "type": "array",
        "items": {
            "type": "string",
            "enum": [
                "amqp",
                "apache",
                "apcu",
                "bcmath",
                "blackfire",
                "bz2",
                "calendar",
                "cassandra",
                "com_dotnet",
                "Core",
                "couchbase",
                "crypto",
                "ctype",
                "cubrid",
                "curl",
                "date",
                "dba",
                "decimal",
                "dom",
                "ds",
                "enchant",
                "Ev",
                "event",
                "exif",
                "fann",
                "FFI",
                "ffmpeg",
                "fileinfo",
                "filter",
                "fpm",
                "ftp",
                "gd",
                "gearman",
                "geoip",
                "geos",
                "gettext",
                "gmagick",
                "gmp",
                "gnupg",
                "grpc",
                "hash",
                "http",
                "ibm_db2",
                "iconv",
                "igbinary",
                "imagick",
                "imap",
                "inotify",
                "interbase",
                "intl",
                "json",
                "judy",
                "ldap",
                "leveldb",
                "libevent",
                "libsodium",
                "libxml",
                "lua",
                "lzf",
                "mailparse",
                "mapscript",
                "mbstring",
                "mcrypt",
                "memcache",
                "memcached",
                "meminfo",
                "meta",
                "ming",
                "mongo",
                "mongodb",
                "mosquitto-php",
                "mqseries",
                "msgpack",
                "mssql",
                "mysql",
                "mysql_xdevapi",
                "mysqli",
                "ncurses",
                "newrelic",
                "oauth",
                "oci8",
                "odbc",
                "openssl",
                "parallel",
                "Parle",
                "pcntl",
                "pcov",
                "pcre",
                "pdflib",
                "PDO",
                "pdo_ibm",
                "pdo_mysql",
                "pdo_pgsql",
                "pdo_sqlite",
                "pgsql",
                "Phar",
                "phpdbg",
                "posix",
                "pspell",
                "pthreads",
                "radius",
                "rar",
                "rdkafka",
                "readline",
                "recode",
                "redis",
                "Reflection",
                "regex",
                "rpminfo",
                "rrd",
                "SaxonC",
                "session",
                "shmop",
                "SimpleXML",
                "snmp",
                "soap",
                "sockets",
                "sodium",
                "solr",
                "SPL",
                "SplType",
                "SQLite",
                "sqlite3",
                "sqlsrv",
                "ssh2",
                "standard",
                "stats",
                "stomp",
                "suhosin",
                "superglobals",
                "svn",
                "sybase",
                "sync",
                "sysvmsg",
                "sysvsem",
                "sysvshm",
                "tidy",
                "tokenizer",
                "uopz",
                "uv",
                "v8js",
                "wddx",
                "win32service",
                "winbinder",
                "wincache",
                "wordpress",
                "xcache",
                "xdebug",
                "xhprof",
                "xml",
                "xmlreader",
                "xmlrpc",
                "xmlwriter",
                "xsl",
                "xxtea",
                "yaf",
                "yaml",
                "yar",
                "zend",
                "Zend OPcache",
                "ZendCache",
                "ZendDebugger",
                "ZendUtils",
                "zip",
                "zlib",
                "zmq",
                "zookeeper"
            ]
        },
        "default": [
            "apache",
            "bcmath",
            "bz2",
            "calendar",
            "com_dotnet",
            "Core",
            "ctype",
            "curl",
            "date",
            "dba",
            "dom",
            "enchant",
            "exif",
            "FFI",
            "fileinfo",
            "filter",
            "fpm",
            "ftp",
            "gd",
            "gettext",
            "gmp",
            "hash",
            "iconv",
            "imap",
            "intl",
            "json",
            "ldap",
            "libxml",
            "mbstring",
            "meta",
            "mysqli",
            "oci8",
            "odbc",
            "openssl",
            "pcntl",
            "pcre",
            "PDO",
            "pdo_ibm",
            "pdo_mysql",
            "pdo_pgsql",
            "pdo_sqlite",
            "pgsql",
            "Phar",
            "posix",
            "pspell",
            "readline",
            "Reflection",
            "session",
            "shmop",
            "SimpleXML",
            "snmp",
            "soap",
            "sockets",
            "sodium",
            "SPL",
            "sqlite3",
            "standard",
            "superglobals",
            "sysvmsg",
            "sysvsem",
            "sysvshm",
            "tidy",
            "tokenizer",
            "xml",
            "xmlreader",
            "xmlrpc",
            "xmlwriter",
            "xsl",
            "Zend OPcache",
            "zip",
            "zlib"
        ],
        "description": "Configure stub files for built in symbols and common extensions. The default setting includes PHP core and all bundled extensions.",
        "scope": "window"
    },
    "intelephense.completion.insertUseDeclaration": {
        "type": "boolean",
        "default": true,
        "description": "Use declarations will be automatically inserted for namespaced classes, traits, interfaces, functions, and constants.",
        "scope": "window"
    },
    "intelephense.completion.fullyQualifyGlobalConstantsAndFunctions": {
        "type": "boolean",
        "default": false,
        "description": "Global namespace constants and functions will be fully qualified (prefixed with a backslash).",
        "scope": "window"
    },
    "intelephense.completion.triggerParameterHints": {
        "type": "boolean",
        "default": true,
        "description": "Method and function completions will include parentheses and trigger parameter hints.",
        "scope": "window"
    },
    "intelephense.completion.maxItems": {
        "type": "number",
        "default": 100,
        "description": "The maximum number of completion items returned per request.",
        "scope": "window"
    },
    "intelephense.format.enable": {
        "type": "boolean",
        "default": true,
        "description": "Enables formatting.",
        "scope": "window"
    },
    "intelephense.format.braces": {
        "type": "string",
        "default": "psr12",
        "enum": [
            "psr12",
            "allman",
            "k&r"
        ],
        "enumDescriptions": [
            "PHP-FIG PSR-2 and PSR-12 style. A mix of Allman and K&R",
            "Allman. Opening brace on the next line.",
            "K&R (1TBS). Opening brace on the same line."
        ],
        "description": "Controls formatting style of braces",
        "scope": "window"
    },
    "intelephense.environment.documentRoot": {
        "type": "string",
        "description": "The directory of the entry point to the application (index.php). Defaults to the first workspace folder. Used for resolving script inclusion.",
        "scope": "window"
    },
    "intelephense.environment.includePaths": {
        "type": "array",
        "items": {
            "type": "string"
        },
        "description": "The include paths (as individual path items) as defined in the include_path ini setting. Used for resolving script inclusion.",
        "scope": "window"
    },
    "intelephense.environment.phpVersion": {
        "type": "string",
        "default": "7.4.0",
        "description": "A semver compatible string that represents the target PHP version. Used for providing version appropriate suggestions and diagnostics. PHP 5.3.0 and greater supported.",
        "scope": "window"
    },
    "intelephense.environment.shortOpenTag": {
        "type": "boolean",
        "default": false,
        "description": "When enabled '<?' will be parsed as a PHP open tag. Defaults to false.",
        "scope": "window"
    },
    "intelephense.diagnostics.enable": {
        "type": "boolean",
        "default": true,
        "description": "Enables diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.run": {
        "type": "string",
        "default": "onType",
        "enum": [
            "onType",
            "onSave"
        ],
        "enumDescriptions": [
            "Diagnostics will run as changes are made to the document.",
            "Diagnostics will run when the document is saved."
        ],
        "description": "Controls when diagnostics are run.",
        "scope": "window"
    },
    "intelephense.diagnostics.embeddedLanguages": {
        "type": "boolean",
        "default": true,
        "description": "Enables diagnostics in embedded languages.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedSymbols": {
        "type": "boolean",
        "default": true,
        "description": "DEPRECATED. Use the setting for each symbol category.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedVariables": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined variable diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedTypes": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined class, interface and trait diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedFunctions": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined function diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedConstants": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined constant diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedClassConstants": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined class constant diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedMethods": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined method diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedProperties": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined static property diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.unusedSymbols": {
        "type": "boolean",
        "default": true,
        "description": "Enables unused variable, private member, and import diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.unexpectedTokens": {
        "type": "boolean",
        "default": true,
        "description": "Enables unexpected token diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.duplicateSymbols": {
        "type": "boolean",
        "default": true,
        "description": "Enables duplicate symbol diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.argumentCount": {
        "type": "boolean",
        "default": true,
        "description": "Enables argument count diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.typeErrors": {
        "type": "boolean",
        "default": true,
        "description": "Enables diagnostics on type compatibility of arguments, property assignments, and return statements where types have been declared.",
        "scope": "window"
    },
    "intelephense.diagnostics.deprecated": {
        "type": "boolean",
        "default": true,
        "description": "Enables deprecated diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.languageConstraints": {
        "type": "boolean",
        "default": true,
        "description": "Enables reporting of various language constraint errors.",
        "scope": "window"
    },
    "intelephense.diagnostics.implementationErrors": {
        "type": "boolean",
        "default": true,
        "description": "Enables reporting of problems associated with method and class implementations. For example, unimplemented methods or method signature incompatibilities.",
        "scope": "window"
    },
    "intelephense.runtime": {
        "type": "string",
        "description": "Path to a Node.js executable. Use this if you wish to use a different version of Node.js. Defaults to Node.js shipped with VSCode.",
        "scope": "machine"
    },
    "intelephense.maxMemory": {
        "type": "number",
        "description": "Maximum memory (in MB) that the server should use. On some systems this may only have effect when runtime has been set. Minimum 256.",
        "scope": "window"
    },
    "intelephense.licenceKey": {
        "type": "string",
        "description": "DEPRECATED. Don't use this. Go to command palette and search for enter licence key.",
        "scope": "application"
    },
    "intelephense.telemetry.enabled": {
        "type": "boolean",
        "description": "Anonymous usage and crash data will be sent to Azure Application Insights. Inherits from telemetry.enableTelemetry.",
        "scope": "window",
        "default": null
    },
    "intelephense.rename.exclude": {
        "type": "array",
        "items": {
            "type": "string"
        },
        "default": [
            "**/vendor/**"
        ],
        "description": "Glob patterns matching files and folders that should be excluded when renaming symbols. Rename operation will fail if the symbol definition is found in the excluded files/folders.",
        "scope": "resource"
    },
    "intelephense.references.exclude": {
        "type": "array",
        "items": {
            "type": "string"
        },
        "default": [
            "**/vendor/**"
        ],
        "description": "Glob patterns matching files and folders that should be excluded from references search.",
        "scope": "resource"
    },
    "intelephense.phpdoc.returnVoid": {
        "type": "boolean",
        "default": true,
        "description": "Adds `@return void` to auto generated phpdoc for definitions that do not return a value.",
        "scope": "window"
    },
    "intelephense.phpdoc.textFormat": {
        "type": "string",
        "enum": [
            "snippet",
            "text"
        ],
        "default": "snippet",
        "enumDescriptions": [
            "Auto generated phpdoc is returned in snippet format. Templates are partially resolved by evaluating phpdoc specific variables only.",
            "Auto generated phpdoc is returned as plain text. Templates are resolved completely by the server."
        ],
        "scope": "window"
    },
    "intelephense.phpdoc.classTemplate": {
        "type": "object",
        "properties": {
            "summary": {
                "type": "string",
                "description": "A snippet string representing a phpdoc summary."
            },
            "description": {
                "type": "string",
                "description": "A snippet string representing a phpdoc description."
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "An array of snippet strings representing phpdoc tags."
            }
        },
        "default": {
            "summary": "$1",
            "tags": [
                "@package ${1:$SYMBOL_NAMESPACE}"
            ]
        },
        "description": "An object that describes the format of generated class/interface/trait phpdoc. The following snippet variables are available: SYMBOL_NAME; SYMBOL_KIND; SYMBOL_TYPE; SYMBOL_NAMESPACE.",
        "scope": "window"
    },
    "intelephense.phpdoc.propertyTemplate": {
        "type": "object",
        "properties": {
            "summary": {
                "type": "string",
                "description": "A snippet string representing a phpdoc summary."
            },
            "description": {
                "type": "string",
                "description": "A snippet string representing a phpdoc description."
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "An array of snippet strings representing phpdoc tags."
            }
        },
        "default": {
            "summary": "$1",
            "tags": [
                "@var ${1:$SYMBOL_TYPE}"
            ]
        },
        "description": "An object that describes the format of generated property phpdoc. The following snippet variables are available: SYMBOL_NAME; SYMBOL_KIND; SYMBOL_TYPE; SYMBOL_NAMESPACE.",
        "scope": "window"
    },
    "intelephense.phpdoc.functionTemplate": {
        "type": "object",
        "properties": {
            "summary": {
                "type": "string",
                "description": "A snippet string representing a phpdoc summary."
            },
            "description": {
                "type": "string",
                "description": "A snippet string representing a phpdoc description."
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "An array of snippet strings representing phpdoc tags."
            }
        },
        "default": {
            "summary": "$1",
            "tags": [
                "@param ${1:$SYMBOL_TYPE} $SYMBOL_NAME $2",
                "@return ${1:$SYMBOL_TYPE} $2",
                "@throws ${1:$SYMBOL_TYPE} $2"
            ]
        },
        "description": "An object that describes the format of generated function/method phpdoc. The following snippet variables are available: SYMBOL_NAME; SYMBOL_KIND; SYMBOL_TYPE; SYMBOL_NAMESPACE.",
        "scope": "window"
    },
    "intelephense.phpdoc.useFullyQualifiedNames": {
        "type": "boolean",
        "default": false,
        "description": "Fully qualified names will be used for types when true. When false short type names will be used and imported where appropriate. Overrides intelephense.completion.insertUseDeclaration.",
        "scope": "window"
    }
}
```
</details>

---

## DOCUMENT: Intelephense: gettingStarted
**Source:** https://raw.githubusercontent.com/bmewburn/intelephense-docs/master/gettingStarted.md
**Ingested At:** 2026-05-16T00:35:18.285Z

### Getting Started


### Workspace
For Intelephense to work effectively it must have access to the definitions of the symbols used in your code. It does this by scanning the php files found in the workspace. Sometimes PHP files may have a non standard extension. It is important to associate these extensions with PHP using the `intelephense.files.associations` configuration option.

<details>
<summary>intelephense.files.associations</summary>

```json
{
    "type": "array",
    "default": [
        "*.php",
        "*.phtml"
    ],
    "description": "Configure glob patterns to make files available language server features. Inherits from files.associations.",
    "scope": "window"
}
```
</details>

You may have large files in your workspace that by default Intelephense will skip. You can configure the maximum file size with the `intelephense.files.maxSize` option.

<details>
<summary>intelephense.files.maxSize</summary>

```json
{
    "type": "number",
    "default": 1000000,
    "description": "Maximum file size in bytes.",
    "scope": "window"
}
```

</details>

There may be files you do not want to indexed by Intelephense. It is important in large projects to exclude unnecessary files to avoid polluting suggestion lists and degrading performance.

<details>
<summary>intelephense.files.exclude</summary>

```json
{
    "type": "array",
    "items": {
        "type": "string"
    },
    "default": [
        "**/.git/**",
        "**/.svn/**",
        "**/.hg/**",
        "**/CVS/**",
        "**/.DS_Store/**",
        "**/node_modules/**",
        "**/bower_components/**",
        "**/vendor/**/{Tests,tests}/**",
        "**/.history/**",
        "**/vendor/**/vendor/**"
    ],
    "description": "Configure glob patterns to exclude certain files and folders fro    all language server features. Inherits from files.exclude.",
    "scope": "resource"
}
```

</details>

### Environment
Sometimes symbol definitions are not in your workspace but are core PHP symbols or defined in an extension. For this reason Intelephense includes stub definitions for many of these. Extensions that are bundled with PHP are enabled by default. You can configure what other symbols are available in your environment with the `intelephense.stubs` option.

<details>
<summary>intelephense.stubs</summary

```json
{
    "type": "array",
    "items": {
        "type": "string",
        "enum": [
            "amqp",
            "apache",
            "apcu",
            "bcmath",
            "blackfire",
            "bz2",
            "calendar",
            "cassandra",
            "com_dotnet",
            "Core",
            "couchbase",
            "crypto",
            "ctype",
            "cubrid",
            "curl",
            "date",
            "dba",
            "decimal",
            "dom",
            "ds",
            "enchant",
            "Ev",
            "event",
            "exif",
            "fann",
            "FFI",
            "ffmpeg",
            "fileinfo",
            "filter",
            "fpm",
            "ftp",
            "gd",
            "gearman",
            "geoip",
            "geos",
            "gettext",
            "gmagick",
            "gmp",
            "gnupg",
            "grpc",
            "hash",
            "http",
            "ibm_db2",
            "iconv",
            "igbinary",
            "imagick",
            "imap",
            "inotify",
            "interbase",
            "intl",
            "json",
            "judy",
            "ldap",
            "leveldb",
            "libevent",
            "libsodium",
            "libxml",
            "lua",
            "lzf",
            "mailparse",
            "mapscript",
            "mbstring",
            "mcrypt",
            "memcache",
            "memcached",
            "meminfo",
            "meta",
            "ming",
            "mongo",
            "mongodb",
            "mosquitto-php",
            "mqseries",
            "msgpack",
            "mssql",
            "mysql",
            "mysql_xdevapi",
            "mysqli",
            "ncurses",
            "newrelic",
            "oauth",
            "oci8",
            "odbc",
            "openssl",
            "parallel",
            "Parle",
            "pcntl",
            "pcov",
            "pcre",
            "pdflib",
            "PDO",
            "pdo_ibm",
            "pdo_mysql",
            "pdo_pgsql",
            "pdo_sqlite",
            "pgsql",
            "Phar",
            "phpdbg",
            "posix",
            "pspell",
            "pthreads",
            "radius",
            "rar",
            "rdkafka",
            "readline",
            "recode",
            "redis",
            "Reflection",
            "regex",
            "rpminfo",
            "rrd",
            "SaxonC",
            "session",
            "shmop",
            "SimpleXML",
            "snmp",
            "soap",
            "sockets",
            "sodium",
            "solr",
            "SPL",
            "SplType",
            "SQLite",
            "sqlite3",
            "sqlsrv",
            "ssh2",
            "standard",
            "stats",
            "stomp",
            "suhosin",
            "superglobals",
            "svn",
            "sybase",
            "sync",
            "sysvmsg",
            "sysvsem",
            "sysvshm",
            "tidy",
            "tokenizer",
            "uopz",
            "uv",
            "v8js",
            "wddx",
            "win32service",
            "winbinder",
            "wincache",
            "wordpress",
            "xcache",
            "xdebug",
            "xhprof",
            "xml",
            "xmlreader",
            "xmlrpc",
            "xmlwriter",
            "xsl",
            "xxtea",
            "yaf",
            "yaml",
            "yar",
            "zend",
            "Zend OPcache",
            "ZendCache",
            "ZendDebugger",
            "ZendUtils",
            "zip",
            "zlib",
            "zmq",
            "zookeeper"
        ]
    },
    "default": [
        "apache",
        "bcmath",
        "bz2",
        "calendar",
        "com_dotnet",
        "Core",
        "ctype",
        "curl",
        "date",
        "dba",
        "dom",
        "enchant",
        "exif",
        "FFI",
        "fileinfo",
        "filter",
        "fpm",
        "ftp",
        "gd",
        "gettext",
        "gmp",
        "hash",
        "iconv",
        "imap",
        "intl",
        "json",
        "ldap",
        "libxml",
        "mbstring",
        "meta",
        "mysqli",
        "oci8",
        "odbc",
        "openssl",
        "pcntl",
        "pcre",
        "PDO",
        "pdo_ibm",
        "pdo_mysql",
        "pdo_pgsql",
        "pdo_sqlite",
        "pgsql",
        "Phar",
        "posix",
        "pspell",
        "readline",
        "Reflection",
        "session",
        "shmop",
        "SimpleXML",
        "snmp",
        "soap",
        "sockets",
        "sodium",
        "SPL",
        "sqlite3",
        "standard",
        "superglobals",
        "sysvmsg",
        "sysvsem",
        "sysvshm",
        "tidy",
        "tokenizer",
        "xml",
        "xmlreader",
        "xmlrpc",
        "xmlwriter",
        "xsl",
        "Zend OPcache",
        "zip",
        "zlib"
    ],
    "description": "Configure stub files for built in symbols and common extensions.The default setting includes PHP core and all bundled extensions.",
    "scope": "window"
}
```
</details>

Other configuration settings that allow you to further define the PHP environment include:

<details>
<summary>intelephense.environment.documentRoot</summary>

```json
{
    "type": "string",
    "description": "The directory of the entry point to the application (index.php).Defaults to the first workspace folder. Used for resolving script inclusion.",
    "scope": "window"
}
```
</details>

<details>
<summary>intelephense.environment.includePaths</summary>

```json
{
    "type": "array",
    "items": {
        "type": "string"
    },
    "description": "The include paths (as individual path items) as defined in theinclude_path ini setting. Used for resolving script inclusion.",
    "scope": "window"
}
```

</details>

<details>
<summary>intelephense.environment.phpVersion</summary>

```json
{
    "type": "string",
    "default": "7.4.0",
    "description": "A semver compatible string that represents the target PHP version.Used for providing version appropriate suggestions and diagnostics. PHP 5.3.0 andgreater supported.",
    "scope": "window"
}
```

</details>

<details>
<summary>intelephense.environment.shortOpenTag</summary>

```json
{
    "type": "boolean",
    "default": false,
    "description": "When enabled '<?' will be parsed as a PHP open tag. Defaults tofalse.",
    "scope": "window"
}
```

</details>

### Type Declarations and Annotations
You will get more out of Intelephense if you provide type declarations and/or type annotations. Where possible types will be inferred but there are places where it is difficult or impossible to determine the type. Class properties and function and method parameters are examples where this is very important. Providing type declarations and/or annotations may also improve performance as Intelephense does not need to dig through too much code to determine types. When a type cannot be determined for a property, variable, or parameter then it is assigned the `mixed` type.

```php
<?php
class MyClass
{
    public MyOtherClass $withTypeDeclaration;

    /** @var MyOtherClass **/
    public $withTypeAnnotation

    public function withTypeDeclarations(string $param): int { }

    /**
     * @param string $param
     * @return int
     */
    public function withTypeAnnotations($param) { }
}
```

Variables can be annotated with a type if necessary. The annotation immediately preceeding an assignment overrides the assigned type. Subsequent assignments may change the type again.

```php
<?php
/** @var callable $var */
$var = 'is_numeric'; //$var is callable instead of string
$var = 1; //$var is now an int

```

In addition to the standard PHPDoc type annotations Intelephense also supports generic type syntax for `iterable` and `ArrayAccess` types. For example:

* `Generator<KeyType, ElementType>`
* `ArrayAccess<string, ElementType>`
* `array<int, ElementType>`

Union (`TypeA|TypeB`) and intersection (`TypeA&TypeB`) types are supported. Where both a type declaration and a type annotation is provided then the resulting type will be the intersection of the two. Types will be reduced where possible using the following rules.

* `SuperType|SubType` => `SuperType`
* `SuperType&SubType` => `SubType`

Sometimes there may be type annotations in libraries or project files that do not accurately reflect the desired type. Intelephense offers compatibility settings to handle some common cases.

<details>
<summary>intelephense.compatibility.correctForBaseClassStaticUnionTypes</summary>

```json
{
    "type": "boolean",
    "default": true,
    "description": "Resolves `BaseClass|static` union types to `static` instead of `BaseClass`.",
    "scope": "window"
}
```

</details>

<details>
<summary>intelephense.compatibility.correctForArrayAccessArrayAndTraversableArrayUnionTypes</summary>

```json
{
    "type": "boolean",
    "default": true,
    "description": "Resolves `ArrayAccess` and `Traversable` implementations that are unionedwith a typed array to generic syntax. eg `ArrayAccessOrTraversable|ElementType[]` =>`ArrayAccessOrTraversable<mixed, ElementType>`.",
    "scope": "window"
}
```

</details>

You may also see several non standard types in hovers.

* `unset` - the type given to variables that are undefined or `unset()`.
* `never` - the type returned from a function that does not terminate normally (eg `die()`) or that represents an impossibility (added in PHP 8.1).

### Framework Support
Intelephense aims to support all frameworks but does not implement framework specific solutions. Some frameworks are coded in a way that make it difficult to analyse. This may be because of lack of type declarations/annotations; heavy use of `__get`, `__set`, `__call`, `__callStatic` magic methods; or dynamic generation of class aliases at runtime.

Packages can be found online that aim to workaround these issues by providing stubs of symbols to help static analysers like Intelephense understand the code.

* Laravel - [barryvdh/laravel-ide-helper](https://github.com/barryvdh/laravel-ide-helper)

---

## DOCUMENT: Intelephense: features
**Source:** https://raw.githubusercontent.com/bmewburn/intelephense-docs/master/features.md
**Ingested At:** 2026-05-16T00:35:18.317Z

### Features


### Workspace Symbols


### Document Symbols


### Go To Definition


### Completion


### Signature Help


### Hover


### Document Highlight


### Find All References


### Document and Range Formatting


### Rename -- [PREMIUM](https://intelephense.com)


### Code Folding -- [PREMIUM](https://intelephense.com)


### Find all Implementations -- [PREMIUM](https://intelephense.com)


### Go to Declaration -- [PREMIUM](https://intelephense.com)


### Go to Type Definition -- [PREMIUM](https://intelephense.com)


### Smart Selection -- [PREMIUM](https://intelephense.com)


### PHP Doc Block Generation -- [PREMIUM](https://intelephense.com)


---

## DOCUMENT: Intelephense: support
**Source:** https://raw.githubusercontent.com/bmewburn/intelephense-docs/master/support.md
**Ingested At:** 2026-05-16T00:35:18.347Z

### Overview
https://github.com/bmewburn/vscode-intelephense/issues

ben@intelephense.com

---

## DOCUMENT: software info by fk – software-online-review – Filip Keser
**Source:** https://software-online-review.com
**Ingested At:** 2026-05-16T00:35:18.116Z

### Introduction
[Skip to content](#content)
- ads – analitics – advertising
[ads – analitics – advertising](https://software-online-review.com/ads-analitics/)
- affiliate – partner – reseller
[affiliate – partner – reseller](https://software-online-review.com/affiliate-partner-reseller/)
- all about cookies
[all about cookies](https://software-online-review.com/all-about-cookies/)
- Amazon affiliate program
[Amazon affiliate program](https://software-online-review.com/amazon-affiliate-program/)
- Author.jpg
[Author.jpg](https://software-online-review.com/author-jpg/)
- Auto magazine
[Auto magazine](https://software-online-review.com/auto-magazine/)

### - BUY IT NOW – ESCROW – PROJECT SOR – DOMAIN WITH CONTENT
[BUY IT NOW – ESCROW – PROJECT SOR – DOMAIN WITH CONTENT](https://software-online-review.com/buy-it-now/)
- Companylink Business
[Companylink Business](https://software-online-review.com/companylink-business/)
- Cosmetic & parfumes
[Cosmetic & parfumes](https://software-online-review.com/cosmetic-parfumes/)
- Customer Management System Process Driver
[Customer Management System Process Driver](https://software-online-review.com/customer-management-system-process-driver/)
- design style
[design style](https://software-online-review.com/design-style/)
- draagster – India
[draagster – India](https://software-online-review.com/draagster-2/)
- E&N
[E&N](https://software-online-review.com/en/)
- Fintech bussines card example scheme links
[Fintech bussines card example scheme links](https://software-online-review.com/fintech-bussines-card/)
- gadget
[gadget](https://software-online-review.com/gadget/)
- Game zone
[Game zone](https://software-online-review.com/games/)
- Google search
[Google search](https://software-online-review.com/google/)
- google third party cookies – privacy sandbox – safari dont use third party … 2023
[google third party cookies – privacy sandbox – safari dont use third party … 2023](https://software-online-review.com/11249-2/)
- idea to make by fk
[idea to make by fk](https://software-online-review.com/idea-to-make/)
- Informatic magazine
[Informatic magazine](https://software-online-review.com/informatic-magazine/)
- Marketing
[Marketing](https://software-online-review.com/marketing/)
- Music page
[Music page](https://software-online-review.com/music-page/)
- NordVPN
[NordVPN](https://software-online-review.com/nordvpn/)
- notes
[notes](https://software-online-review.com/https-notepad-business-blog/)
- online news & content
[online news & content](https://software-online-review.com/online-news-content/)
- Pilot project
[Pilot project](https://software-online-review.com/pilot-project/)
- software-online-review
[software-online-review](https://software-online-review.com/software-online-review-2/)
- Startup online hiring Scheme links – online & google
[Startup online hiring Scheme links – online & google](https://software-online-review.com/startup-online-hiring-scheme-online/)
- Store
[Store](https://software-online-review.com/store/)
- Study – Courses online
[Study – Courses online](https://software-online-review.com/study-courses-online/)
- Unitedsports News
[Unitedsports News](https://software-online-review.com/unitedsports-news/)
- unofficial
[unofficial](https://software-online-review.com/unofficial-study-of-researchers-graduate-thesis-life-school-of-a-man-with-a-high-school-life-faculty-without-a-diploma-source-google/)
- us-cro-info-news
[us-cro-info-news](https://software-online-review.com/us-cro-info-news/)
- Venture Capital
[Venture Capital](https://software-online-review.com/venture-capital/)
- Web shop us croatia online
[Web shop us croatia online](https://software-online-review.com/web-shop-us-croatia-online/)
- Webshops
[Webshops](https://software-online-review.com/webshops/)
- WordPress links
[WordPress links](https://software-online-review.com/wordpress-links/)
- WordPress Read
[WordPress Read](https://software-online-review.com/wordpress-read/)
- WordPress Upgrade
[WordPress Upgrade](https://software-online-review.com/wordpress-upgrade/)

### software info by fk
[software info by fk](https://software-online-review.com/)
software-online-review – Filip Keser

[software online review](https://software-online-review.com/category/software-online-review/)

### Roadmap and business roadmap
[Roadmap and business roadmap](https://software-online-review.com/2025/11/01/roadmap-and-business-roadmap/)
[November 1, 2025November 1, 2025](https://software-online-review.com/2025/11/01/roadmap-and-business-roadmap/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
A roadmap is a strategic plan that defines a goal or desired outcome and includes the major steps or milestones needed to reach it. It also serves as a communication tool, a high-level document that helps articulate strategic thinking—the why—behind both the goal and the plan for getting there.

A business roadmap is a visual representation of your business strategy. It outlines the steps, goals, initiatives, and milestones needed to achieve your long-term plans. A business roadmap is also more tactical, focusing on how you will reach your objectives.

Eight Bukets – Challenge

Six – Create Value – Capture Value

I’m giving you the map, now you must walk the path

https://youtu.be/qllWAheHkms?si=fCkbOSRuRO5kZ0ol

[https://youtu.be/qllWAheHkms?si=fCkbOSRuRO5kZ0ol](https://youtu.be/qllWAheHkms?si=fCkbOSRuRO5kZ0ol)
The 80 – 20 Rule

https://www.investopedia.com/terms/1/80-20-rule.asp

[https://www.investopedia.com/terms/1/80-20-rule.asp](https://www.investopedia.com/terms/1/80-20-rule.asp)
[software online review](https://software-online-review.com/category/software-online-review/)

### Nvidia Dgx Spark
[Nvidia Dgx Spark](https://software-online-review.com/2025/10/25/nvidia-dgx-spark/)
[October 25, 2025October 25, 2025](https://software-online-review.com/2025/10/25/nvidia-dgx-spark/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/

[https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/)
https://marketplace.nvidia.com/en-us/developer/dgx-spark/

[https://marketplace.nvidia.com/en-us/developer/dgx-spark/](https://marketplace.nvidia.com/en-us/developer/dgx-spark/)
https://www.nvidia.com/en-us/

[https://www.nvidia.com/en-us/](https://www.nvidia.com/en-us/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Chromium
[Chromium](https://software-online-review.com/2025/10/24/chromium/)
[October 24, 2025October 25, 2025](https://software-online-review.com/2025/10/24/chromium/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://en.wikipedia.org/wiki/Chromium_(web_browser)

[https://en.wikipedia.org/wiki/Chromium_(web_browser)](https://en.wikipedia.org/wiki/Chromium_(web_browser))

### The One Investment Rule
https://youtu.be/IBD_AdM3WNI?si=xORYvpzXfwyYxO-a

[https://youtu.be/IBD_AdM3WNI?si=xORYvpzXfwyYxO-a](https://youtu.be/IBD_AdM3WNI?si=xORYvpzXfwyYxO-a)
Chromium org

https://www.chromium.org/chromium-projects/

[https://www.chromium.org/chromium-projects/](https://www.chromium.org/chromium-projects/)
browsing history

https://interestingengineering.com/culture/chatgpt-to-absorb-users-life-history

[https://interestingengineering.com/culture/chatgpt-to-absorb-users-life-history](https://interestingengineering.com/culture/chatgpt-to-absorb-users-life-history)
ghat gpt – gemini – missing personality

https://www.tomsguide.com/ai/i-switched-from-chatgpt-to-gemini-for-one-week-and-heres-why-im-going-back-to-chatgpt

[https://www.tomsguide.com/ai/i-switched-from-chatgpt-to-gemini-for-one-week-and-heres-why-im-going-back-to-chatgpt](https://www.tomsguide.com/ai/i-switched-from-chatgpt-to-gemini-for-one-week-and-heres-why-im-going-back-to-chatgpt)
Chromium base

https://www.pcmag.com/comparisons/chatgpt-vs-gemini-which-ai-chatbot-is-actually-smarter

[https://www.pcmag.com/comparisons/chatgpt-vs-gemini-which-ai-chatbot-is-actually-smarter](https://www.pcmag.com/comparisons/chatgpt-vs-gemini-which-ai-chatbot-is-actually-smarter)

### Gemini
https://gemini.google.com/app/download

[https://gemini.google.com/app/download](https://gemini.google.com/app/download)
https://gemini.google/subscriptions/

[https://gemini.google/subscriptions/](https://gemini.google/subscriptions/)
Chat Gpt – Open AI

https://chatgpt.com/

[https://chatgpt.com/](https://chatgpt.com/)
https://openai.com/

[https://openai.com/](https://openai.com/)
https://en.wikipedia.org/wiki/OpenAI

[https://en.wikipedia.org/wiki/OpenAI](https://en.wikipedia.org/wiki/OpenAI)
[software online review](https://software-online-review.com/category/software-online-review/)

### Project Sor
[Project Sor](https://software-online-review.com/2024/11/25/project-sor/)
[November 25, 2024November 25, 2024](https://software-online-review.com/2024/11/25/project-sor/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
[marketing](https://software-online-review.com/category/technology/marketing/)

### Google marketing
[Google marketing](https://software-online-review.com/2023/12/07/google-marketing/)
[December 7, 2023June 2, 2024](https://software-online-review.com/2023/12/07/google-marketing/)
[Filip Keser](https://software-online-review.com/author/fkeser/)

### Subscribe to continue reading
Subscribe to get access to the rest of this post and other subscriber-only content.

Type your email…

### Subscribe
[Already a subscriber?](https://wordpress.com/log-in/link?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fsoftware-online-review.com%252F)
[software online review](https://software-online-review.com/category/software-online-review/)

### chronicle
[chronicle](https://software-online-review.com/2023/10/17/chronicle/)
[October 17, 2023November 30, 2023](https://software-online-review.com/2023/10/17/chronicle/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://chronicle.security/

[https://chronicle.security/](https://chronicle.security/)
https://cloud.google.com/chronicle-soar

[https://cloud.google.com/chronicle-soar](https://cloud.google.com/chronicle-soar)
Chronicle ingests your own data into a private container at petabyte scale with 1-year retention

https://chronicle.security/platform/

[https://chronicle.security/platform/](https://chronicle.security/platform/)
https://www.partneradvantage.goog/

[https://www.partneradvantage.goog/](https://www.partneradvantage.goog/)
https://www.group-ib.com/

[https://www.group-ib.com/](https://www.group-ib.com/)
https://www.mandiant.com/

[https://www.mandiant.com/](https://www.mandiant.com/)
https://cloud.google.com/partners

[https://cloud.google.com/partners](https://cloud.google.com/partners)
https://inthecloud.withgoogle.com/pck-page/register.html

[https://inthecloud.withgoogle.com/pck-page/register.html](https://inthecloud.withgoogle.com/pck-page/register.html)
https://www.partneradvantage.goog/GCPPRM/s/memberregistration

[https://www.partneradvantage.goog/GCPPRM/s/memberregistration](https://www.partneradvantage.goog/GCPPRM/s/memberregistration)
https://cloud.google.com/partners/become-a-partner/

[https://cloud.google.com/partners/become-a-partner/](https://cloud.google.com/partners/become-a-partner/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Security key
[Security key](https://software-online-review.com/2023/04/24/security-key/)
[April 24, 2023November 30, 2023](https://software-online-review.com/2023/04/24/security-key/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://webauthn.io/

[https://webauthn.io/](https://webauthn.io/)
https://store.google.com/us/product/titan_security_key

[https://store.google.com/us/product/titan_security_key](https://store.google.com/us/product/titan_security_key)
https://www.ftsafe.com/Products/FIDO

[https://www.ftsafe.com/Products/FIDO](https://www.ftsafe.com/Products/FIDO)
https://www.ftsafe.com/

[https://www.ftsafe.com/](https://www.ftsafe.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### search google
[search google](https://software-online-review.com/2022/08/25/search-google/)
[August 25, 2022November 30, 2023](https://software-online-review.com/2022/08/25/search-google/)
[Filip Keser](https://software-online-review.com/author/fkeser/)

### BUY IT NOW – ESCROW – PROJECT SOR – DOMAIN WITH CONTENT
Buy it Now

[Buy it Now](https://secureapi.escrow.com/api/ecart/#/StartTransactionLanding?Token=76CA3FAF-7B47-40CB-BF47-F01D79C6CF2C)
https://www.google.com/

[https://www.google.com/](https://www.google.com/)
https://search.google.com/search-console/about

[https://search.google.com/search-console/about](https://search.google.com/search-console/about)
https://developers.google.com/search

[https://developers.google.com/search](https://developers.google.com/search)
[software online review](https://software-online-review.com/category/software-online-review/)

### software-online-review
[software-online-review](https://software-online-review.com/2022/07/22/software-online-review/)
[July 22, 2022October 23, 2024](https://software-online-review.com/2022/07/22/software-online-review/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
NEED CONSTRUCTION WORKER – https://software-online-review.com/startup-online-hiring-scheme-online/ARCHITECTS & SOFTWARE DEVELOPERS

[https://software-online-review.com/startup-online-hiring-scheme-online/](https://software-online-review.com/startup-online-hiring-scheme-online/)
https://www.delawareinc.com/

[https://www.delawareinc.com/](https://www.delawareinc.com/)
[https://www.sba.gov/](https://www.sba.gov/)
https://eqvista.com/

[https://eqvista.com/](https://eqvista.com/)
https://www.ycombinator.com/library/Ek-stages-of-startups

[https://www.ycombinator.com/library/Ek-stages-of-startups](https://www.ycombinator.com/library/Ek-stages-of-startups)
https://www.investopedia.com/articles/personal-finance/011216/llc-vs-incorporation-inc-which-should-i-choose.asp

[https://www.investopedia.com/articles/personal-finance/011216/llc-vs-incorporation-inc-which-should-i-choose.asp](https://www.investopedia.com/articles/personal-finance/011216/llc-vs-incorporation-inc-which-should-i-choose.asp)
https://www.investopedia.com/terms/i/incorporate.asp

[https://www.investopedia.com/terms/i/incorporate.asp](https://www.investopedia.com/terms/i/incorporate.asp)
https://www.investopedia.com/terms/a/acquisition.asp

[https://www.investopedia.com/terms/a/acquisition.asp](https://www.investopedia.com/terms/a/acquisition.asp)
https://system1.com/

[https://system1.com/](https://system1.com/)
https://www.semrush.com/

[https://www.semrush.com/](https://www.semrush.com/)
https://www.theverge.com/2019/12/4/20994361/google-alphabet-larry-page-sergey-brin-sundar-pichai-co-founders-ceo-timeline

[https://www.theverge.com/2019/12/4/20994361/google-alphabet-larry-page-sergey-brin-sundar-pichai-co-founders-ceo-timeline](https://www.theverge.com/2019/12/4/20994361/google-alphabet-larry-page-sergey-brin-sundar-pichai-co-founders-ceo-timeline)
https://www.britannica.com/topic/Google-Inc

[https://www.britannica.com/topic/Google-Inc](https://www.britannica.com/topic/Google-Inc)
https://www.cnbc.com/2018/09/04/8-surprising-facts-you-might-not-know-about-googles-early-days.html

[https://www.cnbc.com/2018/09/04/8-surprising-facts-you-might-not-know-about-googles-early-days.html](https://www.cnbc.com/2018/09/04/8-surprising-facts-you-might-not-know-about-googles-early-days.html)
https://en.wikipedia.org/wiki/PageRank

[https://en.wikipedia.org/wiki/PageRank](https://en.wikipedia.org/wiki/PageRank)
https://www.google.com/search/howsearchworks/

[https://www.google.com/search/howsearchworks/](https://www.google.com/search/howsearchworks/)
https://www.google.com/search/howsearchworks/our-approach/ads-on-search/

[https://www.google.com/search/howsearchworks/our-approach/ads-on-search/](https://www.google.com/search/howsearchworks/our-approach/ads-on-search/)
https://developers.google.com/search

[https://developers.google.com/search](https://developers.google.com/search)
https://pagespeed.web.dev/

[https://pagespeed.web.dev/](https://pagespeed.web.dev/)
https://www.catchpoint.com/

[https://www.catchpoint.com/](https://www.catchpoint.com/)
https://search.google.com/search-console/about

[https://search.google.com/search-console/about](https://search.google.com/search-console/about)
[WordPress VIP](https://wpvip.com/)
[Site Kit by Google – Analytics, Search Console, AdSense, Speed](https://wordpress.org/plugins/google-site-kit/)
https://sitekit.withgoogle.com/

[https://sitekit.withgoogle.com/](https://sitekit.withgoogle.com/)
https://www.investopedia.com/articles/markets/011516/top-5-google-shareholders-goog.asp

[https://www.investopedia.com/articles/markets/011516/top-5-google-shareholders-goog.asp](https://www.investopedia.com/articles/markets/011516/top-5-google-shareholders-goog.asp)
https://www.nasdaq.com/market-activity/stocks/goog

[https://www.nasdaq.com/market-activity/stocks/goog](https://www.nasdaq.com/market-activity/stocks/goog)
https://startup.google.com/programs/accelerator/

[https://startup.google.com/programs/accelerator/](https://startup.google.com/programs/accelerator/)
https://developers.google.com/community/accelerators

[https://developers.google.com/community/accelerators](https://developers.google.com/community/accelerators)
https://www.jetbrains.com/idea/

[https://www.jetbrains.com/idea/](https://www.jetbrains.com/idea/)
https://www.jetbrains.com

[https://www.jetbrains.com](https://www.jetbrains.com)
https://neuechair.com/

[https://neuechair.com/](https://neuechair.com/)
[Neue™](https://secretlab.eu/collections/neue)
https://www.google.com/

[https://www.google.com/](https://www.google.com/)
The 5 stages of a startup

- Solving the problem. Running a successful business is all about producing something that solves a problem. …
- 2. Development. This is where it starts getting serious. …
- Entering the market. …
- Scaling. …
- Maturity.
Buy it Now

[Buy it Now](https://secureapi.escrow.com/api/ecart/#/StartTransactionLanding?Token=76CA3FAF-7B47-40CB-BF47-F01D79C6CF2C)
https://sedo.com/us/

[https://sedo.com/us/](https://sedo.com/us/)
https://sedo.com/search/?keyword=software-online-review.com

[https://sedo.com/search/?keyword=software-online-review.com](https://sedo.com/search/?keyword=software-online-review.com)
[Trustpilot](https://www.trustpilot.com/review/software-online-review.com)
https://www.trustpilot.com/review/software-online-review.com

[https://www.trustpilot.com/review/software-online-review.com](https://www.trustpilot.com/review/software-online-review.com)

### Uncut Diamond
This article breaks down everything you need to know about uncut diamonds and how you can make a smart investment.

Filling in some gaps in your jewellery knowledge or trying to discover some untold secrets in the jewellery business? Uncut diamonds are not something that are often talked about. This article breaks down everything you need to know about uncut diamonds and how you can make a smart investment when picking out gorgeous stone jewellery.

### Uncut Diamond Jewellery explained?
An uncut diamond, as suggested by the name, is a diamond in its most natural form. Prior to any shaping to enhance proportion, symmetry and polish involved in diamond cutting, an uncut diamond is a raw diamond that is completely virgin and free from human manipulation.

### What is an uncut Diamond worth and why are Diamonds cut?
Apart from their quirky edge, there is not a whole lot of value in purchasing raw diamonds. Uncut diamonds are typically worth less than traditionally cut diamonds as their unpolished, rough edges hinder how well light is refracted. This reduces their sparkle and brilliance, thus reducing their market value.

### What does a raw uncut Diamond look like?
An uncut diamond is often bumpy and dull with no real structure. An acquired taste, uncut diamond rings provide a uniqueness and level of beauty some like to hold with others even looking for a rough diamond ring to mark their love.

### Diamond Cut Breakdown
To create beautiful diamonds that are worth thousands, diamond cutters have the difficult job of trying to create finished products which align in proportion, symmetry and polish. Make no mistake, while this is easy to decide in theory, cutting diamonds is a challenge where compromises often have to be made. Compromising factors such as diamond weight, to create the right proportions and symmetry, or proportions and symmetry to avoid cutting further diamond and reducing weight.

In a similar way to natural diamonds, poorly cut diamonds can also refract light badly, resulting in little to no sparkle and less spread for your carat weight. To identify how you can be savvy and well informed when choosing your own diamond jewellery, here is everything you need to know about cuts.

Developed in the 1940’s to 1950’s by the Gemological Institute of America (GIA), cut grades were developed to allow independent labs to identify a diamond’s clarity, colour and structure. A prime example of a predetermined cut grade is a brilliant cut diamond which will have 57 or 58 facets accurately cut and defined. While miniature, this provides a system to govern how well a diamond will sparkle.

While they offer a significant discount in price, poorly cut diamonds lack luster and you will be paying for a diamond without any sparkle. To ensure that you have an effective diamond that is worthwhile, we always suggest purchasing a diamond with an “excellent” to “good” cut. However, if you are still interested in purchasing a diamond of a lower cut, we suggest taking a look in person under various lighting conditions to avoid any disappointment.

Website, other related websites and blogs created as a scratch base pilot project for merging and evolving to something better and highly valuable.

[software online review](https://software-online-review.com/category/software-online-review/)

### Client Portal
[Client Portal](https://software-online-review.com/2022/03/22/client-portal/)
[March 22, 2022March 25, 2023](https://software-online-review.com/2022/03/22/client-portal/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
[https://atomic-temporary-178675373.wpcomstaging.com/clients/](https://atomic-temporary-178675373.wpcomstaging.com/clients/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Harvard Business Review – Ideas and Advice for Leaders
[Harvard Business Review – Ideas and Advice for Leaders](https://software-online-review.com/2022/03/21/harvard-business-review-ideas-and-advice-for-leaders-2/)
[March 21, 2022March 20, 2023](https://software-online-review.com/2022/03/21/harvard-business-review-ideas-and-advice-for-leaders-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://hbr.org/

[https://hbr.org/](https://hbr.org/)
[management](https://software-online-review.com/category/management/)
[software](https://software-online-review.com/category/software/)
[software online review](https://software-online-review.com/category/software-online-review/)
[technology](https://software-online-review.com/category/technology/)
[workflow](https://software-online-review.com/category/workflow/)

### Perfect Strangers
[Perfect Strangers](https://software-online-review.com/2022/02/24/perfect-strangers/)
[February 24, 2022February 25, 2022](https://software-online-review.com/2022/02/24/perfect-strangers/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Small Business Administration
[Small Business Administration](https://software-online-review.com/2021/05/14/small-business-administration/)
[May 14, 2021February 27, 2025](https://software-online-review.com/2021/05/14/small-business-administration/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.sba.gov/

[https://www.sba.gov/](https://www.sba.gov/)
https://www.sba.gov/funding-programs/loans/7a-loans

[https://www.sba.gov/funding-programs/loans/7a-loans](https://www.sba.gov/funding-programs/loans/7a-loans)
https://www.sba.gov/funding-programs/loans/

[https://www.sba.gov/funding-programs/loans/](https://www.sba.gov/funding-programs/loans/)
https://www.sba.gov/funding-programs/

[https://www.sba.gov/funding-programs/](https://www.sba.gov/funding-programs/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Chromium – Base
[Chromium – Base](https://software-online-review.com/2026/02/20/chromium-base/)
[February 20, 2026February 20, 2026](https://software-online-review.com/2026/02/20/chromium-base/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
It’s true—Chromium has become the “engine” powering approximately 80% of the global browser market. While initiated by Google, it is an open-source project, allowing other companies to skip the massive cost of developing their own rendering engines and focus instead on unique features. StatCounter Global Stats +5

Browsers Built on Chromium:

Beyond Google Chrome, prominent examples include:

[Google Chrome](https://www.google.com/chrome/)
- Microsoft Edge: Switched to Chromium in 2020 for better web compatibility and extension support.
- Brave: Focuses on privacy by automatically blocking ads and trackers.
- Opera & Opera GX: Some of the earliest adopters after abandoning their custom “Presto” engine.
- Vivaldi: Aimed at power users with extreme interface customization.
- Samsung Internet: The dominant browser for Samsung mobile devices.
- Arc: A modern browser that rethinks tab management and user experience. Efficient App +6
The Major Exceptions (Non-Chromium):

Only two major players still maintain their own independent engines:

- Mozilla Firefox: Uses its own Gecko engine.
- Apple Safari: Uses the WebKit engine. Interestingly, Chromium originally started as a fork of WebKit before they split into separate projects. Reddit +3
Why the Shift to Chromium?

The transition is driven by security, speed (specifically the V8 JavaScript engine), and a massive extension ecosystem. Maintaining a modern engine is so complex that even giants like Microsoft found it more efficient to adopt the Chromium base to ensure perfect website compatibility. Sahi Pro +3

1. Privacy Differences (Brave vs. Vivaldi vs. Chrome)

While they are all built on Chromium, each browser handles your data differently:

- Google Chrome: The least private. It integrates deep telemetry with your Google account and uses your browsing history for targeted advertising.
- Brave: A “hardcore” approach to privacy. It blocks ads, trackers, and fingerprinting directly in the engine by default. It is also fully open-source.
[directly in the engine](https://brave.com/compare/chrome-vs-brave/)
- Vivaldi: Focused on user control. It offers built-in blockers and granular permissions for every site. Unlike Brave, Vivaldi’s interface (UI) is not open-source, as noted in PCMag reviews.
[PCMag reviews](https://www.pcmag.com/picks/stop-trackers-dead-the-best-private-browsers)
- Ungoogled Chromium: For maximalists—this is Chromium with every link to Google’s servers manually stripped out, though it requires manual updates.
[manually stripped out](https://bugbug.io/blog/software-testing/chrome-vs-chromium/)
2. The Monopoly Problem and Web Standards

Since Google controls Chromium’s development, it effectively sets the rules for the entire internet:

- Dictating Standards: If Google introduces a new feature in Chromium (e.g., Privacy Sandbox), it overnight becomes the standard that web developers must follow. This makes it harder for Firefox (Gecko engine) to survive, as developers often optimize sites only for Chromium.
[Privacy Sandbox](https://www.reddit.com/r/browsers/comments/1is89og/why_is_chromium_usually_considered_bad_for/)
[only for Chromium](https://medium.com/@lowharris15/master-of-the-web-how-google-rules-the-internet-with-chromium-65c9e10bd7dd)
- Manifest V3: Google recently changed how extensions work (Manifest V3), which complicates the effectiveness of traditional ad blockers. While Brave and Vivaldi strive to maintain old functionality, they are ultimately limited by what Google allows in the base code.
[complicates the effectiveness of traditional ad blockers](https://dev.to/kenbellows/chromium-and-the-browser-monoculture-problem-420n)
- Antitrust Battles: Due to this dominance, the U.S. Department of Justice (DOJ) attempted to force Google to sell Chrome. However, according to rulings from September 2025, Google will not have to sell the browser but must share search data with competitors.
[sell Chrome](https://www.bbc.com/news/articles/cp8zdrenm1zo)
[will not have to sell the browser](https://www.theguardian.com/technology/2025/sep/02/google-chrome-monopoly-ruling)
Conclusion: Which one to use?

If you want to escape Google’s influence, Firefox is the only true alternative with an independent engine. If you want Chromium’s speed but with privacy, Brave or the Mullvad Browser are the top choices for 2026.

https://www.chromium.org/getting-involved/download-chromium/

[https://www.chromium.org/getting-involved/download-chromium/](https://www.chromium.org/getting-involved/download-chromium/)
https://developer.apple.com/safari/resources/

[https://developer.apple.com/safari/resources/](https://developer.apple.com/safari/resources/)
https://chromium.woolyss.com/download/

[https://chromium.woolyss.com/download/](https://chromium.woolyss.com/download/)
https://download-chromium.appspot.com/

[https://download-chromium.appspot.com/](https://download-chromium.appspot.com/)
https://webkit.org/downloads

[https://webkit.org/downloads](https://webkit.org/downloads)
https://www.google.com/chrome/canary/

[https://www.google.com/chrome/canary/](https://www.google.com/chrome/canary/)
https://www.google.com/chrome/dev/

[https://www.google.com/chrome/dev/](https://www.google.com/chrome/dev/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Schema
[Schema](https://software-online-review.com/2026/02/17/schema/)
[February 17, 2026](https://software-online-review.com/2026/02/17/schema/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
Schema.org is a collaborative, community-driven initiative that provides a standardized “language” or dictionary of structured data tags to help search engines understand the content of web pages.

[community-driven initiative](https://schema.org/)
[structured data tags](https://schema.org/docs/schemas.html)
Here is exactly what it does and why it matters:

- Clarifies Content Meaning: While standard HTML tells a browser how to display text (e.g., as a heading), Schema tags tell search engines what that text is—distinguishing, for instance, between a movie title, a person’s name, or a product’s price.
- Powers Rich Snippets: By using these tags, your page can appear in search results with enhanced visual features like review stars, recipe images, or price listings, which often lead to higher click-through rates.
[click-through rates](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- Universal Industry Standard: It was founded and is maintained by major search engines, including Google, Microsoft (Bing), Yahoo, and Yandex, ensuring that all major crawlers recognize the same set of definitions.
- Broad Versatility: The vocabulary covers thousands of “types” including local businesses, articles, events, recipes, and products, helping search engines categorize almost any kind of information.
In practice, this is typically implemented using the JSON-LD format, which Google recommends as the most efficient way to add these metadata “labels” to your site’s code.

[JSON-LD format](https://schema.org/docs/gs.html)
https://schema.org/

[https://schema.org/](https://schema.org/)
https://validator.schema.org/

[https://validator.schema.org/](https://validator.schema.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Google AI
[Google AI](https://software-online-review.com/2025/12/18/google-ai/)
[December 18, 2025December 18, 2025](https://software-online-review.com/2025/12/18/google-ai/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://one.google.com/

[https://one.google.com/](https://one.google.com/about/google-ai-plans/)
https://one.google.com/about/

[https://one.google.com/about/](https://one.google.com/about/google-ai-plans/)
https://one.google.com/about/google-ai-plans/

[https://one.google.com/about/google-ai-plans/](https://one.google.com/about/google-ai-plans/)
https://gemini.google.com/

[https://gemini.google.com/](https://gemini.google.com/)
Gemini 3 Pro is Google’s most advanced AI model. It is designed to handle complex tasks that require advanced reasoning and understanding of different types of data. It is currently available in preview for developers and through the Google AI Pro plan.

Key features and capabilities:

- Complex tasks: Gemini 3 Pro is optimized for complex tasks that require broad general knowledge and advanced reasoning across various data types, such as text, images, and video.
- Creative generation: The model excels at creative writing and developing complex, multifaceted concepts.
- Advanced reasoning: It is considered the most intelligent Google model to date, with improved logical reasoning, analysis, and coding capabilities.
- Research assistance: It assists users in summarizing hours of work into minutes by providing detailed reports on topics by analyzing hundreds of web pages in real-time.
- Multimodality: It has advanced visual and spatial reasoning capabilities (such as the Gemini 3 Pro Image model).
Availability:

Gemini 3 Pro is currently in preview and is available through:

- Gemini API: Developers can access the model through the Google AI Studio and Vertex AI platforms to build applications.
[Google AI Studio](https://aistudio.google.com/)
- Google AI Pro subscription: Users who subscribe to the Google AI Pro plan get extended access to Gemini 3 Pro features, including the “Deep Research” feature.
The model was launched in November 2025. Demand was so high that Google had to temporarily adjust the system to ensure availability. Pricing is calculated per million tokens, and details are available on the API pricing page.

https://jules.google/

[https://jules.google/](https://jules.google/)
Jules is Google’s autonomous, asynchronous AI coding agent designed to help software developers automate complex tasks like fixing bugs, writing tests, and implementing new features.

Unlike traditional “co-pilots” that suggest code as you type, Jules acts like an independent collaborator that clones your codebase into a secure virtual machine (VM) to perform work in the background.

Key Capabilities and Features (2025 Updates)

- Autonomous Workflow: Tasks are submitted via prompt, and Jules plans, executes, and verifies the changes independently, eventually opening a pull request.
- Asynchronous Development: Developers can assign tasks to Jules and continue working on other projects while it runs in a cloud environment.
- Gemini-Powered Intelligence: As of late 2025, Jules utilizes advanced models like Gemini 2.5 Pro and has been updated with integrations for Gemini 3 for improved reasoning and transparency.
- Critic-Augmented Generation: A “critic” feature provides an adversarial review of Jules’ proposed changes before completion to ensure high code quality.
- Proactive Assistance: A new Suggested Tasks feature automatically scans code to propose improvements or schedule routine updates without being prompted.
- Audio Changelogs: It can generate audible summaries of recent commits to help developers catch up on project history.
How to Use Jules

- Web Interface: You can sign in and manage repositories at jules.google.com.
- Command Line (CLI): Use Jules Tools to interact with the agent directly from your terminal, allowing for parallel task runs and local diff viewing.
- Jules API: Developers can programmatically integrate Jules into custom workflows, CI/CD pipelines, or tools like Slack and Linear.
- GitHub Integration: Tasks can be assigned directly by adding a jules label to an issue in a connected GitHub repository.
Pricing and Availability

Jules is currently in Public Beta. It is available globally where Gemini is supported and offers structured tiers:

- Free Tier: Accessible to all users for basic exploration.
- Paid Tiers: Higher usage limits are available via Google AI Pro and Ultra subscriptions.
https://antigravity.google/

[https://antigravity.google/](https://antigravity.google/)
In 2025, “Google Antigravity” primarily refers to a professional software development platform, though it can also refer to a classic search engine Easter egg.

1. Google Antigravity (Agentic IDE)

Launched on November 18, 2025, Google Antigravity is an “agent-first” AI-powered Integrated Development Environment (IDE). Antigravity uses autonomous agents to plan, execute, and verify entire development tasks. Standard coding assistants suggest code snippets.

- Key Components: Agent Manager: This is an interface for orchestrating multiple background agents. The agents work across different workspaces. Editor View: This is a fully-featured IDE (forked from Visual Studio Code) for coding with AI-powered tab completion and inline commands. Antigravity Browser: This browser allows agents to navigate, test, and verify web applications.
- Agent Manager: This is an interface for orchestrating multiple background agents. The agents work across different workspaces.
- Editor View: This is a fully-featured IDE (forked from Visual Studio Code) for coding with AI-powered tab completion and inline commands.
- Antigravity Browser: This browser allows agents to navigate, test, and verify web applications.
- Core Features: Artifacts: Agents produce deliverables like implementation plans, code diffs, and browser recordings. These allow for easy verification. Model Optionality: It is powered primarily by Gemini 3, but also supports other models. These include Anthropic’s Claude Sonnet 4.5 and OpenAI’s GPT-OSS. Feedback Loops: Users can leave comments directly on artifacts to guide agent iteration. This is similar to “Google Docs-style” comments.
- Artifacts: Agents produce deliverables like implementation plans, code diffs, and browser recordings. These allow for easy verification.
- Model Optionality: It is powered primarily by Gemini 3, but also supports other models. These include Anthropic’s Claude Sonnet 4.5 and OpenAI’s GPT-OSS.
- Feedback Loops: Users can leave comments directly on artifacts to guide agent iteration. This is similar to “Google Docs-style” comments.
- Availability: It is currently in Public Preview for individual users with personal Gmail accounts. There is no charge. Higher rate limits are available for Google AI Pro and Ultra subscribers.
2. Google Antigravity (Easter Egg)

This web trick mimics the lack of gravity on the Google search page. It is often hosted by third-party sites like Mr. Doob.

- How to trigger: Searching “Google Gravity” or “Google Antigravity” and clicking “I’m Feeling Lucky” typically causes the search bar and buttons to fall to the bottom of the screen or float around.
- Interaction: Users can click and “throw” the various page elements across the screen.
google antigravity vs google jules

In 2025, Google offers two distinct agentic coding tools:

Antigravity and Jules. Both use Gemini 3 models for coding automation, but they differ in their environment and interaction style.

Quick Comparison (2025)

Google Antigravity: The AI-First IDE

Launched in November 2025, Antigravity is an “agent-first” development platform designed as a direct competitor to Cursor.

- Key Strength: Orchestration. It allows multiple agent threads to run simultaneously, such as one agent refactoring a file while another writes unit tests.
- Browser Control: It integrates Chrome, allowing agents to “see” rendered HTML, click buttons, and run front-end tests autonomously.
- Status: Currently in public preview; it supports Gemini 3 Pro and Claude 3.5 models.
Google Jules: The Asynchronous Agent

Jules is a specialist “subcontractor” that handles bounded tasks in the background.

- Key Strength: Autonomy. Jules runs in a secure cloud environment (VM), meaning it can work on a task for hours without requiring the user’s session to stay active.
- GitHub Focused: It is primarily used to open branches, fix GitHub issues, and submit pull requests automatically.
- Availability: Now out of beta and available via Jules.google or as a VS Code extension.
[Jules.google](https://jules.google/)
Pricing & Access

Both tools are part of the Google AI Pro/Ultra plans (typically bundled with Google One subscriptions):

[Google AI Pro/Ultra plans](https://one.google.com/about/google-ai-plans/)
- Jules: Offers a free tier; paid tiers provide higher concurrency (e.g., 15 tasks at once).
- Antigravity: Available for free during its initial launch period, with premium rate limits tied to the Google AI Pro plan.
https://geminicli.com/

[https://geminicli.com/](https://geminicli.com/)
https://codeassist.google/

[https://codeassist.google/](https://codeassist.google/)
https://developer.android.com/studio

[https://developer.android.com/studio](https://developer.android.com/studio)
[Google](https://software-online-review.com/category/google/)
[management](https://software-online-review.com/category/management/)
[marketing](https://software-online-review.com/category/technology/marketing/)
[platform](https://software-online-review.com/category/platform/)
[software](https://software-online-review.com/category/software/)
[software online review](https://software-online-review.com/category/software-online-review/)
[technology](https://software-online-review.com/category/technology/)

### deepmind.google
[deepmind.google](https://software-online-review.com/2025/12/02/deepmind-google/)
[December 2, 2025December 14, 2025](https://software-online-review.com/2025/12/02/deepmind-google/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://deepmind.google/models/gemini/pro/

[https://deepmind.google/models/gemini/pro/](https://deepmind.google/models/gemini/pro/)
https://deepmind.google/models

[https://deepmind.google/models](https://deepmind.google/models)
https://deepmind.google

[https://deepmind.google](https://deepmind.google)
https://aistudio.google.com/

[https://aistudio.google.com/](https://aistudio.google.com/)
https://gemini.google.com/

[https://gemini.google.com/](https://gemini.google.com/)
https://jules.google.com/

[https://jules.google.com/](https://jules.google.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Gemini & AI Pro
[Gemini & AI Pro](https://software-online-review.com/2025/11/16/gemini-ai-pro/)
[November 16, 2025](https://software-online-review.com/2025/11/16/gemini-ai-pro/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://one.google.com/ai

[https://one.google.com/ai](https://one.google.com/ai)
https://one.google.com/about/

[https://one.google.com/about/](https://one.google.com/about/)
[software online review](https://software-online-review.com/category/software-online-review/)

### topic – top
[topic – top](https://software-online-review.com/2025/10/22/topic-top/)
[October 22, 2025](https://software-online-review.com/2025/10/22/topic-top/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.financialexpress.com/world-news/us-news/googles-ex-ceonbsperic-schmidtnbspsued-for-abuse-stalking-who-is-michelle-ritternbspnbsp/4016867/

[https://www.financialexpress.com/world-news/us-news/googles-ex-ceonbsperic-schmidtnbspsued-for-abuse-stalking-who-is-michelle-ritternbspnbsp/4016867/](https://www.financialexpress.com/world-news/us-news/googles-ex-ceonbsperic-schmidtnbspsued-for-abuse-stalking-who-is-michelle-ritternbspnbsp/4016867/)
https://nypost.com/2025/10/20/business/eric-schmidts-ex-mistress-31-sues-former-google-ceo-70-over-alleged-stalking-abuse-and-digital-surveillance/

[https://nypost.com/2025/10/20/business/eric-schmidts-ex-mistress-31-sues-former-google-ceo-70-over-alleged-stalking-abuse-and-digital-surveillance/](https://nypost.com/2025/10/20/business/eric-schmidts-ex-mistress-31-sues-former-google-ceo-70-over-alleged-stalking-abuse-and-digital-surveillance/)
https://torontosun.com/news/world/ex-google-ceo-controlling-behaviour-former-mistress

[https://torontosun.com/news/world/ex-google-ceo-controlling-behaviour-former-mistress](https://torontosun.com/news/world/ex-google-ceo-controlling-behaviour-former-mistress)
[software online review](https://software-online-review.com/category/software-online-review/)

### FK – I was a worker without even knowing it.
[FK – I was a worker without even knowing it.](https://software-online-review.com/2025/09/20/5-millionare-habits-no-one-talks-about/)
[September 20, 2025February 17, 2026](https://software-online-review.com/2025/09/20/5-millionare-habits-no-one-talks-about/)
[Filip Keser](https://software-online-review.com/author/fkeser/)

### How The Rich Think
https://youtu.be/vgqOD_RQDXo?si=0z_kZBJSBQ7VHDCM

[https://youtu.be/vgqOD_RQDXo?si=0z_kZBJSBQ7VHDCM](https://youtu.be/vgqOD_RQDXo?si=0z_kZBJSBQ7VHDCM)
Why Saving Money Won’t Make You Rich

https://youtu.be/8_OhhDArtXA?si=92Am9vdD2x1eKKF_

[https://youtu.be/8_OhhDArtXA?si=92Am9vdD2x1eKKF_](https://youtu.be/8_OhhDArtXA?si=92Am9vdD2x1eKKF_)
5 Millionare Habits No One Talks About

https://youtu.be/wctHLA2U864?si=QJrW1h6awHGbNUvr

[https://youtu.be/wctHLA2U864?si=QJrW1h6awHGbNUvr](https://youtu.be/wctHLA2U864?si=QJrW1h6awHGbNUvr)

### Nobody Cares Until You Win
https://youtu.be/dOel-VRlWDE?si=_eNFbyn1vgOIQxuo

[https://youtu.be/dOel-VRlWDE?si=_eNFbyn1vgOIQxuo](https://youtu.be/dOel-VRlWDE?si=_eNFbyn1vgOIQxuo)
Don’t Stop Just Before You Make It

https://youtu.be/DwnX20RMSTg?si=MIAr3RL8avAusGpJ

[https://youtu.be/DwnX20RMSTg?si=MIAr3RL8avAusGpJ](https://youtu.be/DwnX20RMSTg?si=MIAr3RL8avAusGpJ)
Secrets the Welthy Alredy Know

https://youtu.be/deQU7CWxSTc?si=XJTnzXQ9OJgJ7_RD

[https://youtu.be/deQU7CWxSTc?si=XJTnzXQ9OJgJ7_RD](https://youtu.be/deQU7CWxSTc?si=XJTnzXQ9OJgJ7_RD)
Never Start What You Can’t Finish

https://youtu.be/5yx7HALtRfA?si=_5IwLx-vEFqxrreH

[https://youtu.be/5yx7HALtRfA?si=_5IwLx-vEFqxrreH](https://youtu.be/5yx7HALtRfA?si=_5IwLx-vEFqxrreH)
The Billionare Lawyer Who Took Down Disney & Coca-Cola, Grow or Die, Google Vision

https://youtu.be/u0XdaETDMjg?si=jKyGpuhxzXH2FQKp

[https://youtu.be/u0XdaETDMjg?si=jKyGpuhxzXH2FQKp](https://youtu.be/u0XdaETDMjg?si=jKyGpuhxzXH2FQKp)
John Morgan – Morgan & Morgan

https://youtu.be/EF6-Ed2H2cE?si=eH4YLVA1REs3JFmj

[https://youtu.be/EF6-Ed2H2cE?si=eH4YLVA1REs3JFmj](https://youtu.be/EF6-Ed2H2cE?si=eH4YLVA1REs3JFmj)
How to Be a Business Champion – John Morgan

https://youtu.be/dM1x8vexP5E?si=KsUWt3WusJwjfB54

[https://youtu.be/dM1x8vexP5E?si=KsUWt3WusJwjfB54](https://youtu.be/dM1x8vexP5E?si=KsUWt3WusJwjfB54)
John Morgan speach

https://youtu.be/KsFu2emsnaY?si=JElhIqoGhlFJjwe1

[https://youtu.be/KsFu2emsnaY?si=JElhIqoGhlFJjwe1](https://youtu.be/KsFu2emsnaY?si=JElhIqoGhlFJjwe1)

### Charlie Munger Advice
https://youtu.be/HofGOXEgLKw?si=DxSUBMWhWzLa_ofI

[https://youtu.be/HofGOXEgLKw?si=DxSUBMWhWzLa_ofI](https://youtu.be/HofGOXEgLKw?si=DxSUBMWhWzLa_ofI)

### Machiavelli
https://youtu.be/GWFGoPTOeQA?si=RCyttQv9n21wK-WZ

[https://youtu.be/GWFGoPTOeQA?si=RCyttQv9n21wK-WZ](https://youtu.be/GWFGoPTOeQA?si=RCyttQv9n21wK-WZ)
Learn Like a Loser

https://youtu.be/Xrt-J9wMygM?si=xXLePuXqwzuh-7_U

[https://youtu.be/Xrt-J9wMygM?si=xXLePuXqwzuh-7_U](https://youtu.be/Xrt-J9wMygM?si=xXLePuXqwzuh-7_U)
How to Never Lose Money

https://youtu.be/Kv_pEewrVgA?si=jHLgzMGeSme0j_y-

[https://youtu.be/Kv_pEewrVgA?si=jHLgzMGeSme0j_y-](https://youtu.be/Kv_pEewrVgA?si=jHLgzMGeSme0j_y-)
[software online review](https://software-online-review.com/category/software-online-review/)

### Systems
[Systems](https://software-online-review.com/2025/09/14/systems/)
[September 14, 2025October 10, 2025](https://software-online-review.com/2025/09/14/systems/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
Don’t Set Goals, Create Systems

https://youtu.be/oz4TPEccl5Y?si=EXIRewkt7FBWDpYF

[https://youtu.be/oz4TPEccl5Y?si=EXIRewkt7FBWDpYF](https://youtu.be/oz4TPEccl5Y?si=EXIRewkt7FBWDpYF)
[software online review](https://software-online-review.com/category/software-online-review/)

### daily
[daily](https://software-online-review.com/2025/08/22/daily/)
[August 22, 2025](https://software-online-review.com/2025/08/22/daily/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://youtube.com/shorts/6x0z18DK1yI?si=mRksxb1UwWWl1QEu

[https://youtube.com/shorts/6x0z18DK1yI?si=mRksxb1UwWWl1QEu](https://youtube.com/shorts/6x0z18DK1yI?si=mRksxb1UwWWl1QEu)
[software online review](https://software-online-review.com/category/software-online-review/)

### No One Is Your Friend Until You Win | Jack Ma’s Most Brutal Truth
[No One Is Your Friend Until You Win | Jack Ma’s Most Brutal Truth](https://software-online-review.com/2025/08/20/no-one-is-your-friend-until-you-win-jack-mas-most-brutal-truth/)
[August 20, 2025](https://software-online-review.com/2025/08/20/no-one-is-your-friend-until-you-win-jack-mas-most-brutal-truth/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
[software online review](https://software-online-review.com/category/software-online-review/)

### MC post
[MC post](https://software-online-review.com/2025/06/22/mc-post/)
[June 22, 2025October 22, 2025](https://software-online-review.com/2025/06/22/mc-post/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
Mark Cuban: I didn’t take a vacation for 7 years—until I became a millionaire

https://www.cnbc.com/2025/06/13/mark-cuban-i-didnt-take-a-vacation-while-building-my-first-business.html

[https://www.cnbc.com/2025/06/13/mark-cuban-i-didnt-take-a-vacation-while-building-my-first-business.html](https://www.cnbc.com/2025/06/13/mark-cuban-i-didnt-take-a-vacation-while-building-my-first-business.html)
[software online review](https://software-online-review.com/category/software-online-review/)

### Why Do the Hardest Workers Often Earn the Least? – Nietzsche and the Lie of Moral Labor
[Why Do the Hardest Workers Often Earn the Least? – Nietzsche and the Lie of Moral Labor](https://software-online-review.com/2025/06/14/why-do-the-hardest-workers-often-earn-the-least-nietzsche-and-the-lie-of-moral-labor/)
[June 14, 2025](https://software-online-review.com/2025/06/14/why-do-the-hardest-workers-often-earn-the-least-nietzsche-and-the-lie-of-moral-labor/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
[e commerce](https://software-online-review.com/category/e-commerce/)
[Google](https://software-online-review.com/category/google/)
[management](https://software-online-review.com/category/management/)
[marketing](https://software-online-review.com/category/technology/marketing/)
[platform](https://software-online-review.com/category/platform/)
[software online review](https://software-online-review.com/category/software-online-review/)
[technology](https://software-online-review.com/category/technology/)
[workflow](https://software-online-review.com/category/workflow/)

### School of Hard Knocks – Edwin Arroyave is an entrepreneur known as the founder and CEO of Skyline Security Management
[School of Hard Knocks – Edwin Arroyave is an entrepreneur known as the founder and CEO of Skyline Security Management](https://software-online-review.com/2025/05/29/school-of-hard-knocks-edwin-arroyave-is-an-entrepreneur-known-as-the-founder-and-ceo-of-skyline-security-management/)
[May 29, 2025May 29, 2025](https://software-online-review.com/2025/05/29/school-of-hard-knocks-edwin-arroyave-is-an-entrepreneur-known-as-the-founder-and-ceo-of-skyline-security-management/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
[Google](https://software-online-review.com/category/google/)
[software online review](https://software-online-review.com/category/software-online-review/)
[April 29, 2025May 1, 2025](https://software-online-review.com/2025/04/29/14445/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Uncut Diamond
[Uncut Diamond](https://software-online-review.com/2025/03/04/uncut-diamond/)
[March 4, 2025](https://software-online-review.com/2025/03/04/uncut-diamond/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
When you merge gmail, history of account gmail and web search, and web presence on exmpl webpage and similar, you got hell of potential to make “imagination” to virtual experience in real time, the real picture. And with right skill, people and of course software and seed it, can develop very good and fast. But it is on higher level. fk

[software online review](https://software-online-review.com/category/software-online-review/)

### Sor – notebooklm google
[Sor – notebooklm google](https://software-online-review.com/2024/10/18/sor-notebooklm-google/)
[October 18, 2024October 19, 2024](https://software-online-review.com/2024/10/18/sor-notebooklm-google/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
for better understanding try insert https://software-online-review.com in notebooklm, the ai generate voices will reproduce context

[https://software-online-review.com](https://software-online-review.com)
https://notebooklm.google/

[https://notebooklm.google/](https://notebooklm.google/)
or just listen produced audio

[https://notebooklm.google.com/notebook/14500c25-5fd5-42e9-b456-7ebd0735f319/audio](https://notebooklm.google.com/notebook/14500c25-5fd5-42e9-b456-7ebd0735f319/audio)
[marketing](https://software-online-review.com/category/technology/marketing/)
[software](https://software-online-review.com/category/software/)
[software online review](https://software-online-review.com/category/software-online-review/)
[technology](https://software-online-review.com/category/technology/)
[workflow](https://software-online-review.com/category/workflow/)

### U.S. Patent and Trademark Office: Official Website and Resources
[U.S. Patent and Trademark Office: Official Website and Resources](https://software-online-review.com/2024/09/01/u-s-patent-and-trademark-office-official-website-and-resources/)
[September 1, 2024](https://software-online-review.com/2024/09/01/u-s-patent-and-trademark-office-official-website-and-resources/)
[F K](https://software-online-review.com/author/filkes/)
https://www.uspto.gov/

[https://www.uspto.gov/](https://www.uspto.gov/)
https://ipidentifier.uspto.gov/#/identifier/welcome

[https://ipidentifier.uspto.gov/#/identifier/welcome](https://ipidentifier.uspto.gov/#/identifier/welcome)
https://www.usa.gov/agencies/u-s-patent-and-trademark-office

[https://www.usa.gov/agencies/u-s-patent-and-trademark-office](https://www.usa.gov/agencies/u-s-patent-and-trademark-office)
https://patents.google.com/

[https://patents.google.com/](https://patents.google.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Stock example
[Stock example](https://software-online-review.com/2023/11/30/stock-example/)
[November 30, 2023](https://software-online-review.com/2023/11/30/stock-example/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.nasdaq.com/

[https://www.nasdaq.com/](https://www.nasdaq.com/)
https://www.google.com/finance/

[https://www.google.com/finance/](https://www.google.com/finance/)
https://www.google.com/finance/quote/GOOGL:NASDAQ?window=MAX

[https://www.google.com/finance/quote/GOOGL:NASDAQ?window=MAX](https://www.google.com/finance/quote/GOOGL:NASDAQ?window=MAX)
https://www.google.com/finance/quote/MSFT:NASDAQ?window=MAX

[https://www.google.com/finance/quote/MSFT:NASDAQ?window=MAX](https://www.google.com/finance/quote/MSFT:NASDAQ?window=MAX)
[software online review](https://software-online-review.com/category/software-online-review/)

### Cast
[Cast](https://software-online-review.com/2023/03/24/cast/)
[March 24, 2023](https://software-online-review.com/2023/03/24/cast/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://cast.ai/

[https://cast.ai/](https://cast.ai/)
[software online review](https://software-online-review.com/category/software-online-review/)

### web apps – blazor
[web apps – blazor](https://software-online-review.com/2023/03/15/web-apps/)
[March 15, 2023March 15, 2023](https://software-online-review.com/2023/03/15/web-apps/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps

[https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps](https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps)
https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor

[https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor](https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor)
[software online review](https://software-online-review.com/category/software-online-review/)

### ibm itsm itil
[ibm itsm itil](https://software-online-review.com/2023/03/09/ibm-itsm-itil/)
[March 9, 2023](https://software-online-review.com/2023/03/09/ibm-itsm-itil/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.ibm.com/us-en/

[https://www.ibm.com/us-en/](https://www.ibm.com/us-en/)
https://www.ibm.com/topics/it-service-management

[https://www.ibm.com/topics/it-service-management](https://www.ibm.com/topics/it-service-management)
https://www.ibm.com/topics/it-infrastructure-library

[https://www.ibm.com/topics/it-infrastructure-library](https://www.ibm.com/topics/it-infrastructure-library)
[software online review](https://software-online-review.com/category/software-online-review/)

### Uml
[Uml](https://software-online-review.com/2023/03/09/uml/)
[March 9, 2023](https://software-online-review.com/2023/03/09/uml/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.uml.org/

[https://www.uml.org/](https://www.uml.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### duplocloud
[duplocloud](https://software-online-review.com/2023/03/09/duplocloud/)
[March 9, 2023](https://software-online-review.com/2023/03/09/duplocloud/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
[Home – Old](https://duplocloud.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### archimatetool
[archimatetool](https://software-online-review.com/2023/03/09/archimatetool/)
[March 9, 2023](https://software-online-review.com/2023/03/09/archimatetool/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
[Home](https://www.archimatetool.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### zyte
[zyte](https://software-online-review.com/2022/12/14/zyte/)
[December 14, 2022](https://software-online-review.com/2022/12/14/zyte/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.zyte.com/b/

[https://www.zyte.com/b/](https://www.zyte.com/b/)
[software online review](https://software-online-review.com/category/software-online-review/)

### os
[os](https://software-online-review.com/2022/10/27/os/)
[October 27, 2022](https://software-online-review.com/2022/10/27/os/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://zorin.com/

[https://zorin.com/](https://zorin.com/)
https://ubuntu.com/

[https://ubuntu.com/](https://ubuntu.com/)
https://linuxmint.com/

[https://linuxmint.com/](https://linuxmint.com/)
https://puppylinux-woof-ce.github.io/index.html

[https://puppylinux-woof-ce.github.io/index.html](https://puppylinux-woof-ce.github.io/index.html)
https://getsol.us/home/

[https://getsol.us/home/](https://getsol.us/home/)
https://www.debian.org/

[https://www.debian.org/](https://www.debian.org/)
https://getfedora.org/

[https://getfedora.org/](https://getfedora.org/)
https://archlinux.org/

[https://archlinux.org/](https://archlinux.org/)
https://www.parrotsec.org/

[https://www.parrotsec.org/](https://www.parrotsec.org/)
https://www.linux.org/

[https://www.linux.org/](https://www.linux.org/)
https://elementary.io/

[https://elementary.io/](https://elementary.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### appian
[appian](https://software-online-review.com/2022/10/24/appian/)
[October 24, 2022](https://software-online-review.com/2022/10/24/appian/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://appian.com/

[https://appian.com/](https://appian.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Amazon
[Amazon](https://software-online-review.com/2022/10/14/amazon/)
[October 14, 2022October 14, 2022](https://software-online-review.com/2022/10/14/amazon/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.amazon.com/

[https://www.amazon.com/](https://www.amazon.com/)
https://developer.amazon.com/

[https://developer.amazon.com/](https://developer.amazon.com/)
https://business.amazon.com/

[https://business.amazon.com/](https://business.amazon.com/)
https://aws.amazon.com/

[https://aws.amazon.com/](https://aws.amazon.com/)
https://en.m.wikipedia.org/wiki/Amazon_(company)

[https://en.m.wikipedia.org/wiki/Amazon_(company)](https://en.m.wikipedia.org/wiki/Amazon_(company))
https://www.nasdaq.com/market-activity/stocks/amzn

[https://www.nasdaq.com/market-activity/stocks/amzn](https://www.nasdaq.com/market-activity/stocks/amzn)
[software online review](https://software-online-review.com/category/software-online-review/)

### Oracle
[Oracle](https://software-online-review.com/2022/10/14/oracle/)
[October 14, 2022](https://software-online-review.com/2022/10/14/oracle/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.oracle.com/

[https://www.oracle.com/](https://www.oracle.com/)
https://www.oracle.com/products/

[https://www.oracle.com/products/](https://www.oracle.com/products/)
https://www.oracle.com/products/software/

[https://www.oracle.com/products/software/](https://www.oracle.com/products/software/)
https://developer.oracle.com/

[https://developer.oracle.com/](https://developer.oracle.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### IBM
[IBM](https://software-online-review.com/2022/10/14/ibm/)
[October 14, 2022](https://software-online-review.com/2022/10/14/ibm/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.ibm.com/

[https://www.ibm.com/](https://www.ibm.com/)
https://www.ibm.com/products

[https://www.ibm.com/products](https://www.ibm.com/products)
https://www.ibm.com/db2

[https://www.ibm.com/db2](https://www.ibm.com/db2)
[software online review](https://software-online-review.com/category/software-online-review/)

### Microsoft
[Microsoft](https://software-online-review.com/2022/10/12/microsoft/)
[October 12, 2022October 14, 2022](https://software-online-review.com/2022/10/12/microsoft/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://visualstudio.microsoft.com/

[https://visualstudio.microsoft.com/](https://visualstudio.microsoft.com/)
https://about.ads.microsoft.com/en-us/partners/

[https://about.ads.microsoft.com/en-us/partners/](https://about.ads.microsoft.com/en-us/partners/)
https://www.microsoft.com/en-us/evalcenter/evaluate-windows-11-enterprise

[https://www.microsoft.com/en-us/evalcenter/evaluate-windows-11-enterprise](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-11-enterprise)
https://www.microsoft.com/en-us/evalcenter/evaluate-windows-10-enterprise

[https://www.microsoft.com/en-us/evalcenter/evaluate-windows-10-enterprise](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-10-enterprise)
https://azuremarketplace.microsoft.com/en-us/

[https://azuremarketplace.microsoft.com/en-us/](https://azuremarketplace.microsoft.com/en-us/)
https://azuremarketplace.microsoft.com/en-us/marketplace/apps

[https://azuremarketplace.microsoft.com/en-us/marketplace/apps](https://azuremarketplace.microsoft.com/en-us/marketplace/apps)
https://azuremarketplace.microsoft.com/en-us/sell

[https://azuremarketplace.microsoft.com/en-us/sell](https://azuremarketplace.microsoft.com/en-us/sell)
https://partner.microsoft.com/en-us/membership

[https://partner.microsoft.com/en-us/membership](https://partner.microsoft.com/en-us/membership)
https://partner.microsoft.com/en-us/training

[https://partner.microsoft.com/en-us/training](https://partner.microsoft.com/en-us/training)
[platform](https://software-online-review.com/category/platform/)

### Apache
[Apache](https://software-online-review.com/2022/10/12/apache/)
[October 12, 2022](https://software-online-review.com/2022/10/12/apache/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://httpd.apache.org/

[https://httpd.apache.org/](https://httpd.apache.org/)
https://spark.apache.org/

[https://spark.apache.org/](https://spark.apache.org/)
https://orc.apache.org/

[https://orc.apache.org/](https://orc.apache.org/)
https://airflow.apache.org/

[https://airflow.apache.org/](https://airflow.apache.org/)
https://parquet.apache.org/

[https://parquet.apache.org/](https://parquet.apache.org/)
https://cassandra.apache.org/

[https://cassandra.apache.org/](https://cassandra.apache.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### shellscript – unix
[shellscript – unix](https://software-online-review.com/2022/10/10/shellscript-unix/)
[October 10, 2022](https://software-online-review.com/2022/10/10/shellscript-unix/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.shellscript.sh/

[https://www.shellscript.sh/](https://www.shellscript.sh/)
https://www.tutorialspoint.com/unix/shell_scripting.htm

[https://www.tutorialspoint.com/unix/shell_scripting.htm](https://www.tutorialspoint.com/unix/shell_scripting.htm)
https://www.opengroup.org/membership/forums/platform/unix

[https://www.opengroup.org/membership/forums/platform/unix](https://www.opengroup.org/membership/forums/platform/unix)
https://www.opengroup.org/membership/forums/platform/unix

[https://www.opengroup.org/membership/forums/platform/unix](https://www.opengroup.org/membership/forums/platform/unix)
[software online review](https://software-online-review.com/category/software-online-review/)

### tableau
[tableau](https://software-online-review.com/2022/10/07/tableau/)
[October 7, 2022October 11, 2022](https://software-online-review.com/2022/10/07/tableau/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.tableau.com/

[https://www.tableau.com/](https://www.tableau.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### qlik
[qlik](https://software-online-review.com/2022/10/07/qlik/)
[October 7, 2022October 11, 2022](https://software-online-review.com/2022/10/07/qlik/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.qlik.com/us/

[https://www.qlik.com/us/](https://www.qlik.com/us/)
[software](https://software-online-review.com/category/software/)

### Global Cybersecurity Leader – Palo Alto Networks
[Global Cybersecurity Leader – Palo Alto Networks](https://software-online-review.com/2022/09/23/global-cybersecurity-leader-palo-alto-networks/)
[September 23, 2022October 11, 2022](https://software-online-review.com/2022/09/23/global-cybersecurity-leader-palo-alto-networks/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.paloaltonetworks.com/

[https://www.paloaltonetworks.com/](https://www.paloaltonetworks.com/)
https://www.paloaltonetworks.com/services/education

[https://www.paloaltonetworks.com/services/education](https://www.paloaltonetworks.com/services/education)
[software online review](https://software-online-review.com/category/software-online-review/)

### Telepresence
[Telepresence](https://software-online-review.com/2022/09/23/telepresence/)
[September 23, 2022](https://software-online-review.com/2022/09/23/telepresence/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.telepresence.io/

[https://www.telepresence.io/](https://www.telepresence.io/)
[management](https://software-online-review.com/category/management/)
[software](https://software-online-review.com/category/software/)

### The world’s most powerful smart workplace management platform | Planon
[The world’s most powerful smart workplace management platform | Planon](https://software-online-review.com/2022/09/21/the-worlds-most-powerful-smart-workplace-management-platform-planon/)
[September 21, 2022](https://software-online-review.com/2022/09/21/the-worlds-most-powerful-smart-workplace-management-platform-planon/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://planonsoftware.com/us/

[https://planonsoftware.com/us/](https://planonsoftware.com/us/)
[technology](https://software-online-review.com/category/technology/)

### Crypto Invoicing, Payroll & Expenses | Request Finance
[Crypto Invoicing, Payroll & Expenses | Request Finance](https://software-online-review.com/2022/08/26/crypto-invoicing-payroll-expenses-request-finance/)
[August 26, 2022](https://software-online-review.com/2022/08/26/crypto-invoicing-payroll-expenses-request-finance/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.request.finance/

[https://www.request.finance/](https://www.request.finance/)
[software](https://software-online-review.com/category/software/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Hightouch | Sync your customer data to business tools
[Hightouch | Sync your customer data to business tools](https://software-online-review.com/2022/08/24/hightouch-sync-your-customer-data-to-business-tools/)
[August 24, 2022August 24, 2022](https://software-online-review.com/2022/08/24/hightouch-sync-your-customer-data-to-business-tools/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://hightouch.com/

[https://hightouch.com/](https://hightouch.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Grafana: The open observability platform | Grafana Labs
[Grafana: The open observability platform | Grafana Labs](https://software-online-review.com/2022/08/24/grafana-the-open-observability-platform-grafana-labs-2/)
[August 24, 2022](https://software-online-review.com/2022/08/24/grafana-the-open-observability-platform-grafana-labs-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://grafana.com/

[https://grafana.com/](https://grafana.com/)
[technology](https://software-online-review.com/category/technology/)

### OpenAI
[OpenAI](https://software-online-review.com/2022/08/22/openai/)
[August 22, 2022](https://software-online-review.com/2022/08/22/openai/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://openai.com/

[https://openai.com/](https://openai.com/)
[software](https://software-online-review.com/category/software/)
[workflow](https://software-online-review.com/category/workflow/)

### UltraEdit Text Editor + Coding Software
[UltraEdit Text Editor + Coding Software](https://software-online-review.com/2022/08/22/ultraedit-text-editor-coding-software/)
[August 22, 2022](https://software-online-review.com/2022/08/22/ultraedit-text-editor-coding-software/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.ultraedit.com/

[https://www.ultraedit.com/](https://www.ultraedit.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Unbounce – The Landing Page Builder & Platform
[Unbounce – The Landing Page Builder & Platform](https://software-online-review.com/2022/08/21/unbounce-the-landing-page-builder-platform/)
[August 21, 2022](https://software-online-review.com/2022/08/21/unbounce-the-landing-page-builder-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://unbounce.com/

[https://unbounce.com/](https://unbounce.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### sumologic
[sumologic](https://software-online-review.com/2022/08/20/sumologic/)
[August 20, 2022](https://software-online-review.com/2022/08/20/sumologic/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.sumologic.com/

[https://www.sumologic.com/](https://www.sumologic.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Global Leader of Cyber Security Solutions and Services | Fortinet
[Global Leader of Cyber Security Solutions and Services | Fortinet](https://software-online-review.com/2022/08/20/global-leader-of-cyber-security-solutions-and-services-fortinet/)
[August 20, 2022](https://software-online-review.com/2022/08/20/global-leader-of-cyber-security-solutions-and-services-fortinet/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.fortinet.com/

[https://www.fortinet.com/](https://www.fortinet.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### LDAP.com – Lightweight Directory Access Protocol
[LDAP.com – Lightweight Directory Access Protocol](https://software-online-review.com/2022/08/20/ldap-com-lightweight-directory-access-protocol/)
[August 20, 2022](https://software-online-review.com/2022/08/20/ldap-com-lightweight-directory-access-protocol/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://ldap.com/

[https://ldap.com/](https://ldap.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Kerberos: The Network Authentication Protocol
[Kerberos: The Network Authentication Protocol](https://software-online-review.com/2022/08/20/kerberos-the-network-authentication-protocol/)
[August 20, 2022](https://software-online-review.com/2022/08/20/kerberos-the-network-authentication-protocol/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://web.mit.edu/kerberos/

[https://web.mit.edu/kerberos/](https://web.mit.edu/kerberos/)
[software online review](https://software-online-review.com/category/software-online-review/)

### MIT – Massachusetts Institute of Technology
[MIT – Massachusetts Institute of Technology](https://software-online-review.com/2022/08/20/mit-massachusetts-institute-of-technology/)
[August 20, 2022](https://software-online-review.com/2022/08/20/mit-massachusetts-institute-of-technology/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://web.mit.edu/

[https://web.mit.edu/](https://web.mit.edu/)
[software online review](https://software-online-review.com/category/software-online-review/)

### DataSunrise – Data and Database Security and Compliance
[DataSunrise – Data and Database Security and Compliance](https://software-online-review.com/2022/08/20/datasunrise-data-and-database-security-and-compliance/)
[August 20, 2022](https://software-online-review.com/2022/08/20/datasunrise-data-and-database-security-and-compliance/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.datasunrise.com/

[https://www.datasunrise.com/](https://www.datasunrise.com/)
[software](https://software-online-review.com/category/software/)
[software online review](https://software-online-review.com/category/software-online-review/)
[technology](https://software-online-review.com/category/technology/)

### software-online-review
[software-online-review](https://software-online-review.com/2022/08/18/software-online-review-2/)
[August 18, 2022](https://software-online-review.com/2022/08/18/software-online-review-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
[software-online-review](https://software-online-review.com/2022/08/18/software-online-review-2/?wp-story-load-in-fullscreen=true&wp-story-play-on-load=true)
[software online review](https://software-online-review.com/category/software-online-review/)

### Yotpo | eCommerce Marketing Platform
[Yotpo | eCommerce Marketing Platform](https://software-online-review.com/2022/08/11/yotpo-ecommerce-marketing-platform/)
[August 11, 2022](https://software-online-review.com/2022/08/11/yotpo-ecommerce-marketing-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.yotpo.com/

[https://www.yotpo.com/](https://www.yotpo.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### The UNIX and Linux Forums – Free Linux and Unix Tech Support
[The UNIX and Linux Forums – Free Linux and Unix Tech Support](https://software-online-review.com/2022/08/08/the-unix-and-linux-forums-free-linux-and-unix-tech-support/)
[August 8, 2022](https://software-online-review.com/2022/08/08/the-unix-and-linux-forums-free-linux-and-unix-tech-support/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.unix.com/

[https://www.unix.com/](https://www.unix.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### PrimeFaces – Ultimate UI Framework
[PrimeFaces – Ultimate UI Framework](https://software-online-review.com/2022/08/08/primefaces-ultimate-ui-framework/)
[August 8, 2022](https://software-online-review.com/2022/08/08/primefaces-ultimate-ui-framework/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.primefaces.org/

[https://www.primefaces.org/](https://www.primefaces.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Jakarta® EE | Cloud Native Enterprise Java | Java EE | the Eclipse Foundation | The Eclipse Foundation
[Jakarta® EE | Cloud Native Enterprise Java | Java EE | the Eclipse Foundation | The Eclipse Foundation](https://software-online-review.com/2022/08/08/jakarta-ee-cloud-native-enterprise-java-java-ee-the-eclipse-foundation-the-eclipse-foundation/)
[August 8, 2022](https://software-online-review.com/2022/08/08/jakarta-ee-cloud-native-enterprise-java-java-ee-the-eclipse-foundation-the-eclipse-foundation/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://jakarta.ee/

[https://jakarta.ee/](https://jakarta.ee/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Download .NET (Linux, macOS, and Windows)
[Download .NET (Linux, macOS, and Windows)](https://software-online-review.com/2022/08/08/download-net-linux-macos-and-windows/)
[August 8, 2022](https://software-online-review.com/2022/08/08/download-net-linux-macos-and-windows/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dotnet.microsoft.com/en-us/download

[https://dotnet.microsoft.com/en-us/download](https://dotnet.microsoft.com/en-us/download)
[software online review](https://software-online-review.com/category/software-online-review/)

### WildFly
[WildFly](https://software-online-review.com/2022/08/08/wildfly/)
[August 8, 2022](https://software-online-review.com/2022/08/08/wildfly/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.wildfly.org/

[https://www.wildfly.org/](https://www.wildfly.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Payara Services Ltd – devoted to Open Source, Java, our customers and the community
[Payara Services Ltd – devoted to Open Source, Java, our customers and the community](https://software-online-review.com/2022/08/08/payara-services-ltd-devoted-to-open-source-java-our-customers-and-the-community/)
[August 8, 2022](https://software-online-review.com/2022/08/08/payara-services-ltd-devoted-to-open-source-java-our-customers-and-the-community/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.payara.fish/

[https://www.payara.fish/](https://www.payara.fish/)
[software online review](https://software-online-review.com/category/software-online-review/)

### JFrog Platform | Complete DevOps Platform from Code to Production
[JFrog Platform | Complete DevOps Platform from Code to Production](https://software-online-review.com/2022/08/08/jfrog-platform-complete-devops-platform-from-code-to-production/)
[August 8, 2022](https://software-online-review.com/2022/08/08/jfrog-platform-complete-devops-platform-from-code-to-production/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://jfrog.com/platform/

[https://jfrog.com/platform/](https://jfrog.com/platform/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Microsoft Endpoint Manager | Microsoft Security
[Microsoft Endpoint Manager | Microsoft Security](https://software-online-review.com/2022/08/03/microsoft-endpoint-manager-microsoft-security/)
[August 3, 2022](https://software-online-review.com/2022/08/03/microsoft-endpoint-manager-microsoft-security/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.microsoft.com/en-us/security/business/microsoft-endpoint-manager

[https://www.microsoft.com/en-us/security/business/microsoft-endpoint-manager](https://www.microsoft.com/en-us/security/business/microsoft-endpoint-manager)
[software online review](https://software-online-review.com/category/software-online-review/)

### Google Data Studio
[Google Data Studio](https://software-online-review.com/2022/07/18/google-data-studio-3/)
[July 18, 2022March 19, 2023](https://software-online-review.com/2022/07/18/google-data-studio-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://datastudio.google.com

[https://datastudio.google.com](https://datastudio.google.com/u/0/)
[software online review](https://software-online-review.com/category/software-online-review/)

### PowerPoint charts :: Waterfall, Gantt, Mekko, Process Flow and Agenda :: think-cell
[PowerPoint charts :: Waterfall, Gantt, Mekko, Process Flow and Agenda :: think-cell](https://software-online-review.com/2022/07/18/powerpoint-charts-waterfall-gantt-mekko-process-flow-and-agenda-think-cell/)
[July 18, 2022](https://software-online-review.com/2022/07/18/powerpoint-charts-waterfall-gantt-mekko-process-flow-and-agenda-think-cell/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.think-cell.com/en/

[https://www.think-cell.com/en/](https://www.think-cell.com/en/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Get started with Google Cloud training and certification
[Get started with Google Cloud training and certification](https://software-online-review.com/2022/07/12/get-started-with-google-cloud-training-and-certification/)
[July 12, 2022March 19, 2023](https://software-online-review.com/2022/07/12/get-started-with-google-cloud-training-and-certification/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://cloudonair.withgoogle.com/events/get-started-google-cloud-training

[https://cloudonair.withgoogle.com/events/get-started-google-cloud-training](https://cloudonair.withgoogle.com/events/get-started-google-cloud-training)
[software online review](https://software-online-review.com/category/software-online-review/)

### API Documentation & Design Tools for Teams | Swagger
[API Documentation & Design Tools for Teams | Swagger](https://software-online-review.com/2022/05/23/api-documentation-design-tools-for-teams-swagger/)
[May 23, 2022](https://software-online-review.com/2022/05/23/api-documentation-design-tools-for-teams-swagger/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://swagger.io/

[https://swagger.io/](https://swagger.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Project Lombok
[Project Lombok](https://software-online-review.com/2022/05/23/project-lombok/)
[May 23, 2022](https://software-online-review.com/2022/05/23/project-lombok/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://projectlombok.org/

[https://projectlombok.org/](https://projectlombok.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Amazon.com. Spend less. Smile more.
[Amazon.com. Spend less. Smile more.](https://software-online-review.com/2022/05/07/amazon-com-spend-less-smile-more/)
[May 7, 2022](https://software-online-review.com/2022/05/07/amazon-com-spend-less-smile-more/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.amazon.com/

[https://www.amazon.com/](https://www.amazon.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Product Hunt – The best new products in tech.
[Product Hunt – The best new products in tech.](https://software-online-review.com/2022/04/07/product-hunt-the-best-new-products-in-tech-4/)
[April 7, 2022](https://software-online-review.com/2022/04/07/product-hunt-the-best-new-products-in-tech-4/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.producthunt.com/

[https://www.producthunt.com/](https://www.producthunt.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Microsoft Download Center: Windows, Office, Xbox & More
[Microsoft Download Center: Windows, Office, Xbox & More](https://software-online-review.com/2022/04/07/microsoft-download-center-windows-office-xbox-more/)
[April 7, 2022](https://software-online-review.com/2022/04/07/microsoft-download-center-windows-office-xbox-more/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.microsoft.com/en-us/download

[https://www.microsoft.com/en-us/download](https://www.microsoft.com/en-us/download)
[software online review](https://software-online-review.com/category/software-online-review/)

### Red Hat Ansible | Automation Platform
[Red Hat Ansible | Automation Platform](https://software-online-review.com/2022/04/05/red-hat-ansible-automation-platform-2/)
[April 5, 2022](https://software-online-review.com/2022/04/05/red-hat-ansible-automation-platform-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.ansible.com/products/automation-platform

[https://www.ansible.com/products/automation-platform](https://www.ansible.com/products/automation-platform)
[software online review](https://software-online-review.com/category/software-online-review/)

### Harvard Business Review – Ideas and Advice for Leaders
[Harvard Business Review – Ideas and Advice for Leaders](https://software-online-review.com/2022/03/21/harvard-business-review-ideas-and-advice-for-leaders/)
[March 21, 2022October 24, 2023](https://software-online-review.com/2022/03/21/harvard-business-review-ideas-and-advice-for-leaders/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://hbr.org/

[https://hbr.org/](https://hbr.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Datawheel
[Datawheel](https://software-online-review.com/2022/03/21/datawheel/)
[March 21, 2022March 20, 2023](https://software-online-review.com/2022/03/21/datawheel/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.datawheel.us/

[https://www.datawheel.us/](https://www.datawheel.us/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Oracle | Cloud Applications and Cloud Platform
[Oracle | Cloud Applications and Cloud Platform](https://software-online-review.com/2022/03/21/oracle-cloud-applications-and-cloud-platform-2/)
[March 21, 2022October 24, 2023](https://software-online-review.com/2022/03/21/oracle-cloud-applications-and-cloud-platform-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.oracle.com/index.html

[https://www.oracle.com/index.html](https://www.oracle.com/index.html)
[software online review](https://software-online-review.com/category/software-online-review/)

### software-online-review-by-fk
[software-online-review-by-fk](https://software-online-review.com/2022/03/21/software-online-review-by-fk/)
[March 21, 2022October 24, 2023](https://software-online-review.com/2022/03/21/software-online-review-by-fk/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://softwareonlinereviewbyfk.wordpress.com/

[https://softwareonlinereviewbyfk.wordpress.com/](https://softwareonlinereviewbyfk.wordpress.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Database Documentation Oracle
[Database Documentation Oracle](https://software-online-review.com/2022/02/24/database-documentation-oracle/)
[February 24, 2022](https://software-online-review.com/2022/02/24/database-documentation-oracle/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://docs.oracle.com/en/database/index.html

[https://docs.oracle.com/en/database/index.html](https://docs.oracle.com/en/database/index.html)
[software online review](https://software-online-review.com/category/software-online-review/)

### Oracle Center
[Oracle Center](https://software-online-review.com/2022/02/24/oracle-center/)
[February 24, 2022](https://software-online-review.com/2022/02/24/oracle-center/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://docs.oracle.com/en/

[https://docs.oracle.com/en/](https://docs.oracle.com/en/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Figma: the collaborative interface design tool.
[Figma: the collaborative interface design tool.](https://software-online-review.com/2022/01/31/figma-the-collaborative-interface-design-tool/)
[January 31, 2022](https://software-online-review.com/2022/01/31/figma-the-collaborative-interface-design-tool/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.figma.com/

[https://www.figma.com/](https://www.figma.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### SiteManager: No Code Collaborative web design platform
[SiteManager: No Code Collaborative web design platform](https://software-online-review.com/2022/01/31/sitemanager-no-code-collaborative-web-design-platform-2/)
[January 31, 2022](https://software-online-review.com/2022/01/31/sitemanager-no-code-collaborative-web-design-platform-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.sitemanager.io/

[https://www.sitemanager.io/](https://www.sitemanager.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Helm
[Helm](https://software-online-review.com/2022/01/31/helm-2/)
[January 31, 2022](https://software-online-review.com/2022/01/31/helm-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://helm.sh/

[https://helm.sh/](https://helm.sh/)
[software online review](https://software-online-review.com/category/software-online-review/)

### .NET | Free. Cross-platform. Open Source.
[.NET | Free. Cross-platform. Open Source.](https://software-online-review.com/2022/01/29/net-free-cross-platform-open-source/)
[January 29, 2022](https://software-online-review.com/2022/01/29/net-free-cross-platform-open-source/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dotnet.microsoft.com/en-us/

[https://dotnet.microsoft.com/en-us/](https://dotnet.microsoft.com/en-us/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Prisma Developer Docs | Palo Alto Networks
[Prisma Developer Docs | Palo Alto Networks](https://software-online-review.com/2022/01/27/prisma-developer-docs-palo-alto-networks/)
[January 27, 2022](https://software-online-review.com/2022/01/27/prisma-developer-docs-palo-alto-networks/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://prisma.pan.dev/

[https://prisma.pan.dev/](https://prisma.pan.dev/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Splunk | Turn Data Into Doing
[Splunk | Turn Data Into Doing](https://software-online-review.com/2022/01/27/splunk-turn-data-into-doing/)
[January 27, 2022](https://software-online-review.com/2022/01/27/splunk-turn-data-into-doing/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.splunk.com/

[https://www.splunk.com/](https://www.splunk.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Cloud SQL: for PostgreSQL, MySQL & SQL Server | Cloud SQL: Relational Database Service | Google Cloud
[Cloud SQL: for PostgreSQL, MySQL & SQL Server | Cloud SQL: Relational Database Service | Google Cloud](https://software-online-review.com/2022/01/27/cloud-sql-for-postgresql-mysql-sql-server-cloud-sql-relational-database-service-google-cloud/)
[January 27, 2022March 19, 2023](https://software-online-review.com/2022/01/27/cloud-sql-for-postgresql-mysql-sql-server-cloud-sql-relational-database-service-google-cloud/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://cloud.google.com/sql

[https://cloud.google.com/sql](https://cloud.google.com/sql)
[software online review](https://software-online-review.com/category/software-online-review/)

### Artifact Registry | Google Cloud
[Artifact Registry | Google Cloud](https://software-online-review.com/2022/01/26/artifact-registry-google-cloud/)
[January 26, 2022March 19, 2023](https://software-online-review.com/2022/01/26/artifact-registry-google-cloud/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://cloud.google.com/artifact-registry

[https://cloud.google.com/artifact-registry](https://cloud.google.com/artifact-registry)
[software online review](https://software-online-review.com/category/software-online-review/)

### Container Registry | Google Cloud
[Container Registry | Google Cloud](https://software-online-review.com/2022/01/26/container-registry-google-cloud/)
[January 26, 2022March 19, 2023](https://software-online-review.com/2022/01/26/container-registry-google-cloud/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://cloud.google.com/container-registry

[https://cloud.google.com/container-registry](https://cloud.google.com/container-registry)
[software online review](https://software-online-review.com/category/software-online-review/)

### GPU-optimized AI, Machine Learning, & HPC Software | NVIDIA NGC
[GPU-optimized AI, Machine Learning, & HPC Software | NVIDIA NGC](https://software-online-review.com/2022/01/25/gpu-optimized-ai-machine-learning-hpc-software-nvidia-ngc/)
[January 25, 2022](https://software-online-review.com/2022/01/25/gpu-optimized-ai-machine-learning-hpc-software-nvidia-ngc/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://catalog.ngc.nvidia.com/

[https://catalog.ngc.nvidia.com/](https://catalog.ngc.nvidia.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### vi
[vi](https://software-online-review.com/2022/01/24/vi/)
[January 24, 2022](https://software-online-review.com/2022/01/24/vi/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.vi.ai/

[https://www.vi.ai/](https://www.vi.ai/)
[software online review](https://software-online-review.com/category/software-online-review/)

### npm
[npm](https://software-online-review.com/2022/01/24/npm/)
[January 24, 2022](https://software-online-review.com/2022/01/24/npm/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.npmjs.com/

[https://www.npmjs.com/](https://www.npmjs.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Work hub | Qatalog
[Work hub | Qatalog](https://software-online-review.com/2022/01/24/work-hub-qatalog/)
[January 24, 2022](https://software-online-review.com/2022/01/24/work-hub-qatalog/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://qatalog.com/

[https://qatalog.com/](https://qatalog.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Java | Oracle
[Java | Oracle](https://software-online-review.com/2022/01/24/java-oracle/)
[January 24, 2022](https://software-online-review.com/2022/01/24/java-oracle/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.java.com/en/

[https://www.java.com/en/](https://www.java.com/en/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Oracle | Cloud Applications and Cloud Platform
[Oracle | Cloud Applications and Cloud Platform](https://software-online-review.com/2022/01/24/oracle-cloud-applications-and-cloud-platform/)
[January 24, 2022](https://software-online-review.com/2022/01/24/oracle-cloud-applications-and-cloud-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.oracle.com/index.html

[https://www.oracle.com/index.html](https://www.oracle.com/index.html)
[software online review](https://software-online-review.com/category/software-online-review/)

### Java Software | Oracle
[Java Software | Oracle](https://software-online-review.com/2022/01/24/java-software-oracle/)
[January 24, 2022](https://software-online-review.com/2022/01/24/java-software-oracle/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.oracle.com/java/

[https://www.oracle.com/java/](https://www.oracle.com/java/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Apache HBase – Apache HBase™ Home
[Apache HBase – Apache HBase™ Home](https://software-online-review.com/2022/01/24/apache-hbase-apache-hbase-home/)
[January 24, 2022](https://software-online-review.com/2022/01/24/apache-hbase-apache-hbase-home/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://hbase.apache.org/

[https://hbase.apache.org/](https://hbase.apache.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Redis
[Redis](https://software-online-review.com/2022/01/24/redis/)
[January 24, 2022](https://software-online-review.com/2022/01/24/redis/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://redis.io/

[https://redis.io/](https://redis.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Apache Kafka
[Apache Kafka](https://software-online-review.com/2022/01/24/apache-kafka/)
[January 24, 2022](https://software-online-review.com/2022/01/24/apache-kafka/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://kafka.apache.org/

[https://kafka.apache.org/](https://kafka.apache.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Welcome to Python.org
[Welcome to Python.org](https://software-online-review.com/2022/01/24/welcome-to-python-org-2/)
[January 24, 2022](https://software-online-review.com/2022/01/24/welcome-to-python-org-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.python.org/

[https://www.python.org/](https://www.python.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Apache Airflow
[Apache Airflow](https://software-online-review.com/2022/01/24/apache-airflow-2/)
[January 24, 2022](https://software-online-review.com/2022/01/24/apache-airflow-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://airflow.apache.org/

[https://airflow.apache.org/](https://airflow.apache.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Apache Spark™ – Unified Engine for large-scale data analytics
[Apache Spark™ – Unified Engine for large-scale data analytics](https://software-online-review.com/2022/01/24/apache-spark-unified-engine-for-large-scale-data-analytics-2/)
[January 24, 2022](https://software-online-review.com/2022/01/24/apache-spark-unified-engine-for-large-scale-data-analytics-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://spark.apache.org/

[https://spark.apache.org/](https://spark.apache.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Apache NiFi
[Apache NiFi](https://software-online-review.com/2022/01/24/apache-nifi/)
[January 24, 2022](https://software-online-review.com/2022/01/24/apache-nifi/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://nifi.apache.org/

[https://nifi.apache.org/](https://nifi.apache.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Apache Flink: Stateful Computations over Data Streams
[Apache Flink: Stateful Computations over Data Streams](https://software-online-review.com/2022/01/24/apache-flink-stateful-computations-over-data-streams-2/)
[January 24, 2022](https://software-online-review.com/2022/01/24/apache-flink-stateful-computations-over-data-streams-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://flink.apache.org/

[https://flink.apache.org/](https://flink.apache.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Google Workspace | Business Apps & Collaboration Tools
[Google Workspace | Business Apps & Collaboration Tools](https://software-online-review.com/2022/01/06/google-workspace-business-apps-collaboration-tools/)
[January 6, 2022March 20, 2023](https://software-online-review.com/2022/01/06/google-workspace-business-apps-collaboration-tools/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://workspace.google.com/intl/en_ie/

[https://workspace.google.com/intl/en_ie/](https://workspace.google.com/intl/en_ie/)
[software online review](https://software-online-review.com/category/software-online-review/)

### AWS Marketplace: Homepage
[AWS Marketplace: Homepage](https://software-online-review.com/2022/01/05/aws-marketplace-homepage-6/)
[January 5, 2022](https://software-online-review.com/2022/01/05/aws-marketplace-homepage-6/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://aws.amazon.com/marketplace

[https://aws.amazon.com/marketplace](https://aws.amazon.com/marketplace)
[software online review](https://software-online-review.com/category/software-online-review/)

### Bitnami: Packaged Applications for Any Platform – Cloud, Container, Virtual Machine
[Bitnami: Packaged Applications for Any Platform – Cloud, Container, Virtual Machine](https://software-online-review.com/2022/01/05/bitnami-packaged-applications-for-any-platform-cloud-container-virtual-machine/)
[January 5, 2022](https://software-online-review.com/2022/01/05/bitnami-packaged-applications-for-any-platform-cloud-container-virtual-machine/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://bitnami.com/

[https://bitnami.com/](https://bitnami.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Code Quality and Code Security | Developers First | SonarSource
[Code Quality and Code Security | Developers First | SonarSource](https://software-online-review.com/2022/01/04/code-quality-and-code-security-developers-first-sonarsource-2/)
[January 4, 2022](https://software-online-review.com/2022/01/04/code-quality-and-code-security-developers-first-sonarsource-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.sonarsource.com/

[https://www.sonarsource.com/](https://www.sonarsource.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Code Quality and Code Security | SonarQube
[Code Quality and Code Security | SonarQube](https://software-online-review.com/2022/01/04/code-quality-and-code-security-sonarqube-4/)
[January 4, 2022](https://software-online-review.com/2022/01/04/code-quality-and-code-security-sonarqube-4/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.sonarqube.org/

[https://www.sonarqube.org/](https://www.sonarqube.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Market leading Real Estate and Facility Management software | Planon
[Market leading Real Estate and Facility Management software | Planon](https://software-online-review.com/2021/11/24/market-leading-real-estate-and-facility-management-software-planon/)
[November 24, 2021](https://software-online-review.com/2021/11/24/market-leading-real-estate-and-facility-management-software-planon/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://planonsoftware.com/us/

[https://planonsoftware.com/us/](https://planonsoftware.com/us/)
[software online review](https://software-online-review.com/category/software-online-review/)

### The Open Data Lake Company | Qubole
[The Open Data Lake Company | Qubole](https://software-online-review.com/2021/11/20/the-open-data-lake-company-qubole/)
[November 20, 2021](https://software-online-review.com/2021/11/20/the-open-data-lake-company-qubole/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.qubole.com/

[https://www.qubole.com/](https://www.qubole.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Firebase
[Firebase](https://software-online-review.com/2021/11/13/firebase-4/)
[November 13, 2021](https://software-online-review.com/2021/11/13/firebase-4/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://firebase.google.com/?hl=hr

[https://firebase.google.com/?hl=hr](https://firebase.google.com/?hl=hr)
[software online review](https://software-online-review.com/category/software-online-review/)

### Drupal – Open Source CMS | Drupal.org
[Drupal – Open Source CMS | Drupal.org](https://software-online-review.com/2021/11/12/drupal-open-source-cms-drupal-org/)
[November 12, 2021](https://software-online-review.com/2021/11/12/drupal-open-source-cms-drupal-org/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.drupal.org/home

[https://www.drupal.org/home](https://www.drupal.org/home)
[software online review](https://software-online-review.com/category/software-online-review/)

### Home | Yarn – Package Manager
[Home | Yarn – Package Manager](https://software-online-review.com/2021/11/12/home-yarn-package-manager-2/)
[November 12, 2021](https://software-online-review.com/2021/11/12/home-yarn-package-manager-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://yarnpkg.com/

[https://yarnpkg.com/](https://yarnpkg.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Composer
[Composer](https://software-online-review.com/2021/11/12/composer/)
[November 12, 2021](https://software-online-review.com/2021/11/12/composer/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://getcomposer.org/

[https://getcomposer.org/](https://getcomposer.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### aliexpress
[aliexpress](https://software-online-review.com/2021/11/10/aliexpress/)
[November 10, 2021](https://software-online-review.com/2021/11/10/aliexpress/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://aliexpress.com

[https://aliexpress.com](https://aliexpress.com)
[software online review](https://software-online-review.com/category/software-online-review/)

### Affiliatly admin panel
[Affiliatly admin panel](https://software-online-review.com/2021/11/09/affiliatly-admin-panel/)
[November 9, 2021](https://software-online-review.com/2021/11/09/affiliatly-admin-panel/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.affiliatly.com/af-1053314/affiliate.panel?mode=register

[https://www.affiliatly.com/af-1053314/affiliate.panel?mode=register](https://www.affiliatly.com/af-1053314/affiliate.panel?mode=register)
[software online review](https://software-online-review.com/category/software-online-review/)

### Making Delivery & Field Service Management Smarter – GSM Tasks
[Making Delivery & Field Service Management Smarter – GSM Tasks](https://software-online-review.com/2021/10/20/making-delivery-field-service-management-smarter-gsm-tasks/)
[October 20, 2021](https://software-online-review.com/2021/10/20/making-delivery-field-service-management-smarter-gsm-tasks/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://gsmtasks.com/

[https://gsmtasks.com/](https://gsmtasks.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Getswift – Your Complete Delivery Management Software Solution
[Getswift – Your Complete Delivery Management Software Solution](https://software-online-review.com/2021/10/20/getswift-your-complete-delivery-management-software-solution/)
[October 20, 2021](https://software-online-review.com/2021/10/20/getswift-your-complete-delivery-management-software-solution/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.getswift.co/

[https://www.getswift.co/](https://www.getswift.co/)
[software online review](https://software-online-review.com/category/software-online-review/)

### topratedlocal
[topratedlocal](https://software-online-review.com/2021/10/20/topratedlocal/)
[October 20, 2021](https://software-online-review.com/2021/10/20/topratedlocal/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.topratedlocal.com

[https://www.topratedlocal.com](https://www.topratedlocal.com)
[software online review](https://software-online-review.com/category/software-online-review/)

### Jungleworks | Powering The On-Demand World
[Jungleworks | Powering The On-Demand World](https://software-online-review.com/2021/10/20/jungleworks-powering-the-on-demand-world/)
[October 20, 2021](https://software-online-review.com/2021/10/20/jungleworks-powering-the-on-demand-world/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://jungleworks.com/

[https://jungleworks.com/](https://jungleworks.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Box — Secure Cloud Content Management, Workflow, and Collaboration
[Box — Secure Cloud Content Management, Workflow, and Collaboration](https://software-online-review.com/2021/10/20/box-secure-cloud-content-management-workflow-and-collaboration/)
[October 20, 2021](https://software-online-review.com/2021/10/20/box-secure-cloud-content-management-workflow-and-collaboration/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.box.com/home

[https://www.box.com/home](https://www.box.com/home)
[software online review](https://software-online-review.com/category/software-online-review/)

### Process Management and Workflow Automation Software – Nintex
[Process Management and Workflow Automation Software – Nintex](https://software-online-review.com/2021/10/20/process-management-and-workflow-automation-software-nintex/)
[October 20, 2021](https://software-online-review.com/2021/10/20/process-management-and-workflow-automation-software-nintex/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.nintex.com/

[https://www.nintex.com/](https://www.nintex.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Document Management Software | eFileCabinet
[Document Management Software | eFileCabinet](https://software-online-review.com/2021/10/20/document-management-software-efilecabinet/)
[October 20, 2021](https://software-online-review.com/2021/10/20/document-management-software-efilecabinet/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.efilecabinet.com/

[https://www.efilecabinet.com/](https://www.efilecabinet.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### DocStar Enterprise Content Management and AP Automation Solutions
[DocStar Enterprise Content Management and AP Automation Solutions](https://software-online-review.com/2021/10/20/docstar-enterprise-content-management-and-ap-automation-solutions/)
[October 20, 2021](https://software-online-review.com/2021/10/20/docstar-enterprise-content-management-and-ap-automation-solutions/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.docstar.com/

[https://www.docstar.com/](https://www.docstar.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Document Management Software | Workflow Automation | DocuWare
[Document Management Software | Workflow Automation | DocuWare](https://software-online-review.com/2021/10/20/document-management-software-workflow-automation-docuware/)
[October 20, 2021](https://software-online-review.com/2021/10/20/document-management-software-workflow-automation-docuware/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://start.docuware.com/

[https://start.docuware.com/](https://start.docuware.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Enterprise Content Management (ECM) | Laserfiche
[Enterprise Content Management (ECM) | Laserfiche](https://software-online-review.com/2021/10/20/enterprise-content-management-ecm-laserfiche/)
[October 20, 2021](https://software-online-review.com/2021/10/20/enterprise-content-management-ecm-laserfiche/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.laserfiche.com/

[https://www.laserfiche.com/](https://www.laserfiche.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### FileNet Content Manager – Overview | IBM
[FileNet Content Manager – Overview | IBM](https://software-online-review.com/2021/10/20/filenet-content-manager-overview-ibm-3/)
[October 20, 2021](https://software-online-review.com/2021/10/20/filenet-content-manager-overview-ibm-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.ibm.com/products/filenet-content-manager

[https://www.ibm.com/products/filenet-content-manager](https://www.ibm.com/products/filenet-content-manager)
[software online review](https://software-online-review.com/category/software-online-review/)

### Apache Spark™ – Unified Engine for large-scale data analytics
[Apache Spark™ – Unified Engine for large-scale data analytics](https://software-online-review.com/2021/10/19/apache-spark-unified-engine-for-large-scale-data-analytics/)
[October 19, 2021](https://software-online-review.com/2021/10/19/apache-spark-unified-engine-for-large-scale-data-analytics/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://spark.apache.org/

[https://spark.apache.org/](https://spark.apache.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Apache Hive TM
[Apache Hive TM](https://software-online-review.com/2021/10/19/apache-hive-tm/)
[October 19, 2021](https://software-online-review.com/2021/10/19/apache-hive-tm/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://hive.apache.org/

[https://hive.apache.org/](https://hive.apache.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Apache Airflow
[Apache Airflow](https://software-online-review.com/2021/10/19/apache-airflow/)
[October 19, 2021](https://software-online-review.com/2021/10/19/apache-airflow/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://airflow.apache.org/

[https://airflow.apache.org/](https://airflow.apache.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Medallia | Customer Experience and Employee Experience
[Medallia | Customer Experience and Employee Experience](https://software-online-review.com/2021/10/05/medallia-customer-experience-and-employee-experience/)
[October 5, 2021](https://software-online-review.com/2021/10/05/medallia-customer-experience-and-employee-experience/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.medallia.com/

[https://www.medallia.com/](https://www.medallia.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Circle | Payments infrastructure for internet businesses
[Circle | Payments infrastructure for internet businesses](https://software-online-review.com/2021/09/30/circle-payments-infrastructure-for-internet-businesses/)
[September 30, 2021](https://software-online-review.com/2021/09/30/circle-payments-infrastructure-for-internet-businesses/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.circle.com/en/

[https://www.circle.com/en/](https://www.circle.com/en/)
[software online review](https://software-online-review.com/category/software-online-review/)

### .NET UI Controls for Developers of Mobile, Desktop, Web, Reporting & BI Apps
[.NET UI Controls for Developers of Mobile, Desktop, Web, Reporting & BI Apps](https://software-online-review.com/2021/09/29/net-ui-controls-for-developers-of-mobile-desktop-web-reporting-bi-apps/)
[September 29, 2021](https://software-online-review.com/2021/09/29/net-ui-controls-for-developers-of-mobile-desktop-web-reporting-bi-apps/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.devexpress.com/

[https://www.devexpress.com/](https://www.devexpress.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Unlock digital potential – Optimizely
[Unlock digital potential – Optimizely](https://software-online-review.com/2021/09/24/unlock-digital-potential-optimizely/)
[September 24, 2021](https://software-online-review.com/2021/09/24/unlock-digital-potential-optimizely/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.optimizely.com/

[https://www.optimizely.com/](https://www.optimizely.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Bulbshare | The Customer Collaboration Platform
[Bulbshare | The Customer Collaboration Platform](https://software-online-review.com/2021/09/24/bulbshare-the-customer-collaboration-platform/)
[September 24, 2021](https://software-online-review.com/2021/09/24/bulbshare-the-customer-collaboration-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://bulbshare.com/

[https://bulbshare.com/](https://bulbshare.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Rock-solid SMS gateway – Sign up for free – GatewayAPI
[Rock-solid SMS gateway – Sign up for free – GatewayAPI](https://software-online-review.com/2021/09/24/rock-solid-sms-gateway-sign-up-for-free-gatewayapi/)
[September 24, 2021](https://software-online-review.com/2021/09/24/rock-solid-sms-gateway-sign-up-for-free-gatewayapi/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://gatewayapi.com/

[https://gatewayapi.com/](https://gatewayapi.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Supermetrics: the easiest way to move your marketing data
[Supermetrics: the easiest way to move your marketing data](https://software-online-review.com/2021/09/18/supermetrics-the-easiest-way-to-move-your-marketing-data-2/)
[September 18, 2021](https://software-online-review.com/2021/09/18/supermetrics-the-easiest-way-to-move-your-marketing-data-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://supermetrics.com/

[https://supermetrics.com/](https://supermetrics.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Code Quality and Code Security | SonarQube
[Code Quality and Code Security | SonarQube](https://software-online-review.com/2021/09/17/code-quality-and-code-security-sonarqube-3/)
[September 17, 2021](https://software-online-review.com/2021/09/17/code-quality-and-code-security-sonarqube-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.sonarqube.org/

[https://www.sonarqube.org/](https://www.sonarqube.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Free Online Survey Software and Tools | QuestionPro®
[Free Online Survey Software and Tools | QuestionPro®](https://software-online-review.com/2021/09/17/free-online-survey-software-and-tools-questionpro/)
[September 17, 2021](https://software-online-review.com/2021/09/17/free-online-survey-software-and-tools-questionpro/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.questionpro.com/

[https://www.questionpro.com/](https://www.questionpro.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### The FreeBSD Project
[The FreeBSD Project](https://software-online-review.com/2021/09/16/the-freebsd-project-3/)
[September 16, 2021](https://software-online-review.com/2021/09/16/the-freebsd-project-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.freebsd.org/

[https://www.freebsd.org/](https://www.freebsd.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Visa Partner
[Visa Partner](https://software-online-review.com/2021/09/11/visa-partner/)
[September 11, 2021](https://software-online-review.com/2021/09/11/visa-partner/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://partner.visa.com/homepage.html

[https://partner.visa.com/homepage.html](https://partner.visa.com/homepage.html)
[software online review](https://software-online-review.com/category/software-online-review/)

### KnowledgeForce Platform | Market Force
[KnowledgeForce Platform | Market Force](https://software-online-review.com/2021/09/11/knowledgeforce-platform-market-force/)
[September 11, 2021](https://software-online-review.com/2021/09/11/knowledgeforce-platform-market-force/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.marketforce.com/knowledgeforce

[https://www.marketforce.com/knowledgeforce](https://www.marketforce.com/knowledgeforce)
[software online review](https://software-online-review.com/category/software-online-review/)

### Customer Experience Management (CX) | Market Force
[Customer Experience Management (CX) | Market Force](https://software-online-review.com/2021/09/11/customer-experience-management-cx-market-force/)
[September 11, 2021](https://software-online-review.com/2021/09/11/customer-experience-management-cx-market-force/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.marketforce.com/

[https://www.marketforce.com/](https://www.marketforce.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Partnership Automation: Key to Partnership Success | Impact
[Partnership Automation: Key to Partnership Success | Impact](https://software-online-review.com/2021/09/10/partnership-automation-key-to-partnership-success-impact/)
[September 10, 2021](https://software-online-review.com/2021/09/10/partnership-automation-key-to-partnership-success-impact/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://impact.com/

[https://impact.com/](https://impact.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Impactio – America’s #1 Impact Analytics and Reputation Management Platform for PhDs
[Impactio – America’s #1 Impact Analytics and Reputation Management Platform for PhDs](https://software-online-review.com/2021/09/10/impactio-americas-1-impact-analytics-and-reputation-management-platform-for-phds/)
[September 10, 2021](https://software-online-review.com/2021/09/10/impactio-americas-1-impact-analytics-and-reputation-management-platform-for-phds/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.impactio.com/

[https://www.impactio.com/](https://www.impactio.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### TrustRadius: Software Reviews, Software Comparisons and More
[TrustRadius: Software Reviews, Software Comparisons and More](https://software-online-review.com/2021/09/07/trustradius-software-reviews-software-comparisons-and-more-2/)
[September 7, 2021](https://software-online-review.com/2021/09/07/trustradius-software-reviews-software-comparisons-and-more-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.trustradius.com/

[https://www.trustradius.com/](https://www.trustradius.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### MX | Powering the Money Experience for 30 Million Users
[MX | Powering the Money Experience for 30 Million Users](https://software-online-review.com/2021/09/04/mx-powering-the-money-experience-for-30-million-users/)
[September 4, 2021](https://software-online-review.com/2021/09/04/mx-powering-the-money-experience-for-30-million-users/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.mx.com/

[https://www.mx.com/](https://www.mx.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Databricks – The Data and AI Company
[Databricks – The Data and AI Company](https://software-online-review.com/2021/09/04/databricks-the-data-and-ai-company/)
[September 4, 2021](https://software-online-review.com/2021/09/04/databricks-the-data-and-ai-company/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://databricks.com/

[https://databricks.com/](https://databricks.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Front – Customer Communication Platform | Team Email
[Front – Customer Communication Platform | Team Email](https://software-online-review.com/2021/09/02/front-customer-communication-platform-team-email-2/)
[September 2, 2021](https://software-online-review.com/2021/09/02/front-customer-communication-platform-team-email-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://front.com/

[https://front.com/](https://front.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### The most powerful Git client for Mac and Windows | Tower Git Client
[The most powerful Git client for Mac and Windows | Tower Git Client](https://software-online-review.com/2021/09/02/the-most-powerful-git-client-for-mac-and-windows-tower-git-client/)
[September 2, 2021](https://software-online-review.com/2021/09/02/the-most-powerful-git-client-for-mac-and-windows-tower-git-client/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.git-tower.com/

[https://www.git-tower.com/](https://www.git-tower.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Welcome | AWS Training & Certification
[Welcome | AWS Training & Certification](https://software-online-review.com/2021/08/30/welcome-aws-training-certification/)
[August 30, 2021](https://software-online-review.com/2021/08/30/welcome-aws-training-certification/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.aws.training/

[https://www.aws.training/](https://www.aws.training/)
[software online review](https://software-online-review.com/category/software-online-review/)

### The Power Query user interface | Microsoft Docs
[The Power Query user interface | Microsoft Docs](https://software-online-review.com/2021/08/30/the-power-query-user-interface-microsoft-docs/)
[August 30, 2021](https://software-online-review.com/2021/08/30/the-power-query-user-interface-microsoft-docs/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://docs.microsoft.com/en-us/power-query/power-query-ui

[https://docs.microsoft.com/en-us/power-query/power-query-ui](https://docs.microsoft.com/en-us/power-query/power-query-ui)
[software online review](https://software-online-review.com/category/software-online-review/)

### XenForo – Compelling community forum platform
[XenForo – Compelling community forum platform](https://software-online-review.com/2021/08/30/xenforo-compelling-community-forum-platform/)
[August 30, 2021](https://software-online-review.com/2021/08/30/xenforo-compelling-community-forum-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://xenforo.com/

[https://xenforo.com/](https://xenforo.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Ondato: complete and cost-effective compliance management suite
[Ondato: complete and cost-effective compliance management suite](https://software-online-review.com/2021/08/26/ondato-complete-and-cost-effective-compliance-management-suite/)
[August 26, 2021](https://software-online-review.com/2021/08/26/ondato-complete-and-cost-effective-compliance-management-suite/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://ondato.com/

[https://ondato.com/](https://ondato.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Cyber Security Leader | Imperva, Inc.
[Cyber Security Leader | Imperva, Inc.](https://software-online-review.com/2021/08/23/cyber-security-leader-imperva-inc-3/)
[August 23, 2021](https://software-online-review.com/2021/08/23/cyber-security-leader-imperva-inc-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.imperva.com/

[https://www.imperva.com/](https://www.imperva.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### id.me
[id.me](https://software-online-review.com/2021/08/23/https-www-id-me/)
[August 23, 2021August 23, 2021](https://software-online-review.com/2021/08/23/https-www-id-me/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.id.me/

[https://www.id.me/](https://www.id.me/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Premium Bootstrap Themes and Templates: Download @ Creative Tim
[Premium Bootstrap Themes and Templates: Download @ Creative Tim](https://software-online-review.com/2021/08/22/premium-bootstrap-themes-and-templates-download-creative-tim-2/)
[August 22, 2021](https://software-online-review.com/2021/08/22/premium-bootstrap-themes-and-templates-download-creative-tim-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.creative-tim.com/

[https://www.creative-tim.com/](https://www.creative-tim.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Gorilla Experiment Builder » Create online behavioural experiments easily
[Gorilla Experiment Builder » Create online behavioural experiments easily](https://software-online-review.com/2021/08/21/gorilla-experiment-builder-create-online-behavioural-experiments-easily/)
[August 21, 2021](https://software-online-review.com/2021/08/21/gorilla-experiment-builder-create-online-behavioural-experiments-easily/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://gorilla.sc/

[https://gorilla.sc/](https://gorilla.sc/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Firebase
[Firebase](https://software-online-review.com/2021/08/20/firebase-3/)
[August 20, 2021March 20, 2023](https://software-online-review.com/2021/08/20/firebase-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://firebase.google.com/?hl=hr

[https://firebase.google.com/?hl=hr](https://firebase.google.com/?hl=hr)
[software online review](https://software-online-review.com/category/software-online-review/)

### Integrations Directory – OneSignal
[Integrations Directory – OneSignal](https://software-online-review.com/2021/08/20/integrations-directory-onesignal/)
[August 20, 2021](https://software-online-review.com/2021/08/20/integrations-directory-onesignal/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://onesignal.com/integrations

[https://onesignal.com/integrations](https://onesignal.com/integrations)
[software online review](https://software-online-review.com/category/software-online-review/)

### Facebook for Business: Marketing on Facebook
[Facebook for Business: Marketing on Facebook](https://software-online-review.com/2021/08/20/facebook-for-business-marketing-on-facebook-4/)
[August 20, 2021](https://software-online-review.com/2021/08/20/facebook-for-business-marketing-on-facebook-4/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://web.facebook.com/business

[https://web.facebook.com/business](https://web.facebook.com/business)
[software online review](https://software-online-review.com/category/software-online-review/)

### Front – Customer Communication Platform | Team Email
[Front – Customer Communication Platform | Team Email](https://software-online-review.com/2021/08/20/front-customer-communication-platform-team-email/)
[August 20, 2021](https://software-online-review.com/2021/08/20/front-customer-communication-platform-team-email/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://front.com/

[https://front.com/](https://front.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Customer Success and Product Experience Software | Gainsight
[Customer Success and Product Experience Software | Gainsight](https://software-online-review.com/2021/08/20/customer-success-and-product-experience-software-gainsight/)
[August 20, 2021](https://software-online-review.com/2021/08/20/customer-success-and-product-experience-software-gainsight/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.gainsight.com/

[https://www.gainsight.com/](https://www.gainsight.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### MoEngage: Insights-led Customer Engagement Platform
[MoEngage: Insights-led Customer Engagement Platform](https://software-online-review.com/2021/08/20/moengage-insights-led-customer-engagement-platform/)
[August 20, 2021](https://software-online-review.com/2021/08/20/moengage-insights-led-customer-engagement-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.moengage.com/

[https://www.moengage.com/](https://www.moengage.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Pendo.io – Product Experience and Digital Adoption Solutions
[Pendo.io – Product Experience and Digital Adoption Solutions](https://software-online-review.com/2021/08/20/pendo-io-product-experience-and-digital-adoption-solutions/)
[August 20, 2021](https://software-online-review.com/2021/08/20/pendo-io-product-experience-and-digital-adoption-solutions/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.pendo.io/

[https://www.pendo.io/](https://www.pendo.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### RudderStack – The Customer Data Platform for Developers
[RudderStack – The Customer Data Platform for Developers](https://software-online-review.com/2021/08/20/rudderstack-the-customer-data-platform-for-developers/)
[August 20, 2021](https://software-online-review.com/2021/08/20/rudderstack-the-customer-data-platform-for-developers/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://rudderstack.com/

[https://rudderstack.com/](https://rudderstack.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Cloud Object Storage | Store & Retrieve Data Anywhere | Amazon Simple Storage Service (S3)
[Cloud Object Storage | Store & Retrieve Data Anywhere | Amazon Simple Storage Service (S3)](https://software-online-review.com/2021/08/20/cloud-object-storage-store-retrieve-data-anywhere-amazon-simple-storage-service-s3/)
[August 20, 2021](https://software-online-review.com/2021/08/20/cloud-object-storage-store-retrieve-data-anywhere-amazon-simple-storage-service-s3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://aws.amazon.com/s3/

[https://aws.amazon.com/s3/](https://aws.amazon.com/s3/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Mparticle
[Mparticle](https://software-online-review.com/2021/08/20/home/)
[August 20, 2021September 10, 2021](https://software-online-review.com/2021/08/20/home/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.mparticle.com/

[https://www.mparticle.com/](https://www.mparticle.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Integrations · Hightouch
[Integrations · Hightouch](https://software-online-review.com/2021/08/20/integrations-%c2%b7-hightouch/)
[August 20, 2021](https://software-online-review.com/2021/08/20/integrations-%c2%b7-hightouch/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://hightouch.io/integrations

[https://hightouch.io/integrations](https://hightouch.io/integrations)
[software online review](https://software-online-review.com/category/software-online-review/)

### Knowledge Base Software That Scales With Your Product-Document360
[Knowledge Base Software That Scales With Your Product-Document360](https://software-online-review.com/2021/08/20/knowledge-base-software-that-scales-with-your-product-document360/)
[August 20, 2021](https://software-online-review.com/2021/08/20/knowledge-base-software-that-scales-with-your-product-document360/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://document360.com/

[https://document360.com/](https://document360.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Payhawk | The Financial System of Tomorrow with NextGen Visa Cards
[Payhawk | The Financial System of Tomorrow with NextGen Visa Cards](https://software-online-review.com/2021/08/20/payhawk-the-financial-system-of-tomorrow-with-nextgen-visa-cards/)
[August 20, 2021](https://software-online-review.com/2021/08/20/payhawk-the-financial-system-of-tomorrow-with-nextgen-visa-cards/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://payhawk.com/

[https://payhawk.com/](https://payhawk.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Online payment processing for internet businesses – Stripe
[Online payment processing for internet businesses – Stripe](https://software-online-review.com/2021/08/20/online-payment-processing-for-internet-businesses-stripe/)
[August 20, 2021](https://software-online-review.com/2021/08/20/online-payment-processing-for-internet-businesses-stripe/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://stripe.com/

[https://stripe.com/](https://stripe.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Send Money, Pay Online or Set Up a Merchant Account – PayPal
[Send Money, Pay Online or Set Up a Merchant Account – PayPal](https://software-online-review.com/2021/08/20/send-money-pay-online-or-set-up-a-merchant-account-paypal/)
[August 20, 2021August 20, 2021](https://software-online-review.com/2021/08/20/send-money-pay-online-or-set-up-a-merchant-account-paypal/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.paypal.com

[https://www.paypal.com](https://www.paypal.com/hr/home)
[software online review](https://software-online-review.com/category/software-online-review/)

### BillDesk – All Your Payments. Single Location.
[BillDesk – All Your Payments. Single Location.](https://software-online-review.com/2021/08/20/billdesk-all-your-payments-single-location/)
[August 20, 2021](https://software-online-review.com/2021/08/20/billdesk-all-your-payments-single-location/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.billdesk.com/

[https://www.billdesk.com/](https://www.billdesk.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Financial Services for Emerging Markets | PayU Global
[Financial Services for Emerging Markets | PayU Global](https://software-online-review.com/2021/08/20/financial-services-for-emerging-markets-payu-global-2/)
[August 20, 2021](https://software-online-review.com/2021/08/20/financial-services-for-emerging-markets-payu-global-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://corporate.payu.com/

[https://corporate.payu.com/](https://corporate.payu.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Global HR Solutions for Distributed Teams | Remote
[Global HR Solutions for Distributed Teams | Remote](https://software-online-review.com/2021/08/19/global-hr-solutions-for-distributed-teams-remote/)
[August 19, 2021](https://software-online-review.com/2021/08/19/global-hr-solutions-for-distributed-teams-remote/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://remote.com/

[https://remote.com/](https://remote.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Payroll & Compliance for International Teams | Deel
[Payroll & Compliance for International Teams | Deel](https://software-online-review.com/2021/08/19/payroll-compliance-for-international-teams-deel/)
[August 19, 2021](https://software-online-review.com/2021/08/19/payroll-compliance-for-international-teams-deel/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.letsdeel.com/

[https://www.letsdeel.com/](https://www.letsdeel.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Save S$1,080 on one year of Accounting and Tax with Osome and OCBC Bank
[Save S$1,080 on one year of Accounting and Tax with Osome and OCBC Bank](https://software-online-review.com/2021/08/18/save-s1080-on-one-year-of-accounting-and-tax-with-osome-and-ocbc-bank/)
[August 18, 2021](https://software-online-review.com/2021/08/18/save-s1080-on-one-year-of-accounting-and-tax-with-osome-and-ocbc-bank/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://osome.com/sg/start-digital/

[https://osome.com/sg/start-digital/](https://osome.com/sg/start-digital/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Online Accounting Software | Small Business Accounting | Xero US
[Online Accounting Software | Small Business Accounting | Xero US](https://software-online-review.com/2021/08/18/online-accounting-software-small-business-accounting-xero-us/)
[August 18, 2021](https://software-online-review.com/2021/08/18/online-accounting-software-small-business-accounting-xero-us/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.xero.com/us/accounting-software/

[https://www.xero.com/us/accounting-software/](https://www.xero.com/us/accounting-software/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Event Management Technology & Hospitality Solutions | Cvent
[Event Management Technology & Hospitality Solutions | Cvent](https://software-online-review.com/2021/08/18/event-management-technology-hospitality-solutions-cvent-2/)
[August 18, 2021](https://software-online-review.com/2021/08/18/event-management-technology-hospitality-solutions-cvent-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.cvent.com/

[https://www.cvent.com/](https://www.cvent.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Product Hunt – The best new products in tech.
[Product Hunt – The best new products in tech.](https://software-online-review.com/2021/08/18/product-hunt-the-best-new-products-in-tech-3/)
[August 18, 2021](https://software-online-review.com/2021/08/18/product-hunt-the-best-new-products-in-tech-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.producthunt.com/

[https://www.producthunt.com/](https://www.producthunt.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### SalesAI Powered Copywriting – ClosersCopy
[SalesAI Powered Copywriting – ClosersCopy](https://software-online-review.com/2021/08/18/salesai-powered-copywriting-closerscopy/)
[August 18, 2021](https://software-online-review.com/2021/08/18/salesai-powered-copywriting-closerscopy/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.closerscopy.com/

[https://www.closerscopy.com/](https://www.closerscopy.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### PyCharm: the Python IDE for Professional Developers by JetBrains
[PyCharm: the Python IDE for Professional Developers by JetBrains](https://software-online-review.com/2021/08/18/pycharm-the-python-ide-for-professional-developers-by-jetbrains-2/)
[August 18, 2021](https://software-online-review.com/2021/08/18/pycharm-the-python-ide-for-professional-developers-by-jetbrains-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.jetbrains.com/pycharm/

[https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Integrations | Parabola
[Integrations | Parabola](https://software-online-review.com/2021/08/18/integrations-parabola/)
[August 18, 2021](https://software-online-review.com/2021/08/18/integrations-parabola/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://parabola.io/integrations

[https://parabola.io/integrations](https://parabola.io/integrations)
[software online review](https://software-online-review.com/category/software-online-review/)

### Where to Pay Later with Zip
[Where to Pay Later with Zip](https://software-online-review.com/2021/08/17/where-to-pay-later-with-zip/)
[August 17, 2021](https://software-online-review.com/2021/08/17/where-to-pay-later-with-zip/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://zip.co/

[https://zip.co/](https://zip.co/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Tricent Compliance Tool
[Tricent Compliance Tool](https://software-online-review.com/2021/08/16/tricent-compliance-tool-2/)
[August 16, 2021](https://software-online-review.com/2021/08/16/tricent-compliance-tool-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.tricent.com/

[https://www.tricent.com/](https://www.tricent.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Apache OpenOffice – Official Site – The Free and Open Productivity Suite
[Apache OpenOffice – Official Site – The Free and Open Productivity Suite](https://software-online-review.com/2021/08/15/apache-openoffice-official-site-the-free-and-open-productivity-suite/)
[August 15, 2021](https://software-online-review.com/2021/08/15/apache-openoffice-official-site-the-free-and-open-productivity-suite/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
http://www.openoffice.org/

[http://www.openoffice.org/](http://www.openoffice.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Prevent Cybersecurity Breaches | Comodo Cybersecurity
[Prevent Cybersecurity Breaches | Comodo Cybersecurity](https://software-online-review.com/2021/08/15/prevent-cybersecurity-breaches-comodo-cybersecurity/)
[August 15, 2021](https://software-online-review.com/2021/08/15/prevent-cybersecurity-breaches-comodo-cybersecurity/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.comodo.com/

[https://www.comodo.com/](https://www.comodo.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Bazaarvoice: Meet shoppers in all the moments that matter
[Bazaarvoice: Meet shoppers in all the moments that matter](https://software-online-review.com/2021/08/10/bazaarvoice-meet-shoppers-in-all-the-moments-that-matter/)
[August 10, 2021](https://software-online-review.com/2021/08/10/bazaarvoice-meet-shoppers-in-all-the-moments-that-matter/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.bazaarvoice.com/

[https://www.bazaarvoice.com/](https://www.bazaarvoice.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### EViews.com
[EViews.com](https://software-online-review.com/2021/08/01/eviews-com-3/)
[August 1, 2021](https://software-online-review.com/2021/08/01/eviews-com-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.eviews.com/home.html

[https://www.eviews.com/home.html](https://www.eviews.com/home.html)
[software online review](https://software-online-review.com/category/software-online-review/)

### Zendesk: Customer Service Software & Sales CRM | Best in 2021
[Zendesk: Customer Service Software & Sales CRM | Best in 2021](https://software-online-review.com/2021/07/31/zendesk-customer-service-software-sales-crm-best-in-2021/)
[July 31, 2021](https://software-online-review.com/2021/07/31/zendesk-customer-service-software-sales-crm-best-in-2021/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.zendesk.com/

[https://www.zendesk.com/](https://www.zendesk.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Top Software at Capterra | Software & Software Reviews For Business & Nonprofit
[Top Software at Capterra | Software & Software Reviews For Business & Nonprofit](https://software-online-review.com/2021/07/27/top-software-at-capterra-software-software-reviews-for-business-nonprofit-5/)
[July 27, 2021](https://software-online-review.com/2021/07/27/top-software-at-capterra-software-software-reviews-for-business-nonprofit-5/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.capterra.com/

[https://www.capterra.com/](https://www.capterra.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Jarvis – AI Copywriting Assistant
[Jarvis – AI Copywriting Assistant](https://software-online-review.com/2021/07/27/jarvis-ai-copywriting-assistant/)
[July 27, 2021](https://software-online-review.com/2021/07/27/jarvis-ai-copywriting-assistant/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.conversion.ai/

[https://www.conversion.ai/](https://www.conversion.ai/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Memgraph | In-Memory Cypher Graph Database
[Memgraph | In-Memory Cypher Graph Database](https://software-online-review.com/2021/07/25/memgraph-in-memory-cypher-graph-database/)
[July 25, 2021](https://software-online-review.com/2021/07/25/memgraph-in-memory-cypher-graph-database/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://memgraph.com/

[https://memgraph.com/](https://memgraph.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Buy Autodesk Software | Get Prices & Buy Online | Official Autodesk Store
[Buy Autodesk Software | Get Prices & Buy Online | Official Autodesk Store](https://software-online-review.com/2021/07/25/buy-autodesk-software-get-prices-buy-online-official-autodesk-store-2/)
[July 25, 2021](https://software-online-review.com/2021/07/25/buy-autodesk-software-get-prices-buy-online-official-autodesk-store-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.autodesk.com/products

[https://www.autodesk.com/products](https://www.autodesk.com/products)
[software online review](https://software-online-review.com/category/software-online-review/)

### Autodesk | 3D Design, Engineering & Construction Software
[Autodesk | 3D Design, Engineering & Construction Software](https://software-online-review.com/2021/07/25/autodesk-3d-design-engineering-construction-software-4/)
[July 25, 2021](https://software-online-review.com/2021/07/25/autodesk-3d-design-engineering-construction-software-4/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.autodesk.com/

[https://www.autodesk.com/](https://www.autodesk.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### EAGLE | PCB Design And Electrical Schematic Software | Autodesk
[EAGLE | PCB Design And Electrical Schematic Software | Autodesk](https://software-online-review.com/2021/07/25/eagle-pcb-design-and-electrical-schematic-software-autodesk/)
[July 25, 2021](https://software-online-review.com/2021/07/25/eagle-pcb-design-and-electrical-schematic-software-autodesk/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.autodesk.com/products/eagle/overview

[https://www.autodesk.com/products/eagle/overview](https://www.autodesk.com/products/eagle/overview)
[software online review](https://software-online-review.com/category/software-online-review/)

### PCB Design Software & Tools | Altium
[PCB Design Software & Tools | Altium](https://software-online-review.com/2021/07/25/pcb-design-software-tools-altium/)
[July 25, 2021](https://software-online-review.com/2021/07/25/pcb-design-software-tools-altium/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.altium.com/

[https://www.altium.com/](https://www.altium.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Workplace Productivity & Automation Tools | Formstack
[Workplace Productivity & Automation Tools | Formstack](https://software-online-review.com/2021/07/25/workplace-productivity-automation-tools-formstack/)
[July 25, 2021](https://software-online-review.com/2021/07/25/workplace-productivity-automation-tools-formstack/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.formstack.com/

[https://www.formstack.com/](https://www.formstack.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Umbraco – the flexible open source .NET CMS
[Umbraco – the flexible open source .NET CMS](https://software-online-review.com/2021/07/20/umbraco-the-flexible-open-source-net-cms-2/)
[July 20, 2021](https://software-online-review.com/2021/07/20/umbraco-the-flexible-open-source-net-cms-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://umbraco.com/

[https://umbraco.com/](https://umbraco.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Umbraco – the flexible open source .NET CMS
[Umbraco – the flexible open source .NET CMS](https://software-online-review.com/2021/07/20/umbraco-the-flexible-open-source-net-cms/)
[July 20, 2021](https://software-online-review.com/2021/07/20/umbraco-the-flexible-open-source-net-cms/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://umbraco.com/

[https://umbraco.com/](https://umbraco.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### The Only Tool You Need To Run a Profitable Agency | Productive
[The Only Tool You Need To Run a Profitable Agency | Productive](https://software-online-review.com/2021/07/18/the-only-tool-you-need-to-run-a-profitable-agency-productive-3/)
[July 18, 2021](https://software-online-review.com/2021/07/18/the-only-tool-you-need-to-run-a-profitable-agency-productive-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.productive.io/

[https://www.productive.io/](https://www.productive.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Talent Relationship Management Software & Applicant Tracking System
[Talent Relationship Management Software & Applicant Tracking System](https://software-online-review.com/2021/07/17/talent-relationship-management-software-applicant-tracking-system-2/)
[July 17, 2021](https://software-online-review.com/2021/07/17/talent-relationship-management-software-applicant-tracking-system-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://thrivetrm.com/

[https://thrivetrm.com/](https://thrivetrm.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Windows Virtual Desktop | Remote Desktop | Microsoft Azure
[Windows Virtual Desktop | Remote Desktop | Microsoft Azure](https://software-online-review.com/2021/07/16/windows-virtual-desktop-remote-desktop-microsoft-azure/)
[July 16, 2021](https://software-online-review.com/2021/07/16/windows-virtual-desktop-remote-desktop-microsoft-azure/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://azure.microsoft.com/en-us/services/virtual-desktop/

[https://azure.microsoft.com/en-us/services/virtual-desktop/](https://azure.microsoft.com/en-us/services/virtual-desktop/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Procurement & Supply Chain Solutions for Spend Management | SAP Ariba
[Procurement & Supply Chain Solutions for Spend Management | SAP Ariba](https://software-online-review.com/2021/07/16/procurement-supply-chain-solutions-for-spend-management-sap-ariba/)
[July 16, 2021](https://software-online-review.com/2021/07/16/procurement-supply-chain-solutions-for-spend-management-sap-ariba/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.ariba.com/

[https://www.ariba.com/](https://www.ariba.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### SAP Store
[SAP Store](https://software-online-review.com/2021/07/16/sap-store/)
[July 16, 2021](https://software-online-review.com/2021/07/16/sap-store/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://store.sap.com/dcp/en/

[https://store.sap.com/dcp/en/](https://store.sap.com/dcp/en/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Semrush – Online Visibility Management Platform
[Semrush – Online Visibility Management Platform](https://software-online-review.com/2021/07/15/semrush-online-visibility-management-platform/)
[July 15, 2021](https://software-online-review.com/2021/07/15/semrush-online-visibility-management-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.semrush.com/

[https://www.semrush.com/](https://www.semrush.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### B2B Network for Supply Chain E Procurement Marketplaces & Digital B2B Payments | Tradeshift
[B2B Network for Supply Chain E Procurement Marketplaces & Digital B2B Payments | Tradeshift](https://software-online-review.com/2021/07/10/b2b-network-for-supply-chain-e-procurement-marketplaces-digital-b2b-payments-tradeshift/)
[July 10, 2021](https://software-online-review.com/2021/07/10/b2b-network-for-supply-chain-e-procurement-marketplaces-digital-b2b-payments-tradeshift/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://tradeshift.com/

[https://tradeshift.com/](https://tradeshift.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Endpoint Management, Security and Risk | Home | Tanium
[Endpoint Management, Security and Risk | Home | Tanium](https://software-online-review.com/2021/07/10/endpoint-management-security-and-risk-home-tanium/)
[July 10, 2021](https://software-online-review.com/2021/07/10/endpoint-management-security-and-risk-home-tanium/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.tanium.com/

[https://www.tanium.com/](https://www.tanium.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Webinar Software. New Platform for Webinars – LiveWebinar.com
[Webinar Software. New Platform for Webinars – LiveWebinar.com](https://software-online-review.com/2021/07/08/webinar-software-new-platform-for-webinars-livewebinar-com/)
[July 8, 2021](https://software-online-review.com/2021/07/08/webinar-software-new-platform-for-webinars-livewebinar-com/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.livewebinar.com/

[https://www.livewebinar.com/](https://www.livewebinar.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Copy Shark | AI Powered Copywriting
[Copy Shark | AI Powered Copywriting](https://software-online-review.com/2021/07/05/copy-shark-ai-powered-copywriting/)
[July 5, 2021](https://software-online-review.com/2021/07/05/copy-shark-ai-powered-copywriting/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.copyshark.ai/

[https://www.copyshark.ai/](https://www.copyshark.ai/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Bryxen – We Create Video Marketing Tools
[Bryxen – We Create Video Marketing Tools](https://software-online-review.com/2021/07/04/bryxen-we-create-video-marketing-tools-2/)
[July 4, 2021](https://software-online-review.com/2021/07/04/bryxen-we-create-video-marketing-tools-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
http://www.bryxen.com/

[http://www.bryxen.com/](http://www.bryxen.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Maps, geocoding, and navigation APIs & SDKs | Mapbox
[Maps, geocoding, and navigation APIs & SDKs | Mapbox](https://software-online-review.com/2021/07/04/maps-geocoding-and-navigation-apis-sdks-mapbox-2/)
[July 4, 2021](https://software-online-review.com/2021/07/04/maps-geocoding-and-navigation-apis-sdks-mapbox-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.mapbox.com/

[https://www.mapbox.com/](https://www.mapbox.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Marker.io: Website Feedback Tool & Bug Tracking
[Marker.io: Website Feedback Tool & Bug Tracking](https://software-online-review.com/2021/07/02/marker-io-website-feedback-tool-bug-tracking/)
[July 2, 2021](https://software-online-review.com/2021/07/02/marker-io-website-feedback-tool-bug-tracking/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://marker.io/

[https://marker.io/](https://marker.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Talent Relationship Management Software & Applicant Tracking System
[Talent Relationship Management Software & Applicant Tracking System](https://software-online-review.com/2021/07/02/talent-relationship-management-software-applicant-tracking-system/)
[July 2, 2021](https://software-online-review.com/2021/07/02/talent-relationship-management-software-applicant-tracking-system/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://thrivetrm.com/

[https://thrivetrm.com/](https://thrivetrm.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Descript | All-in-one audio/video editing, as easy as a doc.
[Descript | All-in-one audio/video editing, as easy as a doc.](https://software-online-review.com/2021/07/02/descript-all-in-one-audio-video-editing-as-easy-as-a-doc/)
[July 2, 2021](https://software-online-review.com/2021/07/02/descript-all-in-one-audio-video-editing-as-easy-as-a-doc/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.descript.com/

[https://www.descript.com/](https://www.descript.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Automatically convert audio and video to text: Fast, Accurate, & Affordable | Sonix
[Automatically convert audio and video to text: Fast, Accurate, & Affordable | Sonix](https://software-online-review.com/2021/07/02/automatically-convert-audio-and-video-to-text-fast-accurate-affordable-sonix/)
[July 2, 2021](https://software-online-review.com/2021/07/02/automatically-convert-audio-and-video-to-text-fast-accurate-affordable-sonix/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://sonix.ai/

[https://sonix.ai/](https://sonix.ai/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Happy Scribe: Audio Transcription & Video Subtitles
[Happy Scribe: Audio Transcription & Video Subtitles](https://software-online-review.com/2021/07/02/happy-scribe-audio-transcription-video-subtitles/)
[July 2, 2021](https://software-online-review.com/2021/07/02/happy-scribe-audio-transcription-video-subtitles/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.happyscribe.com/

[https://www.happyscribe.com/](https://www.happyscribe.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### GoodDay: Inspiring Work Management Platform
[GoodDay: Inspiring Work Management Platform](https://software-online-review.com/2021/07/02/goodday-inspiring-work-management-platform-2/)
[July 2, 2021](https://software-online-review.com/2021/07/02/goodday-inspiring-work-management-platform-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.goodday.work/

[https://www.goodday.work/](https://www.goodday.work/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Instructure | Educational Software Development
[Instructure | Educational Software Development](https://software-online-review.com/2021/07/02/instructure-educational-software-development/)
[July 2, 2021](https://software-online-review.com/2021/07/02/instructure-educational-software-development/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.instructure.com/en-gb

[https://www.instructure.com/en-gb](https://www.instructure.com/en-gb)
[software online review](https://software-online-review.com/category/software-online-review/)

### Digital Publishing Platform for Everyone | Joomag
[Digital Publishing Platform for Everyone | Joomag](https://software-online-review.com/2021/07/01/digital-publishing-platform-for-everyone-joomag/)
[July 1, 2021](https://software-online-review.com/2021/07/01/digital-publishing-platform-for-everyone-joomag/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.joomag.com/en

[https://www.joomag.com/en](https://www.joomag.com/en)
[software online review](https://software-online-review.com/category/software-online-review/)

### Product Integrations – Virtual and Hybrid Events Platform | Airmeet
[Product Integrations – Virtual and Hybrid Events Platform | Airmeet](https://software-online-review.com/2021/06/30/product-integrations-virtual-and-hybrid-events-platform-airmeet/)
[June 30, 2021](https://software-online-review.com/2021/06/30/product-integrations-virtual-and-hybrid-events-platform-airmeet/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.airmeet.com/hub/product-integrations/

[https://www.airmeet.com/hub/product-integrations/](https://www.airmeet.com/hub/product-integrations/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Qlik | Data Analytics & Data Integration Solutions
[Qlik | Data Analytics & Data Integration Solutions](https://software-online-review.com/2021/06/29/qlik-data-analytics-data-integration-solutions/)
[June 29, 2021](https://software-online-review.com/2021/06/29/qlik-data-analytics-data-integration-solutions/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.qlik.com/us/

[https://www.qlik.com/us/](https://www.qlik.com/us/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Angular
[Angular](https://software-online-review.com/2021/06/28/angular-2/)
[June 28, 2021](https://software-online-review.com/2021/06/28/angular-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://angular.io/

[https://angular.io/](https://angular.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### TypeScript: Typed JavaScript at Any Scale.
[TypeScript: Typed JavaScript at Any Scale.](https://software-online-review.com/2021/06/28/typescript-typed-javascript-at-any-scale/)
[June 28, 2021](https://software-online-review.com/2021/06/28/typescript-typed-javascript-at-any-scale/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.typescriptlang.org/

[https://www.typescriptlang.org/](https://www.typescriptlang.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Jest · 🃏 Delightful JavaScript Testing
[Jest · 🃏 Delightful JavaScript Testing](https://software-online-review.com/2021/06/28/jest-%c2%b7-%f0%9f%83%8f-delightful-javascript-testing-2/)
[June 28, 2021](https://software-online-review.com/2021/06/28/jest-%c2%b7-%f0%9f%83%8f-delightful-javascript-testing-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://jestjs.io/

[https://jestjs.io/](https://jestjs.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### RxJS
[RxJS](https://software-online-review.com/2021/06/28/rxjs/)
[June 28, 2021](https://software-online-review.com/2021/06/28/rxjs/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://rxjs.dev/

[https://rxjs.dev/](https://rxjs.dev/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Redux – A predictable state container for JavaScript apps. | Redux
[Redux – A predictable state container for JavaScript apps. | Redux](https://software-online-review.com/2021/06/28/redux-a-predictable-state-container-for-javascript-apps-redux-2/)
[June 28, 2021](https://software-online-review.com/2021/06/28/redux-a-predictable-state-container-for-javascript-apps-redux-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://redux.js.org/

[https://redux.js.org/](https://redux.js.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Duck Creek Technologies | Enterprise P&C Insurance Software
[Duck Creek Technologies | Enterprise P&C Insurance Software](https://software-online-review.com/2021/06/24/duck-creek-technologies-enterprise-pc-insurance-software/)
[June 24, 2021](https://software-online-review.com/2021/06/24/duck-creek-technologies-enterprise-pc-insurance-software/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.duckcreek.com/

[https://www.duckcreek.com/](https://www.duckcreek.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### PHP: Hypertext Preprocessor
[PHP: Hypertext Preprocessor](https://software-online-review.com/2021/06/23/php-hypertext-preprocessor/)
[June 23, 2021](https://software-online-review.com/2021/06/23/php-hypertext-preprocessor/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.php.net/index.php

[https://www.php.net/index.php](https://www.php.net/index.php)
[software online review](https://software-online-review.com/category/software-online-review/)

### SiteManager: No Code Collaborative web design platform
[SiteManager: No Code Collaborative web design platform](https://software-online-review.com/2021/06/23/sitemanager-no-code-collaborative-web-design-platform/)
[June 23, 2021](https://software-online-review.com/2021/06/23/sitemanager-no-code-collaborative-web-design-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.sitemanager.io/

[https://www.sitemanager.io/](https://www.sitemanager.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Home | Grass Valley
[Home | Grass Valley](https://software-online-review.com/2021/06/23/home-grass-valley/)
[June 23, 2021](https://software-online-review.com/2021/06/23/home-grass-valley/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.grassvalley.com/

[https://www.grassvalley.com/](https://www.grassvalley.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Stratus Technologies | Zero-touch Edge Computing
[Stratus Technologies | Zero-touch Edge Computing](https://software-online-review.com/2021/06/23/stratus-technologies-zero-touch-edge-computing/)
[June 23, 2021](https://software-online-review.com/2021/06/23/stratus-technologies-zero-touch-edge-computing/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.stratus.com/

[https://www.stratus.com/](https://www.stratus.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Oracle VM VirtualBox
[Oracle VM VirtualBox](https://software-online-review.com/2021/06/23/oracle-vm-virtualbox/)
[June 23, 2021](https://software-online-review.com/2021/06/23/oracle-vm-virtualbox/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.virtualbox.org/

[https://www.virtualbox.org/](https://www.virtualbox.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Home – Chatlayer.ai
[Home – Chatlayer.ai](https://software-online-review.com/2021/06/21/home-chatlayer-ai/)
[June 21, 2021](https://software-online-review.com/2021/06/21/home-chatlayer-ai/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://chatlayer.ai/

[https://chatlayer.ai/](https://chatlayer.ai/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Sinch – SMS, Voice, Video & Verification APIs
[Sinch – SMS, Voice, Video & Verification APIs](https://software-online-review.com/2021/06/21/sinch-sms-voice-video-verification-apis-2/)
[June 21, 2021](https://software-online-review.com/2021/06/21/sinch-sms-voice-video-verification-apis-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.sinch.com/

[https://www.sinch.com/](https://www.sinch.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Video transcoding, streaming, capture, screen recording, captioning and workflow automation solutions | Telestream, LLC
[Video transcoding, streaming, capture, screen recording, captioning and workflow automation solutions | Telestream, LLC](https://software-online-review.com/2021/06/19/video-transcoding-streaming-capture-screen-recording-captioning-and-workflow-automation-solutions-telestream-llc/)
[June 19, 2021](https://software-online-review.com/2021/06/19/video-transcoding-streaming-capture-screen-recording-captioning-and-workflow-automation-solutions-telestream-llc/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
http://www.telestream.net/

[http://www.telestream.net/](http://www.telestream.net/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Braintree | Online Payment Solutions and Global Payment Processor
[Braintree | Online Payment Solutions and Global Payment Processor](https://software-online-review.com/2021/06/17/braintree-online-payment-solutions-and-global-payment-processor-2/)
[June 17, 2021](https://software-online-review.com/2021/06/17/braintree-online-payment-solutions-and-global-payment-processor-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.braintreepayments.com/hr/

[https://www.braintreepayments.com/hr/](https://www.braintreepayments.com/hr/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Customer Data Platform – CDP | Microsoft Dynamics 365
[Customer Data Platform – CDP | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/customer-data-platform-cdp-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/customer-data-platform-cdp-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/customer-data-platform/

[https://dynamics.microsoft.com/en-us/customer-data-platform/](https://dynamics.microsoft.com/en-us/customer-data-platform/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Customer Insights | Microsoft Dynamics 365
[Customer Insights | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/customer-insights-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/customer-insights-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/ai/customer-insights/

[https://dynamics.microsoft.com/en-us/ai/customer-insights/](https://dynamics.microsoft.com/en-us/ai/customer-insights/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Sales Overview | Microsoft Dynamics 365
[Sales Overview | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/sales-overview-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/sales-overview-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/sales/overview/

[https://dynamics.microsoft.com/en-us/sales/overview/](https://dynamics.microsoft.com/en-us/sales/overview/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Relationship Sales | Microsoft Dynamics 365
[Relationship Sales | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/relationship-sales-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/relationship-sales-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/sales/relationship-sales/

[https://dynamics.microsoft.com/en-us/sales/relationship-sales/](https://dynamics.microsoft.com/en-us/sales/relationship-sales/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Product Visualize | Microsoft Dynamics 365
[Product Visualize | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/product-visualize-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/product-visualize-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/mixed-reality/product-visualize/

[https://dynamics.microsoft.com/en-us/mixed-reality/product-visualize/](https://dynamics.microsoft.com/en-us/mixed-reality/product-visualize/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Customer Service | Microsoft Dynamics 365
[Customer Service | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/customer-service-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/customer-service-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/customer-service/overview/

[https://dynamics.microsoft.com/en-us/customer-service/overview/](https://dynamics.microsoft.com/en-us/customer-service/overview/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Field Service | Microsoft Dynamics 365
[Field Service | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/field-service-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/field-service-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/field-service/overview/

[https://dynamics.microsoft.com/en-us/field-service/overview/](https://dynamics.microsoft.com/en-us/field-service/overview/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Remote Assist | Microsoft Dynamics 365
[Remote Assist | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/remote-assist-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/remote-assist-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/mixed-reality/remote-assist/

[https://dynamics.microsoft.com/en-us/mixed-reality/remote-assist/](https://dynamics.microsoft.com/en-us/mixed-reality/remote-assist/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Marketing – Customer Journey | Microsoft Dynamics 365
[Marketing – Customer Journey | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/marketing-customer-journey-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/marketing-customer-journey-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/marketing/overview/

[https://dynamics.microsoft.com/en-us/marketing/overview/](https://dynamics.microsoft.com/en-us/marketing/overview/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Commerce | Microsoft Dynamics 365
[Commerce | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/commerce-microsoft-dynamics-365-2/)
[June 15, 2021](https://software-online-review.com/2021/06/15/commerce-microsoft-dynamics-365-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/commerce/overview/

[https://dynamics.microsoft.com/en-us/commerce/overview/](https://dynamics.microsoft.com/en-us/commerce/overview/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Commerce | Microsoft Dynamics 365
[Commerce | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/commerce-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/commerce-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/commerce/overview/

[https://dynamics.microsoft.com/en-us/commerce/overview/](https://dynamics.microsoft.com/en-us/commerce/overview/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Connected Store | Microsoft Dynamics 365
[Connected Store | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/connected-store-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/connected-store-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/ai/connected-store/

[https://dynamics.microsoft.com/en-us/ai/connected-store/](https://dynamics.microsoft.com/en-us/ai/connected-store/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Fraud Protection and Loss Prevention | Microsoft Dynamics 365
[Fraud Protection and Loss Prevention | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/fraud-protection-and-loss-prevention-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/fraud-protection-and-loss-prevention-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/ai/fraud-protection/

[https://dynamics.microsoft.com/en-us/ai/fraud-protection/](https://dynamics.microsoft.com/en-us/ai/fraud-protection/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Supply Chain Management | Microsoft Dynamics 365
[Supply Chain Management | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/supply-chain-management-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/supply-chain-management-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/supply-chain-management/overview/

[https://dynamics.microsoft.com/en-us/supply-chain-management/overview/](https://dynamics.microsoft.com/en-us/supply-chain-management/overview/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Microsoft Mixed Reality / AR Guides | Microsoft Dynamics 365
[Microsoft Mixed Reality / AR Guides | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/microsoft-mixed-reality-ar-guides-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/microsoft-mixed-reality-ar-guides-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/mixed-reality/guides/

[https://dynamics.microsoft.com/en-us/mixed-reality/guides/](https://dynamics.microsoft.com/en-us/mixed-reality/guides/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Intelligent Order Management | Microsoft Dynamics 365
[Intelligent Order Management | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/intelligent-order-management-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/intelligent-order-management-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/intelligent-order-management/

[https://dynamics.microsoft.com/en-us/intelligent-order-management/](https://dynamics.microsoft.com/en-us/intelligent-order-management/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Customer Service Professional | Microsoft Dynamics 365
[Customer Service Professional | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/customer-service-professional-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/customer-service-professional-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/customer-service/professional/

[https://dynamics.microsoft.com/en-us/customer-service/professional/](https://dynamics.microsoft.com/en-us/customer-service/professional/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Dynamics 365 Sales Professional
[Dynamics 365 Sales Professional](https://software-online-review.com/2021/06/15/dynamics-365-sales-professional/)
[June 15, 2021](https://software-online-review.com/2021/06/15/dynamics-365-sales-professional/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/sales/professional/

[https://dynamics.microsoft.com/en-us/sales/professional/](https://dynamics.microsoft.com/en-us/sales/professional/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Human Resources | Microsoft Dynamics 365
[Human Resources | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/human-resources-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/human-resources-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/human-resources/overview/

[https://dynamics.microsoft.com/en-us/human-resources/overview/](https://dynamics.microsoft.com/en-us/human-resources/overview/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Finance | Microsoft Dynamics 365
[Finance | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/finance-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/finance-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/finance/overview/

[https://dynamics.microsoft.com/en-us/finance/overview/](https://dynamics.microsoft.com/en-us/finance/overview/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Project Operations | Microsoft Dynamics 365
[Project Operations | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/project-operations-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/project-operations-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/project-operations/overview/

[https://dynamics.microsoft.com/en-us/project-operations/overview/](https://dynamics.microsoft.com/en-us/project-operations/overview/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Business Application Platform | Microsoft Power Platform
[Business Application Platform | Microsoft Power Platform](https://software-online-review.com/2021/06/15/business-application-platform-microsoft-power-platform-3/)
[June 15, 2021](https://software-online-review.com/2021/06/15/business-application-platform-microsoft-power-platform-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://powerplatform.microsoft.com/en-us/

[https://powerplatform.microsoft.com/en-us/](https://powerplatform.microsoft.com/en-us/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Common Data Model | Microsoft Power Platform
[Common Data Model | Microsoft Power Platform](https://software-online-review.com/2021/06/15/common-data-model-microsoft-power-platform/)
[June 15, 2021](https://software-online-review.com/2021/06/15/common-data-model-microsoft-power-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://powerplatform.microsoft.com/en-us/common-data-model/

[https://powerplatform.microsoft.com/en-us/common-data-model/](https://powerplatform.microsoft.com/en-us/common-data-model/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Microsoft Dataverse | Microsoft Power Platform
[Microsoft Dataverse | Microsoft Power Platform](https://software-online-review.com/2021/06/15/microsoft-dataverse-microsoft-power-platform/)
[June 15, 2021](https://software-online-review.com/2021/06/15/microsoft-dataverse-microsoft-power-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://powerplatform.microsoft.com/en-us/dataverse/

[https://powerplatform.microsoft.com/en-us/dataverse/](https://powerplatform.microsoft.com/en-us/dataverse/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Business Application Platform | Microsoft Power Platform
[Business Application Platform | Microsoft Power Platform](https://software-online-review.com/2021/06/15/business-application-platform-microsoft-power-platform-2/)
[June 15, 2021](https://software-online-review.com/2021/06/15/business-application-platform-microsoft-power-platform-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://powerplatform.microsoft.com/en-us/

[https://powerplatform.microsoft.com/en-us/](https://powerplatform.microsoft.com/en-us/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Business Central | Microsoft Dynamics 365
[Business Central | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/business-central-microsoft-dynamics-365-2/)
[June 15, 2021](https://software-online-review.com/2021/06/15/business-central-microsoft-dynamics-365-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/business-central/overview/

[https://dynamics.microsoft.com/en-us/business-central/overview/](https://dynamics.microsoft.com/en-us/business-central/overview/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Business Central Pricing | Microsoft Dynamics 365
[Business Central Pricing | Microsoft Dynamics 365](https://software-online-review.com/2021/06/15/business-central-pricing-microsoft-dynamics-365/)
[June 15, 2021](https://software-online-review.com/2021/06/15/business-central-pricing-microsoft-dynamics-365/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dynamics.microsoft.com/en-us/business-central/pricing/

[https://dynamics.microsoft.com/en-us/business-central/pricing/](https://dynamics.microsoft.com/en-us/business-central/pricing/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Small Business Software and Tools – Microsoft Store
[Small Business Software and Tools – Microsoft Store](https://software-online-review.com/2021/06/14/small-business-software-and-tools-microsoft-store/)
[June 14, 2021](https://software-online-review.com/2021/06/14/small-business-software-and-tools-microsoft-store/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.microsoft.com/en-us/store/b/software

[https://www.microsoft.com/en-us/store/b/software](https://www.microsoft.com/en-us/store/b/software)
[software online review](https://software-online-review.com/category/software-online-review/)

### Business Application Platform | Microsoft Power Platform
[Business Application Platform | Microsoft Power Platform](https://software-online-review.com/2021/06/14/business-application-platform-microsoft-power-platform/)
[June 14, 2021](https://software-online-review.com/2021/06/14/business-application-platform-microsoft-power-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://powerplatform.microsoft.com/en-us/

[https://powerplatform.microsoft.com/en-us/](https://powerplatform.microsoft.com/en-us/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Software for Mac – Microsoft Store
[Software for Mac – Microsoft Store](https://software-online-review.com/2021/06/14/software-for-mac-microsoft-store/)
[June 14, 2021](https://software-online-review.com/2021/06/14/software-for-mac-microsoft-store/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.microsoft.com/en-us/store/collections/SoftwareforMac/

[https://www.microsoft.com/en-us/store/collections/SoftwareforMac/](https://www.microsoft.com/en-us/store/collections/SoftwareforMac/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Otter Voice Meeting Notes – Otter.ai
[Otter Voice Meeting Notes – Otter.ai](https://software-online-review.com/2021/06/13/otter-voice-meeting-notes-otter-ai/)
[June 13, 2021](https://software-online-review.com/2021/06/13/otter-voice-meeting-notes-otter-ai/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://otter.ai/

[https://otter.ai/](https://otter.ai/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Bring structure to your research – protocols.io
[Bring structure to your research – protocols.io](https://software-online-review.com/2021/06/10/bring-structure-to-your-research-protocols-io-2/)
[June 10, 2021](https://software-online-review.com/2021/06/10/bring-structure-to-your-research-protocols-io-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.protocols.io/welcome

[https://www.protocols.io/welcome](https://www.protocols.io/welcome)
[software online review](https://software-online-review.com/category/software-online-review/)

### Mollie – Effortless payments
[Mollie – Effortless payments](https://software-online-review.com/2021/06/10/mollie-effortless-payments/)
[June 10, 2021](https://software-online-review.com/2021/06/10/mollie-effortless-payments/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.mollie.com/en

[https://www.mollie.com/en](https://www.mollie.com/en)
[software online review](https://software-online-review.com/category/software-online-review/)

### Buy Autodesk Software | Get Prices & Buy Online | Official Autodesk Store
[Buy Autodesk Software | Get Prices & Buy Online | Official Autodesk Store](https://software-online-review.com/2021/06/08/buy-autodesk-software-get-prices-buy-online-official-autodesk-store/)
[June 8, 2021](https://software-online-review.com/2021/06/08/buy-autodesk-software-get-prices-buy-online-official-autodesk-store/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.autodesk.com/products

[https://www.autodesk.com/products](https://www.autodesk.com/products)
[software online review](https://software-online-review.com/category/software-online-review/)

### WSCAD – Next Generation Electrical CAD
[WSCAD – Next Generation Electrical CAD](https://software-online-review.com/2021/06/08/wscad-next-generation-electrical-cad/)
[June 8, 2021](https://software-online-review.com/2021/06/08/wscad-next-generation-electrical-cad/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.wscad.com/

[https://www.wscad.com/](https://www.wscad.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### AUCOTEC AG – Engineering Software
[AUCOTEC AG – Engineering Software](https://software-online-review.com/2021/06/08/aucotec-ag-engineering-software/)
[June 8, 2021](https://software-online-review.com/2021/06/08/aucotec-ag-engineering-software/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.aucotec.com/en/

[https://www.aucotec.com/en/](https://www.aucotec.com/en/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Bring structure to your research – protocols.io
[Bring structure to your research – protocols.io](https://software-online-review.com/2021/06/03/bring-structure-to-your-research-protocols-io/)
[June 3, 2021](https://software-online-review.com/2021/06/03/bring-structure-to-your-research-protocols-io/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.protocols.io/

[https://www.protocols.io/](https://www.protocols.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Hire Freelancer. Find Remote Jobs & Get Paid Online at Useme.eu | useme.com
[Hire Freelancer. Find Remote Jobs & Get Paid Online at Useme.eu | useme.com](https://software-online-review.com/2021/06/02/hire-freelancer-find-remote-jobs-get-paid-online-at-useme-eu-useme-com/)
[June 2, 2021](https://software-online-review.com/2021/06/02/hire-freelancer-find-remote-jobs-get-paid-online-at-useme-eu-useme-com/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://useme.com/en/

[https://useme.com/en/](https://useme.com/en/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Bamboo
[Bamboo](https://software-online-review.com/2021/06/01/bamboo-2/)
[June 1, 2021](https://software-online-review.com/2021/06/01/bamboo-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.bamboo-cloud.com/

[https://www.bamboo-cloud.com/](https://www.bamboo-cloud.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Drools – Business Rules Management System (Java™, Open Source)
[Drools – Business Rules Management System (Java™, Open Source)](https://software-online-review.com/2021/06/01/drools-business-rules-management-system-java-open-source/)
[June 1, 2021](https://software-online-review.com/2021/06/01/drools-business-rules-management-system-java-open-source/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.drools.org/

[https://www.drools.org/](https://www.drools.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### SocialBee | Social Media Management Tools, Training, and Teams
[SocialBee | Social Media Management Tools, Training, and Teams](https://software-online-review.com/2021/06/01/socialbee-social-media-management-tools-training-and-teams/)
[June 1, 2021](https://software-online-review.com/2021/06/01/socialbee-social-media-management-tools-training-and-teams/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://socialbee.io/

[https://socialbee.io/](https://socialbee.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Documentation | Dataform
[Documentation | Dataform](https://software-online-review.com/2021/06/01/documentation-dataform/)
[June 1, 2021](https://software-online-review.com/2021/06/01/documentation-dataform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://docs.dataform.co/

[https://docs.dataform.co/](https://docs.dataform.co/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Dataform | Manage data pipelines in BigQuery
[Dataform | Manage data pipelines in BigQuery](https://software-online-review.com/2021/06/01/dataform-manage-data-pipelines-in-bigquery/)
[June 1, 2021](https://software-online-review.com/2021/06/01/dataform-manage-data-pipelines-in-bigquery/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://dataform.co/

[https://dataform.co/](https://dataform.co/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Cloud Computing Services | Google Cloud
[Cloud Computing Services | Google Cloud](https://software-online-review.com/2021/06/01/cloud-computing-services-google-cloud-4/)
[June 1, 2021March 20, 2023](https://software-online-review.com/2021/06/01/cloud-computing-services-google-cloud-4/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://cloud.google.com/

[https://cloud.google.com/](https://cloud.google.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Univision
[Univision](https://software-online-review.com/2021/06/01/univision/)
[June 1, 2021](https://software-online-review.com/2021/06/01/univision/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://corporate.univision.com/

[https://corporate.univision.com/](https://corporate.univision.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Create 3D Floor Plans & Interior Designs for Home, Office Online | Foyr
[Create 3D Floor Plans & Interior Designs for Home, Office Online | Foyr](https://software-online-review.com/2021/05/31/create-3d-floor-plans-interior-designs-for-home-office-online-foyr-2/)
[May 31, 2021](https://software-online-review.com/2021/05/31/create-3d-floor-plans-interior-designs-for-home-office-online-foyr-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://foyr.com/

[https://foyr.com/](https://foyr.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Data-Driven Marketing Solutions | Audience Targeting | Social Media & Email Marketing Consultant
[Data-Driven Marketing Solutions | Audience Targeting | Social Media & Email Marketing Consultant](https://software-online-review.com/2021/05/26/data-driven-marketing-solutions-audience-targeting-social-media-email-marketing-consultant/)
[May 26, 2021](https://software-online-review.com/2021/05/26/data-driven-marketing-solutions-audience-targeting-social-media-email-marketing-consultant/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.stirista.com/

[https://www.stirista.com/](https://www.stirista.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Create 3D Floor Plans & Interior Designs for Home, Office Online | Foyr
[Create 3D Floor Plans & Interior Designs for Home, Office Online | Foyr](https://software-online-review.com/2021/05/25/create-3d-floor-plans-interior-designs-for-home-office-online-foyr/)
[May 25, 2021](https://software-online-review.com/2021/05/25/create-3d-floor-plans-interior-designs-for-home-office-online-foyr/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://foyr.com/

[https://foyr.com/](https://foyr.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Amara – Award-winning Subtitle Editor and Enterprise Offerings
[Amara – Award-winning Subtitle Editor and Enterprise Offerings](https://software-online-review.com/2021/05/25/amara-award-winning-subtitle-editor-and-enterprise-offerings/)
[May 25, 2021](https://software-online-review.com/2021/05/25/amara-award-winning-subtitle-editor-and-enterprise-offerings/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://amara.org/en/

[https://amara.org/en/](https://amara.org/en/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Sinch developers
[Sinch developers](https://software-online-review.com/2021/05/25/sinch-developers/)
[May 25, 2021](https://software-online-review.com/2021/05/25/sinch-developers/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://developers.sinch.com/

[https://developers.sinch.com/](https://developers.sinch.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Sinch – SMS, Voice, Video & Verification APIs
[Sinch – SMS, Voice, Video & Verification APIs](https://software-online-review.com/2021/05/25/sinch-sms-voice-video-verification-apis/)
[May 25, 2021](https://software-online-review.com/2021/05/25/sinch-sms-voice-video-verification-apis/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.sinch.com/

[https://www.sinch.com/](https://www.sinch.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Sales Engagement Platform, Sales Automation Software | Outreach
[Sales Engagement Platform, Sales Automation Software | Outreach](https://software-online-review.com/2021/05/24/sales-engagement-platform-sales-automation-software-outreach-3/)
[May 24, 2021](https://software-online-review.com/2021/05/24/sales-engagement-platform-sales-automation-software-outreach-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.outreach.io/

[https://www.outreach.io/](https://www.outreach.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Outreach integrations
[Outreach integrations](https://software-online-review.com/2021/05/24/outreach-integrations/)
[May 24, 2021](https://software-online-review.com/2021/05/24/outreach-integrations/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.outreach.io/product/integrations

[https://www.outreach.io/product/integrations](https://www.outreach.io/product/integrations)
[software online review](https://software-online-review.com/category/software-online-review/)

### Gmail: Secure Enterprise Email for Business | Google Workspace
[Gmail: Secure Enterprise Email for Business | Google Workspace](https://software-online-review.com/2021/05/24/gmail-secure-enterprise-email-for-business-google-workspace-2/)
[May 24, 2021March 20, 2023](https://software-online-review.com/2021/05/24/gmail-secure-enterprise-email-for-business-google-workspace-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://workspace.google.com/products/gmail/

[https://workspace.google.com/products/gmail/](https://workspace.google.com/products/gmail/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Google Workspace (Formerly G Suite): Business Collaboration Tools
[Google Workspace (Formerly G Suite): Business Collaboration Tools](https://software-online-review.com/2021/05/24/google-workspace-formerly-g-suite-business-collaboration-tools-5/)
[May 24, 2021March 20, 2023](https://software-online-review.com/2021/05/24/google-workspace-formerly-g-suite-business-collaboration-tools-5/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://workspace.google.com/

[https://workspace.google.com/](https://workspace.google.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### BeDigital Network
[BeDigital Network](https://software-online-review.com/2021/05/24/bedigital-network/)
[May 24, 2021](https://software-online-review.com/2021/05/24/bedigital-network/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.bedigital.io/

[https://www.bedigital.io/](https://www.bedigital.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Trustpilot Reviews: Experience the power of customer reviews
[Trustpilot Reviews: Experience the power of customer reviews](https://software-online-review.com/2021/05/23/trustpilot-reviews-experience-the-power-of-customer-reviews-2/)
[May 23, 2021](https://software-online-review.com/2021/05/23/trustpilot-reviews-experience-the-power-of-customer-reviews-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.trustpilot.com/

[https://www.trustpilot.com/](https://www.trustpilot.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Axonaut : the best all-in-one CRM
[Axonaut : the best all-in-one CRM](https://software-online-review.com/2021/05/22/axonaut-the-best-all-in-one-crm-3/)
[May 22, 2021](https://software-online-review.com/2021/05/22/axonaut-the-best-all-in-one-crm-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://axonaut.com/en

[https://axonaut.com/en](https://axonaut.com/en)
[software online review](https://software-online-review.com/category/software-online-review/)

### Clustaar Conversational AI – actionable insights from your customers
[Clustaar Conversational AI – actionable insights from your customers](https://software-online-review.com/2021/05/22/clustaar-conversational-ai-actionable-insights-from-your-customers/)
[May 22, 2021](https://software-online-review.com/2021/05/22/clustaar-conversational-ai-actionable-insights-from-your-customers/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://clustaar.com/

[https://clustaar.com/](https://clustaar.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Flowrite – Supercharge your daily communication
[Flowrite – Supercharge your daily communication](https://software-online-review.com/2021/05/22/flowrite-supercharge-your-daily-communication/)
[May 22, 2021](https://software-online-review.com/2021/05/22/flowrite-supercharge-your-daily-communication/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.flowrite.com/

[https://www.flowrite.com/](https://www.flowrite.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Masterworks – Learn to Invest in Fine Art
[Masterworks – Learn to Invest in Fine Art](https://software-online-review.com/2021/05/21/masterworks-learn-to-invest-in-fine-art/)
[May 21, 2021](https://software-online-review.com/2021/05/21/masterworks-learn-to-invest-in-fine-art/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.masterworks.io/trading/bulletin

[https://www.masterworks.io/trading/bulletin](https://www.masterworks.io/trading/bulletin)
[software online review](https://software-online-review.com/category/software-online-review/)

### Freemius – The new standard in selling WordPress plugins and themes
[Freemius – The new standard in selling WordPress plugins and themes](https://software-online-review.com/2021/05/21/freemius-the-new-standard-in-selling-wordpress-plugins-and-themes-3/)
[May 21, 2021](https://software-online-review.com/2021/05/21/freemius-the-new-standard-in-selling-wordpress-plugins-and-themes-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://freemius.com/

[https://freemius.com/](https://freemius.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### abc.xyz na Googleu
[abc.xyz na Googleu](https://software-online-review.com/2021/05/21/abc-xyz-na-googleu/)
[May 21, 2021March 20, 2023](https://software-online-review.com/2021/05/21/abc-xyz-na-googleu/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
Pogledajte taj post tvrtke abc.xyz na Googleu: https://posts.gle/m6MVA9

[https://posts.gle/m6MVA9](https://posts.gle/m6MVA9)
[software online review](https://software-online-review.com/category/software-online-review/)

### Chill
[Chill](https://software-online-review.com/2021/05/21/chill/)
[May 21, 2021](https://software-online-review.com/2021/05/21/chill/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
[software online review](https://software-online-review.com/category/software-online-review/)

### abc.xyz
[abc.xyz](https://software-online-review.com/2021/05/21/abc-xyz/)
[May 21, 2021March 20, 2023](https://software-online-review.com/2021/05/21/abc-xyz/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
abc.xyz 00385992135341

[software online review](https://software-online-review.com/category/software-online-review/)

### Objavite recenziju za abc.xyz na Googleu
[Objavite recenziju za abc.xyz na Googleu](https://software-online-review.com/2021/05/21/objavite-recenziju-za-abc-xyz-na-googleu/)
[May 21, 2021March 20, 2023](https://software-online-review.com/2021/05/21/objavite-recenziju-za-abc-xyz-na-googleu/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
Tvrtka abc.xyz rado bi čula vaše povratne informacije! Objavite recenziju na našem profilu. https://g.page/r/CXJb5DQpP4Q1EA0/review

[https://g.page/r/CXJb5DQpP4Q1EA0/review](https://g.page/r/CXJb5DQpP4Q1EA0/review)
[software online review](https://software-online-review.com/category/software-online-review/)

### Civo Kubernetes – Fast, Simple, Managed Kubernetes Service – Civo.com
[Civo Kubernetes – Fast, Simple, Managed Kubernetes Service – Civo.com](https://software-online-review.com/2021/05/20/civo-kubernetes-fast-simple-managed-kubernetes-service-civo-com/)
[May 20, 2021](https://software-online-review.com/2021/05/20/civo-kubernetes-fast-simple-managed-kubernetes-service-civo-com/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.civo.com/

[https://www.civo.com/](https://www.civo.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### I Was Made For Lovin’ You by Tonight Intro Kiss • A podcast on Anchor
[I Was Made For Lovin’ You by Tonight Intro Kiss • A podcast on Anchor](https://software-online-review.com/2021/05/20/i-was-made-for-lovin-you-by-tonight-intro-kiss-a-podcast-on-anchor/)
[May 20, 2021](https://software-online-review.com/2021/05/20/i-was-made-for-lovin-you-by-tonight-intro-kiss-a-podcast-on-anchor/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://anchor.fm/eight-bukets/episodes/I-Was-Made-For-Lovin-You-e118lpc

[https://anchor.fm/eight-bukets/episodes/I-Was-Made-For-Lovin-You-e118lpc](https://anchor.fm/eight-bukets/episodes/I-Was-Made-For-Lovin-You-e118lpc)
[software online review](https://software-online-review.com/category/software-online-review/)

### I Was Made For Lovin’ You
[I Was Made For Lovin’ You](https://software-online-review.com/2021/05/20/i-was-made-for-lovin-you/)
[May 20, 2021](https://software-online-review.com/2021/05/20/i-was-made-for-lovin-you/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://anchor.fm/eight-bukets/episodes/I-Was-Made-For-Lovin-You-e118lpc

[https://anchor.fm/eight-bukets/episodes/I-Was-Made-For-Lovin-You-e118lpc](https://anchor.fm/eight-bukets/episodes/I-Was-Made-For-Lovin-You-e118lpc)
[software online review](https://software-online-review.com/category/software-online-review/)

### Subscription business financial metrics. Absolutely free.
[Subscription business financial metrics. Absolutely free.](https://software-online-review.com/2021/05/20/subscription-business-financial-metrics-absolutely-free-3/)
[May 20, 2021](https://software-online-review.com/2021/05/20/subscription-business-financial-metrics-absolutely-free-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.profitwell.com/

[https://www.profitwell.com/](https://www.profitwell.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Priceintelligently
[Priceintelligently](https://software-online-review.com/2021/05/20/priceintelligently/)
[May 20, 2021](https://software-online-review.com/2021/05/20/priceintelligently/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.priceintelligently.com/blog

[https://www.priceintelligently.com/blog](https://www.priceintelligently.com/blog)
[software online review](https://software-online-review.com/category/software-online-review/)

### Pricing Strategy Driven by Data
[Pricing Strategy Driven by Data](https://software-online-review.com/2021/05/20/pricing-strategy-driven-by-data/)
[May 20, 2021](https://software-online-review.com/2021/05/20/pricing-strategy-driven-by-data/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.priceintelligently.com/

[https://www.priceintelligently.com/](https://www.priceintelligently.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Integromat – Achieve more in less time with fewer people
[Integromat – Achieve more in less time with fewer people](https://software-online-review.com/2021/05/20/integromat-achieve-more-in-less-time-with-fewer-people/)
[May 20, 2021](https://software-online-review.com/2021/05/20/integromat-achieve-more-in-less-time-with-fewer-people/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.integromat.com/en

[https://www.integromat.com/en](https://www.integromat.com/en)
[software online review](https://software-online-review.com/category/software-online-review/)

### Rise above mundane tasks with our no-code AI platform
[Rise above mundane tasks with our no-code AI platform](https://software-online-review.com/2021/05/20/rise-above-mundane-tasks-with-our-no-code-ai-platform-3/)
[May 20, 2021](https://software-online-review.com/2021/05/20/rise-above-mundane-tasks-with-our-no-code-ai-platform-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://levity.ai/

[https://levity.ai/](https://levity.ai/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Chill • A podcast on Anchor
[Chill • A podcast on Anchor](https://software-online-review.com/2021/05/20/chill-a-podcast-on-anchor/)
[May 20, 2021](https://software-online-review.com/2021/05/20/chill-a-podcast-on-anchor/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://anchor.fm/filip-keser4

[https://anchor.fm/filip-keser4](https://anchor.fm/filip-keser4)
[software online review](https://software-online-review.com/category/software-online-review/)

### Jekyll • Simple, blog-aware, static sites | Transform your plain text into static websites and blogs
[Jekyll • Simple, blog-aware, static sites | Transform your plain text into static websites and blogs](https://software-online-review.com/2021/05/19/jekyll-simple-blog-aware-static-sites-transform-your-plain-text-into-static-websites-and-blogs/)
[May 19, 2021October 24, 2024](https://software-online-review.com/2021/05/19/jekyll-simple-blog-aware-static-sites-transform-your-plain-text-into-static-websites-and-blogs/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://jekyllrb.com/

[https://jekyllrb.com/](https://jekyllrb.com/)
[https://import.jekyllrb.com/docs/wordpress/](https://import.jekyllrb.com/docs/wordpress/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Gatsby | The Speed you Need to Delight Every Customer | Gatsby
[Gatsby | The Speed you Need to Delight Every Customer | Gatsby](https://software-online-review.com/2021/05/19/gatsby-the-speed-you-need-to-delight-every-customer-gatsby/)
[May 19, 2021](https://software-online-review.com/2021/05/19/gatsby-the-speed-you-need-to-delight-every-customer-gatsby/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.gatsbyjs.com/

[https://www.gatsbyjs.com/](https://www.gatsbyjs.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Postach.io | The Evernote Powered Blogging Platform
[Postach.io | The Evernote Powered Blogging Platform](https://software-online-review.com/2021/05/19/postach-io-the-evernote-powered-blogging-platform/)
[May 19, 2021](https://software-online-review.com/2021/05/19/postach-io-the-evernote-powered-blogging-platform/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://postach.io/

[https://postach.io/](https://postach.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### MovableType.org
[MovableType.org](https://software-online-review.com/2021/05/19/movabletype-org/)
[May 19, 2021](https://software-online-review.com/2021/05/19/movabletype-org/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.movabletype.org/

[https://www.movabletype.org/](https://www.movabletype.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Netlify: Develop & deploy the best web experiences in record time
[Netlify: Develop & deploy the best web experiences in record time](https://software-online-review.com/2021/05/19/netlify-develop-deploy-the-best-web-experiences-in-record-time/)
[May 19, 2021](https://software-online-review.com/2021/05/19/netlify-develop-deploy-the-best-web-experiences-in-record-time/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.netlify.com/

[https://www.netlify.com/](https://www.netlify.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### OpenStreetMap
[OpenStreetMap](https://software-online-review.com/2021/05/19/openstreetmap-2/)
[May 19, 2021](https://software-online-review.com/2021/05/19/openstreetmap-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.openstreetmap.org/

[https://www.openstreetmap.org/](https://www.openstreetmap.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Leaflet – a JavaScript library for interactive maps
[Leaflet – a JavaScript library for interactive maps](https://software-online-review.com/2021/05/19/leaflet-a-javascript-library-for-interactive-maps-2/)
[May 19, 2021](https://software-online-review.com/2021/05/19/leaflet-a-javascript-library-for-interactive-maps-2/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://leafletjs.com/

[https://leafletjs.com/](https://leafletjs.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### CARTO | Unlock the power of spatial analysis
[CARTO | Unlock the power of spatial analysis](https://software-online-review.com/2021/05/19/carto-unlock-the-power-of-spatial-analysis-3/)
[May 19, 2021](https://software-online-review.com/2021/05/19/carto-unlock-the-power-of-spatial-analysis-3/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://carto.com/

[https://carto.com/](https://carto.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Gartner Digital Market Contact
[Gartner Digital Market Contact](https://software-online-review.com/2021/05/16/gartner-digital-market-contact/)
[May 16, 2021](https://software-online-review.com/2021/05/16/gartner-digital-market-contact/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.gartner.com/en/digital-markets/get-started

[https://www.gartner.com/en/digital-markets/get-started](https://www.gartner.com/en/digital-markets/get-started)
[software online review](https://software-online-review.com/category/software-online-review/)

### Global Research and Advisory Company | Gartner
[Global Research and Advisory Company | Gartner](https://software-online-review.com/2021/05/16/global-research-and-advisory-company-gartner/)
[May 16, 2021](https://software-online-review.com/2021/05/16/global-research-and-advisory-company-gartner/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.gartner.com/en

[https://www.gartner.com/en](https://www.gartner.com/en)
[software online review](https://software-online-review.com/category/software-online-review/)

### Business Software Reviews from Software Advice®
[Business Software Reviews from Software Advice®](https://software-online-review.com/2021/05/16/business-software-reviews-from-software-advice/)
[May 16, 2021](https://software-online-review.com/2021/05/16/business-software-reviews-from-software-advice/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.softwareadvice.com/

[https://www.softwareadvice.com/](https://www.softwareadvice.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### GetApp | Business Software, Reviews & Comparisons
[GetApp | Business Software, Reviews & Comparisons](https://software-online-review.com/2021/05/16/getapp-business-software-reviews-comparisons/)
[May 16, 2021](https://software-online-review.com/2021/05/16/getapp-business-software-reviews-comparisons/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.getapp.com/

[https://www.getapp.com/](https://www.getapp.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Top Software at Capterra | Software & Software Reviews For Business & Nonprofit
[Top Software at Capterra | Software & Software Reviews For Business & Nonprofit](https://software-online-review.com/2021/05/15/top-software-at-capterra-software-software-reviews-for-business-nonprofit-4/)
[May 15, 2021](https://software-online-review.com/2021/05/15/top-software-at-capterra-software-software-reviews-for-business-nonprofit-4/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.capterra.com/

[https://www.capterra.com/](https://www.capterra.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### High Risk Support, No Reserves, Instant Payouts – MyUser
[High Risk Support, No Reserves, Instant Payouts – MyUser](https://software-online-review.com/2021/05/15/high-risk-support-no-reserves-instant-payouts-myuser/)
[May 15, 2021](https://software-online-review.com/2021/05/15/high-risk-support-no-reserves-instant-payouts-myuser/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.myuser.com/

[https://www.myuser.com/](https://www.myuser.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### TheFunded.com: The Resource for Entrepreneurs.
[TheFunded.com: The Resource for Entrepreneurs.](https://software-online-review.com/2021/05/14/thefunded-com-the-resource-for-entrepreneurs/)
[May 14, 2021](https://software-online-review.com/2021/05/14/thefunded-com-the-resource-for-entrepreneurs/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
http://www.thefunded.com/

[http://www.thefunded.com/](http://www.thefunded.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### InBIA: Global Network of Entrepreneurial Ecosystem Builders InBIA
[InBIA: Global Network of Entrepreneurial Ecosystem Builders InBIA](https://software-online-review.com/2021/05/14/inbia-global-network-of-entrepreneurial-ecosystem-builders-inbia/)
[May 14, 2021](https://software-online-review.com/2021/05/14/inbia-global-network-of-entrepreneurial-ecosystem-builders-inbia/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://inbia.org/

[https://inbia.org/](https://inbia.org/)
[software online review](https://software-online-review.com/category/software-online-review/)

### RAISON – pre-IPO investments from €100
[RAISON – pre-IPO investments from €100](https://software-online-review.com/2021/05/14/raison-pre-ipo-investments-from-e100/)
[May 14, 2021](https://software-online-review.com/2021/05/14/raison-pre-ipo-investments-from-e100/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://raison.ai/

[https://raison.ai/](https://raison.ai/)
[software online review](https://software-online-review.com/category/software-online-review/)

### YC Recommendations | Y Combinator
[YC Recommendations | Y Combinator](https://software-online-review.com/2021/05/14/yc-recommendations-y-combinator/)
[May 14, 2021](https://software-online-review.com/2021/05/14/yc-recommendations-y-combinator/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.ycombinator.com/recommend/

[https://www.ycombinator.com/recommend/](https://www.ycombinator.com/recommend/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Technology Partners | WordPress VIP
[Technology Partners | WordPress VIP](https://software-online-review.com/2021/05/14/technology-partners-wordpress-vip/)
[May 14, 2021](https://software-online-review.com/2021/05/14/technology-partners-wordpress-vip/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://wpvip.com/partners/technology-partners/

[https://wpvip.com/partners/technology-partners/](https://wpvip.com/partners/technology-partners/)
[software online review](https://software-online-review.com/category/software-online-review/)

### WordPress for the Enterprise | WordPress VIP
[WordPress for the Enterprise | WordPress VIP](https://software-online-review.com/2021/05/14/wordpress-for-the-enterprise-wordpress-vip/)
[May 14, 2021](https://software-online-review.com/2021/05/14/wordpress-for-the-enterprise-wordpress-vip/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://wpvip.com/

[https://wpvip.com/](https://wpvip.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Portfolio | FundersClub
[Portfolio | FundersClub](https://software-online-review.com/2021/05/14/portfolio-fundersclub/)
[May 14, 2021October 31, 2022](https://software-online-review.com/2021/05/14/portfolio-fundersclub/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://fundersclub.com/portfolio/

[https://fundersclub.com/portfolio/](https://fundersclub.com/portfolio/)
https://fundersclub.com/

[https://fundersclub.com/](https://fundersclub.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Tools, guides, and resources for startups – Google for Startups
[Tools, guides, and resources for startups – Google for Startups](https://software-online-review.com/2021/05/14/tools-guides-and-resources-for-startups-google-for-startups/)
[May 14, 2021March 20, 2023](https://software-online-review.com/2021/05/14/tools-guides-and-resources-for-startups-google-for-startups/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://startup.google.com/tools/

[https://startup.google.com/tools/](https://startup.google.com/tools/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Best Practices & Helpful Tools for New Startups – Google for Startups
[Best Practices & Helpful Tools for New Startups – Google for Startups](https://software-online-review.com/2021/05/14/best-practices-helpful-tools-for-new-startups-google-for-startups/)
[May 14, 2021March 20, 2023](https://software-online-review.com/2021/05/14/best-practices-helpful-tools-for-new-startups-google-for-startups/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://startup.google.com/

[https://startup.google.com/](https://startup.google.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Y Combinator
[Y Combinator](https://software-online-review.com/2021/05/14/y-combinator/)
[May 14, 2021](https://software-online-review.com/2021/05/14/y-combinator/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://www.ycombinator.com/

[https://www.ycombinator.com/](https://www.ycombinator.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Founder Institute: World’s premier idea-stage accelerator & startup launch program.
[Founder Institute: World’s premier idea-stage accelerator & startup launch program.](https://software-online-review.com/2021/05/14/founder-institute-worlds-premier-idea-stage-accelerator-startup-launch-program/)
[May 14, 2021](https://software-online-review.com/2021/05/14/founder-institute-worlds-premier-idea-stage-accelerator-startup-launch-program/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://fi.co/join

[https://fi.co/join](https://fi.co/join)
[software online review](https://software-online-review.com/category/software-online-review/)

### MicroAcquire – #1 Startup acquisition marketplace
[MicroAcquire – #1 Startup acquisition marketplace](https://software-online-review.com/2021/05/14/microacquire-1-startup-acquisition-marketplace/)
[May 14, 2021](https://software-online-review.com/2021/05/14/microacquire-1-startup-acquisition-marketplace/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://microacquire.com/

[https://microacquire.com/](https://microacquire.com/)
[software online review](https://software-online-review.com/category/software-online-review/)

### Checkaso — ASO Tool | App Store Optimization for iOS & Android
[Checkaso — ASO Tool | App Store Optimization for iOS & Android](https://software-online-review.com/2021/05/14/checkaso-aso-tool-app-store-optimization-for-ios-android/)
[May 14, 2021](https://software-online-review.com/2021/05/14/checkaso-aso-tool-app-store-optimization-for-ios-android/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://checkaso.io/

[https://checkaso.io/](https://checkaso.io/)
[software online review](https://software-online-review.com/category/software-online-review/)

### LiveChat Platform – Chat framework for innovative teams
[LiveChat Platform – Chat framework for innovative teams](https://software-online-review.com/2021/05/13/livechat-platform-chat-framework-for-innovative-teams/)
[May 13, 2021](https://software-online-review.com/2021/05/13/livechat-platform-chat-framework-for-innovative-teams/)
[Filip Keser](https://software-online-review.com/author/fkeser/)
https://developers.livechat.com

[https://developers.livechat.com](https://developers.livechat.com/?mc_cid=890716686c&mc_eid=e109f377b0)

### Posts navigation
[Older posts](https://software-online-review.com/page/2/)
[Follow software info by fk on WordPress.com](https://software-online-review.com)
- ads - analitics - advertising
[ads - analitics - advertising](https://software-online-review.com/ads-analitics/)
- affiliate - partner - reseller
[affiliate - partner - reseller](https://software-online-review.com/affiliate-partner-reseller/)
- all about cookies
[all about cookies](https://software-online-review.com/all-about-cookies/)
- Amazon affiliate program
[Amazon affiliate program](https://software-online-review.com/amazon-affiliate-program/)
- Author.jpg
[Author.jpg](https://software-online-review.com/author-jpg/)
- Auto magazine
[Auto magazine](https://software-online-review.com/auto-magazine/)

### - BUY IT NOW - ESCROW - PROJECT SOR - DOMAIN WITH CONTENT
[BUY IT NOW - ESCROW - PROJECT SOR - DOMAIN WITH CONTENT](https://software-online-review.com/buy-it-now/)
- Companylink Business
[Companylink Business](https://software-online-review.com/companylink-business/)
- Cosmetic & parfumes
[Cosmetic & parfumes](https://software-online-review.com/cosmetic-parfumes/)
- Customer Management System Process Driver
[Customer Management System Process Driver](https://software-online-review.com/customer-management-system-process-driver/)
- design style
[design style](https://software-online-review.com/design-style/)
- draagster - India
[draagster - India](https://software-online-review.com/draagster-2/)
- E&N
[E&N](https://software-online-review.com/en/)
- Fintech bussines card example scheme links
[Fintech bussines card example scheme links](https://software-online-review.com/fintech-bussines-card/)
- gadget
[gadget](https://software-online-review.com/gadget/)
- Game zone
[Game zone](https://software-online-review.com/games/)
- Google search
[Google search](https://software-online-review.com/google/)
- google third party cookies - privacy sandbox - safari dont use third party ... 2023
[google third party cookies - privacy sandbox - safari dont use third party ... 2023](https://software-online-review.com/11249-2/)
- idea to make by fk
[idea to make by fk](https://software-online-review.com/idea-to-make/)
- Informatic magazine
[Informatic magazine](https://software-online-review.com/informatic-magazine/)
- Marketing
[Marketing](https://software-online-review.com/marketing/)
- Music page
[Music page](https://software-online-review.com/music-page/)
- NordVPN
[NordVPN](https://software-online-review.com/nordvpn/)
- notes
[notes](https://software-online-review.com/https-notepad-business-blog/)
- online news & content
[online news & content](https://software-online-review.com/online-news-content/)
- Pilot project
[Pilot project](https://software-online-review.com/pilot-project/)
- software-online-review
[software-online-review](https://software-online-review.com/software-online-review-2/)
- Startup online hiring Scheme links - online & google
[Startup online hiring Scheme links - online & google](https://software-online-review.com/startup-online-hiring-scheme-online/)
- Store
[Store](https://software-online-review.com/store/)
- Study - Courses online
[Study - Courses online](https://software-online-review.com/study-courses-online/)
- Unitedsports News
[Unitedsports News](https://software-online-review.com/unitedsports-news/)
- unofficial
[unofficial](https://software-online-review.com/unofficial-study-of-researchers-graduate-thesis-life-school-of-a-man-with-a-high-school-life-faculty-without-a-diploma-source-google/)
- us-cro-info-news
[us-cro-info-news](https://software-online-review.com/us-cro-info-news/)
- Venture Capital
[Venture Capital](https://software-online-review.com/venture-capital/)
- Web shop us croatia online
[Web shop us croatia online](https://software-online-review.com/web-shop-us-croatia-online/)
- Webshops
[Webshops](https://software-online-review.com/webshops/)
- Wordpress links
[Wordpress links](https://software-online-review.com/wordpress-links/)
- Wordpress Read
[Wordpress Read](https://software-online-review.com/wordpress-read/)
- Wordpress Upgrade
[Wordpress Upgrade](https://software-online-review.com/wordpress-upgrade/)

### Translate


### Search
https://issuu.com/filkes

### Subscribe to Blog via Email
Enter your email address to subscribe to this blog and receive notifications of new posts by email.

Email Address:

### Subscribe
[Follow software info by fk on WordPress.com](https://software-online-review.com)

### Tags
[Academy](https://software-online-review.com/tag/academy/)
[AD](https://software-online-review.com/tag/ad/)
[ADS](https://software-online-review.com/tag/ads/)
[affiliate](https://software-online-review.com/tag/affiliate/)
[ai](https://software-online-review.com/tag/ai/)
[analytics](https://software-online-review.com/tag/analytics/)
[app](https://software-online-review.com/tag/app/)
[artificial-intelligence](https://software-online-review.com/tag/artificial-intelligence/)
[audience](https://software-online-review.com/tag/audience/)
[automating](https://software-online-review.com/tag/automating/)
[automation](https://software-online-review.com/tag/automation/)
[bussines](https://software-online-review.com/tag/bussines/)
[call Center](https://software-online-review.com/tag/call-center/)
[center](https://software-online-review.com/tag/center/)
[chatgpt](https://software-online-review.com/tag/chatgpt/)
[CLICK](https://software-online-review.com/tag/click/)
[cloud](https://software-online-review.com/tag/cloud/)
[customer](https://software-online-review.com/tag/customer/)
[data](https://software-online-review.com/tag/data/)
[database](https://software-online-review.com/tag/database/)
[data privacy software](https://software-online-review.com/tag/data-privacy-software/)
[Discovery](https://software-online-review.com/tag/discovery/)
[elastic](https://software-online-review.com/tag/elastic/)
[email](https://software-online-review.com/tag/email/)
[enterprise](https://software-online-review.com/tag/enterprise/)
[gemini](https://software-online-review.com/tag/gemini/)
[go](https://software-online-review.com/tag/go/)
[golang](https://software-online-review.com/tag/golang/)
[Google](https://software-online-review.com/tag/google/)
[iintegrations](https://software-online-review.com/tag/iintegrations/)
[integrations](https://software-online-review.com/tag/integrations/)
[internet](https://software-online-review.com/tag/internet/)
[java](https://software-online-review.com/tag/java/)
[joomla](https://software-online-review.com/tag/joomla/)
[kibana](https://software-online-review.com/tag/kibana/)
[language](https://software-online-review.com/tag/language/)
[link](https://software-online-review.com/tag/link/)
[localisation](https://software-online-review.com/tag/localisation/)
[m](https://software-online-review.com/tag/m/)
[management](https://software-online-review.com/tag/management/)
[marketing](https://software-online-review.com/tag/marketing/)
[monitoring](https://software-online-review.com/tag/monitoring/)
[news](https://software-online-review.com/tag/news/)
[officecrm](https://software-online-review.com/tag/officecrm/)
[online](https://software-online-review.com/tag/online/)
[Oracle](https://software-online-review.com/tag/oracle/)
[planing](https://software-online-review.com/tag/planing/)
[platform](https://software-online-review.com/tag/platform/)
[play](https://software-online-review.com/tag/play/)
[product](https://software-online-review.com/tag/product/)
[program](https://software-online-review.com/tag/program/)
[programing](https://software-online-review.com/tag/programing/)
[projects](https://software-online-review.com/tag/projects/)
[real estate](https://software-online-review.com/tag/real-estate/)
[Sales](https://software-online-review.com/tag/sales/)
[sap](https://software-online-review.com/tag/sap/)
[School of Hard Knocks](https://software-online-review.com/tag/school-of-hard-knocks/)
[server](https://software-online-review.com/tag/server/)
[shopify](https://software-online-review.com/tag/shopify/)
[SMS](https://software-online-review.com/tag/sms/)
[software](https://software-online-review.com/tag/software/)
[speech](https://software-online-review.com/tag/speech/)
[sql](https://software-online-review.com/tag/sql/)
[storage](https://software-online-review.com/tag/storage/)
[suite](https://software-online-review.com/tag/suite/)
[system](https://software-online-review.com/tag/system/)
[technology](https://software-online-review.com/tag/technology/)
[text](https://software-online-review.com/tag/text/)
[URL](https://software-online-review.com/tag/url/)
[virtual machines](https://software-online-review.com/tag/virtual-machines/)
[visitor](https://software-online-review.com/tag/visitor/)
[vizalize](https://software-online-review.com/tag/vizalize/)
[vode](https://software-online-review.com/tag/vode/)
[web](https://software-online-review.com/tag/web/)
[WordPress](https://software-online-review.com/tag/wordpress/)

### - BUY IT NOW – ESCROW – PROJECT SOR – DOMAIN WITH CONTENT
[BUY IT NOW – ESCROW – PROJECT SOR – DOMAIN WITH CONTENT](https://software-online-review.com/buy-it-now/)
[Create a website or blog at WordPress.com](https://wordpress.com/?ref=footer_custom_svg)

### software info by fk
software-online-review - Filip Keser

Type your email…

### Subscribe
Skip to content ↓

[Skip to content ↓](https://software-online-review.com)
[Cookie Policy](https://automattic.com/cookies/)
- Subscribe Subscribed software info by fk Join 149 other subscribers Sign me up Already have a WordPress.com account? Log in now.
- software info by fk
[software info by fk](https://software-online-review.com)
- Already have a WordPress.com account? Log in now.
[Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fsoftware-online-review.com%252F2025%252F11%252F01%252Froadmap-and-business-roadmap%252F)
- software info by fk Subscribe Subscribed Sign up Log in Report this content View site in Reader Manage subscriptions Collapse this bar
- software info by fk
[software info by fk](https://software-online-review.com)
- Subscribe Subscribed
- Sign up
[Sign up](https://wordpress.com/start/)
- Log in
[Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fsoftware-online-review.com%252F2025%252F11%252F01%252Froadmap-and-business-roadmap%252F)
- Report this content
[Report this content](https://wordpress.com/abuse/?report_url=https://software-online-review.com)
- View site in Reader
[View site in Reader](https://wordpress.com/reader/feeds/126324357)
- Manage subscriptions
[Manage subscriptions](https://subscribe.wordpress.com/)
- Collapse this bar

---
