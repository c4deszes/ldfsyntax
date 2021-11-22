from pygls.capabilities import COMPLETION, TEXT_DOCUMENT_DID_OPEN, TEXT_DOCUMENT_DID_CLOSE
from pygls.lsp.methods import DEFINITION, TEXT_DOCUMENT_DID_CHANGE
from pygls.lsp.types.basic_structures import Location, Position, Range, TextDocumentRegistrationOptions
from pygls.lsp.types.language_features.definition import DefinitionParams
from pygls.lsp.types.workspace import DidChangeTextDocumentParams, DidCloseTextDocumentParams, DidOpenTextDocumentParams
from pygls.server import LanguageServer
from pygls.lsp import CompletionItem, CompletionList, CompletionOptions, CompletionParams
import logging

server = LanguageServer()

@server.feature(COMPLETION, CompletionOptions(trigger_characters=[',']))
def completions(server: LanguageServer, params: CompletionParams):
    """Returns completion items."""
    return CompletionList(
        is_incomplete=False,
        items=[
            CompletionItem(label='{'),
            CompletionItem(label='}'),
        ]
    )

@server.feature(TEXT_DOCUMENT_DID_OPEN)
async def openHandler(server: LanguageServer, params: DidOpenTextDocumentParams):
    server.show_message_log(f"Opened document: {params.text_document.uri}")

@server.feature(TEXT_DOCUMENT_DID_CLOSE)
def closeHandler(server: LanguageServer, params: DidCloseTextDocumentParams):
    server.show_message_log(f"Closed document: {params.text_document.uri}")

@server.feature(TEXT_DOCUMENT_DID_CHANGE)
def changeHandler(server: LanguageServer, params: DidChangeTextDocumentParams):
    server.show_message_log(f"Changed document: {params.text_document.uri}")

@server.feature(DEFINITION)
def onDefinition(server: LanguageServer, params: DefinitionParams):
    word = server.workspace.get_document(params.text_document.uri).word_at_position(params.position)
    server.show_message_log(f"Requesting definition at {params.position.line}:{params.position.character} Word: {word}")
    return Location(uri=params.text_document.uri, range=Range(start=Position(line=0, character=0), end=Position(line=0, character=0)))

server.start_io()
