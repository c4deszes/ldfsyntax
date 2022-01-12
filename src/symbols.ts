'use strict';

import * as vscode from 'vscode';

function createFieldSymbol(name: string, line: vscode.TextLine) {
    return new vscode.DocumentSymbol(name, 'field', vscode.SymbolKind.Field, line.range, line.range);
}

function createGroupSymbol(name: string, line: vscode.TextLine) {
    return new vscode.DocumentSymbol(name, 'group', vscode.SymbolKind.Namespace, line.range, line.range);
}

export class LdfDocumentSymbolProvider implements vscode.DocumentSymbolProvider {
    
    provideDocumentSymbols(document: vscode.TextDocument, token: vscode.CancellationToken): vscode.ProviderResult<vscode.SymbolInformation[] | vscode.DocumentSymbol[]> {
        return new Promise((resolve, reject) => {
            let symbols: vscode.DocumentSymbol[] = [];

            for (let i = 0; i < document.lineCount; i++) {
                let line = document.lineAt(i);

                if (line.text.startsWith('LIN_protocol_version')) {
                    symbols.push(createFieldSymbol('protocol_version', line));
                }
                else if (line.text.startsWith('LIN_language_version')) {
                    symbols.push(createFieldSymbol('language_version', line));
                }
                else if (line.text.startsWith('LIN_speed')) {
                    symbols.push(createFieldSymbol('speed', line));
                }
                else if (line.text.startsWith('Channel_name')) {
                    symbols.push(createFieldSymbol('channel', line));
                }
            }
            resolve(symbols);
        });
    }
}
