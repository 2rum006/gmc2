import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))