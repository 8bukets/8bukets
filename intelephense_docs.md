# Intelephense Documentation

Scraped from [https://intelephense.com/docs](https://intelephense.com/docs)

## Getting Started

About Intelephense is a high performance, cross platform, cross editor PHP language server adhering to the Language Server Protocol (LSP) . When paired with an LSP capable editor it provides an essential set of code tools, making for
                                    a productive and rich PHP coding experience. The Intelephense server is proprietary software released to end users under a "freemium" model.
                                    Many of the features are provided free of charge.
                                    Access to premium features can be obtained by purchasing a licence key .

Installation Visual Studio Code Visual Studio Code users should install the Intelephense extension from within the extensions view
                                    or download it from the VSCode marketplace . The built-in VSCode PHP Language Features extension can cause excessive completion suggestions that are out of context and is best disabled.
                                    Go to the Extensions UI and search for PHP Language Features to disable it.
                                    Alternatively, you can disable parts of it via it's configuration settings .
                                    Other third party extensions that provide similar functionality to Intelephense may also need to be disabled for best results. Optionally purchase and enter your licence key by opening the command palette
                                    -- CTRL + SHIFT + P -- and searching for Enter licence key . Other Editors Intelephense requires a Node.js runtime environment.
                                    It is recommended that you use a current LTS version of Node.js. To install Intelephense server you can use npm. npm i intelephense -g Intelephense needs an LSP compliant client to communicate with and integrate features into the editor.
                                    A list of editors and clients that support the LSP can be found here .
                                    Please follow the setup guide of the relevant tool. The information below may help in configuring the client. To start the intelephense server: intelephense {transport} Where {transport} is one of: --node-ipc --stdio --socket={number} --pipe={string} If your LSP client exposes initializationOptions , then the following values are accepted: interface InitialisationOptions {
    // Optional absolute path to storage directory.
    // Defaults to $TEMPDIR, $TMP, or $TEMP on *nix and %TEMP% or %TMP% on Windows.
    storagePath?: string;

    // Optional absolute path to a global storage dir.
    // Defaults to $HOME on *nix and %USERPROFILE% on Windows.
    globalStoragePath?: string;

    //Optional licence key or absolute path to a text file containing the licence key.
    licenceKey?: string;

    //Optional flag to clear server state.
    //State can also be cleared by deleting {storagePath}/intelephense
    clearCache?: boolean;
} If your LSP client does not expose initializationOptions then a licence key can
                                    be provided by placing (only) the key in a text file at $HOME/intelephense/licence.txt on *nix
                                    or %USERPROFILE%/intelephense/licence.txt on Windows.

Configuration Please see the VSCode client package.json configuration property for a full list of configuration options and associated json schema.
                                    Note that the configuration keys are given in dot notation.
                                    That is, the server expects the client to send, for example, intelephense.files.exclude as {"intelephense": {"files": {"exclude": []}}} . In VSCode, the settings UI can be used to modify the configuration values.
                                    For other LSP clients, please see the client documentation on how to modify these values.
                                    Intelephense supports the LSP workspace/didChangeConfiguration and workspace/configuration methods as a way of supplying configuration values to the server.

Best Practice Providing type information in your PHP code will result in a better experience when using Intelephense.
                                    Type information can be provided via coded type declarations or PHPDoc type annotations .
                                    Where both have been provided, PHPDoc type annotations are given precedence as they can provide more detailed type information. <?php

/**
 * @param string $s  <- A phpdoc parameter type annotation
 * @return string[] <- A phpdoc return type annotation with detail on the array element type
 **/
function foo(string $s): array {} // <- type declarations for $s (string) and function return (array) For Intelephense to work effectively it must have access to the definitions of the symbols used in your code.
                                    Opening a project folder rather than individual files enables these symbols to be discovered by Intelephense via indexing the PHP files in the folder.
                                    Intelephense currently has a limitation of 262143 PHP files.
                                    Large workspaces require more system resources.
                                    Consider opening a smaller workspace or exclude unnecessary files via the intelephense.files.exclude setting to reduce resource usage.

## Installation

### Visual Studio Code

Visual Studio Code users should install the Intelephense extension from within the extensions view
                                    or download it from the VSCode marketplace .

The built-in VSCode PHP Language Features extension can cause excessive completion suggestions that are out of context and is best disabled.
                                    Go to the Extensions UI and search for PHP Language Features to disable it.
                                    Alternatively, you can disable parts of it via it's configuration settings .
                                    Other third party extensions that provide similar functionality to Intelephense may also need to be disabled for best results.

Optionally purchase and enter your licence key by opening the command palette
                                    -- CTRL + SHIFT + P -- and searching for Enter licence key .

### Other Editors

Intelephense requires a Node.js runtime environment.
                                    It is recommended that you use a current LTS version of Node.js. To install Intelephense server you can use npm.

```php
npm i intelephense -g
```

Intelephense needs an LSP compliant client to communicate with and integrate features into the editor.
                                    A list of editors and clients that support the LSP can be found here .
                                    Please follow the setup guide of the relevant tool. The information below may help in configuring the client.

To start the intelephense server:

```php
intelephense {transport}
```

Where {transport} is one of:

--node-ipc --stdio --socket={number} --pipe={string}

If your LSP client exposes initializationOptions , then the following values are accepted:

```php
interface InitialisationOptions {
    // Optional absolute path to storage directory.
    // Defaults to $TEMPDIR, $TMP, or $TEMP on *nix and %TEMP% or %TMP% on Windows.
    storagePath?: string;

    // Optional absolute path to a global storage dir.
    // Defaults to $HOME on *nix and %USERPROFILE% on Windows.
    globalStoragePath?: string;

    //Optional licence key or absolute path to a text file containing the licence key.
    licenceKey?: string;

    //Optional flag to clear server state.
    //State can also be cleared by deleting {storagePath}/intelephense
    clearCache?: boolean;
}
```

If your LSP client does not expose initializationOptions then a licence key can
                                    be provided by placing (only) the key in a text file at $HOME/intelephense/licence.txt on *nix
                                    or %USERPROFILE%/intelephense/licence.txt on Windows.

## Configuration

Please see the VSCode client package.json configuration property for a full list of configuration options and associated json schema.
                                    Note that the configuration keys are given in dot notation.
                                    That is, the server expects the client to send, for example, intelephense.files.exclude as {"intelephense": {"files": {"exclude": []}}} .

In VSCode, the settings UI can be used to modify the configuration values.
                                    For other LSP clients, please see the client documentation on how to modify these values.
                                    Intelephense supports the LSP workspace/didChangeConfiguration and workspace/configuration methods as a way of supplying configuration values to the server.

## Best Practice

Providing type information in your PHP code will result in a better experience when using Intelephense.
                                    Type information can be provided via coded type declarations or PHPDoc type annotations .
                                    Where both have been provided, PHPDoc type annotations are given precedence as they can provide more detailed type information.

```php
<?php

/**
 * @param string $s  <- A phpdoc parameter type annotation
 * @return string[] <- A phpdoc return type annotation with detail on the array element type
 **/
function foo(string $s): array {} // <- type declarations for $s (string) and function return (array)
```

For Intelephense to work effectively it must have access to the definitions of the symbols used in your code.
                                    Opening a project folder rather than individual files enables these symbols to be discovered by Intelephense via indexing the PHP files in the folder.
                                    Intelephense currently has a limitation of 262143 PHP files.
                                    Large workspaces require more system resources.
                                    Consider opening a smaller workspace or exclude unnecessary files via the intelephense.files.exclude setting to reduce resource usage.

## Type System

Intelephense will make use of declared types, documented types and inferred types when providing language intelligence.

Declared types are provided through standard PHP syntax. For example:

```php
function toString(object $obj): string {}
```

Documented types are provided through PHPDoc annotations.
                                Where both a documented type and declared type are provided,
                                Intelephense will prefer the documented type.
                                This is because richer type information can be provided via documented types (e.g. generics, typed arrays).
                                Providing declared or documented types improves the performance and the quality of language intelligence.

Inferred types are computed by intelephense and will be done so when a declared or documented type is not found or during control flow analysis.
                                When a type is inferred it may be reduced to it's minimal representation.
                                For example, MyClass|object would become just object because MyClass is a subtype of object .

Intelephense currently only type checks declared types and will emit diagnostics if there is a type error.
                                In a hierarchy of types, a subtype can be assigned to a supertype constraint.
                                By default, Intelephense also permits the reverse.
                                That is, a supertype or wider type can be assigned to a subtype or narrower type constraint.
                                This behaviour was implemented due to the lack of syntax in PHP or PHPDoc to enable a developer to inline cast an expression or variable.
                                To make type checks more thorough,
                                this behaviour can be switched off by setting intelephense.diagnostics.relaxedTypeCheck to false .

Some of the types listed below can only be used in PHPDoc as documented types.
                                Please see the PHP type system documentation if you are unfamiliar with the standard PHP types.

Additional types used in other static analysis engines that are not listed here are not fully supported.
                                Intelephense attempts to fallback to an appropriate alternative in this situation.

### Top Type

mixed

The supertype of all types.
                                Any other type can be assigned to a type constraint of mixed .
                                If intelephense cannot determine a more specific type for a symbol or expression then this is the type it is given.
                                Because of this, Intelephense also allows mixed to be assigned to any other type constraint as well,
                                effectively turning off type checking for that particular symbol or expression.
                                To switch off this behaviour you can set both intelephense.diagnostics.relaxedTypeCheck and intelephense.diagnostics.noMixedTypeCheck to false .

### Bottom Type

never

The subtype of all types.
                                This type can be assigned to any other type constraint.
                                It is used to represent an impossibility in the code and can be used as the return type of a function that exits or always throws an exception.

### Scalar Types

Any of these types can be assigned to the other unless the declare(strict_types=1) directive is used in the file.

int float bool string

### Unit Types

void null true false unset Intelephense uses this PHP keyword as the type of an undefined variable.

### Literal Types

'myString' String literals are encapsulated in quotes. 9 An integer literal.

### Object Types

object \MyNs\MyClass Classes, interfaces, trait, enums can be fully qualified or not.
                                    If not fully qualified then the standard PHP name resolution rules apply to determine the fully qualified name. object{name: string, optional?: string} Object shapes can be used to provide further information on dynamic object properties.
                                    This improves completion suggestions and type inference when accessing these properties. Optional properties can be declared by adding a ? at the end of the name. static self $this

### Array Types

array array<TKey, TValue> Generic form for an array where the type arguments represent the array key and value types respectively.
                                    If only a single type argument is provided then it will be normalised to array<string|int, TValue> . TValue[] Represents a numeric indexed array where the element type is TValue . array{name: string, 'height (cm)': float, optional?: string, ...<int, string>} Array shapes can be used to provide further information on array element keys and types.
                                    This improves completion suggestions and type inference when accessing these elements.
                                    Keys with non alphanumeric characters need to be in quotes.
                                    Optional keys can be declared by adding a ? at the end of the key.
                                    Unspecified extra elements can be declared by adding an element of form ...<TKey, TValue> .
                                    Keys are optional and default to numerically indexed.
                                    For example a two element tuple would be array{Type0, Type1} .
                                    A mix of keyed and unkeyed elements is not supported.

### Callable Types

callable Base callable type that represents a callable string , callable array or a class that implements __invoke . callable(TParamA $a, TParamB $b): TReturn Callable type signatures can be defined to improve language intelligence.
        Parameter names are optional.
        The callable type should be wrapped in parentheses if it forms part of a union. Closure can be used instead of callable for a more specific type.

### Alias Types

iterable Alias for Traversable|array . ?A Nullable type that is shorthand for null|A . Cannot be used as part of a union or intersection type.

### Union Types

A|B|C

A type which may have multiple atomic type representations.
    For example, a type constraint of A|B can be assigned type A or B .

### Intersection Types

A&B&C

A composite type which consists of multiple atomic types.
    For example, a type of A&B can be assigned to type A and to type B .

### DNF Types

A|B|(C&D&E)

When combining union and intersection types, only a single level of nesting is permitted. The union must be the top level.

### Generic Types

MyType<TypeArg1, TypeArg2>

A generic type can be declared using one or many @template PHPDoc annotations above the target class.
    Type arguments can then be supplied in the same order as the @template declarations.
    The following built-in types are templated:

iterable<TKey, TValue> Traversable<TKey, TValue> array<TKey, TValue> Iterator<TKey, TValue> IteratorAggregate<TKey, TValue> ArrayAccess<TKey, TValue> WeakReference<TObject> WeakMap<TKey, TValue> Fiber<TStart, TResume, TReturn, TSuspend> DatePeriod<TDate, TEnd> ReflectionAttribute<TObject> ReflectionClass<TObject> Generator<TKey, TYield, TSend, TReturn> ArrayObject<TKey, TValue> SplDoublyLinkedList<TValue> SplQueue<TValue> SplStack<TValue> SplHeap<TValue> SplMinHeap<TValue> SplMaxHeap<TValue> SplPriorityQueue<TPriority, TValue> SplFixedArray<TValue> SplObjectStorage<TObject, TValue>

### Conditional Return Type

(TSubject is TCompare ? TTrue : TFalse)

Sometimes the return type of a function may depend on the type of a parameter.
    A conditional type can be used without templates too by using the parameter name.
    For example, ($myParam is string ? string : null) .
    Conditional types must be wrapped in parentheses. Conditional types may also be nested.

### Array Key Type

key-of<TArray>

This type will resolve to a union of the keys of an array shape.

### Index Access Type

TArray[TKey]

This type will resolve to the type of the value at index TKey in TArray .
    It is particularly useful in conjunction with key-of<TArray> and shape types for mapping the return type when accessing container items with arbitrary strings. For example:

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

### Miscellaneous Types

resource class-string<T> A string where the value is the name of class T .

## Frameworks and Libraries

Intelephense aims to support all PHP frameworks and libraries but does not implement specific solutions for these.
                                    Limited or unexpected language intelligence can sometimes be provided if the package:

Declares symbols at runtime via bootstrapping code or configuration. Uses interfaces heavily but encourages calling methods only declared on implementations. Uses __get , __call , or __callStatic magic heavily. Has insufficient or incorrect type declarations/annotations.

In such cases you may notice lack of completion suggestions,
                                    trouble jumping to definitions or undefined symbol diagnostics may appear even though the code may work when executed.

For example, a common problem can be when a framework returns an interface from a function but the project has been
                                    bootstrapped to use a particular concrete type that has additional methods not declared on the interface.

```php
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
```

There are several ways to workaround the problem above.
                                    These workarounds can fall into two categories.
                                    Either they become part of the project executable code itself,
                                    or they are declared in a non-executable helper file and are there only to override the default Intelephense behaviour.

### Solutions that form part of the executable code

The advantage here is that problems in the code would become more apparent
                                    if the bootstrapping logic ever changed and returned a different class.
                                    The disadvantage is it is more code to write and perhaps difficult to retrofit to existing code.

```php
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
```

### Solutions that do not form part of the project executable code

This involves creating a file with alternate symbol declarations and placing
                                    it in your workspace folder (not in vendor ).
                                    Intelephense will prioritise user declared symbols over vendor declared symbols.

The advantage here is that it can be retrofitted easily to existing code,
                                    applies to all usages of the symbol and executable code remains untouched.
                                    The disadvantage is that it could suppress an actual error that Intelephense would otherwise detect.

```php
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
```

If classes, interfaces, traits, or enums have override definitions then
                                    Intelephense will treat them as partial types and merge them with the vendor declared types.
                                    Type overrides should either not use extends or implements clauses, or,
                                    alternatively keep them the same as the real type because implements and extends values are not merged.

There are also packages that provide or generate IDE helper files that may
                                    improve the experience when using various frameworks and libraries. For example:

laravel-ide-helper
