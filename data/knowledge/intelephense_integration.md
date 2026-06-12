# Intelephense Premium

Getting Started
About
Intelephense is a high performance, cross platform, cross editor PHP language server adhering to the Language Server Protocol (LSP).

When paired with an LSP capable editor it provides an essential set of code tools, making for a productive and rich PHP coding experience.

The Intelephense server is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to premium features can be obtained by purchasing a licence key. This makes Intelephense the best solution for cross-platform PHP intelligence.

## Installation
### Visual Studio Code
Visual Studio Code users should install the Intelephense extension from within the extensions view or download it from the VSCode marketplace.

The built-in VSCode PHP Language Features extension can cause excessive completion suggestions that are out of context and is best disabled. Go to the Extensions UI and search for PHP Language Features to disable it. Alternatively, you can disable parts of it via it's configuration settings. Other third party extensions that provide similar functionality to Intelephense may also need to be disabled for best results.

Optionally purchase and enter your licence key by opening the command palette (Ctrl+Shift+P) and searching for Enter licence key.

A screen capture showing how to enter your intelephense licence key into VSCode.
Entering a licence key via the VS Code command palette

### Other Editors
Intelephense requires a Node.js runtime environment. It is recommended that you use a current LTS version of Node.js. To install Intelephense server you can use npm.

```
npm i intelephense -g
```

Intelephense needs an LSP compliant client to communicate with and integrate features into the editor. A list of editors and clients that support the LSP can be found here. Please follow the setup guide of the relevant tool. The information below may help in configuring the client.

To start the intelephense server:
```
intelephense {transport}
```
Where {transport} is one of:
--node-ipc
--stdio
--socket={number}
--pipe={string}

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

OS	Property	Path	Fallback
*nix	storagePath	$XDG_CONFIG_HOME/intelephense/workspace/	$HOME/.config/intelephense/workspace/
*nix	globalStoragePath	$XDG_CONFIG_HOME/intelephense/global/	$HOME/.config/intelephense/global/
*nix	licenceKey	{globalStoragePath}/licence.txt	{globalStoragePath}/license.txt
Windows	storagePath	%AppData%/intelephense/workspace/	%UserProfile%/intelephense/workspace/
Windows	globalStoragePath	%AppData%/intelephense/global/	%UserProfile%/intelephense/global/
Windows	licenceKey	{globalStoragePath}/licence.txt	{globalStoragePath}/license.txt

If your LSP client does not expose initializationOptions then a licence key can be provided by placing (only) the key in a text file at the default licenceKey path listed above.

## Configuration
Please see the VSCode client package.json configuration property for a full list of configuration options and associated JSON schema. Note that the configuration keys are given in dot notation. As an example, the equivalent JSON object for intelephense.files.exclude would be `{"intelephense": {"files": {"exclude": []}}}`.

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

Depending on the framework or library you use, you may find you need additional configuration to provide method declarations or override existing ones. Please see the Frameworks and Libraries section in the appendix for more information on this.

## Features
Intelephense provides a variety of features to enhance the development experience when working with PHP code. Many of these features are provided for free while others require a Premium licence to access. All images and videos in this section are taken from the VS Code client. The features are available to all LSP clients that support the relevant LSP methods. Keybindings listed for each feature are the defaults for the VS Code client.

### Free Features
The following features are available to all users of Intelephense. A licence is not necessary.
* Workspace Symbols
* Document Symbols
* Go to Definition
* Hover
* Highlight
* Code Completion
* Signature Help
* Find All References
* Formatting
* Diagnostics
* Inline Values
* Embedded Languages

### Premium Features
The following features require a licence to access.
* Rename
* Code Folding
* Find All Implementations
* Go to Type Definition
* Go to Declaration
* Smart Select
* Type Hierarchy
* Code Lens
* Inlay Hints
* Document Links
* Code Actions
