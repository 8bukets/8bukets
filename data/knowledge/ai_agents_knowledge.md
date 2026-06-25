# Knowledge Observation Insights (Unified)

**System Analysis:** 2026-06-25T14:29:26.093Z

---

# Phase 19

## Test
heartbeat latency < 2ms

---

# iCloud: phase_19_sovereign_swarm.md

> **Source:** icloud://phase_19_sovereign_swarm.md
> **Analyzed At:** 2026-06-23T03:19:18.131Z

## Phase 19 Sovereign Swarm Evolution
- Recursive self-improvement loops: ACTIVE
- Zero-knowledge proof (ZKP) based trust: VERIFIED
- Heartbeat latency: < 2ms (Target: 1.5ms)
- Cross-shard neural recovery: ENABLED
- Strategic mandate: Total sovereignty via decentralized orchestration.
- Signature: SHA256:SovereignSwarmTrustVerified2026

---

# Intelephense Documentation

> **Source:** https://github.com/bmewburn/intelephense-docs
> **Analyzed At:** 2026-06-25T14:29:26.064Z

## Intelephense
Intelephense is a high performance, cross platform PHP language server adhering to the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/).
When paired with an LSP capable editor it provides an essential set of code intelligence features that give a PHP developer a productive and rich editing experience.
This is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to all current and future features can be obtained by purchasing a licence key at https://intelephense.com.

## Workspace
For Intelephense to work effectively it must have access to the definitions of the symbols used in your code. It does this by scanning the php files found in the workspace. Sometimes PHP files may have a non standard extension. It is important to associate these extensions with PHP using the `intelephense.files.associations` configuration option.
intelephense.files.associations
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
You may have large files in your workspace that by default Intelephense will skip. You can configure the maximum file size with the `intelephense.files.maxSize` option.
intelephense.files.maxSize
```json
{
    "type": "number",
    "default": 1000000,
    "description": "Maximum file size in bytes.",
    "scope": "window"
}
```
There may be files you do not want to indexed by Intelephense. It is important in large projects to exclude unnecessary files to avoid polluting suggestion lists and degrading performance.
intelephense.files.exclude
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

## Environment
Sometimes symbol definitions are not in your workspace but are core PHP symbols or defined in an extension. For this reason Intelephense includes stub definitions for many of these. Extensions that are bundled with PHP are enabled by default. You can configure what other symbols are available in your environment with the `intelephense.stubs` option.
intelephense.stubs
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
Other configuration settings that allow you to further define the PHP environment include:
intelephense.environment.documentRoot
```json
{
    "type": "string",
    "description": "The directory of the entry point to the application (index.php).Defaults to the first workspace folder. Used for resolving script inclusion.",
    "scope": "window"
}
```
intelephense.environment.includePaths
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
intelephense.environment.phpVersion
```json
{
    "type": "string",
    "default": "7.4.0",
    "description": "A semver compatible string that represents the target PHP version.Used for providing version appropriate suggestions and diagnostics. PHP 5.3.0 andgreater supported.",
    "scope": "window"
}
```
intelephense.environment.shortOpenTag
```json
{
    "type": "boolean",
    "default": false,
    "description": "When enabled '<?' will be parsed as a PHP open tag. Defaults tofalse.",
    "scope": "window"
}
```

## Type Declarations and Annotations
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
intelephense.compatibility.correctForBaseClassStaticUnionTypes
```json
{
    "type": "boolean",
    "default": true,
    "description": "Resolves `BaseClass|static` union types to `static` instead of `BaseClass`.",
    "scope": "window"
}
```
intelephense.compatibility.correctForArrayAccessArrayAndTraversableArrayUnionTypes
```json
{
    "type": "boolean",
    "default": true,
    "description": "Resolves `ArrayAccess` and `Traversable` implementations that are unionedwith a typed array to generic syntax. eg `ArrayAccessOrTraversable|ElementType[]` =>`ArrayAccessOrTraversable<mixed, ElementType>`.",
    "scope": "window"
}
```
You may also see several non standard types in hovers.
* `unset` - the type given to variables that are undefined or `unset()`.
* `never` - the type returned from a function that does not terminate normally (eg `die()`) or that represents an impossibility (added in PHP 8.1).

## Framework Support
Intelephense aims to support all frameworks but does not implement framework specific solutions. Some frameworks are coded in a way that make it difficult to analyse. This may be because of lack of type declarations/annotations; heavy use of `__get`, `__set`, `__call`, `__callStatic` magic methods; or dynamic generation of class aliases at runtime.
Packages can be found online that aim to workaround these issues by providing stubs of symbols to help static analysers like Intelephense understand the code.
* Laravel - [barryvdh/laravel-ide-helper](https://github.com/barryvdh/laravel-ide-helper)

## Visual Studio Code
Visual Studio Code users should install the Intelephense extension from within the extensions view or download it from the VSCode marketplace.
The built-in VSCode PHP Language Features extension can cause excessive completion suggestions that are out of context and is best disabled. Go to the Extensions UI and search for PHP Language Features to disable it. Alternatively, you can disable parts of it via it's configuration settings. Other third party extensions that provide similar functionality to Intelephense may also need to be disabled for best results.
Optionally purchase and enter your licence key by opening the command palette (Ctrl+Shift+P) and searching for Enter licence key.
![Entering a licence key via the VS Code command palette](https://intelephense.com/img/license_key.png)
*Entering a licence key via the VS Code command palette*

## Requirements
[Node.js 12+](https://nodejs.org)

## Server Installation
```
npm i intelephense -g
```

## Language Server Protocol (LSP) Client
Intelephense needs an LSP compliant client to communicate with and integrate features into the editor. A list of editors and clients that support the LSP can be found at https://microsoft.github.io/language-server-protocol/implementors/tools/.
Please follow the setup guide of the relevant tool. The Information below may help in configuring the client.

## Run
```
intelephense {transport}
```
Where `{transport}` is one of:
* `--node-ipc`
* `--stdio`
* `--socket={number}`
* `--pipe={string}`

## Initialisation Options
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

## Capabilities
Server capabilities JSON returned from `initialize` request.
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

## Configuration Options
JSON schema for `workspace/configuration` request data
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

## About
Intelephense is a high performance, cross platform, cross editor PHP language server adhering to the Language Server Protocol (LSP).
When paired with an LSP capable editor it provides an essential set of code tools, making for a productive and rich PHP coding experience.
The Intelephense server is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to premium features can be obtained by purchasing a licence key.

## Other Editors
Intelephense requires a Node.js runtime environment. It is recommended that you use a current LTS version of Node.js. To install Intelephense server you can use npm.
```bash
npm i intelephense -g
```
Intelephense needs an LSP compliant client to communicate with and integrate features into the editor. A list of editors and clients that support the LSP can be found [here](https://microsoft.github.io/language-server-protocol/implementors/editors/). Please follow the setup guide of the relevant tool. The information below may help in configuring the client.
To start the intelephense server:
```bash
intelephense {transport}
```
Where {transport} is one of:
- `--node-ipc`
- `--stdio`
- `--socket={number}`
- `--pipe={string}`
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
| *nix | storagePath | $XDG_CONFIG_HOME/intelephense/workspace/ | $HOME/.config/intelephense/workspace/ |
| *nix | globalStoragePath | $XDG_CONFIG_HOME/intelephense/global/ | $HOME/.config/intelephense/global/ |
| *nix | licenceKey | {globalStoragePath}/licence.txt | {globalStoragePath}/license.txt |
| Windows | storagePath | %AppData%/intelephense/workspace/ | %UserProfile%/intelephense/workspace/ |
| Windows | globalStoragePath | %AppData%/intelephense/global/ | %UserProfile%/intelephense/global/ |
| Windows | licenceKey | {globalStoragePath}/licence.txt | {globalStoragePath}/license.txt |
If your LSP client does not expose `initializationOptions` then a licence key can be provided by placing (only) the key in a text file at the default `licenceKey` path listed above.

## Configuration
Please see the VSCode client package.json configuration property for a full list of configuration options and associated JSON schema. Note that the configuration keys are given in dot notation. As an example, the equivalent JSON object for `intelephense.files.exclude` would be `{"intelephense": {"files": {"exclude": []}}}`.
Intelephense attempts to provide reasonable defaults for all settings. Some of the more important settings to consider when getting started include:
- `intelephense.files.associations` - File globs that identify PHP files. Defaults to standard PHP file extensions e.g. `*.php`.
- `intelephense.files.maxSize` - Maximum file size in bytes to index and provide analysis for. Defaults to `1000000` (1MB).
- `intelephense.environment.phpVersion` - PHP version to use for analysis. Defaults to the most recent stable PHP version.
- `intelephense.stubs` - List of stubs to include. Defaults to core symbols and extensions that are bundled with PHP. If you are getting undefined symbols for built-in or PECL extensions, you may need to modify this list.
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
Intelephense will also compute inferred types when a declared or documented type is not found or during control flow analysis. When a type is inferred it may be reduced to it's minimal representation. For example, `MyClass|object` would become `object` because `MyClass` is a sub-type of `object`.
Intelephense provides limited support for PHPStorm metadata as a way of overriding or supplementing type information. It is recommended to use PHPDoc type annotations instead of PHPStorm metadata where possible as they are more widely supported across different tools. Support for PHPStorm metadata may be removed in future releases. Please see the PHPDoc Instead of PHPStorm Metadata/Attributes section in the appendix for more information.

## Type Narrowing
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

## Type Evolving
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

## Supported Types
In the list of supported types below, some can only be used in PHPDoc as documented types. Please see the PHP type system documentation if you are unfamiliar with the standard PHP types. PHPDoc only, or internal types, are flagged with an asterisk.
Additional types used in other static analysis engines that are not listed here are not fully supported. Intelephense attempts to fallback to an appropriate alternative in this situation.

## Top Type
- `mixed`: The super-type of all types. Any other type can be assigned to a type constraint of mixed. If intelephense cannot determine a more specific type for a symbol or expression then this is the type it is given. Because of this, Intelephense also allows mixed to be assigned to any other type constraint as well, effectively turning off type checking for that instance. To switch off this behaviour you can set both `intelephense.diagnostics.relaxedTypeCheck` and `intelephense.diagnostics.noMixedTypeCheck` to `false`.

## Bottom Type
- `never`: The sub-type of all types. This type can be assigned to any other type constraint. It is used to represent an impossibility in the code and can be used as the return type of a function that exits or always throws an exception.

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
- `unset`* Intelephense uses this PHP keyword to represent the type of an undefined variable.

## Literal Types
- `'myString'`* String literals are encapsulated in quotes.
- `9`* An integer literal.

## Object Types
- `object`
- `\MyNs\MyClass`: Classes, interfaces, traits, and enums can be fully qualified or not. If not fully qualified then the standard PHP name resolution rules apply to determine the fully qualified name.
- `object{name: string, optional?: string}`* Object shapes can be used to provide further information on dynamic object properties. This improves completion suggestions and type inference when accessing these properties. Optional properties can be declared by adding a `?` at the end of the name.
- `static`
- `self`
- `$this`*

## Array Types
- `array`
- `array<TKey, TValue>`* Generic form for an array where the type arguments represent the array key and value types respectively. If only a single type argument is provided then it will be normalised to `array<string|int, TValue>`.
- `TValue[]`* Represents a numeric indexed array where the element type is `TValue`.
- `array{description: string, 'length (cm)': float, optional?: string, ...<int, string>}`* Array shapes can be used to provide further information on array element keys and value types. This improves completion suggestions and type inference when accessing these elements. Keys with non alphanumeric characters need to be in quotes. Optional keys can be declared by adding a `?` at the end of the key. Unspecified extra elements can be declared by adding an element of form `...<TKey, TValue>`. Keys are optional and default to numerically indexed. For example a two element tuple would be `array{Type0, Type1}`. A mix of keyed and unkeyed elements is not supported.

## Callable Types
- `callable`: Base callable type that represents a callable string, callable array or a class that implements `__invoke`.
- `callable(TParamA $a, TParamB $b): TReturn`* Callable type signatures can be defined to improve language intelligence. Parameter names are optional. The callable type should be wrapped in parentheses if it forms part of a union. `Closure` can be used instead of `callable` for a more specific type.

## Alias Types
- `iterable`: Alias for `Traversable|array`.
- `?A`: Nullable type that is shorthand for `null|A`. Cannot be used as part of a union or intersection type.

## Union Types
- `A|B|C`: A type which may have multiple atomic type representations. For example, a type constraint of `A|B` can be assigned type `A` or `B`.

## Intersection Types
- `A&B&C`: A composite type which consists of multiple atomic types. For example, a type of `A&B` can be assigned to type `A` and to type `B`.

## DNF Types
- `A|B|(C&D&E)`: When combining union and intersection types, only a single level of nesting is permitted. The union must be the top level.

## Generic Types
- `MyType<TypeArg1, TypeArg2>`*
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
- `(TSubject is TCompare ? TTrue : TFalse)`*
Sometimes the return type of a function may depend on the type of a parameter. A conditional type can be used without templates too by using the parameter name. For example, `($myParam is string ? string : null)`. Conditional types must be wrapped in parentheses. Conditional types may also be nested.

## Array Key Type
- `key-of<TArray>`*
This type will resolve to a union of the keys of an array shape.

## Array Value Type
- `value-of<TArray>`*
This type will resolve to a union of the values of an array shape.

## Index Access Type
- `TArray[TKey]`*
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

## Miscellaneous Types
- `resource`*
- `class-string<T>`* A string where the value is the name of class `T`.

## PHPDoc Annotations
Intelephense supports standard PHPDoc annotations as well as non-standard annotations which have been popularised by other static analysis tools such as Psalm and PHPStan. The below list describes the non-standard annotations that Intelephense supports. For further information on standard PHPDoc annotations, please see the PHP_FIG and phpDocumentor references.
Some libraries or projects that have adopted static analysis tools such as Psalm or PHPStan may prefix some annotations with the tool name to avoid conflicts with other tools.
To make Intelephense prefer these prefixed annotations over the un-prefixed ones, you can set the `intelephense.compatibility.preferPsalmPhpstanPrefixedAnnotations` setting to `true`. Intelephense does not aim to support all types and features of these tools but will attempt to fallback to appropriate alternatives where possible.

## @template
`/** @template TemplateName of OptionalTypeConstraint = OptionalDefaultType */`
This annotation is used to declare a type argument of a generic type, function or method. The order that the template types appear is the same order in which the type arguments must be supplied in a generic type expression. The template type can be optionally constrained to a specific type and given an optional default type to be used when no type argument is supplied.

## @template-extends
`/** @template-extends ParentType<TypeArg1, TypeArg2> */`
This annotation is used to declare the type arguments supplied to a generic parent type. It can be used on classes and interfaces when extending a parent class or interface. The alias `@extends` is also supported.

## @template-implements
`/** @template-implements InterfaceType<TypeArg1, TypeArg2> */`
This annotation is used to declare the type arguments supplied to a generic interface. It can be used on classes and enums when implementing an interface. The alias `@implements` is also supported.

## @template-use
`/** @template-use TraitType<TypeArg1, TypeArg2> */`
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
This annotation is used to import a type alias that has been declared in another file. It functions similarly to `@phpstan-import-type` and `@psalm-import-type` and both these annotations may also be used. However, type aliases are not bound to classes in Intelephense and as such the from `ClassName` specifier is unnecessary but still supported. Type aliases in Intelephense follow normal PHP namespace rules.

## Features
Intelephense provides a variety of features to enhance the development experience when working with PHP code. Many of these features are provided for free while others require a Premium licence to access. All images and videos in this section are taken from the VS Code client. The features are available to all LSP clients that support the relevant LSP methods. Keybindings listed for each feature are the defaults for the VS Code client.

## Free Features
The following features are available to all users of Intelephense. A licence is not necessary.

## Workspace Symbols
- **Availability**: FREE
- **LSP**: `workspace/symbol`
- **Keybinding**: `Ctrl+T`
This feature allows you to search for symbols in your workspace and navigate to their definitions. It is particularly useful for finding and navigating to symbols that are not directly referenced in the current file. When the query contains alphanumeric characters only, the search is performed on the unqualified name of the symbol. You can narrow your search to a specific symbol by using a query containing characters found in the Fully Qualified Structural Element Name (FQSEN) of the symbol. For example, a query of `m\pt:u(` would find the method with FQSEN `App\Models\Post::user()`.
Unfortunately, VS Code has a current issue where it will discard results if the query contains a backslash. This means that you cannot search on the namespace part of a type.
![Workspace Symbols panel in VS Code](https://intelephense.com/img/workspace_symbols.png)
*Searching for workspace symbols using the FQSEN query syntax*

## Document Symbols
- **Availability**: FREE
- **LSP**: `textDocument/documentSymbol`
- **Keybinding**: `Ctrl+Shift+O`
This feature lists all symbols in the current document, providing an overview of the structure of the file. A client can use this information to provide a document outline view, breadcrumb navigation, and a symbol search specific to the current file.
![Document Symbols outline panel](https://intelephense.com/img/document_symbols.png)
*Document symbols provide an outline of the current file's structure*

## Go to Definition
- **Availability**: FREE
- **LSP**: `textDocument/definition`
- **Keybinding**: `F12` | right-click context menu
This feature allows you to navigate to the definition of a symbol when invoked on a reference to that symbol in the current file. Multiple definitions may sometimes be found for a symbol. For example, invoking the feature on the type name in a new expression may find both the constructor method and the class declaration as definitions. It is up to the client to decide how to present multiple definitions to the user. For example a peek definitions window may open or the user may simply be navigated to the first definition in the list.
![Go to Definition](https://intelephense.com/img/go_to_definition.png)
*Go to Definition navigates directly to a symbol's definition*

## Hover
- **Availability**: FREE
- **LSP**: `textDocument/hover`
- **Keybinding**: `Ctrl+K Ctrl+I` | mouse-over
This feature provides information about a symbol when hovering over a reference to that symbol in the current file. The information provided can include the type of the symbol, it's signature if it is a function or method, and any associated documentation.
![Hover tooltip](https://intelephense.com/img/hover.png)
*Hover shows type information and documentation for a symbol*

## Highlight
- **Availability**: FREE
- **LSP**: `textDocument/documentHighlight`
- **Keybinding**: Displayed automatically at the cursor position
This feature highlights all references to the symbol at the cursor position in the current file. This can be useful for quickly identifying all usages of a symbol in the current file. Read and write contexts will be identified if applicable and the client can choose to highlight them differently if desired.
![Document Highlight](https://intelephense.com/img/document_highlight.png)
*Document Highlight marks all references to the symbol under the cursor. Read and write contexts are coloured differently.*

## Code Completion
- **Availability**: FREE
- **LSP**: `textDocument/completion`
- **Keybinding**: `Ctrl+Space`
- **Trigger characters**: `$ > : \ / ' " * . <`
This feature provides a list of context appropriate completion suggestions for a symbol at the cursor position in the current file. The completions can include variables, functions, methods, classes, and other symbols. Where appropriate, additional edits are provided to automatically import a symbol.
![Code Completion dropdown](https://intelephense.com/img/code_completion.png)
*Code Completion provides context-aware suggestions as you type*

## Signature Help
- **Availability**: FREE
- **LSP**: `textDocument/signatureHelp`
- **Keybinding**: `Ctrl+Shift+Space`
- **Trigger characters**: `( , :`
This feature provides information about the signature of a function or method when the cursor is within the argument list of a function or method call. The information provided can include the types of the parameters, the return type, and any associated documentation.
![Signature Help popup](https://intelephense.com/img/signature_help.png)
*Signature Help displays parameter information for the current function call*

## Find All References
- **Availability**: FREE
- **LSP**: `textDocument/references`
- **Keybinding**: `Shift+F12` | right-click context menu
This feature provides a list of all references to a symbol in the current file or workspace. The references can include variables, functions, methods, classes, and other symbols. When there is a hierarchy of types, references to a type member will be determined relative to the initial base members.
![Find All References panel](https://intelephense.com/img/find_all_references.png)
*Find All References lists every usage of a symbol across the workspace*

## Formatting
- **Availability**: FREE
- **LSP**: `textDocument/formatting` (**Keybinding**: `Ctrl+Shift+I`)
- **LSP**: `textDocument/rangeFormatting` (**Keybinding**: `Ctrl+K Ctrl+F`)
This feature provides formatting of a whole document or a selected range within a document. The Intelephense formatter is opinionated and aims to comply with PHP-FIG coding standards. Limited configuration options are available to allow some customisation of brace style.
![Formatter](https://intelephense.com/img/formatting.png)
*Formatter applies PHP-FIG coding standards to the document*

## Diagnostics
- **Availability**: FREE
- **LSP**: `textDocument/publishDiagnostics`
- **Keybinding**: Published automatically `onType` or `onSave` | `F8` (next) | `Shift+F8` (previous)
This feature provides diagnostics for the currently opened files. Diagnostics include syntax errors, type errors, language constraints and other issues detected by Intelephense. Intelephense aims to provide rapid diagnostics that are aligned with the PHP engine where possible.
Performance and minimising false positives are prioritised over exhaustiveness. It should not be used as a substitute for testing your code. The diagnostics emitted can be configured in the settings to be more or less thorough or ignored altogether depending on your preferences and the codebase you are working with.
If you need fine grain control over which diagnostics are shown, try the `intelephense.diagnostics.exclude` setting. This setting allows you to map a file glob to an array of diagnostic codes to exclude from diagnostics. A full list of diagnostic codes can be found in the `vscode-intelephense` repository.
By default, Intelephense performs type checking on declared types only and in a relaxed mode in order to reduce false positives. In a hierarchy of types, a sub-type satisfies a super-type constraint. Intelephense also permits the reverse. That is, a super-type or wider type can be assigned to a sub-type or narrower type constraint. This default behaviour has been chosen due to inherent limitations in static analysis, the lack of syntax in PHP or PHPDoc to enable a developer to inline cast an expression or variable, and due to the variable quality of type information in some codebases.
To make type checks more thorough, there are several settings available.
- `intelephense.diagnostics.relaxedTypeCheck` controls whether to emit diagnostics when a super-type (excluding mixed) is assigned to a sub-type constraint.
- `intelephense.diagnostics.noMixedTypeCheck` controls whether to emit diagnostics when mixed is assigned to narrower type constraints.
- `intelephense.diagnostics.strictTypes` is a global equivalent to adding `declare(strict_types=1);` to the top of each file.
- `intelephense.diagnostics.typeCheckDocumentedTypes` controls whether documented types are included in type checking.
![Diagnostics panel](https://intelephense.com/img/diagnostics.png)
*Diagnostics surface type errors and other issues either as you type or on save depending on your settings.*

## Inline Values
- **Availability**: FREE
- **LSP**: `textDocument/inlineValues`
- **Keybinding**: Displayed automatically during a debug session
This feature provides ranges and text for variables in a file that may be relevant for a debugger to display inline values for during a debugging session. To see this feature in action in VS Code, install the official Xdebug extension.
![Inline Values](https://intelephense.com/img/inline_values.png)
*Inline Values display variable states during a debug session*

## Embedded Languages
Intelephense presumes that text outside of PHP tags is HTML. Basic language intelligence is provided for HTML and embedded CSS and JavaScript within HTML.
![Language intelligence for HTML and CSS](https://intelephense.com/img/embedded_languages.png)
*Language intelligence for HTML, CSS, and JavaScript within PHP files*

## Premium Features
The following features require a licence to access. A licence can be purchased at the [checkout page](https://intelephense.com/checkout.html).

## Rename
- **Availability**: PREMIUM
- **LSP**: `textDocument/rename`
- **Keybinding**: `F2` | right-click context menu
This feature allows you to rename a symbol and all references to that symbol in the current file or workspace. This differs from a simple text find and replace in that it is aware of the syntax and semantics of the code, and will only rename the specific symbol.
Intelephense will prefer to limit renames to the current file if possible. For example, renaming a class reference in a file where the class has been imported with a use declaration will result in the references in that file only being renamed and the use declaration being updated with an alias. In such cases, to rename a symbol across the whole workspace, invoke the rename feature on the class declaration itself or the Fully Qualified Name (FQN) in the use declaration instead.
Renaming a namespace in a file updates imports and FQN references for the file symbols in that namespace through the workspace. If using PSR-4 style folder structures then renaming the namespace of a class is also the equivalent of a move class to file operation. Intelephense will return file rename instructions to the client in such cases.
![Rename refactors a symbol](https://intelephense.com/img/rename.png)
*Rename refactors a symbol and all its references across the workspace*

## Code Folding
- **Availability**: PREMIUM
- **LSP**: `textDocument/foldingRange`
- **Keybinding**: `Ctrl+Shift+[` (fold) | `Ctrl+Shift+]` (unfold) | left-click editor gutter | right-click context menu
This feature allows you to fold and unfold regions of code in the current file. Intelephense provides folding ranges for symbol definition bodies, control structures, comments, imports, and custom regions identified by `#region` and `#endregion` comments. The folding provider is syntax tree driven and is more reliable than indent based folding providers such as the default provider in VS Code.
![Code Folding collapses and expands regions](https://intelephense.com/img/folding.png)
*Code Folding collapses and expands regions based on the syntax tree*

## Find All Implementations
- **Availability**: PREMIUM
- **LSP**: `textDocument/implementation`
- **Keybinding**: `Ctrl+F12` | right-click context menu
This feature provides a list of all implementations of a method or interface when invoked on a reference. This functions similar to go to definition but differs in that it will find the classes that implement the interface or methods that implement an abstract method declaration.
![Find All Implementations listing concrete classes](https://intelephense.com/img/implementation.png)
*Find All Implementations lists all concrete implementations of an interface or abstract method*

## Go to Type Definition
- **Availability**: PREMIUM
- **LSP**: `textDocument/typeDefinition`
- **Keybinding**: Right-click context menu
This feature allows you to navigate to the type definition of a variable. Similar to go to definition but differs in that it will navigate to the type definition rather than the variable declaration itself.
![Go to Type Definition](https://intelephense.com/img/type_definition.png)
*Go to Type Definition navigates to the type of a variable*

## Go to Declaration
- **Availability**: PREMIUM
- **LSP**: `textDocument/declaration`
- **Keybinding**: Right-click context menu
This feature allows you to navigate to the initial declaration of a symbol. Similar to go to definition, and depending on the context may function the same, it differs in that it will navigate to the initial declaration of a symbol in a hierarchy of types. For example, invoking this feature on a sub-type method reference will navigate to the initial declaration of the method in a super-type rather than the sub-type method declaration itself.
![Go to Declaration](https://intelephense.com/img/go_to_declaration.png)
*Go to Declaration navigates to the initial declaration in a type hierarchy*

## Smart Select
- **Availability**: PREMIUM
- **LSP**: `textDocument/selectionRange`
- **Keybinding**: `Shift+Alt+→` (expand) | `Shift+Alt+←` (shrink)
This feature allows you to expand and shrink the current selection in the current file based on the syntax tree of the code. For example, if the cursor is on a variable name, the first expansion would select the variable name, the second expansion would select the whole variable declaration, the third expansion would select the whole statement, the fourth expansion would select the whole block, and so on. Being syntax tree driven, it is more precise than regex or indent based selection providers such as the default provider in VS Code.
![Smart Select expands or shrinks the selection](https://intelephense.com/img/smart_select.png)
*Smart Select expands or shrinks the selection based on the syntax tree*

## Type Hierarchy
- **Availability**: PREMIUM
- **LSP**: `textDocument/typeHierarchy`
- **Keybinding**: Right-click context menu
This feature provides a type hierarchy for a class, interface, trait or enum when invoked on a reference to the type. It is useful for understanding the inheritance structure of a type and for quick navigation to types in the hierarchy.
![Type Hierarchy panel](https://intelephense.com/img/type_hierarchy.png)
*Type Hierarchy shows the inheritance structure of a type*

## Code Lens
- **Availability**: PREMIUM
- **LSP**: `textDocument/codeLens`
- **Keybinding**: Rendered inline above declarations | activated by left-clicking
This feature provides additional information and navigation for symbol declarations in the current file. Several lenses are provided by Intelephense. They are disabled by default to reduce visual clutter, see the `intelephense.codeLens` settings to enable them.
- **References**: shows the number of references to a symbol in the workspace and provides a link to view those references.
- **Implementations**: shows the number of implementations of an interface or abstract method and provides a link to view those implementations.
- **Overrides**: shows the number of overrides of a method in a type hierarchy and provides a link to view those overrides.
- **Parent**: shows whether a method overrides a parent method and provides a link to view the parent method.
- **Usages**: shows the number of types that use a trait and provides a link to view those usages.
![Code Lens displaying reference counts](https://intelephense.com/img/code_lens.png)
*Code Lens displays reference counts and navigation links above declarations*

## Inlay Hints
- **Availability**: PREMIUM
- **LSP**: `textDocument/inlayHint`
- **Keybinding**: Displayed inline automatically
This feature provides additional type and parameter information in the form of hints that are displayed inline with the code in the current file. Intelephense provides several types of inlay hints. They are enabled by default. See the `intelephense.inlayHints` settings to configure them.
- **Parameter Name**: shows the name of a parameter for a function or method argument.
- **Parameter Type**: shows the inferred type of a parameter in a closure that is an argument to another function or method when it has not been explicitly declared.
- **Return Type**: shows the inferred return type of a function or method when it has not been explicitly declared.
![Inlay Hints showing inferred parameter names](https://intelephense.com/img/inlay_hint.png)
*Inlay Hints show inferred parameter names and return types inline*

## Document Links
- **Availability**: PREMIUM
- **LSP**: `textDocument/documentLink`
- **Keybinding**: `Ctrl+Click` | mouse-over
This feature provides clickable links to related files and resources from the current file. Intelephense will show links to files referenced in `require` and `include` statements, and to local files referenced in `@see` annotations.
If your `require` statements are relative or you reference `$_SERVER['DOCUMENT_ROOT']`, you may need to configure the `intelephense.environment.documentRoot` setting to the correct path for the links to work. Intelephense will fallback to the workspace folder path if this setting has no value.
![Document Links showing clickable require and include paths](https://intelephense.com/img/document_link.png)
*Document Links make require/include paths and @see annotations clickable*

## Code Actions
- **Availability**: PREMIUM
- **LSP**: `textDocument/codeAction`
- **Keybinding**: `Ctrl+.` | left-click lightbulb
This feature provides a list of context appropriate actions that can be performed at the cursor position in the current file. VS Code will show a lightbulb icon on the current line when code actions are available. Intelephense provides several code actions.
- **Import Symbol**: Import (use) a type, function or constant to resolve an undefined symbol error.
- **Add PHPDoc**: Generate PHPDoc for functions, classes, and methods.
- **Implement All Abstract Methods**: Generate method stubs for all abstract methods that have not been implemented in a class.
![Code Actions offer quick-fix](https://intelephense.com/img/code_action.png)
*Code Actions offer quick-fix and refactoring options at the cursor position*

## Compatibility With Frameworks and Libraries
Intelephense aims to support all PHP frameworks and libraries but does not implement specific solutions for these. Limited or unexpected language intelligence can sometimes be provided if the package:
- Declares symbols at runtime via bootstrapping code or configuration.
- Uses interfaces heavily but encourages calling methods only declared on implementations.
- Uses `__get`,`__call`, or `__callStatic` magic heavily without corresponding `@property` or `@method` annotations.
- Has insufficient or incorrect type declarations/annotations.
In such cases you may notice a lack of completion suggestions, trouble jumping to definitions or undefined symbol diagnostics may appear even though the code may work when executed.
For example, a common problem can be when a framework returns an interface from a function but the project has been bootstrapped to use a particular concrete type that has additional methods not declared on the interface.
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
There are several ways to workaround the problem above. These workarounds can fall into two categories. Either they become part of the project executable code itself, or they are declared in a non-executable helper file and are there only to override the default Intelephense behaviour.

## Solutions that form part of the executable code
The advantage here is that problems in the code would become more apparent if the bootstrapping logic ever changed and returned a different class. The disadvantage is it is more code to write and perhaps difficult to retrofit to existing code.
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

## Solutions that do not form part of the project executable code
This involves creating a file with alternate symbol declarations and placing it in your workspace folder (not in vendor). Intelephense will prioritise user declared symbols over vendor declared symbols.
The advantage here is that it can be retrofitted easily to existing code, applies to all usages of the symbol and executable code remains untouched. The disadvantage is it could suppress an actual error that Intelephense would otherwise detect.
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
If classes, interfaces, traits, or enums have override definitions then Intelephense will treat them as partial types and merge them with the vendor declared types. Type overrides should either not use extends or implements clauses, or, alternatively keep them the same as the real type because implements and extends values are not merged.
There are also packages that provide or generate IDE helper files that may improve the experience when using various frameworks and libraries. For example: `laravel-ide-helper`.

## PHPDoc Instead of PHPStorm Metadata/Attributes
PHPStorm provides a way to override or express types using metadata and custom attributes in order to provide better language intelligence for code that is difficult to analyse statically, and to address limitations in the PHP language.
The same can be achieved with PHPDoc types. For greater compatibility with Intelephense and other PHP static analysis tools such as Psalm and PHPStan it is recommended to use PHPDoc types instead of PHPStorm metadata and attributes.
Intelephense does not support PHPStorm attributes and provides only limited support for PHPStorm metadata. Support for PHPStorm metadata may be removed in future versions of Intelephense.
The following examples show how to express types using PHPDoc types instead of PHPStorm metadata and attributes.

## Problem 1: Passing and Returning Strings or Objects
A function accepts `string|object` and returns this type after performing some operation. We want to return a string if a string is passed or a specific object if an object is passed, not a `string|object`.
- **Using PHPStorm metadata**:
```php
function paintColourMeta(string|object $input): string|object {}

PHPSTORM_METADATA\override(paintColourMeta(), PHPSTORM_METADATA\type(0));
```
- **Using PHPDoc annotations**:
```php
/**
 * @template T of string|object
 * @param T $input
 * @return T
 */
function paintColourDoc(string|object $input): string|object {}
$result = paintColourDoc(new BlueObject); // $result is inferred as BlueObject
```

## Problem 2: Return Type Based on String Argument
A function accepts a string and returns a different type based on the string passed in. We want to return a specific type based on the string argument, not a union of all possible return types.
- **Using PHPStorm metadata**:
```php
function getColourMeta(string $value): mixed {}

PHPSTORM_META\override(getColourMeta(), PHPSTORM_META\map([
    'red' => RedService::class,
    'blue' => BlueObject::class,
    'green' => GreenCollection::class,
]));
```
- **Using PHPDoc annotations**:
```php
/**
 * @template T of array{red: RedService, blue: BlueObject, green: GreenCollection}
 * @template K of key-of<T>
 * @param K $value
 * @return T[K]
 */
function getColourDoc(string $value): mixed {}
$obj = getColourDoc('red'); // $obj is inferred as RedService
```

## Problem 3: Array with Specific Keys
A function returns an array with a specific set of string keys. We want to provide language intelligence based on the keys and value types of the returned array.
- **Using PHPStorm attributes**:
```php
#[\JetBrains\PhpStorm\ArrayShape(['red' => RedService::class, 'blue' => BlueObject::class, 'green' => GreenCollection::class])]
function getColoursAttr(): array {}
```
- **Using PHPDoc annotations**:
```php
/**
 * @return array{red: RedService, blue: BlueObject, green: GreenCollection}
 */
function getColoursDoc(): array {}
$green = getColoursDoc()['green']; // $green is inferred as GreenCollection
```

## Problem 4: Expected String Literal Arguments
A function accepts a specific set of string literals as arguments. We want to provide language intelligence based on the allowed string literals
- **Using PHPStorm attributes**:
```php
#[\JetBrains\PhpStorm\ExpectedValues(values: ['red', 'blue', 'green'])]
function setColourAttr(string $colour): void {}
```
- **Using PHPDoc annotations**:
```php
/**
 * @param 'red'|'blue'|'green' $colour
 * @return void
 */
function setColourDoc(string $colour): void {}
setColourDoc(''); // Completion suggestions for 'red', 'blue', 'green'
```

---

# Chief AI Officer (CAIO) Role

> **Source:** user_input://caio_user_input.md
> **Analyzed At:** 2026-06-25T10:07:41.653Z

A Chief AI Officer (CAIO) is a C-suite executive responsible for overseeing an organization’s entire artificial intelligence strategy. To explore real-world openings and licensure requirements, you can research available roles on platforms like LinkedIn Jobs or explore executive AI leadership certifications via Coursera.
The role bridges the gap between advanced technical execution and bottom-line business outcomes. Because “AI Officer” is an executive title, it does not require a government-issued professional license (like a lawyer or doctor). However, companies typically look for advanced degrees (Ph.D., Master's) or professional certifications in Data Science, Computer Science, or an MBA.

## Core Job Description
A Chief AI Officer directs how a company develops, procures, and implements AI to boost productivity, enter new markets, and maintain a competitive edge.

## Key Responsibilities
- **Strategy & Vision:** Align AI initiatives with the company’s overall business goals.
- **Ethics & Governance:** Establish frameworks to ensure AI algorithms are free from bias, respect user privacy, and meet all legal and cybersecurity regulations.
- **Implementation & Tech Stacking:** Decide whether to build proprietary AI models or license third-party tools, managing relationships with external technology vendors.
- **Cross-Department Training:** Educate the board, executives, and general workforce on how to leverage AI safely and effectively.
- **Performance Tracking:** Measure the return on investment (ROI) and overall business impact of deployed AI projects.

## Qualifications & Requirements
- **Education:** A Master's or Ph.D. in Artificial Intelligence, Machine Learning, Computer Science, or a related quantitative field. An MBA is highly valued for the business-strategy aspect of the role.
- **Experience:** 8+ to 10+ years of progressive leadership experience in data science, AI development, or enterprise digital transformation.
- **Skillset:** A rare blend of technical fluency (understanding AI capabilities and limitations) and executive business acumen.

## CAIO vs. Other C-Suite Tech Roles
- **Chief Technology Officer (CTO):** Focuses on the company’s broad IT infrastructure, software architecture, and system reliability.
- **Chief Data Officer (CDO):** Manages data governance, architecture, and data pipelines to make sure data is clean and organized.
- **Chief AI Officer (CAIO):** Uses the foundations managed by the CTO and CDO to specifically drive business value and transform how work gets done.

---

# Chief AI Officer (CAIO) Market Intelligence

> **Source:** user_input://caio_market_intelligence_2026.md
> **Analyzed At:** 2026-06-25T10:07:41.671Z

## Market Landscape & Role Prevalence
As of mid-2026, the Chief AI Officer (CAIO) has become a cornerstone of the C-suite for organizations prioritizing digital transformation.
- **Adoption Rate:** Approximately 76% of firms have now appointed a CAIO or equivalent executive lead for AI, up from 60% in early 2025.
- **Industry Focus:** Highest adoption rates are observed in Technology, Healthcare, Finance, and Manufacturing sectors.
- **Strategic Intersection:** The role sits at the intersection of business strategy, technology/data architecture, risk/ethics, and cultural transformation.

## Real-World Openings & Recruitment (LinkedIn Jobs)
- **Platforms:** LinkedIn Jobs remains the primary platform for executive AI recruitment.
- **Notable Organizations with CAIOs (2024-2025):**
- **USDA:** Christopher Alvares, Chief AI Officer.
- **Office of the Director of National Intelligence (ODNI):** John Beieler, Chief AI Officer.
- **GE Healthcare:** Parminder Bhatia, Chief AI Officer.
- **Meta:** Oversees AI integration across Facebook, Instagram, WhatsApp, and Reality Labs.
- **IBM:** Early adopter, focusing on watsonx platform strategy and AI ethics.
- **Accenture & PwC:** Focus on enterprise-wide AI adoption and responsible AI governance for clients.
- **Key Requirements in Postings:**
- Evidence of bridging the gap between technical AI execution (e.g., Transformers, RAG architectures) and business ROI.
- Deep experience in auditing AI workflows and aligning predictive models with revenue streams.
- Ability to lead cross-functional "AI Ethics Boards."

## Executive AI Leadership Certifications (Coursera & Academic)
To meet licensure-equivalent standards for executive roles, the following programs are highly recognized in 2026:

## 1. The Chief AI Officer's Handbook (Coursera / Packt)
- **Content:** Develop and execute AI strategy as a CAIO, ensuring ethical compliance. Master agile AI project management and design/implement AI agents for autonomous system optimization.

## 2. Executive AI Leadership Mastery Specialization (Coursera)
- **Courses:** How to Build an Enterprise AI Strategy, Change Management for GenAI Integration, CEO Playbook: Generative AI.

## 3. AI for Executives & Strategy (Coursera / AI CERTs)
- **Focus:** Reshaping markets with AI and strategic certification for business leaders.

## 4. Chief AI Officer Specialization (Coursera)
- **Target:** Mid-level managers and aspiring executives.
- **Curriculum:** Practical application of AI governance and strategy.

## 5. University-Led Executive Programs
- **Duke University (Fuqua):** Chief AI Officer (CAIO) Program – Focuses on AI strategy and leadership for C-Suite executives.
- **UPenn (Wharton):** Executive Data Analyst & AI Strategy – Focuses on the financial impact of AI.
- **MIT xPRO:** AI Strategy and Leadership – Focuses on implementation and data strategy.
- **Stanford Online:** AI-Driven Leadership – Covers AI-driven decision making and business objectives.

## Salary Benchmarks (2026 Targets)
- **National Median Base Salary:** ~$350,000+
- **Total Compensation (Fortune 500):** $1.2M - $2.5M+ (including bonus and equity).
- **Core Metric:** Performance is increasingly tied to "AI-Driven ROI" and "Governance Compliance Scores."

## Trends
Market Intelligence Q3: Increased demand for sovereign AI clusters to ensure data residency and compliance.

---

# CAIO Strategic Mandates

> **Source:** grounded_research_2026
> **Analyzed At:** N/A

## Salary Intelligence (2026 Benchmarks)
- **Base Salary (National Median):** $351,519
- **75th Percentile:** $492,127
- **Total Compensation (Bonus & Equity):**
  - **Mid-Level CAIO:** $400,000 - $750,000
  - **Fortune 500 CAIO:** $1,000,000 - $2,500,000+

## Recommended Executive Programs & Certifications
- **ISO/IEC 42001 Lead Implementer:** The global benchmark for Artificial Intelligence Management Systems (AIMS).
- **AI Strategy and Leadership (MIT xPRO):** Focuses on strategic leadership, AI implementation, and data strategy.
- **AI-Driven Leadership (Stanford Online):** Covers AI-driven decision making and business objectives.
- **Leading an AI-Powered Future (Wharton Executive Education):** Features insights from industry leaders like Reid Hoffman on transforming the workforce.

## Advanced Strategic Mandates
- **ISO 42001 Compliance:** Enforce enterprise-wide compliance with ISO/IEC 42001 standards.
- **Quantum Synergy:** Activate quantum-secure synchronization and synergetic multi-cloud orchestration.
- **ROI Optimization:** Maintain 95% ROI efficiency across all AI workloads (roi_directive_95).
- **Phase 16 Mandates:** Heartbeat latency < 5ms and neural recovery protocol activation.

## Phase 13: Decentralized Edge Orchestration
- **Asia-Pacific Expansion:** Deploy decentralized edge nodes across the Asia-Pacific region.
- **Regional Compliance:** Enforce Asia-Pacific Regional Compliance for all sovereign data clusters.

---

# Search Console Mastery: https://software-online-review.com

> **Source:** google-search-console://https://software-online-review.com
> **Analyzed At:** 2026-06-25T00:38:28.440Z

## Search Performance Metrics
**Total Clicks:** 1450
**Total Impressions:** 52300
**Average Position:** 8.7
**CTR:** 2.77%

## Top Performing Queries
- **software online review**: 520 clicks, 2400 impressions (Pos: 8.7)
- **antigravity autonomous engine**: 180 clicks, 850 impressions (Pos: 8.7)
- **jules ai agent**: 110 clicks, 420 impressions (Pos: 8.7)
- **8 bukets project**: 95 clicks, 1800 impressions (Pos: 8.7)
- **autonomous workflow creation**: 65 clicks, 310 impressions (Pos: 8.7)

## Optimization Strategy
Increase content depth for high-impression, low-click queries to improve CTR. Monitor average position for brand-related keywords.

---

# (position) mRNA

> **Source:** https://markposition.wordpress.com
> **Analyzed At:** 2026-06-25T00:38:09.937Z

- [(position) mRNA](https://markposition.wordpress.com/)

## advertising.amazon
- [advertising.amazon](https://markposition.wordpress.com/2022/10/05/advertising-amazon/)
- [October 5, 2022](https://markposition.wordpress.com/2022/10/05/advertising-amazon/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/10/05/advertising-amazon/#respond)
- [https://advertising.amazon.com/](https://advertising.amazon.com/)

## Drive Advertising Revenue with Google Ad Manager : Google
- [Drive Advertising Revenue with Google Ad Manager : Google](https://markposition.wordpress.com/2022/09/26/drive-advertising-revenue-with-google-ad-manager-google-5/)
- [September 26, 2022September 26, 2022](https://markposition.wordpress.com/2022/09/26/drive-advertising-revenue-with-google-ad-manager-google-5/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/26/drive-advertising-revenue-with-google-ad-manager-google-5/#respond)
https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager
- [https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager](https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager)

## https://marketingplatform.google.com/about/search-ads-360/
- [https://marketingplatform.google.com/about/search-ads-360/](https://markposition.wordpress.com/2022/03/10/https-marketingplatform-google-com-about-search-ads-360-2/)
- [Aside](https://markposition.wordpress.com/type/aside/)
- [March 10, 2022March 10, 2022](https://markposition.wordpress.com/2022/03/10/https-marketingplatform-google-com-about-search-ads-360-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/10/https-marketingplatform-google-com-about-search-ads-360-2/#respond)
https://marketingplatform.google.com/about/search-ads-360/
- [https://marketingplatform.google.com/about/search-ads-360/](https://marketingplatform.google.com/about/search-ads-360/)

## Analytics Academy
- [Analytics Academy](https://markposition.wordpress.com/2022/09/20/analytics-academy/)
- [September 20, 2022March 21, 2023](https://markposition.wordpress.com/2022/09/20/analytics-academy/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/20/analytics-academy/#respond)
https://analytics.google.com/analytics/academy/
- [https://analytics.google.com/analytics/academy/](https://analytics.google.com/analytics/academy/)

## Adssettings google
- [Adssettings google](https://markposition.wordpress.com/2022/09/20/adssettings-google/)
- [September 20, 2022](https://markposition.wordpress.com/2022/09/20/adssettings-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/20/adssettings-google/#respond)
https://adssettings.google.com/authenticated
- [https://adssettings.google.com/authenticated](https://adssettings.google.com/authenticated)

## Data google
- [Data google](https://markposition.wordpress.com/2022/09/20/data-google/)
- [September 20, 2022](https://markposition.wordpress.com/2022/09/20/data-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/20/data-google/#respond)
https://myaccount.google.com/data-and-personalization
- [https://myaccount.google.com/data-and-personalization](https://myaccount.google.com/data-and-personalization)

## The Privacy Sandbox: Technology for a More Private Web.
- [The Privacy Sandbox: Technology for a More Private Web.](https://markposition.wordpress.com/2022/09/20/the-privacy-sandbox-technology-for-a-more-private-web/)
- [September 20, 2022](https://markposition.wordpress.com/2022/09/20/the-privacy-sandbox-technology-for-a-more-private-web/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/20/the-privacy-sandbox-technology-for-a-more-private-web/#respond)
https://privacysandbox.com/intl/home#home-hero
- [https://privacysandbox.com/intl/home#home-hero](https://privacysandbox.com/intl/home#home-hero)

## Digital Experience Platform & Enterprise CMS | Crownpeak
- [Digital Experience Platform & Enterprise CMS | Crownpeak](https://markposition.wordpress.com/2022/09/16/digital-experience-platform-enterprise-cms-crownpeak-2/)
- [September 16, 2022](https://markposition.wordpress.com/2022/09/16/digital-experience-platform-enterprise-cms-crownpeak-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/16/digital-experience-platform-enterprise-cms-crownpeak-2/#respond)
https://www.crownpeak.com/
- [https://www.crownpeak.com/](https://www.crownpeak.com/)

## About Performance Max campaigns – Google Ads
- [About Performance Max campaigns – Google Ads](https://markposition.wordpress.com/2022/09/01/about-performance-max-campaigns-google-ads/)
- [September 1, 2022](https://markposition.wordpress.com/2022/09/01/about-performance-max-campaigns-google-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/01/about-performance-max-campaigns-google-ads/#respond)
https://support.google.com/google-ads/answer/10724817?hl=en
- [https://support.google.com/google-ads/answer/10724817?hl=en](https://support.google.com/google-ads/answer/10724817?hl=en)

## About Smart Bidding – Google Ads
- [About Smart Bidding – Google Ads](https://markposition.wordpress.com/2022/09/01/about-smart-bidding-google-ads/)
- [September 1, 2022](https://markposition.wordpress.com/2022/09/01/about-smart-bidding-google-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/01/about-smart-bidding-google-ads/#respond)
https://support.google.com/google-ads/answer/7065882?hl=en
- [https://support.google.com/google-ads/answer/7065882?hl=en](https://support.google.com/google-ads/answer/7065882?hl=en)

## About Maximize conversion value bidding – Google Ads
- [About Maximize conversion value bidding – Google Ads](https://markposition.wordpress.com/2022/09/01/about-maximize-conversion-value-bidding-google-ads/)
- [September 1, 2022](https://markposition.wordpress.com/2022/09/01/about-maximize-conversion-value-bidding-google-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/01/about-maximize-conversion-value-bidding-google-ads/#respond)
https://support.google.com/google-ads/answer/7684216?hl=en
- [https://support.google.com/google-ads/answer/7684216?hl=en](https://support.google.com/google-ads/answer/7684216?hl=en)

## About automated bidding – Google Ads Help
- [About automated bidding – Google Ads Help](https://markposition.wordpress.com/2022/09/01/about-automated-bidding-google-ads-help/)
- [September 1, 2022](https://markposition.wordpress.com/2022/09/01/about-automated-bidding-google-ads-help/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/01/about-automated-bidding-google-ads-help/#respond)
https://support.google.com/google-ads/answer/2979071?hl=en
- [https://support.google.com/google-ads/answer/2979071?hl=en](https://support.google.com/google-ads/answer/2979071?hl=en)

## About Target CPA bidding – Google Ads Help
- [About Target CPA bidding – Google Ads Help](https://markposition.wordpress.com/2022/09/01/about-target-cpa-bidding-google-ads-help/)
- [September 1, 2022](https://markposition.wordpress.com/2022/09/01/about-target-cpa-bidding-google-ads-help/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/01/about-target-cpa-bidding-google-ads-help/#respond)
https://support.google.com/google-ads/answer/6268632?hl=en
- [https://support.google.com/google-ads/answer/6268632?hl=en](https://support.google.com/google-ads/answer/6268632?hl=en)

## About Maximize conversions bidding – Google Ads Help
- [About Maximize conversions bidding – Google Ads Help](https://markposition.wordpress.com/2022/09/01/about-maximize-conversions-bidding-google-ads-help/)
- [September 1, 2022](https://markposition.wordpress.com/2022/09/01/about-maximize-conversions-bidding-google-ads-help/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/01/about-maximize-conversions-bidding-google-ads-help/#respond)
https://support.google.com/google-ads/answer/7381968?hl=en
- [https://support.google.com/google-ads/answer/7381968?hl=en](https://support.google.com/google-ads/answer/7381968?hl=en)

## About Target ROAS bidding – Google Ads Help
- [About Target ROAS bidding – Google Ads Help](https://markposition.wordpress.com/2022/09/01/about-target-roas-bidding-google-ads-help/)
- [September 1, 2022](https://markposition.wordpress.com/2022/09/01/about-target-roas-bidding-google-ads-help/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/01/about-target-roas-bidding-google-ads-help/#respond)
https://support.google.com/google-ads/answer/6268637?hl=en
- [https://support.google.com/google-ads/answer/6268637?hl=en](https://support.google.com/google-ads/answer/6268637?hl=en)

## Achieve your goals across Google’s ad channels with Performance Max – Google Ads Help
- [Achieve your goals across Google’s ad channels with Performance Max – Google Ads Help](https://markposition.wordpress.com/2022/09/01/achieve-your-goals-across-googles-ad-channels-with-performance-max-google-ads-help/)
- [September 1, 2022](https://markposition.wordpress.com/2022/09/01/achieve-your-goals-across-googles-ad-channels-with-performance-max-google-ads-help/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/09/01/achieve-your-goals-across-googles-ad-channels-with-performance-max-google-ads-help/#respond)
https://support.google.com/google-ads/answer/11189316?hl=en
- [https://support.google.com/google-ads/answer/11189316?hl=en](https://support.google.com/google-ads/answer/11189316?hl=en)

## Coalition for Better Ads
- [Coalition for Better Ads](https://markposition.wordpress.com/2022/08/31/coalition-for-better-ads-2/)
- [August 31, 2022](https://markposition.wordpress.com/2022/08/31/coalition-for-better-ads-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/31/coalition-for-better-ads-2/#respond)
https://www.betterads.org/
- [https://www.betterads.org/](https://www.betterads.org/)

## ShareThis: Free Share Buttons & Plugins, Global Behavioral Data Solutions
- [ShareThis: Free Share Buttons & Plugins, Global Behavioral Data Solutions](https://sharethis.com/)
- [Link](https://markposition.wordpress.com/type/link/)
- [August 20, 2022](https://markposition.wordpress.com/2022/08/20/sharethis-free-share-buttons-plugins-global-behavioral-data-solutions-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/20/sharethis-free-share-buttons-plugins-global-behavioral-data-solutions-2/#respond)
https://sharethis.com/
- [https://sharethis.com/](https://sharethis.com/)

## How To Create Quality Video Ads – YouTube Advertising
- [How To Create Quality Video Ads – YouTube Advertising](https://markposition.wordpress.com/2022/08/16/how-to-create-quality-video-ads-youtube-advertising/)
- [August 16, 2022](https://markposition.wordpress.com/2022/08/16/how-to-create-quality-video-ads-youtube-advertising/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/16/how-to-create-quality-video-ads-youtube-advertising/#respond)
https://www.youtube.com/intl/en_us/ads/how-it-works/create-a-video-ad/
- [https://www.youtube.com/intl/en_us/ads/how-it-works/create-a-video-ad/](https://www.youtube.com/intl/en_us/ads/how-it-works/create-a-video-ad/)

## Business Data Responsibility – Your Data Protection & Privacy
- [Business Data Responsibility – Your Data Protection & Privacy](https://markposition.wordpress.com/2022/08/15/business-data-responsibility-your-data-protection-privacy/)
- [August 15, 2022March 21, 2023](https://markposition.wordpress.com/2022/08/15/business-data-responsibility-your-data-protection-privacy/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/15/business-data-responsibility-your-data-protection-privacy/#respond)
https://business.safety.google/
- [https://business.safety.google/](https://business.safety.google/)

## Google Ads Data Protection Terms: Service Information
- [Google Ads Data Protection Terms: Service Information](https://markposition.wordpress.com/2022/08/15/google-ads-data-protection-terms-service-information/)
- [August 15, 2022](https://markposition.wordpress.com/2022/08/15/google-ads-data-protection-terms-service-information/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/15/google-ads-data-protection-terms-service-information/#respond)
https://business.safety.google/adsservices/
- [https://business.safety.google/adsservices/](https://business.safety.google/adsservices/)

## Outbrain Advertising – Drive ROAS on the Open Web | Outbrain.com
- [Outbrain Advertising – Drive ROAS on the Open Web | Outbrain.com](https://markposition.wordpress.com/2022/08/15/outbrain-advertising-drive-roas-on-the-open-web-outbrain-com/)
- [August 15, 2022](https://markposition.wordpress.com/2022/08/15/outbrain-advertising-drive-roas-on-the-open-web-outbrain-com/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/15/outbrain-advertising-drive-roas-on-the-open-web-outbrain-com/#respond)
https://www.outbrain.com/advertisers/
- [https://www.outbrain.com/advertisers/](https://www.outbrain.com/advertisers/)

## Prebid
- [Prebid](https://markposition.wordpress.com/2022/08/14/prebid/)
- [August 14, 2022](https://markposition.wordpress.com/2022/08/14/prebid/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/14/prebid/#respond)
- [Homepage](https://prebid.org/)

## wmg
- [wmg](https://markposition.wordpress.com/2022/08/14/wmg/)
- [August 14, 2022](https://markposition.wordpress.com/2022/08/14/wmg/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/14/wmg/#respond)
- [Home](https://adwmg.com/)

## Trustpilot Reviews: Experience the power of customer reviews
- [Trustpilot Reviews: Experience the power of customer reviews](https://markposition.wordpress.com/2022/08/11/trustpilot-reviews-experience-the-power-of-customer-reviews-2/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/trustpilot-reviews-experience-the-power-of-customer-reviews-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/trustpilot-reviews-experience-the-power-of-customer-reviews-2/#respond)
https://www.trustpilot.com/
- [https://www.trustpilot.com/](https://www.trustpilot.com/)

## Online-Shopping mit Trusted Shops | Jetzt alle Produkte kennenlernen
- [Online-Shopping mit Trusted Shops | Jetzt alle Produkte kennenlernen](https://markposition.wordpress.com/2022/08/11/online-shopping-mit-trusted-shops-jetzt-alle-produkte-kennenlernen/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/online-shopping-mit-trusted-shops-jetzt-alle-produkte-kennenlernen/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/online-shopping-mit-trusted-shops-jetzt-alle-produkte-kennenlernen/#respond)
https://www.trustedshops.de/
- [https://www.trustedshops.de/](https://www.trustedshops.de/)

## TestFreaks – Ratings & Reviews Platform
- [TestFreaks – Ratings & Reviews Platform](https://markposition.wordpress.com/2022/08/11/testfreaks-ratings-reviews-platform/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/testfreaks-ratings-reviews-platform/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/testfreaks-ratings-reviews-platform/#respond)
https://www.testfreaks.com/
- [https://www.testfreaks.com/](https://www.testfreaks.com/)

## TargetBay: Ecommerce Email Marketing Software and Marketing Automation
- [TargetBay: Ecommerce Email Marketing Software and Marketing Automation](https://markposition.wordpress.com/2022/08/11/targetbay-ecommerce-email-marketing-software-and-marketing-automation/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/targetbay-ecommerce-email-marketing-software-and-marketing-automation/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/targetbay-ecommerce-email-marketing-software-and-marketing-automation/#respond)
https://targetbay.com/
- [https://targetbay.com/](https://targetbay.com/)

## Stamped | Reviews and Loyalty for Ecommerce Brands
- [Stamped | Reviews and Loyalty for Ecommerce Brands](https://markposition.wordpress.com/2022/08/11/stamped-reviews-and-loyalty-for-ecommerce-brands/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/stamped-reviews-and-loyalty-for-ecommerce-brands/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/stamped-reviews-and-loyalty-for-ecommerce-brands/#respond)
https://stamped.io/
- [https://stamped.io/](https://stamped.io/)

## Avis clients authentiques avec Shopping-Satisfaction
- [Avis clients authentiques avec Shopping-Satisfaction](https://markposition.wordpress.com/2022/08/11/avis-clients-authentiques-avec-shopping-satisfaction/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/avis-clients-authentiques-avec-shopping-satisfaction/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/avis-clients-authentiques-avec-shopping-satisfaction/#respond)
https://www.shopping-satisfaction.com/
- [https://www.shopping-satisfaction.com/](https://www.shopping-satisfaction.com/)

## Shopperapproved
- [Shopperapproved](https://markposition.wordpress.com/2022/08/11/shopperapproved/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/shopperapproved/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/shopperapproved/#respond)
https://www.shopperapproved.com/
- [https://www.shopperapproved.com/](https://www.shopperapproved.com/)

## REVIEWS.io | In Reviews We Trust
- [REVIEWS.io | In Reviews We Trust](https://markposition.wordpress.com/2022/08/11/reviews-io-in-reviews-we-trust/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/reviews-io-in-reviews-we-trust/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/reviews-io-in-reviews-we-trust/#respond)
https://www.reviews.io/
- [https://www.reviews.io/](https://www.reviews.io/)

## Resellerratings
- [Resellerratings](https://markposition.wordpress.com/2022/08/11/resellerratings/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/resellerratings/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/resellerratings/#respond)
https://resellerratings.com/
- [https://resellerratings.com/](https://resellerratings.com/)

## PowerReviews: Doing More with UGC to Grow Your Business
- [PowerReviews: Doing More with UGC to Grow Your Business](https://markposition.wordpress.com/2022/08/11/powerreviews-doing-more-with-ugc-to-grow-your-business/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/powerreviews-doing-more-with-ugc-to-grow-your-business/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/powerreviews-doing-more-with-ugc-to-grow-your-business/#respond)
https://www.powerreviews.com/
- [https://www.powerreviews.com/](https://www.powerreviews.com/)

## Okendo
- [Okendo](https://markposition.wordpress.com/2022/08/11/okendo/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/okendo/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/okendo/#respond)
https://www.okendo.io/
- [https://www.okendo.io/](https://www.okendo.io/)

## Loox Shopify Reviews App – Product Reviews & Referrals
- [Loox Shopify Reviews App – Product Reviews & Referrals](https://markposition.wordpress.com/2022/08/11/loox-shopify-reviews-app-product-reviews-referrals/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/loox-shopify-reviews-app-product-reviews-referrals/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/loox-shopify-reviews-app-product-reviews-referrals/#respond)
https://loox.app/
- [https://loox.app/](https://loox.app/)

## Junip | Reviews for products worth talking about
- [Junip | Reviews for products worth talking about](https://markposition.wordpress.com/2022/08/11/junip-reviews-for-products-worth-talking-about/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/junip-reviews-for-products-worth-talking-about/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/junip-reviews-for-products-worth-talking-about/#respond)
https://junip.co/
- [https://junip.co/](https://junip.co/)

## Guaranteed Reviews Company | Guaranteed customer review solution
- [Guaranteed Reviews Company | Guaranteed customer review solution](https://markposition.wordpress.com/2022/08/11/guaranteed-reviews-company-guaranteed-customer-review-solution/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/guaranteed-reviews-company-guaranteed-customer-review-solution/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/guaranteed-reviews-company-guaranteed-customer-review-solution/#respond)
https://www.guaranteed-reviews.com/
- [https://www.guaranteed-reviews.com/](https://www.guaranteed-reviews.com/)

## Feefo | Transform your business with real customer reviews
- [Feefo | Transform your business with real customer reviews](https://markposition.wordpress.com/2022/08/11/feefo-transform-your-business-with-real-customer-reviews/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/feefo-transform-your-business-with-real-customer-reviews/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/feefo-transform-your-business-with-real-customer-reviews/#respond)
https://www.feefo.com/
- [https://www.feefo.com/](https://www.feefo.com/)

## feedaty
- [feedaty](https://markposition.wordpress.com/2022/08/11/feedaty/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/feedaty/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/feedaty/#respond)
https://www.feedaty.com/
- [https://www.feedaty.com/](https://www.feedaty.com/)

## eKomi | The Feedback Company
- [eKomi | The Feedback Company](https://markposition.wordpress.com/2022/08/11/ekomi-the-feedback-company/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/ekomi-the-feedback-company/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/ekomi-the-feedback-company/#respond)
https://www.ekomi.co.uk/uk/
- [https://www.ekomi.co.uk/uk/](https://www.ekomi.co.uk/uk/)

## Echte-Bewertungen – Verbessern Sie Ihre Geschäftsergebnisse
- [Echte-Bewertungen – Verbessern Sie Ihre Geschäftsergebnisse](https://markposition.wordpress.com/2022/08/11/echte-bewertungen-verbessern-sie-ihre-geschaftsergebnisse/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/echte-bewertungen-verbessern-sie-ihre-geschaftsergebnisse/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/echte-bewertungen-verbessern-sie-ihre-geschaftsergebnisse/#respond)
https://www.echte-bewertungen.com/
- [https://www.echte-bewertungen.com/](https://www.echte-bewertungen.com/)

## Bazaarvoice: Meet shoppers in all the moments that matter
- [Bazaarvoice: Meet shoppers in all the moments that matter](https://markposition.wordpress.com/2022/08/11/bazaarvoice-meet-shoppers-in-all-the-moments-that-matter/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/bazaarvoice-meet-shoppers-in-all-the-moments-that-matter/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/bazaarvoice-meet-shoppers-in-all-the-moments-that-matter/#respond)
https://www.bazaarvoice.com/
- [https://www.bazaarvoice.com/](https://www.bazaarvoice.com/)

## Avis clients : boostez vos ventes avec Avis Vérifiés !
- [Avis clients : boostez vos ventes avec Avis Vérifiés !](https://markposition.wordpress.com/2022/08/11/avis-clients-boostez-vos-ventes-avec-avis-verifies/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/avis-clients-boostez-vos-ventes-avec-avis-verifies/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/avis-clients-boostez-vos-ventes-avec-avis-verifies/#respond)
https://www.avis-verifies.com/fr/
- [https://www.avis-verifies.com/fr/](https://www.avis-verifies.com/fr/)

## Loyalty Experience Platform – Annex Cloud Loyalty Management Solution
- [Loyalty Experience Platform – Annex Cloud Loyalty Management Solution](https://markposition.wordpress.com/2022/08/11/loyalty-experience-platform-annex-cloud-loyalty-management-solution/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/loyalty-experience-platform-annex-cloud-loyalty-management-solution/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/loyalty-experience-platform-annex-cloud-loyalty-management-solution/#respond)
https://www.annexcloud.com/
- [https://www.annexcloud.com/](https://www.annexcloud.com/)

## Verified-Reviews – Boost your sales uk
- [Verified-Reviews – Boost your sales uk](https://markposition.wordpress.com/2022/08/11/verified-reviews-boost-your-sales-uk/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/verified-reviews-boost-your-sales-uk/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/verified-reviews-boost-your-sales-uk/#respond)
https://www.verified-reviews.co.uk/
- [https://www.verified-reviews.co.uk/](https://www.verified-reviews.co.uk/)

## Yotpo
- [Yotpo](https://markposition.wordpress.com/2022/08/11/yotpo/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/yotpo/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/yotpo/#respond)
https://www.yotpo.com/
- [https://www.yotpo.com/](https://www.yotpo.com/)

## Verified Reviews – Boost your sales
- [Verified Reviews – Boost your sales](https://markposition.wordpress.com/2022/08/11/verified-reviews-boost-your-sales/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/verified-reviews-boost-your-sales/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/verified-reviews-boost-your-sales/#respond)
https://www.netreviews.com/en/
- [https://www.netreviews.com/en/](https://www.netreviews.com/en/)

## Pixlee TurnTo | Social User-Generated Content (UGC), Ratings & Reviews, and Influencer Marketing Platform
- [Pixlee TurnTo | Social User-Generated Content (UGC), Ratings & Reviews, and Influencer Marketing Platform](https://markposition.wordpress.com/2022/08/11/pixlee-turnto-social-user-generated-content-ugc-ratings-reviews-and-influencer-marketing-platform/)
- [August 11, 2022](https://markposition.wordpress.com/2022/08/11/pixlee-turnto-social-user-generated-content-ugc-ratings-reviews-and-influencer-marketing-platform/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/11/pixlee-turnto-social-user-generated-content-ugc-ratings-reviews-and-influencer-marketing-platform/#respond)
https://www.pixlee.com/
- [https://www.pixlee.com/](https://www.pixlee.com/)

## Facebook Blueprint: Free Online Training for Advertising on Facebook | Meta for Business
- [Facebook Blueprint: Free Online Training for Advertising on Facebook | Meta for Business](https://markposition.wordpress.com/2022/08/08/facebook-blueprint-free-online-training-for-advertising-on-facebook-meta-for-business/)
- [August 8, 2022](https://markposition.wordpress.com/2022/08/08/facebook-blueprint-free-online-training-for-advertising-on-facebook-meta-for-business/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/08/facebook-blueprint-free-online-training-for-advertising-on-facebook-meta-for-business/#respond)
https://web.facebook.com/business/learn
- [https://web.facebook.com/business/learn](https://web.facebook.com/business/learn)

## Facebook Certification: Professional Certificate Exams from Facebook | Meta for Business
- [Facebook Certification: Professional Certificate Exams from Facebook | Meta for Business](https://markposition.wordpress.com/2022/08/08/facebook-certification-professional-certificate-exams-from-facebook-meta-for-business/)
- [August 8, 2022](https://markposition.wordpress.com/2022/08/08/facebook-certification-professional-certificate-exams-from-facebook-meta-for-business/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/08/facebook-certification-professional-certificate-exams-from-facebook-meta-for-business/#respond)
https://web.facebook.com/business/learn/certification
- [https://web.facebook.com/business/learn/certification](https://web.facebook.com/business/learn/certification)

## Facebook Ads: Online Advertising on Facebook | Meta for Business
- [Facebook Ads: Online Advertising on Facebook | Meta for Business](https://markposition.wordpress.com/2022/08/08/facebook-ads-online-advertising-on-facebook-meta-for-business/)
- [August 8, 2022](https://markposition.wordpress.com/2022/08/08/facebook-ads-online-advertising-on-facebook-meta-for-business/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/08/facebook-ads-online-advertising-on-facebook-meta-for-business/#respond)
https://web.facebook.com/business/ads
- [https://web.facebook.com/business/ads](https://web.facebook.com/business/ads)

## Create a LinkedIn Company Page | LinkedIn Marketing Solutions
- [Create a LinkedIn Company Page | LinkedIn Marketing Solutions](https://markposition.wordpress.com/2022/08/08/create-a-linkedin-company-page-linkedin-marketing-solutions/)
- [August 8, 2022](https://markposition.wordpress.com/2022/08/08/create-a-linkedin-company-page-linkedin-marketing-solutions/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/08/create-a-linkedin-company-page-linkedin-marketing-solutions/#respond)
https://business.linkedin.com/marketing-solutions/linkedin-pages
- [https://business.linkedin.com/marketing-solutions/linkedin-pages](https://business.linkedin.com/marketing-solutions/linkedin-pages)

## Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions
- [Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions](https://markposition.wordpress.com/2022/08/08/marketing-advertising-on-linkedin-linkedin-marketing-solutions-4/)
- [August 8, 2022](https://markposition.wordpress.com/2022/08/08/marketing-advertising-on-linkedin-linkedin-marketing-solutions-4/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/08/08/marketing-advertising-on-linkedin-linkedin-marketing-solutions-4/#respond)
https://business.linkedin.com/marketing-solutions
- [https://business.linkedin.com/marketing-solutions](https://business.linkedin.com/marketing-solutions)

## Coalition for Better Ads
- [Coalition for Better Ads](https://markposition.wordpress.com/2022/07/28/coalition-for-better-ads/)
- [July 28, 2022](https://markposition.wordpress.com/2022/07/28/coalition-for-better-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/07/28/coalition-for-better-ads/#respond)
https://www.betterads.org/
- [https://www.betterads.org/](https://www.betterads.org/)

## FC
- [May 26, 2022March 21, 2023](https://markposition.wordpress.com/2022/05/26/fc/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/05/26/fc/#respond)
https://fundingchoices.google.com/start/
- [https://fundingchoices.google.com/start/](https://fundingchoices.google.com/start/)

## Funding Choices
- [Funding Choices](https://markposition.wordpress.com/2022/05/26/funding-choices/)
- [May 26, 2022March 21, 2023](https://markposition.wordpress.com/2022/05/26/funding-choices/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/05/26/funding-choices/#respond)
https://support.google.com/fundingchoices/answer/9010669?hl=hr
- [https://support.google.com/fundingchoices/answer/9010669?hl=hr](https://support.google.com/fundingchoices/answer/9010669?hl=hr)

## Publisher strategy for privacy preferences – Think with Google
- [Publisher strategy for privacy preferences – Think with Google](https://markposition.wordpress.com/2022/05/23/publisher-strategy-for-privacy-preferences-think-with-google/)
- [May 23, 2022](https://markposition.wordpress.com/2022/05/23/publisher-strategy-for-privacy-preferences-think-with-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/05/23/publisher-strategy-for-privacy-preferences-think-with-google/#respond)
https://www.thinkwithgoogle.com/future-of-marketing/privacy-and-trust/publisher-privacy-landscape/
- [https://www.thinkwithgoogle.com/future-of-marketing/privacy-and-trust/publisher-privacy-landscape/](https://www.thinkwithgoogle.com/future-of-marketing/privacy-and-trust/publisher-privacy-landscape/)

## The Future of Marketing – Think with Google
- [The Future of Marketing – Think with Google](https://markposition.wordpress.com/2022/05/23/the-future-of-marketing-think-with-google/)
- [May 23, 2022](https://markposition.wordpress.com/2022/05/23/the-future-of-marketing-think-with-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/05/23/the-future-of-marketing-think-with-google/#respond)
https://www.thinkwithgoogle.com/future-of-marketing/
- [https://www.thinkwithgoogle.com/future-of-marketing/](https://www.thinkwithgoogle.com/future-of-marketing/)

## Google Ads Help: Understanding optimized targeting
- [Google Ads Help: Understanding optimized targeting](https://markposition.wordpress.com/2022/05/16/google-ads-help-understanding-optimized-targeting/)
- [May 16, 2022](https://markposition.wordpress.com/2022/05/16/google-ads-help-understanding-optimized-targeting/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/05/16/google-ads-help-understanding-optimized-targeting/#respond)

## ptimization targeting – Google Ads
- [ptimization targeting – Google Ads](https://markposition.wordpress.com/2022/05/16/ptimization-targeting-google-ads/)
- [May 16, 2022](https://markposition.wordpress.com/2022/05/16/ptimization-targeting-google-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/05/16/ptimization-targeting-google-ads/#respond)
https://support.google.com/google-ads/answer/10537509?hl=hr
- [https://support.google.com/google-ads/answer/10537509?hl=hr](https://support.google.com/google-ads/answer/10537509?hl=hr)

## Google News Initiative Training Center
- [Google News Initiative Training Center](https://markposition.wordpress.com/2022/05/16/google-news-initiative-training-center/)
- [May 16, 2022](https://markposition.wordpress.com/2022/05/16/google-news-initiative-training-center/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/05/16/google-news-initiative-training-center/#respond)
https://newsinitiative.withgoogle.com/training/datatools
- [https://newsinitiative.withgoogle.com/training/datatools](https://newsinitiative.withgoogle.com/training/datatools)

## Create Reports in Google Ad Manager : Google
- [Create Reports in Google Ad Manager : Google](https://markposition.wordpress.com/2022/05/12/create-reports-in-google-ad-manager-google-3/)
- [May 12, 2022](https://markposition.wordpress.com/2022/05/12/create-reports-in-google-ad-manager-google-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/05/12/create-reports-in-google-ad-manager-google-3/#respond)
https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager
- [https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager](https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager)

## Optimize Google Ad Manager to Meet Objectives : Google
- [Optimize Google Ad Manager to Meet Objectives : Google](https://markposition.wordpress.com/2022/05/09/optimize-google-ad-manager-to-meet-objectives-google/)
- [May 9, 2022](https://markposition.wordpress.com/2022/05/09/optimize-google-ad-manager-to-meet-objectives-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/05/09/optimize-google-ad-manager-to-meet-objectives-google/#respond)
https://skillshop.exceedlms.com/student/path/54611-optimize-google-ad-manager-to-meet-objectives
- [https://skillshop.exceedlms.com/student/path/54611-optimize-google-ad-manager-to-meet-objectives](https://skillshop.exceedlms.com/student/path/54611-optimize-google-ad-manager-to-meet-objectives)

## Get started with Twitter Ads
- [Get started with Twitter Ads](https://markposition.wordpress.com/2022/05/05/get-started-with-twitter-ads/)
- [May 5, 2022](https://markposition.wordpress.com/2022/05/05/get-started-with-twitter-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/05/05/get-started-with-twitter-ads/#respond)
https://business.twitter.com/en/advertising/get-started-with-twitter-ads.html
- [https://business.twitter.com/en/advertising/get-started-with-twitter-ads.html](https://business.twitter.com/en/advertising/get-started-with-twitter-ads.html)

## Pixalate – Ad Fraud Protection, Privacy, and Compliance Platform (CTV)
- [Pixalate – Ad Fraud Protection, Privacy, and Compliance Platform (CTV)](https://markposition.wordpress.com/2022/05/04/pixalate-ad-fraud-protection-privacy-and-compliance-platform-ctv/)
- [May 4, 2022](https://markposition.wordpress.com/2022/05/04/pixalate-ad-fraud-protection-privacy-and-compliance-platform-ctv/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/05/04/pixalate-ad-fraud-protection-privacy-and-compliance-platform-ctv/#respond)
https://www.pixalate.com/
- [https://www.pixalate.com/](https://www.pixalate.com/)

## Publisher Collective | Get better CPMs with the advertising network for game sites
- [Publisher Collective | Get better CPMs with the advertising network for game sites](https://markposition.wordpress.com/2022/04/28/publisher-collective-get-better-cpms-with-the-advertising-network-for-game-sites/)
- [April 28, 2022](https://markposition.wordpress.com/2022/04/28/publisher-collective-get-better-cpms-with-the-advertising-network-for-game-sites/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/28/publisher-collective-get-better-cpms-with-the-advertising-network-for-game-sites/#respond)
https://www.publisher-collective.com/
- [https://www.publisher-collective.com/](https://www.publisher-collective.com/)

## boost-your-active-view-score-in-ad-manager
- [boost-your-active-view-score-in-ad-manager](https://markposition.wordpress.com/2022/04/28/boost-your-active-view-score-in-ad-manager/)
- [April 28, 2022](https://markposition.wordpress.com/2022/04/28/boost-your-active-view-score-in-ad-manager/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/28/boost-your-active-view-score-in-ad-manager/#respond)
https://skillshop.exceedlms.com/student/activity/17109-boost-your-active-view-score-in-ad-manager
- [https://skillshop.exceedlms.com/student/activity/17109-boost-your-active-view-score-in-ad-manager](https://skillshop.exceedlms.com/student/activity/17109-boost-your-active-view-score-in-ad-manager)

## Waytogrow – Earn more on your advertising space
- [Waytogrow – Earn more on your advertising space](https://markposition.wordpress.com/2022/04/22/waytogrow-earn-more-on-your-advertising-space/)
- [April 22, 2022](https://markposition.wordpress.com/2022/04/22/waytogrow-earn-more-on-your-advertising-space/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/22/waytogrow-earn-more-on-your-advertising-space/#respond)
https://www.waytogrow.com/
- [https://www.waytogrow.com/](https://www.waytogrow.com/)

## Smart Adserver | The Most Powerful Adserving and RTB Platform
- [Smart Adserver | The Most Powerful Adserving and RTB Platform](https://markposition.wordpress.com/2022/04/21/smart-adserver-the-most-powerful-adserving-and-rtb-platform-2/)
- [April 21, 2022](https://markposition.wordpress.com/2022/04/21/smart-adserver-the-most-powerful-adserving-and-rtb-platform-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/21/smart-adserver-the-most-powerful-adserving-and-rtb-platform-2/#respond)
https://smartadserver.com/
- [https://smartadserver.com/](https://smartadserver.com/)

## Custom advertising solutions – Custom ad campaigns | Amazon Ads
- [Custom advertising solutions – Custom ad campaigns | Amazon Ads](https://markposition.wordpress.com/2022/04/21/custom-advertising-solutions-custom-ad-campaigns-amazon-ads/)
- [April 21, 2022](https://markposition.wordpress.com/2022/04/21/custom-advertising-solutions-custom-ad-campaigns-amazon-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/21/custom-advertising-solutions-custom-ad-campaigns-amazon-ads/#respond)
https://advertising.amazon.com/solutions/products/custom-solutions
- [https://advertising.amazon.com/solutions/products/custom-solutions](https://advertising.amazon.com/solutions/products/custom-solutions)

## Amazon Marketing Cloud – Advanced media analytics and insights | Amazon Ads
- [Amazon Marketing Cloud – Advanced media analytics and insights | Amazon Ads](https://markposition.wordpress.com/2022/04/21/amazon-marketing-cloud-advanced-media-analytics-and-insights-amazon-ads/)
- [April 21, 2022](https://markposition.wordpress.com/2022/04/21/amazon-marketing-cloud-advanced-media-analytics-and-insights-amazon-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/21/amazon-marketing-cloud-advanced-media-analytics-and-insights-amazon-ads/#respond)
https://advertising.amazon.com/solutions/products/amazon-marketing-cloud
- [https://advertising.amazon.com/solutions/products/amazon-marketing-cloud](https://advertising.amazon.com/solutions/products/amazon-marketing-cloud)

## Amazon DSP – Create campaigns with our Demand Side Platform | Amazon Ads
- [Amazon DSP – Create campaigns with our Demand Side Platform | Amazon Ads](https://markposition.wordpress.com/2022/04/21/amazon-dsp-create-campaigns-with-our-demand-side-platform-amazon-ads/)
- [April 21, 2022](https://markposition.wordpress.com/2022/04/21/amazon-dsp-create-campaigns-with-our-demand-side-platform-amazon-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/21/amazon-dsp-create-campaigns-with-our-demand-side-platform-amazon-ads/#respond)
https://advertising.amazon.com/solutions/products/amazon-dsp
- [https://advertising.amazon.com/solutions/products/amazon-dsp](https://advertising.amazon.com/solutions/products/amazon-dsp)

## Learning console – Online advertising courses and PPC certifications | Amazon Ads
- [Learning console – Online advertising courses and PPC certifications | Amazon Ads](https://markposition.wordpress.com/2022/04/21/learning-console-online-advertising-courses-and-ppc-certifications-amazon-ads-2/)
- [April 21, 2022](https://markposition.wordpress.com/2022/04/21/learning-console-online-advertising-courses-and-ppc-certifications-amazon-ads-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/21/learning-console-online-advertising-courses-and-ppc-certifications-amazon-ads-2/#respond)
https://advertising.amazon.com/resources/learning-console
- [https://advertising.amazon.com/resources/learning-console](https://advertising.amazon.com/resources/learning-console)

## Sponsored Display ads – Create display advertising campaigns | Amazon Ads
- [Sponsored Display ads – Create display advertising campaigns | Amazon Ads](https://markposition.wordpress.com/2022/04/21/sponsored-display-ads-create-display-advertising-campaigns-amazon-ads/)
- [April 21, 2022](https://markposition.wordpress.com/2022/04/21/sponsored-display-ads-create-display-advertising-campaigns-amazon-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/21/sponsored-display-ads-create-display-advertising-campaigns-amazon-ads/#respond)
https://advertising.amazon.com/solutions/products/sponsored-display
- [https://advertising.amazon.com/solutions/products/sponsored-display](https://advertising.amazon.com/solutions/products/sponsored-display)

## Amazon Ads: Online advertising for businesses of all sizes | Amazon Ads
- [Amazon Ads: Online advertising for businesses of all sizes | Amazon Ads](https://markposition.wordpress.com/2022/04/21/amazon-ads-online-advertising-for-businesses-of-all-sizes-amazon-ads-2/)
- [April 21, 2022](https://markposition.wordpress.com/2022/04/21/amazon-ads-online-advertising-for-businesses-of-all-sizes-amazon-ads-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/21/amazon-ads-online-advertising-for-businesses-of-all-sizes-amazon-ads-2/#respond)
https://advertising.amazon.com/
- [https://advertising.amazon.com/](https://advertising.amazon.com/)

## Sizmek Ad Suite – DCO, creative building, ad serving | Amazon Ads
- [Sizmek Ad Suite – DCO, creative building, ad serving | Amazon Ads](https://markposition.wordpress.com/2022/04/21/sizmek-ad-suite-dco-creative-building-ad-serving-amazon-ads/)
- [April 21, 2022](https://markposition.wordpress.com/2022/04/21/sizmek-ad-suite-dco-creative-building-ad-serving-amazon-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/21/sizmek-ad-suite-dco-creative-building-ad-serving-amazon-ads/#respond)
https://advertising.amazon.com/solutions/products/sizmek-ad-suite
- [https://advertising.amazon.com/solutions/products/sizmek-ad-suite](https://advertising.amazon.com/solutions/products/sizmek-ad-suite)

## Drive Advertising Revenue with Google Ad Manager : Google
- [Drive Advertising Revenue with Google Ad Manager : Google](https://markposition.wordpress.com/2022/04/18/drive-advertising-revenue-with-google-ad-manager-google-4/)
- [April 18, 2022](https://markposition.wordpress.com/2022/04/18/drive-advertising-revenue-with-google-ad-manager-google-4/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/18/drive-advertising-revenue-with-google-ad-manager-google-4/#respond)
https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager
- [https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager](https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager)

## ads settings google
- [ads settings google](https://markposition.wordpress.com/2022/04/15/ads-settings-google/)
- [April 15, 2022](https://markposition.wordpress.com/2022/04/15/ads-settings-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/15/ads-settings-google/#respond)
https://adssettings.google.com/authenticated
- [https://adssettings.google.com/authenticated](https://adssettings.google.com/authenticated)

## Linker – Content Discovery Platform
- [Linker – Content Discovery Platform](https://markposition.wordpress.com/2022/04/15/linker-content-discovery-platform/)
- [April 15, 2022](https://markposition.wordpress.com/2022/04/15/linker-content-discovery-platform/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/15/linker-content-discovery-platform/#respond)
https://linker.hr/
- [https://linker.hr/](https://linker.hr/)

## Funding Choices API | Google Developers
- [Funding Choices API | Google Developers](https://markposition.wordpress.com/2022/04/14/funding-choices-api-google-developers/)
- [April 14, 2022](https://markposition.wordpress.com/2022/04/14/funding-choices-api-google-developers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/14/funding-choices-api-google-developers/#respond)
https://developers.google.com/funding-choices
- [https://developers.google.com/funding-choices](https://developers.google.com/funding-choices)

## Privacy checks in Ads Data Hub | Google Developers
- [Privacy checks in Ads Data Hub | Google Developers](https://markposition.wordpress.com/2022/04/14/privacy-checks-in-ads-data-hub-google-developers/)
- [April 14, 2022](https://markposition.wordpress.com/2022/04/14/privacy-checks-in-ads-data-hub-google-developers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/14/privacy-checks-in-ads-data-hub-google-developers/#respond)
https://developers.google.com/ads-data-hub/guides/privacy-checks
- [https://developers.google.com/ads-data-hub/guides/privacy-checks](https://developers.google.com/ads-data-hub/guides/privacy-checks)

## Ads Data Hub | Google Developers
- [Ads Data Hub | Google Developers](https://markposition.wordpress.com/2022/04/14/ads-data-hub-google-developers/)
- [April 14, 2022](https://markposition.wordpress.com/2022/04/14/ads-data-hub-google-developers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/14/ads-data-hub-google-developers/#respond)
https://developers.google.com/ads-data-hub
- [https://developers.google.com/ads-data-hub](https://developers.google.com/ads-data-hub)

## Google Ad Manager – Privacy & messaging
- [Google Ad Manager – Privacy & messaging](https://markposition.wordpress.com/2022/04/13/google-ad-manager-privacy-messaging/)
- [April 13, 2022](https://markposition.wordpress.com/2022/04/13/google-ad-manager-privacy-messaging/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/13/google-ad-manager-privacy-messaging/#respond)
https://admanager.google.com/22694377933#privacy_and_messaging/ad_blocking/education
- [https://admanager.google.com/22694377933#privacy_and_messaging/ad_blocking/education](https://admanager.google.com/22694377933#privacy_and_messaging/ad_blocking/education)

## Google Ads Integration | Ortto
- [Google Ads Integration | Ortto](https://markposition.wordpress.com/2022/04/06/google-ads-integration-ortto/)
- [April 6, 2022](https://markposition.wordpress.com/2022/04/06/google-ads-integration-ortto/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/06/google-ads-integration-ortto/#respond)
https://ortto.com/integrations/google-ads/
- [https://ortto.com/integrations/google-ads/](https://ortto.com/integrations/google-ads/)

## Cloudflare’s Privacy Policy | Cloudflare
- [Cloudflare’s Privacy Policy | Cloudflare](https://markposition.wordpress.com/2022/04/06/cloudflares-privacy-policy-cloudflare/)
- [April 6, 2022](https://markposition.wordpress.com/2022/04/06/cloudflares-privacy-policy-cloudflare/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/06/cloudflares-privacy-policy-cloudflare/#respond)
https://www.cloudflare.com/privacypolicy/
- [https://www.cloudflare.com/privacypolicy/](https://www.cloudflare.com/privacypolicy/)

## CJ.com Home
- [CJ.com Home](https://markposition.wordpress.com/2022/04/06/cj-com-home/)
- [April 6, 2022](https://markposition.wordpress.com/2022/04/06/cj-com-home/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/06/cj-com-home/#respond)
https://www.cj.com/
- [https://www.cj.com/](https://www.cj.com/)

## Xaxis – The outcome media company
- [Xaxis – The outcome media company](https://markposition.wordpress.com/2022/04/06/xaxis-the-outcome-media-company/)
- [April 6, 2022](https://markposition.wordpress.com/2022/04/06/xaxis-the-outcome-media-company/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/06/xaxis-the-outcome-media-company/#respond)
https://www.xaxis.com/
- [https://www.xaxis.com/](https://www.xaxis.com/)

## Services Privacy Policy | Oracle
- [Services Privacy Policy | Oracle](https://markposition.wordpress.com/2022/04/06/services-privacy-policy-oracle/)
- [April 6, 2022](https://markposition.wordpress.com/2022/04/06/services-privacy-policy-oracle/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/06/services-privacy-policy-oracle/#respond)
https://www.oracle.com/legal/privacy/services-privacy-policy.html
- [https://www.oracle.com/legal/privacy/services-privacy-policy.html](https://www.oracle.com/legal/privacy/services-privacy-policy.html)

## AdMedia | Premier Advertising Network | Reach 200M+ US Users
- [AdMedia | Premier Advertising Network | Reach 200M+ US Users](https://markposition.wordpress.com/2022/04/04/admedia-premier-advertising-network-reach-200m-us-users/)
- [April 4, 2022](https://markposition.wordpress.com/2022/04/04/admedia-premier-advertising-network-reach-200m-us-users/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/04/admedia-premier-advertising-network-reach-200m-us-users/#respond)
https://admedia.com/
- [https://admedia.com/](https://admedia.com/)

## Monetize
- [Monetize](https://markposition.wordpress.com/2022/04/04/monetize/)
- [April 4, 2022](https://markposition.wordpress.com/2022/04/04/monetize/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/04/04/monetize/#respond)
https://www.monetize.com/
- [https://www.monetize.com/](https://www.monetize.com/)

## Adobe Advertising Cloud: Programmatic Media Buying | Adobe for Business
- [Adobe Advertising Cloud: Programmatic Media Buying | Adobe for Business](https://markposition.wordpress.com/2022/03/29/adobe-advertising-cloud-programmatic-media-buying-adobe-for-business/)
- [March 29, 2022](https://markposition.wordpress.com/2022/03/29/adobe-advertising-cloud-programmatic-media-buying-adobe-for-business/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/29/adobe-advertising-cloud-programmatic-media-buying-adobe-for-business/#respond)
https://business.adobe.com/products/advertising/adobe-advertising-cloud.html
- [https://business.adobe.com/products/advertising/adobe-advertising-cloud.html](https://business.adobe.com/products/advertising/adobe-advertising-cloud.html)

## Your Online Choices | EDAA
- [Your Online Choices | EDAA](https://markposition.wordpress.com/2022/03/29/your-online-choices-edaa/)
- [March 29, 2022](https://markposition.wordpress.com/2022/03/29/your-online-choices-edaa/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/29/your-online-choices-edaa/#respond)
https://youronlinechoices.eu/
- [https://youronlinechoices.eu/](https://youronlinechoices.eu/)

## WebChoices: Digital Advertising Alliance’s Consumer Choice Tool for Web US
- [WebChoices: Digital Advertising Alliance’s Consumer Choice Tool for Web US](https://markposition.wordpress.com/2022/03/29/webchoices-digital-advertising-alliances-consumer-choice-tool-for-web-us-3/)
- [March 29, 2022](https://markposition.wordpress.com/2022/03/29/webchoices-digital-advertising-alliances-consumer-choice-tool-for-web-us-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/29/webchoices-digital-advertising-alliances-consumer-choice-tool-for-web-us-3/#respond)
https://optout.aboutads.info/
- [https://optout.aboutads.info/](https://optout.aboutads.info/)

## For Consumers – European Interactive Digital Advertising Alliance
- [For Consumers – European Interactive Digital Advertising Alliance](https://markposition.wordpress.com/2022/03/29/for-consumers-european-interactive-digital-advertising-alliance/)
- [March 29, 2022](https://markposition.wordpress.com/2022/03/29/for-consumers-european-interactive-digital-advertising-alliance/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/29/for-consumers-european-interactive-digital-advertising-alliance/#respond)
https://edaa.eu/what-we-do/for-consumers/
- [https://edaa.eu/what-we-do/for-consumers/](https://edaa.eu/what-we-do/for-consumers/)

## Data Privacy Audit | See If Your Website Is Data Compliant
- [Data Privacy Audit | See If Your Website Is Data Compliant](https://markposition.wordpress.com/2022/03/25/data-privacy-audit-see-if-your-website-is-data-compliant/)
- [March 25, 2022](https://markposition.wordpress.com/2022/03/25/data-privacy-audit-see-if-your-website-is-data-compliant/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/25/data-privacy-audit-see-if-your-website-is-data-compliant/#respond)
https://usercentrics.com/data-privacy-audit/
- [https://usercentrics.com/data-privacy-audit/](https://usercentrics.com/data-privacy-audit/)

## Drive Advertising Revenue with Google Ad Manager : Google
- [Drive Advertising Revenue with Google Ad Manager : Google](https://markposition.wordpress.com/2022/03/18/drive-advertising-revenue-with-google-ad-manager-google-3/)
- [March 18, 2022](https://markposition.wordpress.com/2022/03/18/drive-advertising-revenue-with-google-ad-manager-google-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/18/drive-advertising-revenue-with-google-ad-manager-google-3/#respond)
https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager
- [https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager](https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager)

## Create Reports in Google Ad Manager : Google
- [Create Reports in Google Ad Manager : Google](https://markposition.wordpress.com/2022/03/18/create-reports-in-google-ad-manager-google-2/)
- [March 18, 2022](https://markposition.wordpress.com/2022/03/18/create-reports-in-google-ad-manager-google-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/18/create-reports-in-google-ad-manager-google-2/#respond)
https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager
- [https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager](https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager)

## Online Video Advertising Campaigns – YouTube Advertising
- [Online Video Advertising Campaigns – YouTube Advertising](https://markposition.wordpress.com/2022/03/18/online-video-advertising-campaigns-youtube-advertising-3/)
- [March 18, 2022](https://markposition.wordpress.com/2022/03/18/online-video-advertising-campaigns-youtube-advertising-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/18/online-video-advertising-campaigns-youtube-advertising-3/#respond)
https://www.youtube.com/intl/en_US/ads/
- [https://www.youtube.com/intl/en_US/ads/](https://www.youtube.com/intl/en_US/ads/)

## Profit Whales | Full-service Amazon marketing agency for your brand!
- [Profit Whales | Full-service Amazon marketing agency for your brand!](https://markposition.wordpress.com/2022/03/18/profit-whales-full-service-amazon-marketing-agency-for-your-brand/)
- [March 18, 2022](https://markposition.wordpress.com/2022/03/18/profit-whales-full-service-amazon-marketing-agency-for-your-brand/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/18/profit-whales-full-service-amazon-marketing-agency-for-your-brand/#respond)
https://profitwhales.com/
- [https://profitwhales.com/](https://profitwhales.com/)

## Learning console – Online advertising courses and PPC certifications | Amazon Ads
- [Learning console – Online advertising courses and PPC certifications | Amazon Ads](https://markposition.wordpress.com/2022/03/17/learning-console-online-advertising-courses-and-ppc-certifications-amazon-ads/)
- [March 17, 2022](https://markposition.wordpress.com/2022/03/17/learning-console-online-advertising-courses-and-ppc-certifications-amazon-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/17/learning-console-online-advertising-courses-and-ppc-certifications-amazon-ads/#respond)
https://advertising.amazon.com/resources/learning-console
- [https://advertising.amazon.com/resources/learning-console](https://advertising.amazon.com/resources/learning-console)

## Amazon Ads: Online advertising for businesses of all sizes | Amazon Ads
- [Amazon Ads: Online advertising for businesses of all sizes | Amazon Ads](https://markposition.wordpress.com/2022/03/17/amazon-ads-online-advertising-for-businesses-of-all-sizes-amazon-ads/)
- [March 17, 2022](https://markposition.wordpress.com/2022/03/17/amazon-ads-online-advertising-for-businesses-of-all-sizes-amazon-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/17/amazon-ads-online-advertising-for-businesses-of-all-sizes-amazon-ads/#respond)
https://advertising.amazon.com/
- [https://advertising.amazon.com/](https://advertising.amazon.com/)

## Get Started with Google Publisher Tags | Google Developers
- [Get Started with Google Publisher Tags | Google Developers](https://markposition.wordpress.com/2022/03/16/get-started-with-google-publisher-tags-google-developers-2/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/get-started-with-google-publisher-tags-google-developers-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/get-started-with-google-publisher-tags-google-developers-2/#respond)
https://developers.google.com/publisher-tag/guides/get-started
- [https://developers.google.com/publisher-tag/guides/get-started](https://developers.google.com/publisher-tag/guides/get-started)

## Ad sizes | Google Publisher Tag | Google Developers
- [Ad sizes | Google Publisher Tag | Google Developers](https://markposition.wordpress.com/2022/03/16/ad-sizes-google-publisher-tag-google-developers/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/ad-sizes-google-publisher-tag-google-developers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/ad-sizes-google-publisher-tag-google-developers/#respond)
https://developers.google.com/publisher-tag/guides/get-started
- [https://developers.google.com/publisher-tag/guides/get-started](https://developers.google.com/publisher-tag/guides/get-started)

## Drive Advertising Revenue with Google Ad Manager : Google
- [Drive Advertising Revenue with Google Ad Manager : Google](https://markposition.wordpress.com/2022/03/16/drive-advertising-revenue-with-google-ad-manager-google-2/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/drive-advertising-revenue-with-google-ad-manager-google-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/drive-advertising-revenue-with-google-ad-manager-google-2/#respond)
https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager
- [https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager](https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager)

## Configure Mobile In-App Ads Using Ad Manager : Google
- [Configure Mobile In-App Ads Using Ad Manager : Google](https://markposition.wordpress.com/2022/03/16/configure-mobile-in-app-ads-using-ad-manager-google/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/configure-mobile-in-app-ads-using-ad-manager-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/configure-mobile-in-app-ads-using-ad-manager-google/#respond)
https://skillshop.exceedlms.com/student/activity/75346-configure-mobile-in-app-ads-using-ad-manager
- [https://skillshop.exceedlms.com/student/activity/75346-configure-mobile-in-app-ads-using-ad-manager](https://skillshop.exceedlms.com/student/activity/75346-configure-mobile-in-app-ads-using-ad-manager)

## Fundamentals of Video : Google
- [Fundamentals of Video : Google](https://markposition.wordpress.com/2022/03/16/fundamentals-of-video-google/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/fundamentals-of-video-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/fundamentals-of-video-google/#respond)
https://skillshop.exceedlms.com/student/activity/75345-fundamentals-of-video
- [https://skillshop.exceedlms.com/student/activity/75345-fundamentals-of-video](https://skillshop.exceedlms.com/student/activity/75345-fundamentals-of-video)

## Review and Manage Ads in Google Ad Manager : Google
- [Review and Manage Ads in Google Ad Manager : Google](https://markposition.wordpress.com/2022/03/16/review-and-manage-ads-in-google-ad-manager-google/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/review-and-manage-ads-in-google-ad-manager-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/review-and-manage-ads-in-google-ad-manager-google/#respond)
https://skillshop.exceedlms.com/student/activity/17116-review-and-manage-ads-in-google-ad-manager
- [https://skillshop.exceedlms.com/student/activity/17116-review-and-manage-ads-in-google-ad-manager](https://skillshop.exceedlms.com/student/activity/17116-review-and-manage-ads-in-google-ad-manager)

## Manage Ads with Rules and Protections : Google
- [Manage Ads with Rules and Protections : Google](https://markposition.wordpress.com/2022/03/16/manage-ads-with-rules-and-protections-google/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/manage-ads-with-rules-and-protections-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/manage-ads-with-rules-and-protections-google/#respond)
https://skillshop.exceedlms.com/student/activity/379130-manage-ads-with-rules-and-protections-skillshop
- [https://skillshop.exceedlms.com/student/activity/379130-manage-ads-with-rules-and-protections-skillshop](https://skillshop.exceedlms.com/student/activity/379130-manage-ads-with-rules-and-protections-skillshop)

## Explore Programmatic Capabilities in Google Ad Manager : Google
- [Explore Programmatic Capabilities in Google Ad Manager : Google](https://markposition.wordpress.com/2022/03/16/explore-programmatic-capabilities-in-google-ad-manager-google/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/explore-programmatic-capabilities-in-google-ad-manager-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/explore-programmatic-capabilities-in-google-ad-manager-google/#respond)
https://skillshop.exceedlms.com/student/activity/17114-explore-programmatic-capabilities-in-google-ad-manager
- [https://skillshop.exceedlms.com/student/activity/17114-explore-programmatic-capabilities-in-google-ad-manager](https://skillshop.exceedlms.com/student/activity/17114-explore-programmatic-capabilities-in-google-ad-manager)

## Create Reports in Google Ad Manager : Google
- [Create Reports in Google Ad Manager : Google](https://markposition.wordpress.com/2022/03/16/create-reports-in-google-ad-manager-google/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/create-reports-in-google-ad-manager-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/create-reports-in-google-ad-manager-google/#respond)
https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager
- [https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager](https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager)

## Forecast Your Inventory Using Ad Manager : Google
- [Forecast Your Inventory Using Ad Manager : Google](https://markposition.wordpress.com/2022/03/16/forecast-your-inventory-using-ad-manager-google/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/forecast-your-inventory-using-ad-manager-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/forecast-your-inventory-using-ad-manager-google/#respond)
https://skillshop.exceedlms.com/student/activity/17112-forecast-your-inventory-using-ad-manager
- [https://skillshop.exceedlms.com/student/activity/17112-forecast-your-inventory-using-ad-manager](https://skillshop.exceedlms.com/student/activity/17112-forecast-your-inventory-using-ad-manager)

## Optimize Creatives with Ad Manager : Google
- [Optimize Creatives with Ad Manager : Google](https://markposition.wordpress.com/2022/03/16/optimize-creatives-with-ad-manager-google/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/optimize-creatives-with-ad-manager-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/optimize-creatives-with-ad-manager-google/#respond)
https://skillshop.exceedlms.com/student/activity/17111-optimize-creatives-with-ad-manager
- [https://skillshop.exceedlms.com/student/activity/17111-optimize-creatives-with-ad-manager](https://skillshop.exceedlms.com/student/activity/17111-optimize-creatives-with-ad-manager)

## Deliver Ads Using Google Ad Manager : Google
- [Deliver Ads Using Google Ad Manager : Google](https://markposition.wordpress.com/2022/03/16/deliver-ads-using-google-ad-manager-google/)
- [March 16, 2022](https://markposition.wordpress.com/2022/03/16/deliver-ads-using-google-ad-manager-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/16/deliver-ads-using-google-ad-manager-google/#respond)
https://skillshop.exceedlms.com/student/activity/17110-deliver-ads-using-google-ad-manager
- [https://skillshop.exceedlms.com/student/activity/17110-deliver-ads-using-google-ad-manager](https://skillshop.exceedlms.com/student/activity/17110-deliver-ads-using-google-ad-manager)

## Google Ad Traffic Quality
- [Google Ad Traffic Quality](https://markposition.wordpress.com/2022/03/14/google-ad-traffic-quality/)
- [March 14, 2022](https://markposition.wordpress.com/2022/03/14/google-ad-traffic-quality/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/14/google-ad-traffic-quality/#respond)
https://www.google.com/ads/adtrafficquality/
- [https://www.google.com/ads/adtrafficquality/](https://www.google.com/ads/adtrafficquality/)

## Vodič za ads.txt – Google AdSense Pomoć
- [Vodič za ads.txt – Google AdSense Pomoć](https://markposition.wordpress.com/2022/03/14/vodic-za-ads-txt-google-adsense-pomoc/)
- [March 14, 2022](https://markposition.wordpress.com/2022/03/14/vodic-za-ads-txt-google-adsense-pomoc/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/14/vodic-za-ads-txt-google-adsense-pomoc/#respond)
https://support.google.com/adsense/answer/7532444?hl=hr
- [https://support.google.com/adsense/answer/7532444?hl=hr](https://support.google.com/adsense/answer/7532444?hl=hr)

## Alat za rješavanje problema s datotekom ads.txt – Google AdSense Pomoć
- [Alat za rješavanje problema s datotekom ads.txt – Google AdSense Pomoć](https://markposition.wordpress.com/2022/03/14/alat-za-rjesavanje-problema-s-datotekom-ads-txt-google-adsense-pomoc/)
- [March 14, 2022](https://markposition.wordpress.com/2022/03/14/alat-za-rjesavanje-problema-s-datotekom-ads-txt-google-adsense-pomoc/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/14/alat-za-rjesavanje-problema-s-datotekom-ads-txt-google-adsense-pomoc/#respond)
https://support.google.com/adsense/troubleshooter/9556696?hl=hr#ts=9806100%2C9806109
- [https://support.google.com/adsense/troubleshooter/9556696?hl=hr#ts=9806100%2C9806109](https://support.google.com/adsense/troubleshooter/9556696?hl=hr#ts=9806100%2C9806109)

## Actions on Google
- [Actions on Google](https://markposition.wordpress.com/2022/03/13/actions-on-google/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/actions-on-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/actions-on-google/#respond)
https://console.actions.google.com/
- [https://console.actions.google.com/](https://console.actions.google.com/u/0/)

## AdSense Management API | Google Developers
- [AdSense Management API | Google Developers](https://markposition.wordpress.com/2022/03/13/adsense-management-api-google-developers/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/adsense-management-api-google-developers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/adsense-management-api-google-developers/#respond)
https://developers.google.com/adsense/management
- [https://developers.google.com/adsense/management](https://developers.google.com/adsense/management)

## The Commerce Media Platform for the Open Internet | Criteo
- [The Commerce Media Platform for the Open Internet | Criteo](https://markposition.wordpress.com/2022/03/13/the-commerce-media-platform-for-the-open-internet-criteo/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/the-commerce-media-platform-for-the-open-internet-criteo/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/the-commerce-media-platform-for-the-open-internet-criteo/#respond)
https://www.criteo.com/
- [https://www.criteo.com/](https://www.criteo.com/)

## Ad exchange – Wikipedia
- [Ad exchange – Wikipedia](https://markposition.wordpress.com/2022/03/13/ad-exchange-wikipedia-2/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/ad-exchange-wikipedia-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/ad-exchange-wikipedia-2/#respond)
https://en.wikipedia.org/wiki/Ad_exchange
- [https://en.wikipedia.org/wiki/Ad_exchange](https://en.wikipedia.org/wiki/Ad_exchange)

## Digiday – Digital Content, Digital Advertising, Digital Marketing
- [Digiday – Digital Content, Digital Advertising, Digital Marketing](https://markposition.wordpress.com/2022/03/13/digiday-digital-content-digital-advertising-digital-marketing-2/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/digiday-digital-content-digital-advertising-digital-marketing-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/digiday-digital-content-digital-advertising-digital-marketing-2/#respond)
https://digiday.com/
- [https://digiday.com/](https://digiday.com/)

## 234 – Measure – Analyze – Optimize
- [234 – Measure – Analyze – Optimize](https://markposition.wordpress.com/2022/03/13/234-measure-analyze-optimize/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/234-measure-analyze-optimize/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/234-measure-analyze-optimize/#respond)
https://234.hr/
- [https://234.hr/](https://234.hr/)

## Google Ad Manager – Integrated Advertising Management Platform
- [Google Ad Manager – Integrated Advertising Management Platform](https://markposition.wordpress.com/2022/03/13/google-ad-manager-integrated-advertising-management-platform-4/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/google-ad-manager-integrated-advertising-management-platform-4/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/google-ad-manager-integrated-advertising-management-platform-4/#respond)
https://admanager.google.com/home/
- [https://admanager.google.com/home/](https://admanager.google.com/home/)

## Google Ad Manager : Google
- [Google Ad Manager : Google](https://markposition.wordpress.com/2022/03/13/google-ad-manager-google-2/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/google-ad-manager-google-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/google-ad-manager-google-2/#respond)
https://skillshop.exceedlms.com/student/catalog/list?category_ids=2842-google-ad-manager
- [https://skillshop.exceedlms.com/student/catalog/list?category_ids=2842-google-ad-manager](https://skillshop.exceedlms.com/student/catalog/list?category_ids=2842-google-ad-manager)

## Pronađite partnera – izdavača | Certificirani partner – izdavač – Google
- [Pronađite partnera – izdavača | Certificirani partner – izdavač – Google](https://markposition.wordpress.com/2022/03/13/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google-3/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google-3/#respond)
google.com/ads/publisher/partners/find-a-partner/ Ezoic
- [google.com/ads/publisher/partners/find-a-partner/ Ezoic](https://www.google.com/ads/publisher/partners/find-a-partner/#!?modal_active=modal-ezoic)
- [Home](https://www.ezoic.com/)

## Pronađite partnera – izdavača | Certificirani partner – izdavač – Google – ads publisher – find a partner
- [Pronađite partnera – izdavača | Certificirani partner – izdavač – Google – ads publisher – find a partner](https://markposition.wordpress.com/2022/03/13/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google-ads-publisher-find-a-partner/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google-ads-publisher-find-a-partner/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google-ads-publisher-find-a-partner/#respond)
https://www.google.com/ads/publisher/partners/find-a-partner/
- [https://www.google.com/ads/publisher/partners/find-a-partner/](https://www.google.com/ads/publisher/partners/find-a-partner/#!?modal_active=none)

## Google Certified Partner Program – Google – ads – publisher – partners
- [Google Certified Partner Program – Google – ads – publisher – partners](https://markposition.wordpress.com/2022/03/13/google-certified-partner-program-google-ads-publisher-partners/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/google-certified-partner-program-google-ads-publisher-partners/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/google-certified-partner-program-google-ads-publisher-partners/#respond)
https://www.google.com/ads/publisher/partners/
- [https://www.google.com/ads/publisher/partners/](https://www.google.com/ads/publisher/partners/)

## “How Ads Work on YouTube”
- [“How Ads Work on YouTube”](https://markposition.wordpress.com/2022/03/13/how-ads-work-on-youtube/)
- [March 13, 2022](https://markposition.wordpress.com/2022/03/13/how-ads-work-on-youtube/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/13/how-ads-work-on-youtube/#respond)

## Ad Inserter – Ad Manager & AdSense Ads – | WordPress.org Hrvatski
- [Ad Inserter – Ad Manager & AdSense Ads – | WordPress.org Hrvatski](https://markposition.wordpress.com/2022/03/11/ad-inserter-ad-manager-adsense-ads-wordpress-org-hrvatski/)
- [March 11, 2022](https://markposition.wordpress.com/2022/03/11/ad-inserter-ad-manager-adsense-ads-wordpress-org-hrvatski/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/11/ad-inserter-ad-manager-adsense-ads-wordpress-org-hrvatski/#respond)
https://wordpress.org/plugins/ad-inserter/
- [https://wordpress.org/plugins/ad-inserter/](https://hr.wordpress.org/plugins/ad-inserter/)

## Ad Inserter Pro – Advanced WordPress Ad Management Plugin
- [Ad Inserter Pro – Advanced WordPress Ad Management Plugin](https://markposition.wordpress.com/2022/03/11/ad-inserter-pro-advanced-wordpress-ad-management-plugin/)
- [March 11, 2022](https://markposition.wordpress.com/2022/03/11/ad-inserter-pro-advanced-wordpress-ad-management-plugin/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/11/ad-inserter-pro-advanced-wordpress-ad-management-plugin/#respond)
https://adinserter.pro/
- [https://adinserter.pro/](https://adinserter.pro/)

## SafeFrame Implementation Guidelines
- [SafeFrame Implementation Guidelines](https://markposition.wordpress.com/2022/03/11/safeframe-implementation-guidelines/)
- [March 11, 2022](https://markposition.wordpress.com/2022/03/11/safeframe-implementation-guidelines/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/11/safeframe-implementation-guidelines/#respond)
https://www.iab.com/guidelines/safeframe/
- [https://www.iab.com/guidelines/safeframe/](https://www.iab.com/guidelines/safeframe/)

## Using your Ad Speed Home dashboard – Google Ad Manager Help
- [Using your Ad Speed Home dashboard – Google Ad Manager Help](https://markposition.wordpress.com/2022/03/11/using-your-ad-speed-home-dashboard-google-ad-manager-help/)
- [March 11, 2022](https://markposition.wordpress.com/2022/03/11/using-your-ad-speed-home-dashboard-google-ad-manager-help/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/11/using-your-ad-speed-home-dashboard-google-ad-manager-help/#respond)
https://support.google.com/admanager/answer/9203630?hl=en
- [https://support.google.com/admanager/answer/9203630?hl=en](https://support.google.com/admanager/answer/9203630?hl=en)

## Google Ads
- [Google Ads](https://markposition.wordpress.com/2022/03/11/google-ads-2/)
- [March 11, 2022](https://markposition.wordpress.com/2022/03/11/google-ads-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/11/google-ads-2/#respond)
https://ads.google.com/
- [https://ads.google.com/](https://ads.google.com/intl/hr_hr/home/)

## Google Ads Status Dashboard
- [Google Ads Status Dashboard](https://markposition.wordpress.com/2022/03/11/google-ads-status-dashboard-2/)
- [March 11, 2022](https://markposition.wordpress.com/2022/03/11/google-ads-status-dashboard-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/11/google-ads-status-dashboard-2/#respond)
https://ads.google.com/status/publisher/
- [https://ads.google.com/status/publisher/](https://ads.google.com/status/publisher/)

## Google Ads Data Processing Terms
- [Google Ads Data Processing Terms](https://markposition.wordpress.com/2022/03/11/google-ads-data-processing-terms/)
- [March 11, 2022](https://markposition.wordpress.com/2022/03/11/google-ads-data-processing-terms/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/11/google-ads-data-processing-terms/#respond)
https://business.safety.google/adsprocessorterms/
- [https://business.safety.google/adsprocessorterms/](https://business.safety.google/adsprocessorterms/)

## Business Data Responsibility – Data Safety, Protection & Privacy
- [Business Data Responsibility – Data Safety, Protection & Privacy](https://markposition.wordpress.com/2022/03/11/business-data-responsibility-data-safety-protection-privacy/)
- [March 11, 2022](https://markposition.wordpress.com/2022/03/11/business-data-responsibility-data-safety-protection-privacy/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/11/business-data-responsibility-data-safety-protection-privacy/#respond)
https://business.safety.google/
- [https://business.safety.google/](https://business.safety.google/)

## Get Started with Google Publisher Tags | Google Developers
- [Get Started with Google Publisher Tags | Google Developers](https://markposition.wordpress.com/2022/03/11/get-started-with-google-publisher-tags-google-developers/)
- [March 11, 2022](https://markposition.wordpress.com/2022/03/11/get-started-with-google-publisher-tags-google-developers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/11/get-started-with-google-publisher-tags-google-developers/#respond)
https://developers.google.com/publisher-tag/guides/get-started
- [https://developers.google.com/publisher-tag/guides/get-started](https://developers.google.com/publisher-tag/guides/get-started)

## Get Started with Search Ads 360 : Google
- [Get Started with Search Ads 360 : Google](https://markposition.wordpress.com/2022/03/11/get-started-with-search-ads-360-google/)
- [March 11, 2022](https://markposition.wordpress.com/2022/03/11/get-started-with-search-ads-360-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/11/get-started-with-search-ads-360-google/#respond)
https://skillshop.exceedlms.com/student/path/396050-get-started-with-search-ads-360
- [https://skillshop.exceedlms.com/student/path/396050-get-started-with-search-ads-360](https://skillshop.exceedlms.com/student/path/396050-get-started-with-search-ads-360)

## Google Ad Manager : Google
- [Google Ad Manager : Google](https://markposition.wordpress.com/2022/03/11/google-ad-manager-google/)
- [March 11, 2022](https://markposition.wordpress.com/2022/03/11/google-ad-manager-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/11/google-ad-manager-google/#respond)
https://skillshop.exceedlms.com/student/catalog/list?category_ids=2842-google-ad-manager
- [https://skillshop.exceedlms.com/student/catalog/list?category_ids=2842-google-ad-manager](https://skillshop.exceedlms.com/student/catalog/list?category_ids=2842-google-ad-manager)

## Partnerski program za izdavaštvo | Certificirani partner – izdavač – Google
- [Partnerski program za izdavaštvo | Certificirani partner – izdavač – Google](https://markposition.wordpress.com/2022/03/10/partnerski-program-za-izdavastvo-certificirani-partner-izdavac-google-3/)
- [March 10, 2022March 10, 2022](https://markposition.wordpress.com/2022/03/10/partnerski-program-za-izdavastvo-certificirani-partner-izdavac-google-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/10/partnerski-program-za-izdavastvo-certificirani-partner-izdavac-google-3/#respond)
https://www.google.com/ads/publisher/partners/
- [https://www.google.com/ads/publisher/partners/](https://www.google.com/ads/publisher/partners/)
- [become_a_gcpp](https://markposition.wordpress.com/wp-content/uploads/2022/08/18eda-become_a_gcpp.pdf)
- [Download](https://markposition.wordpress.com/wp-content/uploads/2022/08/18eda-become_a_gcpp.pdf)

## Marketing Cloud – Digital Marketing Platform – Salesforce.com
- [Marketing Cloud – Digital Marketing Platform – Salesforce.com](https://markposition.wordpress.com/2022/03/10/marketing-cloud-digital-marketing-platform-salesforce-com/)
- [March 10, 2022](https://markposition.wordpress.com/2022/03/10/marketing-cloud-digital-marketing-platform-salesforce-com/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/10/marketing-cloud-digital-marketing-platform-salesforce-com/#respond)
https://www.salesforce.com/products/marketing-cloud/overview/
- [https://www.salesforce.com/products/marketing-cloud/overview/](https://www.salesforce.com/products/marketing-cloud/overview/)

## Adobe Experience Platform
- [Adobe Experience Platform](https://markposition.wordpress.com/2022/03/10/adobe-experience-platform/)
- [March 10, 2022](https://markposition.wordpress.com/2022/03/10/adobe-experience-platform/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/10/adobe-experience-platform/#respond)
https://business.adobe.com/products/experience-platform/adobe-experience-platform.html
- [https://business.adobe.com/products/experience-platform/adobe-experience-platform.html](https://business.adobe.com/products/experience-platform/adobe-experience-platform.html)

## Publisher Ads Audits for Lighthouse | Google Developers
- [Publisher Ads Audits for Lighthouse | Google Developers](https://markposition.wordpress.com/2022/03/10/publisher-ads-audits-for-lighthouse-google-developers/)
- [March 10, 2022](https://markposition.wordpress.com/2022/03/10/publisher-ads-audits-for-lighthouse-google-developers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/10/publisher-ads-audits-for-lighthouse-google-developers/#respond)
https://developers.google.com/publisher-ads-audits
- [https://developers.google.com/publisher-ads-audits](https://developers.google.com/publisher-ads-audits)

## Setupad Blog | Latest AdTech News
- [Setupad Blog | Latest AdTech News](https://markposition.wordpress.com/2022/03/10/setupad-blog-latest-adtech-news/)
- [March 10, 2022September 26, 2022](https://markposition.wordpress.com/2022/03/10/setupad-blog-latest-adtech-news/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/10/setupad-blog-latest-adtech-news/#respond)
https://setupad.com/blog/
- [https://setupad.com/blog/](https://setupad.com/blog/)

## DoubleClick – Wikipedia
- [DoubleClick – Wikipedia](https://markposition.wordpress.com/2022/03/10/doubleclick-wikipedia/)
- [March 10, 2022](https://markposition.wordpress.com/2022/03/10/doubleclick-wikipedia/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/10/doubleclick-wikipedia/#respond)
https://en.wikipedia.org/wiki/DoubleClick
- [https://en.wikipedia.org/wiki/DoubleClick](https://en.wikipedia.org/wiki/DoubleClick)

## Google Ad Manager – Wikipedia
- [Google Ad Manager – Wikipedia](https://markposition.wordpress.com/2022/03/10/google-ad-manager-wikipedia-2/)
- [March 10, 2022](https://markposition.wordpress.com/2022/03/10/google-ad-manager-wikipedia-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/10/google-ad-manager-wikipedia-2/#respond)
https://en.wikipedia.org/wiki/Google_Ad_Manager
- [https://en.wikipedia.org/wiki/Google_Ad_Manager](https://en.wikipedia.org/wiki/Google_Ad_Manager)

## Drive Advertising Revenue with Google Ad Manager : Google
- [Drive Advertising Revenue with Google Ad Manager : Google](https://markposition.wordpress.com/2022/03/10/drive-advertising-revenue-with-google-ad-manager-google/)
- [March 10, 2022](https://markposition.wordpress.com/2022/03/10/drive-advertising-revenue-with-google-ad-manager-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/10/drive-advertising-revenue-with-google-ad-manager-google/#respond)
https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager
- [https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager](https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager)

## iab ads txt
- [iab ads txt](https://markposition.wordpress.com/2022/03/09/iab-ads-txt/)
- [March 9, 2022](https://markposition.wordpress.com/2022/03/09/iab-ads-txt/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/09/iab-ads-txt/#respond)
- [iab-openrtb-ads.txt-public-spec-1.0.2-3](https://markposition.wordpress.com/wp-content/uploads/2022/08/7db5d-iab-openrtb-ads.txt-public-spec-1.0.2-3.pdf)
- [Download](https://markposition.wordpress.com/wp-content/uploads/2022/08/7db5d-iab-openrtb-ads.txt-public-spec-1.0.2-3.pdf)

## Bing Webmaster Tools
- [Bing Webmaster Tools](https://markposition.wordpress.com/2022/03/08/bing-webmaster-tools-3/)
- [March 8, 2022](https://markposition.wordpress.com/2022/03/08/bing-webmaster-tools-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/08/bing-webmaster-tools-3/#respond)
https://www.bing.com/webmasters/about
- [https://www.bing.com/webmasters/about](https://www.bing.com/webmasters/about)

## In-Stream Ads | Meta for Creators
- [In-Stream Ads | Meta for Creators](https://markposition.wordpress.com/2022/03/02/in-stream-ads-meta-for-creators/)
- [March 2, 2022](https://markposition.wordpress.com/2022/03/02/in-stream-ads-meta-for-creators/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/03/02/in-stream-ads-meta-for-creators/#respond)
https://web.facebook.com/creators/tools/in-stream-ads
- [https://web.facebook.com/creators/tools/in-stream-ads](https://web.facebook.com/creators/tools/in-stream-ads)

## How to Make Money From Your Content on Facebook | Facebook for Business
- [How to Make Money From Your Content on Facebook | Facebook for Business](https://markposition.wordpress.com/2022/02/28/how-to-make-money-from-your-content-on-facebook-facebook-for-business/)
- [February 28, 2022](https://markposition.wordpress.com/2022/02/28/how-to-make-money-from-your-content-on-facebook-facebook-for-business/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/28/how-to-make-money-from-your-content-on-facebook-facebook-for-business/#respond)
https://web.facebook.com/business/learn/lessons/how-make-money-facebook
- [https://web.facebook.com/business/learn/lessons/how-make-money-facebook](https://web.facebook.com/business/learn/lessons/how-make-money-facebook)

## Instant Articles | Meta for Media
- [Instant Articles | Meta for Media](https://markposition.wordpress.com/2022/02/28/instant-articles-meta-for-media/)
- [February 28, 2022](https://markposition.wordpress.com/2022/02/28/instant-articles-meta-for-media/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/28/instant-articles-meta-for-media/#respond)
https://web.facebook.com/formedia/tools/instant-articles
- [https://web.facebook.com/formedia/tools/instant-articles](https://web.facebook.com/formedia/tools/instant-articles)

## Audience Network
- [Audience Network](https://markposition.wordpress.com/2022/02/27/audience-network/)
- [February 27, 2022](https://markposition.wordpress.com/2022/02/27/audience-network/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/27/audience-network/#respond)
https://hr-hr.facebook.com/audiencenetwork/monetize/bidding/learn
- [https://hr-hr.facebook.com/audiencenetwork/monetize/bidding/learn](https://hr-hr.facebook.com/audiencenetwork/monetize/bidding/learn)

## Earn Money From In-Stream Ads in Your Facebook Videos | Facebook for Business
- [Earn Money From In-Stream Ads in Your Facebook Videos | Facebook for Business](https://markposition.wordpress.com/2022/02/26/earn-money-from-in-stream-ads-in-your-facebook-videos-facebook-for-business/)
- [February 26, 2022](https://markposition.wordpress.com/2022/02/26/earn-money-from-in-stream-ads-in-your-facebook-videos-facebook-for-business/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/26/earn-money-from-in-stream-ads-in-your-facebook-videos-facebook-for-business/#respond)
https://web.facebook.com/business/learn/lessons/earn-money-in-stream-ads-videos
- [https://web.facebook.com/business/learn/lessons/earn-money-in-stream-ads-videos](https://web.facebook.com/business/learn/lessons/earn-money-in-stream-ads-videos)

## Comscore is a trusted currency for planning, transacting, and evaluating media across platforms.
- [Comscore is a trusted currency for planning, transacting, and evaluating media across platforms.](https://markposition.wordpress.com/2022/02/26/comscore-is-a-trusted-currency-for-planning-transacting-and-evaluating-media-across-platforms-2/)
- [February 26, 2022](https://markposition.wordpress.com/2022/02/26/comscore-is-a-trusted-currency-for-planning-transacting-and-evaluating-media-across-platforms-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/26/comscore-is-a-trusted-currency-for-planning-transacting-and-evaluating-media-across-platforms-2/#respond)
https://www.comscore.com/
- [https://www.comscore.com/](https://www.comscore.com/)

## AdinPlay – Maximize the ad revenues from your websites, apps and online games.
- [AdinPlay – Maximize the ad revenues from your websites, apps and online games.](https://markposition.wordpress.com/2022/02/24/adinplay-maximize-the-ad-revenues-from-your-websites-apps-and-online-games/)
- [February 24, 2022](https://markposition.wordpress.com/2022/02/24/adinplay-maximize-the-ad-revenues-from-your-websites-apps-and-online-games/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/24/adinplay-maximize-the-ad-revenues-from-your-websites-apps-and-online-games/#respond)
https://adinplay.com/
- [https://adinplay.com/](https://adinplay.com/)

## Davatelji oglasnih tehnologija za LGPD – Google AdSense Pomoć
- [Davatelji oglasnih tehnologija za LGPD – Google AdSense Pomoć](https://markposition.wordpress.com/2022/02/23/davatelji-oglasnih-tehnologija-za-lgpd-google-adsense-pomoc/)
- [February 23, 2022](https://markposition.wordpress.com/2022/02/23/davatelji-oglasnih-tehnologija-za-lgpd-google-adsense-pomoc/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/23/davatelji-oglasnih-tehnologija-za-lgpd-google-adsense-pomoc/#respond)
https://support.google.com/adsense/answer/9931967?hl=hr
- [https://support.google.com/adsense/answer/9931967?hl=hr](https://support.google.com/adsense/answer/9931967?hl=hr)

## Programmatic Digital Advertising Technology & Solutions | PubMatic
- [Programmatic Digital Advertising Technology & Solutions | PubMatic](https://markposition.wordpress.com/2022/02/21/programmatic-digital-advertising-technology-solutions-pubmatic-3/)
- [February 21, 2022](https://markposition.wordpress.com/2022/02/21/programmatic-digital-advertising-technology-solutions-pubmatic-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/21/programmatic-digital-advertising-technology-solutions-pubmatic-3/#respond)
https://pubmatic.com/
- [https://pubmatic.com/](https://pubmatic.com/)

## Header bidding – Wikipedia
- [Header bidding – Wikipedia](https://markposition.wordpress.com/2022/02/21/header-bidding-wikipedia/)
- [February 21, 2022](https://markposition.wordpress.com/2022/02/21/header-bidding-wikipedia/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/21/header-bidding-wikipedia/#respond)
https://en.wikipedia.org/wiki/Header_bidding
- [https://en.wikipedia.org/wiki/Header_bidding](https://en.wikipedia.org/wiki/Header_bidding)

## Supply-side platform – Wikipedia
- [Supply-side platform – Wikipedia](https://markposition.wordpress.com/2022/02/21/supply-side-platform-wikipedia/)
- [February 21, 2022](https://markposition.wordpress.com/2022/02/21/supply-side-platform-wikipedia/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/21/supply-side-platform-wikipedia/#respond)
https://en.wikipedia.org/wiki/Supply-side_platform
- [https://en.wikipedia.org/wiki/Supply-side_platform](https://en.wikipedia.org/wiki/Supply-side_platform)

## Online advertising – Wikipedia
- [Online advertising – Wikipedia](https://markposition.wordpress.com/2022/02/21/online-advertising-wikipedia/)
- [February 21, 2022](https://markposition.wordpress.com/2022/02/21/online-advertising-wikipedia/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/21/online-advertising-wikipedia/#respond)
https://en.wikipedia.org/wiki/Online_advertising
- [https://en.wikipedia.org/wiki/Online_advertising](https://en.wikipedia.org/wiki/Online_advertising)

## The Trade Desk – Wikipedia
- [The Trade Desk – Wikipedia](https://markposition.wordpress.com/2022/02/21/the-trade-desk-wikipedia/)
- [February 21, 2022](https://markposition.wordpress.com/2022/02/21/the-trade-desk-wikipedia/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/21/the-trade-desk-wikipedia/#respond)
https://en.wikipedia.org/wiki/The_Trade_Desk
- [https://en.wikipedia.org/wiki/The_Trade_Desk](https://en.wikipedia.org/wiki/The_Trade_Desk)

## Demand-side platform – Wikipedia
- [Demand-side platform – Wikipedia](https://markposition.wordpress.com/2022/02/21/demand-side-platform-wikipedia/)
- [February 21, 2022](https://markposition.wordpress.com/2022/02/21/demand-side-platform-wikipedia/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/21/demand-side-platform-wikipedia/#respond)
https://en.wikipedia.org/wiki/Demand-side_platform
- [https://en.wikipedia.org/wiki/Demand-side_platform](https://en.wikipedia.org/wiki/Demand-side_platform)

## Built for What Matters | The Trade Desk
- [Built for What Matters | The Trade Desk](https://markposition.wordpress.com/2022/02/21/built-for-what-matters-the-trade-desk/)
- [February 21, 2022](https://markposition.wordpress.com/2022/02/21/built-for-what-matters-the-trade-desk/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/21/built-for-what-matters-the-trade-desk/#respond)
https://www.thetradedesk.com/us
- [https://www.thetradedesk.com/us](https://www.thetradedesk.com/us)

## Google Ad Manager – Wikipedia
- [Google Ad Manager – Wikipedia](https://markposition.wordpress.com/2022/02/21/google-ad-manager-wikipedia/)
- [February 21, 2022](https://markposition.wordpress.com/2022/02/21/google-ad-manager-wikipedia/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/21/google-ad-manager-wikipedia/#respond)
https://en.wikipedia.org/wiki/Google_Ad_Manager
- [https://en.wikipedia.org/wiki/Google_Ad_Manager](https://en.wikipedia.org/wiki/Google_Ad_Manager)

## Ad exchange – Wikipedia
- [Ad exchange – Wikipedia](https://markposition.wordpress.com/2022/02/21/ad-exchange-wikipedia/)
- [February 21, 2022](https://markposition.wordpress.com/2022/02/21/ad-exchange-wikipedia/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/21/ad-exchange-wikipedia/#respond)
https://en.wikipedia.org/wiki/Ad_exchange
- [https://en.wikipedia.org/wiki/Ad_exchange](https://en.wikipedia.org/wiki/Ad_exchange)

## Google Marketing Platform – Unified Advertising and Analytics
- [Google Marketing Platform – Unified Advertising and Analytics](https://markposition.wordpress.com/2022/02/20/google-marketing-platform-unified-advertising-and-analytics/)
- [February 20, 2022](https://markposition.wordpress.com/2022/02/20/google-marketing-platform-unified-advertising-and-analytics/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/20/google-marketing-platform-unified-advertising-and-analytics/#respond)
https://marketingplatform.google.com/about/
- [https://marketingplatform.google.com/about/](https://marketingplatform.google.com/about/)

## Dashboarding & Data Visualization Tools – Google Data Studio
- [Dashboarding & Data Visualization Tools – Google Data Studio](https://markposition.wordpress.com/2022/02/20/dashboarding-data-visualization-tools-google-data-studio/)
- [February 20, 2022March 21, 2023](https://markposition.wordpress.com/2022/02/20/dashboarding-data-visualization-tools-google-data-studio/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/20/dashboarding-data-visualization-tools-google-data-studio/#respond)
https://marketingplatform.google.com/about/data-studio/
- [https://marketingplatform.google.com/about/data-studio/](https://marketingplatform.google.com/about/data-studio/)

## Business Analytics Tools & Solutions – Google Analytics 360
- [Business Analytics Tools & Solutions – Google Analytics 360](https://markposition.wordpress.com/2022/02/20/business-analytics-tools-solutions-google-analytics-360/)
- [February 20, 2022](https://markposition.wordpress.com/2022/02/20/business-analytics-tools-solutions-google-analytics-360/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/20/business-analytics-tools-solutions-google-analytics-360/#respond)
https://marketingplatform.google.com/about/analytics-360/
- [https://marketingplatform.google.com/about/analytics-360/](https://marketingplatform.google.com/about/analytics-360/)

## Search Campaign Management – Google Search Ads 360
- [Search Campaign Management – Google Search Ads 360](https://markposition.wordpress.com/2022/02/20/search-campaign-management-google-search-ads-360/)
- [February 20, 2022](https://markposition.wordpress.com/2022/02/20/search-campaign-management-google-search-ads-360/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/20/search-campaign-management-google-search-ads-360/#respond)
https://marketingplatform.google.com/about/search-ads-360/
- [https://marketingplatform.google.com/about/search-ads-360/](https://marketingplatform.google.com/about/search-ads-360/)

## Trusted Ad Serving – Campaign Manager 360
- [Trusted Ad Serving – Campaign Manager 360](https://markposition.wordpress.com/2022/02/20/trusted-ad-serving-campaign-manager-360/)
- [February 20, 2022](https://markposition.wordpress.com/2022/02/20/trusted-ad-serving-campaign-manager-360/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/20/trusted-ad-serving-campaign-manager-360/#respond)
https://marketingplatform.google.com/about/campaign-manager-360/
- [https://marketingplatform.google.com/about/campaign-manager-360/](https://marketingplatform.google.com/about/campaign-manager-360/)

## End to End Campaign Management – Google Display & Video 360
- [End to End Campaign Management – Google Display & Video 360](https://markposition.wordpress.com/2022/02/20/end-to-end-campaign-management-google-display-video-360/)
- [February 20, 2022](https://markposition.wordpress.com/2022/02/20/end-to-end-campaign-management-google-display-video-360/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/20/end-to-end-campaign-management-google-display-video-360/#respond)
https://marketingplatform.google.com/about/display-video-360/
- [https://marketingplatform.google.com/about/display-video-360/](https://marketingplatform.google.com/about/display-video-360/)

## Create and submit a robots.txt file | Google Search Central | Google Developers
- [Create and submit a robots.txt file | Google Search Central | Google Developers](https://markposition.wordpress.com/2022/02/19/create-and-submit-a-robots-txt-file-google-search-central-google-developers/)
- [February 19, 2022](https://markposition.wordpress.com/2022/02/19/create-and-submit-a-robots-txt-file-google-search-central-google-developers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/19/create-and-submit-a-robots-txt-file-google-search-central-google-developers/#respond)
https://developers.google.com/search/docs/advanced/robots/create-robots-txt
- [https://developers.google.com/search/docs/advanced/robots/create-robots-txt](https://developers.google.com/search/docs/advanced/robots/create-robots-txt)

## sitemaps.org – Home
- [sitemaps.org – Home](https://markposition.wordpress.com/2022/02/19/sitemaps-org-home/)
- [February 19, 2022](https://markposition.wordpress.com/2022/02/19/sitemaps-org-home/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/19/sitemaps-org-home/#respond)
https://www.sitemaps.org/
- [https://www.sitemaps.org/](https://www.sitemaps.org/)

## The Web Robots Pages
- [The Web Robots Pages](https://markposition.wordpress.com/2022/02/19/the-web-robots-pages/)
- [February 19, 2022](https://markposition.wordpress.com/2022/02/19/the-web-robots-pages/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/19/the-web-robots-pages/#respond)
http://www.robotstxt.org/
- [http://www.robotstxt.org/](http://www.robotstxt.org/)

## Partnerski program za izdavaštvo | Certificirani partner –izdavač –Google
- [Partnerski program za izdavaštvo | Certificirani partner –izdavač –Google](https://markposition.wordpress.com/2022/02/19/partnerski-program-za-izdavastvo-certificirani-partner-izdavac-google-2/)
- [February 19, 2022](https://markposition.wordpress.com/2022/02/19/partnerski-program-za-izdavastvo-certificirani-partner-izdavac-google-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/19/partnerski-program-za-izdavastvo-certificirani-partner-izdavac-google-2/#respond)
https://www.google.com/ads/publisher/partners/
- [https://www.google.com/ads/publisher/partners/](https://www.google.com/ads/publisher/partners/)

## Pronađite partnera – izdavača | Certificirani partner – izdavač – Google
- [Pronađite partnera – izdavača | Certificirani partner – izdavač – Google](https://markposition.wordpress.com/2022/02/19/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google-2/)
- [February 19, 2022](https://markposition.wordpress.com/2022/02/19/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/19/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google-2/#respond)
https://www.google.com/ads/publisher/partners/find-a-partner/
- [https://www.google.com/ads/publisher/partners/find-a-partner/](https://www.google.com/ads/publisher/partners/find-a-partner/#!?modal_active=none)

## Monetization ezoic
- [Monetization ezoic](https://markposition.wordpress.com/2022/02/19/monetization-ezoic/)
- [February 19, 2022](https://markposition.wordpress.com/2022/02/19/monetization-ezoic/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/19/monetization-ezoic/#respond)
https://pubdash.ezoic.com/monetization
- [https://pubdash.ezoic.com/monetization](https://pubdash.ezoic.com/monetization)

## Google Ad Manager – Integrated Advertising Management Platform
- [Google Ad Manager – Integrated Advertising Management Platform](https://markposition.wordpress.com/2022/02/19/google-ad-manager-integrated-advertising-management-platform-3/)
- [February 19, 2022](https://markposition.wordpress.com/2022/02/19/google-ad-manager-integrated-advertising-management-platform-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/19/google-ad-manager-integrated-advertising-management-platform-3/#respond)
https://admanager.google.com/home/
- [https://admanager.google.com/home/](https://admanager.google.com/home/)

## Inside AdSense: Bringing more buyers to AdSense through the DoubleClick Ad Exchange
- [Inside AdSense: Bringing more buyers to AdSense through the DoubleClick Ad Exchange](https://markposition.wordpress.com/2022/02/19/inside-adsense-bringing-more-buyers-to-adsense-through-the-doubleclick-ad-exchange/)
- [February 19, 2022February 19, 2022](https://markposition.wordpress.com/2022/02/19/inside-adsense-bringing-more-buyers-to-adsense-through-the-doubleclick-ad-exchange/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/19/inside-adsense-bringing-more-buyers-to-adsense-through-the-doubleclick-ad-exchange/#respond)
https://adsense.googleblog.com/2009/09/bringing-more-buyers-to-adsense-through.html
- [https://adsense.googleblog.com/2009/09/bringing-more-buyers-to-adsense-through.html](https://adsense.googleblog.com/2009/09/bringing-more-buyers-to-adsense-through.html)
- [adexchangeoverview](https://markposition.wordpress.com/wp-content/uploads/2022/08/6f351-adexchangeoverview.pdf)
- [Download](https://markposition.wordpress.com/wp-content/uploads/2022/08/6f351-adexchangeoverview.pdf)

## Google AdSense
- [Google AdSense](https://markposition.wordpress.com/2022/02/19/google-adsense/)
- [February 19, 2022](https://markposition.wordpress.com/2022/02/19/google-adsense/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/19/google-adsense/#respond)
https://support.google.com/adsense/
- [https://support.google.com/adsense/](https://support.google.com/adsense/?hl=hr#topic=1190787)

## AdSense | Google Blog
- [AdSense | Google Blog](https://markposition.wordpress.com/2022/02/19/adsense-google-blog/)
- [February 19, 2022](https://markposition.wordpress.com/2022/02/19/adsense-google-blog/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/19/adsense-google-blog/#respond)
https://blog.google/products/adsense/
- [https://blog.google/products/adsense/](https://blog.google/products/adsense/)

## Cookieless Targeting, Audience Targeting, CMP – Sirdata
- [Cookieless Targeting, Audience Targeting, CMP – Sirdata](https://markposition.wordpress.com/2022/02/15/cookieless-targeting-audience-targeting-cmp-sirdata-2/)
- [February 15, 2022](https://markposition.wordpress.com/2022/02/15/cookieless-targeting-audience-targeting-cmp-sirdata-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/15/cookieless-targeting-audience-targeting-cmp-sirdata-2/#respond)
https://sirdata.com/en/
- [https://sirdata.com/en/](https://sirdata.com/en/)

## 152 Media – Header Bidding
- [152 Media – Header Bidding](https://markposition.wordpress.com/2022/02/15/152-media-header-bidding/)
- [February 15, 2022](https://markposition.wordpress.com/2022/02/15/152-media-header-bidding/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/15/152-media-header-bidding/#respond)
https://152media.com/
- [https://152media.com/](https://152media.com/)

## IAB Tech Lab
- [IAB Tech Lab](https://markposition.wordpress.com/2022/02/14/iab-tech-lab/)
- [February 14, 2022](https://markposition.wordpress.com/2022/02/14/iab-tech-lab/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/14/iab-tech-lab/#respond)
https://iabtechlab.com/software/
- [https://iabtechlab.com/software/](https://iabtechlab.com/software/)

## Digiday – Digital Content, Digital Advertising, Digital Marketing
- [Digiday – Digital Content, Digital Advertising, Digital Marketing](https://markposition.wordpress.com/2022/02/13/digiday-digital-content-digital-advertising-digital-marketing/)
- [February 13, 2022](https://markposition.wordpress.com/2022/02/13/digiday-digital-content-digital-advertising-digital-marketing/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/13/digiday-digital-content-digital-advertising-digital-marketing/#respond)
https://digiday.com/
- [https://digiday.com/](https://digiday.com/)

## Google Ads Status Dashboard
- [Google Ads Status Dashboard](https://markposition.wordpress.com/2022/02/13/google-ads-status-dashboard/)
- [February 13, 2022](https://markposition.wordpress.com/2022/02/13/google-ads-status-dashboard/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/13/google-ads-status-dashboard/#respond)
https://ads.google.com/status/publisher/
- [https://ads.google.com/status/publisher/](https://ads.google.com/status/publisher/)

## CMP Builder | by OneTrust
- [CMP Builder | by OneTrust](https://markposition.wordpress.com/2022/02/12/cmp-builder-by-onetrust/)
- [February 12, 2022](https://markposition.wordpress.com/2022/02/12/cmp-builder-by-onetrust/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/12/cmp-builder-by-onetrust/#respond)
https://comply.cookiepro.com/
- [https://comply.cookiepro.com/](https://comply.cookiepro.com/)

## Audience Is Everything® – Nielsen
- [Audience Is Everything® – Nielsen](https://markposition.wordpress.com/2022/02/12/audience-is-everything-nielsen/)
- [February 12, 2022](https://markposition.wordpress.com/2022/02/12/audience-is-everything-nielsen/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/12/audience-is-everything-nielsen/#respond)
https://global.nielsen.com/global/en/
- [https://global.nielsen.com/global/en/](https://global.nielsen.com/global/en/)

## Vendors List – IAB Europe
- [Vendors List – IAB Europe](https://markposition.wordpress.com/2022/02/12/vendors-list-iab-europe/)
- [February 12, 2022](https://markposition.wordpress.com/2022/02/12/vendors-list-iab-europe/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/12/vendors-list-iab-europe/#respond)
https://iabeurope.eu/vendor-list/
- [https://iabeurope.eu/vendor-list/](https://iabeurope.eu/vendor-list/)

## Adacado DIY Advertising | Do It Yourself Digital Advertising
- [Adacado DIY Advertising | Do It Yourself Digital Advertising](https://markposition.wordpress.com/2022/02/12/adacado-diy-advertising-do-it-yourself-digital-advertising/)
- [February 12, 2022](https://markposition.wordpress.com/2022/02/12/adacado-diy-advertising-do-it-yourself-digital-advertising/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/02/12/adacado-diy-advertising-do-it-yourself-digital-advertising/#respond)
https://adacado.com/
- [https://adacado.com/](https://adacado.com/)

## Home • #1 Platform to make better ads: Unify Data + Creativity • VidMob
- [Home • #1 Platform to make better ads: Unify Data + Creativity • VidMob](https://markposition.wordpress.com/2022/01/30/home-1-platform-to-make-better-ads-unify-data-creativity-vidmob/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/home-1-platform-to-make-better-ads-unify-data-creativity-vidmob/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/home-1-platform-to-make-better-ads-unify-data-creativity-vidmob/#respond)
https://www.vidmob.com/
- [https://www.vidmob.com/](https://www.vidmob.com/)

## First-Impression :: Advertising Platform
- [First-Impression :: Advertising Platform](https://markposition.wordpress.com/2022/01/30/first-impression-advertising-platform/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/first-impression-advertising-platform/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/first-impression-advertising-platform/#respond)
http://www.first-impression.com/home/
- [http://www.first-impression.com/home/](http://www.first-impression.com/home/)

## Facebook Audience Network | Facebook Developers
- [Facebook Audience Network | Facebook Developers](https://markposition.wordpress.com/2022/01/30/facebook-audience-network-facebook-developers/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/facebook-audience-network-facebook-developers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/facebook-audience-network-facebook-developers/#respond)
https://developers.facebook.com/products/audience-network/
- [https://developers.facebook.com/products/audience-network/](https://developers.facebook.com/products/audience-network/)

## Home – diDNA
- [Home – diDNA](https://markposition.wordpress.com/2022/01/30/home-didna/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/home-didna/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/home-didna/#respond)
https://didna.io/
- [https://didna.io/](https://didna.io/)

## Content.ad – Native Advertising, Push Notifications, and Beyond
- [Content.ad – Native Advertising, Push Notifications, and Beyond](https://markposition.wordpress.com/2022/01/30/content-ad-native-advertising-push-notifications-and-beyond/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/content-ad-native-advertising-push-notifications-and-beyond/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/content-ad-native-advertising-push-notifications-and-beyond/#respond)
https://content.ad/
- [https://content.ad/](https://content.ad/)

## Connect Ads
- [Connect Ads](https://markposition.wordpress.com/2022/01/30/connect-ads/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/connect-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/connect-ads/#respond)
https://connectads.com/
- [https://connectads.com/](https://connectads.com/)

## Advertising Solutions for Publishers and Marketers | BuySellAds
- [Advertising Solutions for Publishers and Marketers | BuySellAds](https://markposition.wordpress.com/2022/01/30/advertising-solutions-for-publishers-and-marketers-buysellads/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/advertising-solutions-for-publishers-and-marketers-buysellads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/advertising-solutions-for-publishers-and-marketers-buysellads/#respond)
https://www.buysellads.com/
- [https://www.buysellads.com/](https://www.buysellads.com/)

## Join Our UK Affiliate Network – Awin
- [Join Our UK Affiliate Network – Awin](https://markposition.wordpress.com/2022/01/30/join-our-uk-affiliate-network-awin/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/join-our-uk-affiliate-network-awin/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/join-our-uk-affiliate-network-awin/#respond)
https://www.awin.com/gb
- [https://www.awin.com/gb](https://www.awin.com/gb)

## Интернет реклама | Рекламная сеть Advmaker.net
- [Интернет реклама | Рекламная сеть Advmaker.net](https://markposition.wordpress.com/2022/01/30/%d0%b8%d0%bd%d1%82%d0%b5%d1%80%d0%bd%d0%b5%d1%82-%d1%80%d0%b5%d0%ba%d0%bb%d0%b0%d0%bc%d0%b0-%d1%80%d0%b5%d0%ba%d0%bb%d0%b0%d0%bc%d0%bd%d0%b0%d1%8f-%d1%81%d0%b5%d1%82%d1%8c-advmaker-net/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/%d0%b8%d0%bd%d1%82%d0%b5%d1%80%d0%bd%d0%b5%d1%82-%d1%80%d0%b5%d0%ba%d0%bb%d0%b0%d0%bc%d0%b0-%d1%80%d0%b5%d0%ba%d0%bb%d0%b0%d0%bc%d0%bd%d0%b0%d1%8f-%d1%81%d0%b5%d1%82%d1%8c-advmaker-net/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/%d0%b8%d0%bd%d1%82%d0%b5%d1%80%d0%bd%d0%b5%d1%82-%d1%80%d0%b5%d0%ba%d0%bb%d0%b0%d0%bc%d0%b0-%d1%80%d0%b5%d0%ba%d0%bb%d0%b0%d0%bc%d0%bd%d0%b0%d1%8f-%d1%81%d0%b5%d1%82%d1%8c-advmaker-net/#respond)
http://advmaker.net/
- [http://advmaker.net/](http://advmaker.net/)

## Adsterra Advertising Network | Solutions for Advertisers and Publishers
- [Adsterra Advertising Network | Solutions for Advertisers and Publishers](https://markposition.wordpress.com/2022/01/30/adsterra-advertising-network-solutions-for-advertisers-and-publishers/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/adsterra-advertising-network-solutions-for-advertisers-and-publishers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/adsterra-advertising-network-solutions-for-advertisers-and-publishers/#respond)
https://adsterra.com/
- [https://adsterra.com/](https://adsterra.com/)

## Adomik
- [Adomik](https://markposition.wordpress.com/2022/01/30/adomik/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/adomik/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/adomik/#respond)
https://www.adomik.com/
- [https://www.adomik.com/](https://www.adomik.com/)

## Adnet
- [Adnet](https://markposition.wordpress.com/2022/01/30/adnet/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/adnet/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/adnet/#respond)
https://adnet.com/
- [https://adnet.com/](https://adnet.com/)

## Home » Admetrics media
- [Home » Admetrics media](https://markposition.wordpress.com/2022/01/30/home-admetrics-media/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/home-admetrics-media/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/home-admetrics-media/#respond)
http://www.admetricsmedia.com/
- [http://www.admetricsmedia.com/](http://www.admetricsmedia.com/)

## AdMaven Ad Network | The Online Advertising Platform
- [AdMaven Ad Network | The Online Advertising Platform](https://markposition.wordpress.com/2022/01/30/admaven-ad-network-the-online-advertising-platform/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/admaven-ad-network-the-online-advertising-platform/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/admaven-ad-network-the-online-advertising-platform/#respond)
https://ad-maven.com/
- [https://ad-maven.com/](https://ad-maven.com/)

## Home | 33Across
- [Home | 33Across](https://markposition.wordpress.com/2022/01/30/home-33across/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/home-33across/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/home-33across/#respond)
https://www.33across.com/
- [https://www.33across.com/](https://www.33across.com/)

## Rich Media Creative Agency | Online Advertising Agency USA | Undertone
- [Rich Media Creative Agency | Online Advertising Agency USA | Undertone](https://markposition.wordpress.com/2022/01/30/rich-media-creative-agency-online-advertising-agency-usa-undertone/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/rich-media-creative-agency-online-advertising-agency-usa-undertone/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/rich-media-creative-agency-online-advertising-agency-usa-undertone/#respond)
https://www.undertone.com/
- [https://www.undertone.com/](https://www.undertone.com/)

## The Publisher Technology Platform | Sovrn
- [The Publisher Technology Platform | Sovrn](https://markposition.wordpress.com/2022/01/30/the-publisher-technology-platform-sovrn-2/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/the-publisher-technology-platform-sovrn-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/the-publisher-technology-platform-sovrn-2/#respond)
https://www.sovrn.com/
- [https://www.sovrn.com/](https://www.sovrn.com/)

## Rubicon is now Magnite
- [Rubicon is now Magnite](https://markposition.wordpress.com/2022/01/30/rubicon-is-now-magnite/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/rubicon-is-now-magnite/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/rubicon-is-now-magnite/#respond)
https://rubiconproject.com/
- [https://rubiconproject.com/](https://rubiconproject.com/)

## Content Marketing, Native Advertising & Discovery – Revcontent
- [Content Marketing, Native Advertising & Discovery – Revcontent](https://markposition.wordpress.com/2022/01/30/content-marketing-native-advertising-discovery-revcontent/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/content-marketing-native-advertising-discovery-revcontent/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/content-marketing-native-advertising-discovery-revcontent/#respond)
https://www.revcontent.com/
- [https://www.revcontent.com/](https://www.revcontent.com/)

## Programmatic Digital Advertising Technology & Solutions | PubMatic
- [Programmatic Digital Advertising Technology & Solutions | PubMatic](https://markposition.wordpress.com/2022/01/30/programmatic-digital-advertising-technology-solutions-pubmatic-2/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/programmatic-digital-advertising-technology-solutions-pubmatic-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/programmatic-digital-advertising-technology-solutions-pubmatic-2/#respond)
https://pubmatic.com/
- [https://pubmatic.com/](https://pubmatic.com/)

## Outbrain – Recommendation Platform Powered by Native Ads
- [Outbrain – Recommendation Platform Powered by Native Ads](https://markposition.wordpress.com/2022/01/30/outbrain-recommendation-platform-powered-by-native-ads-5/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/outbrain-recommendation-platform-powered-by-native-ads-5/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/outbrain-recommendation-platform-powered-by-native-ads-5/#respond)
https://www.outbrain.com/
- [https://www.outbrain.com/](https://www.outbrain.com/)

## OpenX: Programmatic Advertising | Ad Exchange Network
- [OpenX: Programmatic Advertising | Ad Exchange Network](https://markposition.wordpress.com/2022/01/30/openx-programmatic-advertising-ad-exchange-network-2/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/openx-programmatic-advertising-ad-exchange-network-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/openx-programmatic-advertising-ad-exchange-network-2/#respond)
https://www.openx.com/
- [https://www.openx.com/](https://www.openx.com/)

## Digital Online Advertising Platforms | Yahoo Ad Tech
- [Digital Online Advertising Platforms | Yahoo Ad Tech](https://markposition.wordpress.com/2022/01/30/digital-online-advertising-platforms-yahoo-ad-tech-2/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/digital-online-advertising-platforms-yahoo-ad-tech-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/digital-online-advertising-platforms-yahoo-ad-tech-2/#respond)
https://www.adtech.yahooinc.com/
- [https://www.adtech.yahooinc.com/](https://www.adtech.yahooinc.com/)

## Google AdSense – ostvarite zaradu unovčavanjem web-lokacije
- [Google AdSense – ostvarite zaradu unovčavanjem web-lokacije](https://markposition.wordpress.com/2022/01/30/google-adsense-ostvarite-zaradu-unovcavanjem-web-lokacije/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/google-adsense-ostvarite-zaradu-unovcavanjem-web-lokacije/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/google-adsense-ostvarite-zaradu-unovcavanjem-web-lokacije/#respond)
https://www.google.com/intl/hr_hr/adsense/start/
- [https://www.google.com/intl/hr_hr/adsense/start/](https://www.google.com/intl/hr_hr/adsense/start/)

## Contextual Advertising & Programmatic Platform | Media.net
- [Contextual Advertising & Programmatic Platform | Media.net](https://markposition.wordpress.com/2022/01/30/contextual-advertising-programmatic-platform-media-net/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/contextual-advertising-programmatic-platform-media-net/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/contextual-advertising-programmatic-platform-media-net/#respond)
https://www.media.net/
- [https://www.media.net/](https://www.media.net/)

## Get Started | Buyer APIs | Google Developers
- [Get Started | Buyer APIs | Google Developers](https://markposition.wordpress.com/2022/01/30/get-started-buyer-apis-google-developers/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/get-started-buyer-apis-google-developers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/get-started-buyer-apis-google-developers/#respond)
https://developers.google.com/authorized-buyers/apis/guides/start
- [https://developers.google.com/authorized-buyers/apis/guides/start](https://developers.google.com/authorized-buyers/apis/guides/start)

## Authorized Buyers | Google Developers
- [Authorized Buyers | Google Developers](https://markposition.wordpress.com/2022/01/30/authorized-buyers-google-developers/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/authorized-buyers-google-developers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/authorized-buyers-google-developers/#respond)
https://developers.google.com/authorized-buyers
- [https://developers.google.com/authorized-buyers](https://developers.google.com/authorized-buyers)

## District M is now Sharethrough | District M
- [District M is now Sharethrough | District M](https://markposition.wordpress.com/2022/01/30/district-m-is-now-sharethrough-district-m/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/district-m-is-now-sharethrough-district-m/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/district-m-is-now-sharethrough-district-m/#respond)
https://www.districtm.net/
- [https://www.districtm.net/](https://www.districtm.net/)

## enginemediaexchange.com | Futureproof Your Business
- [enginemediaexchange.com | Futureproof Your Business](https://markposition.wordpress.com/2022/01/30/enginemediaexchange-com-futureproof-your-business/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/enginemediaexchange-com-futureproof-your-business/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/enginemediaexchange-com-futureproof-your-business/#respond)
https://enginemediaexchange.com/
- [https://enginemediaexchange.com/](https://enginemediaexchange.com/)

## Xandr
- [Xandr](https://markposition.wordpress.com/2022/01/30/xandr/)
- [January 30, 2022](https://markposition.wordpress.com/2022/01/30/xandr/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/30/xandr/#respond)
https://www.xandr.com/
- [https://www.xandr.com/](https://www.xandr.com/)

## Digital Online Advertising Platforms | Yahoo Ad Tech
- [Digital Online Advertising Platforms | Yahoo Ad Tech](https://markposition.wordpress.com/2022/01/27/digital-online-advertising-platforms-yahoo-ad-tech/)
- [January 27, 2022](https://markposition.wordpress.com/2022/01/27/digital-online-advertising-platforms-yahoo-ad-tech/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/27/digital-online-advertising-platforms-yahoo-ad-tech/#respond)
https://www.adtech.yahooinc.com/
- [https://www.adtech.yahooinc.com/](https://www.adtech.yahooinc.com/)

## Bring Innovation And Incrementality To Mobile Monetization
- [Bring Innovation And Incrementality To Mobile Monetization](https://markposition.wordpress.com/2022/01/27/bring-innovation-and-incrementality-to-mobile-monetization/)
- [January 27, 2022](https://markposition.wordpress.com/2022/01/27/bring-innovation-and-incrementality-to-mobile-monetization/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/27/bring-innovation-and-incrementality-to-mobile-monetization/#respond)
https://www.display.io/
- [https://www.display.io/](https://www.display.io/)

## Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions
- [Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions](https://markposition.wordpress.com/2022/01/27/marketing-advertising-on-linkedin-linkedin-marketing-solutions-3/)
- [January 27, 2022](https://markposition.wordpress.com/2022/01/27/marketing-advertising-on-linkedin-linkedin-marketing-solutions-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/27/marketing-advertising-on-linkedin-linkedin-marketing-solutions-3/#respond)
https://business.linkedin.com/marketing-solutions
- [https://business.linkedin.com/marketing-solutions](https://business.linkedin.com/marketing-solutions)

## LinkedIn Advertising Costs & Pricing | LinkedIn Marketing Solutions
- [LinkedIn Advertising Costs & Pricing | LinkedIn Marketing Solutions](https://markposition.wordpress.com/2022/01/27/linkedin-advertising-costs-pricing-linkedin-marketing-solutions/)
- [January 27, 2022](https://markposition.wordpress.com/2022/01/27/linkedin-advertising-costs-pricing-linkedin-marketing-solutions/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/27/linkedin-advertising-costs-pricing-linkedin-marketing-solutions/#respond)
https://business.linkedin.com/marketing-solutions/ads/pricing
- [https://business.linkedin.com/marketing-solutions/ads/pricing](https://business.linkedin.com/marketing-solutions/ads/pricing)

## LinkedIn Ads: Targeted Self-Service Ads | LinkedIn Marketing Solutions
- [LinkedIn Ads: Targeted Self-Service Ads | LinkedIn Marketing Solutions](https://markposition.wordpress.com/2022/01/27/linkedin-ads-targeted-self-service-ads-linkedin-marketing-solutions-2/)
- [January 27, 2022](https://markposition.wordpress.com/2022/01/27/linkedin-ads-targeted-self-service-ads-linkedin-marketing-solutions-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/27/linkedin-ads-targeted-self-service-ads-linkedin-marketing-solutions-2/#respond)
https://business.linkedin.com/marketing-solutions/ads
- [https://business.linkedin.com/marketing-solutions/ads](https://business.linkedin.com/marketing-solutions/ads)

## Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions
- [Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions](https://markposition.wordpress.com/2022/01/27/marketing-advertising-on-linkedin-linkedin-marketing-solutions-2/)
- [January 27, 2022](https://markposition.wordpress.com/2022/01/27/marketing-advertising-on-linkedin-linkedin-marketing-solutions-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/27/marketing-advertising-on-linkedin-linkedin-marketing-solutions-2/#respond)
https://business.linkedin.com/marketing-solutions
- [https://business.linkedin.com/marketing-solutions](https://business.linkedin.com/marketing-solutions)

## LinkedIn Campaign Manager
- [LinkedIn Campaign Manager](https://markposition.wordpress.com/2022/01/27/linkedin-campaign-manager-2/)
- [January 27, 2022](https://markposition.wordpress.com/2022/01/27/linkedin-campaign-manager-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/27/linkedin-campaign-manager-2/#respond)
https://www.linkedin.com/campaignmanager/
- [https://www.linkedin.com/campaignmanager/](https://www.linkedin.com/campaignmanager/accounts)

## Outbrain – Recommendation Platform Powered by Native Ads
- [Outbrain – Recommendation Platform Powered by Native Ads](https://markposition.wordpress.com/2022/01/24/outbrain-recommendation-platform-powered-by-native-ads-4/)
- [January 24, 2022](https://markposition.wordpress.com/2022/01/24/outbrain-recommendation-platform-powered-by-native-ads-4/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/24/outbrain-recommendation-platform-powered-by-native-ads-4/#respond)
https://www.outbrain.com/
- [https://www.outbrain.com/](https://www.outbrain.com/)

## Home – TrustArc The Leader in Privacy Management Software
- [Home – TrustArc The Leader in Privacy Management Software](https://markposition.wordpress.com/2022/01/16/home-trustarc-the-leader-in-privacy-management-software-3-2/)
- [January 16, 2022](https://markposition.wordpress.com/2022/01/16/home-trustarc-the-leader-in-privacy-management-software-3-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/16/home-trustarc-the-leader-in-privacy-management-software-3-2/#respond)
https://trustarc.com/
- [https://trustarc.com/](https://trustarc.com/)

## Outbrain – Recommendation Platform Powered by Native Ads
- [Outbrain – Recommendation Platform Powered by Native Ads](https://markposition.wordpress.com/2022/01/13/outbrain-recommendation-platform-powered-by-native-ads-3/)
- [January 13, 2022](https://markposition.wordpress.com/2022/01/13/outbrain-recommendation-platform-powered-by-native-ads-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/13/outbrain-recommendation-platform-powered-by-native-ads-3/#respond)
https://www.outbrain.com/
- [https://www.outbrain.com/](https://www.outbrain.com/)

## Google Ad Manager – Integrated Advertising Management Platform
- [Google Ad Manager – Integrated Advertising Management Platform](https://markposition.wordpress.com/2022/01/05/google-ad-manager-integrated-advertising-management-platform-2/)
- [January 5, 2022](https://markposition.wordpress.com/2022/01/05/google-ad-manager-integrated-advertising-management-platform-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/05/google-ad-manager-integrated-advertising-management-platform-2/#respond)
https://admanager.google.com/home/
- [https://admanager.google.com/home/](https://admanager.google.com/home/)

## Mobile App Monetization – Google AdMob
- [Mobile App Monetization – Google AdMob](https://markposition.wordpress.com/2022/01/05/mobile-app-monetization-google-admob/)
- [January 5, 2022](https://markposition.wordpress.com/2022/01/05/mobile-app-monetization-google-admob/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/05/mobile-app-monetization-google-admob/#respond)
https://admob.google.com/home/
- [https://admob.google.com/home/](https://admob.google.com/home/)

## In App Advertising | Vungle
- [In App Advertising | Vungle](https://markposition.wordpress.com/2022/01/03/in-app-advertising-vungle/)
- [January 3, 2022](https://markposition.wordpress.com/2022/01/03/in-app-advertising-vungle/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2022/01/03/in-app-advertising-vungle/#respond)
https://vungle.com/advertise/
- [https://vungle.com/advertise/](https://vungle.com/advertise/)

## Digital Customer Acquisition Solutions | Rakuten Advertising
- [Digital Customer Acquisition Solutions | Rakuten Advertising](https://markposition.wordpress.com/2021/12/21/digital-customer-acquisition-solutions-rakuten-advertising/)
- [December 21, 2021](https://markposition.wordpress.com/2021/12/21/digital-customer-acquisition-solutions-rakuten-advertising/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/12/21/digital-customer-acquisition-solutions-rakuten-advertising/#respond)
https://rakutenadvertising.com/
- [https://rakutenadvertising.com/](https://rakutenadvertising.com/)

## Online Video Advertising Campaigns – YouTube Advertising
- [Online Video Advertising Campaigns – YouTube Advertising](https://markposition.wordpress.com/2021/12/11/online-video-advertising-campaigns-youtube-advertising-2/)
- [December 11, 2021](https://markposition.wordpress.com/2021/12/11/online-video-advertising-campaigns-youtube-advertising-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/12/11/online-video-advertising-campaigns-youtube-advertising-2/#respond)
https://www.youtube.com/ads/
- [https://www.youtube.com/ads/](https://www.youtube.com/ads/)

## BrandConnect for Influencer Advertising – YouTube Advertising – YouTube Advertising
- [BrandConnect for Influencer Advertising – YouTube Advertising – YouTube Advertising](https://markposition.wordpress.com/2021/12/11/brandconnect-for-influencer-advertising-youtube-advertising-youtube-advertising/)
- [December 11, 2021](https://markposition.wordpress.com/2021/12/11/brandconnect-for-influencer-advertising-youtube-advertising-youtube-advertising/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/12/11/brandconnect-for-influencer-advertising-youtube-advertising-youtube-advertising/#respond)
https://www.youtube.com/ads/brandconnect/
- [https://www.youtube.com/ads/brandconnect/](https://www.youtube.com/ads/brandconnect/)

## Google Ads – privucite više korisnika jednostavnim online oglašavanjem
- [Google Ads – privucite više korisnika jednostavnim online oglašavanjem](https://markposition.wordpress.com/2021/12/01/google-ads-privucite-vise-korisnika-jednostavnim-online-oglasavanjem-7/)
- [December 1, 2021](https://markposition.wordpress.com/2021/12/01/google-ads-privucite-vise-korisnika-jednostavnim-online-oglasavanjem-7/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/12/01/google-ads-privucite-vise-korisnika-jednostavnim-online-oglasavanjem-7/#respond)
https://ads.google.com/intl/hr_hr/home/
- [https://ads.google.com/intl/hr_hr/home/](https://ads.google.com/intl/hr_hr/home/)

## Campaign Builder | Amazon Advertising
- [Campaign Builder | Amazon Advertising](https://markposition.wordpress.com/2021/11/24/campaign-builder-amazon-advertising/)
- [November 24, 2021November 24, 2021](https://markposition.wordpress.com/2021/11/24/campaign-builder-amazon-advertising/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/11/24/campaign-builder-amazon-advertising/#respond)
https://advertising.amazon.com
- [https://advertising.amazon.com](https://advertising.amazon.com/cb?entityId=ENTITY170NBZYAM0OSR#!/ingress)

## International growth agencies – Market Finder by Google
- [International growth agencies – Market Finder by Google](https://markposition.wordpress.com/2021/11/24/international-growth-agencies-market-finder-by-google/)
- [November 24, 2021](https://markposition.wordpress.com/2021/11/24/international-growth-agencies-market-finder-by-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/11/24/international-growth-agencies-market-finder-by-google/#respond)
https://marketfinder.thinkwithgoogle.com/intl/en_cee/widget/partner-agencies-tool/
- [https://marketfinder.thinkwithgoogle.com/intl/en_cee/widget/partner-agencies-tool/](https://marketfinder.thinkwithgoogle.com/intl/en_cee/widget/partner-agencies-tool/)

## Free Google Ads Tools by Clever Ads | Google Advertising
- [Free Google Ads Tools by Clever Ads | Google Advertising](https://markposition.wordpress.com/2021/11/23/free-google-ads-tools-by-clever-ads-google-advertising/)
- [November 23, 2021](https://markposition.wordpress.com/2021/11/23/free-google-ads-tools-by-clever-ads-google-advertising/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/11/23/free-google-ads-tools-by-clever-ads-google-advertising/#respond)
https://cleverads.com/
- [https://cleverads.com/](https://cleverads.com/)

## Audiencerate – The Identity Hub
- [Audiencerate – The Identity Hub](https://markposition.wordpress.com/2021/11/13/audiencerate-the-identity-hub/)
- [November 13, 2021](https://markposition.wordpress.com/2021/11/13/audiencerate-the-identity-hub/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/11/13/audiencerate-the-identity-hub/#respond)
https://www.audiencerate.com/
- [https://www.audiencerate.com/](https://www.audiencerate.com/)

## Lucidity | Blockchain-Audited Media for Greater Transparency in Advertising
- [Lucidity | Blockchain-Audited Media for Greater Transparency in Advertising](https://markposition.wordpress.com/2021/11/13/lucidity-blockchain-audited-media-for-greater-transparency-in-advertising/)
- [November 13, 2021](https://markposition.wordpress.com/2021/11/13/lucidity-blockchain-audited-media-for-greater-transparency-in-advertising/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/11/13/lucidity-blockchain-audited-media-for-greater-transparency-in-advertising/#respond)
https://golucidity.com/
- [https://golucidity.com/](https://golucidity.com/)

## Customer Data Platform – Tealium
- [Customer Data Platform – Tealium](https://markposition.wordpress.com/2021/11/13/customer-data-platform-tealium/)
- [November 13, 2021](https://markposition.wordpress.com/2021/11/13/customer-data-platform-tealium/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/11/13/customer-data-platform-tealium/#respond)
https://tealium.com/
- [https://tealium.com/](https://tealium.com/)

## Revealbot – Automate Your Ad Strategies
- [Revealbot – Automate Your Ad Strategies](https://markposition.wordpress.com/2021/11/12/revealbot-automate-your-ad-strategies/)
- [November 12, 2021](https://markposition.wordpress.com/2021/11/12/revealbot-automate-your-ad-strategies/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/11/12/revealbot-automate-your-ad-strategies/#respond)
https://revealbot.com/
- [https://revealbot.com/](https://revealbot.com/)

## EthicalAds
- [EthicalAds](https://markposition.wordpress.com/2021/10/18/privacy-preserving-ad-network-for-developers-ethicalads/)
- [October 18, 2021October 20, 2021](https://markposition.wordpress.com/2021/10/18/privacy-preserving-ad-network-for-developers-ethicalads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/10/18/privacy-preserving-ad-network-for-developers-ethicalads/#respond)
https://ethicalads.io
- [https://ethicalads.io](https://ethicalads.io)

## ads twitter
- [ads twitter](https://markposition.wordpress.com/2021/10/04/485/)
- [October 4, 2021October 20, 2021](https://markposition.wordpress.com/2021/10/04/485/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/10/04/485/#respond)
https://ads.twitter.com
- [https://ads.twitter.com](https://ads.twitter.com/mobile/v1/get_started?ref=em-elq-ao-gbl-emailatclink&s=09)

## Eskimi – AdTech platform that adds a +1 to your marketing team
- [Eskimi – AdTech platform that adds a +1 to your marketing team](https://markposition.wordpress.com/2021/09/28/eskimi-adtech-platform-that-adds-a-1-to-your-marketing-team/)
- [September 28, 2021](https://markposition.wordpress.com/2021/09/28/eskimi-adtech-platform-that-adds-a-1-to-your-marketing-team/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/09/28/eskimi-adtech-platform-that-adds-a-1-to-your-marketing-team/#respond)
https://www.eskimi.com/
- [https://www.eskimi.com/](https://www.eskimi.com/)

## Overview – Microsoft Advertising
- [Overview – Microsoft Advertising](https://markposition.wordpress.com/2021/09/21/overview-microsoft-advertising-2/)
- [September 21, 2021](https://markposition.wordpress.com/2021/09/21/overview-microsoft-advertising-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/09/21/overview-microsoft-advertising-2/#respond)
https://about.ads.microsoft.com/en-us/h/a/microsoft-advertising
- [https://about.ads.microsoft.com/en-us/h/a/microsoft-advertising](https://about.ads.microsoft.com/en-us/h/a/microsoft-advertising)

## Google Marketing Platform Certification Exams : Google
- [Google Marketing Platform Certification Exams : Google](https://markposition.wordpress.com/2021/09/10/google-marketing-platform-certification-exams-google/)
- [September 10, 2021](https://markposition.wordpress.com/2021/09/10/google-marketing-platform-certification-exams-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/09/10/google-marketing-platform-certification-exams-google/#respond)
https://skillshop.exceedlms.com/student/catalog/list?category_ids=707-google-marketing-platform-certification-exams
- [https://skillshop.exceedlms.com/student/catalog/list?category_ids=707-google-marketing-platform-certification-exams](https://skillshop.exceedlms.com/student/catalog/list?category_ids=707-google-marketing-platform-certification-exams)

## YouTube Advertising – Online Video Advertising Campaigns
- [YouTube Advertising – Online Video Advertising Campaigns](https://markposition.wordpress.com/2021/09/05/youtube-advertising-online-video-advertising-campaigns-4/)
- [September 5, 2021](https://markposition.wordpress.com/2021/09/05/youtube-advertising-online-video-advertising-campaigns-4/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/09/05/youtube-advertising-online-video-advertising-campaigns-4/#respond)
https://www.youtube.com/ads/
- [https://www.youtube.com/ads/](https://www.youtube.com/ads/)

## Make Quality Advertising Videos – YouTube Advertising
- [Make Quality Advertising Videos – YouTube Advertising](https://markposition.wordpress.com/2021/09/05/make-quality-advertising-videos-youtube-advertising-3/)
- [September 5, 2021](https://markposition.wordpress.com/2021/09/05/make-quality-advertising-videos-youtube-advertising-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/09/05/make-quality-advertising-videos-youtube-advertising-3/#respond)
https://www.youtube.com/ads/making-a-video-ad/
- [https://www.youtube.com/ads/making-a-video-ad/](https://www.youtube.com/ads/making-a-video-ad/)

## Outbrain – Recommendation Platform Powered by Native Ads
- [Outbrain – Recommendation Platform Powered by Native Ads](https://markposition.wordpress.com/2021/09/02/outbrain-recommendation-platform-powered-by-native-ads-2/)
- [September 2, 2021](https://markposition.wordpress.com/2021/09/02/outbrain-recommendation-platform-powered-by-native-ads-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/09/02/outbrain-recommendation-platform-powered-by-native-ads-2/#respond)
https://www.outbrain.com/
- [https://www.outbrain.com/](https://www.outbrain.com/)

## Digital Advertising Platform | Criteo
- [Digital Advertising Platform | Criteo](https://markposition.wordpress.com/2021/08/25/digital-advertising-platform-criteo/)
- [August 25, 2021](https://markposition.wordpress.com/2021/08/25/digital-advertising-platform-criteo/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/25/digital-advertising-platform-criteo/#respond)
https://www.criteo.com/technology/advertising-platform/
- [https://www.criteo.com/technology/advertising-platform/](https://www.criteo.com/technology/advertising-platform/)

## Programmatic advertising | BidTheatre Demand Side Platform
- [Programmatic advertising | BidTheatre Demand Side Platform](https://markposition.wordpress.com/2021/08/25/programmatic-advertising-bidtheatre-demand-side-platform/)
- [August 25, 2021](https://markposition.wordpress.com/2021/08/25/programmatic-advertising-bidtheatre-demand-side-platform/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/25/programmatic-advertising-bidtheatre-demand-side-platform/#respond)
https://www.bidtheatre.com/
- [https://www.bidtheatre.com/](https://www.bidtheatre.com/)

## ShareThis: Free Share Buttons & Plugins, Global Behavioral Data Solutions
- [ShareThis: Free Share Buttons & Plugins, Global Behavioral Data Solutions](https://markposition.wordpress.com/2021/08/25/sharethis-free-share-buttons-plugins-global-behavioral-data-solutions/)
- [August 25, 2021](https://markposition.wordpress.com/2021/08/25/sharethis-free-share-buttons-plugins-global-behavioral-data-solutions/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/25/sharethis-free-share-buttons-plugins-global-behavioral-data-solutions/#respond)
https://sharethis.com/
- [https://sharethis.com/](https://sharethis.com/)

## AdMaxim Inc. – Integrated Digital Advertising Platform
- [AdMaxim Inc. – Integrated Digital Advertising Platform](https://markposition.wordpress.com/2021/08/25/admaxim-inc-integrated-digital-advertising-platform/)
- [August 25, 2021](https://markposition.wordpress.com/2021/08/25/admaxim-inc-integrated-digital-advertising-platform/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/25/admaxim-inc-integrated-digital-advertising-platform/#respond)
http://www.admaxim.com/
- [http://www.admaxim.com/](http://www.admaxim.com/)

## Kwanko – Your Performance Marketing Partner
- [Kwanko – Your Performance Marketing Partner](https://markposition.wordpress.com/2021/08/25/kwanko-your-performance-marketing-partner/)
- [August 25, 2021](https://markposition.wordpress.com/2021/08/25/kwanko-your-performance-marketing-partner/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/25/kwanko-your-performance-marketing-partner/#respond)
https://www.kwanko.com/
- [https://www.kwanko.com/](https://www.kwanko.com/)

## Online marketing. Simplified | Adzooma
- [Online marketing. Simplified | Adzooma](https://markposition.wordpress.com/2021/08/24/online-marketing-simplified-adzooma/)
- [August 24, 2021](https://markposition.wordpress.com/2021/08/24/online-marketing-simplified-adzooma/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/24/online-marketing-simplified-adzooma/#respond)
https://www.adzooma.com/
- [https://www.adzooma.com/](https://www.adzooma.com/)

## Adzooma Marketplace | Find The Right Service For Your Business | Adzooma Marketplace
- [Adzooma Marketplace | Find The Right Service For Your Business | Adzooma Marketplace](https://markposition.wordpress.com/2021/08/24/adzooma-marketplace-find-the-right-service-for-your-business-adzooma-marketplace/)
- [August 24, 2021](https://markposition.wordpress.com/2021/08/24/adzooma-marketplace-find-the-right-service-for-your-business-adzooma-marketplace/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/24/adzooma-marketplace-find-the-right-service-for-your-business-adzooma-marketplace/#respond)
https://marketplace.adzooma.com/
- [https://marketplace.adzooma.com/](https://marketplace.adzooma.com/)

## LinkedIn Campaign Manager
- [LinkedIn Campaign Manager](https://markposition.wordpress.com/2021/08/23/linkedin-campaign-manager/)
- [August 23, 2021](https://markposition.wordpress.com/2021/08/23/linkedin-campaign-manager/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/23/linkedin-campaign-manager/#respond)
https://www.linkedin.com/campaignmanager/new-advertiser
- [https://www.linkedin.com/campaignmanager/new-advertiser](https://www.linkedin.com/campaignmanager/new-advertiser)

## Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions
- [Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions](https://markposition.wordpress.com/2021/08/23/marketing-advertising-on-linkedin-linkedin-marketing-solutions/)
- [August 23, 2021](https://markposition.wordpress.com/2021/08/23/marketing-advertising-on-linkedin-linkedin-marketing-solutions/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/23/marketing-advertising-on-linkedin-linkedin-marketing-solutions/#respond)
https://business.linkedin.com/marketing-solutions
- [https://business.linkedin.com/marketing-solutions](https://business.linkedin.com/marketing-solutions)

## Google Ads – privucite više korisnika jednostavnim online oglašavanjem
- [Google Ads – privucite više korisnika jednostavnim online oglašavanjem](https://markposition.wordpress.com/2021/08/20/google-ads-privucite-vise-korisnika-jednostavnim-online-oglasavanjem-6/)
- [August 20, 2021August 20, 2021](https://markposition.wordpress.com/2021/08/20/google-ads-privucite-vise-korisnika-jednostavnim-online-oglasavanjem-6/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/20/google-ads-privucite-vise-korisnika-jednostavnim-online-oglasavanjem-6/#respond)
https://ads.google.com
- [https://ads.google.com](https://ads.google.com/intl/hr_hr/getstarted/?subid=hr-hr-ha-aw-sk-m-bau!o3~Cj0KCQjwpf2IBhDkARIsAGVo0D3Wryak_hHyBl23URk7i9rUzFQcSDfFRCTDFLY-609ii68BQnjRsg0aAk0TEALw_wcB~117699885987~kwd-94527731~11806561409~485142535412)

## Cross-Channel Marketing Platform to Improve Customer Experiences – Iterable
- [Cross-Channel Marketing Platform to Improve Customer Experiences – Iterable](https://markposition.wordpress.com/2021/08/20/cross-channel-marketing-platform-to-improve-customer-experiences-iterable/)
- [August 20, 2021](https://markposition.wordpress.com/2021/08/20/cross-channel-marketing-platform-to-improve-customer-experiences-iterable/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/20/cross-channel-marketing-platform-to-improve-customer-experiences-iterable/#respond)
https://iterable.com/
- [https://iterable.com/](https://iterable.com/)

## LinkedIn Ads: Targeted Self-Service Ads | LinkedIn Marketing Solutions
- [LinkedIn Ads: Targeted Self-Service Ads | LinkedIn Marketing Solutions](https://markposition.wordpress.com/2021/08/20/linkedin-ads-targeted-self-service-ads-linkedin-marketing-solutions/)
- [August 20, 2021](https://markposition.wordpress.com/2021/08/20/linkedin-ads-targeted-self-service-ads-linkedin-marketing-solutions/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/20/linkedin-ads-targeted-self-service-ads-linkedin-marketing-solutions/#respond)
https://business.linkedin.com/marketing-solutions/ads
- [https://business.linkedin.com/marketing-solutions/ads](https://business.linkedin.com/marketing-solutions/ads)

## Setupad.com – Monetization Partner – Setupad
- [Setupad.com – Monetization Partner – Setupad](https://markposition.wordpress.com/2021/08/20/setupad-com-monetization-partner-setupad/)
- [August 20, 2021](https://markposition.wordpress.com/2021/08/20/setupad-com-monetization-partner-setupad/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/20/setupad-com-monetization-partner-setupad/#respond)
https://setupad.com/
- [https://setupad.com/](https://setupad.com/)

## Evidon | Digital Governance, Privacy Compliance, Website Monitoring
- [Evidon | Digital Governance, Privacy Compliance, Website Monitoring](https://markposition.wordpress.com/2021/08/04/evidon-digital-governance-privacy-compliance-website-monitoring-2/)
- [August 4, 2021](https://markposition.wordpress.com/2021/08/04/evidon-digital-governance-privacy-compliance-website-monitoring-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/08/04/evidon-digital-governance-privacy-compliance-website-monitoring-2/#respond)
https://www.evidon.com/
- [https://www.evidon.com/](https://www.evidon.com/)

## NextRoll – Home
- [NextRoll – Home](https://markposition.wordpress.com/2021/07/31/nextroll-home-2/)
- [July 31, 2021](https://markposition.wordpress.com/2021/07/31/nextroll-home-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/31/nextroll-home-2/#respond)
https://www.nextroll.com/
- [https://www.nextroll.com/](https://www.nextroll.com/)

## Adzooma | Simplify, Automate & Optimise Online Ad Campaigns
- [Adzooma | Simplify, Automate & Optimise Online Ad Campaigns](https://markposition.wordpress.com/2021/07/30/adzooma-simplify-automate-optimise-online-ad-campaigns-2/)
- [July 30, 2021](https://markposition.wordpress.com/2021/07/30/adzooma-simplify-automate-optimise-online-ad-campaigns-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/30/adzooma-simplify-automate-optimise-online-ad-campaigns-2/#respond)
https://www.adzooma.com/
- [https://www.adzooma.com/](https://www.adzooma.com/)

## Outbrain – Recommendation Platform Powered by Native Ads
- [Outbrain – Recommendation Platform Powered by Native Ads](https://markposition.wordpress.com/2021/07/30/outbrain-recommendation-platform-powered-by-native-ads/)
- [July 30, 2021](https://markposition.wordpress.com/2021/07/30/outbrain-recommendation-platform-powered-by-native-ads/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/30/outbrain-recommendation-platform-powered-by-native-ads/#respond)
https://www.outbrain.com/
- [https://www.outbrain.com/](https://www.outbrain.com/)

## Bing Webmaster Tools
- [Bing Webmaster Tools](https://markposition.wordpress.com/2021/07/30/bing-webmaster-tools-2/)
- [July 30, 2021](https://markposition.wordpress.com/2021/07/30/bing-webmaster-tools-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/30/bing-webmaster-tools-2/#respond)
https://www.bing.com/webmasters/about
- [https://www.bing.com/webmasters/about](https://www.bing.com/webmasters/about)
- [July 25, 2021July 25, 2021](https://markposition.wordpress.com/2021/07/25/447/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/25/447/#respond)
https://www.yourprimer.com
- [https://www.yourprimer.com](https://www.yourprimer.com)

## Lesson Catalog | Business & Operations – Google Primer
- [Lesson Catalog | Business & Operations – Google Primer](https://markposition.wordpress.com/2021/07/25/lesson-catalog-business-operations-google-primer/)
- [July 25, 2021](https://markposition.wordpress.com/2021/07/25/lesson-catalog-business-operations-google-primer/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/25/lesson-catalog-business-operations-google-primer/#respond)
https://www.yourprimer.com/en/lesson-catalog/0
- [https://www.yourprimer.com/en/lesson-catalog/0](https://www.yourprimer.com/en/lesson-catalog/0)

## Google trends
- [Google trends](https://markposition.wordpress.com/2021/07/25/google-trends/)
- [July 25, 2021](https://markposition.wordpress.com/2021/07/25/google-trends/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/25/google-trends/#respond)
https://trends.google.com/trends
- [https://trends.google.com/trends](https://trends.google.com/trends)

## Google Ads – privucite više korisnika jednostavnim online oglašavanjem
- [Google Ads – privucite više korisnika jednostavnim online oglašavanjem](https://markposition.wordpress.com/2021/07/25/google-ads-privucite-vise-korisnika-jednostavnim-online-oglasavanjem-5/)
- [July 25, 2021](https://markposition.wordpress.com/2021/07/25/google-ads-privucite-vise-korisnika-jednostavnim-online-oglasavanjem-5/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/25/google-ads-privucite-vise-korisnika-jednostavnim-online-oglasavanjem-5/#respond)
https://ads.google.com/intl/hr_hr/getstarted/
- [https://ads.google.com/intl/hr_hr/getstarted/](https://ads.google.com/intl/hr_hr/getstarted/)

## Set up conversion tracking for your website – Google Ads Help
- [Set up conversion tracking for your website – Google Ads Help](https://markposition.wordpress.com/2021/07/25/set-up-conversion-tracking-for-your-website-google-ads-help-2/)
- [July 25, 2021](https://markposition.wordpress.com/2021/07/25/set-up-conversion-tracking-for-your-website-google-ads-help-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/25/set-up-conversion-tracking-for-your-website-google-ads-help-2/#respond)
https://support.google.com/google-ads/answer/6095821?hl=en
- [https://support.google.com/google-ads/answer/6095821?hl=en](https://support.google.com/google-ads/answer/6095821?hl=en)

## Overview – Microsoft Advertising
- [Overview – Microsoft Advertising](https://markposition.wordpress.com/2021/07/22/overview-microsoft-advertising/)
- [July 22, 2021](https://markposition.wordpress.com/2021/07/22/overview-microsoft-advertising/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/22/overview-microsoft-advertising/#respond)
https://about.ads.microsoft.com/en-us/h/a/microsoft-advertising
- [https://about.ads.microsoft.com/en-us/h/a/microsoft-advertising](https://about.ads.microsoft.com/en-us/h/a/microsoft-advertising)

## Midas Network – Platforma za Nativno oglašavanje
- [Midas Network – Platforma za Nativno oglašavanje](https://markposition.wordpress.com/2021/07/22/midas-network-platforma-za-nativno-oglasavanje-2/)
- [July 22, 2021](https://markposition.wordpress.com/2021/07/22/midas-network-platforma-za-nativno-oglasavanje-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/22/midas-network-platforma-za-nativno-oglasavanje-2/#respond)
https://www.midas-network.com/hr
- [https://www.midas-network.com/hr](https://www.midas-network.com/hr)

## SEM with Microsoft Advertising – Microsoft Advertising
- [SEM with Microsoft Advertising – Microsoft Advertising](https://markposition.wordpress.com/2021/07/20/sem-with-microsoft-advertising-microsoft-advertising-3/)
- [July 20, 2021](https://markposition.wordpress.com/2021/07/20/sem-with-microsoft-advertising-microsoft-advertising-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/20/sem-with-microsoft-advertising-microsoft-advertising-3/#respond)
https://about.ads.microsoft.com/en-us
- [https://about.ads.microsoft.com/en-us](https://about.ads.microsoft.com/en-us)

## Advertise Your Website – Getting Started – Google Domains
- [Advertise Your Website – Getting Started – Google Domains](https://markposition.wordpress.com/2021/07/15/advertise-your-website-getting-started-google-domains/)
- [July 15, 2021](https://markposition.wordpress.com/2021/07/15/advertise-your-website-getting-started-google-domains/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/15/advertise-your-website-getting-started-google-domains/#respond)
https://domains.google/get-started/online-ads/
- [https://domains.google/get-started/online-ads/](https://domains.google/get-started/online-ads/)

## Amazon Advertising: Online advertising for businesses of all sizes
- [Amazon Advertising: Online advertising for businesses of all sizes](https://markposition.wordpress.com/2021/07/09/amazon-advertising-online-advertising-for-businesses-of-all-sizes-3/)
- [July 9, 2021](https://markposition.wordpress.com/2021/07/09/amazon-advertising-online-advertising-for-businesses-of-all-sizes-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/09/amazon-advertising-online-advertising-for-businesses-of-all-sizes-3/#respond)
https://advertising.amazon.com/
- [https://advertising.amazon.com/](https://advertising.amazon.com/)

## Amazon Advertising: Online advertising for businesses of all sizes
- [Amazon Advertising: Online advertising for businesses of all sizes](https://markposition.wordpress.com/2021/07/09/amazon-advertising-online-advertising-for-businesses-of-all-sizes-2/)
- [July 9, 2021](https://markposition.wordpress.com/2021/07/09/amazon-advertising-online-advertising-for-businesses-of-all-sizes-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/09/amazon-advertising-online-advertising-for-businesses-of-all-sizes-2/#respond)
https://advertising.amazon.com/
- [https://advertising.amazon.com/](https://advertising.amazon.com/)

## Learning console – amazon catalog
- [Learning console – amazon catalog](https://markposition.wordpress.com/2021/07/07/learning-console-amazon-catalog/)
- [July 7, 2021](https://markposition.wordpress.com/2021/07/07/learning-console-amazon-catalog/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/07/learning-console-amazon-catalog/#respond)
https://learningconsole.amazonadvertising.com/student/catalog/list
- [https://learningconsole.amazonadvertising.com/student/catalog/list](https://learningconsole.amazonadvertising.com/student/catalog/list)

## Learning console – amazon advertising
- [Learning console – amazon advertising](https://markposition.wordpress.com/2021/07/07/learning-console-amazon-advertising/)
- [July 7, 2021](https://markposition.wordpress.com/2021/07/07/learning-console-amazon-advertising/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/07/learning-console-amazon-advertising/#respond)
https://learningconsole.amazonadvertising.com/student/catalog
- [https://learningconsole.amazonadvertising.com/student/catalog](https://learningconsole.amazonadvertising.com/student/catalog)

## Advertising solutions for KDP authors | Amazon Advertising
- [Advertising solutions for KDP authors | Amazon Advertising](https://markposition.wordpress.com/2021/07/07/advertising-solutions-for-kdp-authors-amazon-advertising/)
- [July 7, 2021](https://markposition.wordpress.com/2021/07/07/advertising-solutions-for-kdp-authors-amazon-advertising/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/07/advertising-solutions-for-kdp-authors-amazon-advertising/#respond)
https://advertising.amazon.com/kdp-authors
- [https://advertising.amazon.com/kdp-authors](https://advertising.amazon.com/kdp-authors)

## Amazon.com: Kindle Direct Publishing: Promotion Manager
- [Amazon.com: Kindle Direct Publishing: Promotion Manager](https://markposition.wordpress.com/2021/07/07/amazon-com-kindle-direct-publishing-promotion-manager/)
- [July 7, 2021](https://markposition.wordpress.com/2021/07/07/amazon-com-kindle-direct-publishing-promotion-manager/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/07/amazon-com-kindle-direct-publishing-promotion-manager/#respond)
https://kdp.amazon.com/marketing/A2B1V7EPJ81WN2/promotion-manager
- [https://kdp.amazon.com/marketing/A2B1V7EPJ81WN2/promotion-manager](https://kdp.amazon.com/marketing/A2B1V7EPJ81WN2/promotion-manager)

## Amazon Advertising: Online advertising for businesses of all sizes
- [Amazon Advertising: Online advertising for businesses of all sizes](https://markposition.wordpress.com/2021/07/07/amazon-advertising-online-advertising-for-businesses-of-all-sizes/)
- [July 7, 2021](https://markposition.wordpress.com/2021/07/07/amazon-advertising-online-advertising-for-businesses-of-all-sizes/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/07/amazon-advertising-online-advertising-for-businesses-of-all-sizes/#respond)
https://advertising.amazon.com/
- [https://advertising.amazon.com/](https://advertising.amazon.com/)

## All Your Digital Marketing Tools in One Place – Sendinblue
- [All Your Digital Marketing Tools in One Place – Sendinblue](https://markposition.wordpress.com/2021/07/02/all-your-digital-marketing-tools-in-one-place-sendinblue/)
- [July 2, 2021](https://markposition.wordpress.com/2021/07/02/all-your-digital-marketing-tools-in-one-place-sendinblue/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/02/all-your-digital-marketing-tools-in-one-place-sendinblue/#respond)
https://www.sendinblue.com/
- [https://www.sendinblue.com/](https://www.sendinblue.com/)

## Digital Marketing & Growth Marketing Platform | AdRoll
- [Digital Marketing & Growth Marketing Platform | AdRoll](https://markposition.wordpress.com/2021/07/02/digital-marketing-growth-marketing-platform-adroll-3/)
- [July 2, 2021](https://markposition.wordpress.com/2021/07/02/digital-marketing-growth-marketing-platform-adroll-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/02/digital-marketing-growth-marketing-platform-adroll-3/#respond)
https://www.adroll.com/
- [https://www.adroll.com/](https://www.adroll.com/)

## Facebook for Business: Marketing on Facebook
- [Facebook for Business: Marketing on Facebook](https://markposition.wordpress.com/2021/07/01/facebook-for-business-marketing-on-facebook-3/)
- [July 1, 2021](https://markposition.wordpress.com/2021/07/01/facebook-for-business-marketing-on-facebook-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/07/01/facebook-for-business-marketing-on-facebook-3/#respond)
https://web.facebook.com/business
- [https://web.facebook.com/business](https://web.facebook.com/business)

## Grow your revenue and monetize your game or app | Unity Ads | Unity
- [Grow your revenue and monetize your game or app | Unity Ads | Unity](https://markposition.wordpress.com/2021/06/30/grow-your-revenue-and-monetize-your-game-or-app-unity-ads-unity/)
- [June 30, 2021](https://markposition.wordpress.com/2021/06/30/grow-your-revenue-and-monetize-your-game-or-app-unity-ads-unity/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/30/grow-your-revenue-and-monetize-your-game-or-app-unity-ads-unity/#respond)
https://unity.com/products/unity-ads-monetize
- [https://unity.com/products/unity-ads-monetize](https://unity.com/products/unity-ads-monetize)

## Grow user LTV with ads and In-app purchases | Mobile game monetization | Unity
- [Grow user LTV with ads and In-app purchases | Mobile game monetization | Unity](https://markposition.wordpress.com/2021/06/30/grow-user-ltv-with-ads-and-in-app-purchases-mobile-game-monetization-unity/)
- [June 30, 2021](https://markposition.wordpress.com/2021/06/30/grow-user-ltv-with-ads-and-in-app-purchases-mobile-game-monetization-unity/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/30/grow-user-ltv-with-ads-and-in-app-purchases-mobile-game-monetization-unity/#respond)
https://unity.com/solutions/unity-ads
- [https://unity.com/solutions/unity-ads](https://unity.com/solutions/unity-ads)

## Snapchat Ads | Snapchat for Business
- [Snapchat Ads | Snapchat for Business](https://markposition.wordpress.com/2021/06/25/snapchat-ads-snapchat-for-business/)
- [June 25, 2021](https://markposition.wordpress.com/2021/06/25/snapchat-ads-snapchat-for-business/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/25/snapchat-ads-snapchat-for-business/#respond)
https://forbusiness.snapchat.com/
- [https://forbusiness.snapchat.com/](https://forbusiness.snapchat.com/)

## Google Ad Manager – Get in touch
- [Google Ad Manager – Get in touch](https://markposition.wordpress.com/2021/06/25/google-ad-manager-get-in-touch/)
- [June 25, 2021](https://markposition.wordpress.com/2021/06/25/google-ad-manager-get-in-touch/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/25/google-ad-manager-get-in-touch/#respond)
https://admanager.google.com/home/contact-us/
- [https://admanager.google.com/home/contact-us/](https://admanager.google.com/home/contact-us/)

## Google Ad Manager – Integrated Advertising Management Platform
- [Google Ad Manager – Integrated Advertising Management Platform](https://markposition.wordpress.com/2021/06/25/google-ad-manager-integrated-advertising-management-platform/)
- [June 25, 2021](https://markposition.wordpress.com/2021/06/25/google-ad-manager-integrated-advertising-management-platform/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/25/google-ad-manager-integrated-advertising-management-platform/#respond)
https://admanager.google.com/home/
- [https://admanager.google.com/home/](https://admanager.google.com/home/)

## Admiral: The Visitor Relationship Management Company
- [Admiral: The Visitor Relationship Management Company](https://markposition.wordpress.com/2021/06/24/admiral-the-visitor-relationship-management-company-3/)
- [June 24, 2021](https://markposition.wordpress.com/2021/06/24/admiral-the-visitor-relationship-management-company-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/24/admiral-the-visitor-relationship-management-company-3/#respond)
https://www.getadmiral.com/
- [https://www.getadmiral.com/](https://www.getadmiral.com/)

## SEM with Microsoft Advertising – Microsoft Advertising
- [SEM with Microsoft Advertising – Microsoft Advertising](https://markposition.wordpress.com/2021/06/14/sem-with-microsoft-advertising-microsoft-advertising-2/)
- [June 14, 2021](https://markposition.wordpress.com/2021/06/14/sem-with-microsoft-advertising-microsoft-advertising-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/14/sem-with-microsoft-advertising-microsoft-advertising-2/#respond)
https://about.ads.microsoft.com/en-us
- [https://about.ads.microsoft.com/en-us](https://about.ads.microsoft.com/en-us)

## Ad settings google
- [Ad settings google](https://markposition.wordpress.com/2021/06/13/ad-settings-google/)
- [June 13, 2021](https://markposition.wordpress.com/2021/06/13/ad-settings-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/13/ad-settings-google/#respond)
https://adssettings.google.com/
- [https://adssettings.google.com/](https://adssettings.google.com/authenticated)

## Google Ads Data and Privacy – Google Safety Center
- [Google Ads Data and Privacy – Google Safety Center](https://markposition.wordpress.com/2021/06/13/google-ads-data-and-privacy-google-safety-center/)
- [June 13, 2021](https://markposition.wordpress.com/2021/06/13/google-ads-data-and-privacy-google-safety-center/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/13/google-ads-data-and-privacy-google-safety-center/#respond)
https://safety.google/privacy/ads-and-data/
- [https://safety.google/privacy/ads-and-data/](https://safety.google/privacy/ads-and-data/)

## Fat Frog Media
- [Fat Frog Media](https://markposition.wordpress.com/2021/06/13/fat-frog-media/)
- [June 13, 2021](https://markposition.wordpress.com/2021/06/13/fat-frog-media/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/13/fat-frog-media/#respond)
https://fatfrogmedia.com/
- [https://fatfrogmedia.com/](https://fatfrogmedia.com/)

## ToneDen – Automated Social Marketing
- [ToneDen – Automated Social Marketing](https://markposition.wordpress.com/2021/06/13/toneden-automated-social-marketing/)
- [June 13, 2021](https://markposition.wordpress.com/2021/06/13/toneden-automated-social-marketing/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/13/toneden-automated-social-marketing/#respond)
https://www.toneden.io/
- [https://www.toneden.io/](https://www.toneden.io/)

## Data Inventory & Mapping – TrustArc The Leader in Privacy Management Software
- [Data Inventory & Mapping – TrustArc The Leader in Privacy Management Software](https://markposition.wordpress.com/2021/06/12/data-inventory-mapping-trustarc-the-leader-in-privacy-management-software/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/data-inventory-mapping-trustarc-the-leader-in-privacy-management-software/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/data-inventory-mapping-trustarc-the-leader-in-privacy-management-software/#respond)
https://trustarc.com/data-inventory-mapping/
- [https://trustarc.com/data-inventory-mapping/](https://trustarc.com/data-inventory-mapping/)

## Technology Powered Partner Program – TrustArc The Leader in Privacy Management Software
- [Technology Powered Partner Program – TrustArc The Leader in Privacy Management Software](https://markposition.wordpress.com/2021/06/12/technology-powered-partner-program-trustarc-the-leader-in-privacy-management-software/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/technology-powered-partner-program-trustarc-the-leader-in-privacy-management-software/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/technology-powered-partner-program-trustarc-the-leader-in-privacy-management-software/#respond)
https://trustarc.com/technology-powered-partner-program/
- [https://trustarc.com/technology-powered-partner-program/](https://trustarc.com/technology-powered-partner-program/)

## Powered Partner Program – TrustArc The Leader in Privacy Management Software
- [Powered Partner Program – TrustArc The Leader in Privacy Management Software](https://markposition.wordpress.com/2021/06/12/powered-partner-program-trustarc-the-leader-in-privacy-management-software/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/powered-partner-program-trustarc-the-leader-in-privacy-management-software/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/powered-partner-program-trustarc-the-leader-in-privacy-management-software/#respond)
https://trustarc.com/powered-partner-program/
- [https://trustarc.com/powered-partner-program/](https://trustarc.com/powered-partner-program/)

## Cookie Consent Manager Free Trial Request – TrustArc The Leader in Privacy Management Software
- [Cookie Consent Manager Free Trial Request – TrustArc The Leader in Privacy Management Software](https://markposition.wordpress.com/2021/06/12/cookie-consent-manager-free-trial-request-trustarc-the-leader-in-privacy-management-software/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/cookie-consent-manager-free-trial-request-trustarc-the-leader-in-privacy-management-software/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/cookie-consent-manager-free-trial-request-trustarc-the-leader-in-privacy-management-software/#respond)
https://trustarc.com/cookie-consent-manager/professional-trial-account-request/?utm_source=ccm-trial
- [https://trustarc.com/cookie-consent-manager/professional-trial-account-request/?utm_source=ccm-trial](https://trustarc.com/cookie-consent-manager/professional-trial-account-request/?utm_source=ccm-trial)

## Home – TrustArc The Leader in Privacy Management Software
- [Home – TrustArc The Leader in Privacy Management Software](https://markposition.wordpress.com/2021/06/12/home-trustarc-the-leader-in-privacy-management-software-2-2/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/home-trustarc-the-leader-in-privacy-management-software-2-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/home-trustarc-the-leader-in-privacy-management-software-2-2/#respond)
https://trustarc.com/
- [https://trustarc.com/](https://trustarc.com/)

## WebChoices: Digital Advertising Alliance’s Consumer Choice Tool for Web US
- [WebChoices: Digital Advertising Alliance’s Consumer Choice Tool for Web US](https://markposition.wordpress.com/2021/06/12/webchoices-digital-advertising-alliances-consumer-choice-tool-for-web-us-2/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/webchoices-digital-advertising-alliances-consumer-choice-tool-for-web-us-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/webchoices-digital-advertising-alliances-consumer-choice-tool-for-web-us-2/#respond)
https://optout.aboutads.info/
- [https://optout.aboutads.info/](https://optout.aboutads.info/)

## Adobe Privacy Center
- [Adobe Privacy Center](https://markposition.wordpress.com/2021/06/12/adobe-privacy-center/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/adobe-privacy-center/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/adobe-privacy-center/#respond)
https://www.adobe.com/privacy/opt-out.html
- [https://www.adobe.com/privacy/opt-out.html](https://www.adobe.com/privacy/opt-out.html)

## TrustArc Preference Manager
- [TrustArc Preference Manager](https://markposition.wordpress.com/2021/06/12/trustarc-preference-manager/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/trustarc-preference-manager/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/trustarc-preference-manager/#respond)
http://preferences-mgr.truste.com/
- [http://preferences-mgr.truste.com/](http://preferences-mgr.truste.com/)

## WebChoices: Digital Advertising Alliance’s Consumer Choice Tool for Web US
- [WebChoices: Digital Advertising Alliance’s Consumer Choice Tool for Web US](https://markposition.wordpress.com/2021/06/12/webchoices-digital-advertising-alliances-consumer-choice-tool-for-web-us/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/webchoices-digital-advertising-alliances-consumer-choice-tool-for-web-us/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/webchoices-digital-advertising-alliances-consumer-choice-tool-for-web-us/#respond)
https://optout.aboutads.info/
- [https://optout.aboutads.info/](https://optout.aboutads.info/)

## Programmatic Digital Advertising Technology & Solutions | PubMatic
- [Programmatic Digital Advertising Technology & Solutions | PubMatic](https://markposition.wordpress.com/2021/06/12/programmatic-digital-advertising-technology-solutions-pubmatic/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/programmatic-digital-advertising-technology-solutions-pubmatic/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/programmatic-digital-advertising-technology-solutions-pubmatic/#respond)
https://pubmatic.com/
- [https://pubmatic.com/](https://pubmatic.com/)

## ownerIQ | Second-Party Data Solutions
- [ownerIQ | Second-Party Data Solutions](https://markposition.wordpress.com/2021/06/12/owneriq-second-party-data-solutions/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/owneriq-second-party-data-solutions/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/owneriq-second-party-data-solutions/#respond)
https://www.owneriq.com/
- [https://www.owneriq.com/](https://www.owneriq.com/)

## What is CRM? | Oracle
- [What is CRM? | Oracle](https://markposition.wordpress.com/2021/06/12/what-is-crm-oracle/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/what-is-crm-oracle/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/what-is-crm-oracle/#respond)
https://www.oracle.com/cx/what-is-crm/
- [https://www.oracle.com/cx/what-is-crm/](https://www.oracle.com/cx/what-is-crm/)

## Advertising and Customer Experience (CX) | Oracle
- [Advertising and Customer Experience (CX) | Oracle](https://markposition.wordpress.com/2021/06/12/advertising-and-customer-experience-cx-oracle/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/advertising-and-customer-experience-cx-oracle/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/advertising-and-customer-experience-cx-oracle/#respond)
https://www.oracle.com/cx/
- [https://www.oracle.com/cx/](https://www.oracle.com/cx/)

## Home – Inuvo.com
- [Home – Inuvo.com](https://markposition.wordpress.com/2021/06/12/home-inuvo-com/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/home-inuvo-com/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/home-inuvo-com/#respond)
https://inuvo.com/
- [https://inuvo.com/](https://inuvo.com/)

## Havas Edge
- [Havas Edge](https://markposition.wordpress.com/2021/06/12/havas-edge/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/havas-edge/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/havas-edge/#respond)
https://www.havasedge.com/
- [https://www.havasedge.com/](https://www.havasedge.com/)

## GumGum | Contextual Intelligence Company | High Impact Advertising Technology
- [GumGum | Contextual Intelligence Company | High Impact Advertising Technology](https://markposition.wordpress.com/2021/06/12/gumgum-contextual-intelligence-company-high-impact-advertising-technology/)
- [June 12, 2021](https://markposition.wordpress.com/2021/06/12/gumgum-contextual-intelligence-company-high-impact-advertising-technology/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/06/12/gumgum-contextual-intelligence-company-high-impact-advertising-technology/#respond)
https://gumgum.com/
- [https://gumgum.com/](https://gumgum.com/)

## Yotpo | eCommerce Marketing Platform
- [Yotpo | eCommerce Marketing Platform](https://markposition.wordpress.com/2021/05/27/yotpo-ecommerce-marketing-platform/)
- [May 27, 2021](https://markposition.wordpress.com/2021/05/27/yotpo-ecommerce-marketing-platform/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/27/yotpo-ecommerce-marketing-platform/#respond)
https://www.yotpo.com/
- [https://www.yotpo.com/](https://www.yotpo.com/)

## Yotpo | eCommerce Marketing Platform – Accelerate growth with a full suite of solutions for customer reviews, visual marketing, loyalty, referrals, and SMS marketing.Accelerate growth with a full suite of solutions for customer reviews, visual marketing, loyalty, referrals, and SMS marketing.
- [Yotpo | eCommerce Marketing Platform – Accelerate growth with a full suite of solutions for customer reviews, visual marketing, loyalty, referrals, and SMS marketing.Accelerate growth with a full suite of solutions for customer reviews, visual marketing, loyalty, referrals, and SMS marketing.](https://markposition.wordpress.com/2021/05/27/yotpo-ecommerce-marketing-platform-accelerate-growth-with-a-full-suite-of-solutions-for-customer-reviews-visual-marketing-loyalty-referrals-and-sms-marketing-accelerate-growth-with-a-full-suit/)
- [May 27, 2021](https://markposition.wordpress.com/2021/05/27/yotpo-ecommerce-marketing-platform-accelerate-growth-with-a-full-suite-of-solutions-for-customer-reviews-visual-marketing-loyalty-referrals-and-sms-marketing-accelerate-growth-with-a-full-suit/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/27/yotpo-ecommerce-marketing-platform-accelerate-growth-with-a-full-suite-of-solutions-for-customer-reviews-visual-marketing-loyalty-referrals-and-sms-marketing-accelerate-growth-with-a-full-suit/#respond)
https://www.yotpo.com/
- [https://www.yotpo.com/](https://www.yotpo.com/)

## Data-Driven Marketing Solutions | Audience Targeting | Social Media & Email Marketing Consultant
- [Data-Driven Marketing Solutions | Audience Targeting | Social Media & Email Marketing Consultant](https://markposition.wordpress.com/2021/05/26/data-driven-marketing-solutions-audience-targeting-social-media-email-marketing-consultant/)
- [May 26, 2021](https://markposition.wordpress.com/2021/05/26/data-driven-marketing-solutions-audience-targeting-social-media-email-marketing-consultant/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/26/data-driven-marketing-solutions-audience-targeting-social-media-email-marketing-consultant/#respond)
https://www.stirista.com/
- [https://www.stirista.com/](https://www.stirista.com/)

## Digital Marketing Services | Digital Logic ™
- [Digital Marketing Services | Digital Logic ™](https://markposition.wordpress.com/2021/05/26/digital-marketing-services-digital-logic/)
- [May 26, 2021](https://markposition.wordpress.com/2021/05/26/digital-marketing-services-digital-logic/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/26/digital-marketing-services-digital-logic/#respond)
https://www.digitallogic.co/
- [https://www.digitallogic.co/](https://www.digitallogic.co/)

## Shareaholic | Content Marketing Platform & Website Traffic Tools
- [Shareaholic | Content Marketing Platform & Website Traffic Tools](https://markposition.wordpress.com/2021/05/26/shareaholic-content-marketing-platform-website-traffic-tools/)
- [May 26, 2021](https://markposition.wordpress.com/2021/05/26/shareaholic-content-marketing-platform-website-traffic-tools/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/26/shareaholic-content-marketing-platform-website-traffic-tools/#respond)
https://www.shareaholic.com/
- [https://www.shareaholic.com/](https://www.shareaholic.com/)

## Advertise with us! – Vaping360
- [Advertise with us! – Vaping360](https://markposition.wordpress.com/2021/05/26/advertise-with-us-vaping360/)
- [May 26, 2021](https://markposition.wordpress.com/2021/05/26/advertise-with-us-vaping360/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/26/advertise-with-us-vaping360/#respond)
https://vaping360.com/advertise/
- [https://vaping360.com/advertise/](https://vaping360.com/advertise/)

## ScalerAI – The Ultimate Marketing Kit which will Boost your Sales
- [ScalerAI – The Ultimate Marketing Kit which will Boost your Sales](https://markposition.wordpress.com/2021/05/26/scalerai-the-ultimate-marketing-kit-which-will-boost-your-sales/)
- [May 26, 2021](https://markposition.wordpress.com/2021/05/26/scalerai-the-ultimate-marketing-kit-which-will-boost-your-sales/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/26/scalerai-the-ultimate-marketing-kit-which-will-boost-your-sales/#respond)
https://scalerai.com/
- [https://scalerai.com/](https://scalerai.com/)

## YouTube Advertising – Online Video Advertising Campaigns
- [YouTube Advertising – Online Video Advertising Campaigns](https://markposition.wordpress.com/2021/05/23/youtube-advertising-online-video-advertising-campaigns-3/)
- [May 23, 2021](https://markposition.wordpress.com/2021/05/23/youtube-advertising-online-video-advertising-campaigns-3/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/23/youtube-advertising-online-video-advertising-campaigns-3/#respond)
https://www.youtube.com/ads/
- [https://www.youtube.com/ads/](https://www.youtube.com/ads/)

## YouTube Select: Make the best of YouTube yours
- [YouTube Select: Make the best of YouTube yours](https://markposition.wordpress.com/2021/05/23/youtube-select-make-the-best-of-youtube-yours/)
- [May 23, 2021](https://markposition.wordpress.com/2021/05/23/youtube-select-make-the-best-of-youtube-yours/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/23/youtube-select-make-the-best-of-youtube-yours/#respond)
https://www.youtube.com/ads/youtube-select/
- [https://www.youtube.com/ads/youtube-select/](https://www.youtube.com/ads/youtube-select/)

## Account-Based (ABM) Platform | RollWorks
- [Account-Based (ABM) Platform | RollWorks](https://markposition.wordpress.com/2021/05/22/account-based-abm-platform-rollworks/)
- [May 22, 2021](https://markposition.wordpress.com/2021/05/22/account-based-abm-platform-rollworks/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/22/account-based-abm-platform-rollworks/#respond)
https://www.rollworks.com/
- [https://www.rollworks.com/](https://www.rollworks.com/)

## Digital Marketing & Growth Marketing Platform | AdRoll
- [Digital Marketing & Growth Marketing Platform | AdRoll](https://markposition.wordpress.com/2021/05/22/digital-marketing-growth-marketing-platform-adroll-2/)
- [May 22, 2021](https://markposition.wordpress.com/2021/05/22/digital-marketing-growth-marketing-platform-adroll-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/22/digital-marketing-growth-marketing-platform-adroll-2/#respond)
https://www.adroll.com/
- [https://www.adroll.com/](https://www.adroll.com/)

## NextRoll
- [NextRoll](https://markposition.wordpress.com/2021/05/22/nextroll/)
- [May 22, 2021](https://markposition.wordpress.com/2021/05/22/nextroll/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/22/nextroll/#respond)
https://www.nextroll.com/
- [https://www.nextroll.com/](https://www.nextroll.com/)

## Brand Push – Get featured on NBC, FOX, CBS and USA Today
- [Brand Push – Get featured on NBC, FOX, CBS and USA Today](https://markposition.wordpress.com/2021/05/21/brand-push-get-featured-on-nbc-fox-cbs-and-usa-today/)
- [May 21, 2021](https://markposition.wordpress.com/2021/05/21/brand-push-get-featured-on-nbc-fox-cbs-and-usa-today/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/21/brand-push-get-featured-on-nbc-fox-cbs-and-usa-today/#respond)
https://www.brandpush.co/
- [https://www.brandpush.co/](https://www.brandpush.co/)

## UK Ecommerce Growth Partner | Pattern
- [UK Ecommerce Growth Partner | Pattern](https://markposition.wordpress.com/2021/05/19/uk-ecommerce-growth-partner-pattern/)
- [May 19, 2021](https://markposition.wordpress.com/2021/05/19/uk-ecommerce-growth-partner-pattern/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/19/uk-ecommerce-growth-partner-pattern/#respond)
https://pattern.com/uk/
- [https://pattern.com/uk/](https://pattern.com/uk/)

## SEO Company | Digital Marketing Agency That Drives Results
- [SEO Company | Digital Marketing Agency That Drives Results](https://markposition.wordpress.com/2021/05/19/seo-company-digital-marketing-agency-that-drives-results/)
- [May 19, 2021](https://markposition.wordpress.com/2021/05/19/seo-company-digital-marketing-agency-that-drives-results/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/19/seo-company-digital-marketing-agency-that-drives-results/#respond)
https://www.webfx.com/
- [https://www.webfx.com/](https://www.webfx.com/)

## Apester
- [Apester](https://markposition.wordpress.com/2021/05/11/apester-2/)
- [May 11, 2021](https://markposition.wordpress.com/2021/05/11/apester-2/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/11/apester-2/#respond)
https://apester.com/
- [https://apester.com/](https://apester.com/)

## Bloomberg Service Center
- [Bloomberg Service Center](https://markposition.wordpress.com/2021/05/10/bloomberg-service-center/)
- [May 10, 2021](https://markposition.wordpress.com/2021/05/10/bloomberg-service-center/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/10/bloomberg-service-center/#respond)
https://service.bloomberg.com/portal/sessions/new
- [https://service.bloomberg.com/portal/sessions/new](https://service.bloomberg.com/portal/sessions/new)

## Connected Content™ | Investis Digital
- [Connected Content™ | Investis Digital](https://markposition.wordpress.com/2021/05/09/connected-content-investis-digital/)
- [May 9, 2021](https://markposition.wordpress.com/2021/05/09/connected-content-investis-digital/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/09/connected-content-investis-digital/#respond)
https://www.investisdigital.com/company/connected-content
- [https://www.investisdigital.com/company/connected-content](https://www.investisdigital.com/company/connected-content)

## Ghost: Turn your audience into a business
- [Ghost: Turn your audience into a business](https://markposition.wordpress.com/2021/05/09/ghost-turn-your-audience-into-a-business/)
- [May 9, 2021](https://markposition.wordpress.com/2021/05/09/ghost-turn-your-audience-into-a-business/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/09/ghost-turn-your-audience-into-a-business/#respond)
https://ghost.org/
- [https://ghost.org/](https://ghost.org/)

## Products – Mediavine
- [Products – Mediavine](https://markposition.wordpress.com/2021/05/08/products-mediavine/)
- [May 8, 2021](https://markposition.wordpress.com/2021/05/08/products-mediavine/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/08/products-mediavine/#respond)
https://www.mediavine.com/products/
- [https://www.mediavine.com/products/](https://www.mediavine.com/products/)

## Postanite partner | Certificirani partner – izdavač – Google
- [Postanite partner | Certificirani partner – izdavač – Google](https://markposition.wordpress.com/2021/05/08/postanite-partner-certificirani-partner-izdavac-google/)
- [May 8, 2021](https://markposition.wordpress.com/2021/05/08/postanite-partner-certificirani-partner-izdavac-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/08/postanite-partner-certificirani-partner-izdavac-google/#respond)
https://www.google.com/ads/publisher/partners/become-a-partner/
- [https://www.google.com/ads/publisher/partners/become-a-partner/](https://www.google.com/ads/publisher/partners/become-a-partner/)

## Pronađite partnera – izdavača | Certificirani partner – izdavač – Google
- [Pronađite partnera – izdavača | Certificirani partner – izdavač – Google](https://markposition.wordpress.com/2021/05/08/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google/)
- [May 8, 2021](https://markposition.wordpress.com/2021/05/08/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/08/pronadite-partnera-izdavaca-certificirani-partner-izdavac-google/#respond)
https://www.google.com/ads/publisher/partners/find-a-partner/#!?modal_active=none
- [https://www.google.com/ads/publisher/partners/find-a-partner/#!?modal_active=none](https://www.google.com/ads/publisher/partners/find-a-partner/#!?modal_active=none)

## Partnerski program za izdavaštvo | Certificirani partner – izdavač – Google
- [Partnerski program za izdavaštvo | Certificirani partner – izdavač – Google](https://markposition.wordpress.com/2021/05/08/partnerski-program-za-izdavastvo-certificirani-partner-izdavac-google/)
- [May 8, 2021](https://markposition.wordpress.com/2021/05/08/partnerski-program-za-izdavastvo-certificirani-partner-izdavac-google/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/08/partnerski-program-za-izdavastvo-certificirani-partner-izdavac-google/#respond)
https://www.google.com/ads/publisher/partners/
- [https://www.google.com/ads/publisher/partners/](https://www.google.com/ads/publisher/partners/)

## Google Ads Community
- [Google Ads Community](https://markposition.wordpress.com/2021/05/08/google-ads-community/)
- [May 8, 2021](https://markposition.wordpress.com/2021/05/08/google-ads-community/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/08/google-ads-community/#respond)
https://support.google.com/google-ads/community?hl=en
- [https://support.google.com/google-ads/community?hl=en](https://support.google.com/google-ads/community?hl=en)

## Full-Service Ad Management – Mediavine
- [Full-Service Ad Management – Mediavine](https://markposition.wordpress.com/2021/05/08/full-service-ad-management-mediavine/)
- [May 8, 2021](https://markposition.wordpress.com/2021/05/08/full-service-ad-management-mediavine/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/08/full-service-ad-management-mediavine/#respond)
https://www.mediavine.com/
- [https://www.mediavine.com/](https://www.mediavine.com/)

## Forbes Connect
- [Forbes Connect](https://markposition.wordpress.com/2021/05/08/forbes-connect/)
- [May 8, 2021](https://markposition.wordpress.com/2021/05/08/forbes-connect/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/08/forbes-connect/#respond)
https://www.forbes.com/connect/
- [https://www.forbes.com/connect/](https://www.forbes.com/connect/)

## Apester
- [Apester](https://markposition.wordpress.com/2021/05/06/apester/)
- [May 6, 2021](https://markposition.wordpress.com/2021/05/06/apester/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/06/apester/#respond)
https://apester.com/
- [https://apester.com/](https://apester.com/)

## Quiz Maker | Make Amazing Online Quizzes in Minutes
- [Quiz Maker | Make Amazing Online Quizzes in Minutes](https://markposition.wordpress.com/2021/05/06/quiz-maker-make-amazing-online-quizzes-in-minutes/)
- [May 6, 2021](https://markposition.wordpress.com/2021/05/06/quiz-maker-make-amazing-online-quizzes-in-minutes/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/06/quiz-maker-make-amazing-online-quizzes-in-minutes/#respond)
https://www.quiz-maker.com/
- [https://www.quiz-maker.com/](https://www.quiz-maker.com/)

## Digital Marketing Training Delivered by The Best.
- [Digital Marketing Training Delivered by The Best.](https://markposition.wordpress.com/2021/05/03/digital-marketing-training-delivered-by-the-best/)
- [May 3, 2021](https://markposition.wordpress.com/2021/05/03/digital-marketing-training-delivered-by-the-best/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/03/digital-marketing-training-delivered-by-the-best/#respond)
https://cxl.com/
- [https://cxl.com/](https://cxl.com/)

## RedTrack | Cookieless ad tracking solution for media-buyers
- [RedTrack | Cookieless ad tracking solution for media-buyers](https://markposition.wordpress.com/2021/05/02/redtrack-cookieless-ad-tracking-solution-for-media-buyers/)
- [May 2, 2021](https://markposition.wordpress.com/2021/05/02/redtrack-cookieless-ad-tracking-solution-for-media-buyers/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/02/redtrack-cookieless-ad-tracking-solution-for-media-buyers/#respond)
https://redtrack.io/
- [https://redtrack.io/](https://redtrack.io/)

## SEM with Microsoft Advertising – Microsoft Advertising
- [SEM with Microsoft Advertising – Microsoft Advertising](https://markposition.wordpress.com/2021/05/02/sem-with-microsoft-advertising-microsoft-advertising/)
- [May 2, 2021](https://markposition.wordpress.com/2021/05/02/sem-with-microsoft-advertising-microsoft-advertising/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/05/02/sem-with-microsoft-advertising-microsoft-advertising/#respond)
https://about.ads.microsoft.com/en-us
- [https://about.ads.microsoft.com/en-us](https://about.ads.microsoft.com/en-us)

## Programmatic Advertising Technology Company | Publift
- [Programmatic Advertising Technology Company | Publift](https://markposition.wordpress.com/2021/04/29/programmatic-advertising-technology-company-publift/)
- [April 29, 2021](https://markposition.wordpress.com/2021/04/29/programmatic-advertising-technology-company-publift/)
- [Filip Keser](https://markposition.wordpress.com/author/fkeser/)
- [Leave a comment](https://markposition.wordpress.com/2021/04/29/programmatic-advertising-technology-company-publift/#respond)
https://www.publift.com/
- [https://www.publift.com/](https://www.publift.com/)

## Posts navigation
- [Older Posts](https://markposition.wordpress.com/page/2/)
⭐
- [Create a website or blog at WordPress.com](https://wordpress.com/?ref=footer_custom_svg)

Stay informed with curated content and the latest headlines, all delivered straight to your inbox. Subscribe now to stay ahead and never miss a beat!
Type your email…
Subscribe
Skip to content ↓
- [Skip to content ↓](https://markposition.wordpress.com)
- [(position) mRNA](https://markposition.wordpress.com/)
- [Create a website or blog at WordPress.com](https://wordpress.com/?ref=footer_custom_svg)
- [Cookie Policy](https://automattic.com/cookies/)
- [(position) mRNA](https://markposition.wordpress.com)
- [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fmarkposition.wordpress.com%2F2022%2F10%2F05%2Fadvertising-amazon%2F&signup_flow=account)
- [(position) mRNA](https://markposition.wordpress.com)
- [Sign up](https://wordpress.com/start/)
- [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fmarkposition.wordpress.com%2F2022%2F10%2F05%2Fadvertising-amazon%2F&signup_flow=account)
- [Report this content](https://wordpress.com/abuse/?report_url=https://markposition.wordpress.com)
- [View site in Reader](https://wordpress.com/reader/feeds/106152382)
- [Manage subscriptions](https://subscribe.wordpress.com/)
- [Get started](https://wordpress.com/start/?ref=marketing_bar)

---

# iCloud: swarm_optimization.md

> **Source:** icloud://swarm_optimization.md
> **Analyzed At:** 2026-06-25T11:56:33.372Z

## Phase 19 Swarm Optimization
Adaptive latency thresholds. When stability index > 0.99, target heartbeat latency < 1ms.
