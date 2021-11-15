from pygls.capabilities import COMPLETION, TEXT_DOCUMENT_DID_OPEN, TEXT_DOCUMENT_DID_CLOSE
from pygls.lsp.methods import TEXT_DOCUMENT_DID_CHANGE
from pygls.lsp.types.basic_structures import TextDocumentRegistrationOptions
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

server.start_io()
