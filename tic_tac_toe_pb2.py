# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tic_tac_toe.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11tic_tac_toe.proto\x12\tTicTacToe\"\x15\n\x13\x41ssignPlayerRequest\"-\n\x14\x41ssignPlayerResponse\x12\x15\n\rplayer_number\x18\x01 \x01(\x05\":\n\x0bMoveRequest\x12\x0e\n\x06player\x18\x01 \x01(\x05\x12\x0b\n\x03row\x18\x02 \x01(\x05\x12\x0e\n\x06\x63olumn\x18\x03 \x01(\x05\"0\n\x0cMoveResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x14\n\x12\x43heckWinnerRequest\"L\n\x13\x43heckWinnerResponse\x12\x0e\n\x06winner\x18\x01 \x01(\x05\x12\r\n\x05\x62oard\x18\x02 \x03(\x05\x12\x16\n\x0e\x63urrent_player\x18\x03 \x01(\x05\x32\xe8\x01\n\tTicTacToe\x12O\n\x0c\x41ssignPlayer\x12\x1e.TicTacToe.AssignPlayerRequest\x1a\x1f.TicTacToe.AssignPlayerResponse\x12<\n\tUserInput\x12\x16.TicTacToe.MoveRequest\x1a\x17.TicTacToe.MoveResponse\x12L\n\x0b\x43heckWinner\x12\x1d.TicTacToe.CheckWinnerRequest\x1a\x1e.TicTacToe.CheckWinnerResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tic_tac_toe_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ASSIGNPLAYERREQUEST']._serialized_start=32
  _globals['_ASSIGNPLAYERREQUEST']._serialized_end=53
  _globals['_ASSIGNPLAYERRESPONSE']._serialized_start=55
  _globals['_ASSIGNPLAYERRESPONSE']._serialized_end=100
  _globals['_MOVEREQUEST']._serialized_start=102
  _globals['_MOVEREQUEST']._serialized_end=160
  _globals['_MOVERESPONSE']._serialized_start=162
  _globals['_MOVERESPONSE']._serialized_end=210
  _globals['_CHECKWINNERREQUEST']._serialized_start=212
  _globals['_CHECKWINNERREQUEST']._serialized_end=232
  _globals['_CHECKWINNERRESPONSE']._serialized_start=234
  _globals['_CHECKWINNERRESPONSE']._serialized_end=310
  _globals['_TICTACTOE']._serialized_start=313
  _globals['_TICTACTOE']._serialized_end=545
# @@protoc_insertion_point(module_scope)
