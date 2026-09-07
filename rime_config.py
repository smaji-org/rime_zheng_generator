#!/usr/bin/env python3

# rime_config.py
# -----------
# Copyright : (c) 2023 - 2026, smaji.org
# Copyright : (c) 2023 - 2026, ZAN DoYe <zandoye@gmail.com>
# Licence   : GPL2
#
# This file is a part of rime_zheng_generator.


header= ('''---
name: {}
version: "{}"
sort: by_weight
columns:
  - text
  - code
  - weight
  - stem
encoder:
  rules:
    - length_equal: 2
      formula: "AaAbBaBb"
    - length_equal: 3
      formula: "AaBaBbCaCb"
    - length_equal: 4
      formula: "AaBaCaDaDb"
    - length_in_range: [5, 10]
      formula: "AaBaCaDaEa"
...

''')

schema= ('''# Rime schema settings
# encoding: utf-8

schema:
  schema_id: {}
  name: "Smaji 鄭碼"
  version: "{}"
  author:
    - 發明人 郑易里教授
  description: |
    鄭碼
    碼表源自鄭碼發明人以及熱心用戶的貢獻
    敲 ` 鍵進入拼音反查
  dependencies:
    - pinyin_simp

switches:
  - name: ascii_mode
    reset: 0
    states: [ 中文, 西文 ]
  - name: full_shape
    states: [ 半角, 全角 ]

engine:
  processors:
    - ascii_composer
    - recognizer
    - key_binder
    - speller
    - punctuator
    - selector
    - navigator
    - express_editor
  segmentors:
    - ascii_segmentor
    - matcher
    - abc_segmentor
    - punct_segmentor
    - fallback_segmentor
  translators:
    - punct_translator
    - table_translator
    - reverse_lookup_translator

speller:
  delimiter: " '"
  max_code_length: 5

translator:
  dictionary: {}
  enable_sentence: true
  enable_encoder: true
  encode_commit_history: true
  max_phrase_length: 5

reverse_lookup:
  dictionary: pinyin_simp
  prefix: "`"
  tips: 〔拼音〕
  preedit_format:
    - xform/([nljqxy])v/$1ü/

punctuator:
  import_preset: default

key_binder:
  import_preset: default

recognizer:
  import_preset: default
  patterns:
    reverse_lookup: "`[a-z]*$"
''')
