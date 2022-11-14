// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import path = require('path');
import * as vscode from 'vscode';
import {
    LanguageClient,
    LanguageClientOptions,
    ServerOptions,
    TransportKind,
    Executable,
    ExecutableOptions
  } from 'vscode-languageclient/node';

let client: LanguageClient;

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
    let serverCommand = 'python ' + context.asAbsolutePath(path.join('server', 'server.py'));
    let commandOptions: ExecutableOptions = { detached: false, shell: true };

    let serverOptions: ServerOptions = {
        run: <Executable>{command: serverCommand, options: commandOptions},
        debug: <Executable>{command: serverCommand, options: commandOptions}
    };

    // Options to control the language client
    let clientOptions: LanguageClientOptions = {
        // Register the server for plain text documents
        documentSelector: ['ldf'],
        synchronize: {
            // Synchronize the setting section 'languageServerExample' to the server
            configurationSection: 'ldf-syntax-configuration',
            // Notify the server about file changes to '.ldf files contain in the workspace
            fileEvents: vscode.workspace.createFileSystemWatcher('**/*.ldf')
        }
    };

    client = new LanguageClient(
        'ldf-lsp',
        'LDF Language Server',
        serverOptions,
        clientOptions
    );

    client.start();
}

// this method is called when your extension is deactivated
export function deactivate() {
    if (!client) {
        return undefined;
    }
    return client.stop();
}
